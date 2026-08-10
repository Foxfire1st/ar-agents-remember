# mcp/tests/test_pi_rpc_real_smoke.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/tests/test_pi_rpc_real_smoke.py`      |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-07T22:45:00+02:00               |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb` |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Opt-in isolated smoke against the pinned real Pi RPC npm package. Three tests, all behind
`@pytest.mark.ar_run_pi_rpc_smoke` on `PiRpcRealSmokeTests`:

1. `test_pinned_isolated_install_reaches_get_state_ready` — a pinned install launched
   through the real adapter reaches `control="ready"` / `activity="idle"` with a vendor
   session id and `raw["vendorProtocol"] == "pi-rpc/jsonl"`.
2. `test_committed_capability_fixture_still_describes_the_installed_runtime` — re-verifies
   the capability recording against a Pi it installs and drives.
3. `test_installed_guard_rejects_stale_idle_without_native_queueing` — holds a real
   provider stream open (a local HTTP handler that answers the opening chunk and then
   blocks) and proves a second prompt cannot slip past the busy guard, emitting zero
   candidate bytes.

260731-EFA-L7 (trace delta): the live Pi RPC smoke suite is environment-gated (`AR_RUN_PI_RPC_SMOKE=1`); its helpers carry per-function R10 pragmas.
## The Version Pin

`PI_RPC_VERSION = "0.80.7"` is the single source of the pin in this module and must match
what the product pins (`mcp/native_helpers/conversation_library/package.json` and the
native flag contract in `serving/pi_rpc_adapter.py`). A smoke test that installs a
different build proves the adapter works against a runtime nobody ships.

`install_pinned_pi` is the module's **only** install path, deliberately: a second one could
drift to a different build and quietly re-validate the wrong runtime. It runs
`npm install --prefix … --no-save <pkg>@PI_RPC_VERSION` into a temporary prefix with an
isolated `HOME` and npm cache, and never touches global Pi/npm state.

## The Capability Recording

`CAPABILITY_FIXTURE = FIXTURES / f"{PI_RPC_VERSION}-capabilities.json"` — the recording is
addressed by the pin, never by a literal. That naming is the anti-drift mechanism: bump the
pin without re-recording and the path does not exist, so
`test_pi_rpc_adapter.py` fails **offline** with `FileNotFoundError` rather than this
network-gated module silently re-validating a build nobody ships. See the fixture's own
card for the full contract, including the "exactly one `*-capabilities.json`" assertion.

`test_committed_capability_fixture_still_describes_the_installed_runtime` asserts, against
a live install driven by `_pi_rpc_capabilities.observe_capabilities`:

- `schema`, `package` and `version` agree with `CAPABILITY_SCHEMA`, `PI_RPC_PACKAGE` and
  `PI_RPC_VERSION`;
- `launch` equals the argv `pi_rpc_launch` really builds (via `_rpc_launch_argv`), so the
  recording cannot describe a launch the adapter no longer performs;
- `unknown_command_rejected` — without this the "every recorded command was accepted"
  result would prove nothing;
- `framing`, `commands`, `dialogMethods`, `fireAndForgetMethods` — **exact** equality;
- `stateFields` and `events` — **subset** (`assertLessEqual`). Pi may report more than the
  adapter reads; it may not stop reporting something the adapter depends on.

## Invariants And Boundaries

- Installation is isolated (temporary prefix, HOME, npm cache, `PI_CODING_AGENT_DIR`) and
  never changes global Pi/tool state.
- The whole module skips unless the `ar_run_pi_rpc_smoke` marker is selected; the runner
  entry lives in `scripts/run-gated-integration.py` and is asserted reachable by
  `test_gated_integration_runner.py`.
- Provider traffic is either the discard port or a local blocking HTTP handler — no
  credential and no provider account is ever required.
- Exact installed-version facts are evidence, never generic protocol authority: production
  compatibility comes from the structured RPC exchange.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Real adapter and launch path under test. | "class PiRpcAdapter:", "transport_factory: TransportFactory = PiRpcSubprocess" | mcp/src/agents_remember/serving/pi_rpc_adapter.py:94-768; mcp/src/agents_remember/serving/pi_rpc_process.py:43-287 |
| The recording this module re-verifies. | "0.80.7" | mcp/tests/fixtures/pi_rpc/0.80.7-capabilities.json:4-4 |
| Produces the observation compared against the recording. | `observe_capabilities` | mcp/tests/_pi_rpc_capabilities.py:431-473 |
| Imports `PI_RPC_VERSION` and enforces the one-recording rule offline. | `CAPABILITY_FIXTURE`, `PI_RPC_VERSION` | mcp/tests/test_pi_rpc_real_smoke.py:44-44; mcp/tests/test_pi_rpc_real_smoke.py:51-51 |
| Proves this marker is applied and reachable from the gated runner. | "ar_run_pi_rpc_smoke" | scripts/run-gated-integration.py:79-79 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-07T23:35:00+02:00 — 260731-EFA-L7 curator (trace delta): body verified against the current code and updated (260731-EFA-L7 (trace delta): the live Pi RPC smoke suite is environment-gated (`AR_RUN_PI_RPC_SMOKE=...). Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: this test module was split in place into a family under 1,200 lines (L7-R5); the card remains the family entry point and the name set was reconciled item for item. Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.

- 2026-08-03T04:32:19+02:00 — W3-B08 curator: curated 12 citations (citation_anchor_missing=6, citation_prose_not_in_cit_form=0, citation_source_malformed=6); final scoped citation check clean.
- 2026-07-31T15:32+02:00 — 260731-EFA-L2 curator: rewritten. The module now installs
  0.80.7 (the previous card still said 0.80.6 in Purpose and Code Commentary), owns a
  single install path, and re-records the capability fixture from a live probe instead of
  pinning a hand-maintained policy file. Recorded the version-addressed fixture contract
  and the exact-vs-subset assertion split. Verification metadata is pinned to the leaf's
  reformat commit until closeout stamps the code commit.
- 2026-07-17T21:39+02:00 — FEUI-L5: updated installed evidence to Pi 0.80.7 and added
  zero-byte/no-native-queue guarded-write smoke coverage.
- 2026-07-14T16:30:00+02:00 — 260713-PHA-L6 curator: marked the exact Pi smoke version as
  fixture-only evidence.
- 2026-07-14T12:17+02:00 — 260713-PHA-L4 curator: created onboarding for the isolated
  pinned real-Pi readiness smoke and global-tool isolation boundary.
