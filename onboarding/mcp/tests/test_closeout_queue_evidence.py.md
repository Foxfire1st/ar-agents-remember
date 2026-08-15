# mcp/tests/test_closeout_queue_evidence.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_closeout_queue_evidence.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-15T14:05+02:00 |
| lastVerifiedCommitHash | `17987fa66a642306eb8d20fa9a4bff2b881550d2` |
| lastVerifiedCommitDate | 2026-08-15T14:36:30+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Owns structural parsing and exact authority binding for curator readiness, source-candidate
dispositions, grades, priorities, judgments, and atomic barrier aborts.

## Code Commentary

### Logic

The suite exercises the structured attestation and Markdown table parsers with missing, duplicate,
wrong-header, missing-outer-pipe, ragged, malformed-separator, stale-byte, wrong-author,
extra-decision, and mismatched-evidence cases, plus canonical success paths and direct parity with
the orchestration-task template.

### Invariants And Boundaries

- Known table formats are schema-parsed; substring presence never proves a disposition or judgment.
- Optional urgency/risk are absent unless the canonical decision records them; extra keys refuse.
- Only strategist/orchestrator evidence can grade or authorize a barrier abort.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Disposition parsing is structural and rectangular. | `test_disposition_table_parser_is_structural_and_rectangular` | mcp/tests/test_closeout_queue_evidence.py:124-170 |
| Canonical grades bind exact authority and evidence. | `test_canonical_grade_refusal_matrix_and_exact_evidence` | mcp/tests/test_closeout_queue_evidence.py:201-253 |
| Low-level Markdown and decision helpers fail closed. | `test_low_level_markdown_decision_and_evidence_helpers_are_fail_closed` | mcp/tests/test_closeout_queue_evidence.py:452-482 |

## Update History

- 2026-08-15T14:05+02:00 — L3 final targeted-gate repair: forces exact template-schema parity,
  optional urgency/risk authority, invalid provenance translation, unrelated-section skipping,
  empty tables, and malformed header/separator/data rows including pipe-less 4- and 9-cell rows.
- 2026-08-15T13:18+02:00 — No content impact: repository Ruff formatting changed only layout;
  parser and canonical-authority cases are identical.
- 2026-08-15T13:08+02:00 — No content impact: accepted the repository's test-root import grouping
  and private-name ordering; evidence cases and assertions are unchanged.
- 2026-08-15T12:53+02:00 — Created for L3's focused evidence-parser suite; final import ordering is
  Ruff-canonical and does not change test behavior.
