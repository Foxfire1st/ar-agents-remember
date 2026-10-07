# mcp/src/agents_remember/kernel/coordination_context/resolver.py

## Governing Overview

[coordination_context overview](overview.md)

## Purpose

Detects which memory root a code repository uses and assembles the `CoordinationContext`: roots, settings,
storage and path rules, cross-repository settings, and the facts of a worktree contract when the request
selects one. The resolver reads; it initializes no memory, writes no file and moves no branch.

## Code Commentary

### Selection

`detect_coordination_selection(name, code_root, requested_topology, coordination_root_hint, settings_path)`
returns a `CoordinationSelection` (topology, coordination root, memory root, settings path).

1. `_selection_roots` computes the coordination root, the external root
   `<coordination root>/memory-repos/ar-<name>` and the two paths of the removed repository-sidecar layout.
2. A requested topology is narrowed first (`require_supported_topology`), so a request for `internal` is
   refused by name before any root is inspected.
3. An explicit `settings_path` selects through `memory_roots_from_settings`; a memory root that does not
   exist raises `MissingMemoryError`.
4. Without one, an existing `<code root>/ar-memory` is refused as the removed mode, naming that path.
5. A requested `external` topology requires the external root. Without a request the external root is
   selected when it exists. In every other case `MissingMemoryError` names the coordination root and the
   external root.

The only topology is `external`.

### Context

`resolve_coordination_context(name, workspace_root, code_root, *, request)` requires
`request.contract_reader`. `request.hints.onboarding_root` selects `_context_from_onboarding_root`;
otherwise `_context_from_selection` runs the selection above. In that second path the coordination root
comes from the selected contract when `selector.contract_path` exists and loads
(`_contract_coordination_root`); a contract that is missing or fails to load leaves the hint in place.

`build_coordination_context` resolves the contract through `resolve_contract` and fills the context. The
task root, worktree group, memory mode, worktrees and ledger path come from the contract when there is one.
The effective memory root is the contract's memory worktree when it has one. `system_root` and the docs
root fall back to the coordination root's `system` and `docs` when the memory root has none. The onboarding
root is the effective memory root's `onboarding` directory when it exists and the selected root's otherwise.
Cross-repository settings are resolved against the workspace and the coordination root.

### What is recorded

The selection path performs its path operations through the kernel's read recorder:

- the existence of the external root, of the removed `<code root>/ar-memory` root and of a memory root
  implied by explicit settings: `observed_path_exists`, one `exists:` row each;
- the resolution of an explicit settings path, and of a contract path before it is loaded:
  `observed_resolve`, one `resolve:` row each;
- the probe of the contract path in `_contract_coordination_root`: `observed_exists`.

Inside a recording block a computation that selected its memory root this way keeps these rows with its
result, so the result is recomputed when a root appears, disappears or is retargeted, also when the new
target holds settings with identical bytes. A probe that raises is recorded as `unreadable (...)` and the
error is raised. Outside a recording block the resolver records nothing and its answers and errors are the
same. The path through an onboarding-root hint and the fallbacks of `build_coordination_context`
(`_system_root`, `_effective_child_root`, `_existing_path_settings`) use plain path calls and record
nothing for those probes and resolutions. What they consume downstream is still recorded: the settings
parsers record the settings they read, `build_coordination_context` resolves the contract through the
recorded contract resolver, and the included-memory adjacent-repository path records the ledger it loads
(or its absence or failure). The three pre-request context selections of the admitted B5 limitation —
settings presence in `contract_context`, the code root in `_resolve_code_repository` and the task root in
`resolve_terminal_leaf_doc` — remain outside the recording contract; this correction neither moves nor
widens that exception.

## Evidence

- The selection order: request, explicit settings, removed layout, external root, missing memory. [4]
- An existing repository-sidecar root is refused by its path. [5]
- The four roots a selection starts from. [6]
- Explicit settings must imply an existing memory root. [7]
- The public entry requires a contract reader and branches on the onboarding-root hint. [8]
- The selection path of the context. [9]
- The coordination root of a selected contract, with the path probe and resolution recorded. [10]
- The context is filled from roots, settings and the optional contract. [11]
- Root absence, appearance, retargeting and removal each recompute a kept view; a present removed root is refused by name. [12]
- A root probe that raises is recorded as unreadable and nothing is kept. [13]
- The fallback context reads the contract and records the bytes consumed. [14]
- The onboarding gate's settings resolution records the absent memory settings and the contract it read, and no file it did not open. [15]
