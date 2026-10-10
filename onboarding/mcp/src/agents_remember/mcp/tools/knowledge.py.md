# mcp/src/agents_remember/mcp/tools/knowledge.py

## Governing Overview

[mcp/tools route overview](overview.md)

## Purpose

Payload builders for three mounted knowledge operations over converted trees.

## Code Commentary

### Logic

Read selects the tree's derived index and delegates through bounded paging, carrying tree/index state, currentness and applicable proofs. Named source roots with no commit refuse; resolution is complete or absent. [1]

Diff compares knowledge/onboarding Git files, or privately captures working memory when afterRevision is absent. It groups records/entries and cards/sidecars, bounds patches and names every omitted/cut portion; no effect label is inferred. [2]

Integrity runs the knowledge validator and returns the latest leaf worklist for a contract, not a canonical detection run or compatibility verdict. Legacy roots and database files refuse before an open; change/project and selected-run fields are removed. [3] [51] [56]

### Invariants And Boundaries

- A partial index is never complete.
- Unheld selectors refuse rather than implying no change.
- Each public payload uses the shared response-model choke point.

### Logic

`knowledge_read_payload` refuses a view outside `source_context`, `invariant`, `family`, `review_matrix` and `curation_queue` through `_refused_read(view, repositoryId, "unknown_view", ...)` rather than picking a default view; a read the seam refused is returned as its typed refusal rather than as an empty page.

**The read context's source-resolution pair is completed rather than half-supplied, and the mount hands
over a default repository rather than half a pair.** `_source_resolution(request, workspace_root)`
returns `(repository_root, code_tree_id)` and never one without the other: a caller who named both gets
both back untouched, a caller who named a root gets that root's own current tree from
`_current_code_tree` (since 260928-MIK-L01, a named root with no tree is refused by name, below), and a
caller who named neither gets the mount's workspace default **only when a tree can actually be resolved
from it**. `_current_code_tree` shells `git -C <root> rev-parse
HEAD^{tree}` under `_GIT_TIMEOUT_SECONDS`, validates the answer against `_TREE_ID_PATTERN` and returns
`None` — never a guess — when the root is not a repository, Git is absent, Git does not answer in time,
or the answer is not a tree id; the context is then built with neither half. This is what the registration
hands over as `workspace_root=`, and it is why a minimal schema-conformant `knowledge_read` returns a
view instead of a raw `KnowledgeReadContext` validation error.

### Invariants And Boundaries

- **No builder decides anything.** No classification is computed, no effect label inferred, no draft authored, no rationale judged, no ambiguity resolved by choosing, no missing assessment filled and no compatibility verdict produced anywhere in the module.

- **The read payload is the view payload.** The success branch dumps the seam's own payload; no second renderer, filter or classification exists in this module for requirement 6.8 to be violated by.

- **A continuation is carried opaquely.** The builder never resolves or guesses a snapshot binding.

- **A source-resolution pair is named as a pair or not at all.** `_source_resolution` never returns a
  root without a tree or a tree without a root: a caller-named root is completed with that root's own
  current tree, the mount's workspace default is named only when a tree can be resolved from it, and
  since 260928-MIK-L01 a caller-named root Git cannot answer for (no commit, or not a repository) is
  refused `selected_input_unavailable` naming the root, rather than passed on as half a pair. `_current_code_tree` returns `None` — never a
  guess — for a root that is not a repository, an absent Git, a timeout or an answer that is not a tree
  id, so a minimal read reaches the context as "no source resolution was requested" instead of as a
  raised validation error out of the mounted tool.

## 260928-MIK-L28 Proofs Beside The Invariant And Family Views (MIK-R28 Rule 4)

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


- Read paging/source resolution. [1]


- Bounded Git knowledge diff. [2]


- Validator/worklist integrity answer. [3]


- Only admitted views carry proofs. [4]


- Current validator/worklist response, without selected-run identities. [51]


- Legacy selections open no database; partial read stays incomplete. [56]


- - The read adds `proofs` only for a converted memory tree's page, prepared once per page since MIK-R02. [57]
- - A key mismatch joins the selection failures. [58]
- - Invariant and family views of a tree carry their proofs; no pass or result key exists. [59]
- - The integrity check's request value. [60]
- - Dataset, leaf, both or neither; the leaf's worklist fields added when a contract is named. [61]
- - The worklist fields read from the persisted file. [62]
- - The tool returns the latest worklist. [63]
- - A converted tree's page carries `currentness` at the walk's code tree, computed once per page beside its proofs. [64]
- - A named tree flags the stale invariant and keeps it visible. [65]
- - Without `codeTreeId` it is unverifiable and never reads `HEAD`. [66]
- - A failing step never refuses the view. [67]
- - A converted tree's read is handed to the paged tree read right after the selection. [68]
- - The default ordering, applied only when the caller named none. [69]
- - A converted-tree refusal states the threshold; a database refusal does not. [70]
- - The paged tree read this module hands a converted selection to. [71]
- - A named root that resolves no code tree is its own error, refused `selected_input_unavailable` naming the root. [72]
- - `_source_resolution` raises it for a caller-named root without a tree. [73]
- - The leaf read the tree read routes a `source_context` path read to (and, since MIK-R05, a read naming only `familyRevisionId`, as a family seed). [74]
- - The flat read request as one frozen value: the continuation, the two revision selectors, the optional source roots, and an ordering left `None` unless the caller names one. [75]
- - The flat read request's optional source-path seed, beside the unnamed-by-default ordering MIK-R02 introduced. [76]
- - The one refusal envelope the read operation returns for an unknown view and for a view the seam refused. [77]
- - The one refusal envelope the read operation returns for an unknown view and for a view the seam refused. [78]
- - The read builder: the five-view closure, the shared dataset selection (a converted memory tree reads through its index), the resolver call, the seam call, and the payload returned as the view payload itself — with every completeness statement forced to `false` when that index is partial. [79]
- - The source-resolution pair completed rather than half-supplied: the caller's own root with its current tree (refused by name when it has none, since MIK-R01), the mount's workspace default used only when a tree can be resolved from it, and neither half when Git cannot answer for it. [80]
- - **Every way resolving and opening a selection can fail, refused the same way on every handler: a named root with no code tree is `selected_input_unavailable` naming the root (MIK-R01), a tree, Git or cache failure is `snapshot_unavailable` naming the tree, anything else the dataset refusal it was before.** [81]

### Cross-Repo References

No cross-repository contract is established by this file.
