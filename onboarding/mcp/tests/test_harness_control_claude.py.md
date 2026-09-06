# mcp/tests/test_harness_control_claude.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_harness_control_claude.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated            | 2026-08-07T22:45:00+02:00               |
| lastVerifiedCommitHash | `25841d0ddc2d93c4950abf097168fa24b220c5ad` |
| lastVerifiedCommitDate | 2026-08-18T11:30:22+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Reusable Claude stream-json fake transport, fixture replay and adapter-operation builders.

## Code Commentary

### Logic

The fake transport queues incoming frames, records writes and launch arguments, invokes the before-write callback before recording a frame, and exposes controlled disconnect/stop. A scripted relaunch drains the stop sentinel and replays the configured startup frames.

Adapter construction injects the transport, fixed clock and correlation sequence. Replay helpers preserve the session while transforming slash-command text to its structured command echo. Setter helpers create a fresh operation reference and preflight it before invoking the adapter. Bounded activity/snapshot waits fail after twenty scheduler yields. The embedded stub speaker supports initialize/model-list responses and emits a deterministic init/result sequence.

### Invariants And Boundaries

This retained module defines support objects and builders; it contains no collected test functions. Its former family-wide coverage narrative is historical. Helper availability is not evidence that a removed scenario still runs.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Fake stream ownership, relaunch frames and write ordering. | "class _FakeClaudeTransport" | mcp/tests/test_harness_control_claude.py:47-118 |
| Adapter dependencies are injected explicitly. | "def _adapter(" | mcp/tests/test_harness_control_claude.py:152-167 |
| Slash-command replay preserves the command/arguments representation. | "def _replay(" | mcp/tests/test_harness_control_claude.py:182-204 |
| Operation identity is unique within the helper sequence. | "def _operation(" | mcp/tests/test_harness_control_claude.py:240-247 |
| Model setters preflight the operation before invocation. | "def _set_model(" | mcp/tests/test_harness_control_claude.py:250-253 |
| Activity waits have a bounded failure path. | "def _wait_for_activity(" | mcp/tests/test_harness_control_claude.py:266-273 |

## Docs References

No external documentation is needed for these source-owned helper facts.

## Cross-Repo References

No separate cross-repository authority is established by this helper module.

## Update History

- 2026-08-18T09:05+02:00 — Renamed the atomic 'barrier' concept to 'blocker' throughout (terminology unification; no behavioral change). Verification remains closeout-owned.

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: this test module was split in place into a family under 1,200 lines (L7-R5); the card remains the family entry point and the name set was reconciled item for item. Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.

- 2026-08-04T13:54+02:00 — 260731-EFA-L6 S18-B13 curator: reissued whole-claim evidence for Claude catalog parsing and native startup frames for same-reviewer closure.

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 3 line citations. In
  `harness_control_claude.py` the startup/discovery/advertisement row moved from L97-L215 to
  L115-L269 (`start` L115-L237 negotiating startup then catalog, `discover` L246-L261 which builds
  the isolated argv and force-stops the probe in its `finally`, `advertise` L262-L269 returning the
  cached snapshot), and the setter row moved from L233-L308; L467-L550 to L287-L396 (`set_model`,
  `set_effort`, `_submit_set_command`, `_selected_model`, `_unsupported_set`) plus L545-L677 (the
  module-level set-result classifiers through `_model_terminal_results` and
  `_resolved_model_terminal_label`). In this suite itself the Fable row moved from L709-L799 to
  L942-L1031 (`test_terminal_refusal_or_non_echo_never_promotes_claude_capability` L942-L965 and
  `test_native_noninteractive_set_blocked_refusal_maps_without_alias_guessing` L966-L1031). Not
  repaired and reported upward instead: the other eight self-citations in this table are stale by
  roughly the same drift and need their own pass.

- 2026-07-31T15:32+02:00 — 260731-EFA-L2 curator: recorded the arms this leaf added; the rest of this card was re-read against the file and remains true. Call sites in this module now build parameter objects (see the route overview) — what the suite proves is unchanged. Verification metadata pinned until closeout stamps the code commit.

- 2026-07-30T15:05+02:00 — 260727-CHATS-IM-L4: recorded `ClaudeProductionTransportRelaunchTests`, the
  real-transport probe/relaunch proof, and named the restart-tolerant fake as the reason the at-floor
  argv case passed over a transport that would have refused its own re-launch.
- 2026-07-26T15:45+02:00 — 260718-CHATS-L7 curator: recorded the `--forward-subagent-text`
  flag-floor coverage (fix-round finding 8) — the fake transport's scripted re-launch
  (`start_argvs`/`restart_frames`), the below-floor one-launch omission with the exact
  `unverified` note, the at-floor probe-then-relaunch flow, and the unparseable-version
  fail-closed case. Verification metadata stays pinned (uncommitted); closeout re-stamps the
  candidate commit.

- 2026-07-24T13:18:47Z — 260718-CHATS-L5I curator: refreshed the regression-coverage record for the current backend/shared behavior and preserved the pre-commit verification stamp.

- 2026-07-17T21:39+02:00 — FEUI-L5: added Claude sole-authority, exact completion, stale-event, and
  bounded-history regression proof.

- 2026-07-16T07:25+02:00 — 260714-ACPUI-L5 test curator: documented discovery-only Claude MCP
  selector isolation across separate, variadic/repeated, equals-attached, and end-of-options forms;
  normal-start argv preservation; the zero-turn fake/live relationship; and the independent marker
  collision closure. Live catalog counts/keys remain observations, not enums. Verification metadata
  remains at the last landed source commit until closeout stamps the uncommitted L5 candidate.
- 2026-07-16T01:21+02:00 — 260714-ACPUI-L3 curator: documented same-session structured setters,
  exact replay plus terminal-echo evidence, model-gated effort, native-result-driven Fable refusal,
  exact dynamic aliases, and cancellation/timeout/duplicate-correlation neutralization. Verification
  metadata remains pinned until closeout stamps the L3 code commit.
- 2026-07-15T23:00+02:00 — 260714-ACPUI-L2 curator: documented expected-launch injection and the
  force-close/propagate behavior that distinguishes an effective model mismatch from protocol
  unsupported. Verification metadata remains pinned until closeout stamps the L2 code commit.

- 2026-07-15T20:05:47+02:00 — 260714-ACPUI-L1 curator: documented the `2.1.210` catalog fixture,
  zero-turn/zero-cost discovery, cached model-gated advertisement, honest unknown effort, modern
  initialize shape, and loud no-fallback catalog failures; corrected the governing overview
  backlink while preserving existing verification metadata.
- 2026-07-14T16:30:00+02:00 — 260713-PHA-L6 curator: recorded structured Claude negotiation and incompatible
  contract coverage.
- 2026-07-14T12:45:11+02:00 — 260713-PHA-L2 source-tip reconciliation: refreshed verification
  metadata to accepted candidate `acb308c50072d8cde0015c4828e39d12480872ed`.
- 2026-07-14T12:30+02:00 — 260713-PHA-L2 curator: created sidecar.
