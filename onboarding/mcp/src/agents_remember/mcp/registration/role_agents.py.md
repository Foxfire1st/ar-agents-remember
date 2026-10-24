# mcp/src/agents_remember/mcp/registration/role_agents.py

## Governing Overview

[Route overview](overview.md)

## Purpose

Registers role_start, the Manager-owned role_start_set, and role_message with their explicit caller-visible contracts.

## Code Commentary

### Current Contract

The existing typed start/message/set registrars remain the public surface. Current compact descriptions advertise start ok/id/handover and message wait/held/cancellation outcomes plus the longer reference. Mode/feature policy, attachments/hashes, capacity, successor and receipt authority stay with the input/application/reference owners, not a claim that every detail is still inline in the short docstrings. Held answer overrides remain distinct from ordinary compact delivery.

> **Retained historical source account — superseded by the current contract:**
> role_start constructs RoleStartCall, role_start_set constructs RoleStartSetCall with validated per-seat overrides, and role_message constructs RoleMessageCall, running blocking application work in a thread so waiting does not block server transport. Descriptions name caller binding, permitted child scope, same-request retry, receipt-bound addressing, role-message final reply behavior and bounded wait. No developer gate is transported through an invented tool. `role_start` accepts `feature_values` for speed features beside agent/model/effort; its description states that a start call cannot state a mode or a permission-bearing feature, which belong in user settings or the host profile.

> **Retained historical source account — superseded by the current contract:**
> Set overrides admit only agent, model, effort and feature values, never a caller mode or permission-policy setting. Leaf replacement carries the holder ID and explicit interruption permission. Message input carries an optional waiting-message withdrawal ID; the mounted description says held rather than accepted when the product queues unavailable-recipient work, and preserves the developer-only permission prompt boundary.
> The registered `role_message` inputs include unbounded file-only `body` and existing-path `attach`, distinct from settings-bounded wake `text`. Its description preserves receipt/role addressing and wait outcomes while naming filed messages/replies, count/limit refusals, attachment/hash handling and archived-recipient successor remedies. The adapter constructs the typed call and delegates to the same application owner; its advertised filing, wait and strict-contract promises are not independent evidence for every composed branch. Early unfinished-start holding bypasses the filing prologue, held waits omit its cut/file helper, and held `turnId` is absent from the response DTO. These limits do not weaken the normative promises or add a public tool.

> **Retained historical source account — superseded by the current contract:**
> role_start constructs RoleStartCall and role_message constructs RoleMessageCall, running blocking application work in a thread so waiting does not block server transport. Descriptions name caller binding, permitted child scope, same-request retry, receipt-bound addressing, role-message final reply behavior and bounded wait. No developer gate is transported through an invented tool. `role_start` accepts `feature_values` for speed features beside agent/model/effort; its description states that a start call cannot state a mode or a permission-bearing feature, which belong in user settings or the host profile.

## Current Contract

The existing role_start registrar accepts optional step_up and passes it unchanged into RoleStartCall before delegating blocking work through asyncio.to_thread. The registrar adds no mode parameter, permission override, counted-try policy, retirement or launch authority; its compact description remains only the short public summary. role_start_set and role_message keep their existing registration/ownership and do not gain this new argument.


This account is bound to the candidate source, not a claim of a running serving build or a fresh execution/acceptance verdict. Existing historical accounts remain historical.

## Evidence


- Worker/Curator typed review census, record-only exclusion and unknown history. [4]
- Reason admission, threshold and differing-harness/model inheritance boundary. [5]
- File-local implementation of the stated contract; caller-owned effects and governing workflow are separate evidence. [6]


## Investigator scope and request identity

> **Retained historical source account — superseded by the current contract:**
> The mounted description names the shared Investigator slot refusal for new turns. The adapter delegates admission to the same role-message owner and preserves named refusal/detail/remedy values; tool description is not a runtime permission grant.


- **Retained historical source account — superseded by the current contract:** The current source implements this file’s stated Investigator boundary. [2]


## Refreshed current evidence

- **Retained historical source account — superseded by the current contract:** Current registration declares the public input/delegation surface and its normative promises; it does not independently qualify composed filing, held waits or DTO completeness. [1]

- The existing typed start/message/set registrars remain the public surface. Current compact descriptions advertise start ok/id/handover and message wait/held/cancellation outcomes plus the longer reference. Mode/feature policy, attachments/hashes, capacity, successor and receipt authority stay with the input/application/reference owners, not a claim that every detail is still inline in the short docstrings. Held answer overrides remain distinct from ordinary compact delivery. [3]

## The caller's harness name and the settings tool

`caller_harness_name` reads the client name the calling harness sent in its `initialize` request from the served request context, and answers `None` for a client that named nothing or for a call made outside a served request, so the launch reports an unknown caller harness rather than inventing one. `user_settings_init` is registered beside the three role tools, takes a target, an optional harness or per-role harnesses and a dry run, and runs its payload builder in a thread.

- The transport's own client name, or no name at all. [7]
- The registration that mounts the role tools and the settings initializer. [8]
