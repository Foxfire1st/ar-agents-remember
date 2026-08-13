# mcp/tests/test_harness_control_claude_stream_2.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_harness_control_claude_stream_2.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-12T23:08+02:00                                            |
| lastVerifiedCommitHash | `1580f92715ff93c988f9a15439ad9bec60ef4c5d`                                        |
| lastVerifiedCommitDate | 2026-08-13T00:18:59+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Part of the Claude stream-json adapter regression family. It covers model-set
acceptance, replay/tombstone recovery, selector evidence, and clean retry behavior
through the fake transport owned by `ClaudeStreamJsonAdapterTests2`.

## Code Commentary

`ClaudeStreamJsonAdapterTests2` distinguishes acceptance evidence from eventual
terminal results. `test_set_timeout_neutralizes_late_replay_before_a_clean_retry`
compresses the production 30-second acceptance boundary to 50ms in the test-only
`ClaudeAdapterLimits`: long enough for a loaded xdist worker's fake reader to consume
the replay and result frames, while still forcing the first operation to expire. The
test then proves the expired replay does not promote model state or admit a concurrent
second set, and that a later clean retry is echo-verified. No production timeout or
adapter behavior changes.

## Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/tests/test_harness_control_claude_stream_2.py`.
- Test-only compressed limits must preserve the protocol ordering being tested; they
  must not be so short that event-loop scheduling, rather than adapter semantics,
  decides whether replay/result frames are consumed.
- Production acceptance remains 30 seconds; the 50ms value exists only in this fake-
  transport regression.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module. | — | — |

## Update History

- 2026-08-12T23:08+02:00 — 260731-EFA-L23 Dagger flaky-test follow-up: raised only the late-replay regression's compressed acceptance timeout from 5ms to 50ms so loaded xdist scheduling cannot pre-empt the fake reader's replay/result consumption. Production remains 30 seconds. Evidence: 1/100 failure before plus one Dagger gw16 failure; 100/100 one-process repetitions after, with exact-file Ruff clean. Verification remains closeout-owned.
- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
