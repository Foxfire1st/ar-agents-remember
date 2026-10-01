# mcp/src/agents_remember/models/knowledge/review_source_content.py

## Governing Overview

[models route overview](../overview.md)

## Purpose

The wire vocabulary of **one inventory entry opened into its actual content** (ICR-R03@v1). The
review's Source pane lists changes; this module is the shape of what one of those rows expands *into* —
both bound endpoints' content, the generation they were read at, the measurement that bounded the
path, and why the path was opened at all (`admission`).

It is a separate module from `models/knowledge/review.py` for two reasons the module's own docstring
states: it answers a different question (not "what did this task change" but "what exactly do these two
immutable objects hold at this path"), and its answer has to be able to carry a whole file's text — an
obligation the review payload deliberately does not take on, since a payload carrying every file's
bytes would be a document dump rather than a review.

Three prohibitions are **structural here, not notes a renderer is asked to remember**:

1. **A side's content is a state, never a blank.** `ReviewSourceSide.text` may be present exactly when
   that side's bytes were read *and* are renderable, so an added file has no empty before text, a
   binary file has no empty document, and a submodule pointer is not a zero-length file. A value that
   is not textual and carries text cannot be constructed at all.
2. **A truncated expansion says so.** `byte_length` is the exact size of the object the side holds and
   `truncated` is true exactly when the carried text is a bounded prefix of it, so "this is what the
   file says" and "this is the first part of what the file says" are different answers.
3. **The generation is stated.** Every expansion names the two tree object ids it was opened against
   and whether they are still the pair the leaf's review binds now, so content can never be read as
   belonging to a generation the caller did not ask about.

Nothing in this module selects, ranks, diffs or concludes: the text is the object's bytes as Git
reports them, and what the two sides mean to each other is the renderer's business.

## Code Commentary

### Logic

**`ReviewSourceSideState` is six facts rather than a text/no-text pair.** `present` (a regular file's
bytes, carried as text), `absent` (this endpoint holds no entry at this path at all — the before side
of an addition, the after side of a deletion), `binary` (bytes were read and cannot be carried as
text), `symlink` (the entry's content is a link target, not a document's bytes), `submodule` (the entry
records a pointer and no file bytes exist), and `unavailable` (the entry could not be read — a missing
object, a root that is not there, an entry kind this surface does not render — with the reason stated).
The comment above the literal records the distinction a reader must never conflate: `absent` is a
measured fact about the endpoint, `unavailable` is a measurement that was not made.

**`_TEXT_STATES` names the only two states that may carry text.** `("present", "symlink")` — a regular
file's bytes and a link's target. Every other state carries none, which is what makes a missing or
unrenderable side impossible to present as an empty document.

**`ReviewSourceSide` is one endpoint's content, or the exact state that says why there is none.** Its
validator (`_require_text_exactly_when_the_side_is_textual`) enforces the four rules that make the
state machine structural: a `present` side must carry text (a present side with no text is a blank that
reads like an empty file); only a textual state may carry text (an `absent`, `binary`, `submodule` or
`unavailable` side with text would present itself as a document the endpoint does not hold); only
carried text can be truncated (a side with no text has no bounded prefix to label); and an `absent`
side names no object (an object id there would read as an entry this endpoint does not have).
`object_id` is the object the side's address resolves to at its tree — a blob id for a file or a
symlink, and the recorded *commit* for a submodule entry — so a reader has the identity even when the
bytes are not carried.

**`ReviewSourceExpansion` is the value the packet requires an entry to expand into.**
`before_code_tree_id`/`after_code_tree_id` are the **requested** generation — the two object ids the
caller carried in from the listing it is reading, echoed back — so the content is never silently
re-read from a newer generation. `currentness` states whether that generation is still the pair the
leaf's review binds, and `currentness_detail` says what that means for the bytes beside it.

**`path_bound` states which measurement admitted the path, because two can and only one of them is the
requested generation's.** `requested_generation` when the requested pair's own change set listed the
path; `leaf_change_set` when that measurement could not be made and the change set this leaf's review
actually publishes bounded the request instead. The second is **not a wider read** — the path is still
a changed path of a measured pair — and it is stated rather than implied, so a reader can always tell
which change set the row came from. `path_bound_detail` carries the admitting measurement's own words.

**`admission` states why the path was opened, so a renderer never infers it.** `changed` is a path a
measured change set lists; `attributed_unchanged` is a path the requested pair's measured change set
does **not** list, opened only because a realization recorded in the bound comparison's own knowledge
is anchored at it (260921-ICR-L43, under the 2026-09-28 admission ruling). `status` widens to
`ReviewSourceExpansionStatus` — the inventory's `ReviewFileStatus` plus `unchanged` — for expansions
only; the inventory vocabulary is untouched. `unchanged` is a measurement (the pair was compared and
does not differ here) and stays apart from `unknown` (no comparison was made).
`_require_attributed_context_to_be_a_measured_unchanged_path` makes two misstatements
unconstructible: `attributed_unchanged` exactly when `status == "unchanged"`, and an attributed path
bounded by anything other than `requested_generation`.

**`command` is evidence beside the content and never a substitute for it.** It is the exact
reproduction of the two reads, naming both trees and the path, so a reader can obtain the same bytes
without this surface; a reference with no text is the failure this vocabulary exists to make
unrepresentable.

**`ReviewSourceContentRequest` carries the two tree ids as caller input rather than something the
server resolves.** They are the ids the caller read out of the inventory it is looking at, and the
server checks them against the pair it binds. That is what makes "the entry I selected" and "the
generation I expand" the same generation **by construction** instead of by timing.

**`ReviewSourceContentResult` mirrors `KnowledgeReviewResult`'s shape on purpose, and enforces it.** It
is either `content` with an expansion and no refusal, or `refused` with a refusal and no expansion;
`_require_one_outcome` refuses both mixed values, so a caller that received a refusal has no content
and cannot read the absence of content as an empty file. `operation` is the fixed
`"read_review_source_content"`, which is how one response says which read produced it.

### Conventions

`__all__` publishes nine wire names: the request, the result, the expansion, the side, the side-state
literal, and the currentness, path-bound, admission and expansion-status aliases. The module
imports only what it extends: `KnowledgeModel` and the four length ceilings from
`models/knowledge/base.py` (`PROSE_MAX_LENGTH`, `LABEL_MAX_LENGTH`, `REFERENCE_MAX_LENGTH`,
`PATH_MAX_LENGTH`), and `ReviewFileStatus`/`ReviewRefusal` from `models/knowledge/review.py` — the
expansion carries the inventory's own status vocabulary and the review's own refusal shape rather than
declaring second ones. Every field is length-bounded at the type, and the three `model_validator`
methods are the only logic: this module computes nothing.

### Invariants And Boundaries

- **A non-textual side cannot carry text.** Enforced at construction, so no renderer can be handed an
  empty document standing in for a missing blob, a binary file, an absent endpoint or a submodule.
- **`absent` and `unavailable` are separate states with separate sentences.** One is a measurement of
  the endpoint, the other a measurement that was not made.
- **A truncation is labelled.** `truncated` is true exactly when the text is a bounded prefix, and
  `byte_length` is the exact object size beside it.
- **The generation is echoed, never re-derived.** The two tree ids on the value are the caller's own,
  and `currentness` is a statement about them rather than a substitution for them.
- **The bounding measurement and the admission are named.** `path_bound` is a closed two-value set
  with its detail, and `admission` (`changed` | `attributed_unchanged`) with its detail says why the
  path was opened; attributed context is always `unchanged` and always bounded by
  `requested_generation`, so unchanged context can never be presented as a change or vice versa.
- **One outcome per result.** A content result carries no refusal and a refused result carries no
  expansion; the two can never be mixed.
- **This module is vocabulary only.** It selects nothing, ranks nothing, reads nothing and writes
  nothing; the reader is `application/review_source_content.py` and the renderer is
  `dashboard/src/panels/review/SourceContent.tsx`.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

Every claim on this card is checkable in the shipped candidate: the module's own docstring and two
validators, the base vocabulary it extends, the read that fills these values in
`application/review_source_content.py`, the route and client that carry them, and the renderer that
decides from `state` rather than from text.

- **The module's own statement of why the vocabulary is separate from the review payload and of the three structural prohibitions it carries.** [1]
- The published surface: the request, the result, the expansion, the side, and the three closed literal sets. [2]
- **The six side states, with the comment that states why `absent` and `unavailable` must never be conflated.** [3]
- The only two states that may carry text, and the reason every other state carries none. [4]
- The three-value statement of whether the requested generation is still the pair the leaf binds, and the closed set naming which measurement admitted a path. [5]
- **Why a path was opened, and the expansion-only status that adds `unchanged` beside the inventory's vocabulary.** [6]
- **The four structural rules that make a side's content a state rather than a blank: text exactly when textual, no text otherwise, a truncation only on carried text, and no object on an absent side.** [7]
- **The expansion: the requested generation echoed back, the currentness statement, the bounding measurement and the admission with their own details, and the reproduction command beside the content.** [8]
- **Attributed context is exactly the `unchanged` expansion and is bounded only by the requested generation.** [9]
- The request that carries the task context, the path and the exact generation the caller read from the listing it is looking at. [10]
- **One outcome per result, enforced: a content result carries its expansion and no refusal, a refused result its refusal and no expansion.** [11]
- The base vocabulary this module extends rather than redeclares: the shared model base and the four length ceilings every field is bounded by. [12]
- The review vocabulary it re-uses rather than duplicating: the change status an expansion reports and the typed refusal a refused read carries. [13]
- **The read that fills these values in: the six states produced from real Git objects, the admission named on every expansion, and the generation statement measured after the bytes.** [14]
- The transport that accepts this request and serializes this result: the third review route, the selector value and the port type. [15]
- The client mirror of this vocabulary, which keeps an omitted field absent rather than defaulted. [16]
- **The renderer that decides from `state` and never from text: both-present draws the shipped diff, otherwise each textual side is drawn as content beside a note that no diff is claimed.** [17]
- **The cases that hold the vocabulary to its own prohibitions over real objects: each non-text kind, a stated bounded expansion, the requested generation served after the branch advanced, and the two admitted measurements.** [18]

### Cross-Repo References

No cross-repository behavior is implemented in this file. It declares value shapes for one repository
namespace's review and carries no identity that ranges beyond the repository the request names.

No meaningful cross-repo references found.
