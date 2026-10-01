# mcp/src/agents_remember/memory_quality/knowledge_validator/report.py

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

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The validator's design authority is the coordination-root note
Doc14 (`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`) and the
requirement packet `MIK-R22@v1` of task `260928_maintained-invariant-knowledge`; both live outside
the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

The three result types.

- One violation and its rendering. [1]
- The report and its refusing/report-only split. [2]
- The refusal lists every refusing violation. [3]
- A shape refusal names file, field and rule. [4]

### Cross-Repo References

No meaningful cross-repo references found: the validator reads one memory tree and one paired code tree, both addressed explicitly by the caller.

No cross-repo boundary is crossed by this file.
