# dashboard/src/grammar/ — Shared Primitives Library Overview

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| sourceRoute            | `dashboard/src/grammar/`                         |

## Hot Path Summary

`Markdown.tsx` and `TaskRequirementLinks.tsx` resolve only registered task-local requirement addresses into internal reader actions; external links retain normal anchor behavior. Requirement handling is the no-override default: a caller's own `components.a` (the Knowledge reader supplies one) replaces it, because caller overrides are spread last. Read the provider before changing requirement-link refusal or task-context selection.

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

`grammar/` is the **shared primitives library** (note 08 "state grammar" — state carried by colour +
silhouette, never chrome). Each primitive is a small, reusable React component styled by
co-located Panda `css()` / `cva()`. `ModeBar` is the route's sole React Aria wrapper; the remaining
primitives are presentational or use native behavior. Panels and the shell compose these rather than
re-styling raw elements (the slice-5d analogue of the device-management `libs/` discipline, minus
Material).

## Route Model

- `Panel.tsx` — the panel chrome primitive: a self-scrolling box (`overflow:auto`, no top padding)
  with a sticky header **band** (flush at the top so rows scroll under it). Takes `title` or a
  custom `head` (the lifecycle list bundles its pivot there) + a sizing `className`. An opt-in `fill`
  variant swaps the self-scroll block for a bounded flex column (`display:flex` + `overflow:hidden`) — the
  Engine Room uses it to hold a fixed height while its inner columns scroll on their own.
- `ModeBar.tsx` — the viewport switcher: a **React Aria `ToggleButtonGroup`** (single-select
  radiogroup) styled by Panda `_selected` / `_focusVisible` conditions; roving focus + arrow-key
  nav, look unchanged from the old `.modebar`. Since 260928-MIK-L79 it also narrows its spacing below
  40rem so the four product entries fit a phone.
- `ExplorerTree.tsx` — the one shared async tree (260928-MIK-L79): the headless-tree adapter with the
  caller-supplied loader, row type, open behavior and suffix, a failed load shown as an alert with the
  loader's error text (no guaranteed directory name), a revision-driven re-read of every loaded branch
  and a one-shot reveal of a row the filter had hidden.
  The File Viewer and the Knowledge reader both build on it; no page keeps a second tree.
- `Dot.tsx` — the state/severity **mark**: one monospace cell (`width: 1ch`, centred, `flexShrink: 0`)
  whose Panda `cva` sets **`color`** — not `background`, and no `border-radius` — plus a
  distinguishing **glyph** per variant. Nine variants: the six `LIFECYCLE_STATES` (including
  `awaiting-developer`) and the three attention severities `alarm`, `warn`, `info`. Colour is the
  channel and deliberately GROUPS (`blocked` with `alarm`, `running` with `info`,
  `awaiting-developer` with `warn`), so the glyph is what separates the pairs the palette's seven
  tones cannot. The base is `muted` + `?` — "we could not classify this" — and must never borrow a
  live variant's treatment; it used to be `amber`, which is literally `warn`'s colour, and that is
  how `awaiting-developer` reached the developer looking like nothing special. The known-set is
  **derived** from the recipe (`export const DOT_VARIANTS = dot.variantMap.variant`), never
  hand-copied. `paused` moved off `dormant` — which stays the terminal tone with `abandoned` — to a
  muted amber mixed **`in oklab`**: `color-mix` walks the shorter hue arc, and amber (h 75) to muted
  (h 250) is 175°, so an `in oklch` mix runs through h 145 and renders green next to `mint`. Covered
  by `Dot.test.tsx` (three flat properties: vocabulary equality against `LIFECYCLE_STATES` asserted
  in both directions, every variant plus the unknown fallback rendering distinguishably, and every
  variant carrying a `c_*` ink of its own).
- `Affordance.tsx` — the display-only action affordance: a Panda `cva` (ready/off) over the reducer's
  precomputed enabled/reason; `aria-disabled`, never mutates (slice 06 enforces).
- `ProgressFill.tsx` — the bottom-up cyan charge fill (task-step / provider-seed progress).
- `TokenGauge.tsx` — the cumulative-token fuel gauge as a dependency-free SVG sparkline (uPlot stays
  deferred to slice 08).
- `Markdown.tsx` — a **memoized** markdown renderer (react-markdown + remark-gfm) for task-doc prose:
  Panda descendant-selector styling, GFM tables wrapped in a horizontal-scroll box, and an `inline`
  variant (unwraps the paragraph) for list items / decision cells. `React.memo` keeps the projection
  tick from re-parsing stable section strings (the source of the scroll-jank it fixed). No raw HTML.
  Since 260831-CCR-L23 both render modes mount a custom anchor component that renders registered
  `requirements/...` links as opening buttons and refuses unregistered requirement addresses (the
  listing comes from the `TaskRequirementLinks` provider context, never a local fetch). It is the
  no-override default: a caller's own `components.a` replaces it (the Knowledge reader supplies its
  own handler), because caller overrides are spread last. Since
  260928-MIK-L79 the Knowledge reader opts into `referenceMarkers` (prose `[n]` links) and
  `headingIds` (text-derived heading ids with per-slug suffixes and document typography) through
  [`referenceMarkers.ts`](referenceMarkers.ts.md); both stay off for every other consumer.
- `TaskRequirementLinks.tsx` — the requirement-link provider/context (260831-CCR-L23): fetches the
  registered task-local requirement listing for the viewed task document and exposes `open(path)`
  lifting a `{ kind: "requirements", repo, master, document, path }` target; consumed by `Markdown`
  and `TaskNotes` so registered packet addresses open in the internal reader.
- `RankBadge.tsx` — the rank insignia (260703-L14, the developer-picked V4 chevrons): tier
  `orchestration` = three gold chevrons under a filled command pip, tier `management` = two purple
  chevrons; inline SVG on fixed viewBoxes with a soft token-mixed glow, sizes `row` (16px, task rows)
  and `sm` (~13px, supported/tested but currently unused in production). `LifecycleList` is the sole
  production consumer and renders `row`; the retired Chats command tree and current `SessionRail` do
  not import it. It is only visible when an orchestration task exists (D3). Covered by
  `RankBadge.test.tsx` (glyph anatomy and both dimensions are the contract).
- `EvidenceBadge.tsx` — the launch-evidence tier badge (260715-FEUI-L3, R7): five DISTINCT glyphs
  (`…` pending / `✓` readback / `◇` model-validated / `·` defaults / `✕` refused) with the tier
  WORD always in the accessible name (`aria-label`) at EVERY size and the glyph `aria-hidden`;
  sizes `row`/`sm`, podracer token colors. The ONLY renderer of `data/launchEvidence` tiers. Its
  direct production consumers today are exactly **two**: `EvidencePane` (per-tier, `sm`) and
  `FailedLaunchBanner` (`tier="refused"`, `showWord`). Covered by `EvidenceBadge.test.tsx` (glyph
  Set-distinctness + the word at both sizes for all five tiers).

## Invariants And Boundaries

- **Reusable rendering with one task-context boundary** — visual primitives take data props.
  `TaskRequirementLinksProvider` is the explicit stateful exception: it reads the registered
  requirement listing, cancels stale effect responses, and lifts open actions through a callback.
  It does not author task requirements.
- **Panda + one React Aria owner** — visuals use co-located Panda tokens/conditions; `ModeBar` alone
  imports React Aria for toggle-group behavior. `Panel`'s sticky-header contract replaces the old
  `.rail > .panel > h2` descendant rule — each Panel is self-contained.
- **Determinism-safe, and motion is never an identity.** The dot's fault variants (`blocked`,
  `alarm`) carry the shared global `pulse` keyframe; `awaiting-developer` carries the slow
  `pulseSlow` breathe (the developer's 2026-07-16 ruling — never the fault strobe). All three also
  declare `_motionReduce: { animation: "none" }`, so `prefers-reduced-motion` reaches the same
  resting state that `?effects=off` already forces from `index.css`'s unlayered `!important` rule.
  Because both paths null every animation, a variant whose only difference from another is that it
  moves has no difference at all — which is why `Dot.test.tsx` strips the animation atoms out of its
  appearance key before comparing marks.
- **Per-variant tables are derived from the recipe and total, never hand-copied.** `Dot` exports
  `DOT_VARIANTS = dot.variantMap.variant` and builds both its `KNOWN` set and its
  `DOT_GLYPHS: Record<DotVariant, string>` from that single declaration. Re-introduce a second
  hand-maintained key list and the shipped failure returns exactly as it was: the new variant misses
  the copy, `variant` resolves to `undefined`, and the component renders the bare base. Keeping the
  glyph table a total `Record` is the other half — a variant added to the recipe without a mark is a
  `tsc -b` error rather than a dot that silently reads as some other state.
- **The unclassified case gets a treatment of its own, never a live variant's.** No variant may
  share the base's tone; every consumer can reach the base, because `Dot` takes a free
  `variant: string` and `LifecycleList` passes `lifecycle.state` through untouched.
- **This is not the only place a state becomes a visual, and the two do not share a table.**
  `topology/model.ts` maps the same `State` union onto its own five-member `ConstelStatus`
  vocabulary through a total `Record<State, ConstelStatus>` with an explicit `UNCLASSIFIED_STATUS`.
  Neither module imports the other (no `grammar/` reference under `topology/`, no `topology`
  reference under `grammar/`) — they are two independent tables held to the same two rules,
  totality and a default that does not borrow a live state's answer. A new lifecycle state has to be
  answered in both, and `Dot.test.tsx` is the one that catches it here.

## 260928-MIK-L79 Two Shared Primitives Gain Opt-In Extensions

**Route meaning extended (MIK-R79).** The Knowledge reader is built on this route's primitives instead of
page-private copies: [`ExplorerTree.tsx`](ExplorerTree.tsx.md) is the one async tree for the File Viewer and
the Knowledge reader, and [`referenceMarkers.ts`](referenceMarkers.ts.md) adds the opt-in
`remarkReferenceMarkers` / `remarkHeadingIds` plugins the shared [`Markdown.tsx`](Markdown.tsx.md) exposes for
a document's prose. With both options off, every existing consumer renders exactly as before; the page-private
tree, Markdown renderer and code view are gone (the code view is `file-viewer/FilePane.tsx`).

## Evidence

### Repo-Internal References

- The Panda runtime these primitives import (`css`/`cva`/`cx`). [1]
- The React Aria condition reconciliation (data-hovered/-focused). [2]
- The route's sole React Aria import wraps the viewport toggle group. [3]
- The complete direct production `EvidenceBadge` renderer set (two files; re-derived by grepping `dashboard/src` for `EvidenceBadge`). [4]
- The action-availability shape `Affordance` renders. [5]
- The six lifecycle states `Dot`'s variant vocabulary must cover, and the suite that asserts the two lists agree in both directions. [6]
- The OTHER state-to-visual table — a separate, total `Record<State, ConstelStatus>` with its own `UNCLASSIFIED_STATUS`; no import in either direction. [7]
- The shared global `pulse` / `pulseSlow` keyframes and the unlayered `html[data-effects="off"]` freeze the dot's motion rules depend on. [8]
- The attention and lifecycle panels rendered as siblings in the retained side rail — why an `awaiting-developer` state and a `warn` severity are on screen together and colour alone cannot separate them. [9]

## 260831-CCR-L23 Requirement-Address Anchors

L23 gave the route its first context-carrying primitive: `TaskRequirementLinks.tsx`
holds the registered task-local requirement listing per viewed task document and exposes the
`open(path)` callback; `Markdown.tsx` (block and inline) intercepts `requirements/...`
anchors so registered packets open in the internal artifact reader and unregistered addresses
render as refused spans while external/anchor links stay untouched.
