# dashboard/src/panels/session-cockpit/conversation-library/ConversationLibraryList.test.tsx

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

- **child rows render under the parent with label + suffix** (cit:(["renders agent children as indented rows with label + suffix under the parent"], dashboard/src/panels/session-cockpit/conversation-library/ConversationLibraryList.test.tsx:44-53)): `library-agent-row` carries
  the child title, the mono `…AG3NT1` suffix, and the `explorer` role badge; the parent
  `library-row` renders unchanged, without the agent badge.
- **a child selects through the same flow with its own server-minted key** (cit:(["selects a child through the same flow with the child's own server-minted key"], dashboard/src/panels/session-cockpit/conversation-library/ConversationLibraryList.test.tsx:55-66)): clicking the
  child calls `onSelect` once with a promoted row whose `conversationKey`/`identityDigest` are the
  CHILD's, `agents` is `[]` (no deeper nesting), and `capabilities` follow the parent's read path.
- **no child rows without agents** (cit:(["renders no child rows when the row carries no agents"], dashboard/src/panels/session-cockpit/conversation-library/ConversationLibraryList.test.tsx:68-71)): a row with no `agents` renders no
  `library-agent-row` at all.
- **agentsNote verbatim when present, nothing when absent** (cit:(["renders the agentsNote verbatim when present"], dashboard/src/panels/session-cockpit/conversation-library/ConversationLibraryList.test.tsx:73-85)): the exact note string
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

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries are
configured. This one-to-one card therefore relies on its direct agents-remember source/tests and the
reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- The list component under test (child-row grammar, `agentChildRow`, agentsNote render); imported at L14. [1]
- `ConversationLibraryRow` — now the only wire type this file imports directly (L9); `HistoryCapabilities` and `LibraryConversationKey` reach it through the builders instead. [2]
- The `conversationLibraryRow` fixture builder. [3]
- The `conversationLibraryAgentRow` fixture builder. [4]
- The `historyCapabilities` fixture builder. [5]
- The `libraryConversationKey` brand mint. [6]
- The sanctioned-cast registry that records "as LibraryConversationKey" as a permitted site with its reason. [7]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.
