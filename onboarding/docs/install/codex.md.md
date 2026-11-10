# docs/install/codex.md

## Governing Overview

[Repository overview](../../overview.md)

## Purpose

The Codex install page: the two things Codex needs (the Agents Remember MCP server in Codex
config, and one call that starts Bootstrap), how to register the server from the common example, and
where the skills come from (the tool server, as MCP resources).

## What The Page Establishes

- After the restart, one `role_start(role="bootstrap", …)` call prepares the runtime scaffold and
  starts Bootstrap, which ends at memory setup and tells the developer to start the Architect; the
  page gives no provider step.

## Boundaries

Provider setup is not among the install steps. The page names no provider id, setting or
command and gives no enable, start, index or query step.

The page is instructions, not proof: it does not show that `config.toml` accepted the
registration, that Codex read the skills as MCP resources, or that the `role_start` call started
a Bootstrap seat. What Codex does with `config.toml` and MCP resources is the page's account of
that harness.

## Evidence

- Codex needs the MCP server in its config plus one call that starts Bootstrap; skills arrive from the tool server as MCP resources and nothing is copied into the harness. [1]

- One `role_start(role="bootstrap", …)` call prepares the runtime scaffold and starts Bootstrap, which ends at memory setup and hands the knowledge foundation to the Architect; nothing provider-side starts. [4]
