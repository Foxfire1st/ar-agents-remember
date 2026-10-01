# mcp/src/agents_remember/worktrees/modules/closeout_lineage.py

## Governing Overview

[worktree modules overview](overview.md)

## Purpose

Owns the self-healing guard clause for the closeout-family source-lineage boundary. The closeout
entry points prove their full transitive super → master → leaf ancestry before touching Git; this
module decides whether a stale break is carried downstream by the existing `worktree_sync`
transaction or refused. It carries what the sync can settle and refuses only what it cannot.

## Code Commentary

### Logic

`heal_current_source_lineage(contract, operation=..., dry_run=...)` projects the lineage with
`source_lineage_for_contract`. A projection that already satisfies `lineage_refusal` is returned
unchanged, with the caller's contract. Otherwise `_require_settleable` runs first: an
`unavailable` edge (absent/unreadable contract, absent branch, organizational source that is not the
sprint `integrationBranch`, or a comparison Git could not make) refuses immediately with the
escalation duty, and a `dry_run` caller refuses with the preview duty while mutating nothing.

For a settleable break the module runs `sync_result(WorktreeArgs(contract_path=...))` for each
contract in the projection's own ordered `recoveries` — the contract that owns each stale edge — via
`_sync_stale_edge`. The reloaded contract is then read back with `load_contract` and re-projected,
because `finalize_sync` rewrites the base pair on disk; the healed contract identity, not the stale
in-memory object, is what `HealedSourceLineage.contract` returns.

The trigger is `behind > 0`, not the coarse state label. `ahead` is the work branch's own normal
work, so a `diverged` edge (both `behind` and `ahead`) is an ordinary stale edge and is carried; the
sync fast-forwards where the descendant has no own commits and merges where it does. A leaf that
owns its own commit is therefore the normal case, not a refusal.

Three outcomes leave the sync route without continuing. A sync that reports the retained
`sync-resolution-required` state raises `_retained_conflict` →
`source-lineage-sync-conflict`, carrying the sync's `resolution` block and its
`continue_sync_resolution` next operation so the agent resolves in the exact reported worktree. A
sync that returns nonzero for any other reason raises `_sync_refused` →
`source-lineage-sync-refused`, which names the reported sync state and points at
`worktree_sync` for the owning contract. A sync that succeeds but leaves the lineage stale raises
`_still_stale`, which keeps today's stale detail and tells the caller to sync the remaining ordered
parent edges.

### Conventions

The module owns the closeout-family guidance text and refusal statuses as module constants
(`_RESOLUTION_DUTIES`, `_DIVERGENCE_DUTY`, `_PREVIEW_DUTY`, `_SYNC_REFUSED_DUTY`,
`_RETAINED_CONFLICT_STATE`). `_refusal` is the single refusal shape: it prefixes the existing lead
sentence (`<operation> requires current transitive source lineage (<status>): <detail>`) and appends
the guidance to both the `RuntimeError` message and the structured `payload`, so an MCP tool that
renders only the message still states the whole duty.

`SourceLineageRefusal` extends `RuntimeError` so every existing closeout-family caller keeps its
refusal contract while gaining typed `status` and `payload`. The transition guidance is unchanged
in shape from the previous `require_current_source_lineage` message.

`replay` is deliberately untouched by this module. It remains a real, supported integration
strategy and the memory-carryover vehicle; only the ancestor-moved refusal's next-step guidance
moved to `worktree_sync` plus a new targeted closeout.

### Invariants And Boundaries

- This module mutates Git only through the existing journaled sync transaction; it never moves a
  branch itself, never creates a second transaction or store, and never invents a strategy.
- `dry_run` observes only: it refuses with the preview duty and mutates nothing.
- An unprovable projection escalates to the human developer; a carried merge is a mechanical
  settlement, but a missing contract, branch, or comparison is not settleable by an agent.
- A retained sync conflict hands back the sync worktrees and their resolution duties; the closeout
  completes for neither code nor memory while it stands.
- A leaf owning its own commit is normal — `behind > 0` is the trigger, never `ahead > 0`.
- The module returns the reloaded contract because the sync rewrites the base pair on disk; callers
  must re-prove immediate source heads against that identity.

### Todos

The door path (`integration/closeout/door_evidence.require_source_bases_current`) intentionally still
calls `require_current_source_lineage` unchanged: the door evidence also runs on the read-only
closeout-projection rebuild, so mutation rights there would let a projection sync Git. Wiring the
door declaration also needs the reloaded contract threaded into `_declare_generation`.

## Evidence

### Docs References

No Domain Documentation source is configured for this memory root.

### Repo-Internal References

- The heal entry point projects lineage, refuses the unsettleable, runs the existing sync for each stale edge's owning contract, and returns the reloaded contract identity. [1]
- Preview and unprovable projections are the only two pre-sync refusals. [2]
- A retained sync conflict, a refused sync, and a still-stale result each get their own typed status and duty set. [3]
- Every refusal shares one lead-sentence-plus-guidance shape and carries typed status/payload. [4]
- The projection, refusal vocabulary, and ordered sync recoveries this module consumes are owned by the lineage policy. [5]
- The projected state and its ordered `recoveries` are the shared wire model. [6]
- The heal runs the ordinary public sync result for the owning contract. [7]
- Closeout imports this module in place of the bare `require_current_source_lineage` guard at both entry points. [8]

### Cross-Repo References

No cross-repository source is configured for this memory root.
