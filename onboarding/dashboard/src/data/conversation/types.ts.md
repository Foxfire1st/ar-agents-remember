# dashboard/src/data/conversation/types.ts

## Governing Overview

[data/conversation overview](overview.md)

## Purpose

The browser mirror of the landed **SC1 normalized conversation wire grammar**
(`serving/conversation/models.py`). Every field name is the exact camelCase the server's WireModel
emits (`alias_generator=to_camel`). Active + control responses drop null keys (`exclude_none`), so
optional fields are `?` and a decoder must treat absent and null identically. These are **consumed
types only** — the browser never authors durable conversation history (design §2 invariant 8, §11.3);
nothing here validates a schema (the server is the sole authority), and the reducer defends only against
faults it can actually observe (revision regressions, cursor gaps), never against re-validating a
trusted shape.

## Code Commentary

### Logic

- `HarnessId` (`codex`/`claude`/`pi`/`eve`) and `NativeConversationRef` (`harnessId`, `vendorConversationId`,
  `projectScope`, `identityDigest`); `ActiveConversationRef` extends it with `arSessionId` + `bridgeEpoch`
  — the pair the reducer matches identity on. `eve` joined the union with the eve product-integration
  change set so a native session backend whose runtime the adapter starts is representable here like
  any other harness; the comment above the union states the mirror-of-the-server rule, and the server
  side is `models/conversations/identity.py`.
- `ActivePageCursor` / `ActiveEventCursor` are compile-time BRANDED strings (bare on the wire) so a page
  cursor can never be passed to an event route and vice-versa (§6.1/§6.8).
- `ConversationContentBlock` — the block union: `markdown`/`text`/`thinking`/`code`/`tool-input`/
  `tool-output`/`diff`/`image-ref` (carries `alt` + `altProvenance`: `supplied-description` |
  `filename-mime-fallback` — the required-label contract)/`file-ref`/`resource-ref`/`choices`/
  `unknown-vendor` (`vendorType` + `safeSummary` + `evidenceRef`, preserved as labeled evidence).
- `ConversationItem` — `itemId`, `revision`, `globalOrdinal` (the server ordinal the feed's
  `aria-posinset` reads), `turnId?`, `lane`/`source`/`provenance`/`role`/`kind`/`phase`, `blocks`,
  `correlation?`, `agent?`, timestamps, `evidenceRef?`.
- `ConversationAgentStatus` / `ConversationAgentRef` (D2/D3) — harness sub-agent
  identity on the wire. The status union is `registered`/`running`/`completed`/`interrupted`/
  `failed`/`unknown`; the ref carries `agentId` + optional `agentPath`/`nickname`/`role`/`joinKey`/
  `parentAgentId` + `status`. `ConversationItem.agent?` is purely ADDITIVE: absent (or null) means
  the item belongs to the parent conversation. Identity is evidence-bound — the server populates
  `nickname`/`role`/`agentPath` only when collab/join evidence proved them, so an unresolved
  identity renders as `agent <short-id>`, never a fabricated name (the label precedence itself
  lives in `agents.ts`).
- `ConversationStatus` — the canonical status (§6.5): `process`, `freshness`, and `turn`
  (`state`/`turnId: string | null`/`stateSince`/`terminalOutcome`). `turn.turnId` is nullable and IS
  null on the hosted-codex wire during a working turn, which is why the interrupt hook must
  correlate the id from item evidence.
- `ConversationCapabilities` — `live`/`history`/`controls`/`telemetry` `FeatureCapability`s with a
  `CapabilityState` (`supported`/`partial`/`unavailable`/`unverified`). `controls.interrupt` is the
  KNOWN-STALE L1 page view (register L3.5) — reported `unverified` for all three harnesses.
- `ConversationPage`, `ConversationMutation` (`append-item`/`append-block-delta`/`upsert-item`/
  `replace-page`/`status`/`gap`), and `ConversationEventEnvelope` (`cursor`, `previousCursor`,
  `sequence`, `eventId`, `delivery: live | resume-replay | native-rehydrate`, `mutation`) — the exact
  transport shapes the reducer reduces.
- `MetricEvidence<T>` + `ConversationTelemetry` — evidence-bound metrics whose absent members are
  omitted, never zero (A2). `InterruptOperation` — `requestId`-stable, `acknowledgement` ≠ `settlement`.
  `ConversationRouteError` — the typed `{status, detail, httpStatus}` a refusal is surfaced as (never
  guessed into success). `StreamPhase` — the store's connection lifecycle union.

### Invariants And Boundaries

- Consumed-only: no type here is a runtime validator; absent ≡ null for every optional field.
- Agent identity is additive and evidence-bound: `ConversationItem.agent` absent ≡ the parent
  conversation, and the ref's label fields carry only what server evidence proved — the browser
  never invents a name for an unresolved agent.
- Cursors are purpose-branded at compile time; the two families are non-interchangeable.
- Identity is `arSessionId`+`bridgeEpoch`; `identityDigest` exists on the wire but is domain-scoped
  across services and must NOT be used for cross-service equality.
- Telemetry/metric shapes carry evidence + freshness; a missing metric is an omitted key, never a zero.

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries are
configured. This one-to-one card therefore relies on its direct agents-remember source/tests and the
reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- The reducer consumes these item/block/event/status types. [1]
- The roster derivation + focus model consumes `ConversationAgentRef`/`ConversationAgentStatus` and reads `ConversationItem.agent`. [2]
- The client + stream mirror these page/telemetry/interrupt/error shapes. [3]
- The server wire contract this file mirrors exactly (camelCase `to_camel`). [4]
- The stale L1 control/telemetry capability view (`controls.interrupt`). [5]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.
