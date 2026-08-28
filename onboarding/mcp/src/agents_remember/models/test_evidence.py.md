# mcp/src/agents_remember/models/test_evidence.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/test_evidence.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-28T07:20+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Models overview](overview.md)

## Purpose

Defines the opaque candidate-bound Dagger certification capability accepted by coverage, quality,
retry, lifecycle, closeout, and integration consumers. Diagnostic artifacts have separate
test-support schemas and cannot be loaded or modeled here.

## Code Commentary

### Logic

A private module-owned authority mints `CertifyingTestEvidence` only after the Dagger publication
loader verifies candidate-tree and result-digest provenance. Direct construction always raises.
`require_certifying_evidence` accepts only that exact capability and rejects every other object;
`evidence_payload` serializes only already-verified certification.

### Conventions

Typed records and refusal payloads remain owned at the narrowest stable boundary. Callers consume
the public function or model instead of re-deriving its lower-level state machine.

### Invariants And Boundaries

- Diagnostic/non-certifying evidence is intentionally not represented by a production model and
  cannot be elevated, copied, parsed, or inferred into certifying evidence.
- Accepting consumers require the private verified-Dagger construction path and exact module-owned
  authority identity.
- Missing, unreadable, ambiguous, or conflicting authority fails loudly; this file does not add a
  fallback or compatibility shadow.

### Todos

None recorded.

## Docs References

The configured Domain Documentation registry is empty. No external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain source is required to establish this repository-owned implementation. | `EVIDENCE_SCHEMA_VERSION` | mcp/src/agents_remember/models/test_evidence.py:1-123 |

## Repo-Internal References

The source file is the direct evidence for this unit; its governing overview records adjacent owners.

| Finding | Anchor | Source |
| --- | --- | --- |
| The private authority, non-constructible capability, accepting-consumer guard, and certifying serializer are implemented here. | `_DAGGER_AUTHORITY`; `CertifyingTestEvidence`; `require_certifying_evidence`; `evidence_payload` | mcp/src/agents_remember/models/test_evidence.py:33-123 |

## Cross-Repo References

No cross-repository source is allowed by the resolved settings, and this unit owns no external
protocol claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repository reference applies. | `EVIDENCE_SCHEMA_VERSION` | mcp/src/agents_remember/models/test_evidence.py:1-123 |

## Update History

- 2026-08-28T06:28+02:00 — PDLS wave 005 curator: removed the stale diagnostic-model and
  caller-loadable payload claims. Product code now owns only opaque verified-Dagger certification;
  every diagnostic and non-accepting artifact remains test-support evidence with no compatibility
  reader.

- 2026-08-25T15:44+02:00 — Created during PDLS whole-system reconciliation after source and
  requirement review. Verification remains closeout-owned.
