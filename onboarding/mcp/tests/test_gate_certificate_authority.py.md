# mcp/tests/test_gate_certificate_authority.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Content-addressed five-gate certificate and finalization authority contracts.

## Code Commentary

### Logic

The chain separates Gate-2 artifacts from Gate-3 manifests and binds Gate-5 memory inputs and four predecessors. Red, partial, diagnostic or combined results refuse certification. Reuse follows dependencies: memory changes rerun Gate 5, unchanged inputs start none and image changes restart Gate 4. The store enforces exact bounded atomic bytes and admission rejects conflicting semantic inputs.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Certificates require original authority rather than a historical search or recomputed matching label. Finalization currentness is separate from merely holding a five-certificate chain.

### Todos

No file-local implementation change is requested by this reconciliation.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

- Five gate chain separates suite artifacts and finalization authority. [1]
- Red partial diagnostic and combined results never publish certificates. [2]
- Reuse is dependency aware and refuses forged or stale identity. [3]
- Profile mismatch and unproven runtime change fail closed. [4]
- Content store is exact atomic bounded and has no historical lookup. [5]
- Admission refuses conflicts misalignment and unproven candidate. [6]

### Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

Fixture repositories and protocol doubles do not establish a live external integration.
