# mcp/src/agents_remember/application/review_source_content.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/review_source_content.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T04:01:40+02:00 |
| lastVerifiedCommitHash | `8a2d4b478971bf40cca0f24d5e5d24a0844bd563` |
| lastVerifiedCommitDate | 2026-09-30T04:16:14+02:00|
| governingOverview | `mcp/src/agents_remember/application/overview.md` |

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

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Every claim on this card is checkable in the shipped candidate: this module's own docstring and
functions, the vocabulary it fills in `models/knowledge/review_source_content.py`, the inventory and
resolution owners it delegates to, the transport route that reaches it through a port, and the cases
that measure it against real repositories.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The module's own statement of the three properties it exists for — the generation is an input, every side states its own truth, and which paths are addressable is decided by the admission owner (inventory entries and recorded-realization context) — and of what it deliberately does not own (no diff, no re-measurement, no admission policy).** | "does not decide which paths are addressable" | mcp/src/agents_remember/application/review_source_content.py:1-28 |
| The published surface: the expansion's text bound, the operation's own reference, and the one entry point. | `__all__`; `SOURCE_CONTENT_REFERENCE` | mcp/src/agents_remember/application/review_source_content.py:62-66; mcp/src/agents_remember/application/review_source_content.py:70-70 |
| The bound one side may carry — the same 2 MiB the shipped file reader applies — and the window Git itself inspects before this surface classifies a blob. | `EXPANSION_TEXT_BYTES`; `_BINARY_SNIFF_BYTES` | mcp/src/agents_remember/application/review_source_content.py:75-75; mcp/src/agents_remember/application/review_source_content.py:79-79 |
| The entry modes the content read interprets for itself, and the states whose object is a blob printable from its recorded identity. | `_SUBMODULE_MODE`; `_SYMLINK_MODE`; `_BLOB_STATES` | mcp/src/agents_remember/application/review_source_content.py:84-85; mcp/src/agents_remember/application/review_source_content.py:89-89 |
| The four stated sentences a side can carry: no entry here, a link target rather than a document, a target that is not valid text, and a submodule pointer with no bytes of its own. | `_ABSENT_DETAIL`; `_SYMLINK_DETAIL`; `_SYMLINK_UNTEXTUAL_DETAIL`; `_SUBMODULE_DETAIL` | mcp/src/agents_remember/application/review_source_content.py:91-107 |
| **The one entry point: resolve, screen, then read — with the currentness measurement taken after the bytes so it can only qualify them.** | `read_review_source_content` | mcp/src/agents_remember/application/review_source_content.py:110-131 |
| **The four admission facts, each a distinct refusal: a complete object identity, this leaf's recorded baseline, a *tree* as the after generation, and a path Git can be handed.** | `_inadmissible` | mcp/src/agents_remember/application/review_source_content.py:140-207 |
| **The after generation must be a tree: a commit, blob or tag this repository holds is refused by name, while a missing object stays a per-side measurement rather than a refusal.** | `_non_tree_generation` | mcp/src/agents_remember/application/review_source_content.py:210-238 |
| The expansion itself: the measured pair re-asked through the inventory owner, the admission asked of the admission owner, both sides read at the requested trees, and the value assembled with the generation and admission statements. | `_content` | mcp/src/agents_remember/application/review_source_content.py:241-285 |
| **The admission owner this module calls: a changed path of a measured change set, or an unchanged path a recorded realization of the same comparison links; the admission travels on the value.** | `admit_source_path`; `SourceAdmission` | mcp/src/agents_remember/application/review_source_admission.py:54-83; mcp/src/agents_remember/application/review_source_admission.py:86-128 |
| The refusals that keep the read confined, now in the admission owner: an unmeasured pair with no admitting change set, a measured pair whose recorded knowledge does not link the path, and a link that could not be determined. | `_unconfined`; `_not_listed`; `_link_undetermined` | mcp/src/agents_remember/application/review_source_admission.py:160-191; mcp/src/agents_remember/application/review_source_admission.py:194-213; mcp/src/agents_remember/application/review_source_admission.py:216-240 |
| The status of an admitted path — the entry's own, `unchanged` for attributed context, and `unknown` when the pair's change set was not measured, rather than a status guessed from the bytes that happen to be there. | `SourceAdmission`; `_entry_for` | mcp/src/agents_remember/application/review_source_admission.py:54-83; mcp/src/agents_remember/application/review_source_admission.py:243-249 |
| **Whether the requested generation is still the pair the leaf binds: the shipped recheck, and the three statements — current, superseded, unmeasured — that each end by saying the content is the requested generation's and no newer one.** | `_currentness` | mcp/src/agents_remember/application/review_source_content.py:288-324 |
| **One endpoint's content, with the three outcomes kept apart: an unbound root and an unanswered lookup are `unavailable`, an answered lookup with no entry is `absent`, and only a real entry is read.** | `_side_content`; `_Unreadable` | mcp/src/agents_remember/application/review_source_content.py:339-343; mcp/src/agents_remember/application/review_source_content.py:346-365 |
| **The entry's kind decides before its bytes do: a tree is not source, a gitlink is a recorded pointer with no bytes, a symlink mode is a link target, and everything else is a regular file.** | `_entry_content`; `_TreeEntry` | mcp/src/agents_remember/application/review_source_content.py:330-336; mcp/src/agents_remember/application/review_source_content.py:368-390 |
| A regular file's bytes as text or as the stated reason they cannot be carried as text, and a symlink's target as content when it has a lossless spelling. | `_blob_content`; `_symlink_content` | mcp/src/agents_remember/application/review_source_content.py:393-412; mcp/src/agents_remember/application/review_source_content.py:415-434 |
| **The two reasons no text form exists — a NUL inside Git's own sniff window, and bytes that are not valid UTF-8 — and the bounded decode that carries a prefix rather than the whole object.** | `_decoded`; `_binary_detail`; `_text_detail` | mcp/src/agents_remember/application/review_source_content.py:437-451; mcp/src/agents_remember/application/review_source_content.py:454-467; mcp/src/agents_remember/application/review_source_content.py:470-479 |
| **One path's entry in one tree, asked with a literal pathspec so a measured name is an address and not a pattern, and checked against the path that was asked about.** | `_tree_entry`; `_parsed_record` | mcp/src/agents_remember/application/review_source_content.py:491-515; mcp/src/agents_remember/application/review_source_content.py:518-531 |
| The byte-exact blob read through the kernel's own reader, so a file's content is never normalized on its way to a reader. | `_blob_bytes` | mcp/src/agents_remember/application/review_source_content.py:534-544 |
| **The reproduction line: the exact `ls-tree`/`cat-file` commands that obtain the same bytes, naming every object the answer rests on.** | `_reproduction`; `_side_command`; `_quoted` | mcp/src/agents_remember/application/review_source_content.py:550-562; mcp/src/agents_remember/application/review_source_content.py:565-574; mcp/src/agents_remember/application/review_source_content.py:577-582 |
| The second of the two path checks: the spellings Git could not have reported are refused before any argv is built, with the offending input bounded by the admission owner's helper. | `_addressable`; `bounded_input` | mcp/src/agents_remember/application/review_source_content.py:585-596; mcp/src/agents_remember/application/review_source_admission.py:252-259 |
| **The wire vocabulary this module fills: six side states, the closed currentness set, the two bounding measurements, the two admissions, and the structural prohibitions that make a non-textual side carrying text unrepresentable.** | `ReviewSourceSide`; `ReviewSourceSideState`; `ReviewSourceCurrentness`; `ReviewSourcePathBound`; `ReviewSourceAdmission` | mcp/src/agents_remember/models/knowledge/review_source_content.py:69-76; mcp/src/agents_remember/models/knowledge/review_source_content.py:86-86; mcp/src/agents_remember/models/knowledge/review_source_content.py:95-95; mcp/src/agents_remember/models/knowledge/review_source_content.py:102-102; mcp/src/agents_remember/models/knowledge/review_source_content.py:110-150 |
| The expansion value: the requested generation echoed back, the currentness statement, the bounding measurement, the admission, and the command beside the content. | `ReviewSourceExpansion` | mcp/src/agents_remember/models/knowledge/review_source_content.py:153-214 |
| The request that carries the task context, the path and the exact generation, and the result that is either the expansion or one typed refusal and never both. | `ReviewSourceContentRequest`; `ReviewSourceContentResult` | mcp/src/agents_remember/models/knowledge/review_source_content.py:217-231; mcp/src/agents_remember/models/knowledge/review_source_content.py:234-254 |
| **The one measurement this module calls instead of re-deriving: the change inventory of a bound tree pair, and the side value that binds a tree id to the root it resolves in.** | `review_inventory`; `source_tree_side` | mcp/src/agents_remember/application/review_source_inventory.py:429-469; mcp/src/agents_remember/application/review_source_inventory.py:168-176 |
| The resolution this module re-uses to bind the leaf, and the shipped recheck it calls for currentness rather than inventing a second capture. | `resolve_review_candidate`; `require_current_candidate_identity` |mcp/src/agents_remember/application/review_candidate_resolution.py:180-286; mcp/src/agents_remember/application/review_candidate_resolution.py:308-341|
| **The transport that reaches this owner: the third route, its selector value, its unwired answer and its incomplete-generation body.** | `KNOWLEDGE_REVIEW_SOURCE_CONTENT_ROUTE`; `SourceContentRef`; `source_content_request_from_query`; `_source_content_response`; `_incomplete_generation` |mcp/src/agents_remember/serving/review.py:199-216; mcp/src/agents_remember/serving/review.py:584-604; mcp/src/agents_remember/serving/review.py:741-757; mcp/src/agents_remember/serving/review.py:635-653; mcp/src/agents_remember/serving/review.py:96-96; mcp/src/agents_remember/serving/review.py:720-738|
| The third port the composition root supplies, and the wiring that gives it the real owner. | `review_source_content`; `review_source_content_port` | mcp/src/agents_remember/serving/_app_common.py:483-483; mcp/src/agents_remember/cli/dashboard.py:120-130 |
| The refusal code this read publishes, added to the review vocabulary without changing how an unknown code maps. | `source_content_unresolved` | mcp/src/agents_remember/models/knowledge/review.py:159-160 |
| **The production-composition cases: both endpoints' own bytes against an independent `git show`, an unmapped addition's whole text, a deletion's whole base text, every non-text kind, a stated bounded expansion, generation binding across a branch advance, the pruned-blob and missing-object states, the unmeasured-generation confinement, a commit id refused, and the unwired process refused by name.** | `test_a_modified_file_opens_both_endpoints_own_bytes`; `test_an_added_unmapped_file_opens_its_entire_candidate_text`; `test_the_expansion_stays_bound_when_the_branch_advances_after_the_listing`; `test_an_unmeasured_generation_still_confines_the_path_to_a_measured_change_set`; `test_a_generation_that_names_a_commit_is_refused_rather_than_served`; `test_an_unwired_process_refuses_the_route_by_name` | mcp/tests/test_knowledge_review_source_content.py:269-311; mcp/tests/test_knowledge_review_source_content.py:314-334; mcp/tests/test_knowledge_review_source_content.py:495-557; mcp/tests/test_knowledge_review_source_content.py:641-676; mcp/tests/test_knowledge_review_source_content.py:679-719; mcp/tests/test_knowledge_review_source_content.py:798-821 |
| **The attributed-unchanged cases: admission without counting, cross-comparison refusal, historical bytes after the tree moves, exact spelling, and undetermined refusal.** | `test_an_unchanged_path_a_recorded_realization_links_opens_as_context_without_counting`; `test_a_path_linked_only_in_another_comparison_is_refused_for_this_one`; `test_after_the_live_tree_moves_the_listed_pair_keeps_its_exact_attributed_bytes`; `test_a_padded_spelling_is_never_admitted_as_attributed_context`; `test_an_unreadable_snapshot_leaves_the_link_undetermined_rather_than_absent` | mcp/tests/test_knowledge_review_attributed_source_content.py:117-150; mcp/tests/test_knowledge_review_attributed_source_content.py:167-197; mcp/tests/test_knowledge_review_attributed_source_content.py:200-247; mcp/tests/test_knowledge_review_attributed_source_content.py:272-296; mcp/tests/test_knowledge_review_attributed_source_content.py:326-350 |
| The renderer that consumes this value: the shipped `DiffPane` when both sides are text, each side's own state line and content otherwise, the refusal block, and the generation/path-bound statements. | `SourceContent`; `Sides`; `refusalBlock` | dashboard/src/panels/review/SourceContent.tsx:113-125; dashboard/src/panels/review/SourceContent.tsx:222-271; dashboard/src/panels/review/SourceContent.tsx:55-99 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. It reads one repository namespace's Git
objects at task-context-resolved roots and carries no identity that ranges beyond the repository the
request names.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-30T04:01:40+02:00 — 260928-MIK-L25 curator (uncommitted change set on `ar/260928-mik-l25`, code base `3eb034a6ab0493a51da5dcd6d013aa6f27f39496` plus the staged delta): No content impact: this card's source is unchanged. Rows citing lines that MIK-R25 moved in `review_candidate_resolution.py`, `dashboard.py`, `_app_common.py` were re-pointed, by the installed fixer (its generated bullets are kept, since no claim was reworded) or by the exact base-to-staged line shift for the rows it declined; each such row was byte-identical to memory HEAD. No verification stamp was advanced.
- 2026-09-28T17:29:54+02:00 — 260921-ICR-L47 curator (uncommitted candidate tree `72efa4bbc169b16afe8ef249499edf79cad9940d` over code base `58e22246cc09ef0ee12095e284a111a475081c38`): No content impact: citations into `mcp/src/agents_remember/cli/dashboard.py` (and `serving/_app_common.py`) displaced by L47's fourth-port wiring were re-cited to the declarations that hold their anchors now (whole-identifier match); claim wording unchanged. No stamp advanced.
- 2026-09-28T12:38:10+02:00 — 260921-ICR-L43 curator (uncommitted candidate tree `990a5c1a3afab15d04881475b2501ed98cddf908` over code base `a0b2c18d2b8d08ac1242a13f65bde900a190df7a`): **the admission policy moved out, and the admitted population was extended (supersedes the L3 statement "the one addressable population is the inventory's own entries").** `_Admission`, `_admit`, `_unconfined`, `_not_listed`, `_status`, `_entry_for` and `_input` moved to `application/review_source_admission.py` (733 → 596 lines here); this module now calls `admit_source_path` and copies `admission`/`admission_detail` onto the expansion. Under the 2026-09-28 developer ruling the admission owner also opens an unchanged path a realization recorded in the bound comparison's knowledge links, as `attributed_unchanged`/`unchanged`; every other unchanged path is still refused and changed-path answers are byte-identical to base (R2 differential). Purpose, Logic, Conventions, Invariants and the moved reference rows were rewritten; every range was re-derived from the candidate. No stamp advanced; closeout owns it.
- 2026-09-26T20:57:44Z — Reconciled current source-owner citations and exact declarations; superseded wording is corrected in the affected reference rows.
- 2026-09-24T00:43:00+02:00 — 260921-ICR-L24 curator (memory worktree only; no code changed; no commits; leaf base `5f14fc6790cafc3ad2ae612c2e67f176392dc1fe` plus the working-tree delta): **one enforced citation row re-cited to the construct it names, wording unchanged.** The row citing the renderer's refusal block pointed at `SourceContent.tsx:126-138`, which this leaf's growth of `Sides` (the `mode`/`collapse` props) left holding `boundedNote` instead: `refusalBlock` now occupies `143-155`, and that is the range the row carries. The claim's words are untouched and the row's two contributing ranges (`SourceContent` `164-222`, `Sides` `76-112`) are kept verbatim; nothing was deleted or reworded. **Stamp accounting:** no verification stamp was advanced — the candidate is uncommitted (base `5f14fc6790cafc3ad2ae612c2e67f176392dc1fe` plus the working-tree delta) and governed closeout owns the real stamp.
- 2026-09-23T00:45:00+02:00 — 260921-ICR-L10 curator: **removed a verification metadata row for a field that does not exist.** The developer ruled that field out on 2026-09-22 — it has no purpose and had spread by copy-paste — and this pass deleted it here and reworded the sentences that referred to it. The fact it carried (this card describes an uncommitted candidate whose base the verification pair names) is stated in the history entries around it. No content impact: no claim about the source changed.
- 2026-09-21T22:55+02:00 — 260921-ICR-L3 curator (same uncommitted change set on `ar/260921-icr-l3`, base `d80a0513e928ef29a973527d09597c82c96fde87`): **citation-range repair that clears a `claim_reopen` without any commit.** The finding was not a provenance problem: this leaf's new construct resolves exactly once in the working tree, but its **declaration line** fell outside the range the row cited, so the gate could not see the pointer landing on the new content. The row now cites the declaration beside the statement it already cited (the statement and the construct are one evidence unit, so both ranges belong on the row), and the claim's wording is unchanged because it was already true. Nothing was deleted, weakened, invented or re-stamped.

- 2026-09-21T22:45:00+02:00 — 260921-ICR-L3 curator (uncommitted change set on `ar/260921-icr-l3`, base `d80a0513e928ef29a973527d09597c82c96fde87`): created this one-to-one card for the module this leaf introduced as the review surface's one owner of **one inventory entry's actual content at its two bound code trees** (ICR-R03@v1). The card records what the module is for rather than only where the code lives: the generation is an *input* — the two tree ids the listing published are echoed back by the request and used to address the bytes, and the leaf's review is re-resolved only to state `currentness`, so a working tree, `HEAD` or a newer candidate is never substituted; a side is one of six states and `absent` (measured, holds nothing) stays apart from `unavailable` (a measurement that was not made); a path is admitted only by a **measured** change set — the requested generation's own, or, when that measurement is unavailable, the one this leaf's review publishes, with `path_bound`/`path_bound_detail` naming which — and a path in neither is refused in every state, which is what keeps this a change-set read rather than a general file reader over the recorded base; and the after generation must be a *tree*, so a commit, blob or tag this repository holds is refused by name while a missing object stays a per-side measurement. It also records the two details a reader of the read needs: `ls-tree` is asked with a `:(literal)` pathspec because a measured pathname is an address and not a pattern, and text is carried to 2 MiB with the object's exact size and a stated bound rather than truncated silently. **Stamp accounting:** this card exists only in this leaf's uncommitted candidate, so the two verification rows name the **production line this card was read against** — `d80a0513…`, the master line at this leaf's base, committed `2026-09-21T19:51:20+02:00` — and not a commit that contains the module; what was actually read is this leaf's uncommitted working tree, and the governed closeout owns the real stamp once the code commit exists. No verification stamp was advanced onto uncommitted bytes.
