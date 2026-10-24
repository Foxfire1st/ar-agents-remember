# mcp/tests/test_mik_r196_authority_replacement.py

## Governing Overview

[MCP test overview](overview.md)

## Purpose

Pins how the host authority block is created in the MCP settings file: once, without touching sibling files, and with a failed publication reported honestly rather than claimed.

## Code Commentary

The cases drive `establish_authority_paseo_runtime` in the authority module and read the result back through `load_paseo_runtime_settings`. An unreadable file is a modeled refusal with the unreadable code and also a config error; a symlinked authority is refused and its target's bytes are unchanged; an absent file is created while an existing block answers present with `changed` false and untouched bytes. Publication keeps sibling bytes and modes: the sentinel key survives, the target keeps its mode, a neighbouring init file keeps its bytes and mode, and no other name is left behind. A symlinked temporary candidate is refused through the real exclusive open, with the victim's bytes and mode intact. A parametrized case injects a failure at fsync, replace or cleanup and requires the refusal detail to name the actual target state, the temporary's state (absent or holding a block) and the injected error.

## Invariants And Boundaries

The refusal codes are part of the contract: unreadable, symlink and write-failed. No case accepts a refusal whose detail omits which file holds a block and where the temporary went, and none accepts a publication that changed file bytes it was not asked to change.

## Evidence

### Repo-Internal References

- An absent authority is created, an existing block answers present with nothing changed, and sibling bytes and modes survive publication. [1]

- A symlinked authority or temporary candidate is refused with its target untouched. [2]

- A publication failure at fsync, replace or cleanup names the target and temporary states in its detail. [3]
