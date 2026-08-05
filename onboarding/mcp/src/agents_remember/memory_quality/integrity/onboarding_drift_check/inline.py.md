# mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/inline.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/inline.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-29T12:10+02:00                     |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview      | `../../../../../overview.md`               |

## Purpose

`inline.py` extracts inline onboarding blocks embedded in source files and
classifies them by source digest. Inline onboarding reuses the same content model
as sidecars but is verified through an embedded `sourceDigest`.

## Code Commentary

### Logic

`line_bounds` and `expand_inline_bounds` grow the block to include the surrounding
comment delimiter; `extract_inline_onboarding_block` parses metadata between the
`@ar-onboarding` / `@ar-onboarding-end` markers; `compute_inline_source_digest`
hashes the source with the block removed; `classify_inline_source` compares the
recorded `sourceDigest` to the computed digest; `discover_inline_onboarding_sources`
finds inline-eligible sources via storage resolution.

### Invariants And Boundaries

- The digest is computed over the source **with the block removed**, so editing
  the block contents does not register as drift.
- Non-UTF-8 sources are reported as unsupported rather than parsed.
- Reports drift only.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Inline source enumeration reads repo files through `git_ops.list_repo_sources`. | `list_repo_sources` | mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/git_ops.py:41-45 |
| Inline parsing and CLI behavior are covered by the package tests. | `InlineOnboardingTests`; `DriftMainCliTests` | mcp/tests/test_onboarding_drift.py:62-121; mcp/tests/test_onboarding_drift.py:124-153 |

## Update History

- 2026-08-03T04:00:52+02:00 — 260731-EFA-L6 W3-B06 curator: curated 4 citation findings for inline source enumeration and drift-test coverage.

- 2026-05-29T12:10+02:00: Created when `drift.py` was split into focused modules; metadata pending closeout refresh to the split commit.
