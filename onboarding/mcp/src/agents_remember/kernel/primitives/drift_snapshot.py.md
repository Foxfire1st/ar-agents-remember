# mcp/src/agents_remember/kernel/primitives/drift_snapshot.py

| Field                  | Value                                                         |
| ---------------------- | ------------------------------------------------------------- |
| repository             | agents-remember                                               |
| path                   | `mcp/src/agents_remember/kernel/primitives/drift_snapshot.py` |
| doc_type               | `file-level-onboarding`                                       |
| lastUpdated            | 2026-08-08T14:38+02:00                                        |
| lastVerifiedCommitHash | `65cb81f7de4db13c0627264fec1eb46f444e0ee3`                    |
| lastVerifiedCommitDate | 2026-08-12T04:57:26+02:00|
| governingOverview      | `overview.md`                                                 |

## Governing Overview

[kernel primitives overview](overview.md)

## Purpose

`kernel/primitives/drift_snapshot.py` owns the drift-snapshot path and removal primitives,
created by 260731-EFA-L9 so the serving projection readers, worktrees, and memory quality can
resolve and remove drift snapshots without crossing packages.

## Code Commentary

### Logic

`sanitize_report_token` (cit:([`sanitize_report_token`], mcp/src/agents_remember/kernel/primitives/drift_snapshot.py:15-15)) makes a report token filesystem-safe;
`drift_snapshot_path` (cit:([`drift_snapshot_path`], mcp/src/agents_remember/kernel/primitives/drift_snapshot.py:21-21)) resolves the per-repository, per-branch
snapshot path under the coordination root; `remove_drift_snapshot`
(cit:([`remove_drift_snapshot`], mcp/src/agents_remember/kernel/primitives/drift_snapshot.py:27-27)) deletes it with a `missing_ok`-style guard.

### Conventions

- Pure path/side-effect primitives with no repository knowledge; callers own the schema.

### Invariants And Boundaries

- The snapshot filename must stay deterministic from `(repository, branch)` so drift checks and
  pruning agree on the same file.

### Todos

No known follow-up.

## Docs References

No external/domain documentation is configured.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The projection-side pruning policy consumes these primitives. | `prune_orphaned_drift_snapshots` | mcp/src/agents_remember/serving/projections/drift_snapshots.py:23-23 |
| Removal edge coverage rides the structural-coverage suite. | `test_drift_snapshot_removal_edges` | mcp/tests/test_leaf_structural_coverage.py:221-221 |

## Cross-Repo References

No cross-repository implementation participates.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-12T01:38+02:00 — 260731-EFA-L22 citation maintenance: re-anchored the structural
  coverage proof after the test responsibility split; documented behavior is unchanged.

- 2026-08-08T14:38+02:00 — 260731-EFA-L9 curator: created for the kernel drift-snapshot
  primitives extracted during the layering cleanup. Verification metadata pinned until closeout
  stamps the L9 code commit.
