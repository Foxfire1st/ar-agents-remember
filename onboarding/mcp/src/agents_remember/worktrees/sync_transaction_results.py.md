# mcp/src/agents_remember/worktrees/sync_transaction_results.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/sync_transaction_results.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-20T07:30+02:00 |
| lastVerifiedCommitHash | `8b0254263c6998b1d4814b2e97c1bd231d39350f` |
| lastVerifiedCommitDate | 2026-09-29T15:00:35+02:00|
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

**The retained-conflict builder now decides what to do next, and that is CYCLE-02's remainder in this module.** `_resolution_guidance` takes precedence in three shapes. When the journaled `knowledgeConflict` admits an authored decision (`decisions` non-empty), the response's `nextOperation` becomes `reconcile_knowledge_resolution` with `nextArgs` built by `_reconcile_args` from the **journaled** diagnosis — the exact `table` and `record_id` the engine refused, and the decision left as a `"<keep-left|keep-right>"` placeholder because choosing it is the agent's act and not this projection's. That replaced a loop: repeating the generic continuation against a retained knowledge conflict returned the same generic conflict forever. A parked candidate reapply keeps the shipped continuation, and a retained conflict that admits *no* decision (a schema disagreement, or the referential orientation whose retraction the merge measured as unavailable) also keeps it, with a summary that says what the caller must do via `_unsettled_instruction`. `resolution_required` publishes the diagnosis at `resolution.knowledge` as well, so the file name is no longer the whole answer.

**The summary of a conflict no decision settles names which unsettled conflict it is, because the two need different work.** `_unsettled_instruction` splits that sentence on the one fact that decides the caller's next act. A referential refusal whose `precondition` is `no_arriving_insertion` is the orientation where the *arriving* side removed a row the retained side still cites: nothing the arriving delta inserted can account for the violation, so no arriving insertion can be retracted, and the caller restores the removed row or retracts the reference in the worktree dataset, stages it and continues — or cancels, which the same response still carries beside that call. Every other unsettled conflict keeps the shipped "resolve it in the worktree, stage it, then continue". This is the half of the CYCLE-02 residue that lives in this module: the first response used to promise that the merge continues while advertising a `keep-left` that provably could not apply, and driving exactly that advertised call returned the identical response forever. What is advertised now is the route that exists — `continue_sync_resolution` with `resolution_action=continue` — and the offer itself is read from the journaled diagnosis, so a conflict the merge measured as unretractable advertises no decision and no reconcile operation at all.

**A crossing sync's resolution names its report (MIK-R24 rule 8).** When the side record journals a
`crossingReport`, `resolution_required` adds `resolution.crossing`, the output of
`knowledge_crossing.crossing_summary`: the report path, the conflicted-item count, the first 100
`(path, item, reason)` entries with a truncation flag, the cards taken from each side, the moved marker
rows, the record-conflict history owner, and `howToResolve`. It also appends one sentence to the summary.
That sentence says this is a crossing sync, names the report, and says that every conflicted JSON item holds
a `crossing-conflict` marker the knowledge validator refuses until it is resolved. For an ordinary sync
`crossingReport` is empty and nothing is added, so the payload is unchanged.

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
- **The advertised continuation is one that exists.** Where the journaled diagnosis admits no decision — a schema disagreement, or the referential orientation whose retraction the merge measured as unavailable — the response advertises `continue_sync_resolution` with the manual `resolution_action`, carries `cancelArgs` beside it, and says in its summary which conflict it holds and what the caller must do (`_unsettled_instruction`). It never advertises a reconcile call for a conflict that cannot be reconciled, which is the byte-identical loop this module's guidance exists to replace.

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
| Conflict ownership and parked-WIP versus merge result shapes, including the journaled knowledge diagnosis. | `resolution_required` | mcp/src/agents_remember/worktrees/sync_transaction_results.py:71-117 |
| A crossing sync's resolution carries the crossing summary and names the report; an ordinary sync's payload is unchanged. | `resolution_required`; "if side.crossingReport"; `crossing_summary` | mcp/src/agents_remember/worktrees/sync_transaction_results.py:71-117; mcp/src/agents_remember/worktrees/knowledge_crossing.py:265-285 |
| **The next-move decision: reconcile when the conflict admits a decision, otherwise the continuation that exists — with a summary saying which unsettled conflict this is.** | `_resolution_guidance` | mcp/src/agents_remember/worktrees/sync_transaction_results.py:120-166 |
| **The sentence telling the caller what to do about a conflict no decision settles, split by the merge's measured retraction precondition.** | `_unsettled_instruction` | mcp/src/agents_remember/worktrees/sync_transaction_results.py:169-187 |
| **The advertised reconcile call, built from the journal with the decision left to the agent.** | `_reconcile_args` | mcp/src/agents_remember/worktrees/sync_transaction_results.py:190-209 |
| **The one place the refused row is named in a sentence, shared by every builder.** | `_conflict_subject` | mcp/src/agents_remember/worktrees/sync_transaction_results.py:212-222 |
| **The read-only preview of authoring a decision, which predicts nothing about the merge.** | `reconcile_preview` | mcp/src/agents_remember/worktrees/sync_transaction_results.py:225-253 |
| Parked-candidate reapply preview. | `parked_wip_validation_preview` | mcp/src/agents_remember/worktrees/sync_transaction_results.py:256-283 |
| Staged-resolution preview, which now carries the knowledge projection on a dry run. | `resolution_validation_preview` | mcp/src/agents_remember/worktrees/sync_transaction_results.py:286-315 |
| Policy choice and non-mutating initial/active/cancel previews. | `memory_choice_required`; `sync_preview`; `active_preview`; `cancel_preview` | mcp/src/agents_remember/worktrees/sync_transaction_results.py:28-50; mcp/src/agents_remember/worktrees/sync_transaction_results.py:53-68; mcp/src/agents_remember/worktrees/sync_transaction_results.py:318-332; mcp/src/agents_remember/worktrees/sync_transaction_results.py:335-352 |
| Terminal and no-authority replay results remain distinct. | `terminal_resolution_replay` | mcp/src/agents_remember/worktrees/sync_transaction_results.py:355-390 |
| Content-domain conflict and staged-resolution proof is delegated to the Git owner. | `content_conflicts`; `validate_staged_resolution` | mcp/src/agents_remember/worktrees/sync_transaction_git.py:322-329; mcp/src/agents_remember/worktrees/sync_transaction_git.py:597-615 |
| **The journaled diagnosis these builders project, and the response fields that carry it.** | `SyncKnowledgeConflict`; `SyncResolutionProjection` | mcp/src/agents_remember/models/worktree.py:184-203; mcp/src/agents_remember/models/worktree.py:206-222 |

## Cross-Repo References

The operation and fixture boundaries described here are defined by same-repository contracts and Git helpers. No separate cross-repository document is used as evidence for this card.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History
- 2026-09-29T14:21:42+02:00 — 260928-MIK-L24 curator (uncommitted change set on `ar/260928-mik-l24`, code base `cd3e943d740b490d391722389af0a6bca0ccf93e` plus the working-tree delta and untracked files): Added a Logic paragraph and a row for MIK-R24 rule 8: `resolution_required` adds `resolution.crossing` (the crossing summary) and one summary sentence when the side journals a `crossingReport`. The ordinary payload is unchanged. The remaining ranges were re-pointed by the installed fixer and the exact line map, with no wording change.
- 2026-09-22T19:40:00+02:00 — 260921-ICR-L8 curator (candidate `ar/260921-icr-l8`, uncommitted; production line at this leaf's base `02957762709c9b515b4ff57f7f13524a7c0dfb8d`): **metadata-row removal.** The candidate-reading metadata rows this card carried were removed under the developer's 2026-09-22 rule: the field is not a real metadata field, has no purpose, and must not be written or carried anywhere. The reading those rows recorded is preserved in this entry's own words — the claims on this card were taken against the leaf candidate named above where they describe uncommitted work, and against the last real commit the card's stamp names where they describe shipped code. No claim, anchor, wording or citation range changed, no table shape changed, and no verification stamp was advanced.
- 2026-09-20T07:30+02:00 — 260915-KS-L42 curator (uncommitted CYCLE-02 repair change set on `ar/260915-ks-l42-ar`, code base `74c6c693`): **the summary of an unsettleable conflict stopped saying only that it is unsettled, and this card records what it now tells the caller.** `_unsettled_instruction` splits the sentence on the merge's measured retraction precondition: a referential refusal whose `precondition` is `no_arriving_insertion` is the orientation where the arriving side removed a row the retained side still cites, so the response says to restore the removed row or retract the reference in the worktree, stage it and continue, while every other unsettled conflict keeps the shipped sentence. That is the observable half of the repair this leaf makes — no decision and no reconcile operation are advertised where none can apply, the advertised call is the manual `continue_sync_resolution`, and driving it moves the state instead of repeating the response. The card's Logic section gains a paragraph, the invariants gain the rule that the advertised continuation is one that exists, and a reference row cites `_unsettled_instruction` at its own extent. Every citation range in this card that this leaf's insertion shifted (the five builders below `_conflict_subject`) was re-cited to its construct's own declaration extent in the working tree; no claim was weakened and no anchor dropped. **One item is left OPEN, not settled:** `cancelArgs`, which this response carries beside the advertised continuation, returns `sync-operation-refused` / `SyncGitProofError` in both orientations — including the INSERTED-row orientation round 2 verified as working — so the cancel half of the manual continuation is unproven in the sync fixture (most likely its missing canonical enclosure locator chain) and is named for the round-3 reviewer. Verification metadata is advanced to this leaf's own base `74c6c693` with the uncommitted working candidate beside it; closeout owns the committed stamp.
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
