# dashboard/src/data/conversation/agents.ts

## Governing Overview

[data/conversation overview](overview.md)

## Purpose

The **sub-agent roster derivation + timeline focus model** for the harness
sub-agent conversations slice. Everything here is computed from projection evidence ONLY: the
backend mints ONE roster item per sub-agent on the parent timeline (codex `codex-agent-<threadId>`,
claude `claude-agent-<taskId>`; kind `notice`, role `system`, `agent` set — never optimistic, every
upsert bound to one concrete piece of collab/lifecycle evidence), and this module reads exactly that
roster — no optimistic rows, no polling, no fabricated identity. It is a pure function module in the
same spirit as the reducer: the store holds the raw focus id, the surfaces hold none of this logic,
and the tests pin every rule.

## Code Commentary

### Logic

- cit:([`isAgentRosterItem`], dashboard/src/data/conversation/agents.ts:14-18) — roster detection, the ruled wire shape: `kind === "notice"`
  AND `role === "system"` AND `agent != null`. A plain notice, an agent-tagged message, or an
  assistant-role notice are all NOT roster rows.
- cit:([`shortAgentId`], dashboard/src/data/conversation/agents.ts:21-23) — the first 8 chars of the native agent id, the fallback fragment.
- cit:([`agentLabel`], dashboard/src/data/conversation/agents.ts:30-38) — display-label precedence (R7): `nickname` → `role` → the last
  non-empty `agentPath` segment → `agent <short-id>`. Every fallback is bound evidence; the last
  resort names the id, never a fabricated name.
- cit:([`isTerminalAgentStatus`], dashboard/src/data/conversation/agents.ts:41-43) — `completed`/`interrupted`/`failed`; only these may surface a
  final-message preview.
- cit:([`finalMessageOf`], dashboard/src/data/conversation/agents.ts:50-56) — the terminal roster row's final report preview: the
  codex `final-message` TextBlock or the claude task_notification's terminal `summary` TextBlock
  (first non-empty text block, in that order). An in-flight roster's transient labels are not a
  report.
- cit:([`ConversationAgentView`], dashboard/src/data/conversation/agents.ts:58-64) — the agents-area row: `agentId`, `label`, `status`, optional
  `finalMessage` (absent while running/registered/unknown).
- cit:([`deriveAgents`], dashboard/src/data/conversation/agents.ts:71-86) — one view per agent in first-evidence order; later roster upserts
  for the same agent REPLACE the row, and a previously-captured `finalMessage` is preserved across
  an upsert that carries none (`finalMessage ?? existing?.finalMessage`).
- cit:([`cycleAgentFocus`], dashboard/src/data/conversation/agents.ts:93-103) — the Claude Code agents-view
  precedent: parent (`null`) → agent 1 → … → agent N → parent, in both directions. A focus naming an
  agent the roster no longer carries (a stale survivor of an LRU eviction/rehydrate) resolves to
  position 0 — the parent — the honest recompute. Empty roster always yields parent.
- cit:([`effectiveAgentFocus`], dashboard/src/data/conversation/agents.ts:106-112) — the store's raw focus id recomputed against
  the live roster: an unknown/evicted agent id falls back to parent; `null`/`undefined` stays parent.
- cit:([`filterItemsForFocus`], dashboard/src/data/conversation/agents.ts:119-127) — the timeline filter (R7): the parent view keeps
  parent items PLUS the roster rows (never agent-tagged items); an agent view keeps that agent's own
  items by `agent.agentId` match — which includes its roster row, so the focused lane still shows
  its status/final report.

### Conventions

- Pure functions over `readonly ConversationItem[]`; no store import, no side effects — the same
  testable-core idiom as `reducer.ts`.
- The store (`agentFocusBySession`) holds ONLY the raw id; every read recomputes through
  `effectiveAgentFocus`, so nothing downstream ever trusts a stale focus.

### Invariants And Boundaries

- **Projection evidence only.** The roster is minted backend-side from bound collab/join evidence;
  this module never authors a roster row, never polls, and never fabricates an identity — an
  unresolved agent is `agent <short-id>`.
- **Terminal-only previews.** A `finalMessage` exists only on a terminal roster row; a running or
  registered agent surfaces no report preview.
- **Stale focus resolves to parent.** Both `cycleAgentFocus` and `effectiveAgentFocus` treat an
  unknown id as the parent conversation rather than trusting it (the LRU eviction/rehydrate case).
- **Parent view keeps the roster visible.** Filtering to the parent drops agent-tagged items but
  keeps the notice/system roster rows, so the status strip is never hidden by the filter.

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries are
configured. This one-to-one card therefore relies on its direct agents-remember source/tests and the
reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- The wire types this module reads (`ConversationAgentRef`/`ConversationAgentStatus`, `ConversationItem.agent`). [1]
- The store whose `agentFocusBySession` this module's `effectiveAgentFocus` revalidates. [2]
- The codex roster mint: one `codex-agent-<threadId>` notice/system item per agent, upserted across the lifecycle, never optimistic. [3]
- The claude roster mint: `claude-agent-<taskId>` from the task_* frames (with the join-key tool upsert), terminal summary as a "summary: str" TextBlock. [4]
- The surface that cycles/filters by this model (ArrowLeft/Right, Esc, focus bar). [5]
- The roster strip rendering `ConversationAgentView` rows. [6]
- The agent badge rendering `agentLabel`. [7]
- The unit pins for every rule above. [8]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.

## 260727-CHATS-IM-L2 Current Delta

`isAgentRosterItem` now recognizes only explicit `codex-agent-` and `claude-agent-` notice ids.
An arbitrary system notice carrying an agent ref is content, not roster authority. This prevents
selected-child history state and rebound notices from appearing as extra seats.
