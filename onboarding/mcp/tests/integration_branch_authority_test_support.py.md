# mcp/tests/integration_branch_authority_test_support.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/integration_branch_authority_test_support.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T01:15+00:00 |
| lastVerifiedCommitHash | `14582854955223f75588c23c9f29f9d51bde9675` |
| lastVerifiedCommitDate | 2026-09-18T09:05:03+02:00|
| verificationStatus | working-candidate |
| governingOverview | `overview.md` |

The body describes the uncommitted LCA L9 working candidate. The commit fields identify the latest real commit touching this source file; they do not claim that the candidate is committed or accepted.

## Governing Overview

[Nearest governing route overview](overview.md)

## Purpose

Build configured disposable repository/topology and closed-leaf fixtures for integration authority scenarios.

## Code Commentary

### Logic

`_authority_fixture` constructs the exact code/memory repositories, protected branches, task topology, selected profile configuration, and sibling atomic-series contract. External baseline memory is a real content commit with Code-Commit attribution; its ledger is refreshed only as an untracked cache.

`_closed_external_leaf_worktrees` materializes the ordinary leaf worktrees and onboarding root, creates actual code and attributed memory commits, refreshes the disposable cache, and records only the two accepted outputs. `_publish_completed_closeout_fixture` optionally enters the selected/ordinary lifecycle input owner before publishing the fixture's completed state; its explicit final-source override models target changes after admission. `_doc` remains the small task-model builder.

Unused atomic-landing/door/preview builders and their ledger-only commit machinery were removed. Support code itself is not collected scenario coverage.

### Conventions

Helpers build production-shaped inputs for their consumers; synthetic completed fixture state is not an executed acceptance or certification result. Candidate repositories and paths remain explicitly configured and confined to the temporary world.

### Invariants And Boundaries

- Real code/memory objects back the recorded output cells.
- Cache materialization produces no third commit or ledger output field.
- Onboarding-root and canonical task/enclosure identity remain present so tests reach their intended seam.
- No queue row or guessed ambient path substitutes for ref authority.

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
| Closed external leaves are backed by two actual commits and a disposable cache. | `_closed_external_leaf_worktrees` | mcp/tests/integration_branch_authority_test_support.py:48-91 |
| None | `_publish_completed_closeout_fixture` | mcp/tests/integration_branch_authority_test_support.py:94-126 |
| None | `_authority_fixture` | mcp/tests/integration_branch_authority_test_support.py:129-286 |
| Consumers retain ownership, cache-independence, and CAS scenarios. | `test_external_pair_cas_retains_torn_pair_without_clobbering_memory_race` | mcp/tests/test_integration_branch_authority.py:80-170 |

## Cross-Repo References

The operation and fixture boundaries described here are defined by same-repository contracts and Git helpers. No separate cross-repository document is used as evidence for this card.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.


- 2026-09-16T14:05+02:00 — 260915-CAPS-L12 curator: **current-tense claim corrected** for the removal of `internal` memory mode (`CAPS-R12@v1`). The 2026-08-16 fixture-repair entry described code-only authority fixtures as modelling "configured internal memory explicitly", which the removal made false; the entry keeps its historical date and now records the supersession — the fixture declares `external` when `external_memory` is true and the supported `disabled` otherwise (`line 138`). Verification metadata remains closeout-owned: the source is uncommitted, so no stamp was advanced and no commit hash was invented.
- 2026-09-15T01:15+00:00 — 260913-LCA-L9 working candidate: Migrated retained baseline/closed-leaf builders to one attributed memory commit and untracked cache; removed unused ledger-era atomic-door/preview helpers and retired fields. Current source and citation targets were checked; the metadata records the last real file commit, and candidate changes remain uncommitted.
- 2026-09-11T23:05:00+00:00: The claim named `_closed_leaf_worktree` as the closed-leaf fixture helper, but that internal-memory helper was deleted as unreachable when the detached lifecycle worker was removed; the surviving shared helper for closed leaf worktrees is `_closed_external_leaf_worktrees`, and the four cited ranges now project each named helper's exact current definition extent.
- 2026-09-11T22:39:01+00:00: Generated citation repair: "def _claimed_atomic_leaf_door(" repointed to mcp/tests/integration_branch_authority_test_support.py:490-490. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `_record_additional_atomic_leaf_landing` repointed to mcp/tests/integration_branch_authority_test_support.py:406-487. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: "def _authority_fixture(" repointed to mcp/tests/integration_branch_authority_test_support.py:157-157. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-09T02:42:21+02:00 — CCR-L24 inherited/current-source reconciliation 2026-09-09: Re-read the current card purpose, logic, invariants, and cited route against the frozen candidate source; no content or route change was required, and the existing claim bytes remain accurate. source-sha256=a5aabfbfd3259e1f38bf772c6dd51717ccd2cfe3b5e53a585b5659c8ce0708ba; verification metadata remains unchanged because commit-owned realization is pending.


- 2026-09-06T23:08:28+00:00 — Reconciled retained source behavior and fixture limitations for IAS recovery; prior verification pins retained.

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for 99dc249bd507 (CCR-R02@v2/L25):
  claimed atomic-leaf door fixtures now stamp `taskIntent=contract_task_intent(...)` and the
  additional-landing helper attaches the door after task/master writes; documented the intent-bound
  fixture contract. Verified at code commit 99dc249bd507c20b09ece1169c2b1fa2af8e8c1b.

- 2026-08-30T05:55+02:00 — MCAR-L03 A005: external-memory closeout fixtures now create the
  onboarding directory required by the exact pair contract, so lifecycle-conflict tests exercise
  their intended ordering instead of failing on an incomplete memory fixture.

- 2026-08-25T15:44+02:00 — PDLS whole-system reconciliation updated the implementation summary
  above after source and requirement review. Verification remains closeout-owned.


- 2026-08-24T14:48+02:00 — DAGQC cumulative CLIVE final-gap curation: reconciled this test card to current source while preserving prior history and verification provenance.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this test card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-20T05:12+02:00 — L11 landed-wave refresh: the leaf-segment graph-model commit
  (f2e2f4b9) touched this source; card re-verified against the current file, verification stamp
  advanced to f2e2f4b9. Body unchanged — the documented contract still holds.


- 2026-08-18T09:05+02:00 — Renamed the atomic 'barrier' concept to 'blocker' throughout (terminology unification; no behavioral change). Verification remains closeout-owned.

- 2026-08-17T12:30+02:00 — 260815-DAG-L5: extended the support surface for organizational-completion branch and recovery forcing. Verification remains closeout-owned.

- 2026-08-16T05:18+02:00 — Dagger fixture repair: code-only authority fixtures modeled the then-supported internal memory explicitly, keeping code-only integration behavior while satisfying exact runtime memory-mode authority. **Superseded by `CAPS-R12@v1`:** the fixture now models `external` when `external_memory` is true and the supported `disabled` otherwise (`memory_mode = "external" if external_memory else "disabled"`, line 138), because `internal` was removed from the product and is refused by name.
- 2026-08-16T04:06+02:00 — 260815-DAG-L4 Dagger repair: shared closed-leaf helpers now materialize the exact contract-recorded code and external-memory worktrees, and the atomic-series helpers persist each child leaf's exact closeout, integration, queue-binding, and memory-ledger landing facts before series seal tests run.
- 2026-08-16T03:24+02:00 — 260815-DAG-L4: moved shared configured-repository and closed-leaf fixture builders out of the main authority test so both split suites stay independently importable and below the test-file size limit. Verification remains closeout-owned.
- 2026-08-15T23:38+02:00 — 260815-DAG-L4: created integration-authority forcing support onboarding from the frozen integration-authority candidate. Verification remains closeout-owned.
