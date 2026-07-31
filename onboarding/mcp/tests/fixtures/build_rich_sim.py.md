# mcp/tests/fixtures/build_rich_sim.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/fixtures/build_rich_sim.py`           |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-06T10:30+02:00                           |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d`       |
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
| governingOverview      | `../../overview.md`                              |

## Governing Overview

[mcp overview](../../overview.md)

## Purpose

`build_rich_sim.py` generates a **rich sim fixture** for stress-testing the cockpit against the full
Agents Remember domain (slice 5c). The shipped `mcp/tests/fixtures/sim` fixture is one lifecycle;
this script writes a mini coordination root with 30+ lifecycles in variation so the UI is exercised
at real scale — run it, then `... dashboard --sim <out_dir>`.

## Code Commentary

`main(out)` clears the output dir and then calls six named writers in order —
`write_paused_lifecycles`, `write_master_series`, `write_event_backed_lifecycles`,
`write_provider_state`, `write_memory_ledgers_and_drift`, `validate_and_report` — which between
them produce the coordination tree: ~26 worktree contracts (→ paused persistent lifecycles via
the reducer's synthesis, with varied closeout/integration/cleanup), a multi-task `master` series
(master doc + `subTask` slices), ~8 event-backed lifecycle logs (running across phases, blocked
gates, fleeting, completed), light + subTask task documents carrying real content
(objective / requirements / design / steps+substeps / codeExamples / decisions / references), a
workspace provider `current.json`, per-worktree `provider-runtime/provider-state.json` stacks, memory
ledgers, and drift snapshots. `validate_and_report` is the self-check: it `load_contract`s every
contract and `TaskDocument.model_validate`s every doc, then prints the contract/doc/event-log
counts (reading the log dir through the shared `lifecycle_logs_root` helper).

Four frozen dataclasses carry what used to be loose argument runs, and they are the vocabulary the
writers speak:

- `ContractSite(root, repo, task, contract_kind="leaf", leaf_id=None)` is one contract's address.
  Its properties derive every path a contract records — `is_series`, `leaf`, `group`, `task_root`,
  `group_root`, `contract_path`, `worktree_group`, `code_worktree`, `memory_worktree` — so the
  builder that writes a contract, the one that stats its path, and the one that materializes its
  worktrees cannot disagree about where a leaf lives. It replaced the old free `contract_path()`
  function, which is gone.
- `ContractStatus(review, closeout, integration, cleanup)` is one position on the
  review → closeout → integration → cleanup path, varied as whole named states; the module-level
  `AWAITING_INTEGRATION` is the default (approved + completed closeout, not yet integrated or
  cleaned up).
- `Progress(done, total)` travels as a pair through every doc builder that renders steps, with
  `complete` (`done >= total`) deciding Completed.
- `SeriesSlice(master_slug, number, name, progress)` is one numbered slice of the master series;
  `label`, `status`, and `master_reference()` mean the master's subTask rows and each subTask doc
  are read off the same objects.

Helpers emit each surface in its on-disk format: `contract_md(site, *, lifecycle_id, kind, status)`,
`materialize_worktrees(site)`, `steps(progress, current_in_progress)`,
`light_doc(repo, task, lc, *, status, progress)`, `subtask_doc(repo, slice_, lc)`, plus the
unchanged `master_doc`, `event`, `ledger_md`, and `drift_snapshot`. Since the L11 review (L11R-1)
the builder also MATERIALIZES the worktree directories its live contracts record —
`materialize_worktrees` creates the site's code and memory dirs for every `cleanup: pending` leaf
(plus the series repo checkout dir), while landed/abandoned leaves stay dir-less so the hidden
states keep being exercised; without the dirs a `serve --sim` replay renders an empty Hangar under
the physical-existence rule. `serving.sim._materialize_surfaces` copies these surfaces into the sim
root and replays the event logs, so the rich fixture exercises the whole projection.

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

- 2026-07-31T16:50+02:00 — 260731-EFA-L2 curator: rewrote the Code Commentary to match the
  generator's decomposition. `main` no longer contains the tree-writing logic; it now sequences six
  named writers (`write_paused_lifecycles`, `write_master_series`, `write_event_backed_lifecycles`,
  `write_provider_state`, `write_memory_ledgers_and_drift`, `validate_and_report`), with
  `lifecycle_logs_root` shared between two of them. Four frozen dataclasses replaced the long
  argument runs and are now documented by name: `ContractSite` (which absorbed and deleted the free
  `contract_path()` function and owns every derived path), `ContractStatus` with its
  `AWAITING_INTEGRATION` default, `Progress`, and `SeriesSlice`. Updated the helper signatures the
  card lists — `contract_md(site, ...)`, `materialize_worktrees(site)`, `steps(progress, ...)`,
  `light_doc(..., progress=...)`, `subtask_doc(repo, slice_, lc)` — and noted that `master_doc`,
  `event`, `ledger_md`, and `drift_snapshot` are unchanged. The generated tree, the L11R-1
  worktree materialization rule, and the self-validation invariant are all behaviourally identical.
  Verification metadata stays pinned until closeout stamps the candidate commit.

- 2026-07-06T10:30+02:00 — L11 adversarial-review follow-up (L11R-1): materialize_worktrees creates recorded worktree dirs for live leaves (+ series repo dir); regression test at mcp/tests/test_sim_fixture_builder.py. Verification metadata pinned until closeout stamps the L11 commit.

- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: the rich simulation generator now emits `ar-series-contract/v1` root/leaf contracts, leaf enclosure paths, and task docs/projections compatible with the new dashboard identity fields. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-14T23:30+02:00: Created for slice 05 (5c) — the rich sim fixture generator (30+ lifecycles, single + multi task content, per-worktree providers, ledgers, drift) for cockpit stress-testing. Verification metadata pinned until closeout stamps the 5c code commit.
