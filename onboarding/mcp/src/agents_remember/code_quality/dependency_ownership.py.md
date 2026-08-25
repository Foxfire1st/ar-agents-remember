# mcp/src/agents_remember/code_quality/dependency_ownership.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/code_quality/dependency_ownership.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-25T15:44+02:00 |
| lastVerifiedCommitHash |  `1abeed661cbbf813c7c8a1b651a14dbcf2ad2b4e`|
| lastVerifiedCommitDate |  2026-08-25T17:21:45+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Python quality overview](overview.md)

## Purpose

Provides the canonical test-consumer graph used by targeted selection, retry proof, and causal localization.

## Code Commentary

### Logic

It parses Python imports and pytest plugin declarations, combines lifecycle-catalog consumers with explicit ownership, retains reason provenance, and returns safe-full impact when ownership is incomplete.

### Conventions

Typed records and refusal payloads remain owned at the narrowest stable boundary. Callers consume
the public function or model instead of re-deriving its lower-level state machine.

### Invariants And Boundaries

- Selection and retry share one owner; necessary import fan-out is preserved and attributed; unknown or ambiguous dependency truth fails closed to fresh proof.
- Missing, unreadable, ambiguous, or conflicting authority fails loudly; this file does not add a
  fallback or compatibility shadow.

### Todos

None recorded.

## Docs References

The configured Domain Documentation registry is empty. No external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain source is required to establish this repository-owned implementation. | `GLOBAL_TEST_INPUTS` | mcp/src/agents_remember/code_quality/dependency_ownership.py:1-540 |

## Repo-Internal References

The source file is the direct evidence for this unit; its governing overview records adjacent owners.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's concrete API, control flow, and validation boundary are implemented here. | `GLOBAL_TEST_INPUTS` | mcp/src/agents_remember/code_quality/dependency_ownership.py:1-540 |

## Cross-Repo References

No cross-repository source is allowed by the resolved settings, and this unit owns no external
protocol claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repository reference applies. | `GLOBAL_TEST_INPUTS` | mcp/src/agents_remember/code_quality/dependency_ownership.py:1-540 |

## Update History

- 2026-08-25T15:44+02:00 — Created during PDLS whole-system reconciliation after source and
  requirement review. Verification remains closeout-owned.
