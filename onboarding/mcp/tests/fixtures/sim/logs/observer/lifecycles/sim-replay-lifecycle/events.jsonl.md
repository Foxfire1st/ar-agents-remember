# mcp/tests/fixtures/sim/logs/observer/lifecycles/sim-replay-lifecycle/events.jsonl

| Field                  | Value                                                                          |
| ---------------------- | ------------------------------------------------------------------------------ |
| repository             | agents-remember                                                                |
| path                   | `mcp/tests/fixtures/sim/logs/observer/lifecycles/sim-replay-lifecycle/events.jsonl` |
| doc_type               | `file-level-onboarding`                                                        |
| lastUpdated            | 2026-07-31T15:32+02:00                                                         |
| lastVerifiedCommitHash | `b252c42cca200933d5c9c36e26de47a526a569ce`                                     |
| lastVerifiedCommitDate | 2026-08-07T23:58:52+02:00|
| governingOverview      | `../../../../../../overview.md`                                                |

## Governing Overview

[mcp/tests overview](../../../../../../overview.md)

## Purpose

One simulated observer lifecycle event river, replayable by the projection. Eight ordered
records (`sim-e1` … `sim-e8`) for `lifecycleId: "sim-replay-lifecycle"`, covering
`lifecycle.started` (fleeting, phase `request`), `lifecycle.promoted` (trust `approved`,
actor `developer`, with `enclosure` and `repoId`), `lifecycle.phase-changed`,
`tool.completed`, `lifecycle.blocked` and the records that follow.

Its point is the **trust and actor ladder**: the same river carries `observed`, `declared`
and `approved` records from `system`, `model` and `developer`, so a projection that
collapsed trust levels or attributed a developer promotion to the model is visible.

## Consumers

Read by the serving projection; `test_serving.py` asserts the projected lifecycle id is
`sim-replay-lifecycle`.

## Invariants And Boundaries

- Fixture data for a simulated workspace, never production evidence and never a capability
  enabler.
- Records are ordered and ids are stable; the projection's replay assertions depend on both.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The projection assertions that read this fixture. | `SimFixtureTests`; `SimReplayTests` | mcp/tests/test_serving_cli.py:313-338; mcp/tests/test_serving_cli.py:341-405 |



## Update History

- 2026-08-04T13:15:12+02:00 — 260731-EFA-L6 S18-B02 curator: removed the false current-builder ownership and regeneration statements, retaining the source-clear projection-test consumer claim.

- 2026-07-31T15:32+02:00 — 260731-EFA-L2 curator: created the missing sidecar for this
  fixture (a pre-existing 1:1 gap, not introduced by this leaf).
