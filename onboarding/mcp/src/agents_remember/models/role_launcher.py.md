# mcp/src/agents_remember/models/role_launcher.py

## Governing Overview

[Route overview](overview.md)

## Purpose

Defines canonical role selections and HTTP launcher call models.

## Code Commentary

RoleSelection carries exact sprint/master/leaf references; request aliases keep the current role/Paseo vocabulary. `RoleAgentOverride` carries optional `agentId`, `modelId`, `effortId`, `modeId` and `featureValues`. `featureValues` carries strict booleans or option IDs. Service tier retains its own native capability and configuration. The host decides whether to apply a mode. RoleDispatchRequest distinguishes start/revive under the saved request UUID and carries optional replacesAgentId plus replacesInterruptTurn. Replacement remains an explicit request; the model does not authorize retirement or free an occupied seat. The default-false `chatStarted` field records a parentless start from a chat without a role under R113 rule6; dashboard/role-agent starts do not use it. This wire marker is not authority to start, attach a parent or bypass replacement admission.

## Current Contract

RoleLauncherOptionsRequest carries optional agentId and modelId for a selected-model read. The options route uses both fields to return the pair’s options, or returns scoped catalogue and receipt data without a complete pair. A metadata request can ask to refresh provider discovery.

RoleDispatchRequest declares optional step_up aliased stepUp, constrained to string length 1..1000 when present. This wire model does not enforce the one-sentence/nonblank-after-trimming policy or select a model; later launch admission owns those checks. Start/revive and replacement fields remain distinct.


## Evidence


- Worker/Curator typed review census, record-only exclusion and unknown history. [6]

- Step-up reason admission and threshold govern choice of an alternative. An alternative takes mode from its own row at either scope. [7]


- The wire models carry optional provider and model IDs for selected options, explicit dispatch overrides and replacement markers, and a saved request UUID for Result. [8]


- Parentless chat-start marker is default false wire data, not launch or replacement authority. [5]





- The launcher override carries an optional modeId alongside its other launch choices. [2]

- Frozen implementation of RoleDispatchRequest supporting the stated file behavior. [3]

## Investigator scope and request identity

Investigator is canonical in new selection output. The parsed selection retains whether the one earlier role spelling was supplied so API answers can carry the exact notice. Per-request receipt cardinality is independent of Projects versus selected-task altitude; neither creates caller permission.


- The current source implements this file’s stated Investigator boundary. [4]


## Refreshed current evidence

- Frozen implementation of RoleSelection supporting the stated file behavior. [1]

## The free agent as a launcher role

`LauncherRole` admits `bootstrap`, the free agent a new user reaches through the one start call; `system-specialist` normalizes to `investigator`. `RoleDispatchRequest` carries `caller_harness` (`callerHarness`, at most 120 characters), the harness the calling chat itself runs: absent means the caller named none, and nothing substitutes a provider for it. Neither addition authorizes a start, a parent or a replacement.

- The launcher role set that includes the free agent. [9]
- The dispatch request, which carries the caller's harness name. [10]

- The earlier system-specialist spelling names Investigator; Bootstrap and callerHarness remain launcher model data rather than caller permission. [11]
