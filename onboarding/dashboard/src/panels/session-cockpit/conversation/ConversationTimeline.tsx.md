# dashboard/src/panels/session-cockpit/conversation/ConversationTimeline.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/conversation/ConversationTimeline.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-04T03:03+02:00 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
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

- **ARIA honesty** cit:([`knownTotal`], dashboard/src/panels/session-cockpit/conversation/ConversationTimeline.tsx:1170-1170) (R5): `aria-posinset` is the item's server
  `globalOrdinal` (or the run's first ordinal), NOT the array index; `aria-setsize` is emitted ONLY
  when `totalItems` is a known number (`knownTotal`), else omitted and the older-paging button reads
  `Load older (total unknown)`. The button copy and article attributes are owned by the render body
  cit:(["Load older (total unknown)", "aria-posinset={posinset}", "aria-setsize\": knownTotal", "aria-live"], dashboard/src/panels/session-cockpit/conversation/ConversationTimeline.tsx:1189-1189; dashboard/src/panels/session-cockpit/conversation/ConversationTimeline.tsx:1221-1223); every article is
  `aria-live="off"` because the surface owns announcements.
- **Focus pinning** cit:([`rangeExtractor`, `tabbable`], dashboard/src/panels/session-cockpit/conversation/ConversationTimeline.tsx:445-460; dashboard/src/panels/session-cockpit/conversation/ConversationTimeline.tsx:1210-1211; dashboard/src/panels/session-cockpit/conversation/ConversationTimeline.tsx:1168-1169) (F18): `rangeExtractor` pins the focused row AND unconditionally the
  last row (`rows.length - 1`), so a tabbable article always stays mounted even when both scroll out of
  the virtual window — incoming data can never relocate focus to the container. `tabbable` gives the
  focused row, or the last row when nothing is focused, `tabIndex=0`.
- **Bottom-follow** cit:([`handleScroll`, `pendingUpdates`], dashboard/src/panels/session-cockpit/conversation/ConversationTimeline.tsx:372-372; dashboard/src/panels/session-cockpit/conversation/ConversationTimeline.tsx:659-745) (`BOTTOM_FOLLOW_PX=120`): `handleScroll` tracks `nearBottom`.
  The append effect cit:([`ConversationTimeline`], dashboard/src/panels/session-cockpit/conversation/ConversationTimeline.tsx:344-1265) scrolls a new last row to the end while near-bottom and
  otherwise increments `pendingUpdates`. The latest chip render and its `N new updates` count are
  owned by the timeline cit:([`ConversationTimeline`], dashboard/src/panels/session-cockpit/conversation/ConversationTimeline.tsx:344-1265), while its update-state emphasis is static color/border styling rather than a continuous animation
  cit:([`latestChipWithUpdates`], dashboard/src/panels/session-cockpit/conversation/ConversationTimeline.tsx:221-224). Older prepend restores the captured top stable row + pixel
  offset through `prevFirstKeyRef` and the saved anchor cit:([`ConversationTimeline`], dashboard/src/panels/session-cockpit/conversation/ConversationTimeline.tsx:344-1265).
- **Widget-scoped keyboard nav** cit:([`onKeyDown`], dashboard/src/panels/session-cockpit/conversation/ConversationTimeline.tsx:1073-1103) (§14.4/F14 accepted deviation): `onKeyDown` on the `feed`
  element (the ARIA feed pattern), NOT a global document handler. `]`/`[` move next/prev; `Home`/`End`
  jump ends. The exclusion list is complete — cit:([`isEditableTarget`], dashboard/src/panels/session-cockpit/conversation/ConversationTimeline.tsx:264-272) skips
  `INPUT/TEXTAREA/SELECT/contentEditable` and any `closest('button,a,[contenteditable],.cm-editor')`;
  cit:([`inOverflowRegion`], dashboard/src/panels/session-cockpit/conversation/ConversationTimeline.tsx:274-277) plus an active text selection make Home/End YIELD to labeled overflow
  regions (`[role="group"], pre`) and to selections instead of hijacking them.
- **Operator scroll keys** cit:([`OPERATOR_SCROLL_KEYS`, `onScrollKey`], dashboard/src/panels/session-cockpit/conversation/ConversationTimeline.tsx:117-126; dashboard/src/panels/session-cockpit/conversation/ConversationTimeline.tsx:1141-1143): `OPERATOR_SCROLL_KEYS` — Home/End, PageUp/PageDown, ArrowUp,
  Space, `[`/`]` — is the "the operator is scrolling this feed" set for the trusted-input restore
  cancel (a programmatic clamp never carries input; consumed beside the
  wheel/touch/pointer listeners). ArrowDown is deliberately ABSENT: on a non-empty roster the
  conversation surface hijacks ArrowDown into the agents line, so it is no longer a scroll key here
  — PageUp/PageDown, `[`/`]` and the wheel remain the downward scroll paths. The set is EXPORTED for
  the surface keyboard-contract tests.
- **Unknown-vendor run collapse** cit:([`groupUnknownVendorRuns`], dashboard/src/panels/session-cockpit/conversation/collapse.ts:23-55): a run of ≥3
  identical-summary unknown-vendor items folds into one de-emphasized expandable `unknown-run` row;
  members stay addressable (`#ordinal · evidenceRef`), identity is never mutated. The collapsed
  run is a dim mono GUTTER line (`runRow`/`runSummary`, `whiteSpace:nowrap` + ellipsis, full text in
  `title`), and the copy is honest — `N unknown vendor events (same summary)` (was `N identical …
  events`): the members share a summary but each carries its OWN distinct evidence id, so "identical" was
  a copy lie against the visibly-skipping ids. The `show each` toggle (`runButton`) is a de-boxed
  underline text affordance (`flex:none` + `whiteSpace:nowrap`, V12) and expanded members indent under
  the summary (`runMember`, `paddingInlineStart:2ch`).

### FB7 terminal-surface identity

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
- ArrowDown is never treated as an operator scroll key: the surface hijacks it into the agents line
  on a non-empty roster, so the trusted-input restore cancel must not fire on it; downward scrolling
  keeps working through PageDown, `]`, and the wheel.

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
| Feed ARIA, focus pinning, bottom-follow, older paging, widget keyboard nav, the scroll-key set, run collapse. | `ConversationTimeline`, `OPERATOR_SCROLL_KEYS` | dashboard/src/panels/session-cockpit/conversation/ConversationTimeline.tsx:117-126; dashboard/src/panels/session-cockpit/conversation/ConversationTimeline.tsx:344-1265 |
| The pure unknown-vendor run grouping this feed renders. | `groupUnknownVendorRuns` | dashboard/src/panels/session-cockpit/conversation/collapse.ts:23-55 |
| The kind dispatcher + stable accessible-name helper per article. | `ConversationItemView`, `itemAccessibleName` | dashboard/src/panels/session-cockpit/conversation/ConversationItemView.tsx:15-42; dashboard/src/panels/session-cockpit/conversation/ConversationItemView.tsx:68-71 |
| The item wire type (`globalOrdinal`/`kind`/`phase`) the feed reads. | `ConversationItem` | dashboard/src/data/conversation/types.ts:158-176 |
| The surface that mounts this feed, owns announcements + paging callbacks, and hijacks ArrowDown into the agents line. | `ConversationSurface` | dashboard/src/panels/session-cockpit/conversation/ConversationSurface.tsx:100-381 |
| The feed ARIA + default-closed diagnostics render suite. | "ConversationTimeline — one navigable role=feed (R5, §14.2)" | dashboard/src/panels/session-cockpit/conversation/renderer.test.tsx:33-68 |
| The surface keyboard-contract suite pinning the ArrowDown absence from the scroll-key set. | "ConversationSurface agent focus" | dashboard/src/panels/session-cockpit/conversation/ConversationAgentFocus.test.tsx:144-410 |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Current L5I Maintenance

The virtualized timeline owns robust view-switch scroll restoration. It continuously records
per-session `{scrollTop, atBottom}`, ignores box-less/clamp-echo events, arms restores until honest
geometry can contain them, drives bottom restoration through stable frames, and lets trusted user
input cancel any pending restore. A latest chip is outside the scroller so it remains reachable;
measurement anchoring protects a reader's visible row during virtual-row size changes.

## Update History

- 2026-08-04T03:26:26+02:00 — 260731-EFA-L6 S18-SR3-B06 curator: generated and source-inspected the four whole-claim ranges (4 repairs, 0 normalisations, 0 declines); the locked immediate recheck was clean with frozen zero source/tokenize/parse/build telemetry.
- 2026-08-04T03:03:23+02:00 — 260731-EFA-L6 S18-SR3-B06 worker: replaced the
  three underbound append, latest-chip, and prepend fragment records with whole timeline ownership;
  the static update-state styling is split onto its own exact symbol. All changed bindings are
  provisional `:1-1` inputs for the fresh Luna curator; no citation mechanics ran.
- 2026-08-04T02:20:03+02:00 — 260731-EFA-L6 S18-B06 curator delta: repaired the scoped citations against the frozen source snapshot; generated ranges were inspected and the managed index remained warm/frozen with zero source reads, tokenization, parsing, and build.

- 2026-08-04T01:24:49+02:00 — 260731-EFA-L6 S18-SR2-B06 worker: retained the valid
  `knownTotal`/scroll-handler ranges and source-first bound the omitted ARIA render ownership,
  append-follow effect, prepend-anchor restore, and latest-chip rendering with provisional `:1-1`
  citations. No final ranges were hand-authored and no citation mechanics ran.
- 2026-08-04T00:28:23+02:00 — 260731-EFA-L6 S18-B06 curator: repaired and normalized the scoped conversation-timeline citations; final exact frozen-snapshot check is clean.
- 2026-08-02T23:59:26+02:00 — L6 Wave 2 duplicate-range correction: removed 1 repeated path:start-end Citation objects from 1 same-claim citation group(s) at card line(s) 49; retained the first occurrence/order, all unique anchors and source coverage; scoped non-fixing result 0.
- 2026-08-02T20:45:43+02:00 — L6 W2-B02 curator: anchored 7 repository-internal references and normalized 4 prose citation references for the timeline, collapse helper, item dispatcher, wire type, mounting surface, and focused test suites; final scoped result 0 (checker-clean).

- 2026-07-26T21:59+02:00 — 260718-CHATS-L7R curator: recorded the updated scroll-key contract —
  `OPERATOR_SCROLL_KEYS` is now EXPORTED (for the surface keyboard-contract tests) and ArrowDown is
  deliberately absent from it because the conversation surface hijacks ArrowDown into the agents
  line on a non-empty roster; PageUp/PageDown, `[`/`]`, ArrowUp, Home/End, Space, and the
  wheel/touch/pointer remain the scroll/trusted-input paths. Also re-anchored the card's line
  citations, which had drifted from the current file layout (the file is 1223 lines): ARIA honesty
  L1128/L1147/L1179-L1181, focus pinning L439-L464, tabbable L1168-L1177, bottom-follow
  L638-L680 + latest chip L1198-L1215, widget nav L1033-L1060 with `isEditableTarget` L263-L271 and
  `inOverflowRegion` L273-L276, run-collapse consumption L356, and the reference row L356-L1223.
  Verification metadata stays pinned at the file's last committed touch (`842b487`); the scroll-key
  change is uncommitted.
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
