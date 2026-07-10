# mcp/tests/test_store_scaling_cs6.py

| Field                  | Value                                     |
| ---------------------- | ----------------------------------------- |
| repository             | agents-remember                           |
| path                   | `mcp/tests/test_store_scaling_cs6.py`     |
| doc_type               | `file-level-onboarding`                   |
| lastUpdated            | 2026-07-10T01:14+02:00                    |
| lastVerifiedCommitHash |                                           `0d5ce6784930aa4e9006ab4bbf2b788a3296abce`|
| lastVerifiedCommitDate |                                           2026-07-10T22:30:19+02:00|
| governingOverview      | `../overview.md`                          |

## Governing Overview

[mcp overview](../overview.md) — there is no route-local `mcp/tests/overview.md`; existing test sidecars are governed by the package overview.

## Purpose

`test_store_scaling_cs6.py` is the store-level CS-6 regression suite for HFX2-L12. It verifies bounded reads, compaction/reclamation, and malformed-line tolerance across the supervisor signal store, expectation rows, provider metrics/degradation stores, event river, terminal catalog, and dashboard-tolerant JSONL stores.

## Code Commentary

### 260707-HFX2-L13 F3/F7 Storage Bounds

`LifecycleHeartbeatSidecarTests` proves at two heartbeat counts that the lifecycle log retains one
real row, the sidecar stays bounded, and merged reads expose only the latest beat. The B1 regression
creates 10 and 100 beaten lifecycle directories and proves pruning removes every directory before a
later fleeting reap. Event-river cases prove live workspace cursors resume without duplicates or
skips after compaction at two sizes and that the virtual base offset advances.

### Logic

The suite uses `_scaling` helpers to prove post-compaction size is bounded at multiple seed sizes, fixed-limit reads do not scale with whole-file size, per-finding snapshot paths do not re-read stores, tolerant readers skip torn lines, terminal-catalog liveness sweeps perform constant disk I/O at two catalog sizes, and startup workspace-river compaction preserves exactly the retained tail for reconnecting clients.

### Conventions

Each store is temp-rooted. Tests prefer deterministic read/write/count metrics over timing, and they seed at two sizes when proving reclamation or subquadratic growth.

### Invariants And Boundaries

The F3 river test covers the startup-boundary compactor only. It does not claim live cursor-safe compaction; that remains HFX2-L13 scope because live clients resume by byte offset and appenders exist in more than one process.

### Todos

Extend this suite when HFX2-L13 lands live river compaction, task-doc broadcast windowing, or heartbeat coalescing.

## Docs References

No external documentation governs these repo-local store scaling regressions.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant documentation found after checking live sources; no Domain Documentation entries are configured. | N/A | N/A |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Store scaling tests cover signal compaction/snapshot reads, metrics tail reads, expectation compaction, provider degradation compaction, tolerant readers, terminal catalog batch/compact, and workspace-river compaction. | L57-L155; L157-L193; L204-L233; L277-L332; L335-L389; L438-L571 | [mcp/tests/test_store_scaling_cs6.py](agents-remember/mcp/tests/test_store_scaling_cs6.py) |
| The shared CS-6 assertion helpers provide subquadratic, bounded-file-size, and bounded-count assertions used by this suite. | L58-L125 | [mcp/tests/_scaling.py](agents-remember/mcp/tests/_scaling.py) |
| The startup workspace-river compactor documents why live cursor-safe compaction is out of scope for this leaf. | L99-L150 | [mcp/src/agents_remember/observer/event_retention.py](agents-remember/mcp/src/agents_remember/observer/event_retention.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Same-repository tests only. | N/A | N/A |

## Update History

- 2026-07-10T01:14+02:00 — 260707-HFX2-L13 F3/F7/B1: added two-size heartbeat coalescing,
  complete lifecycle-directory reclamation, and live virtual-cursor compaction regressions.
  Verification metadata remains pinned until closeout stamps the eventual L13 code commit.

- 2026-07-09T19:31+02:00 — 260707-HFX2-L12: created for the store, event-river, terminal-catalog, and tolerant-reader CS-6 regressions added by the L12 worker. Verification metadata pinned until closeout stamps the HFX2-L12 commit.
