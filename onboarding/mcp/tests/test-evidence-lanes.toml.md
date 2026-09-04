# mcp/tests/test-evidence-lanes.toml

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test-evidence-lanes.toml` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T22:23+02:00 |
| lastVerifiedCommitHash | `e84c004c37a4bad082e1a7f1bdc4bd062282a185` |
| lastVerifiedCommitDate | 2026-09-04T22:06:05+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Canonical explicit classification manifest for Python test and shared-evidence lanes. It prevents unmarked, unknown, or conflicting files from silently inheriting a cheap/default class and gives selection, lifecycle, and cadence logic one reviewable declaration of test intent. CCR-R17 (260831-CCR-L17) registered the six fully standalone measured-replay suites in the `unit-regression` lane: `test_replay_fold_coverage.py`, `test_replay_freeze.py`, `test_replay_model_edges.py`, `test_replay_scenario_branches.py`, `test_replay_scenarios_and_compare.py`, and `test_replay_spans_and_measure.py`.

## Code Commentary

### Logic

The manifest maps repository-relative test paths into named evidence lanes and records lifecycle metadata for governed artifacts. The architecture-fitness array explicitly contains the M38-M45 doctrine tests and the MCP tool-signature policy suite, making their cost and evidence class deliberate rather than inferred from filename, location, or a pytest marker fallback.

The certification plan-authority, rail-registry, contract-model edge, reachability edge, and registry-validation edge suites are explicitly `unit-regression` because they exercise owned product behavior in-process. The readiness/telemetry/diagnostic/replay contract suites that followed enter the same lane under the same rule: in-process owned-product forcing stays deterministic unit-regression evidence. The L17 change added exactly six replay suites to that lane in rows 148-153.

The retry-selection hook, coverage-composition, and child-environment pure forcing suites are explicitly `unit-regression`; adding each file and its lane in one change prevents new proof from entering through a default classification. The renamed `test_kernel_pure_regressions.py` remains explicitly unit-regression evidence.

The future-code candidate mutation matrix and the exact code-memory candidate-pair suite are explicitly `integration` evidence: they create real temporary Git repositories and exercise process-backed or contract-owned admission boundaries. The ARSPAWN public-surface suite is explicitly `integration` evidence because it launches bounded stdio MCP subprocesses. The A004 repair classifies ambient reviewer dispatch, non-leaf reviewer retention, and quality publication security as `integration`, and the source-derived E2E selector closure proof as `architecture-fitness`. The direct-execution boundary regression module is explicitly `unit-regression`.

The final CCR-R01 candidate explicitly assigns nine focused modules to `unit-regression`: the six field-taxonomy, indexed-admission, semantic-topology, scaling, refusal, and projection-source-fact suites plus the three closeout-projection, semantic-topology, and task-document coverage-edge companions. The L21 gate-certificate suite enters the closed population exactly once as unit-regression evidence.

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
| Architecture-fitness membership explicitly includes the M38, M39, and M40-M45 structural proofs. | `mcp/tests/test_requirement_acceptance_envelope_doctrine.py`; `mcp/tests/test_requirement_attempt_journal_doctrine.py`; `mcp/tests/test_requirement_compilation_gate_doctrine.py` | mcp/tests/test-evidence-lanes.toml:525-527 |
| The structural test checks the complete M38 template surface. | `test_worker_role_brief_and_report_require_one_complete_primary_block`; `test_reviewer_role_and_verdict_require_independent_adjudication_per_id`; `test_manager_and_task_workflow_preserve_primary_ownership_and_adjacent_context` | mcp/tests/test_requirement_acceptance_envelope_doctrine.py:22-113 |
| Retry selection, child-environment forcing, and coverage composition have explicit unit-regression, integration, and architecture-fitness membership respectively. | `mcp/tests/test_retry_selection.py`; `mcp/tests/test_quality_subprocess_environment.py`; `mcp/tests/test_retry_coverage.py` | mcp/tests/test-evidence-lanes.toml:158-158; mcp/tests/test-evidence-lanes.toml:426-426; mcp/tests/test-evidence-lanes.toml:528-528 |
| The retained kernel regressions remain explicitly classified while deleted Candidate A tests are absent. | `mcp/tests/test_kernel_pure_regressions.py` | mcp/tests/test-evidence-lanes.toml:145-145 |
| The future-code candidate real-Git matrix is explicitly classified as integration evidence. | `mcp/tests/test_future_code_candidate.py` | mcp/tests/test-evidence-lanes.toml:302-302 |
| The exact code-memory pair suite is explicitly classified as integration evidence. | `mcp/tests/test_memory_candidate_pair.py` | mcp/tests/test-evidence-lanes.toml:384-384 |
| Every new ARSPAWN repair proof has one explicit semantic lane. | `mcp/tests/test_dispatch_agent_ambient_reviewer.py`; `mcp/tests/test_non_leaf_reviewer_evidence_retention.py`; `mcp/tests/test_quality_report_publication_security.py`; `mcp/tests/test_e2e_harness_selection.py` | mcp/tests/test-evidence-lanes.toml:300-300; mcp/tests/test-evidence-lanes.toml:395-395; mcp/tests/test-evidence-lanes.toml:425-425; mcp/tests/test-evidence-lanes.toml:514-514 |
| The direct-execution boundary regression remains explicitly unit-regression evidence. | `mcp/tests/test_integration_publication_fence.py` | mcp/tests/test-evidence-lanes.toml:97-97 |
| The nine CCR-R01 focused suites each have explicit unit-regression ownership. | `mcp/tests/test_closeout_projection_coverage_edges.py`; `mcp/tests/test_closeout_projection_source_facts.py`; `mcp/tests/test_execution_graph_indexed_admission.py`; `mcp/tests/test_semantic_topology_coverage_edges.py`; `mcp/tests/test_semantic_topology_field_matrix.py`; `mcp/tests/test_semantic_topology_refusals.py`; `mcp/tests/test_semantic_topology_scaling.py`; `mcp/tests/test_task_document_coverage_edges.py`; `mcp/tests/test_task_document_field_effects.py` | mcp/tests/test-evidence-lanes.toml:29-30; mcp/tests/test-evidence-lanes.toml:68-68; mcp/tests/test-evidence-lanes.toml:159-162; mcp/tests/test-evidence-lanes.toml:181-182 |
| The L21 gate-certificate suite enters the closed population exactly once as unit-regression. | `mcp/tests/test_gate_certificate_authority.py` | mcp/tests/test-evidence-lanes.toml:72-72 |
| The six CCR-R17 measured-replay suites are explicit unit-regression evidence. | `mcp/tests/test_replay_fold_coverage.py`; `mcp/tests/test_replay_freeze.py`; `mcp/tests/test_replay_model_edges.py`; `mcp/tests/test_replay_scenario_branches.py`; `mcp/tests/test_replay_scenarios_and_compare.py`; `mcp/tests/test_replay_spans_and_measure.py` | mcp/tests/test-evidence-lanes.toml:148-153 |

## Cross-Repo References

No cross-repository evidence is required.

| Finding | Anchor | Source |
| --- | --- | --- |
| Classification applies only to this repository's verification tree. | - | - |

## Update History

- 2026-09-04T22:23+02:00 - 260831-CCR-L17 Gate-5 memory pass: recorded the six CCR-R17 measured-replay suites (rows 148-153, `unit-regression`) and re-anchored the manifest citations shifted by the new rows plus prior registrations (doctrine 525-527, retry 158/426/528, kernel 145, future-code 302, pair 384, ARSPAWN 300/395/425/514, fence 97, CCR-R01 nine suites 29-30/68/159-162/181-182, gate-certificate 72). Verification stamp is the full leaf code commit `e84c004c37a4bad082e1a7f1bdc4bd062282a185`.

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
