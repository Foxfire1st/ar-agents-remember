# mcp/tests/test_integration_branch_authority.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_integration_branch_authority.py` |
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

Protect exact integration-ref ownership, two-output CAS races, and real object/ancestry checks independently of cached ledger data.

## Code Commentary

### Logic

The class exercises protected branch aliases/nested checkouts/memory names, a code CAS followed by a competing memory CAS, and successful publication with missing or damaged cache data. The torn-pair case preserves the raced memory ref and reports accepted/intended code and actual memory commits. Cache-damage cases verify the accepted refs land without increasing reachable memory history.

Two minimal real-repository cases exercise the surviving proof directly: accepted memory outside the exact source ancestry refuses, and an absent accepted code object refuses even when memory is current. Historical table-row/header tests and their cache-commit fixture machinery are retired; arbitrary cached rows are no longer a publication predicate.

### Conventions

The broader cases use the shared configured authority fixture; the object/ancestry cases use a minimal contract so the Git predicate is the subject. These assertions do not certify a live installation.

### Invariants And Boundaries

- A torn pair never permits clobbering concurrent memory work.
- Cache damage cannot change accepted output identity or block ref movement.
- The accepted code object and memory source ancestry remain mandatory.
- Fixture setup and historical coverage notes do not imply additional retained scenarios.

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
| Protected branch aliases and nested/foreign workbench identities refuse. | `test_branch_alias_nested_checkout_and_memory_name_cannot_bypass_refusal` | mcp/tests/test_integration_branch_authority.py:54-78 |
| A competing memory CAS is preserved after code has landed. | `test_external_pair_cas_retains_torn_pair_without_clobbering_memory_race` | mcp/tests/test_integration_branch_authority.py:80-170 |
| Cache absence/corruption cannot affect the accepted pair or create another memory commit. | `test_cache_damage_cannot_change_the_accepted_pair_or_block_its_ref_move` | mcp/tests/test_integration_branch_authority.py:172-213 |
| Real accepted-object and source-ancestry failures remain enforced. | `test_the_accepted_memory_commit_must_descend_from_the_exact_source` | mcp/tests/test_integration_branch_authority.py:262-277 |
| Production ref preparation and publication proof. | `prepare_integration_ref_move` | mcp/src/agents_remember/worktrees/integration/integration_ref_transaction.py:103-160 |

## Cross-Repo References

The operation and fixture boundaries described here are defined by same-repository contracts and Git helpers. No separate cross-repository document is used as evidence for this card.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.

- 2026-09-15T01:15+00:00 — 260913-LCA-L9 working candidate: Consolidated ledger row/header clauses into actual accepted-object/ancestry checks and cache-independent ref movement; preserved branch-ownership and torn-pair CAS regressions. Current source and citation targets were checked; the metadata records the last real file commit, and candidate changes remain uncommitted.
- 2026-09-14T11:58+02:00 — 260913-LCA-L11 curator (uncommitted change set on `ar/260913-lca-l11-ar`,
  base `4214d7a1`): the module's landing-clause surface was rewritten rather than trimmed, and this
  card previously did not describe it at all. Recorded the six-case inventory with ranges: the
  mapping clause (including a table that names the landed code commit with *different* memory
  content), the **conditional** source-ancestry clause with the divergent-source fixture that makes
  it bite, the replacement row-truth rule with the two shapes now **asserted as accepted** (a
  dropped and a duplicated source row — the shapes a rebuild produces), the unchanged reclosed-leaf
  accumulation case, and the two new module-level cases that drive `_require_true_rows` directly
  over a minimal contract. Recorded why the accepted cases are kept rather than deleted, and that
  the card must not be read as licensing a weakened rule. Repointed the two case ranges that had
  drifted and corrected "the retained three cases" to the measured population. Verification metadata
  remains closeout-owned; no acceptance claim and no verification stamp advanced.
- 2026-09-12T01:26:36+00:00: Generated citation repair: `test_r4_no_crash_recovery_path_exists_after_a_torn_ref_move` repointed to mcp/tests/test_closeout_kept_rules_pins.py:286-300. No content impact: mechanical anchor-range projection bound to citation source snapshot 1b5cbe38ab438de766feb0fc3860228f5125b623ebbee641f90211d51326d68e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T23:05:00+00:00: The claim said a code-only crash completes the exact memory ref on retry and cited `test_external_code_only_crash_completes_the_exact_memory_ref_on_retry`; that capability and its case were removed, and the behaviour now lands as the negative pin `test_r4_no_crash_recovery_path_exists_after_a_torn_ref_move` in `mcp/tests/test_closeout_kept_rules_pins.py`.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `test_branch_alias_nested_checkout_and_memory_name_cannot_bypass_refusal` repointed to mcp/tests/test_integration_branch_authority.py:132-156. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-06T21:46+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.


- 2026-08-26T03:37+02:00 — Updated the exact authority edge: canonical series sync is admitted,
  but direct unjournaled protected-ref integration remains refused. Verification remains
  post-Dagger/closeout-owned.

- 2026-08-25T15:44+02:00 — PDLS whole-system reconciliation updated the implementation summary
  above after source and requirement review. Verification remains closeout-owned.


- 2026-08-24T14:48+02:00 — DAGQC cumulative CLIVE final-gap curation: reconciled this test card to current source while preserving prior history and verification provenance.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this test card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: curated relationship changes against accepted candidate tree `4241908c`; verification metadata remains pinned until governed closeout.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-19T22:32+02:00 — No content impact: 260815-DAG-L13 added an isinstance narrowing to the recovered series-bootstrap assertion after `ensure_master_series_contract` gained the blocked-result union; documented authority behavior is unchanged. Verification remains closeout-owned.

- 2026-08-17T13:20+02:00 — No content impact: L5 repair: re-pointed stale mock targets and return tuples to match the L5 integration API (publish_queue_candidate_integration_result_under_authority, branch_commit, 4-tuple _prepare_integration_commits, durable-removal-intent idempotency). The documented test intent and coverage surface are unchanged.

- 2026-08-16T05:18+02:00 — Dagger fixture repair: repository-global standalone census expectations include the concurrently commanded atomic sibling, and journaled candidate worktrees remain inside their contract-owned worktree group.
- 2026-08-16T04:06+02:00 — Dagger fixture repair: exact authority tests now use recorded leaf worktrees, named atomic-memory checkouts, standalone default sources, active-task surface lifetime, and fresh paired bootstrap recovery facts.
- 2026-08-16T03:29+02:00 — No content impact: retargeted the injected Git-error mock to the extracted repository-facts owner so the same fail-closed public assertion remains executable after the size split. Verification remains closeout-owned.
- 2026-08-16T03:24+02:00 — 260815-DAG-L4: moved shared fixture builders to the dedicated support module without changing the production routes or assertions. Verification remains closeout-owned.
- 2026-08-15T23:38+02:00 — 260815-DAG-L4: created integration branch authority forcing onboarding from the frozen integration-authority candidate. Verification remains closeout-owned.
