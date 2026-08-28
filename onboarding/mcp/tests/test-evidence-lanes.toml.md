# mcp/tests/test-evidence-lanes.toml

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test-evidence-lanes.toml` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-28T14:18+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
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
| Architecture-fitness membership explicitly includes the M38, M39, and M40-M45 structural proofs. | "mcp/tests/test_requirement_acceptance_envelope_doctrine.py"; "mcp/tests/test_requirement_attempt_journal_doctrine.py"; "mcp/tests/test_requirement_compilation_gate_doctrine.py" | mcp/tests/test-evidence-lanes.toml:457-459 |
| The structural test checks the complete M38 template surface. | `test_worker_role_brief_and_report_require_one_complete_primary_block`; `test_reviewer_role_and_verdict_require_independent_adjudication_per_id`; `test_manager_and_task_workflow_preserve_primary_ownership_and_adjacent_context` | mcp/tests/test_requirement_acceptance_envelope_doctrine.py:22-113 |
| Retry selection, child-environment forcing, and coverage composition have explicit unit-regression, integration, and architecture-fitness membership respectively. | "mcp/tests/test_retry_selection.py"; "mcp/tests/test_quality_subprocess_environment.py"; "mcp/tests/test_retry_coverage.py" | mcp/tests/test-evidence-lanes.toml:126-126; mcp/tests/test-evidence-lanes.toml:363-363; mcp/tests/test-evidence-lanes.toml:460-460 |
| The seven retained kernel regressions remain explicitly classified while deleted Candidate A tests are absent. | "mcp/tests/test_kernel_pure_regressions.py" | mcp/tests/test-evidence-lanes.toml:123-123 |

## Cross-Repo References

No cross-repository evidence is required.

| Finding | Anchor | Source |
| --- | --- | --- |
| Classification applies only to this repository's verification tree. | — | — |

## Update History

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
