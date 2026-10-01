# dashboard/src/data/conversation-library/types.ts

## Governing Overview

[data/conversation-library overview](overview.md)

## Purpose

The browser mirror of the landed native-library wire grammar (`serving/conversation/library/api.py` +
`models.py`), for the DORMANT previous-conversation history side of structured Chats (design §4.4,
§11.2). These are read-only, consumed-only types: a `ConversationLibraryRow` is native history, NEVER
a live AR session, and this module carries no field that could mark one active. It is the sibling of
the active-side `../conversation/types.ts`; the two projections are deliberately separate authorities
(R1/R4).

## Code Commentary

### Logic

- **Branded cursor/key types**: `LibraryListCursor`, `LibraryReadCursor`,
  `LibraryConversationKey` are opaque `string & { __brand }` values — the browser never parses or
  mints them; it echoes the server's exact tokens (the purpose-bound cursor discipline). cit:([`LibraryListCursor`, `LibraryReadCursor`, `LibraryConversationKey`], dashboard/src/data/conversation-library/types.ts:14-16)
- **`HistoryCapabilities`**: per-conversation `list`/`read`/`resume`/`completeness`/
  `toolCompleteness` `FeatureCapability` states (reused from the active-side types). These drive the
  read-only preview's honest partial-history note (the preview prints the reason from the capability
  that is actually unsupported — F13. cit:([`HistoryCapabilities`], dashboard/src/data/conversation-library/types.ts:18-24)
- **`ConversationLibraryRow`**: one dormant row — `conversationKey`, `identityDigest`,
  `title`, optional `safeNativeIdSuffix`/`lastActivityAt`, its capability block, and
  an optional `agents` list of harness sub-agent conversations grouped under it. Each child's
  `conversationKey` is minted server-side and opens through the exact same read/open path. cit:([`ConversationLibraryRow`], dashboard/src/data/conversation-library/types.ts:26-36)
- **`ConversationLibraryAgentRow`**: one grouped sub-agent conversation —
  its own `conversationKey`/`identityDigest`/`title` plus optional `agentPath`/`nickname`/`role`/
  `model`/`joinKey`/`safeNativeIdSuffix`/`lastActivityAt`. It carries NO `HistoryCapabilities` of its
  own; consumers inherit the parent's read-path capabilities. cit:([`ConversationLibraryAgentRow`], dashboard/src/data/conversation-library/types.ts:39-50)
- **`ConversationLibraryPage`**: a scope-stamped page (`harnessId`,
  `canonicalProjectScope`, `queryDigest`) of rows plus `nextCursor` for accessible paging, and
  an optional `agentsNote` — capability honesty: the exact native reason sub-agent
  conversations are (partially) unavailable on this page, when they are, never silently absent. cit:([`ConversationLibraryPage`], dashboard/src/data/conversation-library/types.ts:52-59)
- **`HistoricalConversationPage`**: the read-only preview page — a `NativeConversationRef`,
  `ConversationItem[]` (the SAME block grammar the active surface renders), `olderCursor`/`hasOlder`,
  optional exact `totalItems`, and its own `historicalCapabilities`. cit:([`HistoricalConversationPage`], dashboard/src/data/conversation-library/types.ts:61-68)
- **Open operation types**: `OpenPhase` (`requested`→`launching`→`catalog-wait`→`opened`/
  `retiring`/`failed`/`unknown`) and `OpenOutcome` (`pending`/`opened`/`unsupported`/`stale-identity`/
  `launch-failed`/`identity-mismatch`/`timeout-unknown`/`request-conflict`). `OpenConversationOperation`
  carries `requestId`, `requestFingerprint`, monotonic `revision`, phase/outcome, optional
  `arSessionId`/`bridgeEpoch`/`identity`/`catalogGeneration`, a `rollback` disposition, and `detail`. cit:([`OpenPhase`, `OpenOutcome`, `OpenConversationOperation`], dashboard/src/data/conversation-library/types.ts:72-79; dashboard/src/data/conversation-library/types.ts:81-89; dashboard/src/data/conversation-library/types.ts:91-110)
- **`LibraryRouteError`**: the typed failure shape (`status`/`detail`/`httpStatus`/optional
  `capabilityState`) the client returns instead of guessing a refusal into success. cit:([`LibraryRouteError`], dashboard/src/data/conversation-library/types.ts:112-117)

### Invariants And Boundaries

- **Null keys are explicit, not fabricated.** Library responses keep null keys (the server does NOT
  `exclude_none`), so `nextCursor`/`olderCursor`/`safeNativeIdSuffix`/`lastActivityAt` arrive as literal
  `null` and are treated identically to absent (no fabricated value, no reassurance zero — A1/A2).
- **A library row can never become active from this module.** Only exact opened-catalog proof in the
  live session store may focus a session; the sole focus signal these types expose is
  `phase==="opened" && outcome==="opened"` on the open operation (R4/§9.4).
- The digest here (`identityDigest`) is a within-service field; the active projection matches
  conversations by identity fields, never by digest equality across the L1/L2/L3 services (precision
  note 4).
- **Agent grouping is server-minted and honestly reported.** The browser never
  fabricates a child row or its key — `agents` arrives grouped under the parent with a server-minted
  `conversationKey`, and a child carries no capabilities block (the parent's read path applies). When
  the harness cannot (fully) list agent conversations, the page carries the exact native reason in
  `agentsNote`; consumers must render it verbatim, never drop it silently.

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries are
configured. This one-to-one card therefore relies on its direct agents-remember source/tests and the
reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- Shared active-side types (`ConversationItem`, `FeatureCapability`, `HarnessId`, `NativeConversationRef`) reused here. [1]
- The client that returns these types as or-null reads / typed open evidence. [2]
- The store that holds the paged list, preview, and open-operation state over these types. [3]
- The native library route authority these types mirror. [4]
- The wire model authority these types mirror (moved to `models/conversations/` by L9). [5]
- Server-side `ConversationLibraryAgentRow` / `agents` / `agents_note` producer these types mirror. [6]
- The Claude harness lister's unavailable-agent note. [7]
- The Codex harness lister's degraded/truncated agent-page note. [8]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.
