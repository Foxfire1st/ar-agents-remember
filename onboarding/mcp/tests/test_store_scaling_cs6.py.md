# mcp/tests/test_store_scaling_cs6.py

| Field                  | Value                                     |
| ---------------------- | ----------------------------------------- |
| repository             | agents-remember                           |
| path                   | `mcp/tests/test_store_scaling_cs6.py`     |
| doc_type               | `file-level-onboarding`                   |
| lastUpdated            | 2026-07-10T01:14+02:00                    |
| lastVerifiedCommitHash |                                           `1abeed661cbbf813c7c8a1b651a14dbcf2ad2b4e`|
| lastVerifiedCommitDate |                                           2026-08-25T17:21:45+02:00|
| governingOverview      | `../overview.md`                          |

## Governing Overview

[mcp overview](../overview.md) — there is no route-local `mcp/tests/overview.md`; existing test sidecars are governed by the package overview.

## Purpose

Scaling and corruption-tolerance suite for notifier, expectation, provider, event, lifecycle, and terminal stores.

## Code Commentary

### Logic

Notifier signal fixtures use canonical master `TaskDocumentRef` plus seat role while the suite proves bounded compaction, snapshot reuse, tolerant reads, constant-I/O sweeps, and subquadratic behavior across store sizes.

### Conventions

Test-only evidence uses deterministic fakes/fixtures and exercises the owning seam directly.

### Invariants And Boundaries

Scaling behavior must not depend on retired leaf-key grouping; task-document-and-role identity remains stable across compaction and sweep snapshots.

## Docs References

No Domain Documentation source is configured for this repository-local regression contract.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Current suite declaration anchoring this card. | `_signal` | mcp/tests/test_store_scaling_cs6.py:80-80 |

## Cross-Repo References

No cross-repository implementation source governs this test module.

## PDLS Reconciliation

Store-scaling forcing now accounts for enclosure-local journal and projection-store ownership without changing scaling bounds.

The test continues to exercise production-owned behavior. No diagnostic result is treated as
certifying evidence and no fallback or threshold exception was introduced.

## Update History

- 2026-08-25T15:44+02:00 — PDLS whole-system reconciliation updated the implementation summary
  above after source and requirement review. Verification remains closeout-owned.

- 2026-08-11T19:58+02:00 — Reconciled `test_store_scaling_cs6.py` with its current structural task/seat, tool-vocabulary, or quality-boundary regression contract and removed stale exact-id/leaf implications where present.
- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B22 curator: replaced the `n/a` table rows and
  the history `_scaling.py`/`compact_workspace_river` citations with exact anchors and
  fixer-generated ranges; exact non-fixing check returns zero findings.

- 2026-07-31T16:50+02:00 — 260731-EFA-L2 code-quality gate: the store entry points this suite
  drives moved their loose keywords into parameter objects
  (`AgentNotifierSignalKey`/`AgentNotifierSignalTarget` for `in_cooldown`,
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
