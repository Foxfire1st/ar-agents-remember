# mcp/src/agents_remember/cli/role_launch_publication.py

## Governing Overview

[MCP package overview](../../../overview.md)

## Purpose

Publishes a prepared role launch's handover artifacts and initial execution receipt inside the enclosure's `publication_scope` without contacting the Paseo host runtime.

## Code Commentary

- `publish_prepared_launch` enters `role_launch_enclosure.publication_scope`, writes handover artifacts via `_publish_files`, builds the launch call via `_prepared_launch_call`, builds the initial receipt via `_launch_receipt`, and atomically installs it through the caller-supplied `install_receipt` callback.
- `_publish_files` composes the opening prompt with `successor_prompt`, optional opening message (omitted when `start.held` is true), and optional ACP instruction, then writes the handover artifact and complete handover JSON through `publish_handover_files` before building `first_message`.
- `_prepared_launch_call` mints the new `agent_id` (`mint_agent_id`) and wraps `RoleLaunch` into `build_launch_call` with tool-server acceptance, denied tools, replacement/parent IDs, and held status.
- `_launch_receipt` constructs the `RECEIPT_SCHEMA` payload with `status: "starting"`, `heldStoreGeneration: 0`, request/binding/capsule/task digests, `preparation.briefsProblem`, `acpInstruction`, `replayRequest`, `applied_to_agent(launch_call)`, and held-seat fields (`heldSeat`, `heldOpeningPrompt`) when `start.held` is true.

## Relationships

- Consumed by `cli/role_launch_routes.py`; isolates in-enclosure artifact and receipt publication from host dispatch and post-launch receipt transitions.
- Uses `cli/role_launch_enclosure.py::publication_scope` to prevent writes into a retired enclosure generation.

## Evidence

- `publish_prepared_launch` publishes handover files, constructs the launch call and initial receipt, and installs the receipt inside `role_launch_enclosure.publication_scope` without calling the host. [1]
- `_publish_files` applies `successor_prompt`, non-held opening message, and ACP instruction before writing artifacts via `publish_handover_files` and building `first_message`. [2]
- `_prepared_launch_call` mints the agent ID and builds the serialized launch call payload via `build_launch_call(RoleLaunch(...))`. [3]
- `_launch_receipt` populates `RECEIPT_SCHEMA`, `heldStoreGeneration: 0`, `status: "starting"`, digests, `acpInstruction`, `replayRequest`, and conditional held-seat fields. [4]
