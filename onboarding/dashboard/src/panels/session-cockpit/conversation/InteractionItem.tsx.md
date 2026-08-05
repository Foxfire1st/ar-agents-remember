# dashboard/src/panels/session-cockpit/conversation/InteractionItem.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/conversation/InteractionItem.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-26T15:40+0200 |
| lastVerifiedCommitHash | `4e5fbcf872bbc1ec2566a6ccb17276a6bad80c7f` |
| lastVerifiedCommitDate | 2026-07-26T18:40:37+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[session-cockpit/conversation overview](overview.md)

## Purpose

The interaction item of the harness-neutral grammar (design §12.2, §12.4): the historical prompt and
its resolved answer as they sit in the timeline. It is deliberately NON-LIVE — the live pending prompt
is owned and announced by the existing `InteractionBar` — so this timeline copy carries
`aria-live="off"` and never becomes an answer surface. Native or PTY text can never count as an
interaction answer. An item carrying an agent ref (a sub-agent's multiplexed
approval request) badges WHO is asking, from the bound evidence only.

## Code Commentary

### Logic

- cit:([`InteractionItem`], dashboard/src/panels/session-cockpit/conversation/InteractionItem.tsx:73-101) — The wrap sets `aria-live="off"` so the historical record never competes with the live gate
  channel for announcements.
- cit:([`InteractionItem`], dashboard/src/panels/session-cockpit/conversation/InteractionItem.tsx:73-101) — **Agent badge (R7)**: the `interaction` label now sits in a `labelRow`
  flex; when `item.agent != null`, a cyan uppercase `interaction-agent-badge` renders
  `agentLabel(item.agent)` beside it (badge styling). A parent-conversation interaction stays
  unbadged — the badge is bound evidence, never an invented attribution.
- cit:([`phaseText`], dashboard/src/panels/session-cockpit/conversation/InteractionItem.tsx:40-52) maps the item phase to `waiting for answer` / `answered` / `failed`.
- cit:([`ChoicesBlock`], dashboard/src/panels/session-cockpit/conversation/InteractionItem.tsx:54-71) renders a `choices` block's options as a marked list (`label — description`);
  `markdown`/`text` blocks flow through `MarkdownBlock`.

### Invariants And Boundaries

- This component is a read-only historical projection; it does not submit, answer, or gate. The live
  interaction authority is `InteractionBar` + `data/interactionAnswer.ts` (the gate channel) — this
  component invents no second interaction store or answer path.
- The badge renders only from the item's bound `agent` ref; an unbadged interaction is the parent
  conversation, never a guess.
- Operator text, agent-bus messages, control commands, and interaction answers remain distinct
  authority channels (the standing cockpit invariant).

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
| The item/`choices`-block types this component narrows over (incl. the `item.agent` ref). | `choices` | dashboard/src/data/conversation/types.ts:95-95 |
| The `agentLabel` precedence (nickname → role → agentPath tail → `agent <first8>`) the badge prints. | `agentLabel` | dashboard/src/data/conversation/agents.ts:30-38 |
| Streaming-safe Markdown renderer used for the prompt body. | `MarkdownBlock` | dashboard/src/panels/session-cockpit/conversation/MarkdownBlock.tsx:88-88 |
| The LIVE gate-channel interaction authority this timeline copy defers to. | `InteractionBar` | dashboard/src/panels/session-cockpit/InteractionBar.tsx:242-281 |
| The kind dispatcher that routes interaction items here. | `ConversationItemView` | dashboard/src/panels/session-cockpit/conversation/ConversationItemView.tsx:68-71 |
| The badge present/absent pinning suite. | "badges the asking agent's label when the item carries an agent ref" | dashboard/src/panels/session-cockpit/conversation/InteractionItem.test.tsx:32-39 |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-02T20:53:56+02:00 — W2-B04 curator: repaired 10 citation findings; scoped check passed.

- 2026-07-26T15:40+0200 — 260718-CHATS-L7 curator: recorded the R7 asking-agent badge — an item
  carrying an agent ref renders `agentLabel(item.agent)` in a cyan uppercase
  `interaction-agent-badge` beside the `interaction` label, from bound evidence only; a
  parent-conversation interaction stays unbadged. All pre-L7 line citations re-verified against the
  current source. The L7 source is uncommitted; lastVerified* stays as-is and closeout re-stamps
  verification.
- 2026-07-20T22:30+02:00 — 260718-CHATS-L4 curator: created the sidecar for the interaction item —
  the non-live (`aria-live="off"`) historical prompt/answer record that never becomes an answer
  surface, deferring the live gate channel to InteractionBar. Verification is pinned to the leaf base
  (`0be0099`) because the new source file is uncommitted; closeout owns its first source stamp.
