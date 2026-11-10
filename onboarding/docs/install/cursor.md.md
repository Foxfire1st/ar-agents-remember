# docs/install/cursor.md

## Governing Overview

[Repository overview](../../overview.md)

## Purpose

The Cursor install page: how to register the Agents Remember MCP server from the common
registration example, the one `role_start` call that starts Bootstrap, and where the skills come
from (the tool server, as MCP resources).

## What The Page Establishes

- Skills: Cursor discovers skills from folders it scans; Agents Remember writes none, and the tool
  server publishes each skill as an MCP resource, so there is no skill tree to copy, render or keep in sync.
- MCP: registration adapts the common example to the `mcpServers.agents-remember` entry in
  Cursor's MCP configuration, with the absolute user-config settings path.
- After the restart, one `role_start(role="bootstrap", …)` call prepares the runtime scaffold and
  starts Bootstrap, which ends at memory setup and tells the developer to start the Architect; the
  page gives no provider step.

## Boundaries

Provider setup is not among the install steps. The page names no provider id, setting or
command and gives no enable, start, index or query step.

The page is instructions, not proof: nothing in it shows that Cursor accepted the
`mcpServers.agents-remember` entry, that it read the skills as MCP resources, or that the
`role_start` call started a Bootstrap seat. Which surfaces Cursor honours is the page's account
of that harness.

## Evidence

- One `role_start(role="bootstrap", …)` call prepares the runtime scaffold and starts Bootstrap, which ends at memory setup and hands the knowledge foundation to the Architect; nothing provider-side starts. [3]

- The page names the `mcpServers.agents-remember` entry in Cursor's MCP configuration, adapted from the common registration example with the absolute user-config settings path. [5]

- The skills section says Cursor discovers skills from folders it scans, Agents Remember writes none, and the tool server publishes each skill as an MCP resource, so first-run setup copies no skill tree. [6]
