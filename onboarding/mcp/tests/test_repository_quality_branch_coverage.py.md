# mcp/tests/test_repository_quality_branch_coverage.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_repository_quality_branch_coverage.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T00:23:26+00:00 |
| lastVerifiedCommitHash | `97e8ed2e1fae21756c3ad995c30613d4fbfcc503` |
| lastVerifiedCommitDate | 2026-09-06T02:09:33+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

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

### Logic

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
- Strict gate cases reject a missing published manifest both before and after reporting; recovery rejects a typed published failure. The organizational-quality case records repair only when an operation-progress owner exists.

### Conventions

The refusal matrix calls the public `parse_published_quality_manifest` owner directly. The rename removes the private parser entry point without adding a compatibility alias; the seven existing field-refusal cases retain their behavior.

### Invariants And Boundaries

- The real parser is exercised by the seven explicit refusal cases listed above; this suite does not independently corrupt every bound field. The separate helper test rejects incomplete digest/dependency field sets.
- Generation digests and dependency helpers accept exactly the declared field sets; incomplete
  or ambiguous sets refuse.
- Publication inventory bounds (size limits, required artifacts) are enforced on real exported
  directories; no fallback inventory is accepted.

### Todos

None recorded.

## Docs References

No external Domain Documentation source is configured. These are repository-owned implementation and verification contracts; no external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external domain source. | N/A | N/A |

## Repo-Internal References

These source owners establish the current behavior and the stated fixture boundaries.

| Finding | Anchor | Source |
| --- | --- | --- |
| The fixture publishes a real host generation for parser input. | `_valid_manifest` | mcp/tests/test_repository_quality_branch_coverage.py:30-42 |
| Seven bound-field faults refuse through the public parser. | `test_manifest_parser_refuses_each_uncovered_bound_field` | mcp/tests/test_repository_quality_branch_coverage.py:57-85 |
| Digest and dependency helpers reject incomplete fields. | `test_manifest_digest_and_dependency_helpers_require_exact_field_sets` | mcp/tests/test_repository_quality_branch_coverage.py:88-103 |
| Export inventory enforces size and required-artifact bounds. | `test_report_publication_refuses_oversized_and_missing_required_artifacts` | mcp/tests/test_repository_quality_branch_coverage.py:106-123 |
| A zero return code cannot substitute for a retained manifest. | `test_strict_gate_refuses_success_without_a_manifest_before_and_after_reporting` | mcp/tests/test_repository_quality_branch_coverage.py:126-159 |
| A published failed terminal result cannot recover as a green gate. | `test_recovery_refuses_a_typed_published_failed_terminal_result` | mcp/tests/test_repository_quality_branch_coverage.py:162-200 |
| Repair recording requires the operation-progress owner. | `test_organizational_quality_failure_records_repair_only_with_progress` | mcp/tests/test_repository_quality_branch_coverage.py:204-242 |

## Cross-Repo References

No separate cross-repository protocol is established by this file. In-tree fixture languages and Dagger SDK doubles remain same-repository evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository evidence is required. | N/A | N/A |


## Update History

- 2026-09-06T00:23:26+00:00 — L30 recovery: Reverified retained source or route ownership against actual candidate commit 97e8ed2e1fae21756c3ad995c30613d4fbfcc503; replaced the superseded private-candidate stamp.

- 2026-09-06T00:17+02:00 — Documented the public manifest parser owner and existing seven-field refusal matrix; corrected the nearest overview and stale integration-test claims after checking the full source.

- 2026-09-04T10:05+02:00 - 260831-CCR-L12 Gate-5 memory pass for cfd09381 (CCR-R12@v4): recorded the schema-v3.1/runtime-authority coverage additions in the repository-quality branch-coverage suite.


- 2026-09-03T12:30+02:00 -- 260831-CCR memory curation pass for 685f83c44055 (CCR-R22@v1/L22): created the sidecar for the new repository-profile publication/branch-coverage tests.
