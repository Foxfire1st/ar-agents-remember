# dashboard/src/panels/session-cockpit/conversation/ToolItem.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/conversation/ToolItem.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-21T05:30+02:00 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview | `overview.md` |

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
| The item/block/phase types (`tool-input.summary`, `tool-output`, `diff`) this component narrows over. | "tool-input", "tool-output", "diff" | dashboard/src/data/conversation/types.ts:63-76 |
| The per-file diff renderer that a `diff` block routes to. | `DiffBlock` | dashboard/src/panels/session-cockpit/conversation/DiffBlock.tsx:35-79 |
| The shared ClampButton, `sourceLineCount`, and `useClampIds`. | `ClampButton`, `sourceLineCount`, `useClampIds` | dashboard/src/panels/session-cockpit/conversation/primitives.tsx:38-68; dashboard/src/panels/session-cockpit/conversation/primitives.tsx:71-74; dashboard/src/panels/session-cockpit/conversation/primitives.tsx:161-164 |
| The kind dispatcher that routes tool items here. | `ConversationItemView` | dashboard/src/panels/session-cockpit/conversation/ConversationItemView.tsx:68-71 |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-03T04:32:19+02:00 — W3-B08 curator: curated 6 citations (citation_anchor_missing=3, citation_prose_not_in_cit_form=0, citation_source_malformed=3); amended max-reviewer subject binding for all three block types; final scoped citation check clean.
- 2026-07-31T19:30+02:00 — 260731-EFA-L2 curator: re-derived 3 stale self-citations that pointed at a
  single line inside the construct instead of its definition — `verbPhrase` L55→L52-L56 (L55 was only
  the fallback `return`), `phaseClass` L45→L42-L50 (L45 was only the `waiting` entry), and
  `OutputBlock` L61→L58-L85 (L61 was only the non-`tool-output` guard). Described behavior is
  unchanged and still accurate.
- 2026-07-21T05:30+02:00 — 260718-CHATS-L5P curator: recorded the FB7.4 gutter-grammar restyle — the
  `●` phase-colored gutter dot + dim lowercase phase word (was a bordered uppercase `phaseTag`), and the
  Toad ShellResult left-rule output wash (was a four-sided box). Behavior (in-place recompose, honest
  clamp, diff routing, labeled overflow group) unchanged. Verification pinned to the leaf base
  (`352d5cd`) until closeout stamps the candidate commit.
- 2026-07-20T22:30+02:00 — 260718-CHATS-L4 curator: created the sidecar for the tool item —
  stable-ID in-place recompose, verb-phrase head with a text-plus-color phase accent, output clamp in
  a labeled `role="group"` scroll region, and diff routing to DiffBlock. Verification is pinned to the
  leaf base (`0be0099`) because the new source file is uncommitted; closeout owns its first source
  stamp.
