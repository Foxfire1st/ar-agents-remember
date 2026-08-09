# mcp/tests/test_facade_surface.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_facade_surface.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-09T01:21+02:00                                            |
| lastVerifiedCommitHash | `2dea095cd68454a7a68893e37c07dbd8daa86d32`                                        |
| lastVerifiedCommitDate | 2026-08-09T18:00:39+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Mechanical facade-surface pin (260731-EFA-L7 F1 / reviewer CS-6): every split facade must keep the base module's top-level names importable. The base is the L16-synced commit `a3e43cb`; the pin reads the base file from git and compares against the imported facade, so a missing name is a blocking finding even when no in-repo consumer references it yet.

## Code Commentary

- `FACADES` — the eight split facades under pin (`snapshots`, `reducer`, `agentic_settings`, `projectors.codex`, `harness_control_client`, `serving.app`, `serving.agent_notifier`, `serving.conversation.models`).
- Reads each base file at `BASE_COMMIT` via git, imports the current facade, and asserts every base top-level public name (plus private names used as mock-patch targets) is importable from the facade.
- `REMOVED_FACADE_NAMES` (260713-TES-L2) — the pin's deliberate-removal allowlist: the
  `serving.agent_notifier` facade is permitted to drop `_nudge_reason`,
  `evaluate_turn_report_findings`, and `turn_report_path_for_leaf_key`, which the worker→manager
  predicate retirement deleted from the surface. The loop skips a missing name only when it is
  listed for that module, so every other removal still fails the pin.

## Invariants And Boundaries

- R12 ("public surfaces unchanged") is enforced mechanically, not by consumer search: a missing name blocks even with no in-repo consumer.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The pinned base commit. | `BASE_COMMIT` | mcp/tests/test_facade_surface.py:23-23 |

## 260713-TES-L5 Current Delta — L5 Removed Names Pinned

`REMOVED_FACADE_NAMES` grows the L5 intended deletions for
`agents_remember.kernel.agentic_settings` (the whole escalation family: `EscalationSettings`,
`KNOWN_ESCALATION_*`, `DEFAULT_ESCALATION_*`, `DEFAULT_RESPAWN_AFTER_RUNG`,
`_parse_escalation*`, `_parse_respawn_after_rung`) and for
`agents_remember.serving.agent_notifier` (`_auto_nudge`, `_escalate_rung`, `_respawn_suspect`,
`_rung_entry`, `_resolve_ladder_terminal`, `_mark_expectation_missed`,
`_ladder_terminal_and_dead`, `_delivery_failure_still_retrying`, `EscalationSchedule`,
`_INACTIVE_EXPECTATION_KINDS`, `evaluate_escalation_findings`,
`evaluate_expectation_findings`, `evaluate_ladder_terminal_findings`,
`DEFAULT_ESCALATION_*`, `_nudge_reason`).

## Update History

- 2026-08-09T12:08+02:00 — 260713-TES-L5 curator: recorded the L5 additions to
  `REMOVED_FACADE_NAMES` for the settings and notifier facades. Verification metadata pinned
  until closeout stamps the 260713-TES-L5 commit.
- 2026-08-09T01:21+02:00 — 260713-TES-L2 curator: recorded `REMOVED_FACADE_NAMES` — the pin's
  deliberate-removal allowlist for `_nudge_reason`, `evaluate_turn_report_findings`, and
  `turn_report_path_for_leaf_key` from the agent-notifier facade. Verification metadata pinned
  until closeout stamps the 260713-TES-L2 commit.
- 2026-08-08T22:10+02:00 — 260713-TES-L1 completion round (curator): refreshed this sidecar body for the supervisor -> agent-notifier rename (module paths, identifiers, settings keys, wire keys, prose) and the compat seams; verification metadata pinned until closeout stamps the 260713-TES-L1 commit.
- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the surface pin. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
