# mcp/tests/test_paseo_bridge_agents.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

Runs the bridge's workspace, creation, message, get and archive commands as the real script against a fake client
package: a workspace is reused or created through the public client, an explicit workspace refuses a partial or
wrong placement without falling back to a directory, and creation tells a created agent from an existing one and
from a refusal. A service tier travels as native creation data, and an unsupported one is rejected before create.

## Code Commentary

### Logic

`AgentCommandScriptTests.call()` starts the real `paseo_bridge.mjs` against the scenario's runtime and
`recorded()` reports what the fake client was asked to do; `failure()` covers the failing path.
`FAKE_DAEMON_CLIENT`/`FAKE_CLIENT_ROOT` install the fake package in a scratch prefix and `WAITED`,
`TOOL_SERVER_START_MS` and the agent ids are the fixtures the commands read.

- **Workspaces.** `test_workspace_open_reuses_or_creates_through_the_public_client` reuses or creates through the
  public client, `test_task_workspace_identity_ignores_titles_and_separates_masters_at_one_cwd` keeps identity
  independent of a title and separates two masters at one working directory, and
  `test_explicit_workspace_refuses_partial_and_wrong_placement_without_directory_fallback` refuses rather than
  falling back.
- **Creation.** `test_service_tier_is_native_creation_data_and_unsupported_is_rejected_before_create` proves the
  tier is native creation data and an unsupported one stops before create, and
  `test_agent_create_uses_the_given_id_and_tells_created_existing_and_refused_apart` keeps the three outcomes
  apart under the id it was given.
- **Messages.** `test_the_first_message_follows_the_creation_and_goes_to_an_agent_that_has_none` sends the first
  message only to an agent that has none, and
  `test_a_300_000_byte_first_message_reaches_the_client_as_data` carries a large message to the client as data
  rather than as a path.
- **Addressing and catalog.** `test_agent_get_and_archive_address_exactly_one_agent` addresses one agent by id,
  and `test_catalog_marks_the_providers_the_runtime_reports_as_taking_no_tool_servers` marks the providers the
  runtime reports as taking no tool servers.

### Conventions

Every case starts the real script, so the command line parsed, the payload sent and the client call recorded are
the production ones — the fake is only the daemon behind them.

### Invariants And Boundaries

- An explicit workspace never falls back to a directory the caller did not name.
- A refused feature sends no creation and no message.

## Evidence


- Workspace, creation, message, get and archive commands against the real script and fake client. [1]


- Feature discovery may precede a refusal, but refused features send no agent create or message. [2]

- Keyed completed-creation replay, pre-refresh current identity and a selectively hidden live listing support the archive cases. [3]
