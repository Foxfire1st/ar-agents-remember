# mcp/src/agents_remember/kernel/primitives/paseo_authority.py

## Governing Overview

[overview](overview.md)

## Purpose

The one installation-wide host authority, shared by every harness.

## Code Commentary

`paseo_runtime_path` names `<coordinationRoot>/system/settings.json`; `load_shared_paseo_runtime` reads and parses the block on every use and returns `None` when the file or block is absent. `warn_per_harness_paseo` states that an old per-harness block is ignored, with the exact migration instruction and no fallback.

## Evidence

- The shared path. [1]
- The per-use read of the shared block. [2]
- The no-fallback migration warning. [3]
