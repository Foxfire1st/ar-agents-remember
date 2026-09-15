# mcp/tests/test_worktree_sync.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_worktree_sync.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T01:15+00:00 |
| lastVerifiedCommitHash | `7cbda30d9a9a4c2944382fbef46ac58b85329935` |
| lastVerifiedCommitDate | 2026-09-15T05:15:42+02:00|
| verificationStatus | working-candidate |
| governingOverview | `overview.md` |

The body describes the uncommitted LCA L9 working candidate. The commit fields identify the latest real commit touching this source file; they do not claim that the candidate is committed or accepted.

## Governing Overview

[Nearest governing route overview](overview.md)

## Purpose

Exercise real code/external-memory sync, retained conflicts, cache independence, exact source/base publication, and journal quarantine.

## Code Commentary

### Logic

`SyncFixture` creates disposable code/memory worktrees and canonical contracts. Some setup deliberately retains or commits historical tracked memory.md states; these are inputs to prove cache independence, not cache commits created by the sync under test. `map_official_memory` writes attribution in a real memory-content commit.

The seven scenario definitions cover two-sided fast-forward, a retained code conflict and continuation, stale/missing/malformed source caches, cache-independent start and memory-candidate identity, an already-current descendant with changed cache rows, native memory merge conflicts, and quarantine of a nonregular journal without following it.

The native memory case checks both cache-only success and a genuine README conflict. Real draft WIP is parked and returned while staged cache data is excluded. It asserts the exact merge parents, only one new reachable merge beyond its parents, a cache-free committed tree, an untracked materialized cache, and both source/work content. Its interrupted-merge branch adds an unstaged real edit after the merge was staged: resume must refuse with both repositories' refs unchanged, then complete after that edit is staged.

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

| Finding | Citations | Source Path |
| --- | --- | --- |

## Repo-Internal References

These current source spans identify the implementation owners and the specific assertions supporting the file's behavior. A test definition is evidence of its assertions, not an execution or certification receipt.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The real Git fixture and attributed official memory update. | L39-L117; L102-L114 | [mcp/tests/test_worktree_sync.py](mcp/tests/test_worktree_sync.py) |
| Fast-forward and retained code conflict behavior. | L121-L141; L143-L178 | [mcp/tests/test_worktree_sync.py](mcp/tests/test_worktree_sync.py) |
| Cache-independent source admission, start, and candidate identity. | L180-L206; L208-L240; L242-L279 | [mcp/tests/test_worktree_sync.py](mcp/tests/test_worktree_sync.py) |
| Native cache-only success, real conflict continuation, and resumed staged-content validation. | L281-L362; L364-L397 | [mcp/tests/test_worktree_sync.py](mcp/tests/test_worktree_sync.py) |
| Nonregular journal quarantine preserves the outside target. | L399-L418 | [mcp/tests/test_worktree_sync.py](mcp/tests/test_worktree_sync.py) |

## Cross-Repo References

The operation and fixture boundaries described here are defined by same-repository contracts and Git helpers. No separate cross-repository document is used as evidence for this card.

| Finding | Citations | Source Path |
| --- | --- | --- |

## Update History

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
