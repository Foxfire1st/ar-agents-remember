# mcp/tests/test_facade_surface.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_facade_surface.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-07T22:45:00+02:00                                            |
| lastVerifiedCommitHash | `b252c42cca200933d5c9c36e26de47a526a569ce`                                        |
| lastVerifiedCommitDate | 2026-08-07T23:58:52+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Mechanical facade-surface pin (260731-EFA-L7 F1 / reviewer CS-6): every split facade must keep the base module's top-level names importable. The base is the L16-synced commit `a3e43cb`; the pin reads the base file from git and compares against the imported facade, so a missing name is a blocking finding even when no in-repo consumer references it yet.

## Code Commentary

- `FACADES` — the eight split facades under pin (`snapshots`, `reducer`, `agentic_settings`, `projectors.codex`, `harness_control_client`, `serving.app`, `serving.supervisor`, `serving.conversation.models`).
- Reads each base file at `BASE_COMMIT` via git, imports the current facade, and asserts every base top-level public name (plus private names used as mock-patch targets) is importable from the facade.

## Invariants And Boundaries

- R12 ("public surfaces unchanged") is enforced mechanically, not by consumer search: a missing name blocks even with no in-repo consumer.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The pinned base commit. | `BASE_COMMIT` | mcp/tests/test_facade_surface.py:23-23 |

## Update History

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the surface pin. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
