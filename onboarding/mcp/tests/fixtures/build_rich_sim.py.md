# mcp/tests/fixtures/build_rich_sim.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/fixtures/build_rich_sim.py`           |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-06T10:30+02:00                           |
| lastVerifiedCommitHash | `4cdb1ef68e2c5f661ea11e12d46a68441ef18088`       |
| lastVerifiedCommitDate | 2026-07-06T01:49:54+02:00|
| governingOverview      | `../../overview.md`                              |

## Governing Overview

[mcp overview](../../overview.md)

## Purpose

`build_rich_sim.py` generates a **rich sim fixture** for stress-testing the cockpit against the full
Agents Remember domain (slice 5c). The shipped `mcp/tests/fixtures/sim` fixture is one lifecycle;
this script writes a mini coordination root with 30+ lifecycles in variation so the UI is exercised
at real scale — run it, then `... dashboard --sim <out_dir>`.

## Code Commentary

`main(out)` writes a coordination tree: ~26 worktree contracts (→ paused persistent lifecycles via
the reducer's synthesis, with varied closeout/integration/cleanup), a multi-task `master` series
(master doc + `subTask` slices), ~8 event-backed lifecycle logs (running across phases, blocked
gates, fleeting, completed), light + subTask task documents carrying real content
(objective / requirements / design / steps+substeps / codeExamples / decisions / references), a
workspace provider `current.json`, per-worktree `provider-runtime/provider-state.json` stacks, memory
ledgers, and drift snapshots. Helpers (`contract_md`, `light_doc`, `master_doc`, `subtask_doc`,
`event`, `steps`, `ledger_md`, `drift_snapshot`) emit each surface in its on-disk format; a
self-check `load_contract`s every contract and `TaskDocument.model_validate`s every doc before
finishing. Since the L11 review (L11R-1) the builder also MATERIALIZES the worktree directories its live contracts record — `materialize_worktrees` creates the code and memory dirs for every `cleanup: pending` leaf (plus the series repo checkout dir), while landed/abandoned leaves stay dir-less so the hidden states keep being exercised; without the dirs a `serve --sim` replay renders an empty Hangar under the physical-existence rule. `serving.sim._materialize_surfaces` copies these surfaces into the sim root and replays
the event logs, so the rich fixture exercises the whole projection.

## Invariants And Boundaries

- **Dev/test tooling, not shipped runtime** — a fixture generator; the product never imports it.
- **Deterministic** — fixed timestamps + content, so the generated fixture is reproducible.
- The generated output (`mcp/tests/fixtures/sim-rich/`) is git-ignored; the generator is the source.
- Self-validates every contract + task doc against the real models before writing completes.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The contract format + loader the contracts must satisfy. | [worktrees/worktree_contract.py](agents-remember/mcp/src/agents_remember/worktrees/worktree_contract.py) |
| The task-document schema the docs are validated against. | [tasks/document.py](agents-remember/mcp/src/agents_remember/tasks/document.py) |
| The event envelope the replayed logs use. | [observer/events.py](agents-remember/mcp/src/agents_remember/observer/events.py) |
| The sim loader/materializer that consumes the fixture. | [serving/sim.py](agents-remember/mcp/src/agents_remember/serving/sim.py) |

## Series-Contract Notes

The rich simulator now fabricates root `kind="series"` contracts and leaf enclosure contracts separately, so generated dashboard data exercises the integration-branch/root-task split.

## Update History

- 2026-07-06T10:30+02:00 — L11 adversarial-review follow-up (L11R-1): materialize_worktrees creates recorded worktree dirs for live leaves (+ series repo dir); regression test at mcp/tests/test_sim_fixture_builder.py. Verification metadata pinned until closeout stamps the L11 commit.

- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: the rich simulation generator now emits `ar-series-contract/v1` root/leaf contracts, leaf enclosure paths, and task docs/projections compatible with the new dashboard identity fields. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-14T23:30+02:00: Created for slice 05 (5c) — the rich sim fixture generator (30+ lifecycles, single + multi task content, per-worktree providers, ledgers, drift) for cockpit stress-testing. Verification metadata pinned until closeout stamps the 5c code commit.
