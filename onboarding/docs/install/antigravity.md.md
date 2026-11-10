# docs/install/antigravity.md

## Governing Overview

[Repository overview](../../overview.md)

## Purpose

The Antigravity install page: how to register the Agents Remember MCP server from the common
registration example, the one `role_start` call that starts Bootstrap, and where the skills come
from (the tool server, as MCP resources).

## What The Page Establishes

- MCP: registration adapts the common example to the `mcpServers.agents-remember` entry in
  Antigravity's MCP settings UI, with the absolute user-config settings path; the harness is
  restarted or reloaded after the change.
- After the restart, one `role_start(role="bootstrap", …)` call prepares the runtime scaffold and
  starts Bootstrap, which ends at memory setup and tells the developer to start the Architect; the
  page gives no provider step.

## Boundaries

Provider setup is not among the install steps. The page names no provider id, no provider
setting, no provider command, and gives no enable, start, index or query step.

The page is instructions for a person and an agent. It is not evidence that a package was
copied, that a renderer ran, that Antigravity restarted, that an MCP server registered, or
that `runtime_install()` executed on any machine. Its statements about Antigravity's
discovery paths and IDE/CLI config locations are the page's account of that harness, not an
independent check of it.

## Evidence

- One `role_start(role="bootstrap", …)` call prepares the runtime scaffold and starts Bootstrap, which ends at memory setup and hands the knowledge foundation to the Architect; nothing provider-side starts. [4]

- The page names the `mcpServers.agents-remember` entry in Antigravity's MCP settings UI, adapted from the common registration example with the absolute user-config settings path. [5]
