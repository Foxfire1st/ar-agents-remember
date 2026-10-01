# mcp/src/agents_remember/application/review_source_content.py

## Governing Overview

[application route overview](overview.md)

## Purpose

The one owner of the question a reviewer asks *after* the review has listed what a task changed:
**what does each of the two bound objects actually hold at this path**. The review's Source pane lists
changes; this module is what one of those rows opens into, and it answers from the two tree ids the
listing published and from nothing else.

Three properties are the reason the module exists rather than living inside the review adapter:

1. **The generation is an input, not a lookup.** The two tree object ids arrive with the request, are
   read back from the inventory the caller is looking at, and are used to address the content. The
   leaf's review is re-resolved only to *measure* whether those ids are still the pair it binds, and
   that measurement travels as `currentness`. A newer candidate is never silently substituted for the
   requested generation, and a working tree, `HEAD` or a branch is never a source of bytes.
2. **Every side states its own truth.** A side is `present` (a regular file's text), `absent` (this
   endpoint holds no entry at this path), `binary`, `symlink` (the content is a link target),
   `submodule` (a recorded pointer with no file bytes at all) or `unavailable` (the entry could not be
   read, with the reason). `absent` and `unavailable` stay apart: one is a measured fact about the
   endpoint, the other a measurement that was not made.
3. **The path is admitted by a measurement or a recorded realization of the same comparison, never by
   the caller — and not by this module.** Since 260921-ICR-L43 the admission policy lives in
   `application/review_source_admission.py`, which admits exactly two populations: a path a measured
   change set lists (the requested generation's own, or — when that pair cannot be measured — the
   change set this leaf's review publishes), and an unchanged path that a realization recorded in the
   bound comparison's own knowledge is anchored at. Every other path is refused by name. That is what
   keeps this route a comparison-bound read rather than a general file reader over the recorded base.

**Why it is a module and not a function in the adapter.** The adapter (`application/knowledge_review.py`)
did not own this responsibility — the review payload never carried a file's text — so nothing had to
move out of it, and the extraction is the same sibling-module shape the master line has used for the
review's other new responsibilities. The adapter is 831 lines before and after this leaf.

## Code Commentary

### Logic

**`read_review_source_content` resolves, screens, and only then reads.** The task context is resolved
first through `resolve_review_candidate`; a refusal there is returned as `ReviewSourceContentResult`
with `state="refused"` and no content. The four admission facts are checked next, before any object is
read, and the bytes are read last. The order is the packet's: an inadmissible expansion is answered by
name, and the leaf's current candidate is measured *afterwards* so the answer can say whether the
caller is reading the candidate's own source or a superseded generation's.

**`_inadmissible` answers four distinct refusals, all `source_content_unresolved`.** (a) Both ids must
be complete Git object identities — `require_git_object_id` refuses an abbreviation, a branch name and
a symbolic revision, because none of them addresses one exact generation. (b) The baseline must be the
recorded base of *this* leaf's review: the comparison is the one the enclosure contract records, and a
different baseline belongs to a comparison this review did not make. (c) The after generation must
name a **tree** (`_non_tree_generation`). (d) The path must be a repository-relative spelling this
surface will hand to Git (`_addressable`), which refuses an empty name, a NUL, an absolute path and a
`..` segment before any argv is built.

**`_non_tree_generation` refuses a commit, a blob and a tag by name — and deliberately not a missing
object.** `after_code_tree_id` is documented as a tree id and the review binds trees, so an object this
repository holds that is not a tree is refused rather than peeled into one or served as the generation
the listing published; the reachable case is a `HEAD` commit id, which `git diff` and `ls-tree` both
accept. An object the repository does **not** hold is not a refusal: a missing object is a measurement
this read reports on the side it affects (`unavailable`, with its reason), and refusing would hide the
readable side of a comparison that is otherwise inspectable.

**`_content` delegates the confinement to `admit_source_path` and reads only after an admission.** It
measures the requested pair through `review_inventory`, hands that inventory to
`application/review_source_admission.admit_source_path`, and returns the refusal unchanged when one
comes back. Only an admission reaches `_side_content`. The expansion's `status`, `mode_change`,
`path_bound`/`path_bound_detail` and `admission`/`admission_detail` are copied from the admission value,
so this module states the admission and never re-derives it: `changed` for a listed path (with the
entry's status, or `unknown` when the leaf change set bounded an unmeasured pair) and
`attributed_unchanged` with status `unchanged` for context a recorded realization of the same
comparison links. The byte reads are identical for both populations.

**`_currentness` re-uses the shipped recheck rather than inventing one.** `require_current_candidate_identity`
recomputes the candidate identity; a moved input yields `unmeasured` with the owner's own detail, and
otherwise the requested after tree is compared with `resolved.candidate_code_tree_id` for `current` or
`superseded`. All three statements say the same second thing: the content beside them is the *requested*
generation's, byte for byte, and a superseded read is not a read of the newer one.

**`_side_content` keeps three outcomes apart.** A root the resolution did not bind is `unavailable`; a
lookup that did not answer (`_Unreadable`) is `unavailable` with the reason; a lookup that answered with
no entry is **`absent`** — a measured fact about that endpoint, with its own sentence. Only then is
anything read, and the entry's *kind* decides before its bytes do (`_entry_content`): a tree object is
`unavailable` rather than a directory listing rendered as source, a gitlink is `submodule` carrying the
recorded commit as `object_id` and no bytes, a symlink mode reads the blob as its target
(`_symlink_content`), and everything else is a regular file's bytes.

**`_decoded` is where "cannot be carried as text" is decided, and the two reasons are stated
separately.** A NUL byte inside the first `_BINARY_SNIFF_BYTES` (Git's own window) is binary; bytes that
are simply not valid UTF-8 have no lossless spelling in this vocabulary and are reported as
unrenderable rather than re-encoded into a document this repository does not hold. Text is carried up to
`EXPANSION_TEXT_BYTES` (2 MiB, the same bound the shipped file reader applies), and `_text_detail` says
either "the complete content of this endpoint's N-byte object" or that the text above is the first
2 097 152 bytes of an N-byte object, cut on a character boundary — a bounded expansion that names its
own bound rather than a silent truncation.

**`_tree_entry` asks `ls-tree` with a literal pathspec and checks the answer against the path it asked
about.** `:(literal)<path>` is not decoration: without it a name beginning with `:` would be read as
pathspec magic and a name holding `*` or `[` could match a neighbour — measured on `git 2.54.0`, where
`ls-tree -- ':colon.py'` exits 0 and prints nothing. The returned record is parsed from the NUL-delimited
answer and its own name compared with the requested path, so a record for some *other* path is a failed
lookup rather than a silent substitution.

**`_reproduction` prints the exact commands that obtain the same bytes.** One line per side: the
`ls-tree -l` lookup, and — when the side's state is a blob state — `cat-file blob <oid>` for the exact
object the answer rests on; a submodule side prints `cat-file -t` for the recorded commit instead, and
a side with no object prints the lookup alone. `_quoted` adds shell quoting only when the name contains
whitespace. The command is evidence *beside* the content, never a substitute for it.

### Conventions

`__all__` publishes exactly three names — `EXPANSION_TEXT_BYTES`, `SOURCE_CONTENT_REFERENCE` and
`read_review_source_content` — leaving the state machine, the tree read and the admission helpers
private. `SOURCE_CONTENT_REFERENCE` is a statement of the operation and its measurement rather than a
cached artifact path, because a caller acts on it by reading the two object identities beside it. The
stated reasons are module-level constants (`_ABSENT_DETAIL`, `_SYMLINK_DETAIL`,
`_SYMLINK_UNTEXTUAL_DETAIL`, `_SUBMODULE_DETAIL`) because two callers and six states have to state the
same fact identically. `_TreeEntry` and `_Unreadable` are frozen dataclasses, not pydantic models: they
are the read's own intermediate values, and only the models in `models/knowledge/review_source_content.py`
are wire shapes. The admission value and the bounded-input helper (`bounded_input`, which this
module's four admission-fact refusals also use) belong to `application/review_source_admission.py`.
Nothing here writes a file, holds state, or selects a record.

### Invariants And Boundaries

- **The bytes come from the requested trees and nowhere else.** Every read is object-addressed
  (`ls-tree <tree>`, `read_git_blob_bytes(<oid>)`); the module contains no filesystem read of a
  working-tree path, so an entry opened after the branch advanced still shows the listed generation and
  says `superseded`.
- **A path is read only when the admission owner admits it.** A changed path of a measured change
  set, or an unchanged path a recorded realization of the same comparison links; both are stated on
  the answer (`path_bound`, `admission`) and neither widens the read to an arbitrary path. Attributed
  context is never an inventory entry and never counts as a changed file.
- **`absent` and `unavailable` are different facts.** One is the endpoint measured and holding nothing
  there; the other is a measurement that was not made, with the reason on the side it affects.
- **A non-textual state never carries text.** The rule is structural in
  `models/knowledge/review_source_content.py` (`ReviewSourceSide._require_text_exactly_when_the_side_is_textual`),
  so an empty document cannot stand in for a missing blob, a binary file or a submodule pointer.
- **A truncation is never silent.** `byte_length` is the object's exact size and `truncated` is true
  exactly when the carried text is a bounded prefix of it.
- **`path_bound` and `admission` are stated, not implied.** The answer always names which measurement
  bounded the path and why it was opened, so a renderer never infers "unchanged context" from the
  inventory.
- **Rank.** `serving` may not import `application`, so the route reaches this module through the
  `ReviewSourceContentPort` the composition root wires, and `_app_common.ServingCollaborators` carries
  the third review field.

### Todos

None recorded. A live-browser end-to-end scenario against a started server is not measured here (the
route is exercised through the real `TestClient` composition and the pane at the real `ReviewSurface`
with `fetch` stubbed); it is named as a boundary rather than a deferred implementation item.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

Every claim on this card is checkable in the shipped candidate: this module's own docstring and
functions, the vocabulary it fills in `models/knowledge/review_source_content.py`, the inventory and
resolution owners it delegates to, the transport route that reaches it through a port, and the cases
that measure it against real repositories.

- **The module's own statement of the three properties it exists for — the generation is an input, every side states its own truth, and which paths are addressable is decided by the admission owner (inventory entries and recorded-realization context) — and of what it deliberately does not own (no diff, no re-measurement, no admission policy).** [1]
- The published surface: the expansion's text bound, the operation's own reference, and the one entry point. [2]
- The bound one side may carry — the same 2 MiB the shipped file reader applies — and the window Git itself inspects before this surface classifies a blob. [3]
- The entry modes the content read interprets for itself, and the states whose object is a blob printable from its recorded identity. [4]
- The four stated sentences a side can carry: no entry here, a link target rather than a document, a target that is not valid text, and a submodule pointer with no bytes of its own. [5]
- **The one entry point: resolve, screen, then read — with the currentness measurement taken after the bytes so it can only qualify them.** [6]
- **The four admission facts, each a distinct refusal: a complete object identity, this leaf's recorded baseline, a *tree* as the after generation, and a path Git can be handed.** [7]
- **The after generation must be a tree: a commit, blob or tag this repository holds is refused by name, while a missing object stays a per-side measurement rather than a refusal.** [8]
- The expansion itself: the measured pair re-asked through the inventory owner, the admission asked of the admission owner, both sides read at the requested trees, and the value assembled with the generation and admission statements. [9]
- **The admission owner this module calls: a changed path of a measured change set, or an unchanged path a recorded realization of the same comparison links; the admission travels on the value.** [10]
- The refusals that keep the read confined, now in the admission owner: an unmeasured pair with no admitting change set, a measured pair whose recorded knowledge does not link the path, and a link that could not be determined. [11]
- The status of an admitted path — the entry's own, `unchanged` for attributed context, and `unknown` when the pair's change set was not measured, rather than a status guessed from the bytes that happen to be there. [12]
- **Whether the requested generation is still the pair the leaf binds: the shipped recheck, and the three statements — current, superseded, unmeasured — that each end by saying the content is the requested generation's and no newer one.** [13]
- **One endpoint's content, with the three outcomes kept apart: an unbound root and an unanswered lookup are `unavailable`, an answered lookup with no entry is `absent`, and only a real entry is read.** [14]
- **The entry's kind decides before its bytes do: a tree is not source, a gitlink is a recorded pointer with no bytes, a symlink mode is a link target, and everything else is a regular file.** [15]
- A regular file's bytes as text or as the stated reason they cannot be carried as text, and a symlink's target as content when it has a lossless spelling. [16]
- **The two reasons no text form exists — a NUL inside Git's own sniff window, and bytes that are not valid UTF-8 — and the bounded decode that carries a prefix rather than the whole object.** [17]
- **One path's entry in one tree, asked with a literal pathspec so a measured name is an address and not a pattern, and checked against the path that was asked about.** [18]
- The byte-exact blob read through the kernel's own reader, so a file's content is never normalized on its way to a reader. [19]
- **The reproduction line: the exact `ls-tree`/`cat-file` commands that obtain the same bytes, naming every object the answer rests on.** [20]
- The second of the two path checks: the spellings Git could not have reported are refused before any argv is built, with the offending input bounded by the admission owner's helper. [21]
- **The wire vocabulary this module fills: six side states, the closed currentness set, the two bounding measurements, the two admissions, and the structural prohibitions that make a non-textual side carrying text unrepresentable.** [22]
- The expansion value: the requested generation echoed back, the currentness statement, the bounding measurement, the admission, and the command beside the content. [23]
- The request that carries the task context, the path and the exact generation, and the result that is either the expansion or one typed refusal and never both. [24]
- **The one measurement this module calls instead of re-deriving: the change inventory of a bound tree pair, and the side value that binds a tree id to the root it resolves in.** [25]
- The resolution this module re-uses to bind the leaf, and the shipped recheck it calls for currentness rather than inventing a second capture. [26]
- **The transport that reaches this owner: the third route, its selector value, its unwired answer and its incomplete-generation body.** [27]
- The third port the composition root supplies, and the wiring that gives it the real owner. [28]
- The refusal code this read publishes, added to the review vocabulary without changing how an unknown code maps. [29]
- **The production-composition cases: both endpoints' own bytes against an independent `git show`, an unmapped addition's whole text, a deletion's whole base text, every non-text kind, a stated bounded expansion, generation binding across a branch advance, the pruned-blob and missing-object states, the unmeasured-generation confinement, a commit id refused, and the unwired process refused by name.** [30]
- **The attributed-unchanged cases: admission without counting, cross-comparison refusal, historical bytes after the tree moves, exact spelling, and undetermined refusal.** [31]
- The renderer that consumes this value: the shipped `DiffPane` when both sides are text, each side's own state line and content otherwise, the refusal block, and the generation/path-bound statements. [32]

### Cross-Repo References

No cross-repository behavior is implemented in this file. It reads one repository namespace's Git
objects at task-context-resolved roots and carries no identity that ranges beyond the repository the
request names.

No meaningful cross-repo references found.
