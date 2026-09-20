# mcp/tests/test_worktree_sync.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_worktree_sync.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T01:15+00:00 |
| lastVerifiedCommitHash | `0da444b3b2b61f6a86fa4076b283c305db025d22` |
| lastVerifiedCommitDate | 2026-09-20T02:38:15+02:00|
| verificationStatus | working-candidate |
| governingOverview | `overview.md` |

The body describes the uncommitted LCA L9 working candidate. The commit fields identify the latest real commit touching this source file; they do not claim that the candidate is committed or accepted.

## Governing Overview

[Nearest governing route overview](overview.md)

## Purpose

Exercise real code/external-memory sync, retained conflicts, cache independence, exact source/base publication, and journal quarantine.

## Code Commentary

The terminal-removal case uses the real Git fixture for tracked, missing, staged and untracked cache states. It verifies cache-free terminal preflight and actual non-forced memory-worktree removal. A neighboring `memory.md.other` file and a code-side `memory.md` remain protected. This adds one collected integration case using the existing fixture; no new test support or budget change is needed.

### Logic

`SyncFixture` creates disposable code/memory worktrees and canonical contracts. Some setup deliberately retains or commits historical tracked memory.md states; these are inputs to prove cache independence, not cache commits created by the sync under test. `map_official_memory` writes attribution in a real memory-content commit.

The scenario definitions cover two-sided fast-forward, a retained code conflict and continuation, stale/missing/malformed source caches, cache-independent start and memory-candidate identity, an already-current descendant with changed cache rows, native memory merge conflicts, and quarantine of a nonregular journal without following it.

The native memory case checks both cache-only success and a genuine README conflict. Real draft WIP is parked and returned while staged cache data is excluded. It asserts the exact merge parents, only one new reachable merge beyond its parents, a cache-free committed tree, an untracked materialized cache, and both source/work content. Its interrupted-merge branch adds an unstaged real edit after the merge was staged: resume must refuse with both repositories' refs unchanged, then complete after that edit is staged.

**CYCLE-02 gave the same case a second conflict shape, and it is the one Git cannot decide.** `_assert_knowledge_database_conflict_settles` builds a real three-commit branching scenario over a knowledge database with disjoint valid edits on both sides, commits those datasets into the memory worktree and the memory repository, and then syncs: the ordinary Git merge must stop on the binary file, the transaction must route the three-way merge through the shipped adapter, and the sync must **complete** with `state == "synced"`. What it asserts is exactly what the review asked for — both sides survive in the merged dataset, the merged identity differs from either side's, the three input datasets are byte-identical afterwards, and the merge commit's two parents are the two sides' own commits. The caller invokes no merge function: the test never calls `resolve_knowledge_merge_base` or `merge_resolved_knowledge_datasets`, which is the property that distinguishes a wired seam from a callable one. Both shapes share one collected case rather than taking one each, because the integration lane sits at its declared ceiling of 400 and a further collected case would breach it — above the ceiling conftest raises and the lane then runs zero tests, which is worse than either outcome it would report. The shipped content scenarios were moved intact into `_assert_memory_content_conflict_scenarios` and their body is unchanged.

The module also became a consumer of the shared `merge_case_test_support` fixture for that case, which is why the lifecycle catalog's byte pin moved at this tip without any registered artifact or contract being added.

### Conventions

The inventory describes current scenario definitions, not a production deployment or a certification receipt. The native merge scenario keeps its subcases inside one collected case. Quarantine assertions inspect the archived symlink itself and preserve its outside target.

### Invariants And Boundaries

- Missing attribution or a broken cache cannot become a sync admission refusal.
- Real content conflicts retain MERGE_HEAD and require the intended resolution.
- Memory-side cache data never enters recorded real WIP or a new merge tree.
- Post-admission tracked edits must be staged before resumed merge publication.
- Real source/base/ref and journal identity remain the operation evidence.

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
| Tracked, missing, staged and untracked caches do not prevent memory removal; real memory and code files remain protected. | `test_terminal_removal_discards_only_the_memory_cache` | mcp/tests/test_worktree_sync.py:308-350 |
| The real Git fixture and attributed official memory update. | `map_official_memory` | mcp/tests/test_worktree_sync.py:44-122 |
| Fast-forward and retained code conflict behavior. | `test_pure_fast_forward_sync_advances_both_sides_and_contract`; `test_code_merge_conflict_is_retained_and_can_continue` | mcp/tests/test_worktree_sync.py:187-207; mcp/tests/test_worktree_sync.py:209-244 |
| Cache-independent source admission, start, and candidate identity. | `test_sync_uses_source_refs_when_the_cache_is_stale_missing_or_malformed`; `test_start_and_memory_candidate_do_not_take_authority_from_the_cache` | mcp/tests/test_worktree_sync.py:246-272; mcp/tests/test_worktree_sync.py:274-306 |
| Native cache-only success, real conflict continuation, and resumed staged-content validation. | `test_memory_merge_settles_content_and_knowledge_conflicts_in_the_transaction`; `_assert_memory_content_conflict_scenarios` | mcp/tests/test_worktree_sync.py:391-408; mcp/tests/test_worktree_sync.py:410-490 |
| **The CYCLE-02 knowledge-dataset case: the sync completes, both sides survive, and the caller invokes no merge entry point.** | `_assert_knowledge_database_conflict_settles` | mcp/tests/test_worktree_sync.py:129-183 |
| **The shared merge-case fixture this module began consuming for that case, and the two imports it takes from it.** | `build_case`; `file_digest` | mcp/tests/merge_case_test_support.py:177-205; mcp/tests/test_worktree_sync.py:44-45 |
| Nonregular journal quarantine preserves the outside target. | `test_nonregular_journal_is_renamed_without_following_and_quarantined` | mcp/tests/test_worktree_sync.py:528-547 |

## Cross-Repo References

The operation and fixture boundaries described here are defined by same-repository contracts and Git helpers. No separate cross-repository document is used as evidence for this card.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History

- 2026-09-20T01:37+02:00 — 260915-KS-L31 curator (uncommitted CYCLE-02 change set on `ar/260915-ks-l31-ar`, code base `7dcec036`): range repair only; no claim re-worded, no anchor renamed, no row deleted. The two pre-existing reference rows still cited this file's **pre-move** spans (`:126-146`/`:148-183` and `:185-211`/`:213-245`), which is where the four cases stood before this leaf's added case and helper pushed them down the class body. Re-derived with `grep -n` and read at each declaration, they now cite the four cases' own extents in the `WorktreeSyncTests` class as it stands: `test_pure_fast_forward_sync_advances_both_sides_and_contract` at `mcp/tests/test_worktree_sync.py:187-207` and `test_code_merge_conflict_is_retained_and_can_continue` at `:209-244` in the fast-forward/retained-conflict row, `test_sync_uses_source_refs_when_the_cache_is_stale_missing_or_malformed` at `:246-272` and `test_start_and_memory_candidate_do_not_take_authority_from_the_cache` at `:274-306` in the cache-independence row. The rows around them were already current on this candidate and are unchanged. No verification stamp advanced: the candidate is uncommitted and closeout owns the stamp.

- 2026-09-19T23:20+00:00 — 260915-KS-L31 curator (uncommitted CYCLE-02 change set on `ar/260915-ks-l31-ar`, code base `7dcec036`): **the module gained the case that proves the merge adapter is wired, and lost the name the card cited.** The shipped content-conflict case was renamed to `test_memory_merge_settles_content_and_knowledge_conflicts_in_the_transaction` and its body split, unchanged, into `_assert_memory_content_conflict_scenarios`; the second half is the new `_assert_knowledge_database_conflict_settles`, which drives a real divergent knowledge dataset through `SyncFixture.sync()` and asserts the sync completes, both sides survive, the inputs are untouched, and the merge commit's parents are the two sides. The claim about the shipped regression still holds, so it was kept and re-cited at its current name and helper rather than re-worded; the reference table gained the two new rows (the knowledge case and the `merge_case_test_support` imports it needs). No verification stamp advanced: the candidate is uncommitted and closeout owns the stamp.

- 2026-09-19T22:49:08+00:00: Generated citation repair: `test_terminal_removal_discards_only_the_memory_cache` repointed to mcp/tests/test_worktree_sync.py:308-350. No content impact: mechanical anchor-range projection bound to citation source snapshot e67b35357c3610162648ff9c1506b2bd840c93c142fe18de408cd68cfbaf5daa; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-19T22:49:08+00:00: Generated citation repair: `test_nonregular_journal_is_renamed_without_following_and_quarantined` repointed to mcp/tests/test_worktree_sync.py:528-547. No content impact: mechanical anchor-range projection bound to citation source snapshot e67b35357c3610162648ff9c1506b2bd840c93c142fe18de408cd68cfbaf5daa; claim bytes unchanged; generated by ccr-r10@v1.
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.

- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): stamped the untimestamped Update History entries with this document's own commit clock

- 2026-09-17T03:31:11+02:00 — 2026-09-15 — LCA L9 terminal delivery: The terminal-removal case uses the real Git fixture for tracked, missing, staged and untracked cache states. It verifies cache-free terminal preflight and actual non-forced memory-worktree removal. A neighboring `memory.md.other` file and a code-side `memory.md` remain protected. This adds one collected integration case using the existing fixture; no new test support or budget change is needed.

- 2026-09-15T06:37:50+02:00 — LCA L9 terminal delivery: The terminal-removal case uses the real Git fixture for tracked, missing, staged and untracked cache states. It verifies cache-free terminal preflight and actual non-forced memory-worktree removal. A neighboring `memory.md.other` file and a code-side `memory.md` remain protected. This adds one collected integration case using the existing fixture; no new test support or budget change is needed.



- 2026-09-15T01:15+00:00 — 260913-LCA-L9 working candidate: Replaced mid-cycle cache-row refusal with source-ref acceptance; added cache-independent start/candidate and native merge coverage. The existing native merge case also pins refusal of unstaged content on resume and successful staged continuation. Current source and citation targets were checked; the metadata records the last real file commit, and candidate changes remain uncommitted.


- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (drift re-verification): the case this card
  documents was added by the frozen change set. Re-read the card: the new case and every cited range
  hold, including `find_mapping` at `memory_ledger.py:261-263`. No wording changed. Verification
  metadata remains closeout-owned.

- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (provenance repair): the gate could not compare
  this claim with its verification provenance because one or more of its anchors resolved more than
  once at the verification commit, so no historical location was unique. Repaired the citation, not
  the claim: each anchor that named a construct by bare name now names its exact declaration text,
  which resolves once in the code tree, and any range that had drifted off its construct was re-read
  at the declaration. The claim wording is unchanged, and the construct each range covers is the one
  the claim is about. Verification metadata remains closeout-owned.

- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (drift re-verification): the source gained the
  descendant-ledger case the card already documents. Re-read the card against the current source:
  every cited range (97-99, 101-110, 117-137, 139-174, 176-204, 206-243, 245-264) still holds. No
  wording changed; verification metadata remains closeout-owned.

- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (citation pass): re-derived the source ranges of 1
  claim(s) whose anchor no longer sat in its cited range and normalised 1 further range(s) in this
  card from their anchors against the frozen source snapshot (`agents-remember memory-citations
  --fix --document`, snapshot 188b8ecd). No claim wording changed; every rewritten range was read
  back at its current position. Verification metadata remains closeout-owned.

- 2026-09-14T13:20+02:00 — Recorded the added dropped-row case: a memory work branch that already
  descends from its source and whose recomputed `memory.md` maps the code base to a newer content
  commit syncs as `already-current` with no `dropped parent mapping` text and no branch movement,
  which is the regression guard for the ruling that the ledger is derived state and the projection
  reports its own exclusions. Added the Purpose and Logic statements, the new reference row, and
  repointed `test_nonregular_journal_is_renamed_without_following_and_quarantined` (206-225 →
  245-264) and the evidence-lane row (182 → 184) after the insertion and the current manifest.
  Verification metadata remains closeout-owned; no acceptance claim and no verification stamp
  advanced.


- 2026-09-13T23:09+02:00 — 260913-LCA-L2 curator (uncommitted change set on `ar/260913-lca-l2-ar`):
  recorded the added mid-cycle case — a code tip the official memory line does not map refuses with
  `official line is mid-cycle`, leaves the work branch at its pre-sync head, and syncs once the pair
  is completed — together with the two fixture helpers it drives and the boundary that the refusal
  comes from `sync_transaction_authority.preflight_official_pair`'s named-ref ledger read rather
  than from the source-ledger reader this leaf changed. Repointed the stale citation for
  `test_nonregular_journal_is_renamed_without_following_and_quarantined` (176-195 → 206-225) after
  the insertion shifted it, and recorded the module's `integration` lane registration with the
  statement that registration is not execution evidence. Verification metadata remains
  closeout-owned; no acceptance claim and no verification stamp advanced.


- 2026-09-06T21:45:53+00:00 — Reconciled the retained IAS test/helper population and exact citation ranges, preserving prior history and verification provenance; no tests or review were run.



- 2026-08-26T08:50+02:00 — Rebound the recovery/cancellation reference to the frozen focused
  function names and range.


- 2026-08-26T08:45+02:00 — Restored canonical Docs/Cross-Repo reference sections for this changed
  sync integration suite card.


- 2026-08-26T08:30+02:00 — Restored the required governing-overview link for the frozen public
  sync integration suite.


- 2026-08-26T06:20+02:00 — Reconciled the fixture's exact-ref helper with the production
  `read_ref` API, removing a duplicate interpretation of Git absence. No test-execution claim is
  made.


- 2026-08-26T03:37+02:00 — Replaced obsolete abort/block coverage with the full resumable-sync
  contract: retained code/memory conflicts, continue/cancel, series temporary worktrees, pinned-ref
  cleanup, preview purity, invalid-input pre-admission refusal, raw/opaque quarantine, and partial
  authority manual repair. Verification remains post-Dagger/closeout-owned.


- 2026-08-17T12:30+02:00 — No content impact: L5 coverage-pragma alignment only; the documented sync behavior is unchanged.


- 2026-08-16T02:51+02:00 — L4 default-branch authority: the repository fixture now installs an
  exact remote default ref and symbolic `origin/HEAD`, allowing sync cases to reach their intended
  source and memory assertions without weakening fail-closed authority.


- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B23 curator: rebased the `sync_log` range; exact
  non-fixing check returns zero findings.


- 2026-08-02T21:14+02:00 — W2-B03 curator: resolved 2 initial citation findings (1 anchor, 0 prose, 1 source); scoped recheck PASS (0 findings). Verification metadata unchanged.


- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.

- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.

- 2026-07-31T16:50+02:00 — 260731-EFA-L2 curator, code-quality hardening sweep.
  No content impact: `SyncFixture` now builds its contract through
  `default_contract(ContractTask(...), leaf=LeafIdentity(...), code=RepoBranchPlan(...),
  memory=RepoBranchPlan(...))` instead of the flat keyword list, and everything else is
  `ruff format` reflow of the two `git worktree add` argument lists, two `assertEqual` calls,
  and the `subprocess.run` inside `git()`. This card names no `default_contract` keyword, and
  the same repo paths, source/work branches, and base commits are still paired, so the eight
  documented sync cases and their assertions are unaffected.

- 2026-06-10T09:56+02:00: Created with issue #54 sub-task D (8 tests over live-worktree fixtures).
