# mcp/src/agents_remember/memory_quality/knowledge_validator/report.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/knowledge_validator/report.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T07:08:34+02:00 |
| lastVerifiedCommitHash | `ee5f14e5405505d126125830e5323f8915c8d047`|
| lastVerifiedCommitDate | 2026-09-29T07:25:39+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[memory_quality route overview](../overview.md)

## Purpose

**What the validator returns: violations, the report, and the refusal (MIK-R22 Failure behaviour).** Every violation names its file, field and rule. A report-only violation is carried but never refuses. A refusal lists every refusing violation.

## Code Commentary

### Logic

- `Violation(path, field, rule, message, report_only)` is ordered, so a report sorts deterministically. `render()` gives `path: field: [rule] message`, with `(report-only)` after the rule when it applies and `-` for an empty field; `to_document()` gives the JSON form.
- `ValidationReport(candidate, violations)` exposes `refusals`, `reports` and `ok` (no refusals), plus `render()` and `to_document()` (with `refusalCount` and `reportCount`).
- `KnowledgeValidationError(report)` is a `ValueError` whose message is "the knowledge validator (MIK-R22) refuses this memory commit: N violation(s) in <candidate>" followed by one rendered line per refusing violation.

### Conventions

- Frozen dataclasses; the message text is the refusal text a route passes on.

### Invariants And Boundaries

- A refusal names every refusing violation, never only the first.
- A formatting violation's message already names `agents-remember knowledge-format <path>` (set in `parsed.py`).

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The validator's design authority is the coordination-root note
Doc14 (`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`) and the
requirement packet `MIK-R22@v1` of task `260928_maintained-invariant-knowledge`; both live outside
the code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

The three result types.

| Finding | Anchor | Source |
| --- | --- | --- |
| One violation and its rendering. | `Violation` | mcp/src/agents_remember/memory_quality/knowledge_validator/report.py:15-35 |
| The report and its refusing/report-only split. | `ValidationReport` | mcp/src/agents_remember/memory_quality/knowledge_validator/report.py:39-67 |
| The refusal lists every refusing violation. | `KnowledgeValidationError` | mcp/src/agents_remember/memory_quality/knowledge_validator/report.py:70-79 |
| A shape refusal names file, field and rule. | `test_shape_refuses_a_bad_field_and_names_file_field_and_rule` | mcp/tests/test_knowledge_validator.py:106-111 |

## Cross-Repo References

No meaningful cross-repo references found: the validator reads one memory tree and one paired code tree, both addressed explicitly by the caller.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T07:08:34+02:00 — 260928-MIK-L22 curator (uncommitted change set on `ar/260928-mik-l22`, code base `4aa9a98cebb65d7bfb492d80a420e794a3fb9f8c` plus the working-tree delta): created this card for the new file MIK-R22 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
