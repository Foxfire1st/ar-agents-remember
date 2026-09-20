# mcp/src/agents_remember/worktrees/modules/sync.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/worktrees/modules/sync.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-09T14:45+02:00|
| reviewedWorkingCandidate | candidate `ar/260915-ks-l31-ar`, uncommitted; base `7dcec036094768c5f50e571fb45e59a27ae78efc` |
| lastVerifiedCommitHash | `74c6c693b8c5a5863ce15f016793192931f4adc1` |
| lastVerifiedCommitDate | 2026-09-20T06:22:08+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[worktrees/modules/overview.md](overview.md)

## Purpose

`sync.py` is the narrow public composition root for resumable, contract-addressed
`worktree_sync`. It establishes the canonical worktree contract, refreshes remote evidence,
serializes live mutation, and delegates either ordinary leaf/direct synchronization or
atomic-series selection plus synchronization to their focused transaction owners.

## Code Commentary

### Logic

`sync_result(args)` loads the configured contract and applies the sync-worktree admission rule.
Only leaf contracts require their ordinary code worktree to exist; a series transaction may create
operation-owned temporary `.sync` worktrees instead. It rejects invalid resolution/memory-choice
combinations before any fetch, selector, ref, or journal mutation.

A dry run does not fetch, acquire integration/store locks, publish series selection, or create
journal residue. It reports `skipped-preview` fetch evidence and asks the transaction driver for an
exact read-only projection. A live call refreshes code and external-memory upstreams outside the
integration-authority lock, then `_sync_live` re-reads and compares the complete contract under the
lock. If it changed during refresh, the result is `sync-contract-changed-retry` with the current
canonical contract path; the function never mutates against the stale object.

Under authority, series contracts delegate to
`sync_selected_atomic_series_under_authority`: this contract's own contract-keyed activation record
becomes `reconciling`, its pinned source pair is reconciled, and only a proven-current candidate
becomes `active`. The activation record is keyed per series contract (`contract_fingerprint` over the
canonical contract path), so a sync never reads, pauses, or names another master's record — the only
surviving activation waiting reason is `atomic-series-reconciling` on the addressed contract, and
genuine wave dependencies stay with the sprint execution graph's own `predecessor-incomplete:`
reasons. Leaf/direct contracts delegate to `sync_contract_under_authority`. Durable operation phase,
retained conflicts, continue/cancel, exact rollback, ledger-pair admission, and contract base updates
belong to the focused sync transaction modules rather than this facade.

### Conventions

This file deliberately contains no merge algorithm, journal parser, selector fallback, or queue
reader. Public expected failures (`ContractError`, `OSError`, `RuntimeError`, `UnicodeError`, and
`ValueError`) are translated at one boundary into `sync-operation-refused` with the observed fetch
evidence. Transaction-specific blocked/recovery states remain typed data returned by their owner.

Fetch is evidence refresh, not mutation authority: failure is reported per side and local protected
refs are re-read under the integration lock. Resolution uses `resolution_action` (`continue` or
`cancel`) on the same contract-addressed tool; no public operation id is accepted.

### Invariants And Boundaries

- Input validation precedes fetch, selector publication, journal writes, and Git mutation.
- Preview is observation-only and cannot claim selection or operation lifecycle authority.
- The contract is re-read under the repository integration lock after remote refresh.
- A genuine merge conflict is retained in the reported worktree for agent resolution; it is not
  aborted or converted into queue state.
- Atomic-series exposure follows successful exact reconciliation of THIS contract's own activation
  record; selection never comes from task prose, queue order, another master's record, or a
  compatibility reader.
- Expected contract/source failures return a controlled result rather than escaping the public MCP
  boundary.

### Todos

Reconcile exact source line ranges and any Dagger-driven state-vocabulary changes before final
verification metadata is stamped.

## Docs References

No external Domain Documentation source is configured for this memory repo.

| Finding | Anchor | Source |
| --- | --- | --- |


## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The public facade validates input, keeps preview mutation-free, refreshes outside the lock, rereads under authority, and dispatches by contract kind. | `sync_result`; `_sync_live` | mcp/src/agents_remember/worktrees/modules/sync.py:28-67; mcp/src/agents_remember/worktrees/modules/sync.py:70-98 |
| Shared upstream refresh reports per-side evidence without treating the remote as local mutation authority. | `fetch_source_upstreams` | mcp/src/agents_remember/worktrees/sync_source_refresh.py:9-29 |
| Atomic-series sync binds the public wrapper to the exact transaction on this contract's own activation record: it validates ownership, publishes `reconciling`, reconciles the pinned source pair, retains incomplete work in reconciling, and publishes `active` only after current-source proof; a foreign master is never read or named. | `sync_selected_atomic_series_under_authority`; `_sync_selected_atomic_series_under_authority` | mcp/src/agents_remember/worktrees/activation/atomic_series_activation_transaction.py:134-161; mcp/src/agents_remember/worktrees/activation/atomic_series_activation_transaction.py:164-226 |
| Ordinary transaction routing owns durable resume, continue, cancel, and recovery behavior. | `sync_contract_under_authority` | mcp/src/agents_remember/worktrees/sync_transaction.py:82-110 |
| Stable status and recovery evidence lives at the enclosure-root journal, not in the queue. | `SyncOperationStore`; `observe_sync_operation` | mcp/src/agents_remember/worktrees/sync_transaction_state.py:172-366; mcp/src/agents_remember/worktrees/sync_transaction_state.py:369-385 |
| Focused integration tests exercise fast-forward sync and contract advance, a retained code merge conflict with continuation, stale-cache source-ref selection, and content-conflict preservation. | `test_pure_fast_forward_sync_advances_both_sides_and_contract`; `test_code_merge_conflict_is_retained_and_can_continue`; `test_sync_uses_source_refs_when_the_cache_is_stale_missing_or_malformed`; `test_memory_merge_settles_content_and_knowledge_conflicts_in_the_transaction` | mcp/tests/test_worktree_sync.py:420-441; mcp/tests/test_worktree_sync.py:442-478; mcp/tests/test_worktree_sync.py:479-506; mcp/tests/test_worktree_sync.py:624-646 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |

## 260815-DAG-L4 Integration-Authority Impact

L4 makes task-derived integration refs mechanically non-ordinary: repository defaults, sprint supers, and active atomic-series refs are censused across code and external memory. Mutation is admitted only through exact lifecycle authority, named-ref compare-and-swap, queue/repository serialization, or a terminal capability; stale topology, aliases, ambient checkouts, and torn recovery fail closed.

## Update History
- 2026-09-20T07:40+02:00 — 260915-KS-L40 curator (uncommitted CYCLE-02-remainder change set on `ar/260915-ks-l40-ar`, code base `b7bfebb550f036a7e51de1f390be1123cd2d2172`): **reopened claim re-read against the construct its range now covers.** This leaf's own source edits grew the cited file, so the claim's evidence changed after the recorded verification. The claim names The focused integration nodes this card names, including `test_memory_merge_settles_content_and_knowledge_conflicts_in_the_transaction`; each named node now resolves at its own current `def` line and the cited range holds it, so the citation is current and the wording still holds unchanged — no re-cite and no re-wording was needed. Recorded here because a re-read is the disposition this class asks for; no bullet, row or range was deleted to silence it, and no verification stamp was advanced (the candidate is uncommitted and the governed closeout owns the real code and memory commits).
- 2026-09-20T07:24+02:00 — 260915-KS-L40 curator (uncommitted CYCLE-02-remainder change set on `ar/260915-ks-l40-ar`, code base `b7bfebb550f036a7e51de1f390be1123cd2d2172`): **citation ranges re-derived by reading the cited construct, not by arithmetic on the old numbers.** This leaf's own source edits grew the file this card cites, so the row(s) naming the four focused integration node names no longer held their anchor in the cited range. Each was re-read in the code worktree at the construct the claim names and re-pointed to that construct's own current declaration extent (`mcp/tests/test_worktree_sync.py:420-441`, `:442-478`, `:479-506` and `:624-646`). No claim wording, anchor or row was changed, added or deleted; no verification stamp was advanced — the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-20T02:24+02:00 — 260915-KS-L31 curator (uncommitted CYCLE-02 change set on `ar/260915-ks-l31-ar`, code base `7dcec036`): **cleared the one enforced `citation_claim_reopened` row this card carried by reading the claim and re-citing the construct that survived the upstream consolidation.** The row — *"Focused integration tests exercise fast-forward sync and contract advance, a retained code merge conflict with continuation, stale-cache source-ref selection, and content-conflict preservation."* — is CURRENT and its Finding text is RETAINED: the four properties it names are still what `mcp/tests/test_worktree_sync.py` measures. What changed is one anchor's name. `test_memory_merge_discards_only_cache_conflicts_and_preserves_content_conflicts` exists NOWHERE in the code tree; the merge-conflict case that carries its meaning is `test_memory_merge_settles_content_and_knowledge_conflicts_in_the_transaction` (`:391-408`), which now drives both conflict shapes — the shipped memory-content scenarios through `_assert_memory_content_conflict_scenarios` (`:410-492`) and CYCLE-02's knowledge-database shape — out of one case rather than two because the integration lane sits at its declared ceiling of 400 and a further collected case would breach it (D-46's mechanism: above the ceiling the lane runs ZERO tests). Only the Anchor cell's fourth entry was re-worded, to that surviving construct, and the Source cell now cites each of the four constructs at its own declaration extent: `:187-207`, `:209-244`, `:246-272` (the stale-cache case had moved from the cited `:185-212`), `:391-408`. No claim was re-worded, no anchor or range was dropped to silence a finding, and the two ranges that still satisfied the checker only because the membership test pools a row's ranges (they pointed at the `SyncFixture` body at `:126-184`) were corrected to the declarations they name rather than left standing. No `Generated citation repair` bullet in this document names this claim's anchors, so none was retired, and no verification stamp advanced: the `lastVerifiedCommitHash`/`lastVerifiedCommitDate` pair is untouched and the metadata block gains the `reviewedWorkingCandidate` row naming this leaf's uncommitted candidate. No commits.

2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.

- 2026-09-17T08:11:27+00:00 — 260915-KS-L9 curator (memory-quality closure): re-read every reopened claim in this card against code commit `c22beb0121946c0637e113ec4cf29da29fd4aec7` and advanced the verification stamp to that commit, which closeout re-stamps. A generated citation repair had already rewritten these ranges mechanically, so each was re-read rather than trusted: the range was checked against the current definition of the construct the claim is about, and the wording still holds. Extents chosen: `WorktreeSyncTests` at mcp/tests/test_worktree_sync.py:116-264.
- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): re-read the reopened claim in the row 97 of this card against the current code: its anchor still resolves inside the cited range, so the wording holds and the stamp advances
- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (reopened-claim judgement): the checker reopened
  the `WorktreeSyncTests` claim because that construct changed after verification and a generated
  repair had already moved its range mechanically. Re-read the claim against
  `mcp/tests/test_worktree_sync.py`: the class is defined at `:116` and the cited range (116-195)
  sits inside it, so the row still describes the focused integration suite. Retained; verification
  metadata remains closeout-owned.
- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (citation pass): re-derived the source ranges of 1
  claim(s) whose anchor no longer sat in its cited range and normalised 1 further range(s) in this
  card from their anchors against the frozen source snapshot (`agents-remember memory-citations
  --fix --document`, snapshot 188b8ecd). No claim wording changed; every rewritten range was read
  back at its current position. Verification metadata remains closeout-owned.
- 2026-09-13T14:21:11+02:00 — 260831-LOCR-L36: corrected the atomic-series sync description to the contract-keyed activation record (keyed by `contract_fingerprint` over the canonical contract path, not by protected source pair). The prose no longer says "the source-pair selector becomes `reconciling`"; it now says this contract's own record does, that a sync never reads/pauses/names another master's record, and that the only surviving activation waiting reason is `atomic-series-reconciling` on the addressed contract. Corrected the invariant that called the lock a "source-pair integration lock" (it is the repository integration lock) and the exposure invariant that implied a shared selection. Re-verified every reference row against the frozen code worktree: `sync_selected_atomic_series_under_authority` (`atomic_series_activation_transaction.py:134-161`) and `_sync_selected_atomic_series_under_authority` (`:164-226`) still hold — the declaration at 134 ends at 161 and the private owner at 164 ends at 226 — so both ranges are retained unchanged. No verification stamp advanced; no acceptance claim.
- 2026-09-11T23:05:00+00:00: Curator citation reconciliation: `SyncOperationStore`, `_sync_live`, `_sync_selected_atomic_series_under_authority`, `observe_sync_operation`, `sync_result`, `sync_selected_atomic_series_under_authority` repointed to mcp/src/agents_remember/worktrees/activation/atomic_series_activation_transaction.py:134-161, mcp/src/agents_remember/worktrees/activation/atomic_series_activation_transaction.py:164-226, mcp/src/agents_remember/worktrees/modules/sync.py:28-67, mcp/src/agents_remember/worktrees/modules/sync.py:70-98, mcp/src/agents_remember/worktrees/sync_transaction_state.py:172-366, mcp/src/agents_remember/worktrees/sync_transaction_state.py:369-385. No content impact: mechanical anchor-range projection against citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged.
- 2026-09-10T15:06+02:00 — No content impact: mechanical citation re-derivation after the closeout auto-carry change shifted lines in `sync_transaction.py` / `sync_transaction_state.py`; the cited symbols and their meanings are unchanged.

- 2026-09-09T14:45+02:00 — CCR-L42 curator reconciliation: re-read affected claims against the frozen current source and corrected only their source anchors/ranges; verification stamps remain closeout-owned.
- 2026-09-08T19:29:21+02:00 — Repaired the inherited claim-reopen citation by reading the current atomic-series transaction behavior and rebinding the sync wrapper/private transaction to their exact current ranges. Verification pins remain unchanged; no acceptance claim.
- 2026-09-06T22:41:21+00:00: Generated citation repair: `WorktreeSyncTests` repointed to mcp/tests/test_worktree_sync.py:116-195. No content impact: mechanical anchor-range projection bound to citation source snapshot 250eac92295fa399589ccf1c9726bfb4cd28a1a0b20dca126769403fba09b52d; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-08-26T08:30+02:00 — Rebounded source-refresh and public sync-suite citations to the frozen
  file extents; behavior claims are unchanged.

- 2026-08-26T03:37+02:00 — Replaced the obsolete abort-on-conflict/local-merge description with
  the current public facade: mutation-free preview, pre-lock source refresh, post-refresh contract
  reread, series selection plus sync, ordinary resumable sync, retained conflicts, explicit
  continue/cancel, and one controlled expected-failure boundary. Verification remains
  post-Dagger/closeout-owned.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-15T23:38+02:00 — Reconciled this worktree owner's role in task-derived protected-ref authority, exact named-ref movement, and crash-safe recovery. Verification metadata remains closeout-owned.
- 2026-08-14T05:26Z — L23 final curator: re-read the expanded task-reopen/worktree-start recovery
  vocabulary and retained sync's separate recovery-guidance ownership with current anchors.
  Verification remains closeout-owned.
- 2026-08-04T13:15:12+02:00 — 260731-EFA-L6 S18-B02 curator: extended the sync-log contract claim through its defining comments and regenerated the final range with the scoped fixer.
- 2026-08-03T02:57+02:00 — W3-B03 curator: curated 5 table citations for freshness, remote fetch, git timeout, recovery guidance, and sync tests; fixer-generated ranges verified.

- 2026-08-01T09:12+02:00 — 260731-EFA-L4 curator: the Conventions section said blocked payloads
  carry "`next_guidance` recovery args"; that call is gone. `_memory_sync_block` now calls
  `recovery_guidance("choose_memory_sync_recovery", tool="worktree_sync",
  args=contract_next_args(contract), required_args=["memory_sync_choice"])`, and the import block
  at the top of the module takes `recovery_guidance` in place of `next_guidance` (it imports no
  `next_guidance` at all now). Corrected the sentence and recorded why the split exists: the emitted
  keys are unchanged, but `next_guidance` is now narrowed to the phase vocabulary
  `WorktreeSummary` imports, and `choose_memory_sync_recovery` is a `RecoveryOperation` because this
  payload is a block rendered as a `FlexibleToolResponse`, not a lifecycle phase. Added the
  `guidance.py` reference row. Nothing else in this module changed — the five L2 helpers, the
  consistent-pair gate, both merge paths and the L3 timeout note all still describe the file
  exactly. Verification metadata pinned until closeout stamps the L4 commit.
- 2026-07-31T20:58+02:00 — 260731-EFA-L3 curator: `run_git` now comes from
  `kernel.git_command`, not `modules.git`. The module's own logic is untouched, but the
  Conventions section asserted "States are data" without qualification and that no
  longer holds unconditionally: the shared runner always sets a timeout (the 300s
  `GIT_LOCAL_TIMEOUT_SECONDS` default, taken by all six `run_git` calls here — `_consistent_pair_block`,
  `_sync_code`, `_aborted_merge_state` x2, `_move_memory_branch` x2), the module's only `except` is
  `LedgerError`, so a stalled git raises `subprocess.TimeoutExpired` out of `sync_result` where the
  old unbounded local runner hung instead. Recorded that one bounded exception and added the
  `kernel/git_command.py` reference. Verification metadata pinned until closeout stamps the L3
  commit.
- 2026-07-31T00:00+02:00 — 260731-EFA-L2 (gate honesty, `C901`/`PLR0911`/`PLR0912` armed with no
  exemptions): extracted `_stop_before_sync`, `_memory_sync_block`, `_memory_branch_move`,
  `_move_memory_branch` and the shared `_aborted_merge_state` (now used by both the code and memory
  merge paths). The dry-run `would-<move>` states are now derived from the same decision the real
  path executes. Every payload, summary string and exit code is unchanged. Verification metadata
  pinned until closeout stamps the L2 commit.
- 2026-06-10T09:56+02:00: Created as issue #54 sub-task D — atomic mid-task base-pair sync with consistent-pair gate, merge/ff sides, memory_sync_choice recoveries, and contract sync_log.
