# mcp/tests/test_task_projection.py

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Focused behaviour cases for the task-context projection against a synthetic coordination tree.
The current source defines 11 test functions: the retained isolation, altitude, operation, refusal,
read-only, import-boundary and compiler/optional-knowledge cases, plus a thin launcher-plan case,
branch/admitted-revision refusals and invalidation after a real task-document revision change.
`test_the_projected_planes_keep_their_kinds_and_carry_every_obligation_verbatim` now combines the
earlier separate fact-plane and verbatim-obligation cases. This describes source definitions and
assertions, not a newly collected or executed test count.

> Historical inventory, superseded by the current source account above:
> Focused behaviour cases for the task-context projection: **9 test functions (9 collected)**, all
> unit, exercising the `application/task_projection/` package against a synthetic coordination tree.

## Code Commentary

### Logic

The module's docstring states the anti-vacuity rule the whole file obeys: **every case derives its
expected side from a source the projection does not feed** — the fixture files written to disk, the
task layer's own frozen vocabularies, or an independently parsed copy of the projection's output. A
comparison whose two sides both came from the projection would be vacuous, and this repository's
reviews have rejected that class twice.

The fixture is a `World`: one synthetic coordination root with an external memory repo (the topology
the real enclosure uses), a code checkout, a memory worktree, a sprint/master/leaf document set, two
leafless-packet requirement documents and generated enclosure contracts. `ContractSpec` and
`BindingSpec` are the two value objects that vary one fact at a time, which is what keeps a case's
failure attributable. `ALPHA_SPEC`/`BETA_SPEC` are the two sibling leaves the isolation cases project
against.

Current source-defined cases and their assertion boundaries (11 definitions; no new collection or execution is claimed):

| Case | Property |
| --- | --- |
| `test_two_leaves_project_their_own_scope_without_leaking_the_other` | Sibling leaves project their own scope without private-content leakage |
| `test_sprint_decision_history_reaches_orchestrator_but_never_a_leaf` | Sprint history is injected at orchestrator altitude and referenced rather than injected for a leaf |
| `test_each_frozen_operation_selects_its_own_channels_and_its_own_document` | Each declared operation selects its own channels and document |
| `test_the_launcher_seat_plan_is_thin_for_every_altitude_and_parent` | A launcher receives objective/scope at its own altitude, without role-operation channels or portfolio facts |
| `test_every_unresolvable_input_returns_its_own_source_resolution_status` | Unresolvable inputs retain their own named refusal statuses |
| `test_the_provider_refuses_a_branch_or_a_revision_its_scope_did_not_bind` | Wrong branch and wrong admitted task revision refuse distinctly; the matching binding remains usable |
| `test_a_changed_task_revision_invalidates_the_previously_selected_projection` | New resolution rejects an old binding after a task edit; re-admission projects the new revision, and an already resolved scope retains its read revision |
| `test_a_refused_and_a_successful_projection_leave_the_task_tree_byte_identical` | Success and every refusal leave the task tree byte-identical |
| `test_the_projection_modules_import_no_writer_transport_or_task_json_reader` | The package import surface contains no writer, transport or task-JSON reader |
| `test_the_projected_planes_keep_their_kinds_and_carry_every_obligation_verbatim` | One combined case distinguishes current/historical/proposal kinds, preserves obligations verbatim and reports a missing required section |
| `test_the_provider_serves_the_compiler_protocol_and_the_knowledge_seam_is_optional` | The provider satisfies the compiler seam, a forged digest refuses, and an absent optional knowledge channel is reported |

Historical nine-case inventory, superseded by the current source-defined inventory above:

> The nine cases, and the property each owns:
>
> | Case | Property |
> | --- | --- |
> | `test_two_leaves_project_their_own_scope_without_leaking_the_other` | Cross-task isolation: two leaves with different scope produce different projections and neither leaks the other's private content |
> | `test_sprint_decision_history_reaches_orchestrator_but_never_a_leaf` | Altitude scope: a sprint's decision log is injected at orchestrator altitude and referenced-with-count, never injected, for a leaf |
> | `test_each_frozen_operation_selects_its_own_channels_and_its_own_document` | Operation specificity: each frozen operation produces its own channel set and its own document |
> | `test_every_unresolvable_input_returns_its_own_source_resolution_status` | Failure taxonomy: every unresolvable input returns its own status rather than one generic error |
> | `test_a_refused_and_a_successful_projection_leave_the_task_tree_byte_identical` | Read-only reality: the task tree's bytes are unchanged after a success *and* after every refusal |
> | `test_the_projection_modules_import_no_writer_transport_or_task_json_reader` | Structural: the package's import surface contains no writer, no transport and no task-JSON reader |
> | `test_current_historical_and_proposal_facts_stay_distinguishable` | Three-plane separation: a historical record and a proposal never read as a current obligation |
> | `test_every_owned_obligation_is_carried_verbatim_and_a_missing_section_is_a_gap` | No truncation: an obligation is carried verbatim, and a section the packet lacks is a reported gap |
> | `test_the_provider_serves_the_compiler_protocol_and_the_knowledge_seam_is_optional` | The L2 seam: the provider satisfies the compiler protocol, a forged digest is refused there, and the knowledge channel is optional and reported when absent |

Two cases carry more weight than their size suggests. The **import-surface case** parses each
module's AST and asserts no writer, transport or task-JSON import appears — that is what makes "read
task truth through the owners" and "the projection is read-only" checkable properties rather than
claims. The **byte-identical case** digests the whole task tree before and after both a successful
projection and every refusal, which is the observable consequence of the read-only contract.

### Fixture conventions

The synthetic tree must mirror the real enclosure's topology. Three rounds were needed to get there
(`CAPS-L3-EV5`–`EV7`): a leaf enclosure needs `kind: leaf` **with** a `leaf_id`, an external-memory
contract needs its ledger leg, and — the subtle one — **an internal memory root silently wins over
an external coordination hint**, so a fixture with an internal memory root searched the task tree in
the wrong place. A new fixture that does not reproduce the external topology will test the wrong
resolution path.

### Invariants And Boundaries

- **This module has its evidence-lane row.** `mcp/tests/test_task_projection.py` is listed in the `unit-regression` lane of `mcp/tests/test-evidence-lanes.toml` (current row `:423`). The fail-closed loader `load_lane_manifest` derives the expected test population from the Python test modules under `testpaths = ["mcp/tests"]` and raises `LaneManifestError` for any test file without an explicit lane; the `pytest_collection_modifyitems` hook calls it on every collection.
- **No case may compare the projection against itself.** The expected side comes from the fixture
  files on disk, a frozen vocabulary, or an independent parse — never from the projection's output.
- The import-surface case walks every module in the package, so a new module is covered
  automatically. Do not narrow it to a hand-written module list.
- This module is a **shipped repository test**, not a task-local fixture. The leaf's mutation probe
  and live-evidence scripts are deliberately *not* promoted here; they are task-local artifacts in
  the coordination tree.

### Todos

None recorded.

## Evidence

### Docs References

No external or domain documentation is configured for this memory root
(`system/sources.md` has no entries), so no external documentation claim is made.

No relevant documentation found after checking the configured sources.

### Repo-Internal References

The cases, the fixture value objects that vary one fact at a time, and the seam they prove.



> Retained earlier citation wording: - The lane manifest registers mcp/tests/test_task_projection.py in unit-regression. Membership selects evidence and does not establish execution.


- The fixture world and the two spec value objects that keep a failure attributable. [1]
- The generated enclosure contract, and the external-memory topology the fixture must reproduce. [2]
- The two sibling leaves the isolation cases project against. [3]
- The structural import-surface case: no writer, no transport, no task-JSON reader. [4]
- The read-only case: the task tree is byte-identical after a success and after every refusal. [5]
- The altitude case: sprint history reaches an orchestrator but never a leaf. [6]
- The failure-taxonomy case: each unresolvable input has its own status. [7]
- The seam case: the provider satisfies the compiler protocol, and the knowledge channel is optional. [8]
- The package the cases exercise, whose read plan they pin. [9]
- The compiler seam these cases verify through, including its digest refusal. [10]

- The fail-closed loader: it raises for any test file without an explicit lane. [16]
- The error type the loader raises. [17]
- The missing-lane finding. [18]


> Retained earlier citation wording: - The lane manifest of record; this module's row stands in the `unit-regression` list.


- The `pytest` hook that runs the loader on every collection, so an unlisted module is a collection failure. [19]





### Cross-Repo References

No sibling-repository contract is exercised by these cases.

No meaningful cross-repo references found.






- The population setting includes modules below mcp/tests. The retained historical collection comment names its default-unit-lane collection method. [15]

- The retained lane entries name three neighbouring test modules. The added test_task_projection.py row establishes this module's own unit-regression membership. [13]


- The retained stored-operation-record row is separate from the added test_task_projection.py membership row. Catalog membership selects evidence and does not establish execution. [21]
