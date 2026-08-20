# mcp/tests/test_l6_diff_coverage_nw5.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_l6_diff_coverage_nw5.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-21T00:45+02:00 |
| lastVerifiedCommitHash | `e5cb139f66abbd6502d4dcc4be883eb5f49770fe` |
| lastVerifiedCommitDate | 2026-08-21T00:28:23+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

L6 closeout diff-coverage tests for batch NW5. Each test targets one exact changed line or untaken branch edge listed in `/tmp/l6-cov-NW5.json`; tests exercise the real helpers and fixtures and never weaken the assertions they encode.

## Code Commentary

- `TestSourceIndexCurrentGeneration` covers manifest-readiness mismatch returning `None`.
- `TestSourceIndexOpenWarm` covers metadata stability across checks.
- `TestReopenPlanning` covers missing masters, non-master parents, index-entry gaps, and master-reference refusals.
- `TestStructuralIndex` covers recorded call expressions and skipped error nodes.
- `TestFinalize` covers reconcile without a document root.

## Repo-Internal References

This module defines the test classes cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Defines the class `TestSourceIndexCurrentGeneration` (lines 105-123). | `TestSourceIndexCurrentGeneration` | mcp/tests/test_l6_diff_coverage_nw5.py:105-123 |
| Defines the class `TestSourceIndexOpenWarm` (lines 139-158). | `TestSourceIndexOpenWarm` | mcp/tests/test_l6_diff_coverage_nw5.py:139-158 |
| Defines the class `TestReopenPlanning` (lines 178-215). | `TestReopenPlanning` | mcp/tests/test_l6_diff_coverage_nw5.py:178-215 |
| Defines the class `TestStructuralIndex` (lines 218-232). | `TestStructuralIndex` | mcp/tests/test_l6_diff_coverage_nw5.py:218-232 |
| Defines the class `TestFinalize` (lines 266-278). | `TestFinalize` | mcp/tests/test_l6_diff_coverage_nw5.py:266-278 |

## Update History

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-15T09:53+02:00 — No content impact: L3's Pyright repair supplies the newly required
  contract fixture to the existing missing-document-root branch proof; its assertion is unchanged.
- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors derived from current worktree source. Verification metadata pinned until closeout stamps the code commit.
