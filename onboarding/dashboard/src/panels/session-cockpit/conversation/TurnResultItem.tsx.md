# dashboard/src/panels/session-cockpit/conversation/TurnResultItem.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/conversation/TurnResultItem.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-21T05:30+02:00 |
| lastVerifiedCommitHash | `1119b64ff1564c5fc76fd518f88e529535c04b34` |
| lastVerifiedCommitDate | 2026-07-21T08:14:40+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[session-cockpit/conversation overview](overview.md)

## Purpose

The turn-result / error / interrupt / notice / unknown-vendor item of the harness-neutral grammar
(design §12.2). Each renders in place at the end of the relevant turn (never toast spam), and an
unknown-vendor item is preserved as LABELED evidence — never guessed into a message/tool meaning
(§6.2). Color is never the only carrier: each state carries a text label (§14.2).

## Code Commentary

### Logic

- `labelFor` (L31) maps `kind` to a `{ text, toneKey }`: `error` → `error`; `turn-result` splits on
  phase into `interrupted` / `turn failed` / `turn complete`; `notice`/`telemetry` → neutral;
  `unknown-vendor` → `unknown vendor event`. The tone classes (L22) carry neutral/error/interrupted/
  done color, always alongside the text label. **FB7.4/A8 (260718-CHATS-L5P):** the label is now a dim
  lowercase FLOW line prefixed with `· ` (e.g. `· turn complete`) — `tagBase` dropped the boxed
  uppercase/letterspaced chip (border, `textTransform`, padding) for a plain sized span; the tone class
  still sets the color but the word is always present.
- An `unknown-vendor` block renders `vendorType: safeSummary` on the head line and its `evidenceRef`
  as a monospace `evidence <ref>` line (L75-L82, `data-testid="unknown-vendor-evidence"`) — the
  honest preserved reference, so a collapsed run (see `collapse.ts`) can still address each member.
- `markdown`/`text` blocks flow through `MarkdownBlock`.

### Invariants And Boundaries

- An unknown-vendor event is preserved as labeled evidence with its `evidenceRef`; it is never
  dropped and never reinterpreted as a known kind (the projector that emits these is L1's concern).
- The interrupt result (`turn-result` at `phase === "interrupted"`) is the rendered evidence a
  successful stop produces — the interrupt hook announces settlement separately (see
  `useConversationControls.ts`).

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
| The item/`unknown-vendor`-block types (`vendorType`, `safeSummary`, `evidenceRef`) narrowed here. | L7 | [../../../data/conversation/types.ts](../../../data/conversation/types.ts) |
| Streaming-safe Markdown renderer used for result detail. | L8 | [MarkdownBlock.tsx](MarkdownBlock.tsx) |
| The pure grouping that folds runs of identical unknown-vendor rows (per-member addressable by ordinal/evidenceRef). | — | [collapse.ts](collapse.ts) |
| The kind dispatcher that routes result items here. | — | [ConversationItemView.tsx](ConversationItemView.tsx) |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Update History

- 2026-07-21T05:30+02:00 — 260718-CHATS-L5P curator: recorded the FB7.4/A8 flow-line restyle — the
  turn-boundary label is now `· turn complete` dim lowercase (tone class keeps the color), replacing the
  boxed uppercase web chip. Kind mapping + unknown-vendor evidence preservation unchanged. Verification
  pinned to the leaf base (`352d5cd`) until closeout stamps the candidate commit.
- 2026-07-20T22:30+02:00 — 260718-CHATS-L4 curator: created the sidecar for the turn-result item —
  labeled turn-complete/failed/interrupted/notice states (text plus color) and unknown-vendor events
  preserved as labeled evidence with their evidenceRef. Verification is pinned to the leaf base
  (`0be0099`) because the new source file is uncommitted; closeout owns its first source stamp.
