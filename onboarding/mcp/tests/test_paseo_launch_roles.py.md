# mcp/tests/test_paseo_launch_roles.py

## Governing Overview

[MCP test overview](overview.md)

## Purpose

The launch's role folders, agent identities and preparation failures against the fake bridge, and the child process the shared dispatch path prepares in.

## Code Commentary

`check_launched_agent` asserts the launched agent carries its folder, title, labels and reachable paths; the cases require each role class to get one agent in its folder and two taskless agents to coexist. `RolePreparationChildTests` replaces the child process and requires the shared dispatch path to prepare Worker and Reviewer in the existing child without adopting the caller's lifecycle, sequential fresh leaves to preserve the caller's binding, and a child that refuses, fails or does not end to refuse the launch.

## Invariants And Boundaries

Preparation happens in the child and the caller's lifecycle binding is not adopted: a sequential launch is judged by the binding it still holds. A child that does not end is a refusal, not a success.

## Evidence

### Repo-Internal References

- Each role class gets one agent in its own folder, with title, labels and reachable paths. [1]


- The shared dispatch path prepares Worker and Reviewer in the existing child, and a refusing, failing or unfinished child refuses the launch. [2]
- The launch-file census includes fixture task documents and published copies. [3]
- Sequential child preparation leaves the caller's binding environment exact. [4]
