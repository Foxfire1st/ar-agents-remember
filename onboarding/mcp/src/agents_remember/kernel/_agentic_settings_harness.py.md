# mcp/src/agents_remember/kernel/_agentic_settings_harness.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/kernel/_agentic_settings_harness.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-07T22:45:00+02:00                                            |
| lastVerifiedCommitHash | `b252c42cca200933d5c9c36e26de47a526a569ce`                                        |
| lastVerifiedCommitDate | 2026-08-07T23:58:52+02:00|
| governingOverview      | `../../../overview.md`                                          |

## Governing Overview

[MCP package overview](../../../overview.md)

## Purpose

``orchestration.harnesses`` parser: the effective harness registry. Entries merge over the builtin table by id; the strict merged pass enforces completeness and delivery-vehicle pairing, while the per-file pass checks shapes and unknown keys only.

## Code Commentary

- `_parse_harnesses`
- `_HarnessEntry`
- `_entry_string`
- `_entry_string_list`
- `_parse_harness_entry`
- `_resolved_launch`
- `_merged_harness`
- `_refuse_unpaired_vehicles`
- `_refuse_bad_effort_template`

## Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/agents_remember/kernel/_agentic_settings_harness.py`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module. | — | — |

## Update History

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
