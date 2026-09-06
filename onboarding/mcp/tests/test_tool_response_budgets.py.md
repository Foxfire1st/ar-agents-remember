# mcp/tests/test_tool_response_budgets.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_tool_response_budgets.py`  |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-09-06T21:45:53+00:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d`|
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

Checks tool-report creation, secret redaction, count/age pruning and full carryover-record preservation. The durable report holds detail while the response can remain compact. The old broad MCP payload/token-ceiling matrix is not retained in this file.

## Code Commentary

### Logic

The current evidence boundary is the source-listed behavior below. Earlier coverage claims in
history describe prior populations and must not be used to recreate removed tests or claim they
still run. The retained behavior and its fixture limits, described above, govern this card.

### Conventions

The table lists retained test definitions, not collected parametrized or subtest counts.
Inspect the cited setup and collaborators before treating a focused result as end-to-end evidence.

### Invariants And Boundaries

Preserve exact refusal, identity, and cleanup assertions rather than adding overlapping helper
cases. Coverage percentages are diagnostic and production CRAP 20 prompts review; neither implies
an obligation to restore removed cases. Full suites and whole-candidate review remain master-end
work. This source inspection does not claim a newly executed test or acceptance result.

### Todos

No additional implementation scope is opened by this memory reconciliation.

## Docs References

The repository has no configured Domain Documentation source. These claims concern its own test
fixtures and assertions, so the exact retained source is the direct evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain claim is required. | N/A | N/A |

## Repo-Internal References

Each current definition below can be inspected in the exact source file. Historical references
to removed methods are superseded by this current inventory.

| Finding | Anchor | Source |
| --- | --- | --- |
| Write creates report and returns path | `test_write_creates_report_and_returns_path` | mcp/tests/test_tool_response_budgets.py:54-60 |
| Secrets are redacted in reports | `test_secrets_are_redacted_in_reports` | mcp/tests/test_tool_response_budgets.py:62-69 |
| Prune keeps last five | `test_prune_keeps_last_five` | mcp/tests/test_tool_response_budgets.py:71-83 |
| Prune drops reports older than max age | `test_prune_drops_reports_older_than_max_age` | mcp/tests/test_tool_response_budgets.py:85-96 |
| Carryover report retains full records | `test_carryover_report_retains_full_records` | mcp/tests/test_tool_response_budgets.py:100-113 |

## Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external evidence is needed for these assertions. | N/A | N/A |

## Update History

- 2026-09-06T21:45:53+00:00 — Reconciled the retained IAS test/helper population and exact citation ranges, preserving prior history and verification provenance; no tests or review were run.


- 2026-08-15T23:38+02:00 — Reconciled the suite's L4 fixture and forcing role for protected integration branches, durable operation authority, external-memory parity, and recovery. Verification metadata remains closeout-owned.
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-02T16:55+02:00 — 260731-EFA-L6 W1-B08 curator: repaired 2 citation rows covering 4 source references and preserved verification metadata.

- 2026-06-10T09:00+02:00 — Added carryover plan/apply budget cases for 2.5.2 (GitHub #52): fat 100-candidate plan, duplicate-array apply, inline cap with overflow marker, and report round-trip retention.
- 2026-06-10T05:30+02:00: Created with the S4 response token budgets (2.5.1).
