# mcp/src/agents_remember/serving/conversation/active/projector/

| Field | Value |
| --- | --- |
| sourceRoute | `mcp/src/agents_remember/serving/conversation/active/projector/` |
| onboardingRoute | `mcp/src/agents_remember/serving/conversation/active/projector/overview.md` |
| parentOverview | [`active/overview.md`](../overview.md) |

## Governing Overview

[Active conversation serving overview](../overview.md)

## Purpose

This package projects one active session at one exact bridge epoch into canonical conversation items and an ordered live mutation stream. Its public facade coordinates native and echo ingestion, selected-child history, pending interactions, paging, hydration, and polling. The package retains the former module's import surface through `projector/__init__.py`.

## Hot Path Summary

The service resolves the exact session/epoch. The facade wires one shared spine and reader bundle; the rebuild coordinator applies native/echo inputs and provenance to the mutation stream’s canonical store. Paging and subscription consume that same projection.

## How It Is Built

`ActiveSessionProjector` in `facade.py` composes the projection graph and runs its one-second, consumer-driven poll lifecycle. `RebuildCoordinator` serializes initial hydration and applies poll cycles under the shared apply lock. Native ingestion owns native-history and evidence watermarks, completeness tracking, mapping, and live/native twin suppression. Echo ingestion owns transcript ordering, queued evidence, and eviction realignment. `ProjectionMutationStream` owns the canonical `ProjectionStore`, event cursors, retained events, and subscriber fan-out; the coordinator also applies submission-provenance verdicts to that same store and emits their mutations through the stream.

Two frozen bundles define the shared session context. `SessionProjectionSpine` carries identity, the controlled-session catalog entry, mapper, mutation stream, agent authority, evidence references, apply lock, and clock, with derived `parent_thread_id` and `bridge_epoch`. `BridgeReaders` carries the five reads—evidence, native pages, transcript, submission provenance, and snapshot—as one substitutable set. Native ingestion, echo ingestion, child-history projection, and the rebuild coordinator receive the same spine and readers. Interaction projection receives the shared stream, parent identity, and agent-reference reader directly; agent authority and evidence-reference minting remain separate components.

Wire contracts are imported from `models/conversations/`, including evidence, content, status, cursors, identity, control wire, and stream events.

| File | Responsibility |
| --- | --- |
| `__init__.py` | Compatibility exports for the former module surface. |
| `facade.py` | Public projector lifecycle and component composition. |
| `rebuild_coordinator.py` | Hydration, page assembly, poll ordering, status, provenance. |
| `mutation_stream.py` | Canonical store ownership, mutation publication, event cursors, retention, subscribers. |
| `native_ingestion.py` | Native/evidence watermarks, mapping, completeness, twin suppression. |
| `echo_ingestion.py` | Transcript submission-echo/evidence zipper and eviction realignment. |
| `agent_authority.py` | Child-thread identity and roster-status authority. |
| `child_history.py` | Selected-child native-history eligibility and singleflight hydration. |
| `interaction_projection.py` | Parent and multiplexed child pending interactions. |
| `references.py` | Public-safe evidence reference coordinates. |
| `wiring.py` | Shared projection spine and the substitutable bridge-read surface. |

## Invariants And Boundaries

- One exact session and epoch share one component graph, canonical store, and totally ordered mutation stream. The active service serializes projector resolution per session and creates or retires instances as identity and lifecycle require.
- Components are separated by mutable authority. Shared ingestion machinery uses the same spine and whole reader bundle; substituting only one reader can interleave different sessions. Cross-component ingestion and poll application use the shared apply lock and stream rather than a second history store or projection pipeline.
- Native history supplies historical items where supported; live evidence supplies the incremental tail. Native re-walks suppress twins of already projected live turns instead of duplicating them under native IDs. Native-read failure can leave completeness unknown.
- The transcript-echo path projects user submission echoes and advances past non-user transcript entries. It zips queued evidence bodies to those echoes in turn order.
- Selected-child native history is opt-in, eligibility-checked, and singleflight per child, with bounded concurrent reads. Native-history unavailability and limit failures produce child-local unavailable state; a successful retry records recovery.
- Subscriber overflow sends a typed retention gap and closes the affected subscriber. Epoch mismatch and ordering faults terminate the projector with a typed gap; repeated control-read failures also terminate it after the configured threshold.
- Without subscribers or a renewed consumer lease, the projector retires and releases heavy projection state after the 30-second consumer TTL.
- `ActiveSessionProjector` remains importable from `projector/__init__.py`, alongside the retained page-result, sentinel, and ordering-error exports.

The memory layer's source registry has no configured entries. The source and tests below provide repository-owned evidence; this package composes repository-local components and bridge ports.

Focused service tests check hydration order, live/native deduplication, prior native history, older paging, epoch gaps, split results, pending-frame completeness and regressed evidence tips. The reconnect test checks singleflight replacement of a retired projector. Described implementation behavior does not by itself establish test coverage or execution acceptance.

## Evidence

- The active service creates and retires projector instances, serializing resolution per session and checking the current bridge epoch. [1]
- The package owns one canonical projection store through its mutation stream. Store operations apply items, deltas, provenance, and chronological page slices; the rebuild coordinator applies provenance verdicts to this same store and publishes the resulting mutations. [2]
- Focused regressions check that settled live turns are projected once despite disjoint native IDs and concurrent reconnect requests replace a retired projector once. [3]
