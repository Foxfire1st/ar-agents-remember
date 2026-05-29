# mcp/tests/test_onboarding_drift.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/tests/test_onboarding_drift.py`       |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-29T12:10+02:00                     |
| lastVerifiedCommitHash | `12737deaac2fd75563ca1e3037cdac911023cf93` |
| lastVerifiedCommitDate | 2026-05-29T12:28:42+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

`test_onboarding_drift.py` covers the inline onboarding classifier and the drift
CLI facade, which were the lowest-coverage paths after `drift.py` was split.

## Code Commentary

### Logic

`InlineOnboardingTests` exercises `extract_inline_onboarding_block` (delimiter
expansion + metadata parse), `compute_inline_source_digest` (independence from
block contents), and `classify_inline_source` across up-to-date, drifted,
missing-block, missing-digest, and orphaned cases — all without git, using
temp files whose recorded digest is made self-consistent. `DriftMainCliTests`
runs `drift.main` on the shared external-memory fixture and asserts a clean
exit plus a written report.

### Invariants And Boundaries

- Inline classification is verifiable from file contents alone (no git needed).
- The CLI smoke test reuses `test_memory_quality.initialize_clean_memory_fixture`
  rather than rebuilding a repo fixture.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The inline classifier under test. | [inline.py](agents-remember-md/mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/inline.py) |
| The CLI facade under test and the reused fixture. | [drift.py](agents-remember-md/mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/drift.py) |

## Update History

- 2026-05-29T12:10+02:00: Created with the drift.py split tests; metadata pending closeout refresh to the split commit.
