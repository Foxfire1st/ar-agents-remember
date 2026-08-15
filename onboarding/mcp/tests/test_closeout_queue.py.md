# mcp/tests/test_closeout_queue.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_closeout_queue.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-15T14:05+02:00 |
| lastVerifiedCommitHash | `17987fa66a642306eb8d20fa9a4bff2b881550d2` |
| lastVerifiedCommitDate | 2026-08-15T14:36:30+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Exercises the closeout queue's model, authority, ordering, evidence, transition, durability,
capacity, projection-cost, and sprint-publication contracts against real task and Git fixtures.
The small model and split-evidence ownership checks live in `test_closeout_queue_models.py` so this
behavior suite remains below the repository hard size limit.

## Code Commentary

### Logic

`QueueFixture` constructs canonical sprint/master/leaf task documents, contracts, curator artifacts,
register rows, repositories, and ledger facts. Tests cover categorical grading and deterministic
ties, internal/disabled memory, request bounds, authority refusal, predecessor/barrier logistics,
candidate/evidence drift, lifecycle ownership, WAL retry receipts, state bounds, linear fleet work,
cross-sprint refusal, and completion/reopen locking.

### Conventions

The suite manipulates the public service and durable store with production-shaped artifacts; exact
failure states are asserted rather than inferred from source strings.

### Invariants And Boundaries

- Judgment and logistics tests remain separate.
- Negative cases mutate one candidate fact at a time.
- Scaling tests compare two fleet sizes and enforce explicit caps.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Core queue tests cover categorical ordering and graph/leaf ties. | `test_explicit_grades_order_ready_candidates_by_graph_then_leaf_tie` | mcp/tests/test_closeout_queue.py:566-587 |
| Internal and disabled memory modes use explicit not-applicable readiness. | `test_internal_and_disabled_memory_modes_use_explicit_not_applicable_readiness` | mcp/tests/test_closeout_queue.py:596-609 |
| Barrier and predecessor logistics remain separate from scheduling judgment. | `test_predecessors_and_atomic_barrier_control_logistics_not_judgment` | mcp/tests/test_closeout_queue.py:633-709 |
| Candidate/evidence drift fails closed. | `test_candidate_and_evidence_drift_fail_closed` | mcp/tests/test_closeout_queue.py:781-791 |
| WAL publication retry and request receipts are exercised behaviorally. | `test_mutations_require_stable_request_id_and_retry_after_wal_publish` | mcp/tests/test_closeout_queue.py:900-942 |
| Sprint completion publication is serialized with queue quiescence. | `test_sprint_completion_publication_is_serialized_with_queue_quiescence` | mcp/tests/test_closeout_queue.py:1122-1151 |

## Cross-Repo References

No meaningful cross-repository reference applies.

## Update History

- 2026-08-15T14:05+02:00 — L3 final targeted-gate repair: shared queue fixtures now render the
  exact canonical Judgment and Priority Register headings, headers, separators, and rows consumed
  by production rather than relying on width-shaped Markdown fragments.
- 2026-08-15T12:53+02:00 — L3 targeted-gate repair: the atomic-series success fixture now proves
  explicit approved human review, preserving its intended all-prerequisites landing path.
- 2026-08-15T11:07+02:00 — L3 Dagger repair: made task rows canonical Markdown refs, stopped the
  negative grade fixture from healing its own corruption, restored exact tree-drift assertions,
  kept persistence-size forcing stable, and moved commit binding to the integration suite.
- 2026-08-15T10:24+02:00 — L3 file-size repair: moved the two small model/ownership checks into
  `test_closeout_queue_models.py`; the fixture and all queue behavior scenarios remain here.
- 2026-08-15T10:10+02:00 — L3 targeted-gate repair: imported the two split evidence modules
  directly and asserted their public owners are callable, allowing deterministic gate-scope
  derivation to select this existing behavior suite.
- 2026-08-15T09:53+02:00 — No content impact: L3's Pyright repair makes fixture model-validation
  boundaries and external-memory narrowing explicit; the queue scenarios, failure injection, and
  assertions are unchanged.
- 2026-08-15T09:10+02:00 — Created for L3's primary queue behavior and durability suite; verification remains closeout-owned.
