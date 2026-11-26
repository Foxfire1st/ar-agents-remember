# mcp/src/agents_remember/application/provider_runtime.py

## Governing Overview

[overview.md](overview.md)

## Purpose

This card records the retirement of `mcp/src/agents_remember/application/provider_runtime.py`. The `261125-DEP-L2` candidate (`DEP-R02@v1`, `DEC-ZGGT0G`) deleted this source file as part of removing the CodeGraphContext and GrepAI search providers and dead code. This file is retained only as a retirement record and grants no current contract, symbol, or route.

Its surviving `remove_tree` helper moved to [worktrees/modules/filesystem.py](../worktrees/modules/filesystem.py.md) under `261125-DEP-L2` (`DEP-R02@v1`); leftover `<group>/provider-runtime` directories are reclaimed directly during cleanup and abandon (`INV-FBATD2`).
