# mcp/tests/test_codex_clean_room_probe.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_codex_clean_room_probe.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-12T15:19+02:00 |
| lastVerifiedCommitHash |  `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`|
| lastVerifiedCommitDate |  2026-08-14T14:36:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

This test is the field-shaped Codex clean-room probe: it uses the real installed Codex app-server when available and otherwise selects the explicit fake mode used in environments without Codex.

## Code Commentary

### Logic

The test selects real/fake mode deterministically, exercises initialize and thread-list through the conversation library, and verifies the reported user-agent/response boundary.

### Conventions

Availability selects the documented mode; a failed real Codex run is not converted into fake success.

### Invariants And Boundaries

- Real installed Codex is preferred when present.
- Fake transport exists only for environments where Codex is unavailable.
- The probe remains read-only.

### Todos

None.

## Docs References

No external Domain Documentation source is configured for this integration probe.

| Finding | Anchor | Source |
| --- | --- | --- |
| Harness availability selects the real or explicit fake integration mode. | `_selected_mode`; `test_codex_initialize_and_thread_list_use_real_when_available` | mcp/tests/test_codex_clean_room_probe.py:72-90 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The test drives initialize and thread-list through the production conversation adapter. | `CODEX`; `test_codex_initialize_and_thread_list_use_real_when_available` | mcp/tests/test_codex_clean_room_probe.py:19-119 |

## Cross-Repo References

Codex app-server is an external harness boundary, not a sibling repository.

| Finding | Anchor | Source |
| --- | --- | --- |
| The probe uses the Codex harness command when the executable is available. | `CODEX`; `_selected_mode` | mcp/tests/test_codex_clean_room_probe.py:19-90 |

## Update History

- 2026-08-12T15:19+02:00 — Created for L23's real-when-available Codex clean-room probe; verification provenance remains closeout-owned.
