# dashboard/src/panels/session-cockpit/conversation/InteractionItem.tsx

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

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries are
configured. This one-to-one card therefore relies on its direct agents-remember source/tests and the
reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- The item/`choices`-block types this component narrows over (incl. the `item.agent` ref). [1]
- The `agentLabel` precedence (nickname → role → agentPath tail → `agent <first8>`) the badge prints. [2]
- Streaming-safe Markdown renderer used for the prompt body. [3]
- The LIVE gate-channel interaction authority this timeline copy defers to. [4]
- The kind dispatcher that routes interaction items here. [5]
- The badge present/absent pinning suite. [6]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.
