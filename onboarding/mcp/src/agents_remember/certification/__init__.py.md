# mcp/src/agents_remember/certification/__init__.py

## Governing Overview

[Governing route overview](overview.md)

## Purpose

Provides the repository-neutral public certification facade: canonical registry and plan operations, certificate storage and invalidation, exact-candidate lifecycle contracts, readiness projections, diagnostic and final-Codex lanes, measured replay, and telemetry contracts.

## Code Commentary

### Logic

Import blocks compose the owning modules; `__all__` names the supported public exports. The accumulated facade includes both final-Codex and replay surfaces, which were previously documented on separate sibling memory branches. Replay exports include frozen population/comparability, scenario evaluation, measured spans and comparison reports. Final-Codex exports retain the two-repetition certifying lane and its certificate compiler.

The facade exposes R05 admission/finalization and R16 telemetry builders, but importing those APIs does not connect them to a production closeout. The R11/R22 bridge is imported from `certification.certification_lane` by its consumers and is not re-exported here.

### Conventions

Keep algorithms, models and storage behavior in their owning modules. The facade selects public names; it does not become a second rail catalog or execution owner.

### Invariants And Boundaries

- Diagnostic output is structurally non-certifying and cannot satisfy a certification gate.
- Final-Codex and replay contracts keep their own identities and acceptance semantics.
- Public availability of lifecycle, telemetry and final-memory libraries is not evidence of production invocation.
- No rail execution, profile selection, memory scan or finalization starts when importing this facade.

### Todos

Production integration of typed lifecycle admission/finalization, closeout telemetry and final-memory executors remains incomplete in the inspected cumulative source. Those missing callers require implementation, not an onboarding stamp.

## Evidence

### Docs References

No external Domain Documentation source is configured for this repository. This card records repository-owned behavior from the source references below; no external documentation claim is made.

External domain documentation is not configured.

### Repo-Internal References

The cited source establishes the current contracts and boundaries described above. Source verification is documentation evidence, not acceptance of the implementation.

- Core certificates and non-certifying diagnostics [1]
- Final-Codex and typed lifecycle interfaces [2]
- Accumulated measured-replay surface [3]
- Telemetry imports and explicit public exports [4]

### Cross-Repo References

No separate cross-repository protocol is established by this file. The configured cross-repository allowance is empty; no external source is relied upon here.

No cross-repository evidence is required for these file-local claims.
