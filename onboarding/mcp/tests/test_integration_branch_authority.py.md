# mcp/tests/test_integration_branch_authority.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_integration_branch_authority.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-14T11:58+02:00 |
| lastVerifiedCommitHash | `187414cef8150a8004fc1b023a8377f77b24e873` |
| lastVerifiedCommitDate | 2026-09-14T12:13:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Protected integration ref ownership and external-pair crash recovery.

## Code Commentary

### Logic

Branch aliases, nested checkouts and memory names cannot bypass protected-ref refusal. If code CAS succeeds while a competing memory update wins, recovery preserves that raced memory ref and reports the torn pair. A code-only crash no longer completes the exact memory ref on retry: mid-crash integration-ref recovery was removed as a capability, so the operator re-runs `worktree_integrate` against live refs.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

**Since 260913-LCA-L11 the module carries the landing's own clause inventory.** Six cases in
`IntegrationBranchAuthorityTests` plus two module-level cases now witness
`require_integrated_ledger_mapping` clause by clause against real repositories built by
`_reclosed_leaf_memory_history` (`:105-136`), so a clause cannot be silently dropped again. Three
of the ledger cases were **rewritten** by this leaf, and two were **added**:

| Case | Range | What it pins |
| --- | --- | --- |
| `test_ledger_keeps_every_true_mapping_a_reclosed_leaf_accumulated` | `:259-293` | unchanged: a leaf that closed out, synced and closed out again lands both real mappings ahead of the source history, each row verified rather than counted. |
| `test_ledger_refuses_a_ledger_that_does_not_map_the_landed_code_commit` | `:295-329` | the first promise, which the file rule never carried: a table that never names the landed code commit, **and** one that names it with different memory content, both refuse. |
| `test_ledger_refuses_memory_content_that_does_not_descend_from_the_source` | `:331-382` | the ancestry promise **and its condition**: it builds a divergent source line, asserts the divergence is real (`is_ancestor` is false) so the case cannot pass by fixture drift, and shows the refusal. |
| `test_ledger_refuses_untrue_rows_and_accepts_a_rebuilt_source_region` | `:384-527` | the replacement rule: an untrue memory cell and a code commit the repository does not hold refuse by name with the row in the message, a header disagreeing with its own first row refuses with the closeout remedy, and — asserted as **accepted** — a dropped source row and a duplicated source row now land, because they are exactly the shapes a rebuild produces. |
| `test_the_landed_ledger_commit_must_carry_the_memory_content_it_maps` | `:581-614` | new, module level: a row naming memory content the landed ledger commit does not carry is refused even though the mapping clause is satisfied. |
| `test_the_landed_ledger_must_name_a_code_commit_the_repository_holds` | `:617-642` | new, module level: the other half, exercised directly on `_require_true_rows` over a minimal repository. |

The two module-level cases import `_require_true_rows` and build a bare `WorktreeContract` through
`_integration_contract` (`:549-578`) rather than standing up a whole enclosure, because the clauses
read exactly three cells (two repositories and the contract kind) and a full fixture would make the
case measure the fixture instead of the rule.

### Invariants And Boundaries

A torn pair is not permission to clobber concurrent memory work. The retained cases do not prove the historical bootstrap-WAL or broad surface census.

**An accepted case is evidence too.** The two shapes this module now asserts as *accepted* are the
leaf's own statement of what the removal changed; deleting them because they no longer refuse would
have hidden the change. Do not restore the refusals, and do not weaken the refusals that remain: a
false row and a disagreeing header still refuse, on both counts.

### Todos

No file-local implementation change is requested by this reconciliation.

## Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain evidence applies to the file-local claims above. | N/A | N/A |

## Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

| Finding | Anchor | Source |
| --- | --- | --- |
| Branch alias nested checkout and memory name cannot bypass refusal. | `test_branch_alias_nested_checkout_and_memory_name_cannot_bypass_refusal` | mcp/tests/test_integration_branch_authority.py:140-164 |
| External pair cas retains torn pair without clobbering memory race. | `test_external_pair_cas_retains_torn_pair_without_clobbering_memory_race` | mcp/tests/test_integration_branch_authority.py:166-257 |
| The landing's first promise: the landed code commit is mapped to the landed memory content, and a table naming it with different content is refused too. | `test_ledger_refuses_a_ledger_that_does_not_map_the_landed_code_commit` | mcp/tests/test_integration_branch_authority.py:295-329 |
| The source-ancestry promise is conditional, and the case builds the divergent source the promise exists for rather than drifting into the trivial answer. | `test_ledger_refuses_memory_content_that_does_not_descend_from_the_source` | mcp/tests/test_integration_branch_authority.py:331-382 |
| Row truth replaced the file rule: an untrue memory cell and a missing code commit refuse by name, a disagreeing header refuses with the closeout remedy, and a dropped or duplicated source row is **asserted as accepted**. | `test_ledger_refuses_untrue_rows_and_accepts_a_rebuilt_source_region` | mcp/tests/test_integration_branch_authority.py:384-527 |
| The two repository-level row-truth clauses, exercised directly and over a minimal contract. | `_require_true_rows`; `_integration_contract`; `test_the_landed_ledger_commit_must_carry_the_memory_content_it_maps`; `test_the_landed_ledger_must_name_a_code_commit_the_repository_holds` | mcp/src/agents_remember/worktrees/integration/integration_ref_transaction.py:345-380; mcp/tests/test_integration_branch_authority.py:549-578; mcp/tests/test_integration_branch_authority.py:581-614; mcp/tests/test_integration_branch_authority.py:617-642 |
| The shared fixture the ledger cases build their world from, and the ledger helpers they author it with. | `_reclosed_leaf_memory_history`; `_ledger_with_rows`; `_commit_ledger`; `_ledger_text_with_header` | mcp/tests/test_integration_branch_authority.py:105-136; mcp/tests/test_integration_branch_authority.py:64-72; mcp/tests/test_integration_branch_authority.py:75-81; mcp/tests/test_integration_branch_authority.py:84-95 |
| Mid-crash code-only ref recovery was removed as a capability: its only input was the journaled expected pre-move ref value, which has no durable source, so the operator re-runs `worktree_integrate` against live refs instead. `test_r4_no_crash_recovery_path_exists_after_a_torn_ref_move` pins that no recovery entry point exists. | `test_r4_no_crash_recovery_path_exists_after_a_torn_ref_move` | mcp/tests/test_closeout_kept_rules_pins.py:286-300 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History
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
## Docs References

No external Domain Documentation source is configured for this internal route; task `260821-CLIVE-L1` and the cited repository source/tests govern this curation.


## Cross-Repo References

This file owns no ambient cross-repository authority. Any external-memory repository it reaches remains explicitly contract-addressed.
