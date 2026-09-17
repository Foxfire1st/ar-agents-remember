# mcp/src/agents_remember/worktrees/sync_transaction_results.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/sync_transaction_results.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T01:15+00:00 |
| lastVerifiedCommitHash | `420669c459aab3650cdaa5b3e5271e71d7d94c0e` |
| lastVerifiedCommitDate | 2026-09-17T10:54:08+02:00|
| verificationStatus | working-candidate |
| governingOverview | `overview.md` |

The body describes the uncommitted LCA L9 working candidate. The commit fields identify the latest real commit touching this source file; they do not claim that the candidate is committed or accepted.

## Governing Overview

[Nearest governing route overview](overview.md)

## Purpose

Centralize typed public results for resumable sync, preserving phase, preview, resolution-owner, and terminal replay semantics.

## Code Commentary

### Logic

Result builders cover the memory policy choice, initial preview, retained merge/WIP conflict, staged-resolution and parked-WIP previews, active/cancel previews, completed/cancelled replay, and no-authority quarantine replay. Retained conflicts name the agent, the side, the exact worktree/files, and contract-addressed continue/cancel calls.

Resolution previews now read `content_conflicts(side)`: memory-side root memory.md is excluded while code-side files and genuine memory content remain visible. `resolution_validation_preview` delegates the exact staged-content/MERGE_HEAD proof. `parked_wip_validation_preview` reports whether the real reapply conflicts are settled; it does not mutate an index, drop a stash, or create a commit.

### Conventions

All builders return WorktreeCommandResult and reuse shared side/recovery payload owners. A wipRestore marker distinguishes a parked-candidate reapply from the source merge itself.

### Invariants And Boundaries

- A preview reports readiness without performing the continuation.
- Memory cache-only index state cannot become a manual resolution requirement.
- Real conflict guidance keeps both continue and cancel addresses.
- A completed generation cannot be retroactively cancelled.
- Quarantine replay does not claim branch restoration without authority refs.

### Todos

No new file-local follow-up is identified by this source reconciliation.

## Docs References

No domain-documentation source is configured for this slice. The behavior described here is established by current repository source and the authorized LCA L9 change, rather than an invented external reference.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

These current source spans identify the implementation owners and the specific assertions supporting the file's behavior. A test definition is evidence of its assertions, not an execution or certification receipt.

| Finding | Anchor | Source |
| --- | --- | --- |
| Conflict ownership and parked-WIP versus merge result shapes. | `resolution_required` | mcp/src/agents_remember/worktrees/sync_transaction_results.py:69-111 |
| Policy choice and non-mutating initial/active/cancel previews. | `memory_choice_required` | mcp/src/agents_remember/worktrees/sync_transaction_results.py:26-48 |
| Terminal and no-authority replay results remain distinct. | `terminal_resolution_replay` | mcp/src/agents_remember/worktrees/sync_transaction_results.py:208-243 |
| Content-domain conflict and staged-resolution proof is delegated to the Git owner. | `content_conflicts` | mcp/src/agents_remember/worktrees/sync_transaction_git.py:285-292 |

## Cross-Repo References

The operation and fixture boundaries described here are defined by same-repository contracts and Git helpers. No separate cross-repository document is used as evidence for this card.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History

- 2026-09-15T01:15+00:00 — 260913-LCA-L9 working candidate: Changed resolution and parked-WIP previews to side-aware content conflict reads; retained read-only semantics, exact continuation guidance, and terminal replay restrictions. Current source and citation targets were checked; the metadata records the last real file commit, and candidate changes remain uncommitted.

- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (drift re-verification): the parked-candidate
  result surface is the frozen change and the card documents it. Re-checked all nine cited ranges:
  they hold. No wording changed. Verification metadata remains closeout-owned.
- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (drift re-verification):
  `mcp/src/agents_remember/worktrees/sync_transaction_results.py` changed since the recorded
  verification commit. Re-read the card against the frozen on-disk source and re-checked its claims
  and cited ranges: nothing this card asserts is falsified by the change, so no wording changed.
  Verification metadata remains closeout-owned; no verification stamp advanced.
- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (citation pass): re-derived the source ranges of 2
  claim(s) whose anchor no longer sat in its cited range and normalised 1 further range(s) in this
  card from their anchors against the frozen source snapshot (`agents-remember memory-citations
  --fix --document`, snapshot 188b8ecd). No claim wording changed; every rewritten range was read
  back at its current position. Verification metadata remains closeout-owned.
- 2026-09-10T15:06+02:00 — Parked-candidate result surface: recorded the `wipRestore` marker and parked-specific summary on `resolution_required`, and the read-only `parked_wip_validation_preview`. Re-derived the builder anchors against the current working tree. Verification remains closeout-owned.

- 2026-08-26T08:20+02:00 — Final frozen reconciliation of preview, retained-resolution,
  cancellation, quarantine, and terminal replay result vocabulary.

- 2026-08-26T02:55+02:00 — Drafted sync-result ownership; final vocabulary, citations, and
  verification remain open.
