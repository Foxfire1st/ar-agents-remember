# mcp/src/agents_remember/models/user_settings_init.py

## Governing Overview

[MCP package overview](../../../overview.md)

## Purpose

Declare the answer of the one user-settings initializer: its state, its path, the harness of each role and what it wrote or preserved.

## Code Commentary

`UserSettingsInitResponse` extends the tool response with the operation name, the `state` that says what happened (`preview` for an unwritten plan, `created` for the one exclusive create the surface makes, `already-initialized` for an existing destination it read and left alone, `refused` for a call that wrote nothing), the settings path and the target (`host-authority` or `role-settings`). A refusal answers `code`, a bounded `detail` and a `nextAction`; a write answers the `roleHarnesses` values it carried, the `writtenKeys` and `preservedKeys`, the `readBack` state of the destination and a `settingsSources` list. `changed` and `dryRun` distinguish a write from a preview. The declared model is the answer's shape, and it decides nothing about the file.

## Evidence

- The response model and its declared fields. [1]
- The registry binds the tool name to this response model. [2]
- A preview writes nothing and reports the preview state. [3]

- Current source account and its stated boundaries. [4]
