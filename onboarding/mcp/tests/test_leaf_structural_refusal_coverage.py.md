# mcp/tests/test_leaf_structural_refusal_coverage.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_leaf_structural_refusal_coverage.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-31T14:06+02:00 |
| lastVerifiedCommitHash | `f2b7c648f540efb9d64ceea22e11e651cb5cc914`|
| lastVerifiedCommitDate | 2026-08-31T15:32:32+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Focused behavioral coverage for L19's fail-closed structural seams. The module forces ambiguity,
missing authority, invalid durable shape, broken containment, failed persistence, and dead/live
occupancy branches that broad happy-path suites do not naturally reach. It supports the targeted
coverage contract without changing production policy or introducing compatibility behavior.

## Code Commentary

### Logic

The first group proves durable migration is atomic/idempotent and structural seat resolution never
guesses through invalid role, missing binding, duplicate current occupants, or invalid parent/child
containment. The next group rejects ambiguous task-document values and undeclared terminal-catalog
shapes, then exercises structural dispatch/message/gate/terminal results across persistence and
adapter refusal states. The remaining tests cover ambiguous signal/inbox routing, curator-checklist
rendering failures, identity and terminal migrations, retire/manager authority, dead-occupant
reaping, topology enumeration/census, exact dispatch targeting, and conversation launch with or
without a plane-supplied structural role.

Dispatch cases whose subject is seat-taken, initial-brief rollback, or adapter delivery explicitly
stub `_implementation_series_admission_refusal` as successful. That keeps each focused case on its
named later seam while separate activation/admission suites own the source-pair gate itself; the
fixture does not create a bypass in production. The child-mutation cohort now calls the current
`parent_address` API and forces the typed retire-serialization refusal without reintroducing exact-id
addressing. Dead-owner reaping also proves a repeated live conflict remains owned after cleanup.
The terminal-opener refusal fixture supplies the complete current provenance shape, including both
nullable structural-parent fields, so it forces task-binding outcomes rather than failing on an
obsolete partial test double.
The signal-routing cohort also proves that a reviewer inbox row follows its durable manager-parent
stamp and that incomplete or invalid routing-layer parent tuples refuse. The manager/reviewer
cohort covers stamped and bounded legacy leaf ownership, while the reviewer seat resolver directly
forces missing, incomplete, and mismatched parent-address states.

### Conventions

Each test names the refusal it forces and imports the narrow production module inside the test.
Mocks supply boundary state; assertions remain on public result status, durable rewrite behavior,
or the exact production exception rather than on invented alternative implementations.

### Invariants And Boundaries

- Structural identity is a canonical task document plus role; session, lifecycle, and legacy leaf
  ids do not become public routing authority.
- Missing or ambiguous topology, occupancy, persistence, or ambient identity fails closed.
- Initial dispatch remains exact-target and persistence-first; a failed durable brief rolls back.
- Legacy migration is bounded to declared old durable shapes and does not create a public
  compatibility route.
- This module is coverage evidence, not proof that the complete targeted/full quality gate passed.
- A test focused after source-pair admission must neutralize that earlier seam explicitly instead
  of depending on unrelated repository fixtures or weakening production admission.

### Todos

None.

## Docs References

No external Domain Documentation source is configured; these are repository-owned contracts.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Durable migration and seat resolution reject invalid, ambiguous, and unowned state. | `test_durable_record_migration_is_atomic_and_idempotent`; `test_structural_seat_current_and_parent_resolution_fail_closed`; `test_structural_seat_child_authorization_fail_closed` | mcp/tests/test_leaf_structural_refusal_coverage.py:20-52; mcp/tests/test_leaf_structural_refusal_coverage.py:55-121; mcp/tests/test_leaf_structural_refusal_coverage.py:124-170 |
| Ambient identity, task-document values, and terminal-catalog disk shapes fail closed. | `test_ambient_seat_resolution_rejects_every_unproven_identity`; `test_task_document_ref_rejects_ambiguous_path_identity`; `test_terminal_catalog_disk_reader_refuses_undeclared_shapes` | mcp/tests/test_leaf_structural_refusal_coverage.py:173-225; mcp/tests/test_leaf_structural_refusal_coverage.py:228-235; mcp/tests/test_leaf_structural_refusal_coverage.py:238-267 |
| Structural dispatch and mutation tests preserve persistence-first and explicit refusal outcomes. | `test_dispatch_agent_refuses_invalid_spawn_and_unpersisted_brief`; `test_structural_agent_message_and_child_mutations_report_refusals`; `test_terminal_tool_task_document_and_open_refusals` | mcp/tests/test_leaf_structural_refusal_coverage.py:296-340; mcp/tests/test_leaf_structural_refusal_coverage.py:382-446; mcp/tests/test_leaf_structural_refusal_coverage.py:430-465 |
| Routing, authority, migration, topology, and launch edge cases preserve unique structural ownership. | `test_signal_routing_refuses_ambiguous_or_broken_task_containment`; `test_retire_policy_and_manager_lookup_refuse_broken_topology`; `test_task_topology_resolve_enumeration_and_id_ambiguity`; `test_dispatch_target_and_library_launch_without_structural_role` | mcp/tests/test_leaf_structural_refusal_coverage.py:497-583; mcp/tests/test_leaf_structural_refusal_coverage.py:679-720; mcp/tests/test_leaf_structural_refusal_coverage.py:951-986; mcp/tests/test_leaf_structural_refusal_coverage.py:1036-1075 |

## Cross-Repo References

No cross-repository implementation participates.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## L23 Refusal Translator Shape

Structural refusal coverage now exercises the extracted
`open_terminal_refusal` translator and treats task-binding refusal as a typed
result object. This keeps bad-kind/binding/seat behavior distinct from the new
lineage refusal evidence while covering the shared application boundary.

## PDLS Reconciliation

Structural refusal forcing now covers current shared configured-contract and lifecycle read failures without per-tool exception duplication.

The test continues to exercise production-owned behavior. No diagnostic result is treated as
certifying evidence and no fallback or threshold exception was introduced.

## 260821-ARSPAWN-L2 Commit-Aware Refusal Coverage

The structural refusal suite distinguishes an invalid or non-successful spawn result, whose
private generation and durable brief state are unknown, from a faithfully identified dispatch
generation that is positively proven unbriefed. Unknown, missing, contradictory, or unreadable
evidence must return a reconciliation refusal without retirement. Only the positive case may
enter the private recovery boundary and retire the exact server-derived generation.

Manager ambiguity expectations use the shared `current_seat_occupant` vocabulary for duplicate
primaries and duplicate staged replacements rather than maintaining another selector.

## Update History

- 2026-08-31T14:06+02:00 — A005 closeout size repair moved reviewer-row durable-parent rebinding
  and routing-layer incomplete/invalid parent forcing into this focused refusal suite, preserving
  the assertions while returning the broad inbox mechanics module below 1,200 lines.

- 2026-08-31T13:42+02:00 — A005 closeout repair completed changed-unit forcing for stamped and
  legacy reviewer manager lookup plus reviewer parent-address refusals.

- 2026-08-31T13:04+02:00 — ARSPAWN-L5 A005 closeout repair completed the opener provenance test
  double with the current structural-parent fields; the existing test again reaches its intended
  task-binding refusal assertions. Verification remains closeout-owned.

- 2026-08-31T09:02+02:00 — 260821-ARSPAWN-L5 A005 citation reconciliation refreshed
  source ranges after the reviewed refusal suite moved; no semantic onboarding claim changed.
  Verification remains closeout-owned.

- 2026-08-26T16:03+02:00 — Post-failure repair: aligned the structural mutation fixture with
  `parent_address`, added typed retire-lock refusal coverage, and forced repeated conflict-owner
  cleanup. No certifying test execution is claimed.


- 2026-08-26T12:30+02:00 — Reconciled ARSPAWN-L2 unknown-state refusal and positive unbriefed-generation
  recovery forcing onto the IAS test card. No certifying test execution is claimed.

- 2026-08-26T08:15+02:00 — Reconciled three focused dispatch fixtures with the new source-pair
  admission predecessor by stubbing it successful before forcing their existing spawn/delivery
  branches. Production admission remains covered separately; verification is closeout-owned.

- 2026-08-25T15:44+02:00 — PDLS whole-system reconciliation updated the implementation summary
  above after source and requirement review. Verification remains closeout-owned.
- 2026-08-12T20:10+02:00 — L23 curator: reconciled extracted refusal translation and typed opener results; verification remains closeout-owned.

- 2026-08-11T22:28+02:00 — 260731-EFA-L19 curator: created one-to-one onboarding for the focused
  structural refusal coverage module. Verification metadata is intentionally blank until governed
  closeout can stamp the real code commit.
