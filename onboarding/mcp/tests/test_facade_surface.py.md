# mcp/tests/test_facade_surface.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_facade_surface.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-09T01:21+02:00                                            |
| lastVerifiedCommitHash | `7af76249ff1aa728d34a6e81c5f09c8bcb797484`                                        |
| lastVerifiedCommitDate | 2026-08-09T02:17:45+02:00|
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

## Update History

- 2026-08-09T01:21+02:00 — 260713-TES-L2 curator: recorded `REMOVED_FACADE_NAMES` — the pin's
  deliberate-removal allowlist for `_nudge_reason`, `evaluate_turn_report_findings`, and
  `turn_report_path_for_leaf_key` from the agent-notifier facade. Verification metadata pinned
  until closeout stamps the 260713-TES-L2 commit.
- 2026-08-08T22:10+02:00 — 260713-TES-L1 completion round (curator): refreshed this sidecar body for the supervisor -> agent-notifier rename (module paths, identifiers, settings keys, wire keys, prose) and the compat seams; verification metadata pinned until closeout stamps the 260713-TES-L1 commit.
- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the surface pin. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
