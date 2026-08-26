# skills/c-09-git-worktree-manager

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `skills/c-09-git-worktree-manager` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-08-26T08:50+02:00 |
| lastVerifiedCommitHash |  `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d`|
| lastVerifiedCommitDate |  2026-08-26T08:10:26+02:00|

## Purpose

This route owns the agent-facing Git worktree lifecycle: start, attach, status, source-pair
selection, resumable synchronization, closeout routing, integration, finalization, cleanup,
abandonment, and reopen recovery. The skill describes public contract-addressed operations; it does
not move private journal, ref, or queue identity into agent prompts.

## Hot Path Summary

Atomic-series admission is scoped to an exact code/external-memory source pair. Manager/worker
dispatch plus atomic start/attach are selecting operations. Selection publishes `reconciling`,
logically pauses the former selection without destroying its task/worktree/journal, reconciles both
recorded source tips, and publishes `active` only when the exact pair is current. Multiple live but
paused series are valid. Task authoring never consults the selector, and the queue only projects its
waiting facts.

`worktree_sync` is one durable enclosure-root transaction. It pins pre-sync heads and source tips,
retains code or memory conflicts in operation-owned `.sync` worktrees, and advertises
`resolution_action=continue|cancel` on the same contract. Continue validates staged resolution and
resumes; cancel restores pinned heads, removes retained temporary worktrees, terminalizes the
journal, and releases an exact reconciling selection to durable `vacant`. No direct-Git recovery,
tolerant reader, or contract-presence fallback is part of the doctrine.

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

- One disposable selector record owns activation for one exact source pair.
- Contract presence, task order, and queue rows never elect a selected master.
- Conflicts are retained, resumable, and cancellable; they are not silently aborted.
- Cleanup releases only the exact selected terminal pointer and preserves newer selections.
- No fallback reader or duplicated lifecycle evidence is allowed.

### Todos

Exact source claims and citations are reconciled to the frozen canonical skill; verification
metadata awaits the real code commit.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The canonical skill owns source-pair admission, resumable sync, integration conflict ownership, and exact terminal release doctrine. | `## Mid-Task Sync`; `## Lifecycle Finalization And Cleanup` | skills/c-09-git-worktree-manager/SKILL.md:254-289; skills/c-09-git-worktree-manager/SKILL.md:376-455 |
| Public sync composes the selection and transaction owners without exposing private ids. | `sync_result` | mcp/src/agents_remember/worktrees/modules/sync.py:29-68 |
| Stable operation recovery is stored below the enclosure root. | `SyncOperationStore` | mcp/src/agents_remember/worktrees/sync_transaction_state.py:145-295 |

## Update History

- 2026-08-26T08:50+02:00 — Corrected the frozen journal-store owner name to
  `SyncOperationStore`.

- 2026-08-26T08:20+02:00 — Final frozen reconciliation of the canonical worktree-manager route;
  verification metadata awaits the real code commit.

- 2026-08-26T05:20+02:00 — Established canonical route onboarding for source-pair activation,
  retained-conflict synchronization, exact cleanup release, and no-fallback ownership.
