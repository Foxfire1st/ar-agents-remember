# mcp/src/agents_remember/application/knowledge_currentness/surface.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_currentness/surface.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T19:59:41+02:00 |
| lastVerifiedCommitHash | `2c6f170ef07bf6767d582f76c9f9dd06bbdd06a4`|
| lastVerifiedCommitDate | 2026-09-29T22:20:46+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[application route overview](../overview.md)

## Purpose

**The `currentness` block the two read surfaces attach for a converted memory tree (MIK-R03 rule 4).**
`knowledge_read` and the published-intent block of `read_ar_files` both read a converted tree through its
derived index, whose projection names records by UUID (MIK-R23 rule 6). This module finds the invariants
and families an answer returns, computes their state with `invariant_currentness`, and returns the block.

## Code Commentary

### Logic

- **What a read returns (architect ruling 3, 18:42:37).** `returned_records(index, answer)` walks every
  string in the answer, keeps the UUIDs, and translates each through the index's reverse map
  (`index.text_id`). Those that name an invariant or family record are returned; a family-membership row
  (a text ID containing `/`), claim, anchor and member UUIDs are ignored. The counts therefore cover every
  invariant the answer carries, whether it names the invariant (for example as a relationship) or returns
  it in full, plus every member of a family it carries (review N5, 19:13:41).
- **Which tree `knowledge_read` asks at (ruling 2, 18:42:37).** `requested_code_tree(code_tree_id,
  repository_root, default_repository)` counts only a named `codeTreeId`. A `repositoryRoot` alone, or
  nothing, requests nothing, so the block is `unverifiable`; `HEAD` is never substituted. A tree named
  without a repository is read from the mount's workspace object store.
  **Since MIK-R02 no production path calls `requested_code_tree` or `read_currentness`:** the
  converted-tree `knowledge_read` applies the same rule in `knowledge_paging/tree_read.py` (`_at_code_tree`:
  only the named `codeTreeId`, or the continuation's tree on a resumed page) and computes the block through
  `evaluate_answer`. Both functions stay exported, and L03's tests still exercise them.
- **The published-intent block's tree (ruling 1, 18:42:37)** is chosen by its caller, `published_intent.py`:
  the tree that route already resolved for the source it returns. This module takes whatever `CodeTree`
  it is given.
- `read_currentness(index_path, tree_key, code_tree, answer)` opens the index for that tree key, collects the
  records, and returns `invariant_currentness(...).to_document()`.
- **It never raises (ruling N2, 19:13:41).** An index, SQLite, file-system, `ValueError` or
  `SubprocessError` failure (`CURRENTNESS_FAILURES`, public since MIK-R02; `IndexMismatchError`, `MemoryTreeError`,
  `KnowledgeStorageError` and `CodeReadError` are all `ValueError`s) returns a block with the `codeTree`,
  zero counts, no invariants or families, and `unverifiableReason` "currentness could not be computed
  (<type>: <message>)". With no readable index there are no entries to attach a per-entry reason to, so the
  reason is stated once for the block (the worker's deviation, accepted in review round 2).
- **The seam MIK-R02 extracted (260928-MIK-L02, ruling F3 of 2026-09-29 20:40:40).** A bounded page is found
  by rendering candidate pages, and each candidate carries its `currentness`, so the evaluation is split
  out to run once per page: `named_uuids(answer)` (every projected UUID), `record_of(index, value)` (the
  `(kind, ID)` one UUID names, or `None`), `evaluate_answer(index_path, tree_key, code_tree, answer)` (every
  named record by UUID plus their `Currentness`; it raises the failures instead of degrading) and
  `failure_document(code_tree, error)` (the degraded block). `returned_records` and `read_currentness` are
  rebuilt on these helpers and behave as before: L03's `test_knowledge_currentness.py` passes unchanged,
  and the index is still opened through this module's `KnowledgeIndex`, so its failure injection holds.
  The caller is `application/knowledge_paging/currentness.py` (`WalkCurrentness`).

### Conventions

- The answer is passed in already dumped to JSON (`knowledge_read` dumps its payload once, review N6).

### Invariants And Boundaries

- **A currentness failure never refuses a read.** The block is advisory beside the answer.
- **The answer is never edited**, so every invariant stays visible with its statement and relationships
  whatever its state (D9).
- **No fallback to `HEAD` or the working tree** for a missing code tree.

### Todos

- None recorded. MIK-R29 may add an explicit tree selector to `read_ar_files` (ruling 1, 18:42:37).

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R03@v2` of task
`260928_maintained-invariant-knowledge` (with the architect rulings in the task's leaf document
`03_stale-invariants-flagged-at-read-time.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module statement: returned records are the UUIDs the index translates, and the answer is never edited. | "The answer itself is never edited" | mcp/src/agents_remember/application/knowledge_currentness/surface.py:1-10 |
| Every failure class the step degrades on, now public for the paged caller. | `CURRENTNESS_FAILURES` | mcp/src/agents_remember/application/knowledge_currentness/surface.py:43-43 |
| The records an answer returns, built on the per-UUID helper. | `returned_records`; `record_of` | mcp/src/agents_remember/application/knowledge_currentness/surface.py:64-73; mcp/src/agents_remember/application/knowledge_currentness/surface.py:76-85 |
| The UUIDs an answer carries, and the index's reverse map for one. | `named_uuids`; `text_id` | mcp/src/agents_remember/application/knowledge_currentness/surface.py:58-61; mcp/src/agents_remember/application/knowledge_currentness/surface.py:67-67 |
| The one evaluation a paged caller cuts candidates from; it raises instead of degrading. | `evaluate_answer` | mcp/src/agents_remember/application/knowledge_currentness/surface.py:125-144 |
| Only a named tree ID is a request; `HEAD` is never substituted. | `requested_code_tree` | mcp/src/agents_remember/application/knowledge_currentness/surface.py:88-101 |
| The block, which degrades to the failure document and never raises. | `read_currentness`; `failure_document` | mcp/src/agents_remember/application/knowledge_currentness/surface.py:104-122; mcp/src/agents_remember/application/knowledge_currentness/surface.py:147-156 |
| The degraded block's reason text. | `failure_document`; "currentness could not be computed" | mcp/src/agents_remember/application/knowledge_currentness/surface.py:147-156 |
| The `knowledge_read` consumer since MIK-R02: currentness once per page at the walk's code tree. | `_tree_extras`; `WalkCurrentness` | mcp/src/agents_remember/mcp/tools/knowledge.py:463-479 |
| The published-intent consumer since MIK-R02, at its resolved source tree and inside the bounded block. | `read_published_intent`; `WalkCurrentness` | mcp/src/agents_remember/application/published_intent.py:460-486 |
| No tree, or only a repository, is unverifiable and never reads `HEAD`. | `test_knowledge_read_without_a_named_tree_is_unverifiable_and_never_reads_head` | mcp/tests/test_knowledge_currentness.py:561-580 |
| A failing step degrades to a reason and never refuses the read. | `test_a_failing_currentness_step_degrades_to_a_reason_and_never_refuses_the_read` | mcp/tests/test_knowledge_currentness.py:633-656 |

## Cross-Repo References

No meaningful cross-repo references found: the module reads one memory tree's index and one code tree,
both named by its caller.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History
- 2026-09-29T19:58:54+00:00: Generated citation repair: `requested_code_tree` repointed to mcp/src/agents_remember/application/knowledge_currentness/surface.py:88-101. No content impact: mechanical anchor-range projection bound to citation source snapshot 1e041d3cc3624746d949d3346f148082cba5203cab5cbced9c44716f89831a84; claim bytes unchanged; generated by ccr-r10@v1.

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T21:41:17+02:00 — 260928-MIK-L02 curator (uncommitted change set on `ar/260928-mik-l02`, code base `a4eba7b7b5b5ffee7277f6c19086697925a22df2` plus the staged delta): **body updated for the seam MIK-R02 extracted.** A Logic paragraph records `named_uuids`, `record_of`, `evaluate_answer`, `failure_document` and the now-public `CURRENTNESS_FAILURES` (formerly `_STEP_FAILURES`), used by `knowledge_paging/currentness.py` to compute currentness once per page (architect ruling F3, 2026-09-29 20:40:40). **Three reopened claims were re-read and reworded:** the failure-class row now names `CURRENTNESS_FAILURES`; the returned-records row names `record_of` (with a new `named_uuids` row and an `evaluate_answer` row); the degraded-block row is split into `read_currentness` and `failure_document`. **The two consumer rows were reworded:** `knowledge_read` now reaches this module through `_tree_extras` and `WalkCurrentness`, and the published-intent block through `WalkCurrentness`; the Logic records that no production path calls `requested_code_tree` or `read_currentness` any more. `returned_records` and `read_currentness` behave as before.
- 2026-09-29T19:59:41+02:00 — 260928-MIK-L03 curator (uncommitted change set on `ar/260928-mik-l03`, code base `e40c314ca55305f7e4334b4e8e16a10297f6f175` plus the working-tree delta and untracked files): created this card for the new file MIK-R03 adds. It records the architect rulings of 2026-09-29: 18:42:37 rulings 1 to 3 (the published-intent tree is its caller's; only `codeTreeId` is a request and `HEAD` is never used; the returned invariants and families) and 19:13:41 rulings N2 (never refuses, never raises) and N5 (the counts cover every invariant carried, named or in full). The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
