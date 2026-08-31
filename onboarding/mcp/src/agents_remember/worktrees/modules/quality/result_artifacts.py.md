# mcp/src/agents_remember/worktrees/modules/quality/result_artifacts.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/modules/quality/result_artifacts.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-31T07:35+02:00 |
| lastVerifiedCommitHash | `f2b7c648f540efb9d64ceea22e11e651cb5cc914` |
| lastVerifiedCommitDate |  2026-08-31T15:32:32+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[worktrees/modules overview](../overview.md)

## Purpose

Cross-validates artifact references asserted by the authoritative clean-quality result before a
report generation is published.

## Code Commentary

### Logic

`validate_result_artifact_references` parses the authoritative result, extracts causal and ambient
E2E references, verifies that every reference is a safe exported path, and enforces that causal
references exist exactly when the quality-wrapper step completed.

### Conventions

The result may name evidence, but the exported inventory proves that the named bytes are part of the
same immutable generation.

### Invariants And Boundaries

- Dangling, malformed, or traversal-like references refuse publication.
- Completed wrapper evidence requires both causal artifacts.
- An incomplete wrapper cannot claim causal artifacts.
- No filename search or compatibility fallback supplies missing evidence.

### Todos

None.

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Result references must resolve inside the exact export inventory. | `validate_result_artifact_references` | mcp/src/agents_remember/worktrees/modules/quality/result_artifacts.py:13-28 |
| Step completion owns causal-reference presence. | `_validate_step_owned_references` | mcp/src/agents_remember/worktrees/modules/quality/result_artifacts.py:67-77 |

## Cross-Repo References

No cross-repository implementation dependency governs this file.

## Update History

- 2026-08-31T07:35+02:00 — Created for 260821-ARSPAWN-L5 independent-review repair. Verification remains closeout-owned.
