# mcp/src/agents_remember/serving/conversation/active/projector/

| Field | Value |
| --- | --- |
| repository | agents-remember |
| doc_type | `route-local-overview` |
| sourceRoute | `mcp/src/agents_remember/serving/conversation/active/projector/` |
| onboardingRoute | `mcp/src/agents_remember/serving/conversation/active/projector/overview.md` |
| parentOverview | [`active/overview.md`](../overview.md) |
| lastUpdated | 2026-07-30T12:51+02:00 |
| lastVerifiedCommitHash |  `3a8ff703d796dc585b86a458daaf9eb2af6b2b31`|
| lastVerifiedCommitDate |  2026-07-30T13:59:13+02:00|

## Governing Overview

[Active conversation serving overview](../overview.md)

## Purpose

Owns the active-session projection component graph. The package replaces the former
`active/projector.py` monolith without changing its public import surface: one facade coordinates
native and echo ingestion, child-history hydration, interaction projection, canonical mutations,
and rebuild/poll lifecycle for one exact session and bridge epoch.

## Architecture And Boundaries

`facade.py` is the only public orchestration object. It composes narrow state owners and retains
the one-second consumer-driven poll lifecycle. `rebuild_coordinator.py` serializes hydration and
poll cycles. `native_ingestion.py` and `echo_ingestion.py` own their respective source watermarks
and ordering rules. `mutation_stream.py` alone owns canonical store mutation, cursors, retention,
and subscriber fan-out. Child identity, selected-child history, pending interactions, and opaque
evidence references remain separate components.

The split is intentionally by mutable authority rather than by helper size. Each component owns a
bounded state set; cross-component writes flow through the shared apply lock and mutation stream.
The package does not add a second history store or a parallel projection pipeline.

## Load-Bearing Invariants

- `ActiveSessionProjector` remains import-compatible through `projector/__init__.py`.
- One exact session/epoch has one component graph and one totally ordered mutation stream.
- Native history remains authoritative where available; live evidence is the incremental tail.
- Claude transcript entries are submission echoes only and are zipped to evidence in turn order.
- Selected-child native history is opt-in, singleflight, bounded, and child-local on failure.
- Subscriber overflow, epoch changes, and ordering faults close with one typed gap.
- Dormant projectors release their heavy projection state after the consumer TTL.

## Onboarding Map

| File | Responsibility |
| --- | --- |
| `__init__.py` | Compatibility exports for the former module surface. |
| `facade.py` | Public projector lifecycle and component composition. |
| `rebuild_coordinator.py` | Hydration, page assembly, poll ordering, status, provenance. |
| `mutation_stream.py` | Canonical store mutations, event cursors, retention, subscribers. |
| `native_ingestion.py` | Native/evidence watermarks, mapping, completeness, twin suppression. |
| `echo_ingestion.py` | Claude transcript/evidence zipper and eviction realignment. |
| `agent_authority.py` | Child-thread identity and roster-status authority. |
| `child_history.py` | Selected-child native-history eligibility and singleflight hydration. |
| `interaction_projection.py` | Parent and multiplexed child pending interactions. |
| `references.py` | Public-safe evidence reference coordinates. |

## Docs References

The resolved `Domain Documentation` registry has no entries; the package contract is
repository-owned and cited through the source and tests below.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The active service creates and retires projector instances. | [service.py](agents-remember/mcp/src/agents_remember/serving/conversation/active/service.py) |
| The package mutates one canonical projection store. | [store.py](agents-remember/mcp/src/agents_remember/serving/conversation/active/store.py) |
| Focused regressions cover projection, restart, overflow, child hydration, and singleflight. | [test_conversation_active_service.py](agents-remember/mcp/tests/test_conversation_active_service.py), [test_active_projector_singleflight.py](agents-remember/mcp/tests/test_active_projector_singleflight.py) |

## Cross-Repo References

No cross-repository implementation participates in this package.

## Update History

- 2026-07-30T12:51+02:00 — 260727-CHATS-IM-L2 curator: replaced the deleted monolith's
  route record with the component-graph ownership map and preserved the projector's public and
  behavioral invariants. Verification metadata remains blank until the code commit.
