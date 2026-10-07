# mcp/src/agents_remember/kernel/coordination_context/contracts.py

## Governing Overview

[coordination_context overview](overview.md)

## Purpose

Finds and loads the worktree contract of a resolution request. The kernel sits below the `worktrees`
package, so every contract operation goes through the injected `ContractReaderPort`; this module only
decides which candidate path to try and what to return when it cannot be loaded.

## Code Commentary

`resolve_contract(selector, coordination_root, code_repository_name, reader)` returns `(contract, path)`.

1. An explicit `selector.contract_path` is resolved with `observed_resolve` and is the candidate.
2. Without one, `selector.task_name` asks `reader.find_task_contract`, with `parent_task` and `leaf_id`
   passed on.
3. Without a candidate so far, `selector.worktree_name` asks `reader.find_worktree_contract`.
4. No candidate gives `(None, None)`. A candidate that does not exist (`observed_exists`) gives
   `(None, candidate)`. A candidate whose load raises any exception gives `(None, candidate)` too, so the
   caller can report the path it tried. Otherwise the loaded contract is returned with its path.

The two path operations go through the kernel's read recorder. Inside a recording block the resolution of an
explicit contract path is recorded as a `resolve:` row keyed by the absolute, unresolved path, and a missing
candidate is recorded as `absent`. A symbolic link that is retargeted between two resolutions of one computation therefore
shows as a conflict, and a kept result is not reused after the link moved. Outside a recording block the
function records nothing and behaves as `Path.resolve()` and `Path.exists()` do. The contract's bytes are
recorded by the loader behind the port.

The module creates and changes no contract.

## Evidence

- The candidate order, the recorded resolution and existence probe, and the three empty answers. [4]
- The recorded resolution keeps the absolute, unresolved path as its key. [5]
- A contract link retargeted during a computation is recorded as a conflict and the result is not kept. [6]
