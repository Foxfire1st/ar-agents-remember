# dashboard/src/data/conversation/agents.test.ts

## Governing Overview

[data/conversation overview](overview.md)

## Purpose

The unit pins for the sub-agent roster derivation + timeline focus model.
Seven vitest suites drive the pure `agents.ts` functions through hand-built `ConversationItem`
fixtures — plus two store-level cases proving the `agentFocusBySession` LRU-survival boundary —
with no network and no DOM. The load-bearing claims pinned here: the roster vocabulary is
projection-evidence only (the ruled notice/system/agent shape), labels fall back through bound
identity evidence and never fabricate a name, and a stale focus surviving an LRU eviction recomputes
to the parent instead of being trusted.

## Code Commentary

### Logic — what each case proves and why it is required

- cit:([`isAgentRosterItem`], dashboard/src/data/conversation/agents.ts:14-18) — detects EXACTLY the
  ruled roster shape (notice + system + agent): a notice without an agent ref is an ordinary notice,
  an agent-tagged message is an agent item (not a roster row), and an assistant-role notice with an
  agent ref is not the roster shape; the negative cases add that an `agent-history:<thread>` item and
  a thread-rebound system notice are not roster seats either.
- **`agentLabel` / cit:([`shortAgentId`], dashboard/src/data/conversation/agents.test.ts:94-106)** — the precedence nickname → role → last `agentPath`
  segment → `agent <short-id>` (first 8 chars), so an unresolved identity is named by its id, never
  invented.
- cit:([`deriveAgents`], dashboard/src/data/conversation/agents.ts:71-86) — one row per roster agent in first-evidence order, ignoring
  non-roster items; the final-message preview surfaces ONLY for a terminal roster row (a running
  roster carrying a `final-message` block yields none), and the claude task_notification's terminal
  `summary` TextBlock is equally a report preview.
- cit:([`cycleAgentFocus`], dashboard/src/data/conversation/agents.ts:93-103) — ArrowRight cycles parent → agent 1 → agent 2 → parent,
  ArrowLeft the reverse; a stale focus (agent gone from the roster) is treated as the parent in both
  directions, and an empty roster always yields parent.
- cit:([`effectiveAgentFocus`], dashboard/src/data/conversation/agents.ts:106-112) — a roster-backed stored focus is kept; an unknown id (the
  evicted-agent case), `null`, and `undefined` all recompute to the parent.
- cit:([`filterItemsForFocus`], dashboard/src/data/conversation/agents.ts:119-127) — the parent view keeps parent items + roster rows and drops
  agent-tagged items; an agent view keeps only that agent's items, its roster row included (so the
  focused lane still shows its status/final report).
- cit:([`setAgentFocus`], dashboard/src/data/conversation/store.ts:69-69) — Agent focus in the store records/clears the focus OUTSIDE the
  projection: after `evict("s-1")` drops `bySession["s-1"]`, the stored focus survives (the surface
  recomputes it against the rehydrated roster via `effectiveAgentFocus` instead of re-applying it
  blindly); `null` deletes the entry, and `reset()` clears the focus map with the rest of the store.

### Invariants And Boundaries

- Fixtures build the exact ruled wire shape (`rosterItem` mints `codex-agent-<id>` notice/system
  items with `agent` set) — the same shape the backend projectors mint, so a drift in the ruled
  shape fails here first.
- `afterEach` `reset()`s the real `activeConversationStore` so the store-level cases do not leak
  state; only the store is real, everything else is a plain object fixture.

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries are
configured. This one-to-one card therefore relies on its direct agents-remember source/tests and the
reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- The roster/focus module under test. [1]
- The store whose `agentFocusBySession`/`evict`/`reset` the store-level cases drive. [2]
- The `emptyProjection` helper used to seed an evictable projection. [3]
- The wire types the fixtures build (`ConversationAgentRef`, `ConversationItem`). [4]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.

## 260727-CHATS-IM-L2 Current Delta

Negative cases now prove that `agent-history:<thread>` and thread-scoped rebound system notices do
not satisfy roster detection even when they carry an agent ref.
