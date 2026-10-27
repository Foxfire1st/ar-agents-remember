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
`_agent_has_message()` is how the fake refuses to hand a message the recipient's timeline already carries
(MIK-R171 rule 3). `state()` sets the status and what goes with it.

`RequestId` supplies the request id a fixture's projections read, and `GivenToAgentExpectations` derives what a
launch must give its agent from that request: `receipt()`, `artifact()`, `handover_object()`,
`planned_handover()`, `first_message()`, `tool_server()`, `recovery_note()` and `given_to_agent()`, with
`watch_launch()` recording, at every runtime call, the receipt on disk and whether its artifact is there.
`assert_applied_is_recorded()` checks the receipt says what the agent was given.

- **Creation payloads.** `_agent_create()` records a service tier only when `featureValues` actually carries
  `service_tier`, copies any supplied `featureValues` map separately and keeps `modeId` when it is supplied, so a
  permission-feature-only payload needs no service tier.
- **Host authority.** `prepare_host()` writes the host authority of the installation a fixture represents into
  its config file, and `LAUNCH_COMMANDS` names the commands a launch may use.

### Conventions

A fake reply is built from the same constants the product reads (`SERVER_ID`, the host contract version), so a
test cannot pass on a value production would never send.

### Invariants And Boundaries

- The fake records every call, so a case can assert what the launch asked for rather than only its answer.
- A failure is staged before or after the effect it names; the fixture never silently succeeds.

## Evidence

- The scoped current source carries the module/document behavior described above. [1]

- The module additionally owns `FakeRuntime`, its catalog/server constants and recorded launch-call set. This in-memory bridge stand-in holds agents/workspaces across calls, preserves before/after-effect failure scenarios and supplies state/archive/resume plus `agents-live` answers; `unlisted` makes the census incomplete. `GivenToAgentExpectations` derives the data a dispatch gives an agent, but its first-message line comes from the production `artifact_line`, so only the data is independent and the formatting is shared. Launch/status/document-chat suites share the fake, not a live harness or production host. [2]

- FakeRuntime._agent_create now records a serviceTier only when featureValues actually contains service_tier, separately copies any supplied featureValues map and retains modeId when supplied. This supports permission-feature-only payloads without a service-tier KeyError and exposes submitted choices to the controlled observations. Default-model and idempotent agent-state behavior remain. [3]
