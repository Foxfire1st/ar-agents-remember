# dashboard/src/data/conversation/agents.test.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/conversation/agents.test.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-26T15:40+02:00 |
| lastVerifiedCommitHash | `4e5fbcf872bbc1ec2566a6ccb17276a6bad80c7f` |
| lastVerifiedCommitDate | 2026-07-26T18:40:37+02:00|
| governingOverview | `overview.md` |

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

- **`isAgentRosterItem` (L53-L69)** — detects EXACTLY the ruled roster shape (notice + system +
  agent): a notice without an agent ref is an ordinary notice, an agent-tagged message is an agent
  item (not a roster row), and an assistant-role notice with an agent ref is not the roster shape.
- **`agentLabel` / `shortAgentId` (L71-L83)** — the precedence nickname → role → last `agentPath`
  segment → `agent <short-id>` (first 8 chars), so an unresolved identity is named by its id, never
  invented.
- **`deriveAgents` (L85-L116)** — one row per roster agent in first-evidence order, ignoring
  non-roster items; the final-message preview surfaces ONLY for a terminal roster row (a running
  roster carrying a `final-message` block yields none), and the claude task_notification's terminal
  `summary` TextBlock is equally a report preview.
- **`cycleAgentFocus` (L118-L139)** — ArrowRight cycles parent → agent 1 → agent 2 → parent,
  ArrowLeft the reverse; a stale focus (agent gone from the roster) is treated as the parent in both
  directions, and an empty roster always yields parent.
- **`effectiveAgentFocus` (L141-L149)** — a roster-backed stored focus is kept; an unknown id (the
  evicted-agent case), `null`, and `undefined` all recompute to the parent.
- **`filterItemsForFocus` (L151-L172)** — the parent view keeps parent items + roster rows and drops
  agent-tagged items; an agent view keeps only that agent's items, its roster row included (so the
  focused lane still shows its status/final report).
- **Agent focus in the store (L174-L212)** — `setAgentFocus` records/clears the focus OUTSIDE the
  projection: after `evict("s-1")` drops `bySession["s-1"]`, the stored focus survives (the surface
  recomputes it against the rehydrated roster via `effectiveAgentFocus` instead of re-applying it
  blindly); `null` deletes the entry, and `reset()` clears the focus map with the rest of the store.

### Invariants And Boundaries

- Fixtures build the exact ruled wire shape (`rosterItem` mints `codex-agent-<id>` notice/system
  items with `agent` set) — the same shape the backend projectors mint, so a drift in the ruled
  shape fails here first.
- `afterEach` `reset()`s the real `activeConversationStore` so the store-level cases do not leak
  state; only the store is real, everything else is a plain object fixture.

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
| The roster/focus module under test. | L8-L16 | [agents.ts](agents.ts) |
| The store whose `agentFocusBySession`/`evict`/`reset` the store-level cases drive. | L18 · L174-L212 | [store.ts](store.ts) |
| The `emptyProjection` helper used to seed an evictable projection. | L17 · L186-L198 | [reducer.ts](reducer.ts) |
| The wire types the fixtures build (`ConversationAgentRef`, `ConversationItem`). | L19 · L21-L51 | [types.ts](types.ts) |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Update History

- 2026-07-26T15:40+02:00 — 260718-CHATS-L7 curator: created the sidecar for the roster/focus unit
  pins — the ruled roster shape, the evidence-bound label precedence, terminal-only final-message
  previews (codex `final-message`, claude `summary`), both focus-cycle directions with the
  stale-id-to-parent recompute, the focus filter lanes, and the store-level LRU-survival + reset
  pins for `agentFocusBySession`. Verification is pinned to the leaf base (`842b487`) because the
  new source file is uncommitted; closeout owns its first source stamp.
