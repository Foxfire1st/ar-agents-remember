# dashboard/src/data/conversation-library/types.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/conversation-library/types.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-26T15:40+02:00 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
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

## Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries are
configured. This one-to-one card therefore relies on its direct agents-remember source/tests and the
reviewed task evidence for any current behavioral claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Shared active-side types (`ConversationItem`, `FeatureCapability`, `HarnessId`, `NativeConversationRef`) reused here. | `ConversationItem`; `FeatureCapability`; `HarnessId`; `NativeConversationRef` | dashboard/src/data/conversation/types.ts:10-10; dashboard/src/data/conversation/types.ts:12-17; dashboard/src/data/conversation/types.ts:158-176; dashboard/src/data/conversation/types.ts:234-244 |
| The client that returns these types as or-null reads / typed open evidence. | `fetchLibraryList`; `openConversation` | dashboard/src/data/conversation-library/client.ts:36-54; dashboard/src/data/conversation-library/client.ts:127-135 |
| The store that holds the paged list, preview, and open-operation state over these types. | `conversationLibraryStore` | dashboard/src/data/conversation-library/store.ts:77-84 |
| The native library route authority these types mirror. | `api_library_list` | mcp/src/agents_remember/serving/conversation/library/api.py:109-130 |
| The wire model authority these types mirror. | `ConversationLibraryPage` | mcp/src/agents_remember/serving/conversation/models.py:813-819 |
| Server-side `ConversationLibraryAgentRow` / `agents` / `agents_note` producer these types mirror. | `ConversationLibraryAgentRow` | mcp/src/agents_remember/serving/conversation/models.py:775-794 |
| The Claude harness lister's unavailable-agent note. | `_AGENTS_UNAVAILABLE_NOTE` | mcp/src/agents_remember/serving/conversation/library/claude.py:75-77 |
| The Codex harness lister's degraded/truncated agent-page note. | `_agent_page` | mcp/src/agents_remember/serving/conversation/library/codex.py:477-500 |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-02T23:59:26+02:00 — L6 Wave 2 duplicate-range correction: removed 3 repeated path:start-end Citation objects from 2 same-claim citation group(s) at card line(s) 56, 91; retained the first occurrence/order, all non-repeated anchor coverage and source ranges; scoped non-fixing result 0.
- 2026-08-02T21:14+02:00 — W2-B03 curator: resolved 22 initial citation findings (6 anchor, 8 prose, 8 source); scoped recheck PASS (0 findings). Verification metadata unchanged.

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired the harness-lister citation. `_AGENTS_UNAVAILABLE_NOTE`
  is still `claude.py` L75, but the grouping/note-minting body moved to `ClaudeConversationLibrary._rows`
  at L235-L281 (was L258-L283). On the Codex side the equivalent material is now split: `list` groups the
  agent rows and appends the nested-sub-agent note at L292-L346, and `_agent_page` mints the
  degraded/truncated note at L477-L500 (was the single range L283-L327). All four ranges read back.
- 2026-07-26T15:40+02:00 — 260718-CHATS-L7 curator: refreshed for the harness sub-agent grouping —
  `ConversationLibraryRow.agents`, the new capability-free `ConversationLibraryAgentRow`, and the
  page-level `agentsNote` capability-honesty field (the exact native reason, rendered verbatim,
  never silently absent); downstream citations re-stamped against the post-L7 source. The L7 source
  is uncommitted, so lastVerifiedCommit* stays on the prior stamp and closeout re-stamps verification.
- 2026-07-20T22:30+02:00 — 260718-CHATS-L4 curator: created the sidecar for the dormant native-library
  wire mirror — branded cursors/keys, per-conversation history capabilities, list/preview page shapes,
  and the caller-stable open-operation phase/outcome grammar, with explicit-null and never-active-row
  semantics. Verification is pinned to the leaf base (`0be0099`) because the new source file is
  uncommitted; closeout owns its first source stamp.
