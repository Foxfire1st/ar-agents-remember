# mcp/src/agents_remember/worktrees/sync_transaction_results.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/sync_transaction_results.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-20T05:58+02:00 |
| reviewedWorkingCandidate | candidate `ar/260915-ks-l40-ar`, uncommitted; base `f79f4db745ad00b908d6ce4871d0b4ab2320207c` |
| lastVerifiedCommitHash | `74c6c693b8c5a5863ce15f016793192931f4adc1` |
| lastVerifiedCommitDate | 2026-09-20T06:22:08+02:00|
| verificationStatus | working-candidate |
| governingOverview | `overview.md` |

The body describes the uncommitted CYCLE-02-remainder working candidate. The commit fields identify the base the candidate sits on; they do not claim that the candidate is committed or accepted.

## Governing Overview

[Nearest governing route overview](overview.md)

## Purpose

Centralize typed public results for resumable sync, preserving phase, preview, resolution-owner, and terminal replay semantics.

## Code Commentary

### Logic

Result builders cover the memory policy choice, initial preview, retained merge/WIP conflict, staged-resolution and parked-WIP previews, active/cancel/reconcile previews, completed/cancelled replay, and no-authority quarantine replay. Retained conflicts name the agent, the side, the exact worktree/files, and contract-addressed continue/cancel calls.

**The retained-conflict builder now decides what to do next, and that is CYCLE-02's remainder in this module.** `_resolution_guidance` takes precedence in three shapes. When the journaled `knowledgeConflict` admits an authored decision (`decisions` non-empty), the response's `nextOperation` becomes `reconcile_knowledge_resolution` with `nextArgs` built by `_reconcile_args` from the **journaled** diagnosis — the exact `table` and `record_id` the engine refused, and the decision left as a `"<keep-left|keep-right>"` placeholder because choosing it is the agent's act and not this projection's. That replaced a loop: repeating the generic continuation against a retained knowledge conflict returned the same generic conflict forever. A parked candidate reapply keeps the shipped continuation, and a retained conflict that admits *no* decision (a schema disagreement) also keeps it, with a summary that says so via `_conflict_subject`. `resolution_required` publishes the diagnosis at `resolution.knowledge` as well, so the file name is no longer the whole answer.

`reconcile_preview` is the read-only dry run of that operation: it reports the conflict the journal holds, the decisions it admits, and that the decision would be applied and the merge validated afterwards — it does not predict the merge's answer, because whether the decision settles it is the merge's. `resolution_validation_preview` now carries the same `knowledge` projection, so a dry run answers "what is still unresolved" with the row rather than only the path.

Resolution previews read `content_conflicts(side)`: memory-side root memory.md is excluded while code-side files and genuine memory content remain visible. `resolution_validation_preview` delegates the exact staged-content/MERGE_HEAD proof. `parked_wip_validation_preview` reports whether the real reapply conflicts are settled; it does not mutate an index, drop a stash, or create a commit.

### Conventions

All builders return WorktreeCommandResult and reuse shared side/recovery payload owners. A wipRestore marker distinguishes a parked-candidate reapply from the source merge itself. The knowledge diagnosis is projected through one owner (`_conflict_subject`) so every builder names the refused row the same way, and the reconcile arguments are read from the journal rather than re-derived from the databases.

### Invariants And Boundaries

- A preview reports readiness without performing the continuation; `reconcile_preview` asserts no prediction about the outcome.
- Memory cache-only index state cannot become a manual resolution requirement.
- Real conflict guidance keeps both continue and cancel addresses; a reconcile-shaped conflict keeps `cancelArgs` too, so the authored path never removes the way out.
- A completed generation cannot be retroactively cancelled.
- Quarantine replay does not claim branch restoration without authority refs.
- **The advertised reconcile call is built from the journal, never from a fresh read.** A resumed sync therefore advertises the same call the first response did, and the decision placeholder stays a placeholder: this layer never chooses a side.

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
| Conflict ownership and parked-WIP versus merge result shapes, including the journaled knowledge diagnosis. | `resolution_required` | mcp/src/agents_remember/worktrees/sync_transaction_results.py:70-107 |
| **The next-move decision: reconcile when the conflict admits a decision, otherwise the shipped continuation.** | `_resolution_guidance` | mcp/src/agents_remember/worktrees/sync_transaction_results.py:110-156 |
| **The advertised reconcile call, built from the journal with the decision left to the agent.** | `_reconcile_args` | mcp/src/agents_remember/worktrees/sync_transaction_results.py:159-178 |
| **The one place the refused row is named in a sentence, shared by every builder.** | `_conflict_subject` | mcp/src/agents_remember/worktrees/sync_transaction_results.py:181-191 |
| **The read-only preview of authoring a decision, which predicts nothing about the merge.** | `reconcile_preview` | mcp/src/agents_remember/worktrees/sync_transaction_results.py:194-222 |
| Parked-candidate reapply preview. | `parked_wip_validation_preview` | mcp/src/agents_remember/worktrees/sync_transaction_results.py:225-252 |
| Staged-resolution preview, which now carries the knowledge projection on a dry run. | `resolution_validation_preview` | mcp/src/agents_remember/worktrees/sync_transaction_results.py:255-284 |
| Policy choice and non-mutating initial/active/cancel previews. | `memory_choice_required`; `sync_preview`; `active_preview`; `cancel_preview` | mcp/src/agents_remember/worktrees/sync_transaction_results.py:27-49; mcp/src/agents_remember/worktrees/sync_transaction_results.py:52-67; mcp/src/agents_remember/worktrees/sync_transaction_results.py:287-303; mcp/src/agents_remember/worktrees/sync_transaction_results.py:304-321 |
| Terminal and no-authority replay results remain distinct. | `terminal_resolution_replay` | mcp/src/agents_remember/worktrees/sync_transaction_results.py:324-359 |
| Content-domain conflict and staged-resolution proof is delegated to the Git owner. | `content_conflicts`; `validate_staged_resolution` | mcp/src/agents_remember/worktrees/sync_transaction_git.py:309-316; mcp/src/agents_remember/worktrees/sync_transaction_git.py:518-536 |
| **The journaled diagnosis these builders project, and the response fields that carry it.** | `SyncKnowledgeConflict`; `SyncResolutionProjection` | mcp/src/agents_remember/models/worktree.py:184-203; mcp/src/agents_remember/models/worktree.py:206-223 |

## Cross-Repo References

The operation and fixture boundaries described here are defined by same-repository contracts and Git helpers. No separate cross-repository document is used as evidence for this card.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History
- 2026-09-20T05:58+02:00 — 260915-KS-L40 curator (uncommitted CYCLE-02-remainder change set on `ar/260915-ks-l40-ar`, code base `f79f4db7`): **the retained-conflict builders stopped advertising a continuation that loops, and this card is rewritten around the next-move decision.** Recorded: `_resolution_guidance` and its three shapes (reconcile when the journaled conflict admits a decision, the shipped continuation for a parked candidate, the shipped continuation with an honest summary when no decision can settle it), `_reconcile_args` building the call from the **journaled** table/record with the decision left as a placeholder, `_conflict_subject` as the one place a refused row is named, `reconcile_preview` as the read-only dry run that predicts nothing about the merge, and `resolution_validation_preview` carrying the `knowledge` projection so a dry run names the row. The card's summary paragraph is corrected rather than extended because its old claim — that the retained conflict surface names only the side, worktree and files — is no longer true. Two invariants are added: the reconcile call is built from the journal and never from a fresh database read, and the authored path keeps `cancelArgs`. Verification metadata is **advanced to the candidate's base `f79f4db7`** with the working candidate recorded; closeout owns the committed stamp.

- 2026-09-20T00:16:01+00:00: Generated citation repair: `content_conflicts`; `validate_staged_resolution` repointed to mcp/src/agents_remember/worktrees/sync_transaction_git.py:286-293; mcp/src/agents_remember/worktrees/sync_transaction_git.py:456-474. No content impact: mechanical anchor-range projection bound to citation source snapshot b8fe5b3589f1357e836aaad1587e69ed38bbda0d58221eaa2150e96eb0561e93; claim bytes unchanged; generated by ccr-r10@v1.
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.

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
