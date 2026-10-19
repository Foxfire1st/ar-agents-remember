# mcp/src/agents_remember/worktrees/knowledge_gate.py

## Governing Overview

[worktrees route overview](overview.md)

## Purpose

**The mandatory invariant gate at the worktree layer's routes (MIK-R09).** Every route that commits or lands memory asks the gate before it moves anything. The gate ranks above this layer and is reached through `services.KnowledgeGatePort`; this module decides whether it applies, with marker probes that read no knowledge, refuses a converted route whose port is unbound, and owns the closeout's own write: the memory commit that publishes a leaf sets `closed: true` in its history file. It also keeps a direct landing's closing across calls in per-generation receipts until that generation is decided, and since MIK-R124 it answers the landing routes' stale-document field (`landing_document_answer`).

## Code Commentary

**A contract that carries the removed mode is never "nothing to judge".** `leaf_cutover_refusal`, `leaf_gate_refusal`, and `direct_gate_verdict` each refuse a disabled contract with the opt-out refusal first, before any probe. An external contract with no converted side meets the unconditional legacy-format refusal; absence of converted memory elsewhere is not a gate exemption. A disabled contract remains refused by its distinct mode boundary before the marker probe.

Otherwise the gate is unchanged. **Applicability (rule 6).** `converted_memory(repository, *treeishes)` is true when any named side holds `knowledge/layout.json`; a side Git cannot read raises `GateProbeError`, never "unconverted". The cutover lock refuses every unconverted operational input, naming crossing sync or the first-conversion procedure as applicable. **No bypass (rule 5).** `GATE_UNBOUND`: a converted route with no bound `knowledge_gate` is refused. No function takes a flag that skips the gate.

`parent_memory_tip(contract)` is the tip of `memory_source_branch`, the validator's base for a leaf. `leaf_gate_refusal` is the closeout validator's gate: probe, port, then the tip, then `port.leaf_refusal`. `direct_gate_verdict` probes the candidate tree and `HEAD`, then forwards optional `leaf_id` to `port.direct_verdict`. Landing callers can suppress worklist persistence without suppressing judgment. `landing_gate_refusal` probes the landed memory commit and its bases, then runs the validator.

`landing_document_answer(contract, code_commit=…, memory_commit=…, master_end=False)` is the stale-document field the landing routes' answers carry (MIK-R124 rule 4): the count of documents the landing made stale — stale at its tip and current or without a record at its base — and the read that lists them, absent where there are none. It answers `None` on an unconverted line, and a state it cannot compute is answered `uncomputable` with its detail and refuses nothing here. `master_end=True` is the master's own line: every document is examined, and one already stale at the base is named as well (`answer(name_already_stale=master_end)`), so a series landing catches the debt a net-zero change would hide. The exclusive prepared-closeout refusal/lock and its unclosable-history constant were removed; the ordinary gate, cutover, closing and receipt owners survive.

`close_owner_history(memory_root, owner)` sets `closed: true` in the owner's latest history file and returns a `HistoryClosing` whose `restore()` returns whether it restored owned bytes, preserving a concurrent edit instead of overwriting it. A direct landing's closing outlives the call in per-generation receipts (`keep_direct_closing` / `forget_direct_closing` / `settle_direct_closing`); a restore happens only while the file's bytes still equal the closed bytes, so a later edit is never overwritten. A probe Git cannot answer is never unconverted memory.

## Evidence

- Disabled contract refused before the cutover probe [19]


- Disabled contract refused before the validator gate [21]


- Disabled contract refused before the direct verdict [22]

- Conversion probe reads one marker, nothing else [23]
