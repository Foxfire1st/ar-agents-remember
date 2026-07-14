# mcp/tests/fixtures/codex_app_server_0_144_3.json

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/fixtures/codex_app_server_0_144_3.json` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-14T12:30+02:00 |
| lastVerifiedCommitHash | `acb308c50072d8cde0015c4828e39d12480872ed`|
| lastVerifiedCommitDate | 2026-07-14T12:32:48+02:00|
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

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Adapter tests load this fixture for fake protocol and effort assertions. | L27-L29; L186-L199 | [test_codex_app_server_adapter.py](../test_codex_app_server_adapter.py) |
| Protocol tests validate thread-open parsing against representative messages. | L93-L116 | [test_codex_app_server_protocol.py](../test_codex_app_server_protocol.py) |

## Cross-Repo References

The fixture was generated from the external Codex CLI app-server schema.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Generated command and pinned schema hashes are recorded in the fixture. | L3-L11 | [codex_app_server_0_144_3.json](../../../../../../../../../../../../agents-remember/mcp/tests/fixtures/codex_app_server_0_144_3.json) |

## Update History

- 2026-07-14T12:30+02:00 — 260713-PHA-L3 curator pass: created onboarding for the exact-version
  schema snapshot and stable protocol evidence. Verification remains unset until closeout stamps
  the code commit.
