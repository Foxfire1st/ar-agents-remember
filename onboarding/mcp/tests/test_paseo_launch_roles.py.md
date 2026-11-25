# mcp/tests/test_paseo_launch_roles.py

## Governing Overview

[MCP test overview](overview.md)

## Purpose

The launch's role folders, agent identities and preparation failures against the fake bridge, and the child process the shared dispatch path prepares in.

## Code Commentary

`check_launched_agent` asserts the launched agent carries its folder, title, labels and reachable paths; the cases require one agent in its own folder for each of four launched roles and two taskless agents to coexist. `RolePreparationChildTests` replaces the child process and requires the shared dispatch path to prepare Worker and Reviewer in the existing child without adopting the caller's lifecycle, sequential fresh leaves to preserve the caller's binding, and a child that refuses, fails or does not end to refuse the launch.

The full-create-payload expectation for Architect, Orchestrator, Manager and Worker includes each seat's Codex grant, which is that role's own allowlist (`tools_for_role(role)`) on the bound task server. The separate grant test in [the catalog fixture](test_paseo_catalog_r71.py.md) checks all seven role options.

## Invariants And Boundaries

Preparation happens in the child and the caller's lifecycle binding is not adopted: a sequential launch is judged by the binding it still holds. A child that does not end is a refusal, not a success.

## Evidence

### Repo-Internal References


- Architect, Orchestrator, Manager and Worker each get one agent in their own folder with title, labels and reachable paths. The fixture checks each complete Codex create input. [1]





- The shared dispatch path prepares Worker and Reviewer in the existing child, and a refusing, failing or unfinished child refuses the launch. [2]



- The launch-file census includes fixture task documents and published copies. [3]



- Sequential child preparation leaves the caller's binding environment exact. [4]
