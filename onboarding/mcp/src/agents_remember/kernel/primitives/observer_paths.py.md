# mcp/src/agents_remember/kernel/primitives/observer_paths.py

| Field                  | Value                                                          |
| ---------------------- | -------------------------------------------------------------- |
| repository             | agents-remember                                                |
| path                   | `mcp/src/agents_remember/kernel/primitives/observer_paths.py`   |
| doc_type               | `file-level-onboarding`                                        |
| lastUpdated            | 2026-08-08T14:38+02:00                                         |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`                     |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `overview.md`                                                  |

## Governing Overview

[kernel primitives overview](overview.md)

## Purpose

`kernel/primitives/observer_paths.py` resolves the observer store root — the one read/write path
abstraction (260731-EFA-L9 moved it into kernel so the serving projection readers, the observer
write side, worktrees, and memory quality resolve the same roots without crossing packages).

## Code Commentary

### Logic

`observer_logs_root` (cit:([`observer_logs_root`], mcp/src/agents_remember/kernel/primitives/observer_paths.py:34-34)) resolves `logs/observer` under the
coordination root; `observer_root` resolves the observer root from the runtime config;
`drift_snapshot_dir` (cit:([`drift_snapshot_dir`], mcp/src/agents_remember/kernel/primitives/observer_paths.py:44-44)) resolves the drift-snapshot directory; and
`LANDING_FINAL_BASENAME` names the immutable landing-final file.

### Conventions

- Dependency-light: no reducer/snapshot/store imports; callers combine these paths with their own
  I/O.

### Invariants And Boundaries

- A future synced coordination store is a swap at this one site, not a refactor of every reader.

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
| The projection readers use these paths after the observer→serving move. | `observer_logs_root` | mcp/src/agents_remember/serving/projections/paths.py:29-29 |

## Cross-Repo References

No cross-repository implementation participates.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-08T14:38+02:00 — 260731-EFA-L9 curator: created for the kernel observer-path
  extraction. Verification metadata pinned until closeout stamps the L9 code commit.
