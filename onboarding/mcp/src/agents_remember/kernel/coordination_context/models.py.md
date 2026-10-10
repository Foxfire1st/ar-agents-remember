# mcp/src/agents_remember/kernel/coordination_context/models.py

## Governing Overview

[coordination_context overview](overview.md)

## Purpose

`models.py` owns the dataclasses and typed dictionaries returned or consumed by the coordination-context resolver.

## Code Commentary

The module defines missing-memory errors, storage/path-rule model types, cross-repo allow state, coordination selection, and the final `CoordinationContext` dataclass.

`CoordinationContext.memory_mode` uses the shared `ReadableMemoryMode` alias from `kernel.memory_mode`: the contract's own recorded mode, so a legacy `disabled` contract still reports itself as it is today. The resolver assembly (`build_coordination_context`) reads `contract.memory_mode` straight into this field when a contract exists, and calls `_memory_mode(roots.topology)` — which now always yields `external` — only when there is no contract.

It also owns the four frozen parameter objects the resolver's public API is signed on. They are the vocabulary of coordination-context resolution; a caller building one is answering one question, not filling in a keyword list: `EnclosureSelector` (how a caller names the enclosure to resolve, directly by contract path or indirectly by task plus leaf id or worktree name), `CoordinationHints` (what a caller already knows about where the coordination tree is; every field is a hint, not a fact), `CodeRepository` (a resolved code repository), and `CoordinationRoots` (the coordination tree after resolution: which topology won and the four roots it implies). All four are re-exported from the `kernel.coordination_context_resolver` facade.

Models stay behavior-light and importable by parser, resolver, and serialization modules. `MissingMemoryError` subclasses `AgentsRememberError`, so it joins the package's typed error family while staying catchable by existing `except ValueError` handlers.

## Evidence

- Context carries the readable mode vocabulary [7]
- Selector names the enclosure one way [8]
- Hints short-circuit detection [9]
- Resolved code repository record [10]
- Resolved coordination tree record [11]
- Missing memory stays a typed, catchable error [12]
