# mcp/tests/test_repository_quality_branch_coverage.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_repository_quality_branch_coverage.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T10:05+02:00 |
| lastVerifiedCommitHash | `cfd0938103b1392e471144b6997c51a41591ad2b` |
| lastVerifiedCommitDate | 2026-09-04T08:34:11+02:00 |
| governingOverview | `../overview.md` |

## Governing Overview

[mcp/tests overview](../overview.md)

## Purpose

Focused publication and quality-gate branch proofs for repository profiles: the new
`published_manifest` schema-v3 parser field refusals, generation/dependency digest helper field
discipline, publication inventory bounds (oversized and missing required artifacts), and the
integration-gate wiring that forwards the profile reference through
`worktrees/integration/integration_quality.py`. It closes the branch-coverage gaps the R22
cutover opened in manifest parsing and profile wiring.


CCR-R12@v4 (260831-CCR-L12, commit `cfd09381`) extends the schema-v3.1 coverage: the strict-gate
visible manifest is built with `runtime_authority_digest=None`, recovery publishes through
`ReportBindings(attestation=..., runtime_authority_digest=None)`, and the bound-field matrix now
implicitly covers the optional runtime-authority root field the parser validates.

## Code Commentary

`_valid_manifest` publishes a passing generation through
`clean_executor._publish_reports` using `agents_remember_profile_execution` and returns the
manifest dict.

- `test_manifest_parser_refuses_each_uncovered_bound_field` parameterizes seven parser
  refusals: invalid decoder, decoder naming no published file, generation drift, non-object
  files, non-string file name, bad profile digest, and blank selection id. Each must raise
  `ValueError` with its expected message fragment.
- `test_manifest_digest_and_dependency_helpers_require_exact_field_sets` proves
  `quality_generation_digest` / `quality_report_dependencies` reject incomplete field sets.
- `test_report_publication_refuses_oversized_and_missing_required_artifacts` proves the export
  inventory refuses artifacts over their declared size limits.
- The integration-gate tests (in `IntegrationQualityGateTests`-style fixtures) prove the full
  gate preview/run forward `profile_reference` and surface
  `certification-profile-invalid`-family failures as `IntegrationQualityFailure`.

## Invariants And Boundaries

- Every new schema-v3 bound field (profile digest, plan digest, selection id, executor adapter,
  result decoder) is individually refusal-covered; the tests run against the real parser.
- Generation digests and dependency helpers accept exactly the declared field sets; incomplete
  or ambiguous sets refuse.
- Publication inventory bounds (size limits, required artifacts) are enforced on real exported
  directories; no fallback inventory is accepted.

## Docs References

CCR-R22@v1 requires profile edits or referenced-input changes to invalidate only the declared
certificate dependency closure and an unchanged-byte interruption to resume with existing
certificates; gate certificates name the exact admitted profile and plan digest. Expected
verification evidence requires malformed, ambiguous, cyclic, later-gate-dependent,
undeclared-artifact, and wrong-gate fixtures to refuse before execution.

## Repo-Internal References

Consumes `agents_remember_profile_execution` from `repository_profile_test_support`, the
publication internals of `clean_executor._publish_reports`, the schema-v3 manifest parser in
`published_manifest.py`, and `integration_quality.run_integration_quality_gate`.
`_checkout_with_profile`/`_quality_target` helpers come from `test_worktree_closeout_quality_gate`.

| Finding | Anchor | Source |
| --- | --- | --- |
| Schema-v3 parser refusal matrix and helper field-discipline proofs. | `test_manifest_parser_refuses_each_uncovered_bound_field`; `test_manifest_digest_and_dependency_helpers_require_exact_field_sets` | mcp/tests/test_repository_quality_branch_coverage.py:48-110 |
| Inventory bound proofs (oversized/missing required artifacts) and the integration-gate profile forwarding. | `test_report_publication_refuses_oversized_and_missing_required_artifacts` | mcp/tests/test_repository_quality_branch_coverage.py:106-125 |

## Update History

- 2026-09-04T10:05+02:00 - 260831-CCR-L12 Gate-5 memory pass for cfd09381 (CCR-R12@v4): recorded the schema-v3.1/runtime-authority coverage additions in the repository-quality branch-coverage suite.


- 2026-09-03T12:30+02:00 -- 260831-CCR memory curation pass for 685f83c44055 (CCR-R22@v1/L22): created the sidecar for the new repository-profile publication/branch-coverage tests.
