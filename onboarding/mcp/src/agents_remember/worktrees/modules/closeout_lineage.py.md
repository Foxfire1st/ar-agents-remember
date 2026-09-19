# mcp/src/agents_remember/worktrees/modules/closeout_lineage.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/modules/closeout_lineage.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-10T15:06+02:00 |
| lastVerifiedCommitHash | `7879f5b22c34a912f939e27868786818463c3b9c` |
| lastVerifiedCommitDate | 2026-09-19T20:18:09+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No Domain Documentation source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The heal entry point projects lineage, refuses the unsettleable, runs the existing sync for each stale edge's owning contract, and returns the reloaded contract identity. | `heal_current_source_lineage`; `HealedSourceLineage` | mcp/src/agents_remember/worktrees/modules/closeout_lineage.py:60-65; mcp/src/agents_remember/worktrees/modules/closeout_lineage.py:81-109 |
| Preview and unprovable projections are the only two pre-sync refusals. | `_require_settleable` | mcp/src/agents_remember/worktrees/modules/closeout_lineage.py:112-125 |
| A retained sync conflict, a refused sync, and a still-stale result each get their own typed status and duty set. | `_retained_conflict`; `_sync_refused`; `_still_stale` | mcp/src/agents_remember/worktrees/modules/closeout_lineage.py:146-167; mcp/src/agents_remember/worktrees/modules/closeout_lineage.py:170-191; mcp/src/agents_remember/worktrees/modules/closeout_lineage.py:194-204 |
| Every refusal shares one lead-sentence-plus-guidance shape and carries typed status/payload. | `_refusal`; `SourceLineageRefusal` | mcp/src/agents_remember/worktrees/modules/closeout_lineage.py:68-78; mcp/src/agents_remember/worktrees/modules/closeout_lineage.py:207-226 |
| The projection, refusal vocabulary, and ordered sync recoveries this module consumes are owned by the lineage policy. | `source_lineage_for_contract`; `lineage_refusal` | mcp/src/agents_remember/worktrees/source_lineage.py:94-107; mcp/src/agents_remember/worktrees/source_lineage.py:110-122 |
| The projected state and its ordered `recoveries` are the shared wire model. | `SourceLineageProjection`; `SourceLineageRecovery` | mcp/src/agents_remember/models/worktree.py:134-140; mcp/src/agents_remember/models/worktree.py:112-119 |
| The heal runs the ordinary public sync result for the owning contract. | `sync_result` | mcp/src/agents_remember/worktrees/modules/sync.py:28-67 |
| Closeout imports this module in place of the bare `require_current_source_lineage` guard at both entry points. | `_validate_closeout_source_state`; `_revalidate_candidate` | mcp/src/agents_remember/worktrees/modules/closeout.py:338-350; mcp/src/agents_remember/worktrees/modules/closeout.py:641-653 |

## Cross-Repo References

No cross-repository source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History
- 2026-09-18T19:51:00+02:00 — 260915-KS-L23 residue clearance, seat B (uncommitted change set on `ar/260915-ks-l23`, memory base `59eab7a0`): **cleared the one enforced `citation_anchor_absent_from_range` row in this document.** The shared-wire-model row's `SourceLineageProjection` cell cited `models/worktree.py:120-128`, the recovery model's declared fields; `class SourceLineageProjection` now sits at `134-140`, which is what the cell cites. The `SourceLineageRecovery` cell at `112-119` and the claim are unchanged. No claim was re-worded, no anchor or range was dropped to silence a row, and no verification stamp advanced: the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-11T23:05:00+00:00: Curator citation reconciliation: `_revalidate_candidate`, `_validate_closeout_source_state` repointed to mcp/src/agents_remember/worktrees/modules/closeout.py:306-316, mcp/src/agents_remember/worktrees/modules/closeout.py:600-609. No content impact: mechanical anchor-range projection against citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `sync_result` repointed to mcp/src/agents_remember/worktrees/modules/sync.py:28-67. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-10T15:06+02:00 — Created for the closeout auto-carry change: the guard-clause heal helper that carries a settleable stale source break through the existing `worktree_sync` transaction instead of refusing, and escalates only an unprovable break. Source reviewed in the uncommitted working tree at base `4bbe2c37`; the new file has no committed identity yet, so verification remains closeout-owned.
