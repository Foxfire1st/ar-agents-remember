# mcp/src/agents_remember/worktrees/sync_transaction.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/sync_transaction.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T01:05 |
| lastVerifiedCommitHash | `420669c459aab3650cdaa5b3e5271e71d7d94c0e` |
| lastVerifiedCommitDate | 2026-09-17T10:54:08+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Nearest governing overview](overview.md)

Working candidate verification: source inspected at 2026-09-15T01:05 UTC against the uncommitted L9 candidate.
The commit fields identify the latest real commit touching this source; they do not identify a future commit for the working changes.

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
| The driver validates choices and routes retained or new transactions. | `sync_contract_under_authority` | mcp/src/agents_remember/worktrees/sync_transaction.py:82-110 |
| Dirty work admission and parking use complete typed side records. | `_preflight_participating_sides` | mcp/src/agents_remember/worktrees/sync_transaction.py:387-402 |
| Currentness and continuation use Git facts and content-only conflicts. | `_already_current_result` | mcp/src/agents_remember/worktrees/sync_transaction.py:333-359 |
| The delegated Git owner excludes only the memory cache while retaining exact native merge proofs. | `worktree_dirty_paths` | mcp/src/agents_remember/worktrees/sync_transaction_git.py:117-141 |
| Pinned authority and parked-work restoration remain separate owners. | `pin_authority` | mcp/src/agents_remember/worktrees/sync_transaction_authority.py:121-126 |
| Terminal finalization/cancellation and damaged-journal recovery are delegated. | `finalize_sync` | mcp/src/agents_remember/worktrees/sync_transaction_recovery.py:56-92 |

## Cross-Repo References

The code/memory or fixture-repository boundaries above are established by package-local source.
No additional configured external or sibling-repository evidence is claimed.

| Finding | Anchor | Source |
| --- | --- | --- |
| No additional configured cross-repository evidence. | — | — |

## Update History

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