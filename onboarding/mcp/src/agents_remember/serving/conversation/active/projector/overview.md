# mcp/src/agents_remember/serving/conversation/active/projector/

| Field | Value |
| --- | --- |
| repository | agents-remember |
| doc_type | `route-local-overview` |
| sourceRoute | `mcp/src/agents_remember/serving/conversation/active/projector/` |
| onboardingRoute | `mcp/src/agents_remember/serving/conversation/active/projector/overview.md` |
| parentOverview | [`active/overview.md`](../overview.md) |
| lastUpdated | 2026-08-09T17:18+02:00 |
| lastVerifiedCommitHash |  `2dea095cd68454a7a68893e37c07dbd8daa86d32`|
| lastVerifiedCommitDate |  2026-08-09T18:00:39+02:00|

## Governing Overview

[Active conversation serving overview](../overview.md)

## Purpose

Owns the active-session projection component graph. The package replaces the former
`active/projector.py` monolith without changing its public import surface: one facade coordinates
native and echo ingestion, child-history hydration, interaction projection, canonical mutations,
and rebuild/poll lifecycle for one exact session and bridge epoch. The native-ingestion boundary
also preserves transport-owned item identity when a raw native body is clipped or cannot satisfy a
harness mapper's exact schema.

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

Since 260731-EFA-L2 that composition is carried by two frozen bundles in `wiring.py`, and every
component takes them instead of re-listing their fields. `SessionProjectionSpine` is the machinery
one session's projection shares (identity, controlled session, mapper, mutation stream, agent
authority, evidence refs, apply lock, clock, plus the derived `parent_thread_id` / `bridge_epoch`);
`BridgeReaders` is the whole five-call read surface, substituted as one set. That is what makes
"one projection, one session, one epoch" structural rather than a convention repeated across five
parameter lists — a component wired to a different spine, or a test that fakes one reader and
leaves the others live, is reading two different sessions.

Native-page mapping is deliberately fail-soft at the shared ingestion boundary. Both the Codex
parent-history walk and Pi eager continuation route each `NativeEvidenceFrame` through
`map_native_frame`. An `arEvidenceTruncated` envelope becomes bounded
`<harness>:evidence-truncated` evidence; an exact mapper `UnmappableShape` becomes
`<harness>:malformed`. In both cases the visible item and parent ids come from the frame envelope,
never the clipped `preview`, and the remaining page continues. Typed gaps remain reserved for
lost ordering proof, epoch change, or repeated control-read failure — not a damaged item body whose
transport identity is intact.

## Load-Bearing Invariants

- `ActiveSessionProjector` remains import-compatible through `projector/__init__.py`.
- One exact session/epoch has one component graph and one totally ordered mutation stream.
- Every component of one projection receives the SAME `SessionProjectionSpine` and the SAME
  `BridgeReaders`; readers are substituted whole, never field by field (`wiring.py`).
- Native history remains authoritative where available; live evidence is the incremental tail.
- Native item and parent identity come from `NativeEvidenceFrame`, outside the raw body; truncation
  or schema failure must degrade one item without inventing an id or closing the projection.
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
| `native_ingestion.py` | Native/evidence watermarks, identity-preserving fail-soft mapping, completeness, twin suppression. |
| `echo_ingestion.py` | Claude transcript/evidence zipper and eviction realignment. |
| `agent_authority.py` | Child-thread identity and roster-status authority. |
| `child_history.py` | Selected-child native-history eligibility and singleflight hydration. |
| `interaction_projection.py` | Parent and multiplexed child pending interactions. |
| `references.py` | Public-safe evidence reference coordinates. |
| `wiring.py` | The shared projection spine and the one substitutable bridge-read surface. |

## Docs References

The resolved `Domain Documentation` registry has no entries; the package contract is
repository-owned and cited through the source and tests below.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The active service creates and retires projector instances. | `ActiveConversationService` | mcp/src/agents_remember/serving/conversation/active/service.py:57-259 |
| The package mutates one canonical projection store. | `ProjectionStore` | mcp/src/agents_remember/serving/conversation/active/store.py:135-445 |
| Focused regressions cover projection, restart, overflow, child hydration, and singleflight. | `test_settled_live_turns_project_once_when_native_ids_disjoint`; `test_concurrent_reconnect_replaces_a_retired_projector_once` | mcp/tests/test_active_projector_singleflight.py:24-94; mcp/tests/test_conversation_active_service.py:320-405 |
| Native truncation, malformed-body degradation, and Codex/Pi mode parity keep transport item and parent ids readable without an ordering gap. | `NativeFrameIdentityFallbackTests`; `test_an_unmappable_native_frame_degrades_without_an_ordering_fault_gap` | mcp/tests/test_conversation_native_ingestion.py:49-107; mcp/tests/test_conversation_control_and_library_helpers.py:937-960 |

## Cross-Repo References

No cross-repository implementation participates in this package.

## Update History
- 2026-08-09T17:18+02:00 — 260713-TES-L5 hotfix route refresh: documented the shared
  native-page fail-soft boundary, its transport-identity invariant, Codex/Pi parity, and the rule
  that a damaged item body is not an ordering fault. Verification stays pinned until closeout.

- 2026-08-03T03:02:37+02:00 — W3-B05 curator: resolved 3 Tier-2 table findings with exact anchors and source paths; fixer generated all final ranges.

- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator: added `wiring.py` (`SessionProjectionSpine`, `BridgeReaders`, `LIVE_BRIDGE_READERS`) to the ownership map and recorded the one-spine/one-reader-set invariant every component is now built from; also recorded `ProjectedSession` (facade entry) and `IngestionComponents` (rebuild order). Verification metadata stays pinned until closeout.
- 2026-07-30T12:51+02:00 — 260727-CHATS-IM-L2 curator: replaced the deleted monolith's
  route record with the component-graph ownership map and preserved the projector's public and
  behavioral invariants. Verification metadata remains blank until the code commit.
