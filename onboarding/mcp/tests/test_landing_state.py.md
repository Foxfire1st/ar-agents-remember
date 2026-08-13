# mcp/tests/test_landing_state.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_landing_state.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-01T09:56+02:00 |
| lastVerifiedCommitHash | `1580f92715ff93c988f9a15439ad9bec60ef4c5d` |
| lastVerifiedCommitDate | 2026-08-13T00:18:59+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[mcp overview](../overview.md)

## Purpose

Focused tests for the background landing observer and its honest snapshot contract.

## Code Commentary

The suite exercises bounded, contract-scoped observation; slow and failed
probes; stale carry-forward and age transitions; startup and rewritten-contract
missing state; cancellation; and the frozen-facts lifecycle. The later tests
cover fully observed completion, refusal to freeze missing or pending facts,
fresh-refresher reads, reducer-key filtering, corrupt or stale frozen files,
and reopening that clears the frozen result.

## Invariants And Boundaries

Tests use temporary coordination roots and mocked observers; they stay
offline and cover the landing-state behavior exercised in this file.

## Docs References

No external Domain Documentation source is configured.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Bounded, isolated refresh and stale-fact behavior. | `test_refresh_is_bounded_and_isolated_by_exact_contract`; `test_failed_refresh_keeps_last_truth_as_explicit_stale_fact` | mcp/tests/test_landing_state.py:104-132; mcp/tests/test_landing_state.py:134-158 |
| Missing, rewritten, cancelled, and recovered refresh lifecycle behavior. | `test_startup_and_rewritten_contract_are_explicitly_missing`; `test_cycle_failure_logs_then_recovers_on_normal_cadence`; `test_run_cancellation_leaves_no_refresh_task` | mcp/tests/test_landing_state.py:160-179; mcp/tests/test_landing_state.py:183-204; mcp/tests/test_landing_state.py:206-225 |
| Fully observed frozen facts and the no-freeze cases. | `test_finished_contract_freezes_once_and_leaves_the_sweep`; `test_unobserved_facts_do_not_freeze`; `test_pending_cleanup_keeps_probing_without_freezing` | mcp/tests/test_landing_state.py:239-266; mcp/tests/test_landing_state.py:268-285; mcp/tests/test_landing_state.py:287-302 |
| Frozen-file persistence, key filtering, corruption, age, and reopen behavior. | `test_frozen_facts_survive_a_fresh_refresher`; `test_frozen_rows_carry_only_reducer_known_keys`; `test_corrupt_final_file_keeps_contract_in_sweep_and_selfheals`; `test_frozen_file_predating_the_contract_is_never_served_or_kept_out_of_sweep`; `test_reopen_task_entry_point_deletes_the_frozen_landing_file` | mcp/tests/test_landing_state.py:304-319; mcp/tests/test_landing_state.py:333-345; mcp/tests/test_landing_state.py:430-457; mcp/tests/test_landing_state.py:475-528; mcp/tests/test_landing_state.py:530-554 |

## Cross-Repo References

No cross-repo references.

## 260718-CHATS-L5I Current Delta

Landing-state tests cover freezing fully observed completed facts, rejecting
stale or corrupt frozen files, and clearing the frozen result on reopen.

This entry supersedes conflicting earlier coverage notes while retaining their history; source verification metadata is deliberately unchanged until the code commit.

## L23 Reopen Test Isolation

The resurrection test explicitly treats parent lineage as non-applicable while
testing landing freeze/reopen behavior. Source-lineage policy is covered by the
dedicated reopen suite, so this mock preserves the test's existing ownership.

## Update History
- 2026-08-12T20:10+02:00 — L23 curator: documented bounded lineage isolation in landing-state reopen coverage; verification remains closeout-owned.
- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-04T08:03:35+02:00 — 260731-EFA-L6 S18-B07 curator: repaired the bounded citation findings from the recovered Avicenna and Kuhn ledgers, splitting or narrowing claims to the frozen source and normalizing scoped citation ranges.

- 2026-08-01T09:56+02:00 — 260731-EFA-L4 curator: corrected the fixture
  helper's workflow kind from `"light"` to `"light-task"`. No current
  landing-state behavior changed.

- 2026-07-31T16:50+02:00 — No content impact: the only change is the `_contract` fixture helper,
  which now calls `default_contract` with the `ContractTask` / `LeafIdentity` / `RepoBranchPlan`
  parameter objects introduced for PLR0913 instead of ten loose keyword arguments. The same
  per-index contract identities are still produced, and no observer test case, probe scenario, or
  assertion in this suite changed, so the coverage record above still holds.

- 2026-07-24T13:18:47Z — 260718-CHATS-L5I curator: refreshed the regression-coverage record for the current backend/shared behavior and preserved the pre-commit verification stamp.

- 2026-07-12T17:30+02:00 — 260712-TRH-L7: created focused coverage for bounded background landing observation and safe cancellation.
