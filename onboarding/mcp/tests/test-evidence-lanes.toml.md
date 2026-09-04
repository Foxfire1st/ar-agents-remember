# mcp/tests/test-evidence-lanes.toml

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test-evidence-lanes.toml` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T22:45+02:00 |
| lastVerifiedCommitHash | `54ff803a05209e06f732f2de1f90e2a71a069e08` |
| lastVerifiedCommitDate | 2026-09-04T22:31:30+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Canonical explicit classification manifest for Python test and shared-evidence lanes. It prevents unmarked, unknown, or conflicting files from silently inheriting a cheap/default class and gives selection, lifecycle, and cadence logic one reviewable declaration of test intent. CCR-R14@v3 (260831-CCR-L14) registered the seven standalone final-codex suites: the five contract suites (test_final_codex_certificate/models/planning/projection/store) in the `unit-regression` lane and the two run-control/coverage suites (test_final_codex_executor/test_final_codex_diff_coverage) in the `integration` lane.

## Code Commentary

### Logic

The manifest maps repository-relative test paths into named evidence lanes and records lifecycle metadata for governed artifacts. The architecture-fitness array explicitly contains the M38-M45 doctrine tests and the MCP tool-signature policy suite, making their cost and evidence class deliberate rather than inferred from filename, location, or a pytest marker fallback.

The five certification plan-authority, rail-registry, contract-model edge, reachability edge, and registry-validation edge suites are explicitly `unit-regression` because they exercise owned product behavior in-process; the readiness/telemetry/diagnostic contract suites that followed enter the same lane under the same rule. CCR-R14@v3 added the five final-codex contract suites to that lane in rows 64-68 and the final-codex executor and diff-coverage closure suites to the `integration` lane in rows 291-292: the contract suites exercise the owned two-fresh model/projection/planning/certificate contracts in-process, while the executor and diff-coverage suites share the R12 authority boundary and python-diff-coverage tooling.

The retry-selection hook, coverage-composition, and child-environment pure forcing suites are explicitly `unit-regression`; adding each file and its lane in one change prevents new proof from entering through a default classification. The future-code candidate mutation matrix is explicitly `integration` evidence because it creates real temporary Git repositories and exercises process-backed operations; the exact code-memory candidate-pair suite is also `integration` because it creates real temporary repositories and linked worktrees and exercises the contract-owned memory-quality admission boundary. The ARSPAWN public-surface suite is explicitly `integration` evidence because it launches bounded stdio MCP subprocesses. The direct-execution boundary regression module is explicitly `unit-regression`.

The final CCR-R01 candidate explicitly assigns nine focused modules to `unit-regression`: the six field-taxonomy, indexed-admission, semantic-topology, scaling, refusal, and projection-source-fact suites plus the three closeout-projection, semantic-topology, and task-document coverage-edge companions. L21 added the gate-certificate authority forcing suite to `unit-regression` in the same change that created it.

### Conventions

- Every classified test path is explicit and repository-relative.
- New test modules enter a named lane in the same change that creates them.
- Lane identity and pytest execution markers are separate namespaces and must not silently collide.

### Invariants And Boundaries

- Unknown or multiply classified tests fail closed in the manifest validator.
- The manifest describes test/verification infrastructure; it does not grant operational product authority to Dagger or pytest helpers.
- This file classifies evidence. It does not replace the per-requirement worker/reviewer envelope.

## Docs References

No external documentation governs this repository-owned evidence catalog.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | - | - |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| All five certification contract suites have explicit unit-regression ownership. | `mcp/tests/test_certification_contract_model_edges.py`; `mcp/tests/test_certification_plan_authority.py`; `mcp/tests/test_certification_rail_registry.py`; `mcp/tests/test_certification_reachability_edges.py`; `mcp/tests/test_certification_registry_validation_edges.py` | mcp/tests/test-evidence-lanes.toml:17-21 |
| Architecture-fitness membership explicitly includes the M38, M39, and M40-M45 structural proofs. | `mcp/tests/test_requirement_acceptance_envelope_doctrine.py`; `mcp/tests/test_requirement_attempt_journal_doctrine.py`; `mcp/tests/test_requirement_compilation_gate_doctrine.py` | mcp/tests/test-evidence-lanes.toml:526-528 |
| The structural test checks the complete M38 template surface. | `test_worker_role_brief_and_report_require_one_complete_primary_block`; `test_reviewer_role_and_verdict_require_independent_adjudication_per_id`; `test_manager_and_task_workflow_preserve_primary_ownership_and_adjacent_context` | mcp/tests/test_requirement_acceptance_envelope_doctrine.py:22-113 |
| Retry selection, child-environment forcing, and coverage composition have explicit unit-regression, integration, and architecture-fitness membership respectively. | `mcp/tests/test_retry_selection.py`; `mcp/tests/test_quality_subprocess_environment.py`; `mcp/tests/test_retry_coverage.py` | mcp/tests/test-evidence-lanes.toml:157-157; mcp/tests/test-evidence-lanes.toml:427-427; mcp/tests/test-evidence-lanes.toml:529-529 |
| The retained kernel regressions remain explicitly classified while deleted Candidate A tests are absent. | `mcp/tests/test_kernel_pure_regressions.py` | mcp/tests/test-evidence-lanes.toml:150-150 |
| The future-code candidate real-Git matrix is explicitly classified as integration evidence. | `mcp/tests/test_future_code_candidate.py` | mcp/tests/test-evidence-lanes.toml:303-303 |
| The exact code-memory pair suite is explicitly classified as integration evidence. | `mcp/tests/test_memory_candidate_pair.py` | mcp/tests/test-evidence-lanes.toml:385-385 |
| Every new ARSPAWN repair proof has one explicit semantic lane. | `mcp/tests/test_dispatch_agent_ambient_reviewer.py`; `mcp/tests/test_non_leaf_reviewer_evidence_retention.py`; `mcp/tests/test_quality_report_publication_security.py`; `mcp/tests/test_e2e_harness_selection.py` | mcp/tests/test-evidence-lanes.toml:301-301; mcp/tests/test-evidence-lanes.toml:396-396; mcp/tests/test-evidence-lanes.toml:426-426; mcp/tests/test-evidence-lanes.toml:515-515 |
| The direct-execution boundary regression remains explicitly unit-regression evidence. | `mcp/tests/test_integration_publication_fence.py` | mcp/tests/test-evidence-lanes.toml:102-102 |
| The nine CCR-R01 focused suites each have explicit unit-regression ownership. | `mcp/tests/test_closeout_projection_coverage_edges.py`; `mcp/tests/test_closeout_projection_source_facts.py`; `mcp/tests/test_execution_graph_indexed_admission.py`; `mcp/tests/test_semantic_topology_coverage_edges.py`; `mcp/tests/test_semantic_topology_field_matrix.py`; `mcp/tests/test_semantic_topology_refusals.py`; `mcp/tests/test_semantic_topology_scaling.py`; `mcp/tests/test_task_document_coverage_edges.py`; `mcp/tests/test_task_document_field_effects.py` | mcp/tests/test-evidence-lanes.toml:29-30; mcp/tests/test-evidence-lanes.toml:73-73; mcp/tests/test-evidence-lanes.toml:158-161; mcp/tests/test-evidence-lanes.toml:180-181 |
| The L21 gate-certificate suite enters the closed population exactly once as unit-regression. | `mcp/tests/test_gate_certificate_authority.py` | mcp/tests/test-evidence-lanes.toml:77-77 |
| The five standalone CCR-R14 final-codex contract suites are explicit unit-regression evidence. | `mcp/tests/test_final_codex_certificate.py`; `mcp/tests/test_final_codex_models.py`; `mcp/tests/test_final_codex_planning.py`; `mcp/tests/test_final_codex_projection.py`; `mcp/tests/test_final_codex_store.py` | mcp/tests/test-evidence-lanes.toml:64-68 |
| The CCR-R14 final-codex executor and diff-coverage closure suites are explicit integration evidence. | `mcp/tests/test_final_codex_executor.py`; `mcp/tests/test_final_codex_diff_coverage.py` | mcp/tests/test-evidence-lanes.toml:291-292 |

## Cross-Repo References

No cross-repository evidence is required.

| Finding | Anchor | Source |
| --- | --- | --- |
| Classification applies only to this repository's verification tree. | - | - |

## MCAR-L02 Coherence Evidence Lane

The manifest classifies `test_curator_coherence.py` explicitly as integration evidence alongside the existing future-code real-Git suite. This prevents the Dagger selector from silently treating the new filesystem/Git/task publication fixture as unit evidence.

## Update History

- 2026-09-04T22:45+02:00 - 260831-CCR-L14 Gate-5 memory pass: recorded the five CCR-R14 final-codex contract suites (rows 64-68, `unit-regression`) and the executor plus diff-coverage closure suites (rows 291-292, `integration`) and re-anchored the manifest citations shifted by the new rows (fence 102, gate-certificate 77, doctrine 526-528, retry 157/427/529, kernel 150, future-code 303, pair 385, ARSPAWN 301/396/426/515, CCR-R01 nine suites 29-30/73/158-161/180-181). Verification stamp is the full leaf code commit `54ff803a05209e06f732f2de1f90e2a71a069e08`.

- 2026-09-03T13:30+02:00 - 260831-CCR-L27 Gate-5 memory pass: re-anchored all 21 manifest lane citations to the exact current line numbers after the L21 gate-certificate registration and prior registrations shifted rows (doctrine 497-499, retry 147/400/500, kernel 140, future-code 281, pair 363, ARSPAWN 279/369/399/486, fence 92, CCR-R01 nine suites 29-30/64/148-151/170-171). Verification remains pinned to the pre-commit source history until closeout.

- 2026-09-03T12:30+02:00 - 260831-CCR memory curation pass for 6f10c24d72db6171c0d434b307e6806996e2f11d (CCR-R21@v2/L21): recorded the L21 lane registration of `mcp/tests/test_gate_certificate_authority.py` as explicit `unit-regression` evidence so the new forcing suite enters the closed population exactly once. Verification is pinned to the owning commit.

- 2026-09-01T11:33+02:00 - CCR-L11 Attempt 10 added explicit `unit-regression` ownership for the three focused certification edge suites and re-anchored every manifest citation shifted by those rows. Verification remains closeout-owned.

- 2026-09-01T08:13+02:00 - Final CCR-R01 reconciliation: expanded the current lane account from six to all nine focused unit-regression suites, including the three coverage-edge companions, and regenerated every manifest citation shifted by their rows. The manifest supplies selection and cost classification only; verification remains closeout-owned.

- 2026-09-01T05:22+02:00 - 260831-CCR-L01 Attempt 9: added explicit `unit-regression` ownership for the six focused CCR-R01 suites and re-anchored every manifest citation shifted by those rows. The lane declaration governs selection/cost only; accepted task evidence remains reviewer-owned. Verification remains closeout-owned.

- 2026-09-01T04:34+02:00 - Added explicit `unit-regression` ownership for the two certification contract suites and repaired every manifest citation shifted by those rows. The manifest remains fail-closed; no default, fallback, or alternate classification authority was introduced.

- 2026-08-31T20:30+02:00 - 260831-DER: explicitly classified `mcp/tests/test_integration_publication_fence.py` in the `unit-regression` lane.

- 2026-08-31T08:05+02:00 - Classified the four A003-unregistered ARSPAWN proof modules exactly once: three integration routes and one architecture-fitness selector-closure route.

- 2026-08-30T15:15:36+02:00 - Classified `test_public_surface_conformance.py` explicitly as integration evidence. Verification remains closeout-owned.

- 2026-08-30T04:54+02:00 - Added explicit integration-lane ownership for the exact code-memory candidate-pair suite after the lifecycle Dagger census rejected an unclassified test file. No product or requirement semantics changed.

- 2026-08-29T08:52+02:00 - Added explicit integration classification for the structured curator-coherence forcing suite. Verification remains closeout-owned.

- 2026-08-29T07:35+02:00 - Added explicit integration-lane ownership for the future-code candidate real-Git matrix and repaired exact manifest citations shifted by that row.

- 2026-08-28T14:18+02:00 - Reconciled manifest citations against the committed PDLS candidate; the explicit-lane contract is unchanged.

- 2026-08-28T05:10+02:00 - Removed the two stale Candidate A test rows and retained the renamed kernel regression module in its explicit unit lane after Q5 v19 forced the stale-row refusal.

- 2026-08-27T18:33+02:00 - Recorded explicit unit-regression membership for the retry coverage composition and quality child-environment suites.

- 2026-08-27T18:06+02:00 - Added explicit architecture-fitness membership for the M40-M45 Requirement Attempt Journal structural proof.

- 2026-08-27T17:19+02:00 - Added explicit unit-regression membership for the retry-selection forcing suite in the same change that introduced it.

- 2026-08-27T13:32+02:00 - Added explicit architecture-fitness membership for M39 compilation doctrine and the split tool-signature exemption suite. Verification remains closeout-owned.

- 2026-08-27T12:43+02:00 - M38: created the manifest sidecar and recorded explicit registration of the acceptance-envelope structural test. Verification metadata remains empty until governed closeout stamps the PDLS code commit.
