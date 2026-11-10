# docs/install/hermes.md

## Governing Overview

[Repository overview](../../overview.md)

## Purpose

The Hermes install page: how to register the Agents Remember MCP server in `~/.hermes/config.yaml`
from the common registration example, the one `role_start` call that starts Bootstrap, and where
the skills come from (the tool server, as MCP resources).

## What The Page Establishes

- MCP: registration adapts the common example to the `mcp_servers.agents-remember` entry in
  `~/.hermes/config.yaml`, with the absolute user-config settings path.
- Skills: Hermes reads the Agents Remember skills from the tool server as MCP resources, so
  `~/.hermes/config.yaml` names no external skill folder.
- After the restart, one `role_start(role="bootstrap", …)` call prepares the runtime scaffold and
  starts Bootstrap, which ends at memory setup and tells the developer to start the Architect; the
  page gives no provider step.

## Boundaries

Provider setup is not among the install steps. The page names no provider id, setting or
command and gives no enable, start, index or query step.

The page is instructions, not proof: it does not show that `~/.hermes/config.yaml` accepted
the registration, that the harness reloaded, or that the `role_start` call started a Bootstrap
seat. Hermes' own context files and skills system are stated as the page's account of
that harness.

## Evidence

- One `role_start(role="bootstrap", …)` call prepares the runtime scaffold and starts Bootstrap, which ends at memory setup and hands the knowledge foundation to the Architect; nothing provider-side starts. [3]

- MCP registration goes under the `mcp_servers.agents-remember` entry in `~/.hermes/config.yaml`, adapted from the common registration example with the absolute user-config settings path. [5]

- Skills arrive from the tool server as MCP resources, so `~/.hermes/config.yaml` names no external skill folder and first-run setup installs none. [6]
