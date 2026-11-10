# docs/install/claude-code.md

## Governing Overview

[Repository overview](../../overview.md)

## Purpose

The Claude Code install page: how to register the Agents Remember MCP server from the common
registration example, the one `role_start` call that starts Bootstrap, and where the skills come
from (the tool server, as MCP resources).

## What The Page Establishes

- After the restart, one `role_start(role="bootstrap", …)` call prepares the runtime scaffold and
  starts Bootstrap, which ends at memory setup and tells the developer to start the Architect; the
  page gives no provider step.

## Boundaries

Provider setup is not among the install steps. The page names no provider id, setting or
command and gives no enable, start, index or query step.

The page is instructions, not proof: it does not show that Claude Code detected the MCP
server, that it read the skills as MCP resources, or that the `role_start` call started a
Bootstrap seat. Its statements about how Claude Code loads context, discovers skills and reads
its MCP configuration are the page's account of that harness.

## Evidence

- One `role_start(role="bootstrap", …)` call prepares the runtime scaffold and starts Bootstrap, which ends at memory setup and hands the knowledge foundation to the Architect; nothing provider-side starts. [3]
