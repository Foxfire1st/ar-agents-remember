# mcp/src/agents_remember/cli/paseo_command.py

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

Owns the command runner for npm and the pinned Paseo management CLI.

## Code Commentary

PaseoCli addresses every command with the configured home and removes inherited PASEO variables. It does not import the agent client or identify/signals processes by port. Command results and parse failures become bounded named runtime failures, allowing tests to replace this one runner.

## Evidence

- Frozen implementation of run_command supporting the stated file behavior. [1]
- Frozen implementation of PaseoCli supporting the stated file behavior. [2]
- Frozen implementation of parse_json_output supporting the stated file behavior. [3]
