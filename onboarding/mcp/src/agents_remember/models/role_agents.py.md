# mcp/src/agents_remember/models/role_agents.py

## Governing Overview

[Route overview](overview.md)

## Purpose

Defines typed role-tool calls, results and finite refusal vocabulary.

## Code Commentary

`RoleMessageCall` declares wake text separately from file-only `body` and attachment paths. `RoleMessageResponse` declares `messageFile`, `messageFileSha256`, `messageLength`, `messageLimit`, `successorAgentId` and its listed held/refusal metadata. Declaring every producer-owned field remains the normative strict-contract duty, not a verified universal fact: facade `_held_then_delivered` conditionally returns `turnId`, which this DTO does not declare. The declaration alone also does not prove early unfinished-start holding filed a body or a held wait cut/filed its reply. Those composed-path gaps remain Owner/Worker-owned; declared file fields do not certify task acceptance.

RoleStartCall extends canonical selection with required UUID and optional override; result distinguishes launch status and saved execution status. `RoleStartCall` adds `feature_values` for speed choices beside agent/model/effort. `RoleStartResponse` carries launch `choices`, a `warning` and `taskDocumentFiles`; `RoleMessageResponse` carries `reportCollection` for the sender's collected execution reports. RoleMessageCall permits agent ID or exact role references and bounded wait; response distinguishes refusal, delivered/resumed/steered/wait facts and final reply. Public detail/nextAction retain native failure causes without claiming semantic acceptance.

## Held set and message wire states

`RoleStartSetCall` carries one set request UUID and exact leaf references with separate Worker/Reviewer/Curator choices, optional Reviewer first work and replacement IDs. `SeatLaunchOverride` carries speed choices only. Both single starts and set replacement carry explicit interruption permission. `RoleStartStatus` and `RoleMessageStatus` admit `held`: a held seat exists without a turn, and a held message is product-stored rather than host-accepted. Message output names waiting IDs/counts, retained terminal lines and held-seat opening; withdrawal is a distinct input. `RoleStartSetResponse` reports each seat and partial completion without implying task acceptance.

## Current Contract

RoleStartCall carries optional step_up reason beside the existing selection, UUID, overrides and replacement intent; it does not validate a reason sentence itself. RoleStartResponse declares optional stepUp metadata on the strict rich response. The requested reason and the reported application result are distinct. Mode and permission features are still user-owned, the ordinary no-step-up route is unchanged, and this DTO neither counts review failures nor certifies applied host choices. Existing message-field incompleteness and held-path caveats remain as recorded.


This account is bound to the candidate source, not a claim of a running serving build or a fresh execution/acceptance verdict. Existing historical accounts remain historical.

## Evidence


- Worker/Curator typed review census, record-only exclusion and unknown history. [8]
- Reason admission, threshold and differing-harness/model inheritance boundary. [9]
- File-local implementation of the stated contract; caller-owned effects and governing workflow are separate evidence. [10]
- File-local implementation of the stated contract; caller-owned effects and governing workflow are separate evidence. [11]

- Frozen implementation of RoleStartCall supporting the stated file behavior. [1]
- Current RoleMessageCall declares body/attachment inputs and waiting-message withdrawal; declarations do not prove every composed branch files payloads. [2]
- Frozen implementation of RoleStartResponse supporting the stated file behavior. [3]
- Current response DTO declares its listed message/held fields but not the held producer’s conditional turnId; source declarations are not universal completeness evidence. [4]

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
