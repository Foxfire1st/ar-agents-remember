# mcp/tests/test_store_scaling_cs6.py

| Field                  | Value                                     |
| ---------------------- | ----------------------------------------- |
| repository             | agents-remember                           |
| path                   | `mcp/tests/test_store_scaling_cs6.py`     |
| doc_type               | `file-level-onboarding`                   |
| lastUpdated            | 2026-07-10T01:14+02:00                    |
| lastVerifiedCommitHash |                                           `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`|
| lastVerifiedCommitDate |                                           2026-08-05T12:41:24+02:00|
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

Each store is temp-rooted. Tests prefer deterministic read/write/count metrics over timing, and they seed at two sizes when proving reclamation or subquadratic growth. Store entry points are addressed through parameter objects rather than loose keywords: `SupervisorSignalCooldownStore.in_cooldown` takes a `SupervisorSignalKey(target=SupervisorSignalTarget(...), finding_kind=..., detail=...)`, `write_expectation_row` takes an `Expectation(kind=..., source_id=..., subject=ExpectationSubject(...))`, `AmbientLifecycle` takes `timing=AmbientTiming(heartbeat_seconds=...)`, and `TerminalCatalogLivenessSweeper` takes `probe=LivenessProbe(hysteresis=TerminalCatalogLivenessConfig(...), pane_capturer=...)`.

### Invariants And Boundaries

The F3 river test covers the startup-boundary compactor only. It does not claim live cursor-safe compaction; that remains HFX2-L13 scope because live clients resume by byte offset and appenders exist in more than one process.

### Todos

Extend this suite when HFX2-L13 lands live river compaction, task-doc broadcast windowing, or heartbeat coalescing.

## Docs References

No external documentation governs these repo-local store scaling regressions.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant documentation found after checking live sources; no Domain Documentation entries are configured. | N/A | N/A |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Store scaling tests cover signal compaction/snapshot reads, metrics tail reads, expectation snapshot reads, heartbeat/lifecycle reclamation, expectation and metrics compaction, provider degradation compaction, tolerant readers, terminal catalog batch/compact, and workspace-river compaction. | `SupervisorSignalStoreScalingTests` | mcp/tests/test_store_scaling_cs6.py:92-160 |
| The shared CS-6 assertion helpers provide subquadratic, bounded-file-size, and bounded-count assertions used by this suite. | "def assert_subquadratic" | mcp/tests/_scaling.py:88-88 |
| The startup workspace-river compactor documents why live cursor-safe compaction is out of scope for this leaf. | `compact_workspace_river` | mcp/src/agents_remember/observer/event_retention.py:110-152 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| Same-repository tests only. | N/A | N/A |

## Update History

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B22 curator: replaced the `n/a` table rows and
  the history `_scaling.py`/`compact_workspace_river` citations with exact anchors and
  fixer-generated ranges; exact non-fixing check returns zero findings.

- 2026-07-31T16:50+02:00 — 260731-EFA-L2 code-quality gate: the store entry points this suite
  drives moved their loose keywords into parameter objects
  (`SupervisorSignalKey`/`SupervisorSignalTarget` for `in_cooldown`,
  `Expectation`/`ExpectationSubject` for `write_expectation_row`, `AmbientTiming` for
  `AmbientLifecycle`, and `LivenessProbe` for `TerminalCatalogLivenessSweeper`), and a whole-file
  reformat pushed every block down. Recorded the new call shapes in Conventions and re-anchored
  the own-file citations against the current source (signal store L76-L162, metrics tail
  L163-L215, expectation snapshot L216-L250, heartbeat/reclamation L288-L383, expectation and
  metrics compaction L384-L464, degradation compaction L465-L482, tolerant readers L251-L287 with
  L483-L525, terminal catalog L526-L650, river compaction L651-L749), plus the moved `_scaling.py`
  helpers cit:(["def assert_subquadratic"], mcp/tests/_scaling.py:88-88) and `compact_workspace_river` cit:([`compact_workspace_river`], mcp/src/agents_remember/observer/event_retention.py:110-152). No test case was added, removed,
  or renamed and every bounded-count, bounded-size, and two-size assertion is unchanged.

- 2026-07-10T01:14+02:00 — 260707-HFX2-L13 F3/F7/B1: added two-size heartbeat coalescing,
  complete lifecycle-directory reclamation, and live virtual-cursor compaction regressions.
  Verification metadata remains pinned until closeout stamps the eventual L13 code commit.

- 2026-07-09T19:31+02:00 — 260707-HFX2-L12: created for the store, event-river, terminal-catalog, and tolerant-reader CS-6 regressions added by the L12 worker. Verification metadata pinned until closeout stamps the HFX2-L12 commit.
