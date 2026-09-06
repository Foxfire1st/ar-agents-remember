# test_provider_containment.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_provider_containment.py`   |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-09-06T21:45:53+00:00 |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb` |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

Proves that a stale in-memory armed provider snapshot cannot override an unconfigured authority file on disk. The retained case reloads launch authority and observes the veto. Historical benchmark self-arming, setup-lock and metrics-parser claims are no longer tests in this file.

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
| Stale armed snapshot is vetoed by disk | `test_stale_armed_snapshot_is_vetoed_by_disk` | mcp/tests/test_provider_containment.py:52-73 |

## Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external evidence is needed for these assertions. | N/A | N/A |

## Update History

- 2026-09-06T21:45:53+00:00 — Reconciled the retained IAS test/helper population and exact citation ranges, preserving prior history and verification provenance; no tests or review were run.

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-04T08:03:35+02:00 — 260731-EFA-L6 S18-B07 curator: repaired the bounded citation findings from the recovered Avicenna and Kuhn ledgers, splitting or narrowing claims to the frozen source and normalizing scoped citation ranges.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-31T16:50+02:00 — 260731-EFA-L2 curator: the `PLR0913` pass rewrote two call shapes this
  card describes, and this entry records both. `QueryFunnelGateTests` now drives
  `_provider_operation_result(config, ProviderOperation(operation=…, required_provider=…, run=…))`
  — that half of the body was already corrected; completing it here, note the old `launch_capable=`
  boolean has no successor keyword at all, because a `None` `required_provider` is now what marks
  an operation needing no launch authority. The second change had not been recorded: both
  `WorktreeStartVetoTests` cases call
  `worktree_start_tool(config, TaskIdentity(repo_id=…, task_name=…, worktree_name=…))` instead of
  passing those three as keywords, so the card now names `TaskIdentity` where it describes the veto
  and armed-launch paths. Everything else in the diff is `ruff format` reflow — rejoined call
  arguments, the redundant parentheses on the docker `Labels` literal, and the uncontended-lock test
  moving to a parenthesized `with (...)` block, which is the same two context managers in the same
  order. Re-read every remaining claim against the current file: the refusal still raises
  `ConfigError` naming `codegraphcontext-code` with the runner never called, the vetoed run still
  produces no settings file and no `provider_setup_config`, and the fail-closed, lock and metrics
  invariants are untouched. This card's references table carries no line citations, so nothing
  needed re-anchoring. Verification metadata stays pinned until closeout stamps the code commit.

- 2026-07-21T11:30+02:00 — 260718-CHATS-L5F curator: recorded the R6 docker-ps timeout bound in
  `MetricsTests` (`test_sampler_bounds_docker_ps_timeout_into_error_sample`) — a timed-out `docker ps`
  now yields an error-annotated snapshot via `allow_timeout=True` instead of an escaping
  `TimeoutExpired` traceback each sampling interval. Verification metadata stays pinned (uncommitted);
  closeout re-stamps the candidate commit.
- 2026-07-07T17:40+02:00 — 260707-HFX-L1 review fixes: the suite grew `QueryFunnelGateTests`
  (per-provider funnel refusal — armed grepai does not authorize a cgc one-shot), the lock
  host-path pin (`fleet_setup_lock_path()` under the system temp dir) with the explicit
  `lock_path` signature in the lock tests, the benchmark sweep tests
  (narrow/idempotent/None-untouched, review B3), and the fail-closed-`None` + env-escape filter
  tests (review B4). Verification metadata pinned until closeout stamps the HFX-L1 commit.
- 2026-07-07T16:30+02:00 — Created for 260707-HFX-L1 (provider containment): pins the authority
  reload fail-closed semantics, the launch-authority refusal/armed paths, the worktree_start
  veto + armed live-map launch, the runtime rebind derivation, the benchmark manifest filter,
  the fleet setup lock contention/timeout/no-op, and the metrics parsers/sampler/store
  (incl. dockerless and torn-line tolerance). Verification metadata pinned to the branch base
  until closeout stamps the HFX-L1 commit.
