# dashboard/src/data/conversation/types.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/conversation/types.ts`       |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-26T15:40+02:00                           |
| lastVerifiedCommitHash | `4e5fbcf872bbc1ec2566a6ccb17276a6bad80c7f`       |
| lastVerifiedCommitDate | 2026-07-26T18:40:37+02:00|
| governingOverview      | `overview.md`                                    |

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

- `HarnessId` (`codex`/`claude`/`pi`) and `NativeConversationRef` (`harnessId`, `vendorConversationId`,
  `projectScope`, `identityDigest`); `ActiveConversationRef` extends it with `arSessionId` + `bridgeEpoch`
  — the pair the reducer matches identity on.
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

## Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries are
configured. This one-to-one card therefore relies on its direct agents-remember source/tests and the
reviewed task evidence for any current behavioral claim.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | `system/sources.md` checked | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The reducer consumes these item/block/event/status types. | L17-L313 | [reducer.ts](reducer.ts) |
| The roster derivation + focus model consumes `ConversationAgentRef`/`ConversationAgentStatus` and reads `ConversationItem.agent`. | L140-L156 · L172 | [agents.ts](agents.ts) |
| The client + stream mirror these page/telemetry/interrupt/error shapes. | L8-L15 | [client.ts](client.ts) · [stream.ts](stream.ts) |
| The server wire contract this file mirrors exactly (camelCase `to_camel`). | — | [models.py](agents-remember/mcp/src/agents_remember/serving/conversation/models.py) |
| The stale L1 control/telemetry capability view (`controls.interrupt`). | L154-L167 | [active/capabilities.py](agents-remember/mcp/src/agents_remember/serving/conversation/active/capabilities.py) |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Update History

- 2026-07-26T15:40+02:00 — 260718-CHATS-L7 curator: recorded the additive harness sub-agent
  identity (D2/D3) — the `ConversationAgentStatus` union, `ConversationAgentRef`
  (`agentId` + evidence-bound `agentPath`/`nickname`/`role`/`joinKey`/`parentAgentId` + `status`),
  and the optional `ConversationItem.agent` (absent = parent conversation). Purely additive; no
  existing wire shape changed. Source uncommitted; closeout re-stamps verification.
- 2026-07-20T22:30+02:00 — 260718-CHATS-L4 curator: created the sidecar for the SC1 wire-grammar
  browser mirror — the consumed-only item/block/status/capability/page/event/telemetry/interrupt types,
  the field-matched identity, the branded cursors, and the nullable hosted-codex `turn.turnId`.
  Verification is pinned to the leaf base (`0be0099`) because the new source file is uncommitted;
  closeout owns its first source stamp.
