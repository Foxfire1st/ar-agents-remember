# mcp/tests/test_pi_rpc_real_smoke.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_pi_rpc_real_smoke.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-17T21:39+02:00 |
| lastVerifiedCommitHash | `f8196d98982f834d68152d307ff8025ea69440d5` |
| lastVerifiedCommitDate | 2026-07-17T22:08:10+02:00|
| governingOverview | `../overview.md` |

## Governing Overview
[mcp/tests overview](../overview.md)

## Purpose
Opt-in integration smoke for the pinned real Pi 0.80.6 RPC package and readiness path.

## Code Commentary
With `AR_RUN_PI_RPC_SMOKE=1`, the test installs `@earendil-works/pi-coding-agent@0.80.6` into
temporary prefix/HOME/cache locations, launches the real child through RPC, and verifies
`get_state` reaches ready/idle. The normal suite skips this networked smoke.

## Invariants And Boundaries
- Installation is isolated and never changes global Pi/tools state.
- This proves protocol readiness only; production registration/cutover remains L5 scope.

## Docs References

No Domain Documentation source is configured for this repository; repository code and tests are the authority.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured live domain-documentation source was available. | — | — |

## Repo-Internal References
| Finding | Source Path |
| --- | --- |
| Real adapter and launch path. | [pi_rpc_adapter.py](../src/agents_remember/serving/pi_rpc_adapter.py), [pi_rpc_process.py](../src/agents_remember/serving/pi_rpc_process.py) |
| Pinned capability policy. | [0.80.6-capabilities.json](fixtures/pi_rpc/0.80.6-capabilities.json) |

## Cross-Repo References
| Finding | Source Path |
| --- | --- |
| Real package RPC documentation. | [Pi RPC](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/rpc.md) |

## 260713-PHA-L6 Fixture Boundary

The opt-in Pi `0.80.6` real-smoke baseline is non-production evidence only. Production compatibility
comes from the structured RPC exchange and does not require this package version.

## 260715-FEUI-L5 Submission Authority Delta

The installed Pi 0.80.7 smoke proves the stale-guard path emits zero candidate bytes and exposes no
native prompt queue. It records readiness/resource evidence without treating installed-version facts
as generic protocol authority.

## Update History

- 2026-07-17T21:39+02:00 — FEUI-L5: updated installed evidence to Pi 0.80.7 and added zero-byte/
  no-native-queue guarded-write smoke coverage.
- 2026-07-14T16:30:00+02:00 — 260713-PHA-L6 curator: marked the exact Pi smoke version as fixture-only evidence.
- 2026-07-14T12:17+02:00 — 260713-PHA-L4 curator: created onboarding for the isolated pinned
  real-Pi readiness smoke and global-tool isolation boundary.
