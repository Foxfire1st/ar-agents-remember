# dashboard/src/data/conversation-library/types.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/conversation-library/types.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-20T22:30+02:00 |
| lastVerifiedCommitHash | `9e6c15d2b2bb663fcd10e26d77d0e4d2795829bd` |
| lastVerifiedCommitDate | 2026-07-20T22:32:02+02:00|
| governingOverview | `overview.md` |

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

- **Branded cursor/key types** (L14-L16): `LibraryListCursor`, `LibraryReadCursor`,
  `LibraryConversationKey` are opaque `string & { __brand }` values — the browser never parses or
  mints them; it echoes the server's exact tokens (the L9 purpose-bound cursor discipline).
- **`HistoryCapabilities`** (L18-L24): per-conversation `list`/`read`/`resume`/`completeness`/
  `toolCompleteness` `FeatureCapability` states (reused from the active-side types). These drive the
  read-only preview's honest partial-history note (the preview prints the reason from the capability
  that is actually unsupported — F13).
- **`ConversationLibraryRow`** (L26-L33): one dormant row — `conversationKey`, `identityDigest`,
  `title`, optional `safeNativeIdSuffix`/`lastActivityAt`, and its capability block.
- **`ConversationLibraryPage`** (L35-L39): a scope-stamped page (`harnessId`,
  `canonicalProjectScope`, `queryDigest`) of rows plus `nextCursor` for accessible paging.
- **`HistoricalConversationPage`** (L41-L48): the read-only preview page — a `NativeConversationRef`,
  `ConversationItem[]` (the SAME block grammar the active surface renders), `olderCursor`/`hasOlder`,
  optional exact `totalItems`, and its own `historicalCapabilities`.
- **Open operation types** (L52-L90): `OpenPhase` (`requested`→`launching`→`catalog-wait`→`opened`/
  `retiring`/`failed`/`unknown`) and `OpenOutcome` (`pending`/`opened`/`unsupported`/`stale-identity`/
  `launch-failed`/`identity-mismatch`/`timeout-unknown`/`request-conflict`). `OpenConversationOperation`
  carries `requestId`, `requestFingerprint`, monotonic `revision`, phase/outcome, optional
  `arSessionId`/`bridgeEpoch`/`identity`/`catalogGeneration`, a `rollback` disposition, and `detail`.
- **`LibraryRouteError`** (L92-L97): the typed failure shape (`status`/`detail`/`httpStatus`/optional
  `capabilityState`) the client returns instead of guessing a refusal into success.

### Invariants And Boundaries

- **Null keys are explicit, not fabricated.** Library responses keep null keys (the server does NOT
  `exclude_none`), so `nextCursor`/`olderCursor`/`safeNativeIdSuffix`/`lastActivityAt` arrive as literal
  `null` and are treated identically to absent (no fabricated value, no reassurance zero — A1/A2).
- **A library row can never become active from this module.** Only exact opened-catalog proof in the
  live session store may focus a session; the sole focus signal these types expose is
  `phase==="opened" && outcome==="opened"` on the open operation (R4/§9.4).
- The digest here (`identityDigest`) is a within-service field; L4 matches conversations by identity
  fields, never by digest equality across the L1/L2/L3 services (L4-facing precision note 4).

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
| Shared active-side types (`ConversationItem`, `FeatureCapability`, `HarnessId`, `NativeConversationRef`) reused here. | L7-L12 | [../conversation/types.ts](../conversation/types.ts) |
| The client that returns these types as or-null reads / typed open evidence. | — | [client.ts](client.ts) |
| The store that holds the paged list, preview, and open-operation state over these types. | — | [store.ts](store.ts) |
| The wire authority these types mirror (native library routes + models). | — | [library/api.py](agents-remember/mcp/src/agents_remember/serving/conversation/library/api.py) · [models.py](agents-remember/mcp/src/agents_remember/serving/conversation/models.py) |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Update History

- 2026-07-20T22:30+02:00 — 260718-CHATS-L4 curator: created the sidecar for the dormant native-library
  wire mirror — branded cursors/keys, per-conversation history capabilities, list/preview page shapes,
  and the caller-stable open-operation phase/outcome grammar, with explicit-null and never-active-row
  semantics. Verification is pinned to the leaf base (`0be0099`) because the new source file is
  uncommitted; closeout owns its first source stamp.
