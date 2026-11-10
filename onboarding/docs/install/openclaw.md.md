# docs/install/openclaw.md

## Governing Overview

[Repository overview](../../overview.md)

## Purpose

The OpenClaw install page: how to register the Agents Remember MCP server in the OpenClaw config
registry from the common registration example, the one `role_start` call that starts Bootstrap,
where the skills come from, and the long-running-turns timeout configuration.

## What The Page Establishes

- OpenClaw uses an agent workspace; MCP server definitions live in the OpenClaw config registry
  under `mcp.servers`.
- MCP: registration adapts the common example to the `mcp.servers.agents-remember` entry in
  `~/.openclaw/openclaw.json`, with the absolute user-config settings path.
- Skills: OpenClaw loads skills from the places it scans; Agents Remember writes none there. The
  tool server publishes each skill as an MCP resource, so there is no workspace skill copy and no
  skill-sync step.
- After the restart, one `role_start(role="bootstrap", …)` call prepares the runtime scaffold and
  starts Bootstrap, which ends at memory setup and tells the developer to start the Architect; the
  page gives no provider step.

## Boundaries

Provider setup is not among the install steps. The page names no provider id for those
retired search providers, no provider setting and no provider command, and gives no enable,
start, index or query step. Its only use of the word "provider" is OpenClaw's own
model-provider timeout configuration in the long-running-turns section, which is the
harness's model routing and not the retired search providers.

The page is instructions, not proof: it does not show that the `mcp.servers` registry entry
was accepted, that the gateway restarted, or that the `role_start` call started a Bootstrap
seat. OpenClaw's registry layout and skill loading are the page's
account of that harness.

## Evidence

- One `role_start(role="bootstrap", …)` call prepares the runtime scaffold and starts Bootstrap, which ends at memory setup and hands the knowledge foundation to the Architect; nothing provider-side starts. [3]

- Registration goes under the `mcp.servers.agents-remember` entry in `~/.openclaw/openclaw.json`, adapted from the common registration example with the absolute user-config settings path. [5]

- OpenClaw loads skills from the places it scans; Agents Remember writes none there, and the tool server publishes each skill as an MCP resource, so there is no workspace skill copy or skill-sync step. [6]

- The long-running-turns section configures model-provider timeouts and a gateway restart. [7]
