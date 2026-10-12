# mcp/tests/paseo_launch_test_support.py

## Governing Overview

[Route overview](overview.md)

## Purpose and current source account

GivenToAgentExpectations independently derives expected handover, first-message, tool-server binding, sandbox write-avoidance values and recovery note from the launch fixture, then checks what the dispatch route gave each role. It shares assertions across launch-related suites and models no live harness.

The module additionally owns `FakeRuntime`, its catalog/server constants and recorded launch-call set. This in-memory bridge stand-in holds agents/workspaces across calls, preserves before/after-effect failure scenarios and supplies state/archive/resume plus `agents-live` answers; `unlisted` makes the census incomplete. `GivenToAgentExpectations` still independently derives what a dispatch gives an agent. Launch/status/document-chat suites share the fake, not a live harness or production host.

## Evidence

- The scoped current source carries the module/document behavior described above. [1]

## Current contract evidence

- The module additionally owns `FakeRuntime`, its catalog/server constants and recorded launch-call set. This in-memory bridge stand-in holds agents/workspaces across calls, preserves before/after-effect failure scenarios and supplies state/archive/resume plus `agents-live` answers; `unlisted` makes the census incomplete. `GivenToAgentExpectations` still independently derives what a dispatch gives an agent. Launch/status/document-chat suites share the fake, not a live harness or production host. [2]
