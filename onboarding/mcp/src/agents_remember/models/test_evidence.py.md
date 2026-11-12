# mcp/src/agents_remember/models/test_evidence.py

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

## Evidence

### Docs References

The configured Domain Documentation registry is empty. No external documentation claim is made.

- No external domain source is required to establish this repository-owned implementation. [1]

### Repo-Internal References

The source file is the direct evidence for this unit; its governing overview records adjacent owners.

- The private authority, non-constructible capability, accepting-consumer guard, and certifying serializer are implemented here. [2]

### Cross-Repo References

No cross-repository source is allowed by the resolved settings, and this unit owns no external
protocol claim.

- No meaningful cross-repository reference applies. [3]
