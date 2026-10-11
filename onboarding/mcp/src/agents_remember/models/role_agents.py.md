# mcp/src/agents_remember/models/role_agents.py

## Governing Overview

[Route overview](overview.md)

## Purpose

Defines typed role-tool calls, results and finite refusal vocabulary.

## Code Commentary

RoleStartCall extends canonical selection with required UUID and optional override; result distinguishes launch status and saved execution status. `RoleStartCall` adds `feature_values` for speed choices beside agent/model/effort. `RoleStartResponse` carries launch `choices`, a `warning` and `taskDocumentFiles`; `RoleMessageResponse` carries `reportCollection` for the sender's collected execution reports. RoleMessageCall permits agent ID or exact role references and bounded wait; response distinguishes refusal, delivered/resumed/steered/wait facts and final reply. Public detail/nextAction retain native failure causes without claiming semantic acceptance.

## Evidence

- Frozen implementation of RoleStartCall supporting the stated file behavior. [1]
- Frozen implementation of RoleMessageCall supporting the stated file behavior. [2]
- Frozen implementation of RoleStartResponse supporting the stated file behavior. [3]
- Frozen implementation of RoleMessageResponse supporting the stated file behavior. [4]

## MIK-R95 Preparation Answer Model

`RoleEnvironmentPreparation` declares the shared start's observed outcome: `enclosure` is `created`, `found` or `not-applicable`, and `workspace` is optional `created`, `found` or `opened` — `opened` deliberately names no host-reported creation outcome. `RoleStartResponse` carries the `preparation` block and an optional `preparationStatus`.

## Investigator scope and request identity

The public message refusal vocabulary includes investigator-capacity. This names a completed selected-task recipient’s unavailable slot before native delivery or resume; it adds no message-owned queue or start authority.


- The current source implements this file’s stated Investigator boundary. [5]

## Current second-server observation

RoleStartResponse declares `secondCopyLoaded: bool = False`. It records whether this
launch also carries the product's other server; unsupported one-launch exclusion keeps
the server-choice sentence in the brief. This response declaration is not host-actual
ambient exclusion/evidence5 or a first-real-agent invocation proof. The recorded D200
host-rule-six/evidence5 disposition assigns host-actual work to L132; no first-real-agent
obligation remains with L112. L112's source/input projection and supplied response/receipt
facts do not establish host consumption or exclusion. Existing F07/CODE history and
UUID/selection/refusal/messaging/wait/preparation and
requested-versus-observed semantics remain unchanged.

## Current model evidence

- Current source section contains excerpt `class RoleStartResponse(ToolResponse):`; DTO/control ownership is not execution acceptance. [6]
- Current source section contains excerpt `def harness_carries_one_server(harness_id: str `; DTO/control ownership is not execution acceptance. [7]
