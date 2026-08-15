# mcp/tests/test_single_owner_primitives.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_single_owner_primitives.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-15T02:42:41+02:00 |
| lastVerifiedCommitHash | `28a66feae742bf02fe4b647388b220f921cc7007` |
| lastVerifiedCommitDate | 2026-08-15T03:44:49+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

Tests for git, atomic-publish, and task-document writer fitness functions.

## Code Commentary

### Logic

Module-level surface:

`TaskDocumentWriterCensusTests` plants every supported spelling of the new cross-root
`write_task_doc_batch` call—direct/renamed import, module alias, and relative import—and requires
the census to report the canonical API name. These join the existing writer cases without weakening
the false-positive boundary for re-exports or unrelated local names.

- `_git` (function, lines 26-31) — What the git rule reports for ``source``, as ``line [form]`` strings.
- `_replace` (function, lines 34-39) — What the atomic-write rule reports for ``source``.
- `_task_writers` (function, lines 42-47) — What the task-document writer census reports for one module.
- `SingleOwnerPrimitiveTests` (class, lines 50-114) — The armed checks run in the ordinary suite, so they run wherever it does.
- `GitSweepReachTests` (class, lines 118-206) — Every bypass the git rule claims to catch, planted and required to be caught.
- `GitSweepFalsePositiveTests` (class, lines 210-293) — Known-good constructs the package really contains. None of these may be reported.
- `ReplaceSweepReachTests` (class, lines 297-316) — Every way to reach the replace syscall, planted and required to be caught.
- `ReplaceSweepFalsePositiveTests` (class, lines 320-350) — The 83 near neighbours measured in the package. None of these may be reported.
- `TaskDocumentWriterCensusTests` (class, lines 353-396) — The production-writer census follows the import forms a new caller can use.
- `OffenderReportTests` (class, lines 400-421) — L6-R15: the message names every offender and the fix, or the check is unusable.

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.

### Todos

None.

## Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Defines the function `_git` (lines 26-31) — What the git rule reports for ``source``, as ``line [form]`` strings.. | `_git` | mcp/tests/test_single_owner_primitives.py:26-31 |
| Defines the function `_replace` (lines 34-39) — What the atomic-write rule reports for ``source``.. | `_replace` | mcp/tests/test_single_owner_primitives.py:34-39 |
| Defines the function `_task_writers` (lines 42-47) — What the task-document writer census reports for one module.. | `_task_writers` | mcp/tests/test_single_owner_primitives.py:42-47 |
| Defines the class `SingleOwnerPrimitiveTests` (lines 50-114) — The armed checks run in the ordinary suite, so they run wherever it does.. | `SingleOwnerPrimitiveTests` | mcp/tests/test_single_owner_primitives.py:50-114 |
| Defines the class `GitSweepReachTests` (lines 118-206) — Every bypass the git rule claims to catch, planted and required to be caught.. | `GitSweepReachTests` | mcp/tests/test_single_owner_primitives.py:118-206 |
| Defines the class `GitSweepFalsePositiveTests` (lines 210-293) — Known-good constructs the package really contains. None of these may be reported.. | `GitSweepFalsePositiveTests` | mcp/tests/test_single_owner_primitives.py:210-293 |
| Defines the class `ReplaceSweepReachTests` (lines 297-316) — Every way to reach the replace syscall, planted and required to be caught.. | `ReplaceSweepReachTests` | mcp/tests/test_single_owner_primitives.py:297-316 |
| Defines the class `ReplaceSweepFalsePositiveTests` (lines 320-350) — The 83 near neighbours measured in the package. None of these may be reported.. | `ReplaceSweepFalsePositiveTests` | mcp/tests/test_single_owner_primitives.py:320-350 |
| Defines the class `TaskDocumentWriterCensusTests` (lines 353-396) — The production-writer census follows the import forms a new caller can use.. | `TaskDocumentWriterCensusTests` | mcp/tests/test_single_owner_primitives.py:353-396 |
| Defines the class `OffenderReportTests` (lines 400-421) — L6-R15: the message names every offender and the fix, or the check is unusable.. | `OffenderReportTests` | mcp/tests/test_single_owner_primitives.py:400-421 |

## Update History

- 2026-08-15T02:42:41+02:00 — 260815-DAG-L1 review repair: added direct-import, module-alias,
  and relative-import forcing cases for `write_task_doc_batch`, so an unreviewed batch publisher
  cannot evade the task-document single-owner census.
- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
