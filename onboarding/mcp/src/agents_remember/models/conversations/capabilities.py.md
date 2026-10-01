# mcp/src/agents_remember/models/conversations/capabilities.py

## Governing Overview

[models conversations overview](overview.md)

## Purpose

`models/conversations/capabilities.py` (260731-EFA-L9, moved from
`serving/conversation/_models_status.py`) owns the fixture-evidence-bound capability contract:
exact evidence products gate `supported`/`partial` claims.

## Code Commentary

### Logic

`CapabilityEvidence` (cit:(["class CapabilityEvidence"], mcp/src/agents_remember/models/conversations/capabilities.py:11-11)) requires the exact runtime-fixture
evidence product; `FeatureCapability` (cit:(["class FeatureCapability"], mcp/src/agents_remember/models/conversations/capabilities.py:18-18)) carries the deliberate
no-version-demotion NOTE — the contract is the only gate and runtime/helper versions are
informational metadata only; `ConversationCapabilities` (cit:(["class ConversationCapabilities"], mcp/src/agents_remember/models/conversations/capabilities.py:102-102)) aggregates the live, history,
attachment, control, and telemetry slices.

### Invariants And Boundaries

- `supported`/`partial` capability claims require exact runtime-fixture evidence and a fixture id;
  fixture evidence itself has `enablesCapabilities=false`.
- Do not reintroduce version-string demotion (L5F R4).

### Todos

No known follow-up.

## Evidence

### Docs References

No external/domain documentation is configured.

No configured domain documentation was available.

### Repo-Internal References

- Capability state requires coherent evidence; supported/partial states require runtime-fixture evidence and version metadata alone does not demote capability. [1]

### Cross-Repo References

No cross-repository implementation participates.

No meaningful cross-repo references found.
