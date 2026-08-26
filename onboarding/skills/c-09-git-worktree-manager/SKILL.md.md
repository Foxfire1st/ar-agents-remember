# skills/c-09-git-worktree-manager/SKILL.md

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `skills/c-09-git-worktree-manager/SKILL.md` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-26T14:32+02:00 |
| lastVerifiedCommitHash |  `7833df0b219bba560f67f6e1158c3f4f155e1ce6`|
| lastVerifiedCommitDate |  2026-08-26T15:02:28+02:00|
| governingOverview | `skills/c-09-git-worktree-manager/overview.md` |

## Governing Overview

[c-09 worktree lifecycle overview](overview.md)

## Purpose

Canonical agent doctrine for the Agents Remember worktree lifecycle. It defines the public,
contract-addressed route from intent/start through source reconciliation, closeout handoff,
integration, terminal cleanup, and reopen recovery while keeping private selector, journal, ref,
and queue mechanics behind their APIs.

## Code Commentary

### Logic

Atomic-series implementation admission is separate from task planning. For one normalized
code/external-memory source pair, manager/worker dispatch and atomic start/attach select a master;
reviewer/curator inspection does not. A selecting operation records `reconciling`, automatically
pauses the former selection without suspending or deleting its durable work, reconciles the exact
recorded source bases, and records `active` only when both are current. A source move during sync
leaves the selection reconciling. Explicit cancellation publishes durable `vacant`.

The task-document plane remains upstream and never reads selector or queue state. Queue rows are a
disposable projection of current waiting facts and own no claim, commit, certification,
integration, or activation transition. Malformed selector bytes invalidate only affected runtime
projection/admission; the next exact selecting operation archives the bytes and replaces the
record. Contract-presence fallback and tolerant readers are prohibited.

`worktree_sync` reconciles the exact source pair as a journaled transaction. It pins recorded bases,
pre-sync branch heads, and admitted source tips before merge mutation. A code or memory conflict is
retained in its exact `.sync` worktree and returned as resolution-required. The agent resolves and
stages derivable conflicts, then calls `resolution_action=continue`; the journal supports resuming
across tool calls and process restarts. `resolution_action=cancel` restores pinned heads, removes
temporary worktrees, terminalizes the journal, and releases an exact reconciling selection.
Memory resolution preserves every exact parent ledger row. Repeated code commits remain valid
newest-first memory history; neither the skill nor the sync transaction collapses them into a
globally unique code key.

Cleanup releases an exact selected terminal contract before removing the authority needed to name
it and never clears a newer selection. Integration conflicts use the same evidence boundary:
agents resolve technically derivable conflicts; only genuine semantic ambiguity escalates to the
architect.

### Conventions

- Preview before mutation and keep dry-run side-effect free.
- Use the canonical enclosure contract as the public recovery address.
- Sync early, before memory work, while preserving exact code/memory ledger admission.
- Never imitate continue/cancel with ambient Git commands.

### Invariants And Boundaries

- Multiple live series may coexist; exactly one is selected per source pair.
- Selection pauses, rather than terminalizes, the former master.
- The enclosure-root journal survives a missing or unreadable task contract.
- The queue never owns operation lifecycle or commit evidence.
- No compatibility reader or contract-presence election exists.
- Ledger order selects current memory authority, while retained exact rows preserve audit history.
  Merge validation requires parent-row preservation, not one row per code commit.

### Todos

None. Exact source claims and vocabulary are reconciled to the canonical skill.

## Docs References

No Domain Documentation source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Canonical source-pair admission and task/queue separation. | "Atomic-series implementation admission is a separate, source-pair-scoped authority." | skills/c-09-git-worktree-manager/SKILL.md:236-236 |
| Resumable retained-conflict transaction and explicit cancellation doctrine. | `## Mid-Task Sync` | skills/c-09-git-worktree-manager/SKILL.md:254-290 |
| Exact cleanup/finalization boundary. | `## Lifecycle Finalization And Cleanup` | skills/c-09-git-worktree-manager/SKILL.md:377-456 |
| Public implementation facade preserves the same contract-addressed API. | `sync_result` | mcp/src/agents_remember/worktrees/modules/sync.py:29-68 |

## Cross-Repo References

No meaningful cross-repository reference applies to this repository-owned lifecycle doctrine.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History
- 2026-08-26T14:32+02:00 — Corrected sync doctrine to preserve every exact parent ledger row while
  accepting repeated code commits as newest-first memory history. Verification remains
  closeout-owned.

- 2026-08-26T10:44:52+02:00 — Completed governed provenance review for the canonical c-09 selector, resumable sync, cancellation, and terminal-release doctrine.

- 2026-08-26T08:45+02:00 — Restored canonical Docs/Cross-Repo reference sections for the changed
  c-09 doctrine card.

- 2026-08-26T08:20+02:00 — Reconciled canonical c-09 selection, resumable-sync, cancellation,
  terminal-release, and no-fallback doctrine to the frozen source.

- 2026-08-26T05:20+02:00 — Created strict canonical onboarding for the source-pair selector,
  reconciliation-before-exposure, retained conflicts, continue/cancel, stable journal, exact
  terminal release, and no-fallback boundary. Final citations remain post-Dagger-owned.