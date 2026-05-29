# mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/inline.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/inline.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-29T12:10+02:00                     |
| lastVerifiedCommitHash | `12737deaac2fd75563ca1e3037cdac911023cf93` |
| lastVerifiedCommitDate | 2026-05-29T12:28:42+02:00|
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

| Finding | Source Path |
| --- | --- |
| Inline source enumeration reads repo files through `git_ops.list_repo_sources`. | [git_ops.py](agents-remember-md/mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/git_ops.py) |
| Inline parsing and CLI behavior are covered by the package tests. | [test_onboarding_drift.py](agents-remember-md/mcp/tests/test_onboarding_drift.py) |

## Update History

- 2026-05-29T12:10+02:00: Created when `drift.py` was split into focused modules; metadata pending closeout refresh to the split commit.
