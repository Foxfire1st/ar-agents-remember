# dashboard/src/data/conversation-library/types.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/conversation-library/types.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-26T15:40+02:00 |
| lastVerifiedCommitHash | `4e5fbcf872bbc1ec2566a6ccb17276a6bad80c7f` |
| lastVerifiedCommitDate | 2026-07-26T18:40:37+02:00|
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
  mints them; it echoes the server's exact tokens (the purpose-bound cursor discipline).
- **`HistoryCapabilities`** (L18-L24): per-conversation `list`/`read`/`resume`/`completeness`/
  `toolCompleteness` `FeatureCapability` states (reused from the active-side types). These drive the
  read-only preview's honest partial-history note (the preview prints the reason from the capability
  that is actually unsupported — F13).
- **`ConversationLibraryRow`** (L26-L36): one dormant row — `conversationKey`, `identityDigest`,
  `title`, optional `safeNativeIdSuffix`/`lastActivityAt`, its capability block, and
  an optional `agents` list of harness sub-agent conversations grouped under it. Each child's
  `conversationKey` is minted server-side and opens through the exact same read/open path.
- **`ConversationLibraryAgentRow`** (L38-L50): one grouped sub-agent conversation —
  its own `conversationKey`/`identityDigest`/`title` plus optional `agentPath`/`nickname`/`role`/
  `model`/`joinKey`/`safeNativeIdSuffix`/`lastActivityAt`. It carries NO `HistoryCapabilities` of its
  own; consumers inherit the parent's read-path capabilities.
- **`ConversationLibraryPage`** (L52-L59): a scope-stamped page (`harnessId`,
  `canonicalProjectScope`, `queryDigest`) of rows plus `nextCursor` for accessible paging, and
  an optional `agentsNote` — capability honesty: the exact native reason sub-agent
  conversations are (partially) unavailable on this page, when they are, never silently absent.
- **`HistoricalConversationPage`** (L61-L68): the read-only preview page — a `NativeConversationRef`,
  `ConversationItem[]` (the SAME block grammar the active surface renders), `olderCursor`/`hasOlder`,
  optional exact `totalItems`, and its own `historicalCapabilities`.
- **Open operation types** (L72-L110): `OpenPhase` (`requested`→`launching`→`catalog-wait`→`opened`/
  `retiring`/`failed`/`unknown`) and `OpenOutcome` (`pending`/`opened`/`unsupported`/`stale-identity`/
  `launch-failed`/`identity-mismatch`/`timeout-unknown`/`request-conflict`). `OpenConversationOperation`
  carries `requestId`, `requestFingerprint`, monotonic `revision`, phase/outcome, optional
  `arSessionId`/`bridgeEpoch`/`identity`/`catalogGeneration`, a `rollback` disposition, and `detail`.
- **`LibraryRouteError`** (L112-L117): the typed failure shape (`status`/`detail`/`httpStatus`/optional
  `capabilityState`) the client returns instead of guessing a refusal into success.

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
| Server-side `ConversationLibraryAgentRow` / `agents` / `agents_note` producer these types mirror. | L755-L775, L784, L799 | [models.py](agents-remember/mcp/src/agents_remember/serving/conversation/models.py) |
| The harness listers that group sub-agent rows and mint the `agents_note` (Claude: `_AGENTS_UNAVAILABLE_NOTE`; Codex: degraded-to-note listing). | L75, L235-L281 · L292-L346, L477-L500 | [library/claude.py](agents-remember/mcp/src/agents_remember/serving/conversation/library/claude.py) · [library/codex.py](agents-remember/mcp/src/agents_remember/serving/conversation/library/codex.py) |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Update History

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
