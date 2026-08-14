# dashboard/src/data/conversation/agents.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/conversation/agents.ts`      |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-07-30T12:51+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`       |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `overview.md`                                    |

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
| The wire types this module reads (`ConversationAgentRef`/`ConversationAgentStatus`, `ConversationItem.agent`). | `ConversationAgentRef`; `ConversationAgentStatus`; `ConversationItem` | dashboard/src/data/conversation/types.ts:140-146; dashboard/src/data/conversation/types.ts:148-156; dashboard/src/data/conversation/types.ts:158-176 |
| The store whose `agentFocusBySession` this module's `effectiveAgentFocus` revalidates. | "agentFocusBySession: Record<string" | dashboard/src/data/conversation/store.ts:61-61; dashboard/src/data/conversation/store.ts:87-87; dashboard/src/data/conversation/store.ts:127-130 |
| The codex roster mint: one `codex-agent-<threadId>` notice/system item per agent, upserted across the lifecycle, never optimistic. |"def _roster_item("; "item_id=f\"codex-agent-{thread_id}\","|mcp/src/agents_remember/serving/conversation/projectors/_codex_collab.py:103-103; mcp/src/agents_remember/serving/conversation/projectors/_codex_collab.py:120-120|
| The claude roster mint: `claude-agent-<taskId>` from the task_* frames (with the join-key tool upsert), terminal summary as a "summary: str" TextBlock. | "def _task_lifecycle_blocks("; "summary: str" | mcp/src/agents_remember/serving/conversation/projectors/claude.py:496-511 |
| The surface that cycles/filters by this model (ArrowLeft/Right, Esc, focus bar). | "cycleAgentFocus" | dashboard/src/panels/session-cockpit/conversation/ConversationSurface.tsx:20-20; dashboard/src/panels/session-cockpit/conversation/ConversationSurface.tsx:208-216 |
| The roster strip rendering `ConversationAgentView` rows. | "import type { ConversationAgentView } from \"../../../data/conversation/agents\";" | dashboard/src/panels/session-cockpit/conversation/AgentsArea.tsx:18-19 |
| The agent badge rendering `agentLabel`. | `agentLabel` | dashboard/src/panels/session-cockpit/conversation/InteractionItem.tsx:73-81 |
| The unit pins for every rule above. | `isAgentRosterItem`; `deriveAgents`; `cycleAgentFocus` | dashboard/src/data/conversation/agents.test.ts:53-60; dashboard/src/data/conversation/agents.test.ts:108-119; dashboard/src/data/conversation/agents.test.ts:141-150 |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## 260727-CHATS-IM-L2 Current Delta

`isAgentRosterItem` now recognizes only explicit `codex-agent-` and `claude-agent-` notice ids.
An arbitrary system notice carrying an agent ref is content, not roster authority. This prevents
selected-child history state and rebound notices from appearing as extra seats.

## Update History

- 2026-08-03T03:56+02:00 — 260731-EFA-L6 W3-B10 curator: anchored 6 table citations and 1 prose citation, normalized 6 source paths, and corrected 2 narrow extents to rendered/constructed evidence; no unresolved Tier-3 claims.

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 2 cross-file line citations that moved
  when the projectors were refactored. The codex roster mint (`_roster_item`, now taking an
  `ItemPlacement`) moved to `codex.py` L722-L753; the claude roster mint was decomposed out of one
  monolithic `_map_task_lifecycle` into `claude.py` L305-L385 plus the extracted
  `_task_lifecycle_blocks` (L496-L511, where the `summary` TextBlock is appended) and
  `_agent_identity_tag_item` (L514-L554, the join-key tool-call upsert). Both claims re-verified
  against the current source; no claim text changed.

- 2026-07-30T12:51+02:00 — 260727-CHATS-IM-L2 curator: narrowed roster detection to the
  backend's explicit `codex-agent-`/`claude-agent-` identities. Agent-tagged child-history and
  rebound system notices no longer create duplicate seats. Verification metadata remains pinned
  until closeout.

- 2026-07-26T15:40+02:00 — 260718-CHATS-L7 curator: created the sidecar for the sub-agent roster
  derivation + timeline focus model (R7) — the ruled roster shape (notice/system/agent), the
  evidence-bound label precedence, terminal-only final-message previews, first-evidence-order
  `deriveAgents` with upsert replacement, the parent↔agents focus cycle, the honest stale-focus
  recompute, and the focus filter that keeps the roster row in its own lane. Verification is pinned
  to the leaf base (`842b487`) because the new source file is uncommitted; closeout owns its first
  source stamp.
