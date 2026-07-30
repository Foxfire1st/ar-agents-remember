# mcp/src/agents_remember/serving/conversation/active/projector/interaction_projection.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/active/projector/interaction_projection.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-30T12:51+02:00 |
| lastVerifiedCommitHash |  `3a8ff703d796dc585b86a458daaf9eb2af6b2b31`|
| lastVerifiedCommitDate |  2026-07-30T13:59:13+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Active projector package overview](overview.md)

## Purpose

Projects parent and multiplexed child pending interactions from current adapter snapshot
authority.

## Code Commentary

### Logic

`InteractionProjection.apply` keeps the singular parent interaction slot and separately projects
every multiplexed pending interaction that carries a thread id. Child requests receive an agent
ref plus adapter-provided label. Slot rotation resolves the evicted interaction; disappearance
resolves each multiplexed id. Resolution keeps the item but marks its phase unknown with an honest
reason because the projector did not observe the answer outcome.

### Conventions

Snapshot authority determines which interactions are pending; the component never invents an
answer.

### Invariants And Boundaries

- The singular parent slot is never double-projected from the multiplexed tuple.
- Concurrent parent requests beyond the oldest remain visible.
- Child labels enrich identity but never replace the thread id.
- Cleared interactions resolve individually.

### Todos

None known.

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Snapshot pending-interaction model. | [harness_control_models.py](agents-remember/mcp/src/agents_remember/serving/harness_control_models.py) |
| Projection transition regressions. | [test_conversation_active_service.py](agents-remember/mcp/tests/test_conversation_active_service.py) |

## Cross-Repo References

No meaningful cross-repository references found.

## Update History

- 2026-07-30T12:51+02:00 — 260727-CHATS-IM-L2 curator: created the interaction
  projection sidecar. Verification metadata remains blank until commit.
