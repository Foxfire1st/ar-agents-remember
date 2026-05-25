# mcp/src/agents_remember/providers/cgc_bundle.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/cgc_bundle.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T19:50+02:00                     |
| lastVerifiedCommitHash | `ae9c4e5b6af38eda7f2b29006130c4263e9db62f` |
| lastVerifiedCommitDate | 2026-05-25T19:55:09+02:00|
| governingOverview      | `../../../overview.md`                     |

## Purpose

`cgc_bundle.py` rewrites CodeGraphContext seed bundle contents from a source repository root to a target repository root.

## Code Commentary

### Logic

It builds path replacement pairs for POSIX and platform string variants, safely extracts the source zip bundle, rewrites JSON, JSONL, Markdown, and text files, and writes a new target zip bundle with rewritten paths.

### Invariants And Boundaries

- Zip entries are checked to ensure extraction cannot escape the temporary root.
- Only JSON, JSONL, Markdown, and text files are rewritten.
- The function reports rewritten files and replacement count for seed diagnostics.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| CGC seed orchestration calls this module between export and load. | [cgc_seed.py](cgc_seed.py.md) |
| Tests exercise JSON, JSONL, and text rewriting through the provider setup facade export. | [test_provider_setup.py](agents-remember-md/mcp/tests/test_provider_setup.py) |

## Update History

- 2026-05-25T19:50+02:00: Created when CGC bundle path rewriting was extracted out of `provider_setup.py`.
