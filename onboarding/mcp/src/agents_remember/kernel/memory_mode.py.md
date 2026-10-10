# mcp/src/agents_remember/kernel/memory_mode.py

## Governing Overview

[MCP package overview](../../../overview.md)

## Purpose

The one declaration of the supported memory topology and memory mode, the readable vocabulary for contracts already on disk, and the two refusals for the removed modes. `disabled` — a task running with no memory at all — was removed from the product (MIK-R50): a task in it can be neither closed out, synced, integrated nor landed, so no task may opt out of memory. The module also names the two directories of the removed repository-sidecar layout, so existing state can be detected and reported at an exact path. It writes nothing.

## Code Commentary

**Vocabulary.** `Topology` is the literal `external`. `MemoryMode` is `external` alone: what a started task does with memory. `ReadableMemoryMode` is `external` or `disabled`: what a contract on disk may carry, so status, attach, and guarded abandon can still read a legacy contract while nothing may start in the removed mode or write it anew. `SUPPORTED_TOPOLOGIES`, `SUPPORTED_MEMORY_MODES`, and `READABLE_MEMORY_MODES` are derived from the literals with `get_args`, so the tuple a refusal prints cannot drift from the type a caller is narrowed onto. `REMOVED_MEMORY_MODES` is `("internal", "disabled")`: a positive statement of what was removed, not an absence, which is what lets detection and refusal be by name.

**Two refusals, never crossed.** `internal` keeps its own unsupported-mode refusal (`memory_mode_refusal_message` builds the one text, `memory_mode_refusal` wraps it in `MemoryModeUnsupportedError`, `memory_mode_refusal_fields` returns the same facts as a mapping for surfaces that answer with a result). `disabled` is refused with the opt-out refusal (`disabled_opt_out_detail`, `disabled_opt_out_refusal`, `disabled_opt_out_refusal_fields`, typed as `MemoryOptOutRefusedError` with status `memory-opt-out-refused`), which names the contract and the mode it carries, the true reason, and the known way out — start again in the default mode, or abandon the legacy contract and start again — and never asks for a developer decision. `refuse_removed_memory_mode` routes by name: `disabled` gets the opt-out refusal, every other removed member gets the `internal` text, because answering `disabled` with the `internal` text would blame a memory root inside the code repository that was never the problem.

**Narrowing.** `require_supported_memory_mode` and `require_supported_topology` refuse a removed member by name through its typed error first, and raise a plain `ValueError` for any other unknown token. That ordering is the whole point: a caller comparing strings inline would answer a removed token and a typo with the same message, which is how a removed mode quietly degrades into "just invalid input".

**Legacy paths.** `LEGACY_INTERNAL_MEMORY_DIRNAME` is `ar-memory` and `LEGACY_INTERNAL_COORDINATION_DIRNAME` is `ar-coordination`. `legacy_internal_memory_root(code_root)` returns the resolved path of `<code root>/ar-memory` through `observed_resolve`; `legacy_internal_coordination_root` resolves `<code root>/ar-coordination` without recording. Neither function creates, reads, or migrates such a root.

**Existing state is reported, never rewritten.** The module names and detects removed layouts and modes; it never migrates one. No code path here writes to a contract, a settings file, or a memory root.

## Evidence

- Supported topology is `external` only [36]
- Supported mode is `external` alone [37]
- On-disk contracts may still carry `disabled` [38]
- Both removed members declared positively [39]
- The one route out, stated once for every surface [40]
- Removed roots resolved only to be reported [41]
- Removed modes refused by name, `disabled` via opt-out [42]
- Opt-out text names contract, reason, and way out [43]
- Removed member refused by name, typo is invalid input [44]
- Same removal-versus-typo distinction for topology [45]
