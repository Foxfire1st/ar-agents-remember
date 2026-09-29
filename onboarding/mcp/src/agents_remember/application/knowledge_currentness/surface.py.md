# mcp/src/agents_remember/application/knowledge_currentness/surface.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_currentness/surface.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T19:59:41+02:00 |
| lastVerifiedCommitHash | `719acba61e491d0b7f1ee82dbeea5314ecec5083`|
| lastVerifiedCommitDate | 2026-09-29T20:27:14+02:00|
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
- **The published-intent block's tree (ruling 1, 18:42:37)** is chosen by its caller, `published_intent.py`:
  the tree that route already resolved for the source it returns. This module takes whatever `CodeTree`
  it is given.
- `read_currentness(index_path, tree_key, code_tree, answer)` opens the index for that tree key, collects the
  records, and returns `invariant_currentness(...).to_document()`.
- **It never raises (ruling N2, 19:13:41).** An index, SQLite, file-system, `ValueError` or
  `SubprocessError` failure (`_STEP_FAILURES`; `IndexMismatchError`, `MemoryTreeError`,
  `KnowledgeStorageError` and `CodeReadError` are all `ValueError`s) returns a block with the `codeTree`,
  zero counts, no invariants or families, and `unverifiableReason` "currentness could not be computed
  (<type>: <message>)". With no readable index there are no entries to attach a per-entry reason to, so the
  reason is stated once for the block (the worker's deviation, accepted in review round 2).

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
| Every failure class the step degrades on. | `_STEP_FAILURES` | mcp/src/agents_remember/application/knowledge_currentness/surface.py:33-33 |
| The records an answer returns. | `returned_records`; `text_id` | mcp/src/agents_remember/application/knowledge_currentness/surface.py:48-64 |
| Only a named tree ID is a request; `HEAD` is never substituted. | `requested_code_tree` | mcp/src/agents_remember/application/knowledge_currentness/surface.py:67-80 |
| The block, and the degraded block that never raises. | `read_currentness`; "currentness could not be computed" | mcp/src/agents_remember/application/knowledge_currentness/surface.py:83-109 |
| The `knowledge_read` consumer, after the selection boundary. | `read_currentness`; `requested_code_tree` | mcp/src/agents_remember/mcp/tools/knowledge.py:432-441 |
| The published-intent consumer, at its resolved source tree. | `read_published_intent`; `read_currentness` | mcp/src/agents_remember/application/published_intent.py:445-473 |
| No tree, or only a repository, is unverifiable and never reads `HEAD`. | `test_knowledge_read_without_a_named_tree_is_unverifiable_and_never_reads_head` | mcp/tests/test_knowledge_currentness.py:561-580 |
| A failing step degrades to a reason and never refuses the read. | `test_a_failing_currentness_step_degrades_to_a_reason_and_never_refuses_the_read` | mcp/tests/test_knowledge_currentness.py:633-656 |

## Cross-Repo References

No meaningful cross-repo references found: the module reads one memory tree's index and one code tree,
both named by its caller.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T19:59:41+02:00 — 260928-MIK-L03 curator (uncommitted change set on `ar/260928-mik-l03`, code base `e40c314ca55305f7e4334b4e8e16a10297f6f175` plus the working-tree delta and untracked files): created this card for the new file MIK-R03 adds. It records the architect rulings of 2026-09-29: 18:42:37 rulings 1 to 3 (the published-intent tree is its caller's; only `codeTreeId` is a request and `HEAD` is never used; the returned invariants and families) and 19:13:41 rulings N2 (never refuses, never raises) and N5 (the counts cover every invariant carried, named or in full). The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
