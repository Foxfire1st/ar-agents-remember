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

- The wrap sets `aria-live="off"` (L75) so the historical record never competes with the live gate
  channel for announcements.
- **Agent badge (R7)** (L76-L83): the `interaction` label now sits in a `labelRow`
  flex; when `item.agent != null`, a cyan uppercase `interaction-agent-badge` renders
  `agentLabel(item.agent)` beside it (badge styling L23-L34). A parent-conversation interaction stays
  unbadged — the badge is bound evidence, never an invented attribution.
- `phaseText` (L40-L52) maps the item phase to `waiting for answer` / `answered` / `failed`.
- `ChoicesBlock` (L54-L71) renders a `choices` block's options as a marked list (`label — description`);
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

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | `system/sources.md` checked | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The item/`choices`-block types this component narrows over (incl. the `item.agent` ref). | L9 | [../../../data/conversation/types.ts](../../../data/conversation/types.ts) |
| The `agentLabel` precedence (nickname → role → agentPath tail → `agent <first8>`) the badge prints. | L8 | [../../../data/conversation/agents.ts](../../../data/conversation/agents.ts) |
| Streaming-safe Markdown renderer used for the prompt body. | L10, L87-L91 | [MarkdownBlock.tsx](MarkdownBlock.tsx) |
| The LIVE gate-channel interaction authority this timeline copy defers to. | — | [../InteractionBar.tsx](../InteractionBar.tsx) |
| The kind dispatcher that routes interaction items here. | — | [ConversationItemView.tsx](ConversationItemView.tsx) |
| The badge present/absent pinning suite. | — | [InteractionItem.test.tsx](InteractionItem.test.tsx) |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Update History

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
