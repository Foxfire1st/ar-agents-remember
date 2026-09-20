# mcp/src/agents_remember/worktrees/sync_transaction.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/sync_transaction.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-20T06:02+02:00 |
| reviewedWorkingCandidate | candidate `ar/260915-ks-l40-ar`, uncommitted; base `f79f4db745ad00b908d6ce4871d0b4ab2320207c` |
| lastVerifiedCommitHash | `74c6c693b8c5a5863ce15f016793192931f4adc1` |
| lastVerifiedCommitDate | 2026-09-20T06:22:08+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Nearest governing overview](overview.md)

Working candidate verification: source inspected at 2026-09-20T06:02+02:00 against the uncommitted
CYCLE-02-remainder candidate on `ar/260915-ks-l40-ar`. The commit fields name the candidate's base; they do
not identify a future commit for the working changes.

## Purpose

Drives resumable, contract-addressed mid-task source synchronization. One durable generation can
be observed, continued after resolving retained content conflicts, cancelled, or recovered without
reconstructing lifecycle evidence from task prose.

## Code Commentary

### Logic

`sync_contract_under_authority` validates input choices and reads the enclosure-root journal. It
routes damaged/missing journal recovery, quarantine, identity validation, active resumption,
terminal replay, or new admission. The operation returns typed results; no lock remains held while
an agent resolves conflicts between calls.

Admission resolves actual code/memory source tips and builds typed `SyncSideRecord` plans for
already-current, fast-forward, merge, or skip behavior. It no longer performs a ledger mapping
preflight. `_already_current_result` uses the recorded bases and participating branch ancestry,
independently of cached rows. A divergent memory plan still requires its explicit merge/skip choice,
and that admitted choice cannot change during continuation.

Before a moving non-temporary side is parked, preflight proves its checkout and rejects real
content conflicts or an active `MERGE_HEAD` outside the sync admission. A merely dirty candidate is
parked rather than refused. `_park_participating_wip` passes the complete side record to dirty-path
and stash helpers, so the memory side excludes only its root `memory.md` cache. It records the stash,
up to 128 sampled paths, and the exact total path count. Failed partial parking attempts restore
already parked work where possible and report any stranded stash identities.

The admitted record pins source/base/pre-sync authority before automatic code-then-memory progress.
Native merge behavior and exact parent/source proofs belong to `sync_transaction_git`. Genuine
content conflicts remain in the retained worktree. The driver reads `content_conflicts(side)` when
refreshing both merge-resolution and parked-WIP-resolution failures, so a memory-cache conflict is
not presented as content requiring agent judgment.

Completed paths, resume, and cancellation restore parked work through the focused authority/recovery
owners. `_reconcile_completed_sides` can recognize an already committed operation-owned merge;
finalization waits for the participating sides and parked work to be settled. Exact checkout,
source, parent/ref, journal, and admitted-choice checks remain in force.

**The retained-conflict continuation was one route with two endings, and it is now the route an authored
decision takes as well.** `_retained_side` reads the side the retained phase names, so the phase really is
the whole address and the three call sites can no longer disagree about which side is meant.
`_finish_retained_merge` is the single continuation both a hand-staged resolution and an authored
reconciliation end in: it commits the retained merge, clears `conflictFiles` **and the journaled
`knowledgeConflict`** together (the agent was told what to reconcile, and the state that carried it goes with
the conflict), restores parked work, and rejoins the ordinary automatic run. So a reconciled sync is a normal
sync with one authored input rather than a second route through the transaction.

**An authored decision is checked against the journal *before* the merge is entered.**
`_reconcile_knowledge_resolution` reads the conflict from the journal, hands it to `_reconcile_problem` (via
`_reconcile_refusal`), and only then calls `reconcile_side_merge`. `_reconcile_problem` names both facts a
caller can get wrong: `_decision_matches` requires the decision to name the exact table and rendered
`record_id` the engine refused (or to be the row-less decision for a conflict with no row), and the decision
must be one `decisions` says that conflict admits. A wrong record, a decision the conflict does not admit,
or a reconcile against the code side (which merges text and carries no knowledge dataset) is refused with
`sync-input-invalid` and `invalidField="knowledge_resolution"` **without entering the merge** — carrying a
decision into a merge that would ignore it and hand back the same conflict is exactly the loop this replaced.
A decision that settles one conflict may reveal the next; that one is journaled through `_knowledge_conflict`
and reported exactly as the first was. `sync_input_refusal` pairs the two inputs both ways:
`resolution_action='reconcile'` without `knowledge_resolution`, and `knowledge_resolution` with any other
action, are refused by name. `_reconcile_preview` routes a dry run to the read-only preview and refuses with
`sync-resolution-not-active` when no knowledge conflict is retained.

### Conventions

The driver owns phase routing and delegates Git mechanics, journal storage, pinned authority,
result formatting, and terminal recovery. Top-level I/O/proof/value failures return
`sync-operation-refused` with the failure family and retained detail. The cache is an ignored
consumer artifact on the memory side, not a second source of sync truth.

### Invariants And Boundaries

- Canonical contract and pinned Git facts identify one retained transaction generation.
- Cached mappings, byte shape, or absence do not authorize or block source synchronization.
- Only memory-side root memory.md is excluded; a code file with that name remains real content.
- New moving-side admission cannot adopt an unrelated active merge.
- Real content conflicts stay resumable, and exact merge/ref proofs cannot be replaced by a cache match.
- Parked work must be restored or explicitly reported before terminal completion.
- **`resolution_action='reconcile'` is admitted only with a knowledge resolution, and the two are refused
  as a pair.** `knowledge_resolution` is read only with `reconcile`, which is what keeps a decided input
  from travelling with an action that would ignore it.
- **A decision never enters the merge unchecked.** It is validated against the *journaled* diagnosis first,
  so a wrong record or an inexpressible decision is refused before the retention is disturbed rather than
  after a merge that would have ignored it.
- **The journaled diagnosis is cleared with the conflict it explains.** A settled retained merge carries
  neither `conflictFiles` nor `knowledgeConflict`, so a completed sync cannot re-advertise a reconcile call
  for a conflict that no longer exists.

### Todos

No new implementation or live-state operation is authorized by this documentation pass.

## Docs References

No Domain Documentation source is configured for this repository. No external domain documents
were available through the configured registry to consult; the current claims are grounded in the
working source and package-local evidence below. The registry is discovery input, not a citation.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external domain-documentation evidence. | — | — |

## Repo-Internal References

These repository-relative targets and exact ranges were checked against the L9 working source.
Source declarations and test assertions are distinguished from execution and acceptance evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| The driver validates choices and routes retained or new transactions, including the reconcile/decision pairing. | `sync_contract_under_authority`; `sync_input_refusal` | mcp/src/agents_remember/worktrees/sync_transaction.py:86-116; mcp/src/agents_remember/worktrees/sync_transaction.py:181-222 |
| Dirty work admission and parking use complete typed side records. | `_preflight_participating_sides`; `_side_live_complete` | mcp/src/agents_remember/worktrees/sync_transaction.py:408-425; mcp/src/agents_remember/worktrees/sync_transaction.py:849-857 |
| Currentness and continuation use Git facts and content-only conflicts. | `_already_current_result`; `_continue_resolution` | mcp/src/agents_remember/worktrees/sync_transaction.py:354-382; mcp/src/agents_remember/worktrees/sync_transaction.py:581-602 |
| **The side the retained phase names is read in one place, so phase and side cannot disagree.** | `_retained_side` | mcp/src/agents_remember/worktrees/sync_transaction.py:603-610 |
| **The one continuation both a hand-staged resolution and an authored reconciliation end in, which clears the journaled diagnosis with the conflict.** | `_finish_retained_merge` | mcp/src/agents_remember/worktrees/sync_transaction.py:611-648 |
| **The authored-decision route: validate against the journal, re-run the adapter with the decision, then finish the retained merge.** | `_reconcile_knowledge_resolution` | mcp/src/agents_remember/worktrees/sync_transaction.py:649-688 |
| **The two facts a caller can get wrong, and the refusal that names them without entering the merge.** | `_reconcile_problem`; `_decision_matches`; `_refused_record` | mcp/src/agents_remember/worktrees/sync_transaction.py:704-741; mcp/src/agents_remember/worktrees/sync_transaction.py:759-769; mcp/src/agents_remember/worktrees/sync_transaction.py:750-758 |
| **The adapter's explanation projected into the journal and the public response, with the decisions that conflict admits.** | `_knowledge_conflict` | mcp/src/agents_remember/worktrees/sync_transaction.py:770-789 |
| **The read-only dry run of an authored decision.** | `_reconcile_preview` | mcp/src/agents_remember/worktrees/sync_transaction.py:486-501 |
| The delegated Git owner excludes only the memory cache while retaining exact native merge proofs, and now returns the adapter's refusal with the merge outcome. | `worktree_dirty_paths`; `_content_pathspec`; `discard_memory_cache_changes`; `exact_created_head`; `SideMergeOutcome` | mcp/src/agents_remember/worktrees/sync_transaction_git.py:141-167; mcp/src/agents_remember/worktrees/sync_transaction_git.py:305-318; mcp/src/agents_remember/worktrees/sync_transaction_git.py:319-340; mcp/src/agents_remember/worktrees/sync_transaction_git.py:571-581; mcp/src/agents_remember/worktrees/sync_transaction_git.py:35-48 |
| Pinned authority and parked-work restoration remain separate owners. | `pin_authority`; `require_pinned_authority` | mcp/src/agents_remember/worktrees/sync_transaction_authority.py:121-126; mcp/src/agents_remember/worktrees/sync_transaction_authority.py:129-143 |
| Terminal finalization/cancellation and damaged-journal recovery are delegated. | `finalize_sync`; `cancel_sync`; `recover_unreadable_journal`; `recover_missing_journal` | mcp/src/agents_remember/worktrees/sync_transaction_recovery.py:56-92; mcp/src/agents_remember/worktrees/sync_transaction_recovery.py:159-283 |
| **The integration case that drives the authored decision through this driver and asserts the advertised call is the one that settles it.** | `_assert_knowledge_conflict_is_diagnosed_and_reconciled` | mcp/tests/test_worktree_sync.py:250-338 |

## Cross-Repo References

The code/memory or fixture-repository boundaries above are established by package-local source.
No additional configured external or sibling-repository evidence is claimed.

| Finding | Anchor | Source |
| --- | --- | --- |
| No additional configured cross-repository evidence. | — | — |

## Update History
- 2026-09-20T06:02+02:00 — 260915-KS-L40 curator (uncommitted CYCLE-02-remainder change set on `ar/260915-ks-l40-ar`, code base `f79f4db7`): **the retained-conflict continuation gained its second ending, and this card now records the authored route end to end.** Added: `_retained_side` (the phase is the whole address), `_finish_retained_merge` (the one continuation a hand-staged resolution and an authored reconciliation share, which clears `conflictFiles` *and* the journaled `knowledgeConflict` together), `_reconcile_knowledge_resolution` (validate against the journal, then re-run the adapter with the decision), `_reconcile_problem` / `_decision_matches` / `_refused_record` (the two facts a caller can get wrong, refused *before* the merge is entered), `_knowledge_conflict` (the projection into journal and response), `_reconcile_preview`, and the two-way pairing in `sync_input_refusal`. Three invariants are added for exactly the properties the acceptance depends on: a decision never enters the merge unchecked, the two inputs are refused as a pair, and the journaled diagnosis is cleared with the conflict it explains. Verification metadata is **advanced to the candidate's base `f79f4db7`** with the working candidate named beside it; the committed stamp remains closeout's.

2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.

- 2026-09-15T01:05 UTC — Reconciled the stable sync driver after ledger admission removal and native cache-conflict repair: typed side records now drive WIP exclusion, content_conflicts filters memory-side cache entries, and moving-side admission still refuses an unrelated active merge. Preserved pinned authority, real content conflict, restore, and exact merge recovery boundaries. Working candidate verified by source inspection; commit metadata records real committed history only.


- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (drift re-verification): the already-current
  branch no longer validates the parent memory side, as the earlier entry records. Re-checked all
  fourteen cited ranges against the frozen source: they hold. No wording changed. Verification
  metadata remains closeout-owned.
- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (drift re-verification):
  `mcp/src/agents_remember/worktrees/sync_transaction.py` changed since the recorded verification
  commit. Re-read the card against the frozen on-disk source and re-checked its claims and cited
  ranges: nothing this card asserts is falsified by the change, so no wording changed. Verification
  metadata remains closeout-owned; no verification stamp advanced.
- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (drift re-verification): the source moved since
  the recorded verification commit (the already-current branch no longer validates the parent memory
  side). Re-read the card: it already records that removal and all fourteen cited ranges still hold.
  No wording changed; verification metadata remains closeout-owned.
- 2026-09-14T13:20+02:00 — The ledger ruling reaches the driver: `_already_current_result` reports an
  already-descendant pair as `already-current` on its recorded bases and branch ancestry alone, and
  the `validate_current_memory_side` call that used to refuse it with `sync-work-branch-invalid` is
  gone. Recorded that boundary in Logic and as a local invariant, and re-derived every reference
  anchor (the Git, recovery, park-boundary, and driver ranges all moved). Verification remains
  closeout-owned.

- 2026-09-11T23:05:00+00:00: Curator citation reconciliation: `SyncOperationRecord`, `SyncOperationStore`, `SyncSideRecord`, `observe_sync_operation` repointed to mcp/src/agents_remember/worktrees/sync_transaction_state.py:172-366, mcp/src/agents_remember/worktrees/sync_transaction_state.py:369-385, mcp/src/agents_remember/worktrees/sync_transaction_state.py:41-67, mcp/src/agents_remember/worktrees/sync_transaction_state.py:70-87. No content impact: mechanical anchor-range projection against citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged.

- 2026-09-10T15:06+02:00 — Parked-candidate curation: recorded the new pre-journal admission (`_admit_participating_sides`, `_park_participating_wip`, `_side_parks_wip`, `_wip_stash_message`, `_restore_already_parked`), the narrowed parkability preflight (`_require_parkable_worktree`), the completed/resume/agent-resolved restore paths, and the bounded `WIP_PATH_SAMPLE_LIMIT`. A dirty moving side is now parked rather than refused; unmerged index entries and unprovable checkouts still refuse. Re-derived every cited range against the current working tree. Verification remains closeout-owned.

- 2026-08-26T08:20+02:00 — Final frozen reconciliation of the resumable state machine and its
  detail-preserving controlled refusal boundary.

- 2026-08-26T06:20+02:00 — Recorded that the public refusal boundary preserves the lower-level
  proof failure's exact detail while keeping the result controlled. No test-execution claim is
  made.

- 2026-08-26T02:55+02:00 — Drafted resumable-sync driver onboarding against the pre-Dagger
  partition; final state vocabulary, citations, and verification remain open.