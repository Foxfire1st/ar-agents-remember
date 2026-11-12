# Agents Remember dashboard: design language

AR's memory layer `system/DESIGN.md`: the web dashboard's concrete look. The process is in
`design-guidelines.md` beside it; the explainer's pages follow `TREATMENT.md` and `TECHNIQUES.md`.
The engine-room pod stage keeps `dashboard/public/_proto/DESIGN.md`.

**Sources.** Colours are cited by token name: the variable in `dashboard/src/styles/tokens.css`
(`--mint`) and its mirror in `dashboard/panda.config.ts` (`mint`). The tokens hold the values; this
file gives their meaning and place. A value with no token names the approved review-page mockup's
variable or selector (D367): coordination workspace,
`tasks/agents-remember/260928_maintained-invariant-knowledge/notes/reference/review-page-mockup-D367/`,
38 states shot at 1920 × 1080 and 1440 × 900. `mock:N` is a line of its frozen `styles.css`,
`app.js:N` of its script; dashboard code is cited by file and export.

## Character

A dark instrument panel, amber accents, one monospace face. State is carried by colour and
silhouette, never by chrome. Colour always means something, and a mark keeps its colour wherever
it appears. One meaning per colour per surface; colour never carries a meaning alone: a dashed
outline, a label or an icon goes with it (D412).

## Colour roles on the review page

| Token | Meaning |
|---|---|
| `--bg` / `bg` | Page, reading column, idle tabs and segments |
| `--bg-panel` / `bgPanel` | Panels, tree, popovers, tray, block heads |
| `--ink` / `ink` | Main text |
| `--grid` / `grid` | Borders, rules, idle outlines |
| `--muted` / `muted` | Idle control text, secondary text, reasons |
| `--amber` / `amber` | Selected, where you are: current, focus, primary action; tinted or dashed: needs attention. The engine room keeps "nominal". |
| `--cyan` / `cyan` | Progress and running; section labels; links; a pressed panel toggle |
| `--mint` / `mint` | Live, added, done, attached |
| `--alarm` / `alarm` | Removed, changed, destructive, fault |
| `--dormant` / `dormant` | Engine room only |
| `--gold` / `gold` | The sprint tier and the "in work" border; no other meaning |
| `--purple` / `purple` | The master tier; dashed on the review page: the explainer's judgment |

Decided as new tokens with the mockup's values, not yet built (D412; Open differences, item 1):
`dim` (mockup `--dim`, tertiary text: hints, group headings, markers), `rule` (`--rule`, light row
separators), the selected fill (`--sel`), `hover` (`--hover`), the code background (`--bg-code`),
and the four diff fills (`--add-bg`, `--add-line`, `--del-bg`, `--del-line`), shared by every diff,
the shared diff pane included.

## Element to token

| Element | Look | Source |
|---|---|---|
| +N count | `mint` | mock:96 (`.ins`); app.js:213, 279, 314 |
| −N count | `alarm` | mock:95 (`.del`) |
| Selected segment ("Changes only", "Review") | `amber` text on the selected fill | mock:75 |
| Selected menu entry | `amber`, with a ● marker | mock:115; app.js:242 |
| Tab on | `amber` text and border, 5 px `amber` glow | mock:60; `viewTabLook.ts` |
| Pressed panel toggle | `cyan` | mock:104 |
| Current tree row | selected fill, 2 px `amber` left border, `amber` name | mock:148-149 |
| Effect badge | `cyan`; retire, weaken, replace: `amber`; "changed": `alarm`; "unknown": `dim`, dashed | mock:84-86, 154-155; app.js:118; D412 |
| Section label | `cyan`, 0.68rem, upper case, 0.1em | mock:91 |
| Primary button | `amber` fill, `bg` text, bold | mock:66 |
| Destructive button | `alarm` text and border | mock:376 |
| Attach ⊕ | `muted`; hover `cyan`; "✓ in tray" `mint` | mock:192-194 |
| Status chip | quiet: `muted`, `dim` dot; attention: `amber`; working: `cyan`; live dot: `mint` | mock:77-82 |
| Explainer's judgment | `purple`, dashed; a stale grade `amber`, struck through | mock:71, 89, 162-163 |
| Tray note | `dim`, dashed (not `gold`) | D412 |
| Word diff | removed struck on the removed fill; inserted underlined on the added fill | mock:190-191 |
| Diff rows | the diff fills; markers `mint`, `alarm` | mock:221-226 |
| "N unchanged lines" bar | `muted`; hover `cyan` | mock:227-228 |

## Type and reading measures

One face, `--font-mono` (`fonts.mono`). Body text 14 px (the base layer of `index.css`, mock:40).

| Surface | Size, line height | Measure | Source |
|---|---|---|---|
| Subject heading | 1rem bold, 1.4 | at most 90ch | mock:186 |
| Statement | 0.83rem, 1.7 | at most 92ch | mock:188 |
| Tree row | 0.76rem, 1.5 | one line | mock:146 |
| Block introduction row | 0.74rem, 1.55 | one line | mock:210 |
| Diff | 0.78rem, 1.55 | full column width | mock:215 |
| Panel heading | 0.72rem bold, upper case, 0.12em, `cyan` | | mock:142 |

Prose keeps its measure; code takes the column's full width. Prose as wide as the code is a defect.
Each surface keeps its own measure. The explanation page's inner type belongs to `TREATMENT.md`.

## Density

- **One line per item.** Tree rows, sub-rows, group rows and a block's rationale or condition rows
  take one line each, cut with an ellipsis (mock:146, 151, 252-254; D48).
- **Overflow opens in place.** The full text shows on hover and a click opens that one item in
  place; word-diff marks stay visible on the line (ruling d9a1ec8f, item 7).
- **No text walls.** Status facts become one chip with a popover; raw records go under "Technical
  details" at the bottom (mock:257-260).
- **Nothing shows for the normal case** (D396). The branch chip stays quiet grey while "not
  measured".
- **Reasons as text:** "weaken · 13 loc." (app.js:207). A collapsed group keeps its count in its
  heading (mock:246-250).
- **Help text is never squeezed;** in a narrow row it moves to its own line (ruling d9a1ec8f,
  item 1). **Menus explain** with a hint (mock:116). **Chips are not cut;** selectors give way
  first.
- **One page scroll.** The reading column is the page scroll (mock:174); the tree is the only other
  scroller, with `overscroll-behavior: contain` (mock:144). The explanation frame scrolls inside
  itself (below).
- **One control where it belongs**, never one per row (D230).

## States

| State | Look | Source |
|---|---|---|
| Hover | `hover` fill, or `amber` or `cyan` text | mock:65, 113, 147, 193 |
| Focus | 2 px `amber` outline, offset 1 px | mock:45 |
| Selected, current | `amber`, with the selected fill or an `amber` border | mock:60, 75, 148 |
| Disabled | opacity 0.5 | `columnTabButton`, `launcherButton` |
| Empty | one `dim` line, or a centred note with one action | mock:166, 264-266 |
| Loading | a skeleton at a default or known height | mock:296-298; D383 |
| Working | `cyan` chip "◌ …" with a percentage; listed steps; `cyan`-to-`mint` bar | mock:82, 333-344 |
| Moved | `amber` chip with a dot: "Task moved: #8 → #9 · n blocks changed" | mock:79-80 |
| Stale | `amber` dashed badge; `amber` bar or left border | mock:90, 212, 284 |
| Error | `alarm` text | the mockup draws none |

## Control patterns

Reuse these. A second look for a job a control already does is a defect (D48).

- **Tabs.** `ModeBar` (`grammar/ModeBar.tsx`), styled by `viewTabButton`; tab-like controls take
  `viewTabMetrics` (`grammar/viewTabLook.ts`).
- **Segmented switch.** Joined buttons in one border; the selected one `amber` on the selected fill
  (mock:72-76): Review | Explanation, Changes only | Full context.
- **Menu.** A `bgPanel` popover: upper-case `dim` group headings, rows with a `dim` reason column, a
  hint (mock:108-117).
- **Panel toggle.** One shared icon button on every sidebar (D359), keys `[` and `]`.
- **Diff.** `panels/changeset/DiffPane.tsx`. Side by side when the reading column is at least
  1080 px wide, unified below; unchanged stretches fold into "N unchanged lines" bars that open in
  place (mock:227, 232-235).
- **The tray.** Minimised: one line, "⊕ Attached · n"; a new pick keeps it minimised, a Send
  returns it there (D397). Expanded: `bgPanel`, 2 px `amber` top border, 6 px corners; the pick
  list scrolls with `overscroll-behavior: contain`, the field and Send stay visible (mock:426,
  430). Closed: an edge pill, `amber` border and text. It docks above Paseo's message box, never
  over it (D367).

## The explanation frame

The explainer's page is a separate document the reader works in. The dashboard gives it:

- **Room.** The reading column's full width (the page sets its own 78ch prose measure and lets
  figures use the rest) and the column's free height. The page scrolls inside itself, so its
  sticky figures stick.
- **The keyboard.** Keys pressed inside the frame stay there; `[`, `]` and other dashboard keys do
  not fire while the page has focus.
- **No shared stylesheet.** The page cannot read these tokens; `TREATMENT.md` maps its roles to
  the token names above and takes the values from the kit's `col()`.

## Motion

- Every animation stops under `html[data-effects="off"]`; script motion also honours
  `prefers-reduced-motion` (`panels/engine-room/useShouldAnimate.ts`). Captures run with effects
  off. The effects switch does not reach the explanation frame; the page follows only
  `prefers-reduced-motion` (Open differences, item 6).
- At most 3 flashes per second; a pulse is a slow ease-in-out of opacity, never on-off blinking.
- Control colour changes take 120 ms; mockup: jump flash 1.6 s, new chip 1.2 s, progress 0.4 s
  (mock:200, 362, 336).
- Content does not move under the reader: blocks stay mounted during reads, and space for late
  content is reserved (UX review F1, 3.6).

## Widths

| | 1920 × 1080 | 1440 × 900 |
|---|---|---|
| Tree, chat, gutter | 340, 500, 14 px | 292, 420, 12 px |
| Diff | side by side | unified |
| Tree rows | file names shown | file names dropped |

The switch is at `max-width: 1600px` (mock:27-33). A hidden sidebar takes no width (mock:133-137).
Below 40rem the view tabs wrap (`grammar/ModeBar.tsx`).

## Open differences

1. **D412's tokens are not built.** `dim`, `rule`, the selected fill, `hover`, the code background
   and the diff fills have no token; the dashboard writes `dim` and `rule` as literals
   (`panels/detail-panel/pageStyles.ts`). Also without a token: the line-number colour (mock:218),
   the fold fill (mock:227), the word-diff inks (mock:190-191) and the explanation inks
   (mock:270-272).
2. **Diff fills.** Mockup alpha about 0.42 and 0.5 (mock:20, 22); `DiffPane.tsx` about 0.67.
   D412: the mockup's values win.
3. **Token comments.** `--amber`'s comment says "nominal wireframe" only; D412 asks it to name both
   meanings. `--purple` is commented as the management tier only.
4. **Focus ring.** Mockup: 2 px, offset 1 px. Dashboard: view tab 1 px, offset 1 px; launcher
   button 2 px, offset 2 px (`viewTabLook.ts`).
5. **Smaller ones.** Body line height: mockup 1.5, the dashboard's base sets none. Panel heading:
   mockup 0.72rem and 0.78rem, base `h2` 0.8rem. The mockup's mono stack adds "DejaVu Sans Mono".
   No shared segmented control exists yet. The mockup draws no tray minimised line (D397's
   "⊕ Attached · n" wins) and no error state.
6. **Explanation frame.** The landed frame is 34rem high (`RevisionFrame.tsx`, `page`); L201's
   candidate gives it the column's free height and a full-screen switch. Neither passes the
   effects switch into the page.
