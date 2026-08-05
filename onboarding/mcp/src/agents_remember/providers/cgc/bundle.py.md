# mcp/src/agents_remember/providers/cgc/bundle.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/providers/cgc/bundle.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T19:50+02:00                     |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

`bundle.py` rewrites CodeGraphContext seed bundle contents from a source repository root to a target repository root.

## Code Commentary

### Logic

It builds path replacement pairs for POSIX and platform string variants, safely extracts the source zip bundle, rewrites JSON, JSONL, Markdown, and text files, and writes a new target zip bundle with rewritten paths.

### Invariants And Boundaries

- Zip entries are checked to ensure extraction cannot escape the temporary root.
- Only JSON, JSONL, Markdown, and text files are rewritten.
- The function reports rewritten files and replacement count for seed diagnostics.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| CGC seed orchestration calls this module between export and load. | `rewrite_cgc_bundle_paths` | mcp/src/agents_remember/providers/cgc/seed.py:591-607 |
| Tests exercise JSON, JSONL, and text rewriting through the provider setup facade export. | `test_rewrite_cgc_bundle_paths_rewrites_json_jsonl_and_text` | mcp/tests/test_provider_setup.py:372-416 |

## Update History

- 2026-08-04T18:20+02:00 — 260731-EFA-L6 S18-B15 curator: resolved 4 citation findings. Re-anchored the
  seed-orchestration row to `_seed_rewrite`'s `rewrite_cgc_bundle_paths` call (seed.py:591-607) and the
  test row to its exact span (test_provider_setup.py:372-417). Scoped recheck clean.
- 2026-05-25T19:50+02:00: Created when CGC bundle path rewriting was extracted out of `provider_setup.py`.
