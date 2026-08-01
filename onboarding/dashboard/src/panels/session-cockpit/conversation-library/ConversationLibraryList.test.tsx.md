# dashboard/src/panels/session-cockpit/conversation-library/ConversationLibraryList.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/conversation-library/ConversationLibraryList.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-01T11:35+02:00 |
| lastVerifiedCommitHash | `e52edaf5b655f495580efd93306afdf922b19b51` |
| lastVerifiedCommitDate | 2026-08-01T11:01:51+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[session-cockpit/conversation-library overview](overview.md)

## Purpose

The regression suite for the library list's harness sub-agent grouping — the tests
that lock the nested-child-row contract and the `agentsNote` capability-honesty render. It mounts the
real `ConversationLibraryList` via `@testing-library/react` with fixture rows, so it proves the
rendered DOM and the selection payload without a server.

## Code Commentary

### Logic

Helpers (260731-EFA-L4 rewrote all three): the local `capabilities()` and `row()` builders and the
hand-written `AGENT` literal are gone. `row` is now `conversationLibraryRow` imported under that alias
from `test/fixtures/conversationWire.ts` — same parent defaults (`key-parent`, `digest-parent`,
`P4R3NT`, an all-`supported` `HistoryCapabilities` from `historyCapabilities()`) — and `AGENT` is
`conversationLibraryAgentRow({ role, safeNativeIdSuffix, lastActivityAt })`, whose base supplies the
own key `key-agent-1` and `digest-agent-1`. The branded `LibraryConversationKey` casts that used to sit
inline are now the single named mint `libraryConversationKey()` inside the builder module.
`renderList(rows, agentsNote?)` mounts the list with a spy `onSelect`, now declared
`vi.fn<(selected: ConversationLibraryRow) => void>()` so the selection assertion reads
`onSelect.mock.calls[0]?.[0]` directly instead of casting it back to `ConversationLibraryRow` — the
cast at the assertion site is what made the payload claim self-authored. `afterEach` cleans up. The
four cases prove:

- **child rows render under the parent with label + suffix** (L44-L54): `library-agent-row` carries
  the child title, the mono `…AG3NT1` suffix, and the `explorer` role badge; the parent
  `library-row` renders unchanged, without the agent badge.
- **a child selects through the same flow with its own server-minted key** (L55-L67): clicking the
  child calls `onSelect` once with a promoted row whose `conversationKey`/`identityDigest` are the
  CHILD's, `agents` is `[]` (no deeper nesting), and `capabilities` follow the parent's read path.
- **no child rows without agents** (L68-L72): a row with no `agents` renders no
  `library-agent-row` at all.
- **agentsNote verbatim when present, nothing when absent** (L73-L85): the exact note string
  renders in `library-agents-note`; with `null` the testid is absent from the DOM.

### Invariants And Boundaries

- The suite is the durable guard on the sub-agent grouping contract: a regression that drops the child-row grammar,
  fabricates a child key client-side, lets children nest, decouples the child's capabilities from the
  parent's read path, or silently swallows the `agentsNote` breaks it.
- Fixtures assert the wire honesty the list relies on: the child's key is server-minted (the test
  never constructs one through any browser-side minting path), and the note is compared
  string-for-string (verbatim, never paraphrased). Since 260731-EFA-L4 the brand is minted in exactly
  one place — `libraryConversationKey()` in `test/fixtures/conversationWire.ts`, registered as a
  sanctioned cast site in `test/wireFixtureGuard.test.ts` with its reason — rather than by an inline
  `"key-agent-1" as LibraryConversationKey` here. The brand carries no structure, so the mint is the
  only thing about these rows that a cast can still express.

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
| The list component under test (child-row grammar, `agentChildRow`, agentsNote render); imported at L14. | L14 | [ConversationLibraryList.tsx](ConversationLibraryList.tsx) |
| `ConversationLibraryRow` — now the only wire type this file imports directly (L9); `HistoryCapabilities` and `LibraryConversationKey` reach it through the builders instead. | L9 | [../../../data/conversation-library/types.ts](../../../data/conversation-library/types.ts) |
| `conversationLibraryRow` (aliased `row`), `conversationLibraryAgentRow`, `historyCapabilities`, and the single `libraryConversationKey` brand mint. | L63-L66; L155-L169; L247-L271 | [../../../test/fixtures/conversationWire.ts](../../../test/fixtures/conversationWire.ts) |
| The sanctioned-cast registry that records `as LibraryConversationKey` as a permitted site with its reason. | L158-L169 | [../../../test/wireFixtureGuard.test.ts](../../../test/wireFixtureGuard.test.ts) |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Update History

- 2026-08-01T11:35+02:00 — 260731-EFA-L4 curator: the Helpers paragraph described three fixtures that
  no longer exist, so it was rewritten. The local `capabilities()` and `row()` builders and the
  hand-written `AGENT` literal are replaced by `conversationLibraryRow` (imported as `row`),
  `conversationLibraryAgentRow` and `historyCapabilities()` from `test/fixtures/conversationWire.ts`,
  and the inline `"key-agent-1" as LibraryConversationKey` casts collapse into the single
  `libraryConversationKey()` mint, which I confirmed is registered as a sanctioned site in
  `test/wireFixtureGuard.test.ts` L158-L169 rather than merely tolerated. Also recorded the
  assertion-site change the four case bullets depend on: `onSelect` is now
  `vi.fn<(selected: ConversationLibraryRow) => void>()`, so the payload assertion reads
  `onSelect.mock.calls[0]?.[0]` instead of casting it back with
  `as ConversationLibraryRow` — the cast was what made the "promoted row" claim self-authored. All four
  described behaviours still hold verbatim; I checked the one that reads capability content
  (`selected.capabilities.completeness.state` is `"supported"`), which `historyCapabilities()` supplies
  exactly as the deleted local helper did. Suite re-run: 4 cases pass. Citation repairs — the file
  shrank 106 → 86 lines and every case range was stale: child rows L64-L73 → L44-L54; child selection
  L75-L86 → L55-L67; no-agents L88-L91 → L68-L72; agentsNote L93-L105 → L73-L85; and the wire-types row
  L9-L13 → L9, since `HistoryCapabilities` and `LibraryConversationKey` are no longer imported here at
  all. Two rows added.

- 2026-07-26T15:40+02:00 — 260718-CHATS-L7 curator: created the sidecar for the sub-agent nesting
  suite — indented child rows with label/suffix/role badges, same-flow selection with the child's
  own server-minted key (parent-inherited capabilities, no deeper nesting), no-child-rows-without-
  agents, and the verbatim/absent `agentsNote` proof. Verification is pinned to the leaf base
  (`842b487`) because the new source file is uncommitted; closeout owns its first source stamp.
