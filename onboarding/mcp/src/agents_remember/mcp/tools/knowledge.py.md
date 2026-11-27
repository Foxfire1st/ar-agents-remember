# mcp/src/agents_remember/mcp/tools/knowledge.py

## Governing Overview

[mcp/tools route overview](overview.md)

## Current source contract evidence




## Purpose

Payload builders for four mounted knowledge operations over converted trees: read, diff, integrity check and write. The writer route delegates response shaping to `write_answer`, which returns bounded notes, problems and violations with their truncation flags and the whole report path.

## Code Commentary

Cutover refusal helpers, worktree candidate capture and contract loading are imported at the operation branches that need them; existing legacy-format and root-selector refusals remain.

### Logic

Read selects the converted tree’s derived index, computes a rich page internally, then projects its rows, proofs and family references to text ID, kind, computed state and file/heading or line locations. Selection-time commit/dirtiness and a shared revalidated resolver bind sizing and projection to one epoch; a moved checkout refuses `snapshot_unavailable`. No record body is delivered by a naming projection: its rows carry names and derived state. The requested marks views and query views are the requirement-authorized top-level exceptions — `weakness` carries a weakness's own statement and measurement, `dependent` supports `folder` fallback and `compact=True` projection through `compact_dependent_rows`, and `QUERY_VIEWS` (`records`, `impact`, `search`) route through `_one_view` and `application/knowledge_queries.py::run_query_view` (with `records` delivering bounded batch full-text records). `ReadToolRequest` carries `repo_id`, `contract_path`, `files`, `folder`, `query`, `kinds`, `record_ids`, and `compact`. Source-resolution pairs remain complete or absent. [1]

Diff compares knowledge/onboarding Git files, privately captures the memory working tree when afterRevision is absent, and writes the whole selected comparison as a report before projecting the answer. `_reported_body` returns both compared trees, counts by kind, decision-ordered record names up to `TOOL_ANSWER_LIST_MAX`, their total `decisionRecordCount`, and the report location. The report holds patches and source/record groups; the mounted answer carries no comparison body, `diff`, `complete` or `leftOut`, and infers no semantic effect label. A report write failure refuses `report-unwritable`, retaining the actual cleanup/residual facts.

Integrity runs the knowledge validator and retains the latest leaf worklist for a contract in its
whole result, not a canonical detection run or compatibility verdict. Its delivered status
projection retains whole-report counts, bounded refusing-first violation entries and worklist
state, while the complete violation population remains in the logged detail. Legacy roots and
database files refuse before an open; change/project and selected-run fields are removed. [3] [56]

### Invariants And Boundaries

- A partial index is never complete.
- Unheld selectors refuse rather than implying no change.
- Each public payload uses the shared response-model choke point.

### Logic

`knowledge_read_payload` refuses a view outside its eleven admitted views — `source_context`, `invariant`, `family`, `record`, `records`, `impact`, `search`, `weakness`, `dependent`, `writers`, `consolidation_proposal` — through `_refused_read(view, repositoryId, "unknown_view", ...)` rather than picking a default view (dispatching `writers` and `consolidation_proposal` through `knowledge_views/record_views.py`) (`review_matrix` and `curation_queue` left with the retired envelope tables, so they earn the unknown-view refusal); a read the seam refused is returned as its typed refusal rather than as an empty page.

**Code-tree resolution and automatic pairing.** Code-tree resolution is delegated to `application/knowledge_code_pairing` (`observe_code_source`, `resolve_paired_code_root`, `code_tree_of`, `NoCodeTreeError` aliased as `_NoCodeTreeError`, `ObservedCodeSource` aliased as `_ObservedSource`). `knowledge_read_payload` and `_read_result` accept `repositories`. For paged views, `_read_result` resolves `paired_code_root` via `resolve_paired_code_root`, observes the code source on fresh reads via `_observe_source`, and forwards `code_state`, captured working-tree `object_directory`, and `paired_code_root` into `open_read_context` and `TreeReadScope`. `_record_view` and `_marks_view` obtain their code tree through `_observed_source_or_none` -> `_code_tree_of`, auto-pairing when no explicit `codeTreeId` is given and degrading to `None`/unverifiable when no root resolves. A caller-named `repositoryRoot` that resolves no tree raises `_NoCodeTreeError` (`selected_input_unavailable`).

### Invariants And Boundaries

- **No builder decides anything.** No classification is computed, no effect label inferred, no draft authored, no rationale judged, no ambiguity resolved by choosing, no missing assessment filled and no compatibility verdict produced anywhere in the module.

- **No semantic classification is added by naming.** `_read_result` retains the rich body, its selected tree and shared resolver internally; `_projected_body` mechanically projects that body for the mounted answer, and it invents no assessment. It is also the route the marks and query views take: on an ordinary naming view it returns names and derived state and no record body; on a requested `weakness` or `dependent` view it carries the top-level rows MIK-R118 and MIK-R124 authorize; and on `records`, `impact`, or `search` it delegates through `_one_view` to `application/knowledge_queries.py::run_query_view`.

- **A continuation is carried opaquely.** The builder never resolves or guesses a snapshot binding.

- **A source-resolution pair is named as a pair or not at all.** `_observe_source` (via `observe_code_source`) never returns a root without a tree or a tree without a root: a caller-named root without a tree raises `_NoCodeTreeError` (`selected_input_unavailable` naming the root); when neither root nor tree is supplied, pairing resolves `paired_code_root` (from `contractPath`/`repo_id`/`memoryRoot`/workspace) and observes its code tree, or leaves the pair unrequested (`None`) when no code root resolves.

## MIK-R118 Rule 6, MIK-R124 Rule 7, And KNO-R07 Query Views

The selected-tree reader sends `record` to `_record_view`, `weakness` and `dependent` to `_marks_view`, `writers` to `_writers_view`, and `QUERY_VIEWS` (`records`, `impact`, `search`) to `application/knowledge_queries.py::run_query_view` via `_one_view` with a `QueryViewContext`. The record view retains derived revision state and writer attribution. The writers view returns aggregate rows and a full report path through the same mounted read.

`weakness` lists the tree's open weaknesses — `weaknessKind` picks one kind, `folder` (falling back to `sourcePath`) a folder, `includeClosed` adds closed records — and a row holds the id, the file, the kind, the statement and the state, with the measurement and the closing where the record holds them and the anchor's state at the read's code tree. `dependent` lists the documents — `folder` (falling back to `sourcePath`) a folder of documents, `staleOnly` the stale ones, `standsOn` those with a link at a named code file, and `compact=True` projects through `compact_dependent_rows` — and a row holds the id, the document, the derived state, the last confirmation and the revision, with `movedLinks` naming each link that moved where it is stale. Neither view writes: a weakness anchor is observed, a dependent's state is derived, and no byte of a record changes.

The answer is a page. `limit` is the caller's, capped at `TOOL_ANSWER_LIST_MAX`; `counts` carries `rowsReturned`, `total`, `rowsRemaining` and `offset`; and while rows remain a `readOn` block names the same view, its narrowing filters and the `rows:<n>` cursor the next page starts at. A continuation is read as `rows:<n>` and nothing more: `_marks_offset` accepts that shape, starts at `0` when none
is given, and refuses `bad_continuation` naming the shape it reads for anything else. It checks no issuer, view, tree
or filter, so a caller-made `rows:0` — or any other syntactically valid offset — is followed as given; the walk is
never restarted in its place.

## 260928-MIK-L28 Proofs Beside The Invariant And Family Views (MIK-R28 Rule 4)

> Historical additive account, not the current mounted response: proofs, currentness and family-complete paging still inform the internal selection, but the answer names records and locations, not these earlier prose-bearing blocks. Database reads and `read_ar_files` publication continuations are not restored by this account.

`_read_result` now adds `proofs` to a read's result. Inside the existing selection-failure boundary, and
only when the selection is a converted memory tree and the view was not refused, it calls
`application/knowledge_proofs.tree_view_proofs` with the tree's index path and key. That function opens the
index only for the `invariant` and `family` views; every other view, and every database read, gets
`proofs: None`, which the response model omits.

- **The additive optional `proofs` field is accepted (architect ruling, 2026-09-29).**
- `IndexMismatchError` joined `_SELECTION_FAILURES`, so an index opened for the wrong tree key becomes the
  ordinary dataset refusal through `_selection_refusal`, not a raised error.
- A proof states what its test demonstrates, never that the test passed or that the invariant holds
  (MIK-R28 exclusions; Doc13).

## 260928-MIK-L08 The Integrity Check Returns A Leaf's Worklist (MIK-R08 Rule 7)

`knowledge_integrity_check_payload` now takes one `IntegrityCheckRequest` (four inputs — `memoryRoot`,
`codeRoot`, `baseCommits`, `contractPath` — as one frozen value); the caller-supplied namespace
(`repositoryId`) is retired, the index's own constant:

- **`contractPath`** names a leaf by its contract: the validator reads the leaf's memory worktree
  against its recorded memory base and code worktree.
- **`memoryRoot` with `codeRoot`** names a tree and its paired code checkout directly.
- **Neither** is refused with `refusalCode: selected_input_unavailable` (name a leaf, or a tree with
  its checkout).
- Whenever `contractPath` is named, the result is extended with `application/knowledge_worklist/surface`'s
  `leaf_worklist_fields`: `worklistState` (`present`, `absent` or `unreadable`) and `worklist` (the
  summary, the owner, one `{id, kind, subject}` row per item, and the persisted file's path for the full
  facts).
- The builder computes nothing: the worklist is the one the leaf's last memory-quality run or completed
  managed sync persisted beside its series contract. The contract path is read as given (read-only).

## 260928-MIK-L03 Currentness Beside The View (MIK-R03)

> Historical additive account, not the current mounted response: proofs, currentness and family-complete paging still inform the internal selection, but the answer names records and locations, not these earlier prose-bearing blocks. Database reads and `read_ar_files` publication continuations are not restored by this account.

`_read_result` now adds `currentness` to a read's result when the selection is a converted memory tree and
the view was not refused. Since MIK-R02 (260928-MIK-L02) it is computed by `_tree_extras`, once per page, through
`knowledge_paging.currentness.WalkCurrentness` at the walk's code tree, and it counts toward the page's
threshold; the rules below are L03's and are unchanged.

- **Only `codeTreeId` is a request (architect ruling 2, 2026-09-29T18:42:37).** A `repositoryRoot` alone,
  or nothing, gives an `unverifiable` block with compact entries; `HEAD` is never substituted. (The view
  context still completes its own source pair from `HEAD` for the blob-level `anchor_state` it already
  reported; that is untouched.) A `codeTreeId` named without `repositoryRoot` is read from the mount's
  workspace object store.
- **A currentness failure never refuses the read (ruling N2, 19:13:41).** The block is computed after the
  `_SELECTION_FAILURES` boundary, and `read_currentness` degrades every index, SQLite, file-system or Git
  failure to `unverifiableReason`, so the view is still answered.
- **The payload is not edited,** so a stale invariant stays visible with its statement and relationships.

## 260928-MIK-L02 A Converted Tree's Read Is A Bounded Page (MIK-R02)

> Historical additive account, not the current mounted response: proofs, currentness and family-complete paging still inform the internal selection, but the answer names records and locations, not these earlier prose-bearing blocks. Database reads and `read_ar_files` publication continuations are not restored by this account.

`_read_result` hands a converted memory tree's read to `application/knowledge_paging/tree_read.read_tree_page`
right after the selection (a two-line seam), so every such response is a page cut to the shared token
threshold, and its `continuation` is the shared token that also resumes the published-intent block's walks.


- **`_tree_extras(selected)`** is a per-page factory `(subject, walk code tree, candidate rows) -> (payload ->
  extras)`: it computes `proofs` (MIK-R28) and `WalkCurrentness` (MIK-R03) once, and returns each candidate
  page's additions, so both count toward the threshold (architect ruling F3, 2026-09-29 20:40:40).
- **`_ordering(request)`** applies `DEFAULT_ORDERING` only when `ordering_input` is `None`; an empty string
  keeps the base refusal `unadmitted_ordering_input` on every path (rulings Q5 of 19:56:40 and F1 of 20:40:40).
  `ReadToolRequest.ordering_input` now defaults to `None`.
- **`knowledge_read_payload`** adds `threshold` to every refusal of a converted-tree selection (unknown view,
  ordering, selection failure), because every response states the threshold (ruling F8).

## 260928-MIK-L01 The Family-Complete Leaf Read, And A Root With No Commit Refused By Name (MIK-R01)

> Historical additive account, not the current mounted response: proofs, currentness and family-complete paging still inform the internal selection, but the answer names records and locations, not these earlier prose-bearing blocks. Database reads and `read_ar_files` publication continuations are not restored by this account.

The tool reaches the family-complete leaf read through `knowledge_paging.tree_read` (a converted tree's
`source_context` read with `sourcePath`, and every `leaf` continuation); nothing in `_read_result` changed
for it. This module changes in two places.
- **A root with no commit is refused by name (the obligation carried from L02, 2026-09-29 21:17:07).**
  Before L01 a `repositoryRoot` naming a repository with no commit raised a pydantic `ValidationError` out of
  `open_read_context`. `_source_resolution` now raises `_NoCodeTreeError` when a caller-named root resolves
  no tree (no commit, or not a Git repository); it is the first member of `_SELECTION_FAILURES`, and
  `_selection_refusal` answers it `selected_input_unavailable` with a detail naming the root and the three
  ways out (a repository with a commit, `codeTreeId`, or no `repositoryRoot`). The fix applies to database
  and tree reads alike (review R1 N7: intended, and not a preservation regression, because base crashed on
  that input). The workspace default is unchanged: with no root named, a workspace without a tree still
  leaves the pair unrequested.
- **Refusals name the memory tree (rule 9, ruling N3 of 2026-09-30 00:08:39)** in `tree_read._refused`, for
  every refusal after the selection; the tree-selection refusals of this module state the threshold as
  before.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no `Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The public read projects names from its selected rich page; code-source observation and internally prepared proof/currentness extras remain distinct. [1]
- A converted tree's read is handed to the paged tree read right after the selection. [68]
- A refused read states the threshold block beside its refusal code and detail; a page states the same block in its own answer. [70]
- The paged tree read this module hands a converted selection to. [71]
- A named root that resolves no code tree is its own error, refused `selected_input_unavailable` naming the root. [72]
- `_observe_source` / `observe_code_source` raises `NoCodeTreeError` for a caller-named root without a tree. [73]
- The leaf read the tree read routes a `source_context` path read to (and, since MIK-R05, a read naming only `familyRevisionId`, as a family seed). [74]
- The mounted reader dispatches `QUERY_VIEWS` (`records`, `impact`, `search`), writers aggregate, record, and mark views through `_one_view`. [79]
- Code-tree observation and pairing resolve explicit or paired code roots (refusing a caller-named root without a tree) or leave the pair unrequested when no root resolves. [80]
- Current candidate source supports the operative account; historical sections grant no current tool or execution acceptance. [82]
- Cutover refusal helpers, worktree candidate capture and contract loading are imported at the operation branches that need them; existing legacy-format and root-selector refusals remain. [83]





- Integrity delivers bounded validator/worklist status beside the whole internal result, not selected-run identities or a semantic verdict. [3]



- Only admitted views carry proofs. [4]









- - The read adds `proofs` only for a converted memory tree's page, prepared once per page since MIK-R02. [57]
- - A key mismatch joins the selection failures. [58]

- - Invariant and family views of a tree carry their proofs; no pass or result key exists. [59]

- - The integrity check's request value. [60]


- - The worklist fields read from the persisted file. [62]
- - The tool returns the latest worklist. [63]
- - A converted tree's page carries `currentness` at the walk's code tree, computed once per page beside its proofs. [64]

- A named tree flags the stale invariant and keeps it visible. [65]
- Without `codeTreeId`, a resolved code root auto-pairs while an absent code root stays unverifiable. [66]
- A failing step never refuses the view. [67]



- - The default ordering, applied only when the caller named none. [69]

- - The one refusal envelope the read operation returns for an unknown view and for a view the seam refused. [77]
- - The one refusal envelope the read operation returns for an unknown view and for a view the seam refused. [78]

- - **Every way resolving and opening a selection can fail, refused the same way on every handler: a named root with no code tree is `selected_input_unavailable` naming the root (MIK-R01), a tree, Git or cache failure is `snapshot_unavailable` naming the tree, anything else the dataset refusal it was before.** [81]

### Cross-Repo References

No cross-repository contract is established by this file.


- All three tools refuse legacy/database selections without opening them; a partial read retains incomplete status. [56]

- Dataset, leaf, both or neither; the leaf's worklist fields added when a contract is named. [61]

- The flat read request as one frozen value: the continuation, the two revision selectors, the optional source roots, and an ordering left `None` unless the caller names one. [75]


- The flat read request's optional source-path seed, beside the unnamed-by-default ordering MIK-R02 introduced. [76]

- Admitted views include `records`, `impact`, and `search`; `_marks_rows` applies `folder` fallback and `compact_dependent_rows` when `compact=True`. [87]



- The whole selected comparison is filed before the answer names both trees, counts and bounded decision records with their total; no carried comparison body. [2]


- The strict integrity model carries validator totals, bounded violations and the optional persisted leaf worklist, not a CODE/currentness verdict. [51]



- The writer route publishes a bounded answer of problems, violations and notes beside its full report. [86]
