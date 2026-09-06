# mcp/tests/test_spawn_agent_session.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_spawn_agent_session.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T21:45:53+00:00 |
| lastVerifiedCommitHash | `f2b7c648f540efb9d64ceea22e11e651cb5cc914` |
| lastVerifiedCommitDate | 2026-08-31T15:32:32+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

Exercises the internal spawn primitive with a fake terminal host and real temporary catalog/task lineage. It creates a bound but explicitly unbriefed seat, preserves existing ownership on seat-taken refusal, and rejects forged structural parent provenance before host creation. Public dispatch remains responsible for the separate durable briefing transaction; no readiness or submitted-brief claim is fabricated.

## Code Commentary

### Logic

The current evidence boundary is the source-listed behavior below. Earlier coverage claims in
history describe prior populations and must not be used to recreate removed tests or claim they
still run. The retained behavior and its fixture limits, described above, govern this card.

### Conventions

The table lists retained test definitions, not collected parametrized or subtest counts.
Inspect the cited setup and collaborators before treating a focused result as end-to-end evidence.

### Invariants And Boundaries

Preserve exact refusal, identity, and cleanup assertions rather than adding overlapping helper
cases. Coverage percentages are diagnostic and production CRAP 20 prompts review; neither implies
an obligation to restore removed cases. Full suites and whole-candidate review remain master-end
work. This source inspection does not claim a newly executed test or acceptance result.

### Todos

No additional implementation scope is opened by this memory reconciliation.

## Docs References

The repository has no configured Domain Documentation source. These claims concern its own test
fixtures and assertions, so the exact retained source is the direct evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain claim is required. | N/A | N/A |

## Repo-Internal References

Each current definition below can be inspected in the exact source file. Historical references
to removed methods are superseded by this current inventory.

| Finding | Anchor | Source |
| --- | --- | --- |
| Spawns bound seat without brief or readiness claim | `test_spawns_bound_seat_without_brief_or_readiness_claim` | mcp/tests/test_spawn_agent_session.py:311-332 |
| Seat taken is surfaced never overridden | `test_seat_taken_is_surfaced_never_overridden` | mcp/tests/test_spawn_agent_session.py:334-368 |
| Spawn refuses forged structural parent before host creation | `test_spawn_refuses_forged_structural_parent_before_host_creation` | mcp/tests/test_spawn_agent_session.py:370-381 |

## Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external evidence is needed for these assertions. | N/A | N/A |

## Update History

- 2026-09-06T21:45:53+00:00 — Reconciled the retained IAS test/helper population and exact citation ranges, preserving prior history and verification provenance; no tests or review were run.


- 2026-08-31T12:00+02:00 — A005 repair aligned reviewer fixtures with mandatory explicit parent
  provenance and settings ownership while preserving stale-lineage as the first actionable refusal.
  Verification remains closeout-owned.

- 2026-08-31T09:02+02:00 — 260821-ARSPAWN-L5 A005 citation reconciliation refreshed
  source ranges after the reviewed spawn suite moved; no semantic onboarding claim changed.
  Verification remains closeout-owned.

- 2026-08-30T13:59+02:00 — 260821-ARSPAWN-L3 replaced the stale low-level brief-delivery recipe
  assertion with forcing proof that the internal primitive refuses before side effects and directs
  callers to the one public `dispatch_agent` transaction. Verification remains closeout-owned.

- 2026-08-21T02:50+02:00 — 260821-ARSPAWN-L1: `_SPAWNED_BY_FIELDS` + `test_spawn_records_caller_kind_provenance` prove the real primitive writes the `spawnedByKind` payload and the catalog caller-kind row. Verification metadata pinned until closeout stamps the 260821-ARSPAWN-L1 commit.

- 2026-08-16T04:06+02:00 — Dagger fixture repair: stale-lineage session forcing advances the exact sprint-super ref, then restores the ambient main checkout before role launch.
- 2026-08-13T12:53+02:00 — No content impact: the stabilized daemon-root derivation reads
  `sys.modules["agents_remember"].__file__` after normal package submodule imports. Spawn and
  all-leaf-role lineage assertions are unchanged, and no Ruff config exception remains. This
  supersedes the 12:26 import-shape note; provenance stays closeout-owned.

- 2026-08-13T12:26+02:00 — No content impact: the final Ruff-safe form imports
  `agents_remember.__file__` directly as `agents_remember_file` when deriving the same daemon
  package root. The already-documented all-leaf-role lineage refusal and every spawn assertion are
  unchanged; verification provenance remains closeout-owned.
- 2026-08-13T08:47+02:00 — L23 integration-gate repair: expanded the pre-host stale-super refusal across worker, reviewer, and curator, proving curator dispatch cannot create a process after lineage moves. Verification metadata remains closeout-owned.

- 2026-08-12T20:10+02:00 — L23 curator: documented real-Git pre-host lineage refusal coverage; verification remains closeout-owned.

- 2026-08-12T08:41+02:00 — No content impact: 260731-EFA-L20 removed redundant task-reference inference from the helper whose callers already supply canonical references; spawn behavior and assertions are unchanged.
- 2026-08-11T12:15+02:00 — Reframed the suite around the current trusted spawn primitive,
  task-document binding, and separate exact-pinned brief delivery. Verification remains pinned
  pending governed closeout.
- 2026-07-04T11:10+02:00 — Through 2026-08-08, coverage accumulated for settings-owned launch selection,
  capture/log evidence, binding conflicts, role provenance, plain terminals, and typed helpers.
