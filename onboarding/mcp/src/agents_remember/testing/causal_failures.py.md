# mcp/src/agents_remember/testing/causal_failures.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/testing/causal_failures.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-25T15:44+02:00 |
| lastVerifiedCommitHash |  `1abeed661cbbf813c7c8a1b651a14dbcf2ad2b4e`|
| lastVerifiedCommitDate |  2026-08-25T17:21:45+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Python test infrastructure overview](overview.md)

## Purpose

Implements pytest-side causal failure classification, dependency suppression, and durable causal reports.

## Code Commentary

### Logic

Hooks load preflight output, annotate execution profiles, skip only proven blocked nodes, retain runtime failure families, and render bounded JSON/Markdown evidence.

### Conventions

Typed records and refusal payloads remain owned at the narrowest stable boundary. Callers consume
the public function or model instead of re-deriving its lower-level state machine.

### Invariants And Boundaries

- Blocked status requires an explicit owner edge; independent or process-sensitive failures remain observable; report publication follows the certifying evidence boundary.
- Missing, unreadable, ambiguous, or conflicting authority fails loudly; this file does not add a
  fallback or compatibility shadow.

### Todos

None recorded.

## Docs References

The configured Domain Documentation registry is empty. No external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain source is required to establish this repository-owned implementation. | `CAUSAL_REPORT_OPTION` | mcp/src/agents_remember/testing/causal_failures.py:1-293 |

## Repo-Internal References

The source file is the direct evidence for this unit; its governing overview records adjacent owners.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's concrete API, control flow, and validation boundary are implemented here. | `CAUSAL_REPORT_OPTION` | mcp/src/agents_remember/testing/causal_failures.py:1-293 |

## Cross-Repo References

No cross-repository source is allowed by the resolved settings, and this unit owns no external
protocol claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repository reference applies. | `CAUSAL_REPORT_OPTION` | mcp/src/agents_remember/testing/causal_failures.py:1-293 |

## Update History

- 2026-08-25T15:44+02:00 — Created during PDLS whole-system reconciliation after source and
  requirement review. Verification remains closeout-owned.
