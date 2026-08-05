# mcp/tests/fixtures/codex_app_server_0_144_3.json

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/fixtures/codex_app_server_0_144_3.json` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-14T12:30+02:00 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`|
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview | `../../overview.md` |

## Governing Overview

[mcp/tests overview](../../overview.md)

## Purpose

Pins the validated Codex CLI `0.144.3` app-server schema snapshot and representative stable
initialize, model, thread, turn, server-request, and notification messages used by tests.

## Code Commentary

The snapshot records protocol/schema hashes, stable method inventory, advertised reasoning efforts,
thread settings/echoes, terminal statuses, structured interactions, and reconnect evidence. It is
test evidence, not runtime configuration.

## Conventions

Fixture values are deterministic and use the exact pinned CLI/protocol identity. Changes require
revalidation against the generated schema.

## Invariants And Boundaries

- `experimental` stays false and the stable inventory remains explicit.
- No credential or prompt data is stored in the fixture.
- The fixture must not be interpreted as authorization for production cutover.

## Todos

None known for this leaf.

## Docs References

No Domain Documentation entries are configured in the resolved source registry.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Adapter tests load this fixture for fake protocol and effort assertions. | `FIXTURE_PATH`; `fixture`; `test_handshake_uses_stable_protocol_and_exposes_effort_menu`; `test_fixture_pins_validated_01443_schema_and_stable_surface` | mcp/tests/test_codex_app_server_adapter.py:34-34; mcp/tests/test_codex_app_server_adapter.py:134-135; mcp/tests/test_codex_app_server_adapter.py:299-356; mcp/tests/test_codex_app_server_adapter.py:1250-1258 |
| Protocol tests validate thread-open parsing against representative messages. | `test_thread_open_parser_covers_fork_echo_and_structured_status` | mcp/tests/test_codex_app_server_protocol.py:294-314 |

## Cross-Repo References

The fixture was generated from the external Codex CLI app-server schema.

| Finding | Anchor | Source |
| --- | --- | --- |
| Generated command and pinned schema hashes are recorded in the fixture. | "generatedBy"; "schemaSha256" | mcp/tests/fixtures/codex_app_server_0_144_3.json:5-5; mcp/tests/fixtures/codex_app_server_0_144_3.json:7-7 |

## Update History

- 2026-08-03T04:00:52+02:00 — 260731-EFA-L6 W3-B06 curator: curated 6 citation findings for fixture loading, protocol coverage, and generated-schema metadata.

- 2026-07-14T12:30+02:00 — 260713-PHA-L3 curator pass: created onboarding for the exact-version
  schema snapshot and stable protocol evidence. Verification remains unset until closeout stamps
  the code commit.
