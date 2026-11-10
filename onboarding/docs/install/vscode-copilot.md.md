# docs/install/vscode-copilot.md

## Governing Overview

[Repository overview](../../overview.md)

## Purpose

The VS Code + GitHub Copilot install page: how to register the Agents Remember MCP server
in VS Code's MCP configuration, the one `role_start` call that begins setup, and how Copilot
receives skills.

## What The Page Establishes

- VS Code supports always-on instructions, workspace MCP configuration and agent hooks, but
  Agents Remember needs only the MCP registration and one call; no skill folder is copied
  into the workspace.
- Registration adapts the common registration example and the shared settings setup to the
  `servers.agents-remember` entry of VS Code's MCP configuration. The settings path is the
  absolute user-config path, not a workspace file, and the harness is restarted or reloaded
  after a registration change.
- Setup starts with one `role_start(role="bootstrap", request_id=...)` call in a Copilot Chat
  session that names no task and no repository. It prepares the runtime scaffold, provisions
  and starts the Paseo host, verifies the plug-in and starts one Bootstrap seat whose dashboard
  chat continues setup; a retry with the same `request_id` reconciles to the same seat.
  Bootstrap ends at memory setup, starts no role and authors no onboarding or knowledge.
- Skills: Agents Remember writes no skill folder. The tool server publishes each skill as an
  MCP resource (the SEP-2640 skills extension) and Copilot reads them from the running
  server, so there is no skill tree to copy, render or keep in sync.

## Boundaries

Provider setup is not among the install steps. The page names no provider id, setting or
command and gives no enable, start, index or query step.

The page is instructions, not proof: it does not show that VS Code accepted the registration
or that the `role_start` call ran. VS Code's skill scanning and MCP configuration are the
page's account of that harness.

## Evidence

- Registration adapts the common example to the `servers.agents-remember` entry of VS Code's MCP configuration, uses the absolute user-config settings path, then restarts or reloads the harness. [1]

- One `role_start(role="bootstrap")` call prepares the runtime scaffold, starts the Paseo host and one Bootstrap seat; Bootstrap ends at memory setup and starts no role. [4]

- Skills arrive as MCP resources (the SEP-2640 skills extension) that Copilot reads from the running server; Agents Remember writes no skill folder. [5]
