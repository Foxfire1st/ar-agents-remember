# mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/capsule-budgets.json

## Governing Overview

[MCP package overview](../../../../../../overview.md)

## Purpose

Generated package-data copy of the canonical capsule-budget registry. It carries no contract of its own; the canonical `skills/l-01-agent-lifecycles/capsule-budgets.json` with its card owns the budgets.

## Code Commentary

`scripts/sync-skills.py` regenerates this copy byte-identical from the canonical source; `sync-skills.py --check` passes 9/9. Never hand-edit a generated copy.

## Evidence

- This copy is byte-identical to the canonical registry, which owns the contract. [1]
- The canonical registry records all 38 ceil(raw*11/10) budgets. [2]
