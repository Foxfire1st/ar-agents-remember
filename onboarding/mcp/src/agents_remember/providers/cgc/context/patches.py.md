# mcp/src/agents_remember/providers/cgc/context/patches.py

## Governing Overview

[overview.md](overview.md)

## Purpose

`cgc/patches.py` owns marker-based CodeGraphContext patch application helpers
used to keep the Docker runner image patched consistently. L12 adds the watcher
timer-pop patch: fired debounce timers pop their own `self.timers` entry (identity
guarded against replacement-timer races) so the per-path dict stays bounded.

## Code Commentary

### Logic

It applies idempotent patches for `.cgcignore` handling, Windows delete-prefix
cleanup, C++/TableGen discovery, and visualizer routing/query behavior. The
module no longer discovers installed CGC modules from host venv layouts; the
managed patch application path belongs to the Docker runner image build.

### Invariants And Boundaries

- This file is part of the direct `providers.context` facade implementation; there is no `context_providers.py` compatibility fallback.
- Patch helpers operate on explicit files supplied by the Docker runner build
  or unit tests. They must not search a coordination-root host venv.

## Evidence

### Repo-Internal References

- The marker-based timer cleanup patch is owned here; no removed patch-helper test coverage is asserted. [1]
