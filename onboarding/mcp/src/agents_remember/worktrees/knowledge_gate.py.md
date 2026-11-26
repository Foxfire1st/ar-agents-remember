# mcp/src/agents_remember/worktrees/knowledge_gate.py

## Governing Overview

[worktrees route overview](overview.md)

## Purpose

**The mandatory invariant gate at the worktree layer's routes (MIK-R09).** Every route that commits or lands memory asks the gate before it moves anything. The gate ranks above this layer and is reached through `services.KnowledgeGatePort`; this module decides whether it applies, with marker probes that read no knowledge, refuses a converted route whose port is unbound, and owns the closeout's own write: the memory commit that publishes a leaf sets `closed: true` in its history file. It also keeps a direct landing's closing across calls in per-generation receipts until that generation is decided, resolves a master's standing document base (`master_document_base`), and answers the landing routes' stale-document field (`landing_document_answer`).

## Code Commentary

**A contract that carries the removed mode is never "nothing to judge".** `leaf_cutover_refusal`, `leaf_gate_refusal`, and `direct_gate_verdict` each refuse a disabled contract with the opt-out refusal first, before any probe. An external contract with no converted side meets the unconditional legacy-format refusal; absence of converted memory elsewhere is not a gate exemption. A disabled contract remains refused by its distinct mode boundary before the marker probe.

**Applicability (rule 6).** `converted_memory(repository, *treeishes)` is true when any named side holds `knowledge/layout.json`; a side Git cannot read raises `GateProbeError`, never "unconverted". The cutover lock refuses every unconverted operational input, naming crossing sync or the first-conversion procedure as applicable. **No bypass (rule 5).** `GATE_UNBOUND`: a converted route with no bound `knowledge_gate` is refused. No function takes a flag that skips the gate.

`parent_memory_tip(contract)` is the tip of `memory_source_branch`, the validator's base for a leaf. `leaf_gate_refusal` is the closeout validator's gate: probe, port, then the tip, then `port.leaf_refusal`. `direct_gate_verdict` probes the candidate tree and `HEAD`, then forwards optional `leaf_id` to `port.direct_verdict`. Landing callers can suppress worklist persistence without suppressing judgment. `landing_gate_refusal` probes the landed memory commit and its bases, then runs the validator.

`master_document_base(contract, *, code_commit, memory_commit)` resolves a master's standing document base by walking `contract.sync_log` newest to oldest: a `repository-default` entry supplies `(codeSourceCommit, memorySourceCommit or memoryBaseTo)` (falling back to `memoryBaseTo` when memory sync was skipped), and any other entry supplies `(codeBaseTo, memoryBaseTo)`. It returns the first pair whose code and memory commits are both ancestors of the judged `(code_commit, memory_commit)` pair, falling back to `original_base_pair(contract)` when no synced pair qualifies.

`landing_document_answer(contract, code_commit=…, memory_commit=…, master_end=False)` builds the stale-document field a landing answer carries (MIK-R124 rule 4): it returns `None` on an unconverted line, answers `{"state": "uncomputable", "detail": ...}` on a `GateProbeError`, and otherwise calls `document_staleness(..., full=master_end).answer(name_already_stale=master_end)`. When `master_end=True`, it also passes `series_contract` (when present) and `document_base=master_document_base(contract, code_commit=code_commit, memory_commit=memory_commit)` so every document is examined against the standing base with own-leaf attribution, parent-line repair checks, and per-kind answer sections.

`close_owner_history` closes the owner's latest history file, creating one for an owner without history. The same update can add the review fact already qualified by the closeout caller. An already closed file remains byte-identical. It returns a `HistoryClosing` whose `restore()` returns whether it restored owned bytes, preserving a concurrent edit instead of overwriting it. A direct landing's closing outlives the call in per-generation receipts (`keep_direct_closing` / `forget_direct_closing` / `settle_direct_closing`); a restore happens only while the file's bytes still equal the closed bytes, so a later edit is never overwritten. A probe Git cannot answer is never unconverted memory.

## Evidence

- Disabled contract refused before the cutover probe [19]



- Disabled contract refused before the validator gate [21]



- Disabled contract refused before the direct verdict [22]

- Conversion probe reads one marker, nothing else [23]

- The owner history closing adds an eligible review fact only in the same write that closes the file. [25]

- `master_document_base` walks `contract.sync_log` newest to oldest for the latest synced pair whose code and memory commits are both ancestors of the judged pair, handling `repository-default` entries and falling back to `original_base_pair`. [26]
- `landing_document_answer` passes `series_contract` and `document_base=master_document_base(...)` when `master_end=True` and delegates to `document_staleness(..., full=master_end).answer(name_already_stale=master_end)`. [27]
