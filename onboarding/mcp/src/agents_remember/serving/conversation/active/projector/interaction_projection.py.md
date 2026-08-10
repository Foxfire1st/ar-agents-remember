# mcp/src/agents_remember/serving/conversation/active/projector/interaction_projection.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/active/projector/interaction_projection.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-30T12:51+02:00 |
| lastVerifiedCommitHash |  `7bf564a663bb61f12844dee39538dd09a1633cdb`|
| lastVerifiedCommitDate |  2026-08-10T12:28:42+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| Snapshot pending-interaction model. | `PendingInteraction` | mcp/src/agents_remember/models/conversations/control_wire.py:115-123 |
| Projection transition regressions. | `test_multiplexed_pending_interactions_project_labeled_and_resolve`; `test_concurrent_parent_pendings_all_project_and_resolve_per_id`; `test_parent_singular_rotation_resolves_evicted_and_keeps_rotated_live` | mcp/tests/test_conversation_projector_codex_agents_engine_1.py:255-309; mcp/tests/test_conversation_projector_codex_agents_engine_1.py:311-366; mcp/tests/test_conversation_projector_codex_agents_engine_1.py:368-417 |

## Cross-Repo References

No meaningful cross-repository references found.

## Update History

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-02T22:10:00+02:00 — 260731-EFA-L6 W2-B05 curator: anchored 2 citation items; scoped citation check now passes.

- 2026-07-31T16:35+02:00 — No content impact: the only change to
  `mcp/src/agents_remember/serving/conversation/active/projector/interaction_projection.py` since
  the L2 base commit is the whole-tree `ruff format` pass in `00e8379`, which re-wrapped 5 line(s)
  with no token change whatsoever. Checked by parsing both revisions and comparing the abstract
  syntax trees (identical) and the comment tokens (identical), so no symbol, signature, default,
  decorator, control-flow branch, docstring, or assertion this card describes has moved, and every
  claim this card makes about its own source still holds.

- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator ATTESTATION: this file was touched by the whole-tree `ruff format` commit (`00e8379`) and by nothing else — `git diff 00e8379 -- <this file>` is empty, so no identifier, signature, branch or behaviour in it changed in this leaf and no claim in this sidecar can have been invalidated by it. Attested, deliberately not rewritten.
- 2026-07-30T12:51+02:00 — 260727-CHATS-IM-L2 curator: created the interaction
  projection sidecar. Verification metadata remains blank until commit.
