# dashboard/src/panels/session-cockpit/conversation/ConversationTimeline.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/conversation/ConversationTimeline.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-24T13:17:17Z |
| lastVerifiedCommitHash | `842b487b854503d95c9c2d9dce1841198ba93c7d` |
| lastVerifiedCommitDate | 2026-07-24T17:08:25+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[session-cockpit/conversation overview](overview.md)

## Purpose

The one navigable `role="feed"` (design §14.2/§14.3): a `@tanstack/react-virtual` timeline virtualized
by stable conversation ITEM (never by rendered line), so DOM pruning is independent of the
store/history authority. Each row is an `<article>` carrying `aria-posinset` from the server
`globalOrdinal` and `aria-setsize` only when the total is honestly known. It owns the accessible feed
mechanics — roving tabindex + focus pinning, bottom-follow, older paging, widget-scoped keyboard
navigation, and unknown-vendor run collapse — and no data/cursor logic.

## Code Commentary

### Logic

- **ARIA honesty** (L337-L355, R5): `aria-posinset` is the item's server `globalOrdinal` (or the run's
  first ordinal), NOT the array index; `aria-setsize` is emitted ONLY when `totalItems` is a known
  number (`knownTotal`), else omitted and the older-paging button reads `Load older (total unknown)`
  (L321). Every article is `aria-live="off"` (the surface owns announcements).
- **Focus pinning** (L184-L194, F18): `rangeExtractor` pins the focused row AND unconditionally the
  last row (`rows.length - 1`), so a tabbable article always stays mounted even when both scroll out of
  the virtual window — incoming data can never relocate focus to the container. `tabbable` (L342-L343)
  gives the focused row, or the last row when nothing is focused, `tabIndex=0`.
- **Bottom-follow** (L205-L232): `handleScroll` tracks `nearBottom` (within `BOTTOM_FOLLOW_PX=120`); a
  new last row while near-bottom scrolls to end, otherwise increments `pendingUpdates` and shows the
  NON-animated `N new updates` button (L369-L382). Older prepend restores the captured top stable row +
  pixel offset (L234-L242, anchor-preserving paging).
- **Widget-scoped keyboard nav** (L259-L289, §14.4/F14 accepted deviation): `onKeyDown` on the `feed`
  element (the ARIA feed pattern), NOT a global document handler. `]`/`[` move next/prev; `Home`/`End`
  jump ends. The exclusion list is complete — `isEditableTarget` (L97-L105) skips
  `INPUT/TEXTAREA/SELECT/contentEditable` and any `closest('button,a,[contenteditable],.cm-editor')`;
  `inOverflowRegion` (L107-L110) plus an active text selection make Home/End YIELD to labeled overflow
  regions (`[role="group"], pre`) and to selections instead of hijacking them.
- **Unknown-vendor run collapse** (L112-L148, L177): `groupUnknownVendorRuns` folds a run of ≥3
  identical-summary unknown-vendor items into one de-emphasized expandable `unknown-run` row; members
  stay addressable (`#ordinal · evidenceRef`), identity is never mutated. **L5P (R12):** the collapsed
  run is now a dim mono GUTTER line (`runRow`/`runSummary`, `whiteSpace:nowrap` + ellipsis, full text in
  `title`), and the copy is honest — `N unknown vendor events (same summary)` (was `N identical …
  events`): the members share a summary but each carries its OWN distinct evidence id, so "identical" was
  a copy lie against the visibly-skipping ids. The `show each` toggle (`runButton`) is a de-boxed
  underline text affordance (`flex:none` + `whiteSpace:nowrap`, V12) and expanded members indent under
  the summary (`runMember`, `paddingInlineStart:2ch`).

### FB7 terminal-surface identity (260718-CHATS-L5P — the developer directive)

The conversation stage was the one surface that replaced an xterm viewport yet did NOT inherit the
xterm "well" — it read as a generic web panel sharing the page background. This leaf gives it the
terminal grammar (spec home: the leaf's visual-audit `## FB7`, derived from Toad `main.tcss` + the
Claude Code / Codex TUIs, NOT first principles):

- **FB7.1 the well** — `viewport` gains `background: well` (the `#070b0f` token, see `styles/tokens.css`
  / `panda.config.ts`) + 1px `grid` border + radius + horizontal inset, EXACTLY matching the pty pane
  (`panels/Terminal.tsx`); the page `bg` shows through as the gutter. `feedInner` centers a `maxWidth:
  100ch` content column (Toad `max-width: 100`). Horizontal inset only — the vertical scroll math stays
  clean for the virtualizer. The pty-pane parity is the acceptance test (composer bg === `--well`,
  proven numerically).
- **FB7.3 rhythm** — `rowShell` DROPS the per-article `borderBottom` hairline (a web-list idiom neither
  reference uses) for line-grid blank-line spacing (`paddingBlockEnd: 0.9rem`); turn boundaries are
  marked by the turn-result flow line, not by rules.
- **FB7.4 gutter grammar** — sibling items (`ToolItem`, `TurnResultItem`, `ThinkingItem`, the run rows
  above, `primitives` ClampButton) replace boxed uppercase web chips with a `●`/`✻`/`·` gutter glyph +
  lowercase phase word + left-rule washes; documented in each item's card.

### Invariants And Boundaries

- Virtualization keys on the stable item, never rendered lines; the store/history authority is
  independent of what is mounted.
- `aria-posinset` is the server ordinal; `aria-setsize` is present ONLY when the total is honestly
  known — never a fabricated total.
- A tabbable article is always mounted (focused or default-last), so keyboard users never skip the feed.
- Keyboard navigation is widget-scoped; printable `[`/`]` cannot live in the document registry without
  fighting the printable-suppression contract, and Home/End defer to labeled overflow regions/selections.

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
| Feed ARIA, focus pinning, bottom-follow, older paging, widget keyboard nav, run collapse. | L160-L385 | [ConversationTimeline.tsx](ConversationTimeline.tsx) |
| The pure unknown-vendor run grouping this feed renders. | — | [collapse.ts](collapse.ts) |
| The kind dispatcher + stable accessible-name helper per article. | — | [ConversationItemView.tsx](ConversationItemView.tsx) |
| The item wire type (`globalOrdinal`/`kind`/`phase`) the feed reads. | — | [../../../data/conversation/types.ts](../../../data/conversation/types.ts) |
| The surface that mounts this feed and owns announcements + paging callbacks. | — | [ConversationSurface.tsx](ConversationSurface.tsx) |
| The feed ARIA + default-closed diagnostics render suite. | — | [renderer.test.tsx](renderer.test.tsx) |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Current L5I Maintenance

The virtualized timeline owns robust view-switch scroll restoration. It continuously records
per-session `{scrollTop, atBottom}`, ignores box-less/clamp-echo events, arms restores until honest
geometry can contain them, drives bottom restoration through stable frames, and lets trusted user
input cancel any pending restore. A latest chip is outside the scroller so it remains reachable;
measurement anchoring protects a reader's visible row during virtual-row size changes.

## Update History

- 2026-07-24T13:17:17Z — Curator: documented restored scroll intent, trusted-input precedence,
  late-clamp protection, latest navigation, and measurement anchoring; verification fields remain
  pre-commit.

- 2026-07-21T05:30+02:00 — 260718-CHATS-L5P curator: recorded the FB7 terminal-surface identity pass —
  the `viewport` well (`background: well` + grid border + `100ch` centered `feedInner` column, FB7.1),
  the FB7.3 line-grid rhythm (per-article hairline removed), and the R12 collapsed-run gutter line with
  the honest `same summary` copy + de-boxed nowrap toggle. Spec home is the leaf visual-audit `## FB7`.
  No feed/ARIA/virtualization behavior changed. Verification pinned to the leaf base (`352d5cd`) until
  closeout stamps the candidate commit.
- 2026-07-20T22:30+02:00 — 260718-CHATS-L4 curator: created the sidecar for the one `role="feed"`
  timeline — item-virtualized with server-ordinal `aria-posinset`, honest `aria-setsize`/`total
  unknown`, focus pinning of both the focused and default-last rows (F18), non-animated bottom-follow,
  anchor-preserving older paging, the widget-scoped keyboard nav with the completed exclusion list
  (F14), and unknown-vendor run collapse (F10). Verification is pinned to the leaf base (`0be0099`)
  because the new source file is uncommitted; closeout owns its first source stamp.
