# mcp/src/agents_remember/cli/paseo_role_caller.py

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

Owns caller identity, message limits and shared runtime refusals.

## Code Commentary

### Logic

`_caller` requires a valid AR role binding and a configured runtime. `starting_agent` records the most specific bound task identity or Projects; unreadable task text retains its reference. `sender_line` renders that identity. `role_message_limit` reads effective settings each call. These functions move from paseo_role_tools without changing their bodies or their refusal meanings.

## Repo-Internal References

- The source implements the behavior and boundaries described above. [1]

## Docs References

No domain-documentation source is configured for this repository.

## Cross-Repo References

No external repository is cited by this file card.
