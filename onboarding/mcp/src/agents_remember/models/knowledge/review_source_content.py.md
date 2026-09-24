# mcp/src/agents_remember/models/knowledge/review_source_content.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/knowledge/review_source_content.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-21T22:55:00+02:00 |
| lastVerifiedCommitHash | `63b476297708f779de8ed5c0bf3555b9d1de70c2` |
| lastVerifiedCommitDate | 2026-09-24T04:10:11+02:00|
| governingOverview | `mcp/src/agents_remember/models/overview.md` |

## Governing Overview

[models route overview](../overview.md)

## Purpose

The wire vocabulary of **one inventory entry opened into its actual content** (ICR-R03@v1). The
review's Source pane lists changes; this module is the shape of what one of those rows expands *into* —
both bound endpoints' content, the generation they were read at, and the measurement that admitted the
path.

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

`__all__` publishes exactly the seven wire names this vocabulary is: the request, the result, the
expansion, the side, the three closed literal sets and the currentness/path-bound aliases. The module
imports only what it extends: `KnowledgeModel` and the four length ceilings from
`models/knowledge/base.py` (`PROSE_MAX_LENGTH`, `LABEL_MAX_LENGTH`, `REFERENCE_MAX_LENGTH`,
`PATH_MAX_LENGTH`), and `ReviewFileStatus`/`ReviewRefusal` from `models/knowledge/review.py` — the
expansion carries the inventory's own status vocabulary and the review's own refusal shape rather than
declaring second ones. Every field is length-bounded at the type, and the two `model_validator`
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
- **The admitting measurement is named.** `path_bound` is a closed two-value set and
  `path_bound_detail` says what that measurement was, so a path can never be read without saying which
  change set listed it.
- **One outcome per result.** A content result carries no refusal and a refused result carries no
  expansion; the two can never be mixed.
- **This module is vocabulary only.** It selects nothing, ranks nothing, reads nothing and writes
  nothing; the reader is `application/review_source_content.py` and the renderer is
  `dashboard/src/panels/review/SourceContent.tsx`.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Every claim on this card is checkable in the shipped candidate: the module's own docstring and two
validators, the base vocabulary it extends, the read that fills these values in
`application/review_source_content.py`, the route and client that carry them, and the renderer that
decides from `state` rather than from text.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The module's own statement of why the vocabulary is separate from the review payload and of the three structural prohibitions it carries.** | `ReviewSourceSide` | mcp/src/agents_remember/models/knowledge/review_source_content.py:1-23; mcp/src/agents_remember/models/knowledge/review_source_content.py:93-133 |
| The published surface: the request, the result, the expansion, the side, and the three closed literal sets. | `__all__`; `ReviewSourceExpansion`; `ReviewSourceContentRequest`; `ReviewSourceContentResult` | mcp/src/agents_remember/models/knowledge/review_source_content.py:43-51; mcp/src/agents_remember/models/knowledge/review_source_content.py:136-211 |
| **The six side states, with the comment that states why `absent` and `unavailable` must never be conflated.** | `ReviewSourceSideState` | mcp/src/agents_remember/models/knowledge/review_source_content.py:53-74 |
| The only two states that may carry text, and the reason every other state carries none. | `_TEXT_STATES` | mcp/src/agents_remember/models/knowledge/review_source_content.py:76-79 |
| The three-value statement of whether the requested generation is still the pair the leaf binds, and the closed set naming which measurement admitted a path. | `ReviewSourceCurrentness`; `ReviewSourcePathBound` | mcp/src/agents_remember/models/knowledge/review_source_content.py:81-90 |
| **The four structural rules that make a side's content a state rather than a blank: text exactly when textual, no text otherwise, a truncation only on carried text, and no object on an absent side.** | `_require_text_exactly_when_the_side_is_textual` | mcp/src/agents_remember/models/knowledge/review_source_content.py:93-133 |
| **The expansion: the requested generation echoed back, the currentness statement, the admitting measurement with its own detail, and the reproduction command beside the content.** | `ReviewSourceExpansion`; `path_bound_detail`; `command` | mcp/src/agents_remember/models/knowledge/review_source_content.py:136-171 |
| The request that carries the task context, the path and the exact generation the caller read from the listing it is looking at. | `ReviewSourceContentRequest`; `before_code_tree_id`; `after_code_tree_id` | mcp/src/agents_remember/models/knowledge/review_source_content.py:174-188 |
| **One outcome per result, enforced: a content result carries its expansion and no refusal, a refused result its refusal and no expansion.** | `ReviewSourceContentResult`; `_require_one_outcome`; `operation` | mcp/src/agents_remember/models/knowledge/review_source_content.py:191-211 |
| The base vocabulary this module extends rather than redeclares: the shared model base and the four length ceilings every field is bounded by. | `KnowledgeModel`; `PROSE_MAX_LENGTH`; `PATH_MAX_LENGTH`; `REFERENCE_MAX_LENGTH`; `LABEL_MAX_LENGTH` | mcp/src/agents_remember/models/knowledge/base.py:24-27; mcp/src/agents_remember/models/knowledge/base.py:34-40 |
| The review vocabulary it re-uses rather than duplicating: the change status an expansion reports and the typed refusal a refused read carries. | `ReviewFileStatus`; `ReviewRefusal` | mcp/src/agents_remember/models/knowledge/review.py:797-797; mcp/src/agents_remember/models/knowledge/review.py:403-415 |
| **The read that fills these values in: the six states produced from real Git objects, the admission named on every expansion, and the generation statement measured after the bytes.** | `read_review_source_content`; `_side_content`; `_admit`; `_currentness` | mcp/src/agents_remember/application/review_source_content.py:110-131; mcp/src/agents_remember/application/review_source_content.py:473-492; mcp/src/agents_remember/application/review_source_content.py:293-337; mcp/src/agents_remember/application/review_source_content.py:415-451 |
| The transport that accepts this request and serializes this result: the third review route, the selector value and the port type. | `KNOWLEDGE_REVIEW_SOURCE_CONTENT_ROUTE`; `SourceContentRef`; `ReviewSourceContentPort` |mcp/src/agents_remember/serving/review.py:110-110; mcp/src/agents_remember/serving/review.py:191-208; mcp/src/agents_remember/serving/review.py:96-96|
| The client mirror of this vocabulary, which keeps an omitted field absent rather than defaulted. | `ReviewSourceSide`; `ReviewSourceExpansion`; `ReviewSourceContentResult` | dashboard/src/data/review.ts:328-335; dashboard/src/data/review.ts:346-361; dashboard/src/data/review.ts:363-369; dashboard/src/data/review.ts:430-430 |
| **The renderer that decides from `state` and never from text: both-present draws the shipped diff, otherwise each textual side is drawn as content beside a note that no diff is claimed.** | `Sides`; `sideLine`; `boundedNote`; `refusalBlock` | dashboard/src/panels/review/SourceContent.tsx:49-66; dashboard/src/panels/review/SourceContent.tsx:76-112; dashboard/src/panels/review/SourceContent.tsx:131-142; dashboard/src/panels/review/SourceContent.tsx:143-155 |
| **The cases that hold the vocabulary to its own prohibitions over real objects: each non-text kind, a stated bounded expansion, the requested generation served after the branch advanced, and the two admitted measurements.** | `test_a_binary_entry_states_its_kind_identity_and_size_with_no_text`; `test_a_symlink_entry_carries_the_link_target_and_never_a_document`; `test_a_submodule_entry_reports_the_recorded_pointer_and_no_file_bytes`; `test_oversized_content_is_a_stated_bounded_expansion`; `test_the_expansion_stays_bound_when_the_branch_advances_after_the_listing` | mcp/tests/test_knowledge_review_source_content.py:384-402; mcp/tests/test_knowledge_review_source_content.py:403-419; mcp/tests/test_knowledge_review_source_content.py:420-438; mcp/tests/test_knowledge_review_source_content.py:473-494; mcp/tests/test_knowledge_review_source_content.py:495-559 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. It declares value shapes for one repository
namespace's review and carries no identity that ranges beyond the repository the request names.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-24T00:43:00+02:00 — 260921-ICR-L24 curator (memory worktree only; no code changed; no commits; leaf base `5f14fc6790cafc3ad2ae612c2e67f176392dc1fe` plus the working-tree delta): **four enforced citation rows re-cited to the constructs they name, wording unchanged.** The dashboard delta moved every construct these rows cite: the client mirror's three interfaces now sit at `data/review.ts:328-335` (`ReviewSourceSide`), `:346-361` (`ReviewSourceExpansion`) and `:363-369` (`ReviewSourceContentResult`), and the renderer's two helpers at `SourceContent.tsx:131-142` (`boundedNote`) and `:143-155` (`refusalBlock`), because `Sides` gained the `mode`/`collapse` props this leaf threads through. Each row's contributing ranges (`SourceContent` `164-222`/`Sides` `76-112`/`sideLine` `49-66`, and the fourth client range) are kept verbatim, and no claim was reworded or dropped. **Stamp accounting:** no verification stamp was advanced — the candidate is uncommitted (base `5f14fc6790cafc3ad2ae612c2e67f176392dc1fe` plus the working-tree delta) and governed closeout owns the real stamp.
- 2026-09-23T00:45:00+02:00 — 260921-ICR-L10 curator: **removed a verification metadata row for a field that does not exist.** The developer ruled that field out on 2026-09-22 — it has no purpose and had spread by copy-paste — and this pass deleted it here and reworded the sentences that referred to it. The fact it carried (this card describes an uncommitted candidate whose base the verification pair names) is stated in the history entries around it. No content impact: no claim about the source changed.
- 2026-09-22T09:20:00+02:00 — 260921-ICR-L4 curator (gate repair pass on the merged line): **one enforced row re-cited.** The reused-vocabulary row cited `models/knowledge/review.py:500-500`/`791-803`, which the six-counts and partition growth moved; it now cites the declarations at `:513-513`/`812-824`. Wording unchanged; no stamp advanced.
- 2026-09-21T22:55+02:00 — 260921-ICR-L3 curator (same uncommitted change set on `ar/260921-icr-l3`, base `d80a0513e928ef29a973527d09597c82c96fde87`): **citation-range repair that clears a `claim_reopen` without any commit.** The finding was not a provenance problem: this leaf's new construct resolves exactly once in the working tree, but its **declaration line** fell outside the range the row cited, so the gate could not see the pointer landing on the new content. The row now cites the declaration beside the statement it already cited (the statement and the construct are one evidence unit, so both ranges belong on the row), and the claim's wording is unchanged because it was already true. Nothing was deleted, weakened, invented or re-stamped.

- 2026-09-21T22:55+02:00 — 260921-ICR-L3 curator (same uncommitted change set on `ar/260921-icr-l3`, base `d80a0513e928ef29a973527d09597c82c96fde87`): **citation-range repair that clears a `claim_reopen` without any commit.** The finding was not a provenance problem: this leaf's new construct resolves exactly once in the working tree, but its **declaration line** fell outside the range the row cited, so the gate could not see the pointer landing on the new content. The row now cites the declaration beside the statement it already cited (the statement and the construct are one evidence unit, so both ranges belong on the row), and the claim's wording is unchanged because it was already true. Nothing was deleted, weakened, invented or re-stamped.

- 2026-09-21T22:50:00+02:00 — 260921-ICR-L3 curator (uncommitted change set on `ar/260921-icr-l3`, base `d80a0513e928ef29a973527d09597c82c96fde87`): created this one-to-one card for the vocabulary module this leaf introduced as the shape of **one inventory entry opened into its actual content** (ICR-R03@v1). The card records why the vocabulary is separate from `models/knowledge/review.py` — it answers a different question and it has to carry a whole file's text, which the review payload deliberately does not — and the three prohibitions that are structural rather than renderer conventions: a side's content is a **state** and `text` exists exactly when that side's bytes were read and are renderable (so an added file has no empty before text, a binary file no empty document, and a submodule pointer is not a zero-length file); a truncated expansion **says so** through `byte_length` plus `truncated`; and every expansion **states the generation** it was opened against together with `currentness`, so content cannot be read as belonging to a generation the caller did not ask about. It also records the two admitted measurements named by `path_bound` — the requested generation's own change set, or, only when that measurement is unavailable, the change set this leaf's review publishes — and that the result type enforces one outcome per answer so a refusal can never be read as an empty file. **Stamp accounting:** this card exists only in this leaf's uncommitted candidate, so the two verification rows name the **production line this card was read against** — `d80a0513…`, the master line at this leaf's base, committed `2026-09-21T19:51:20+02:00` — and not a commit that contains the module; what was actually read is this leaf's uncommitted working tree, and the governed closeout owns the real stamp once the code commit exists. No verification stamp was advanced onto uncommitted bytes. (Post-write repair, same pass: the `## Governing Overview` link was written as `overview.md`, which resolves card-relative to nothing because `models/knowledge/` has no route overview of its own — the models overview lives one level up; it is now `../overview.md`, and `integrity.governing_overview_resolution` reports the card clean.)
