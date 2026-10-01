# dashboard/src/panels/session-cockpit/conversation/TurnResultItem.tsx

## Governing Overview

[session-cockpit/conversation overview](overview.md)

## Purpose

The turn-result / error / interrupt / notice / unknown-vendor item of the harness-neutral grammar
(design §12.2). Each renders in place at the end of the relevant turn (never toast spam), and an
unknown-vendor item is preserved as LABELED evidence — never guessed into a message/tool meaning
(§6.2). Color is never the only carrier: each state carries a text label (§14.2).

## Code Commentary

### Logic

- cit:([`labelFor`], dashboard/src/panels/session-cockpit/conversation/TurnResultItem.tsx:27-44) maps `kind` to a `{ text, toneKey }`: `error` → `error`; `turn-result` splits on
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

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries are
configured. This one-to-one card therefore relies on its direct agents-remember source/tests and the
reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- The item/`unknown-vendor`-block types (`vendorType`, `safeSummary`, `evidenceRef`) narrowed here. [1]
- Streaming-safe Markdown renderer used for result detail. [2]
- The pure grouping that folds runs of identical unknown-vendor rows (per-member addressable by ordinal/evidenceRef). [3]
- The kind dispatcher that routes result items here. [4]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.
