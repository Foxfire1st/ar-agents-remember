# dashboard/src/panels/session-cockpit/conversation/ToolItem.tsx

## Governing Overview

[session-cockpit/conversation overview](overview.md)

## Purpose

The tool item of the harness-neutral grammar (design §12.2, §12.4): ONE stable-ID row that recomposes
in place across start → progress → result (the reducer upserts the same `itemId`, so a failure never
spawns a second row). It shows a verb-phrase head with a phase accent, clamps long output behind a
real disclosure button, and routes diff content to `DiffBlock`.

## Code Commentary

### Logic

- cit:([`verbPhrase`], dashboard/src/panels/session-cockpit/conversation/ToolItem.tsx:52-56) reads the `tool-input` block's `summary` for the head; falls back to `tool
  result`/`tool call` by `kind`. The head carries the phrase in `title` for the full value.
- cit:([`phaseClass`], dashboard/src/panels/session-cockpit/conversation/ToolItem.tsx:42-50) is a STATIC per-phase accent map (pending/streaming/waiting/completed/failed/
  interrupted/unknown). Color is never the only carrier — the phase word itself is always rendered
  (`data-testid="tool-phase"`, §14.2).
- **FB7.4 gutter grammar (260718-CHATS-L5P):** the head is now Claude Code / Toad tool grammar — a
  `●` `gutterDot` (phase-colored, `aria-hidden`) + the verb (`ink`, no longer cyan) + a dim lowercase
  `phaseWord` — NOT a bordered uppercase `phaseTag` chip. The output region adopts Toad's ShellResult
  idiom: `borderRadius:0` + a `borderLeft` 2px wash (the `└` relationship) + `marginInlineStart:2ch`,
  not a four-sided web box. Color still never carries alone — the phase word stays. (Declared FB7.4
  deviation: the left rule is a `grid`-mix, not phase-color at 45% — RV-5, a token-pass polish note.)
- cit:([`OutputBlock`], dashboard/src/panels/session-cockpit/conversation/ToolItem.tsx:58-85) clamps a `tool-output` block at `OUTPUT_THRESHOLD_LINES` (12, L17): it slices to
  the threshold and reports the exact `hiddenLines` on the `ClampButton`; empty output renders
  nothing (reads do not auto-expand). The output sits in a labeled `role="group"` / `aria-label="tool
  output"` / `tabIndex={-1}` overflow region so a wide line scrolls inside itself rather than widening
  the page, and Home/End land as region scroll rather than feed navigation.
- The block loop (L101) routes a `diff` block to `DiffBlock` (path/unified/old/new) and a
  `tool-output` block to `OutputBlock`.

### Invariants And Boundaries

- In-place recompose only: the same `itemId` is upserted by the reducer across phases; this component
  never creates a second row for a failure or a result.
- The clamp count is the honest source-line delta (via `sourceLineCount`), never a pixel clamp.
- The output region is a labeled overflow group (`role="group"`), which is what makes Home/End exempt
  from feed navigation while focus is inside it (the timeline's exclusion contract).

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries are
configured. This one-to-one card therefore relies on its direct agents-remember source/tests and the
reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- The item/block/phase types (`tool-input.summary`, `tool-output`, `diff`) this component narrows over. [1]
- The per-file diff renderer that a `diff` block routes to. [2]
- The shared ClampButton, `sourceLineCount`, and `useClampIds`. [3]
- The kind dispatcher that routes tool items here. [4]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.
