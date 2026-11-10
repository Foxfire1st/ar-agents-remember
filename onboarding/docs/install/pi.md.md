# docs/install/pi.md

## Governing Overview

[Repository overview](../../overview.md)

## Purpose

The Pi install page: how to register the Agents Remember MCP server through
`pi-mcp-adapter`, the one `role_start` call that begins setup, how Pi receives skills, and
which harness-created files Agents Remember leaves alone.

## What The Page Establishes

- Pi core has no built-in MCP client, so the project settings load `pi-mcp-adapter`; the
  settings list no skill folder.
- Registration adapts the common registration example and the shared settings setup to the
  `mcpServers.agents-remember` entry of the adapter's configuration. The settings path is the
  absolute user-config path, not a workspace file; `npm:pi-mcp-adapter` is configured through
  Pi's package settings, and the harness is restarted or reloaded after a registration change.
- Setup starts with one `role_start(role="bootstrap", request_id=...)` call that names no task
  and no repository. It prepares the runtime scaffold, provisions and starts the Paseo host,
  verifies the plug-in and starts one Bootstrap seat whose dashboard chat continues setup; a
  retry with the same `request_id` reconciles to the same seat. Bootstrap ends at memory setup,
  starts no role and authors no onboarding or knowledge.
- Skills: Agents Remember writes no skill folder. The tool server publishes each skill as an
  MCP resource (the SEP-2640 skills extension) and Pi reads them through the adapter, so there
  is no skill tree to copy, render or keep in sync.
- Harness-created files: Pi agents can create `~/.pi/agent/mcp.json`, which Agents Remember's
  agents leave unchanged and report; running `pi` in a worktree creates `.pi/npm`, which Agents
  Remember avoids by running harness commands only in scratch folders.

## Boundaries

Provider setup is not among the install steps. The page names no provider id, setting or
command and gives no enable, start, index or query step.

The page is instructions, not proof: it does not show that Pi installed the adapter or that
the `role_start` call ran. Pi's skill scanning, its package installation and its adapter
behaviour are stated as the page's account of that harness.

## Evidence

- Pi core has no built-in MCP client, so the project settings load `pi-mcp-adapter`. [1]

- Registration adapts the common example to the adapter's `mcpServers.agents-remember` entry, configures `npm:pi-mcp-adapter` through Pi's package settings, then restarts or reloads the harness. [2]

- One `role_start(role="bootstrap")` call prepares the runtime scaffold, starts the Paseo host and one Bootstrap seat; Bootstrap ends at memory setup and starts no role. [4]

- Skills arrive as MCP resources (the SEP-2640 skills extension) that Pi reads through the adapter; there is no skill tree to copy, render or keep in sync. [5]
