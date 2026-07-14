# mcp/tests/test_pi_rpc_real_smoke.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_pi_rpc_real_smoke.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-14T12:17+02:00 |
| lastVerifiedCommitHash | `d5f8edf0ccab21f1cf71723615e394eba40fcebc` |
| lastVerifiedCommitDate | 2026-07-14T12:29:36+02:00 |
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

## Repo-Internal References
| Finding | Source Path |
| --- | --- |
| Real adapter and launch path. | [pi_rpc_adapter.py](../src/agents_remember/serving/pi_rpc_adapter.py), [pi_rpc_process.py](../src/agents_remember/serving/pi_rpc_process.py) |
| Pinned capability policy. | [0.80.6-capabilities.json](fixtures/pi_rpc/0.80.6-capabilities.json) |

## Cross-Repo References
| Finding | Source Path |
| --- | --- |
| Real package RPC documentation. | [Pi RPC](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/rpc.md) |

## Update History
- 2026-07-14T12:17+02:00 — 260713-PHA-L4 curator: created onboarding for the isolated pinned
  real-Pi readiness smoke and global-tool isolation boundary.
