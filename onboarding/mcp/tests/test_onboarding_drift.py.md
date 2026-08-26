# mcp/tests/test_onboarding_drift.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_onboarding_drift.py`       |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-11T15:20+02:00                     |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d` |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview      | `../overview.md`                              |

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

| Finding | Anchor | Source |
| --- | --- | --- |
| The inline classifier under test. | `extract_inline_onboarding_block`; `compute_inline_source_digest`; `classify_inline_source` | mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/inline.py:61-82; mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/inline.py:85-88; mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/inline.py:91-175 |
| The CLI facade under test. | `main` | mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/drift.py:225-315 |
| The CLI test and reused fixture. | "class DriftMainCliTests(unittest.TestCase):"; "def initialize_clean_memory_fixture(root: Path) -> None:" | mcp/tests/test_memory_quality.py:415-415; mcp/tests/test_onboarding_drift.py:124-124 |

## Update History

- 2026-08-11T15:20+02:00 — Replaced generic class/helper anchors with their exact declarations and
  refreshed the moved shared-fixture range.
- 2026-08-03T04:00:52+02:00 — 260731-EFA-L6 W3-B06 curator: curated 4 citation findings for inline classification, CLI, and shared-memory-fixture evidence.

- 2026-06-11T14:12+02:00: No content impact: the repository rename sweep replaced `agents-remember-md` with `agents-remember` in the source file; the card already uses the new name and its semantics are unchanged.
- 2026-05-29T12:10+02:00: Created with the drift.py split tests; metadata pending closeout refresh to the split commit.
