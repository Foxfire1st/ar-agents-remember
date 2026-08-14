# mcp/tests/fixtures/codex_app_server_0_144_3.json

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/fixtures/codex_app_server_0_144_3.json` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-12T04:15+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`|
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview | `../../overview.md` |

## Governing Overview

[mcp/tests overview](../../overview.md)

## Purpose

Pins the validated Codex `0.144.3` app-server schema snapshot and representative stable
initialize, model, thread, turn, server-request, and notification messages used by tests.

## Code Commentary

L23 changes the captured initialize fixture's server product to `agents_remember` while retaining the exact client suffix, exercising product-agnostic validation.

The snapshot records protocol/schema hashes, stable method inventory, advertised reasoning efforts,
thread settings/echoes, terminal statuses, structured interactions, and reconnect evidence. It is
test evidence, not runtime configuration.

## Conventions

Fixture values are deterministic and use the exact pinned protocol identity. The initialize result
uses the current Desktop host-first product plus exact Agents Remember client suffix. Changes
require revalidation against the generated schema and current runtime grammar.

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
| Adapter tests load this fixture for fake protocol and effort assertions. | "FIXTURE_PATH = Path(__file__).parent / \"fixtures\" / \"codex_app_server_0_144_3.json\""; "def fixture() -> JsonObject:"; "async def test_handshake_uses_stable_protocol_and_exposes_effort_menu() -> None:"; "def test_fixture_pins_validated_01443_schema_and_stable_surface() -> None:" | mcp/tests/test_codex_app_server_adapter.py:38-38; mcp/tests/test_codex_app_server_adapter.py:142-142; mcp/tests/test_codex_app_server_adapter.py:307-307; mcp/tests/test_codex_app_server_adapter_basic.py:28-28 |
| Protocol tests validate thread-open parsing against representative messages. | `test_thread_open_parser_covers_fork_echo_and_structured_status` | mcp/tests/test_codex_app_server_protocol.py:294-314 |

## Cross-Repo References

The fixture was generated from the external Codex CLI app-server schema.

| Finding | Anchor | Source |
| --- | --- | --- |
| Generated command and pinned schema hashes are recorded in the fixture. | "generatedBy"; "schemaSha256" | mcp/tests/fixtures/codex_app_server_0_144_3.json:5-5; mcp/tests/fixtures/codex_app_server_0_144_3.json:7-7 |

## Update History

- 2026-08-12T15:56+02:00 — 260731-EFA-L23 curator body review: reconciled this card with the exact current source delta described above; verification provenance remains closeout-owned.

- 2026-08-12T04:15+02:00 — 260731-EFA-L22 Codex Desktop repair: migrated the representative
  initialize result to the clean-cut Desktop host-first user agent with exact client identity; the
  pinned schema/protocol payload is otherwise unchanged.

- 2026-08-03T04:00:52+02:00 — 260731-EFA-L6 W3-B06 curator: curated 6 citation findings for fixture loading, protocol coverage, and generated-schema metadata.

- 2026-07-14T12:30+02:00 — 260713-PHA-L3 curator pass: created onboarding for the exact-version
  schema snapshot and stable protocol evidence. Verification remains unset until closeout stamps
  the code commit.
