# mcp/tests/paseo_launch_test_support.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

The fake Paseo runtime the launch tests share, plus what a launch is expected to give an agent: the handover
artifact, the first message, the tool server and the recovery note. It stands in for `bridge_call`, so a launch
case runs the real dispatch route against an in-memory runtime that records every call it was asked to make.

## Code Commentary

`GivenToAgentExpectations.locator` derives the request's product-owned locator, and `artifact` reports two paths: `path` is the locator's `<request id>/<artifact name>` entry, which the recovery note and the first message name, while `canonicalPath` is the file beside the report that the launch actually writes. `watch_launch` watches `canonicalPath`. The expectations therefore describe the bounded reachable path and the stored path separately, without changing the fixture's fake-host boundary.

### Logic

`FakeRuntime` holds agents and workspaces across calls and answers the catalog, workspace, create, archive, live
listing, state and resume commands. `fail()` stages a failure before or after an effect, and
`_agent_has_message()` reports whether the recipient's timeline contains the message ID. `state()` sets the status and what goes with it.

`RequestId` supplies the request id a fixture's projections read, and `GivenToAgentExpectations` derives what a
launch must give its agent from that request: `receipt()`, `artifact()`, `handover_object()`,
`planned_handover()`, `first_message()`, `tool_server()`, `recovery_note()` and `given_to_agent()`, with
`watch_launch()` recording, at each launch command, the receipt on disk and whether its artifact exists.
`assert_applied_is_recorded()` checks the receipt says what the agent was given.

- **Creation payloads.** `_agent_create()` records a service tier only when `featureValues` actually carries
  `service_tier`, copies any supplied `featureValues` map separately and keeps `modeId` when it is supplied, so a
  permission-feature-only payload needs no service tier. An existing-only request for an absent agent returns a typed failure before the fake creates an agent.
- **Host authority.** `prepare_host()` writes the host authority of the installation a fixture represents into
  its config file, and `LAUNCH_COMMANDS` names the commands a launch may use.
- **Fake server bindings.** When `write_server_bindings` is `True` (default), `FakeRuntime.__call__` calls `_record_fake_binding()` after `agent-create` for providers where `provider_starts_tool_server_at_create(provider)` (from `agents_remember.cli.paseo_seat_policy`) is `True` and whose `agents-remember-task` tool-server env carries `AR_PASEO_AGENT_ID`, `AR_REQUEST_ID`, and `AR_ROLE`, writing `fake-<agentId>.json` (`ServerBindingRecord` with `bindingState="bound"` and the current process's PID and `process_start`) under `bindings_directory(config)` so eager launch-identity confirmation succeeds in-process; `agent-archive` removes that file via `_remove_fake_binding()`. Setting `write_server_bindings = False` suppresses registration for negative binding tests.

### Conventions

A fake reply is built from the same constants the product reads (`SERVER_ID`, the host contract version), so a
test cannot pass on a value production would never send.

### Invariants And Boundaries

- The fake records every call, so a case can assert what the launch asked for rather than only its answer.
- A failure is staged before or after the effect it names; the fixture never silently succeeds.

## Evidence

- The shared fixture records bridge calls and derives the handover artifacts, recovery note and task-server definition from each launch request. [1]

- The stateful fake records calls, can fail before or after an effect, and supports incomplete live listings. Fixture message formatting uses the production artifact helper. [2]


- Creation records supplied feature values and mode. It records a service tier only when the supplied feature map contains one. [3]


- `FakeRuntime` writes synthetic `ServerBindingRecord` files for eager providers (`provider_starts_tool_server_at_create`) on `agent-create` when `write_server_bindings` is enabled and removes them on `agent-archive`. [4]
