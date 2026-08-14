# mcp/tests/test_harness_control_ipc.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_harness_control_ipc.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-07T22:45:00+02:00                                            |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`                                        |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Part of the 260731-EFA-L7 in-place split family for `test_harness_control_ipc.py`'s source module; covers the behaviours named by its test classes.

## Code Commentary

- `HarnessControlIpcTests`
- The duplicate-submit synchronization case waits up to five seconds for both the first submit to
  enter the adapter and the duplicate request to return. The adapter remains explicitly blocked
  until the duplicate result is observed, so the larger test-only margin removes loaded-xdist
  scheduling sensitivity without weakening the single-flight assertion.

## Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/tests/test_harness_control_ipc.py`.
- IPC duplicate-submit semantics remain deterministic: the duplicate must be rejected before the
  held first submit is released; the five-second value is only an outer failure timeout.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module. | — | — |

## Update History

- 2026-08-13T13:08+02:00 — L23 full-Dagger stability repair: documented the duplicate-submit
  test's five-second synchronization margin; ordering and production IPC behavior are unchanged.
  Verification remains closeout-owned.

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
