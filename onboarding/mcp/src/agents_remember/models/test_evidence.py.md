# mcp/src/agents_remember/models/test_evidence.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/test_evidence.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-25T15:44+02:00 |
| lastVerifiedCommitHash |  `1abeed661cbbf813c7c8a1b651a14dbcf2ad2b4e`|
| lastVerifiedCommitDate |  2026-08-25T17:21:45+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Models overview](overview.md)

## Purpose

Separates non-certifying diagnostic feedback from candidate-bound Dagger test certification.

## Code Commentary

### Logic

Typed bindings describe candidate tree and policy identity; a private Dagger authority constructs certifying evidence; loaders validate diagnostic payloads and consumers demand the required altitude.

### Conventions

Typed records and refusal payloads remain owned at the narrowest stable boundary. Callers consume
the public function or model instead of re-deriving its lower-level state machine.

### Invariants And Boundaries

- Diagnostic evidence cannot be elevated, copied, or inferred into certifying evidence; accepting consumers require the private verified-Dagger construction path.
- Missing, unreadable, ambiguous, or conflicting authority fails loudly; this file does not add a
  fallback or compatibility shadow.

### Todos

None recorded.

## Docs References

The configured Domain Documentation registry is empty. No external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain source is required to establish this repository-owned implementation. | `EVIDENCE_SCHEMA_VERSION` | mcp/src/agents_remember/models/test_evidence.py:1-220 |

## Repo-Internal References

The source file is the direct evidence for this unit; its governing overview records adjacent owners.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's concrete API, control flow, and validation boundary are implemented here. | `EVIDENCE_SCHEMA_VERSION` | mcp/src/agents_remember/models/test_evidence.py:1-220 |

## Cross-Repo References

No cross-repository source is allowed by the resolved settings, and this unit owns no external
protocol claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repository reference applies. | `EVIDENCE_SCHEMA_VERSION` | mcp/src/agents_remember/models/test_evidence.py:1-220 |

## Update History

- 2026-08-25T15:44+02:00 — Created during PDLS whole-system reconciliation after source and
  requirement review. Verification remains closeout-owned.
