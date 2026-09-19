# mcp/tests/test_task_projection.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/tests/test_task_projection.py`        |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-16T10:30+02:00 |
| lastVerifiedCommitHash | `2dcacb27446ecbaba01b69ee32e2ac40a1713b09` |
| lastVerifiedCommitDate | 2026-09-18T17:26:34+02:00|
| governingOverview      | `overview.md`                              |

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

## Docs References

No external or domain documentation is configured for this memory root
(`system/sources.md` has no entries), so no external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant documentation found after checking the configured sources. | N/A | N/A |

## Repo-Internal References

The cases, the fixture value objects that vary one fact at a time, and the seam they prove.

| Finding | Anchor | Source |
| --- | --- | --- |
| The fixture world and the two spec value objects that keep a failure attributable. | `World`; `ContractSpec`; `BindingSpec` | mcp/tests/test_task_projection.py:303-472; mcp/tests/test_task_projection.py:225-232; mcp/tests/test_task_projection.py:290-300; mcp/tests/test_task_projection.py:255-263 |
| The generated enclosure contract, and the external-memory topology the fixture must reproduce. | `_contract` | mcp/tests/test_task_projection.py:235-286 |
| The two sibling leaves the isolation cases project against. | `ALPHA_SPEC`; `BETA_SPEC` | mcp/tests/test_task_projection.py:587-598 |
| The structural import-surface case: no writer, no transport, no task-JSON reader. | `test_the_projection_modules_import_no_writer_transport_or_task_json_reader`; `_WRITE_OR_TRANSPORT_MARKERS` | mcp/tests/test_task_projection.py:738-764; mcp/tests/test_task_projection.py:719-736; mcp/tests/test_task_projection.py:1118-1144 |
| The read-only case: the task tree is byte-identical after a success and after every refusal. | `test_a_refused_and_a_successful_projection_leave_the_task_tree_byte_identical` | mcp/tests/test_task_projection.py:1079-1096 |
| The altitude case: sprint history reaches an orchestrator but never a leaf. | `test_sprint_decision_history_reaches_orchestrator_but_never_a_leaf` | mcp/tests/test_task_projection.py:716-766 |
| The failure-taxonomy case: each unresolvable input has its own status. | `test_every_unresolvable_input_returns_its_own_source_resolution_status` | mcp/tests/test_task_projection.py:834-997 |
| The seam case: the provider satisfies the compiler protocol, and the knowledge channel is optional. | `test_the_provider_serves_the_compiler_protocol_and_the_knowledge_seam_is_optional`; `_RecordingExpansion` | mcp/tests/test_task_projection.py:853-897; mcp/tests/test_task_projection.py:838-850; mcp/tests/test_task_projection.py:1232-1287 |
| The package the cases exercise, whose read plan they pin. | `read_plan`; `read_documents` | mcp/src/agents_remember/application/task_projection/scope.py:420-435; mcp/src/agents_remember/application/task_projection/selection.py:175-197 |
| The compiler seam these cases verify through, including its digest refusal. | `compile_admitted_capsule` | mcp/src/agents_remember/application/role_capsules/compilation.py:89-120 |
| The fail-closed loader this module currently fails: it raises for any test file without an explicit lane. | `load_lane_manifest`; `LaneManifestError` | mcp/test_support/agents_remember_test_support/testing/lane_manifest.py:99-142; mcp/test_support/agents_remember_test_support/testing/lane_manifest.py:22-23 |
| The missing-lane finding that names exactly this module. | "test files without an explicit lane" | mcp/test_support/agents_remember_test_support/testing/lane_manifest.py:120-130 |
| The lane manifest of record, which has no row for this module yet. A row belongs in the `unit-regression` list, whose alphabetical neighbours are `test_task_intent_identity.py` (`:111`) and `test_telemetry_store.py` (`:112`). | "unit-regression" | mcp/tests/test-evidence-lanes.toml:5-5 |
| The `pytest` hook that runs the loader on every collection, so an unlisted module is a collection failure. | `pytest_collection_modifyitems` | mcp/test_support/agents_remember_test_support/testing/evidence_lanes.py:200-225 |
| The population setting that makes every module under `mcp/tests/` part of the expected set. | "testpaths" | pyproject.toml:250-250 |

## Cross-Repo References

No sibling-repository contract is exercised by these cases.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | N/A | N/A |

## Update History
- 2026-09-18T15:12:32+00:00: Generated citation repair: "testpaths" repointed to pyproject.toml:250-250. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "testpaths" repointed to pyproject.toml:220-220. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T01:52:52+00:00: Generated citation repair: "testpaths" repointed to pyproject.toml:181-181. No content impact: mechanical anchor-range projection bound to citation source snapshot 1b549a05c7448b2578454675e173eaf65501170ee85e72dbbfb2c4a4132b3242; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `ALPHA_SPEC`; `BETA_SPEC` repointed to mcp/tests/test_task_projection.py:587-592; mcp/tests/test_task_projection.py:593-598. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `test_a_refused_and_a_successful_projection_leave_the_task_tree_byte_identical` repointed to mcp/tests/test_task_projection.py:1079-1096. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `test_sprint_decision_history_reaches_orchestrator_but_never_a_leaf` repointed to mcp/tests/test_task_projection.py:716-766. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `test_every_unresolvable_input_returns_its_own_source_resolution_status` repointed to mcp/tests/test_task_projection.py:834-997. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `read_plan`; `read_documents` repointed to mcp/src/agents_remember/application/task_projection/selection.py:175-197; mcp/src/agents_remember/application/task_projection/scope.py:420-435. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: "testpaths" repointed to pyproject.toml:171-171. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-16T10:30+02:00 — 260915-CAPS-L3 curator: created this card for the focused test module
  added by the scoped-task-context leaf (`CAPS-R03@v1`). Records the nine cases and the property each
  owns, the anti-vacuity rule the module's docstring states as contract (the expected side never
  comes from the projection itself), the three fixture-topology traps that took the leaf three rounds
  to mirror (`CAPS-L3-EV5`–`EV7` — most importantly that an internal memory root silently wins over
  an external coordination hint), and the pre-existing `pytest`-unresolvable pyright condition. Also
  records that the leaf's mutation probe and live-evidence scripts are task-local and deliberately
  not promoted into `mcp/tests/`. **Records the evidence-lane blocker as an invariant**: this module
  is absent from `mcp/tests/test-evidence-lanes.toml`, and `load_lane_manifest` is fail-closed, so the
  manifest does not load as the candidate stands; the same gap exists for the three modules from
  `CAPS-R01@v1`/`CAPS-R02@v1`, so the correct repair is a four-row change owned by the owning seat,
  not by curation. That finding is static — derived from the loader's source — because this seat has
  Python 3.10 while the repository requires `>=3.13,<3.14`, so the loader could not be executed here.
  Verification metadata is left at the leaf base commit because the source is uncommitted — the
  governed closeout stamps the real code commit.
