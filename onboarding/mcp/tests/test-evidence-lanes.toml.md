# mcp/tests/test-evidence-lanes.toml

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test-evidence-lanes.toml` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-31T08:05+02:00 |
| lastVerifiedCommitHash | `f2b7c648f540efb9d64ceea22e11e651cb5cc914`|
| lastVerifiedCommitDate | 2026-08-31T15:32:32+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Canonical explicit classification manifest for Python test and shared-evidence lanes. It prevents
unmarked, unknown, or conflicting files from silently inheriting a cheap/default class and gives
selection, lifecycle, and cadence logic one reviewable declaration of test intent.

## Code Commentary

### Logic

The manifest maps repository-relative test paths into named evidence lanes and records lifecycle
metadata for governed artifacts. The architecture-fitness array explicitly contains the M38-M45
doctrine tests and the MCP tool-signature policy suite, making their cost and evidence class
deliberate rather than inferred from filename, location, or a pytest marker fallback.
The retry-selection hook, coverage-composition, and child-environment pure forcing suites are
explicitly `unit-regression`; adding each file and its lane in one change prevents new proof from
entering through a default classification. Candidate A's two deleted runner/eligibility suites were
removed from the manifest in the same change that removed their files; the renamed
`test_kernel_pure_regressions.py` remains explicitly unit-regression evidence.
The future-code candidate mutation matrix is explicitly `integration` evidence because it creates
real temporary Git repositories and exercises add-all candidate identity across process-backed Git
operations; this row was added in the same correction that closed the Dagger lane-census failure.
The exact code-memory candidate-pair suite is also explicitly `integration` evidence: its tests
create real temporary repositories and linked worktrees, advance source branches, and exercise the
contract-owned memory-quality admission boundary. The lifecycle gate rejects the candidate if this
row is absent instead of silently assigning a cheaper lane.
The ARSPAWN public-surface suite is explicitly `integration` evidence because it launches bounded
stdio MCP subprocesses and performs real protocol initialization, tool listing, and calls for all
eight controlled harness registrations. It must never silently inherit a unit lane.
The A004 repair also classifies ambient reviewer dispatch, non-leaf reviewer retention, and quality
publication security as `integration`, while the source-derived E2E selector closure proof is
`architecture-fitness`. The four modules therefore enter the closed test population exactly once;
none receives an inferred or compatibility lane.

### Conventions

- Every classified test path is explicit and repository-relative.
- New test modules enter a named lane in the same change that creates them.
- Lane identity and pytest execution markers are separate namespaces and must not silently collide.

### Invariants And Boundaries

- Unknown or multiply classified tests fail closed in the manifest validator.
- The manifest describes test/verification infrastructure; it does not grant operational product
  authority to Dagger or pytest helpers.
- This file classifies evidence. It does not replace the per-requirement worker/reviewer envelope.

## Docs References

No external documentation governs this repository-owned evidence catalog.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Architecture-fitness membership explicitly includes the M38, M39, and M40-M45 structural proofs. | "mcp/tests/test_requirement_acceptance_envelope_doctrine.py"; "mcp/tests/test_requirement_attempt_journal_doctrine.py"; "mcp/tests/test_requirement_compilation_gate_doctrine.py" | mcp/tests/test-evidence-lanes.toml:468-470 |
| The structural test checks the complete M38 template surface. | `test_worker_role_brief_and_report_require_one_complete_primary_block`; `test_reviewer_role_and_verdict_require_independent_adjudication_per_id`; `test_manager_and_task_workflow_preserve_primary_ownership_and_adjacent_context` | mcp/tests/test_requirement_acceptance_envelope_doctrine.py:22-113 |
| Retry selection, child-environment forcing, and coverage composition have explicit unit-regression, integration, and architecture-fitness membership respectively. | "mcp/tests/test_retry_selection.py"; "mcp/tests/test_quality_subprocess_environment.py"; "mcp/tests/test_retry_coverage.py" | mcp/tests/test-evidence-lanes.toml:126-126; mcp/tests/test-evidence-lanes.toml:371-371; mcp/tests/test-evidence-lanes.toml:471-471 |
| The seven retained kernel regressions remain explicitly classified while deleted Candidate A tests are absent. | "mcp/tests/test_kernel_pure_regressions.py" | mcp/tests/test-evidence-lanes.toml:123-123 |
| The future-code candidate real-Git matrix is explicitly classified as integration evidence. | "mcp/tests/test_future_code_candidate.py" | mcp/tests/test-evidence-lanes.toml:252-252 |
| The exact code-memory pair suite is explicitly classified as integration evidence. | "mcp/tests/test_memory_candidate_pair.py" | mcp/tests/test-evidence-lanes.toml:334-334 |
| Every new ARSPAWN repair proof has one explicit semantic lane. | "mcp/tests/test_dispatch_agent_ambient_reviewer.py"; "mcp/tests/test_non_leaf_reviewer_evidence_retention.py"; "mcp/tests/test_quality_report_publication_security.py"; "mcp/tests/test_e2e_harness_selection.py" | mcp/tests/test-evidence-lanes.toml:250-250; mcp/tests/test-evidence-lanes.toml:340-340; mcp/tests/test-evidence-lanes.toml:370-370; mcp/tests/test-evidence-lanes.toml:457-457 |

## Cross-Repo References

No cross-repository evidence is required.

| Finding | Anchor | Source |
| --- | --- | --- |
| Classification applies only to this repository's verification tree. | — | — |

## MCAR-L02 Coherence Evidence Lane

The manifest classifies `test_curator_coherence.py` explicitly as integration evidence alongside
the existing future-code real-Git suite. This prevents the Dagger selector from silently treating
the new filesystem/Git/task publication fixture as unit evidence.

## Update History

- 2026-08-31T08:05+02:00 — Classified the four A003-unregistered ARSPAWN proof modules exactly
  once: three integration routes and one architecture-fitness selector-closure route.

- 2026-08-30T15:15:36+02:00 — Classified `test_public_surface_conformance.py` explicitly as
  integration evidence. Verification remains closeout-owned.

- 2026-08-30T04:54+02:00 — Added explicit integration-lane ownership for the exact
  code-memory candidate-pair suite after the lifecycle Dagger census rejected an unclassified
  test file. No product or requirement semantics changed.

- 2026-08-29T08:52+02:00 — Added explicit integration classification for the structured
  curator-coherence forcing suite. Verification remains closeout-owned.

- 2026-08-29T07:35+02:00 — Added explicit integration-lane ownership for the future-code
  candidate real-Git matrix and repaired exact manifest citations shifted by that row.

- 2026-08-28T14:18+02:00 — Reconciled manifest citations against the committed PDLS candidate;
  the explicit-lane contract is unchanged.

- 2026-08-28T05:10+02:00 — Removed the two stale Candidate A test rows and retained the renamed
  kernel regression module in its explicit unit lane after Q5 v19 forced the stale-row refusal.
- 2026-08-27T18:33+02:00 — Recorded explicit unit-regression membership for the retry coverage
  composition and quality child-environment suites.
- 2026-08-27T18:06+02:00 — Added explicit architecture-fitness membership for the M40-M45
  Requirement Attempt Journal structural proof.
- 2026-08-27T17:19+02:00 — Added explicit unit-regression membership for the retry-selection
  forcing suite in the same change that introduced it.
- 2026-08-27T13:32+02:00 — Added explicit architecture-fitness membership for M39 compilation
  doctrine and the split tool-signature exemption suite. Verification remains closeout-owned.

- 2026-08-27T12:43+02:00 — M38: created the manifest sidecar and recorded explicit registration
  of the acceptance-envelope structural test. Verification metadata remains empty until governed
  closeout stamps the PDLS code commit.
