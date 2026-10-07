# mcp/src/agents_remember/kernel/memory_mode.py

## Governing Overview

[MCP package overview](../../../overview.md)

## Purpose

The one declaration of the supported memory topology and memory mode, and the one refusal for the removed
mode `internal`. The module also names the two directories of the removed repository-sidecar layout, so that
existing state can be detected and reported at an exact path. It writes nothing.

## Code Commentary

- **Vocabulary.** `Topology` is the literal `external`. `MemoryMode` is `external` or `disabled`.
  `SUPPORTED_TOPOLOGIES` and `SUPPORTED_MEMORY_MODES` are derived from the literals with `get_args`.
  `REMOVED_MEMORY_MODES` is `("internal",)`.
- **Refusal.** `memory_mode_refusal_message` builds the one text: the removed mode, the artifact that records
  it when one is given, the supported modes and the two remedies of `MEMORY_MODE_REMEDIES`.
  `memory_mode_refusal` wraps it in `MemoryModeUnsupportedError`, `memory_mode_refusal_fields` returns the
  same facts as a mapping for a surface that answers with a result, and `refuse_removed_memory_mode` raises
  it.
- **Narrowing.** `require_supported_memory_mode` and `require_supported_topology` refuse a removed member by
  name through the typed error first, and raise a plain `ValueError` for any other unknown token.
- **Legacy paths.** `LEGACY_INTERNAL_MEMORY_DIRNAME` is `ar-memory` and
  `LEGACY_INTERNAL_COORDINATION_DIRNAME` is `ar-coordination`. `legacy_internal_memory_root(code_root)`
  returns the resolved path of `<code root>/ar-memory` through `observed_resolve`: inside a recording block
  the resolution is recorded as a `resolve:` row with the unresolved absolute path as key, and outside one
  the function returns the same path and records nothing. `legacy_internal_coordination_root` resolves
  `<code root>/ar-coordination` without recording. Neither function creates, reads or migrates such a root.

## Evidence

- The two literals, their derived tuples and the removed set. [14]
- The remedies stated once for every refusal. [15]
- The removed memory root's path is resolved through the recorder. [16]
- The removed coordination root's path is resolved without recording. [17]
- The one refusal text. [18]
- The typed refusal. [19]
- A removed mode is refused by name before the supported set is tested. [20]
- The same order for a topology. [21]
- An existing repository-sidecar root is refused by name with its path, and its presence, absence and retargeting are recorded. [22]
