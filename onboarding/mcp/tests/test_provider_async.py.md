# test_provider_async.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_provider_async.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-08-24T00:51+02:00 |
| lastVerifiedCommitHash | `1d446724d099517f6f52d596b47827ae2391a2a4` |
| lastVerifiedCommitDate | 2026-08-24T00:21:10+02:00 |
| governingOverview      | `../overview.md`                              |

## Purpose

Behavior coverage for the GitHub #53 async worktree provider setup: the
launcher thread, status projections, start ordering, retry path, application entry point
settings ownership, and the teardown guards.

## Code Commentary

### Logic

`make_contract` builds a real committed Git repository under the temp root, installs
`refs/remotes/origin/main` plus symbolic `origin/HEAD` as exact default-branch authority, and uses
its real base commit in the disabled-memory `default_contract`;
`CapturedThreads` is a `thread_factory` seam that records spawned threads so
tests can join them deterministically.

Since 260731-EFA-L2 both constructions this suite drives take parameter objects.
`default_contract` is called as
`default_contract(ContractTask(...), leaf=LeafIdentity(...), code=RepoBranchPlan(...),
memory=RepoBranchPlan(...))` instead of fourteen loose keywords — note the disabled-memory
case still passes an all-empty memory plan and needs a `# type: ignore[arg-type]` because
`RepoBranchPlan.repo_path` is not optional. `launch_provider_setup` takes a
`ProviderSetupJob(request, contract, write_state_file, settings_cleanup)` in its first
positional slot — the four values the daemon thread closes over, which it cannot be started
with a subset of — while `runner` and `thread_factory` remain the keyword-only injection
seams. The start-ordering assertion reads the transferred cleanup path off
`launch_mock.call_args.args[0].settings_cleanup` accordingly, where it previously read
`call_args.kwargs["settings_cleanup"]`.

Launcher tests inject a fake `runner`:
success writes the state file, records `providerStateFile` in the finish
summary, and unlinks the temp settings file from the thread; a failed payload
finishes `failed` without a state file; a raising runner finishes `failed`
with the typed error and still unlinks settings. `ProviderSetupStatusTests` cover
None (no progress, no state file), legacy `prepared`, and the failed-state
`retryArgs` (worktree_name from `code_worktree.name`).

`test_a_prepared_stack_reaches_the_status_payload` closes the gap those three leave: they prove
`provider_setup_status` **computes** a projection, not that it reaches the wire. It calls
`guidance.projected_status_payload(contract, landing=None)` twice against the same contract —
before the state file exists, asserting `"providers"` is `assertNotIn` the payload, then after
writing `<worktree_group>/provider-runtime/provider-state.json`, asserting
`payload.get("providers") == {"state": "prepared"}`. The absence half is the assertion that
carries the weight: `providers` is a `NotRequired` key on `WorktreeStatusFacts`, attached by
`_status_payload_with_landing` only `if providers is not None`, cit:([`_status_payload_with_landing`], mcp/src/agents_remember/worktrees/modules/guidance.py:372-421), so a projection that always
emitted an empty value would pass the presence half alone. This is the only test in the suite
that reads the composed status payload rather than the projector in isolation.

`StartOrderingTests` pins the GitHub #53 core: with the extracted start-contract builder mocked,
the contract file must exist on disk at the moment `run_or_launch_provider_setup`
is invoked, and the started payload carries providers `starting` plus the
background summary. Dry-run stays synchronous (`planned`, launcher never
called), and the settings path transfers to the launcher only when
`unlink_settings_after_setup` is set. Retry tests: refusal (exit 2, poll hint)
while `provider_setup_running` is True; relaunch returning
`provider-setup-retried` otherwise. `_settings_owned_by_background` is pinned
for starting/planned/non-dict/None results. Guard tests: cleanup blocks (exit
2) while setup runs; abandon blocks without `force` with the force hint.

### Invariants And Boundaries

- No real provider setup runs: the launcher's `runner`/`thread_factory` seams
  and `mock.patch.object` on module attributes keep everything side-effect
  free.
- Thread joins are bounded (10s) and assert completion — no sleeps, no flaky
  timing.

## Docs References

No external documentation is needed for these standard-library unit tests.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Launcher and projections under test. | `ProviderSetupJob`, `launch_provider_setup`, `provider_setup_status`, `provider_setup_running` | mcp/src/agents_remember/application/provider_runtime.py:59-70; mcp/src/agents_remember/application/provider_runtime.py:73-121; mcp/src/agents_remember/application/provider_runtime.py:124-147; mcp/src/agents_remember/application/provider_runtime.py:150-155 |
| `projected_status_payload` and the `NotRequired` `providers` key on `WorktreeStatusFacts` the new payload test pins. | `WorktreeStatusFacts`, `projected_status_payload`, `_status_payload_with_landing` | mcp/src/agents_remember/worktrees/modules/guidance.py:85-123; mcp/src/agents_remember/worktrees/modules/guidance.py:399-451; mcp/src/agents_remember/worktrees/modules/guidance.py:454-458 |
| Start ordering and retry path under test. | `start_result`, `run_or_launch_provider_setup`, `_retry_provider_setup_result` | mcp/src/agents_remember/worktrees/modules/start.py:414-425; mcp/src/agents_remember/worktrees/modules/start.py:622-659; mcp/src/agents_remember/worktrees/modules/start.py:662-695 |
| Application-layer ownership helper under test. | `worktree_start_tool`, `_settings_owned_by_background` | mcp/src/agents_remember/application/worktree_tools.py:108-205; mcp/src/agents_remember/application/worktree_tools.py:208-213 |

## L23 Start-Ordering Isolation

The provider-start ordering case marks parent lineage non-applicable so it can
continue measuring provider sequencing. Dedicated source-lineage suites own the
new structural gate.

## 260821-CLIVE-L2 Terminal Gate Ordering

Cleanup and abandon provider-running tests explicitly permit the future L5 archive gate so their
assertions still isolate the provider teardown guard beneath it. The production terminal owners
remain fail-closed when archive proof is unavailable.

| Finding | Source |
| --- | --- |
| Cleanup and abandon each patch only their terminal archive gate while testing the provider-running refusal. | mcp/tests/test_provider_async.py:437-470 |

## Update History

- 2026-08-24T00:51+02:00 — 260821-CLIVE-L2: reconciled the L2 test boundary represented by the changed source. Verified at code commit `1d446724`.

- 2026-08-16T04:30+02:00 — No content impact: accepted Ruff's one-line formatting for the typed sprint execution-graph node list; fixture facts and provider lifecycle assertions are unchanged.
- 2026-08-16T04:06+02:00 — 260815-DAG-L4 Dagger repair: the provider lifecycle fixture now creates a real organizational master, sprint graph, direct-super leaf document, exact leaf id, and remote-default authority before exercising asynchronous start and terminal routes.
- 2026-08-16T02:51+02:00 — L4 configured repository authority: upgraded the async provider fixture
  from placeholder repository facts to a real committed repo with exact remote default authority,
  preserving the provider launch/status assertions while reaching the strengthened boundary.
- 2026-08-12T20:10+02:00 — L23 curator: documented bounded lineage isolation in provider-order coverage; verification remains closeout-owned.
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-02T21:57:37+02:00 — W2-B03 curator ownership correction: resolved 9 citation findings on the manifest-owned test card (`mcp/tests/test_provider_async.py.md`); scoped recheck passed with 0 findings. Verification metadata unchanged.
- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-01T09:24+02:00 — 260731-EFA-L4 curator: `ProviderSetupStatusTests` gained
  cit:([`test_a_prepared_stack_reaches_the_status_payload`], mcp/tests/test_provider_async.py:234-247) and the suite gained a
  `from ...modules.guidance import projected_status_payload` import; the card listed the three
  older projection cases as the whole of that class, so it was incomplete. Documented what the new
  case adds — it is the only test here that drives the composed payload rather than
  `provider_setup_status` alone, and its `assertNotIn("providers", ...)` half is what makes the
  `NotRequired` key meaningful. Verified against `worktrees/modules/guidance.py`:
  `projected_status_payload`, `providers: NotRequired[dict[str, Any]]` on
  `WorktreeStatusFacts`, and the `if providers is not None` attach in
  `_status_payload_with_landing`, cit:([`_status_payload_with_landing`], mcp/src/agents_remember/worktrees/modules/guidance.py:372-421); added the `guidance.py` reference row that the card
  previously lacked despite now importing from it. Re-read the rest of the card against the current
  409-line file — the `ProviderSetupJob` positional slot, the keyword-only `runner`/`thread_factory`
  seams, `call_args.args[0].settings_cleanup`, the disabled-memory `make_contract`, the dry-run and
  retry/teardown guards all still hold; now 15 tests across 6 test classes plus `CapturedThreads`.

- 2026-07-31T16:50+02:00 — 260731-EFA-L2 curator: recorded the parameter-object call shapes the
  `PLR0913` pass introduced here, since the card describes the launcher's seams closely enough that
  the old shape would mislead a reader reconstructing the call. `launch_provider_setup` now takes a
  `ProviderSetupJob` positionally, keeping `runner` and `thread_factory` keyword-only, and
  `default_contract` takes `ContractTask` plus keyword-only `LeafIdentity` and two `RepoBranchPlan`
  values in place of fourteen keywords. The start-ordering test reads the transferred settings path
  off `call_args.args[0].settings_cleanup` rather than `call_args.kwargs["settings_cleanup"]`, which
  is the same assertion against the same expected value. The rest of the diff is `ruff format`
  rejoining eight wrapped calls. Every behavioural claim was re-read against the current file and
  still holds: the contract is still disabled-memory, the success path still writes the state file
  and unlinks settings from the thread, the failed and raising paths still finish `failed`, the
  contract still exists on disk when `run_or_launch_provider_setup` is invoked, dry-run is still
  synchronous, and the retry and teardown guards still return exit 2 with their hints. This card
  carries no line citations, so nothing needed re-anchoring. Verification metadata stays pinned
  until closeout stamps the code commit.

- 2026-07-07T23:30+02:00 — 260707-HFX-L4: updated the start-ordering mock target to the extracted
  `build_start_contract` call site after contract construction moved out of `start.py`. Verification
  metadata pinned until closeout stamps the 260707-HFX-L4 commit.
- 2026-06-10T07:30+02:00 — Created with the GitHub #53 async provider setup.
