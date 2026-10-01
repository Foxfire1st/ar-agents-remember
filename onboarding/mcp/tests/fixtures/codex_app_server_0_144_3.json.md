# mcp/tests/fixtures/codex_app_server_0_144_3.json

## Governing Overview

[mcp/tests overview](../../overview.md)

## Purpose

Pins the validated Codex `0.144.3` app-server schema snapshot and representative stable
initialize, model, thread, turn, server-request, and notification messages used by tests.

## Code Commentary

L23 changes the captured initialize fixture's server product to `agents_remember` while retaining the exact client suffix, exercising product-agnostic validation.

The snapshot records protocol/schema hashes, stable method inventory, advertised reasoning efforts,
thread settings/echoes, terminal statuses and structured interactions. It is a frozen fixture, not runtime configuration or proof of executed tests.

## Conventions

Fixture values are deterministic and use the exact pinned protocol identity. The initialize result
records the fixture product `agents_remember/0.144.3` and the exact Agents Remember client suffix. Changes
require revalidation against the generated schema and current runtime grammar.

## Invariants And Boundaries

- `experimental` stays false and the stable inventory remains explicit.
- No credential or prompt data is stored in the fixture.
- The fixture must not be interpreted as authorization for production cutover.

## Todos

None known for this leaf.

## Evidence

### Docs References

No Domain Documentation entries are configured in the resolved source registry.

No configured live documentation source was available for this pass.

### Repo-Internal References

- This frozen snapshot records schema-generation provenance and its stable method list. [1]
- Thread-start and resume examples retain their distinct result envelopes. [2]

### Cross-Repo References

The fixture was generated from the external Codex CLI app-server schema.

- Generated command and pinned schema hashes are recorded in the fixture. [3]
