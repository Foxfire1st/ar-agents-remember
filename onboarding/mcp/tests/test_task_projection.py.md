# mcp/tests/test_task_projection.py

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Focused behaviour cases for the task-context projection: **9 test functions (9 collected)**, all
unit, exercising the `application/task_projection/` package against a synthetic coordination tree.

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

The nine cases, and the property each owns:

| Case | Property |
| --- | --- |
| `test_two_leaves_project_their_own_scope_without_leaking_the_other` | Cross-task isolation: two leaves with different scope produce different projections and neither leaks the other's private content |
| `test_sprint_decision_history_reaches_orchestrator_but_never_a_leaf` | Altitude scope: a sprint's decision log is injected at orchestrator altitude and referenced-with-count, never injected, for a leaf |
| `test_each_frozen_operation_selects_its_own_channels_and_its_own_document` | Operation specificity: each frozen operation produces its own channel set and its own document |
| `test_every_unresolvable_input_returns_its_own_source_resolution_status` | Failure taxonomy: every unresolvable input returns its own status rather than one generic error |
| `test_a_refused_and_a_successful_projection_leave_the_task_tree_byte_identical` | Read-only reality: the task tree's bytes are unchanged after a success *and* after every refusal |
| `test_the_projection_modules_import_no_writer_transport_or_task_json_reader` | Structural: the package's import surface contains no writer, no transport and no task-JSON reader |
| `test_current_historical_and_proposal_facts_stay_distinguishable` | Three-plane separation: a historical record and a proposal never read as a current obligation |
| `test_every_owned_obligation_is_carried_verbatim_and_a_missing_section_is_a_gap` | No truncation: an obligation is carried verbatim, and a section the packet lacks is a reported gap |
| `test_the_provider_serves_the_compiler_protocol_and_the_knowledge_seam_is_optional` | The L2 seam: the provider satisfies the compiler protocol, a forged digest is refused there, and the knowledge channel is optional and reported when absent |

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

- **This module has no evidence-lane row, and that is an open defect, not a convention.** The
  fail-closed loader `load_lane_manifest` independently derives the expected test population from the
  tracked-and-untracked Python test modules under `pyproject.toml`'s `testpaths = ["mcp/tests"]` and
  **raises `LaneManifestError`** for any test file "without an explicit lane". This module is not
  listed in `mcp/tests/test-evidence-lanes.toml` (nor in `mcp/tests/evidence-lifecycle.toml`), so as
  the candidate stands the manifest does not load and every consumer of it — the
  `pytest_collection_modifyitems` hook that calls the loader, and `code_quality/check.py` — turns into
  a `UsageError`/finding. **The lane row is the owning seat's to add; onboarding does not write code
  and must not claim a registration that does not exist.** Three further modules carry the same gap
  from the two preceding leaves of this master (`test_role_capsule_compiler.py` and
  `test_role_capsule_admission.py` from `CAPS-R02@v1`, and `test_role_instruction_corpus.py` from
  `CAPS-R01@v1`), so a correct repair is a four-row manifest change rather than a one-row one.
  **Static finding, not executed**: it was derived from the loader's source, because this seat has
  Python 3.10 and the repository requires `>=3.13,<3.14`, so `import tomllib` fails and the loader
  could not be run here.
- **No case may compare the projection against itself.** The expected side comes from the fixture
  files on disk, a frozen vocabulary, or an independent parse — never from the projection's output.
- The import-surface case walks every module in the package, so a new module is covered
  automatically. Do not narrow it to a hand-written module list.
- `pyright` reports exactly one finding for this module, `Import "pytest" could not be resolved`,
  which is this repository's **pre-existing** condition for every pytest-importing test module
  (reproduced on the untouched `test_role_capsule_compiler.py`). It is not a defect introduced here
  and no `# type: ignore` was added to hide it.
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
- The fail-closed loader this module currently fails: it raises for any test file without an explicit lane. [11]
- The missing-lane finding that names exactly this module. [12]
- The lane manifest of record, which has no row for this module yet. A row belongs in the `unit-regression` list, whose alphabetical neighbours are `test_task_intent_identity.py` (`:111`) and `test_telemetry_store.py` (`:112`). [13]
- The `pytest` hook that runs the loader on every collection, so an unlisted module is a collection failure. [14]
- The population setting that makes every module under `mcp/tests/` part of the expected set. [15]

### Cross-Repo References

No sibling-repository contract is exercised by these cases.

No meaningful cross-repo references found.
