# mcp/tests/paseo_launch_test_support.py

## Governing Overview

[Route overview](overview.md)

## Purpose and current source account

GivenToAgentExpectations derives expected handover, tool-server binding, sandbox write-avoidance values and recovery note from the launch fixture, then checks what the dispatch route gave each role. Its first-message expectation is not independent of production: it imports role_handover_artifacts.artifact_line, so the line's formatting is the production formatting and only the data it names is derived here. It shares assertions across launch-related suites and models no live harness.

The module additionally owns `FakeRuntime`, its catalog/server constants, recorded launch-call set, the RequestId protocol its projections read a request through, and handover_object/planned_handover, which build the complete hand-over and its file reference the projection names. This in-memory bridge stand-in holds agents/workspaces across calls, preserves before/after-effect failure scenarios and supplies state/archive/resume plus `agents-live` answers; `unlisted` makes the census incomplete. `GivenToAgentExpectations` derives the data a dispatch gives an agent. Launch/status/document-chat suites share the fake, not a live harness or production host.

## Current scoped contract

`FakeRuntime._agent_create` records `modeId` and a copied supplied `featureValues` map independently of the optional `service_tier` entry. It emits `serviceTier` only when that key exists, so a permission-feature-only request does not require a speed choice. This makes fake-host observation possible without claiming native application or permission behavior.

## Test-support boundary

The module holds no tests and makes no product claim. `FakeRuntime._agent_has_message` answers `present` from the fake agent's recorded `timeline`, standing in for the bridge's `agent-has-message` read so the reconciliation before a resend can be exercised; it records nothing on the runtime and is not a host observation.

## Evidence

- The scoped current source carries the module/document behavior described above. [1]

## Current contract evidence


- The module additionally owns `FakeRuntime`, its catalog/server constants and recorded launch-call set. This in-memory bridge stand-in holds agents/workspaces across calls, preserves before/after-effect failure scenarios and supplies state/archive/resume plus `agents-live` answers; `unlisted` makes the census incomplete. `GivenToAgentExpectations` derives the data a dispatch gives an agent, but its first-message line comes from the production `artifact_line`, so only the data is independent and the formatting is shared. Launch/status/document-chat suites share the fake, not a live harness or production host. [2]



- FakeRuntime._agent_create now records a serviceTier only when featureValues actually contains service_tier, separately copies any supplied featureValues map and retains modeId when supplied. This supports permission-feature-only payloads without a service-tier KeyError and exposes submitted choices to the controlled observations. Default-model and idempotent agent-state behavior remain. [3]
