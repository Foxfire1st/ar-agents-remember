# skills/c-09-git-worktree-manager

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `skills/c-09-git-worktree-manager` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-09-15T00:56:17+00:00 |
| lastVerifiedCommitHash |  `420669c459aab3650cdaa5b3e5271e71d7d94c0e`|
| lastVerifiedCommitDate |  2026-09-17T10:54:08+02:00|
| reviewedWorkingCandidate | `ar/260913-lca-l9` uncommitted source; base `bb65a2073228c5e143b055a470f39c6c9e2f4d9d` |

## Purpose

This route owns the agent-facing Git worktree lifecycle: start, attach, status, source-pair
selection, resumable synchronization, closeout routing, integration, finalization, cleanup,
abandonment, and reopen recovery. The skill describes public contract-addressed operations; it does
not move private journal, ref, or queue identity into agent prompts.

## Hot Path Summary

Closeout, sync, checkpoint and integration bind the actual code/memory refs and content. Ledger cache files remain available for downstream readers; their missing/stale/malformed state cannot block these operations or request another commit.

## Detailed Route Context

Atomic-series admission is a contract-scoped authority: each canonical series contract owns its own
activation record, so masters that share one exact code/memory source pair never share that state.
Manager dispatch, worker dispatch, and atomic start/attach are selecting operations; reviewer and
curator inspection is not. Selection publishes `reconciling` for that exact contract, which suspends
nothing — not its chat, process, worktree, contract, or already-claimed lifecycle journal — then
reconciles both protected source tips and publishes `active` only when they are current. One master's
selection never pauses or excludes another, and multiple nonterminal contracts remain valid. Task
authoring never consults the activation authority, and the closeout queue merely projects active,
reconciling, or vacant waiting candidates.

Nothing serializes a graph-less sprint. A sprint without an `executionGraph` declares no
dependencies, so the shipped `atomic-sequential` default describes the sprint's SHAPE — every
commanded master executes atomically — and is not a serialization mechanism: independent atomic
masters proceed concurrently and no master is held because another master is selected. Only an
explicit `executionGraph` gates masters on real predecessors.

`worktree_sync` is one durable enclosure-root transaction. It pins pre-sync heads and source tips,
retains code or memory conflicts in operation-owned `.sync` worktrees, and advertises
`resolution_action=continue|cancel` on the same contract. Continue validates staged resolution and
resumes; cancel restores pinned heads, removes retained temporary worktrees, terminalizes the
journal, and releases an exact reconciling selection to durable `vacant`. No direct-Git recovery,
tolerant reader, or contract-presence fallback is part of the doctrine. For external memory,
continuation proves the admitted Git history and leaves the ledger to its rebuild: the transaction
does not commit `memory.md` or use its rows as a Git guard. A row the
rebuild cannot resolve is reported as an exclusion. Repeated code commits are valid
newest-first state history; the newest row supplies current authority and older same-code rows
remain audit evidence.

Ordinary series integration records absent source-door authority as explicit `not-applicable` and
does not consult `directExecutionEnabled`. The policy-gated direct-landing route is only for an
explicitly selected leaf delivery without an enclosure; a fresh enclosed leaf continues to require
its exact claimed closeout source.

Terminal cleanup releases the exact selected contract before its authority can disappear. A newer
selection is never cleared by cleanup of an older contract. Integration conflicts are agent-owned
when current requirements and evidence determine the resolution; only genuine semantic ambiguity
returns through the architect.

## Conventions

- Address every operation by canonical enclosure contract, never by private operation id.
- Preview before live mutation; dry-run must leave selector, refs, journal, and worktrees unchanged.
- Treat the enclosure-root journal and pinned refs as durable recovery evidence.
- Route closeout sequencing to `c-12-closeout`; this skill resumes at integration/finalization.

## Invariants And Boundaries

- Each canonical series contract owns its own activation record; multiple nonterminal contracts
  remain valid and one master's selection excludes no other.
- Contract presence, task order, and queue rows never elect a selected master.
- Conflicts are retained, resumable, and cancellable; they are not silently aborted.
- Cleanup releases only the exact selected terminal pointer and preserves newer selections.
- No fallback reader or duplicated lifecycle evidence is allowed.
- Memory-merge validation proves Git state only: it requires no row list and never imposes global
  code-key uniqueness. A row the projection cannot resolve is the projection's to report.
- Ordinary series integration is never reclassified as direct execution merely because it uses a
  root series contract.


### Todos

Exact source claims and citations are reconciled to the frozen canonical skill; verification
metadata awaits the real code commit.


## CCR-R12@v5 Transaction Boundary

Closeout and integration are authorized Git transactions over code and memory-content legs, followed by best-effort consumer-cache refresh. Their transaction-owned commit legs suppress automatic quality and test hooks; ordinary explicit Git hook policy outside closeout/integration remains unchanged. Preview, conflict, and ref safeguards remain in this route; quality, tests, memory-quality, certification, and review operations are contextual or explicit rather than automatic.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The canonical skill owns contract-scoped admission, resumable sync, integration conflict ownership, and exact terminal release doctrine. | `## Mid-Task Sync`; `## Lifecycle Finalization And Cleanup` | skills/c-09-git-worktree-manager/SKILL.md:256-303; skills/c-09-git-worktree-manager/SKILL.md:433-512 |
| Ordinary series integration and leaf direct landing remain distinct policy routes. | "An ordinary master/series integration has no leaf closeout door of its own"; `directExecutionEnabled` | skills/c-09-git-worktree-manager/SKILL.md:381-384; skills/c-09-git-worktree-manager/SKILL.md:383-383 |
| The graph-less atomic-sequential default describes sprint shape and serializes nothing between the masters. | "nothing serializes the masters" | mcp/src/agents_remember/worktrees/queue/closeout_queue_graph.py:162-162 |
| Public sync composes the selection and transaction owners without exposing private ids. | `sync_result` | mcp/src/agents_remember/worktrees/modules/sync.py:28-67 |
| Stable operation recovery is stored below the enclosure root. | `SyncOperationStore` | mcp/src/agents_remember/worktrees/sync_transaction_state.py:172-366 |

Current working-candidate evidence for this route:

| Finding | Anchor | Source |
| --- | --- | --- |
| Real memory ancestry is the landing proof. | `require_integrated_memory_ancestry` | mcp/src/agents_remember/worktrees/integration/integration_ref_transaction.py:235-250 |

## Ungoverned Mirror Status (known defect)

This route overview lives in the `onboarding/skills/**` tree, which mirrors the code repository's
`skills/**` route. `skills/**` is absent from `settings.json`'s `pathRules.include`, so this whole
onboarding tree sits outside normal onboarding census coverage: it is legacy and ungoverned. It is
retained here only because the contract-scoped memory-quality checker still validates these documents
whenever `skills/**` is part of a leaf's changed set, which is exactly why this overview was updated
by hand rather than by a governed maintenance pass. The remaining sibling sidecars under
`onboarding/skills/**` — the other role, criteria, and template cards — are knowingly stale and are
deliberately left untouched pending a follow-up decision on whether this mirror should be governed or
removed. That mismatch between the declared path rules and the enforced checking scope is itself the
recorded defect.

## Update History

- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): re-pointed `An ordinary master/series integration has no leaf closeout door of its own` in the row 100 of this card from skills/c-09-git-worktree-manager/SKILL.md:380-380 to skills/c-09-git-worktree-manager/SKILL.md:381, the extent of the construct the claim is about (the checker named line(s) [381] as its live location); re-pointed `directExecutionEnabled` in the row 100 of this card from skills/c-09-git-worktree-manager/SKILL.md:381 to skills/c-09-git-worktree-manager/SKILL.md:384, the extent of the construct the claim is about (the checker named line(s) [384] as its live location)
- 2026-09-15T00:56:17+00:00 — LCA ledger-retirement working-candidate curation: Reconciled canonical worktree doctrine to cache-independent Git authority. Existing verified commit/date remain historical provenance until producer-owned closeout. Source inspection only; no aggregate acceptance claim.


- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (drift re-verification): the
  `skills/c-09-git-worktree-manager/` route changed since the recorded verification commit. Re-read
  the card against the frozen on-disk source and re-checked its claims and cited ranges: nothing
  this card asserts is falsified by the change, so no wording changed. Verification metadata remains
  closeout-owned; no verification stamp advanced.
- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (citation pass): re-derived the source ranges of 2
  claim(s) whose anchor no longer sat in its cited range and normalised 2 further range(s) in this
  card from their anchors against the frozen source snapshot (`agents-remember memory-citations
  --fix --document`, snapshot 188b8ecd). No claim wording changed; every rewritten range was read
  back at its current position. Verification metadata remains closeout-owned.
- 2026-09-14T13:20+02:00 — Corrected the route's external-memory doctrine: the sync transaction proves
  the admitted Git history and requires no row list of the `memory.md` it commits, because the ledger
  is derived state and its rebuild reports the exclusions it cannot resolve. The source skill text at
  `SKILL.md:293-299` was corrected with the code, so the skill no longer carries the removed
parent-row validation; the matching route invariant now
  states the current behaviour. Verification metadata remains closeout-owned.
- 2026-09-13T15:01:46+02:00 — Gate-required ungoverned-mirror curation: rebound the route's citation
  rows against the frozen source after `grep -n` verification — `## Mid-Task Sync` to
  SKILL.md:256-300, `## Lifecycle Finalization And Cleanup` to SKILL.md:430-508, and the ordinary
  master/series integration anchors `"An ordinary master/series integration has no leaf closeout door
  of its own"` and `directExecutionEnabled` from :376-376/:379-379 to :377-377/:380-380 (their only
  real change is the line shift); tightened `SyncOperationStore` to sync_transaction_state.py:172-305.
  Rewrote the hot-path admission summary to per-contract activation (each contract owns its own
  activation record, `reconciling` suspends nothing, one selection excludes no other, multiple
  nonterminal contracts remain valid) and added the explicit developer ruling that nothing serializes
  a graph-less sprint — `atomic-sequential` describes sprint shape, not a serialization mechanism.
  Added the Ungoverned Mirror Status defect statement. Verification metadata remains closeout-owned.
- 2026-09-11T23:05:00+00:00: Curator citation reconciliation: "An ordinary master/series integration has no leaf closeout door of its own", `directExecutionEnabled` repointed to skills/c-09-git-worktree-manager/SKILL.md:376-376, skills/c-09-git-worktree-manager/SKILL.md:379-379. No content impact: mechanical anchor-range projection against citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `sync_result` repointed to mcp/src/agents_remember/worktrees/modules/sync.py:28-67. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-10T15:06+02:00 — No content impact: mechanical citation re-derivation after the closeout auto-carry change shifted lines in `sync_transaction.py` / `sync_transaction_state.py`; the cited symbols and their meanings are unchanged.
- 2026-09-10T07:30+02:00 — CCR-R12@v5 transaction-only curation: updated the current onboarding boundary; verification metadata remains preserved for the coordinated final stamp.
- 2026-09-09T12:22:46+00:00: Generated citation repair: `directExecutionEnabled`; "An ordinary master/series integration has no leaf closeout door of its own" repointed to skills/c-09-git-worktree-manager/SKILL.md:357-357; skills/c-09-git-worktree-manager/SKILL.md:354-354. No content impact: mechanical anchor-range projection bound to citation source snapshot 06f99a0e57ce8b514dd7ed6685874da5285e3ec2e8c4a3f6a5d768b622094451; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-08-31T20:30+02:00 — 260831-DER: documented ordinary series `not-applicable` door authority,
  the narrow leaf-without-enclosure direct-landing policy, and retained exact leaf/journal recovery.
  Also repaired a pre-existing sentence-order defect in the sync summary.

- 2026-08-26T14:32+02:00 — Corrected the route contract from per-code uniqueness to exact
  parent-row preservation with valid newest-first same-code history. Verification remains
  closeout-owned.

- 2026-08-26T08:50+02:00 — Corrected the frozen journal-store owner name to
  `SyncOperationStore`.
- 2026-08-26T08:20+02:00 — Final frozen reconciliation of the canonical worktree-manager route;
  verification metadata awaits the real code commit.

- 2026-08-26T05:20+02:00 — Established canonical route onboarding for source-pair activation,
  retained-conflict synchronization, exact cleanup release, and no-fallback ownership.
