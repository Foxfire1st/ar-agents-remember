# mcp/tests/test_task_execution_topology.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_task_execution_topology.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T21:45:53+00:00 |
| lastVerifiedCommitHash | `d36109038b3f2b500c138f9dc1ea9c9f9a247489` |
| lastVerifiedCommitDate | 2026-09-06T22:21:49+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

Provides shared topology fixtures only: canonical repository/task references, a minimal runtime configuration and a typed master-document constructor. No test functions remain in this module. The former full topology/publication/observer assertions are historical; retained segment suites consume these helpers without turning helper imports into executed protection.

## Code Commentary

### Logic

The current evidence boundary is the source-listed behavior below. Earlier coverage claims in
history describe prior populations and must not be used to recreate removed tests or claim they
still run. The retained behavior and its fixture limits, described above, govern this card.

### Conventions

The test-shaped filename is retained for imports by other suites. Helper availability is not
a passing test, and the module has no collected test definitions of its own.

### Invariants And Boundaries

Preserve exact refusal, identity, and cleanup assertions rather than adding overlapping helper
cases. Coverage percentages are diagnostic and production CRAP 20 prompts review; neither implies
an obligation to restore removed cases. Full suites and whole-candidate review remain master-end
work. This source inspection does not claim a newly executed test or acceptance result.

### Todos

No additional implementation scope is opened by this memory reconciliation.

## Docs References

The repository has no configured Domain Documentation source. These claims concern its own test
fixtures and assertions, so the exact retained source is the direct evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain claim is required. | N/A | N/A |

## Repo-Internal References

Each current definition below can be inspected in the exact source file. Historical references
to removed methods are superseded by this current inventory.

| Finding | Anchor | Source |
| --- | --- | --- |
| Shared helper _config | `_config` | mcp/tests/test_task_execution_topology.py:20-28 |
| Shared helper _master | `_master` | mcp/tests/test_task_execution_topology.py:31-52 |

## Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external evidence is needed for these assertions. | N/A | N/A |

## Update History

- 2026-09-06T21:45:53+00:00 — Reconciled the retained IAS test/helper population and exact citation ranges, preserving prior history and verification provenance; no tests or review were run.


- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for
  3e276f2b2052b641afbee180a472259f21b500df (CCR-R04@v1/L04): recorded the L04 case rename and
  expectation change — `test_unchanged_documents_have_no_scope_despite_unrelated_malformed_task`
  now asserts an empty projection scope because unchanged documents carry no classifier
  invalidation. Verification is pinned to the owning commit.

- 2026-08-24T13:43+02:00 — 260821-DAGQC-L1: reconciled master-facing wave assertions to explicit
  `node.ref` projection after structural node-only equality; this is a mechanical consumer change,
  not a topology-behavior expansion. Verification metadata remains pinned until architect-owned
  closeout stamps the real code commit.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this test card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.

- 2026-08-20T09:35+02:00 — 260815-DAG-L16: signature-compat update (`task_doc_tool` takes
  `call: TaskDocCall`); suite purpose unchanged. Verified at code commit a9d50e08.

- 2026-08-19T22:32+02:00 — 260815-DAG-L13: the finite migration operation is removed; the former
  migration cases are now graph-bootstrap forcing through `author_execution_graph`
  (`test_bootstrap_*`), including the cross-root rollback proof. Verification remains
  closeout-owned.

- 2026-08-19T08:55+02:00 — 260815-DAG-L11: the L11 segment/authoring cases moved out to
  `test_task_execution_topology_segments.py` and `test_author_execution_graph.py` under the
  file-size rail (fixtures and helpers are imported from this suite); this file keeps the schema,
  migration, inventory, and rollback forcing classes. Verification remains closeout-owned.
- 2026-08-18T12:00:00+00:00 — 260815-DAG-L9: added three `inventory_execution_topology` forcing cases
  (branch-backed atomic, empty tree, branch-enumeration refusal); verification remains
  closeout-owned.
- 2026-08-16T04:06+02:00 — Dagger fixture repair: topology downgrade explicitly clears the sprint integration branch together with orchestration and graph facts.
- 2026-08-15T23:38+02:00 — Reconciled the suite's L4 fixture and forcing role for protected integration branches, durable operation authority, external-memory parity, and recovery. Verification metadata remains closeout-owned.

- 2026-08-15T14:05+02:00 — L3 final targeted-gate repair: directly forces queue-scope and
  completion-topology error translation plus task-document publisher refusal without bypassing
  the canonical topology owners.
- 2026-08-15T13:18+02:00 — No content impact: repository Ruff formatting changed only layout;
  topology, queue-scope ownership, rollback, and persistent-lock assertions are identical.
- 2026-08-15T13:08+02:00 — No content impact: accepted Ruff's module/name ordering for the direct
  queue-scope and task-publication imports; ownership and rollback assertions are unchanged.
- 2026-08-15T11:39+02:00 — No content impact: rewrote the direct queue-scope module import to
  Ruff's package-import form; the imported module identity and ownership assertion are unchanged.
- 2026-08-15T11:25+02:00 — L3 static-gate repair: directly bound the extracted queue-scope owner
  to the topology suite; all existing behavioral assertions remain in place.
- 2026-08-15T11:07+02:00 — L3 content update: rollback assertions now distinguish canonical task
  document publication from the persistent coordination lock and separately prove no queue state
  or pending WAL survives a failed graph migration.
- 2026-08-15T03:20:17+02:00 — 260815-DAG-L1 independent-review repair: corrected the
  out-of-repository no-write assertion to the real task-doc filenames and added a poisoned
  second-read regression that distinguishes snapshot-safe wave derivation from the former
  validate-one/read-another sequence.
- 2026-08-15T03:10:06+02:00 — 260815-DAG-L1 targeted-Dagger repair: added production-bound
  refusal cells for every branch reported uncovered by the first targeted artifact and a diamond
  graph that releases its successor only after both predecessors complete. These tests preserve
  the closed contract rather than adding coverage exclusions.
- 2026-08-15T02:42:41+02:00 — 260815-DAG-L1 review repair: expanded forcing proof through
  production task-doc create/replace/set-field paths, alias drift/collision refusals, structured
  preview classifications, same-path master/sprint kind-downgrade refusals, exact
  render/projection cells, and normalized out-of-root refusal.
- 2026-08-15T02:16:50+02:00 — 260815-DAG-L1: created as the forcing suite for the new persisted
  topology and finite migration boundary. Verification remains closeout-owned.
