# dashboard/src/panels/session-cockpit/conversation/InteractionItem.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/conversation/InteractionItem.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-20T22:30+02:00 |
| lastVerifiedCommitHash | `9e6c15d2b2bb663fcd10e26d77d0e4d2795829bd` |
| lastVerifiedCommitDate | 2026-07-20T22:32:02+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[session-cockpit/conversation overview](overview.md)

## Purpose

The interaction item of the harness-neutral grammar (design §12.2, §12.4): the historical prompt and
its resolved answer as they sit in the timeline. It is deliberately NON-LIVE — the live pending prompt
is owned and announced by the existing `InteractionBar` — so this timeline copy carries
`aria-live="off"` and never becomes an answer surface. Native or PTY text can never count as an
interaction answer.

## Code Commentary

### Logic

- The wrap sets `aria-live="off"` (L61) so the historical record never competes with the live gate
  channel for announcements.
- `phaseText` (L26) maps the item phase to `waiting for answer` / `answered` / `failed`.
- `ChoicesBlock` (L40) renders a `choices` block's options as a marked list (`label — description`);
  `markdown`/`text` blocks flow through `MarkdownBlock`.

### Invariants And Boundaries

- This component is a read-only historical projection; it does not submit, answer, or gate. The live
  interaction authority is `InteractionBar` + `data/interactionAnswer.ts` (the gate channel) — L4
  invents no second interaction store or answer path.
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
| The item/`choices`-block types this component narrows over. | L7 | [../../../data/conversation/types.ts](../../../data/conversation/types.ts) |
| Streaming-safe Markdown renderer used for the prompt body. | L8, L66 | [MarkdownBlock.tsx](MarkdownBlock.tsx) |
| The LIVE gate-channel interaction authority this timeline copy defers to. | — | [../InteractionBar.tsx](../InteractionBar.tsx) |
| The kind dispatcher that routes interaction items here. | — | [ConversationItemView.tsx](ConversationItemView.tsx) |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Update History

- 2026-07-20T22:30+02:00 — 260718-CHATS-L4 curator: created the sidecar for the interaction item —
  the non-live (`aria-live="off"`) historical prompt/answer record that never becomes an answer
  surface, deferring the live gate channel to InteractionBar. Verification is pinned to the leaf base
  (`0be0099`) because the new source file is uncommitted; closeout owns its first source stamp.
