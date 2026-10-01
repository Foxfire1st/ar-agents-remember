# mcp/src/agents_remember/kernel/coordination_context/models.py

## Governing Overview

[coordination_context overview](overview.md)

## Purpose

`models.py` owns the dataclasses and typed dictionaries returned or consumed by
the coordination-context resolver.

## Code Commentary

### Logic

The module defines missing-memory errors, storage/path-rule model types,
cross-repo allow state, coordination selection, and the final
`CoordinationContext` dataclass (cit:(["class CoordinationContext"], mcp/src/agents_remember/kernel/coordination_context/models.py:189-189)).

`CoordinationContext.memory_mode` uses the shared `MemoryMode` alias declared here by
260731-EFA-L9 (cit:(["MemoryMode = Literal"], mcp/src/agents_remember/kernel/memory_mode.py:35-35))
and used by the field declaration (cit:(["memory_mode: MemoryMode"], mcp/src/agents_remember/kernel/coordination_context/models.py:211-211)).
The resolver assembly is named by **`build_coordination_context`** and selects the contract's mode
when a contract exists, otherwise calling `_memory_mode(roots.topology)` as its fallback
(cit:(["memory_mode = contract.memory_mode if contract is not None else _memory_mode(roots.topology)"], mcp/src/agents_remember/kernel/coordination_context/resolver.py:279-279)).

Since 260731-EFA-L2 it also owns the **four frozen parameter objects the resolver's public API is
signed on**. They are the vocabulary of coordination-context resolution; a caller building one is
answering one question, not filling in a keyword list:

- **`EnclosureSelector(contract_path=None, task_name=None, parent_task=None, leaf_id=None,
  worktree_name=None)`** — *how a caller names the enclosure to resolve*. Either directly, by
  `contract_path`, or indirectly: a task (with `parent_task` to disambiguate a repeated task name)
  plus the leaf id or worktree name that picks one enclosure inside it. A caller supplying a subset
  is still supplying one selector, and the whole set travels from the tool boundary down to
  `resolve_contract` unchanged.
- **`CoordinationHints(topology=None, coordination_root=None, settings_path=None,
  onboarding_root=None)`** — *what a caller already knows about where the coordination tree is*.
  Every field is a hint, not a fact: a requested topology overrides detection, an explicit
  coordination root or settings file short-circuits the search, and an `onboarding_root` selects
  the from-onboarding resolution path entirely. Detection fills in whatever is absent.
- **`CodeRepository(name, root, workspace)`** — a resolved code repository. This replaces the
  untyped `dict[str, Path | str]` the resolver used to pass around, which forced `Path(repo["root"])`
  / `str(repo["name"])` casts at every read.
- **`CoordinationRoots(topology, coordination_root, memory_root, onboarding_root, settings_path)`**
  — the coordination tree after resolution: which topology won and the four roots it implies.
  Detection produces them together and no reader wants a subset.

All four are re-exported from the `kernel.coordination_context_resolver` facade.

### Invariants And Boundaries

- Models should stay behavior-light and importable by parser, resolver, and
  serialization modules.
- **`memory_mode` uses the shared vocabulary.** `MemoryMode`, cit:(["MemoryMode ="], mcp/src/agents_remember/kernel/memory_mode.py:35-35), is the kernel-owned declaration this module imports for its `memory_mode` field, and `resolver.build_coordination_context`, cit:(["def build_coordination_context"], mcp/src/agents_remember/kernel/coordination_context/resolver.py:252-252), is the current assembly entry point.
- The four parameter objects are frozen and fully defaulted, so a resolver call that supplies
  neither `hints` nor `selector` still resolves — `None` is replaced by an empty instance rather
  than branching on absence.
- `MissingMemoryError` subclasses `AgentsRememberError` (imported from
  `agents_remember.errors`), so it joins the package's typed error family while
  staying catchable by existing `except ValueError` handlers. It keeps the
  checked internal and external memory paths so callers can report actionable
  initialization guidance, naming the skills in full — initialize memory with
  `c-00-initialize-memory-repo`, then run `c-03-repo-bootstrap`.

## Evidence

### Docs References

No external documentation is needed for these package-local data models.

No relevant external documentation is needed.

### Repo-Internal References

- `MissingMemoryError` subclasses the typed `AgentsRememberError` base. [1]
- `AgentsRememberError` remains a `ValueError`-compatible base. [2]
- Resolver assembly returns `CoordinationContext` instances defined here, reading `contract.memory_mode` straight into the field and falling back to the topology only when there is no contract. [3]
- `MemoryMode` is the two-member memory vocabulary declaration (`external`, `disabled`), declared in the kernel memory-mode module. [4]
- The wire face of the same value imports and uses the shared alias for `memory.mode`. [5]
- Serialization converts these models to JSON-safe dictionaries. [6]

### Cross-Repo References

No cross-repository evidence is needed for local model declarations.

No meaningful cross-repo references found.
