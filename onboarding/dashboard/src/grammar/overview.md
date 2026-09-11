# dashboard/src/grammar/ — Shared Primitives Library Overview

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| sourceRoute            | `dashboard/src/grammar/`                         |
| doc_type               | `route-local-overview`                           |
| lastUpdated | 2026-09-05T07:12+00:00 |
| lastVerifiedCommitHash | `ea35964985f30080488270e71ac81657ac40682b` |
| lastVerifiedCommitDate | 2026-09-05T06:48:29+02:00 |
| governingOverview      | `../overview.md`                                 |

## Hot Path Summary

`Markdown.tsx` and `TaskRequirementLinks.tsx` resolve only registered task-local requirement addresses into internal reader actions; external links retain normal anchor behavior. Read the provider before changing requirement-link refusal or task-context selection.

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
  nav, look unchanged from the old `.modebar`.
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
  listing comes from the `TaskRequirementLinks` provider context, never a local fetch).
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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The Panda runtime these primitives import (`css`/`cva`/`cx`). | "export default defineConfig" | dashboard/panda.config.ts:3-3 |
| The React Aria condition reconciliation (data-hovered/-focused). | "[data-hovered]" | dashboard/panda.config.ts:21-21 |
| The route's sole React Aria import wraps the viewport toggle group. | "export function ModeBar" | dashboard/src/grammar/ModeBar.tsx:48-48 |
| The complete direct production `EvidenceBadge` renderer set (two files; re-derived by grepping `dashboard/src` for `EvidenceBadge`). | "export function EvidencePane", "export function FailedLaunchBanner" | dashboard/src/panels/session-cockpit/EvidencePane.tsx:411-411; dashboard/src/panels/session-cockpit/FailedLaunchBanner.tsx:69-69 |
| The action-availability shape `Affordance` renders. | `Affordance` | dashboard/src/grammar/Affordance.tsx:27-42 |
| The six lifecycle states `Dot`'s variant vocabulary must cover, and the suite that asserts the two lists agree in both directions. | "export type State = ", "const ALL_VARIANTS" | dashboard/src/types/projection.ts:15-15; dashboard/src/grammar/Dot.test.tsx:17-17 |
| The OTHER state-to-visual table — a separate, total `Record<State, ConstelStatus>` with its own `UNCLASSIFIED_STATUS`; no import in either direction. | `UNCLASSIFIED_STATUS` | dashboard/src/topology/model.ts:68-68 |
| The shared global `pulse` / `pulseSlow` keyframes and the unlayered `html[data-effects="off"]` freeze the dot's motion rules depend on. | "@keyframes pulse {" | dashboard/src/index.css:88-88 |
| The attention and lifecycle panels rendered as siblings in the retained side rail — why an `awaiting-developer` state and a `warn` severity are on screen together and colour alone cannot separate them. | "<AttentionQueue onSelect={onSelect}"; "<LifecycleList selectedId={selectedId}" | dashboard/src/cockpit/Cockpit.tsx:640-641 |

## 260831-CCR-L23 Requirement-Address Anchors

L23 gave the route its first context-carrying primitive: `TaskRequirementLinks.tsx`
holds the registered task-local requirement listing per viewed task document and exposes the
`open(path)` callback; `Markdown.tsx` (block and inline) intercepts `requirements/...`
anchors so registered packets open in the internal artifact reader and unregistered addresses
render as refused spans while external/anchor links stay untouched.

## Update History

- 2026-09-05T07:12+00:00 — L31 cumulative source review at `ea35964985f30080488270e71ac81657ac40682b`: Qualified the new stateful requirement provider and corrected retained side-rail evidence. Verification records source review, not execution or acceptance.



- 2026-09-05T06:21+00:00 — Re-read the affected source declarations and repaired citation ranges shifted by CCR additions. Preserved the route contract and existing history; literal anchors identify the exact current construct where shared identifiers were ambiguous.

- 2026-09-05T06:12+00:00 — Composed retained CCR route contributions without replacing sibling knowledge; preserved prior source-verification metadata and historical entries.

- 2026-09-04T01:06+02:00 — 260831-CCR-L23 Gate-5 route impact: added the `TaskRequirementLinks.tsx` bullet to the Route Model and recorded `Markdown.tsx` requirement-address anchors (registered links open, unregistered refuse, external/anchor untouched).


- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B20 curator: replaced the `n/a` table rows with
  exact anchors and source-backed ranges; exact non-fixing check returns zero findings.

- 2026-08-01T10:05+02:00 — 260731-EFA-L4 curator: **corrected a factually wrong route claim.** The
  card said `Dot.tsx` was "a Panda `cva` mapping lifecycle state / attention severity to a colour
  (unknown → nominal amber)". Every load-bearing part of that was false against the tree: the base
  is `muted` + `?`, not amber (the amber base was literally `warn`'s colour, and it is how
  `awaiting-developer` shipped looking like nothing special); the recipe sets `color` on a `1ch`
  monospace cell, not `background` on a `border-radius: full` box; `awaiting-developer` is now a
  declared variant, making nine; each variant also carries a distinguishing glyph, because seven
  tones cannot separate nine variants and a base; the known-set is DERIVED from the recipe
  (`DOT_VARIANTS = dot.variantMap.variant`) rather than a hand-copied `KNOWN` array; and `paused`
  moved off `dormant` to a muted amber that must be mixed `in oklab` (an `in oklch` mix of amber and
  muted takes the shorter 175° hue arc through h 145 and renders green). Recorded the new
  `Dot.test.tsx` and the three properties it pins. Replaced the single-clause "Determinism-safe"
  invariant with the motion rule as it now stands (`pulse` on the two fault variants, `pulseSlow` on
  `awaiting-developer`, `_motionReduce` on all three, and the appearance key that excludes animation
  atoms), and added three route invariants the correction depends on: derived-and-total per-variant
  tables, an unclassified treatment that never borrows a live variant's, and the boundary with
  `topology/model.ts` — the other state-to-visual table, which is deliberately separate (neither
  module imports the other) and held to the same two rules.
  Recorded explicitly because an earlier design direction here was cut and must not creep back: this
  leaf contains **no dot suppression machinery**. Re-verified independently of the file-level
  curator — `ls dashboard/src/grammar/` lists no `dotSuppression.ts`, a repo-wide `find` for
  `*suppression*` returns nothing, `grep -rniE 'forced-colors|forcedColors|@media +print'` over
  `dashboard/src/` returns nothing, and `dashboard/src/index.css` is byte-identical to the leaf base
  (`git diff HEAD` empty; `sha256sum` matches `git show HEAD:` at
  `a967c0c42978c8b0e56640b5a3be47ca4c55d518cfed434498c3960b09c832ea`). Nothing in this card describes
  such a mechanism and nothing should. Four `Repo-Internal References` rows added.
  Two PRE-EXISTING errors were found while confirming that every reference path in this card
  resolves, and corrected here — neither is L4's doing (both are already false at the leaf base
  `abc7cbc`, and `HeaderStrip.tsx` is untouched by this leaf): the `EvidenceBadge` consumer set was
  claimed as four files, but `HeaderStrip.tsx` contains no `EvidenceBadge` reference at the leaf base
  or in the working tree, and `panels/session-cockpit/StatusLine.tsx` exists in neither. The direct
  production renderer set — re-derived by grepping `dashboard/src` — is exactly `EvidencePane` and
  `FailedLaunchBanner`.
  Verification metadata pinned until closeout stamps the commit.

- 2026-07-18T16:02+02:00 — FEUI MX-FIX-3: refreshed the directly affected RankBadge route claim:
  `LifecycleList` is the sole production consumer at `row`, while `sm` remains a supported/tested
  dimension without a current production caller. The bounded route census also records `ModeBar` as
  the sole React Aria importer and the exact four direct EvidenceBadge consumers (`HeaderStrip`,
  `EvidencePane`, `StatusLine`, and `FailedLaunchBanner`). These direct import/caller claims, rather
  than every grammar behavior, were verified against code commit
  `31f58834f86c0d98e26b0896e099a2403a8729ee`.

- 2026-07-17T06:20+02:00 — 260715-FEUI-L3 route impact (capability catalog client and launch
  flow): the library gained `EvidenceBadge.tsx` (+ `EvidenceBadge.test.tsx`) — the five-glyph
  launch-evidence tier badge (tier word always in the accessible name, glyph aria-hidden,
  `row`/`sm` sizes) shared by the session-cockpit HeaderStrip, SeatInspector, and
  FailedLaunchBanner; tiers come exclusively from `data/launchEvidence.launchTier`. Verification
  metadata pinned to the leaf base until closeout stamps the L3 code commit.
- 2026-07-06T23:57:30+02:00 — 260703-L14 route impact (visual hierarchy + chat grouping): the library
  gained `RankBadge.tsx` (+ `RankBadge.test.tsx`) — the V4 chevron rank insignia (gold orchestration
  / purple management tiers, `row`/`sm` sizes) shared by `panels/LifecycleList` rows and
  `panels/SessionList` group headers, coloured by the new gold/purple Panda tokens. Verification metadata pinned until closeout stamps the L14 commit.
- 2026-07-06T03:20+02:00 — No route impact: 260703-L9 reuses `Markdown.tsx` unchanged as the renderer for the task reader's opened notes (the sidecar-view treatment); no grammar primitive was added or modified.
- 2026-06-21T02:44+02:00 — slice 6g: added the `Markdown.tsx` primitive (memoized react-markdown + remark-gfm renderer for task-doc prose; GFM tables, `inline` variant). Verification metadata pinned until closeout stamps the 6g code commit.
- 2026-06-17T22:45 — engine-room visual-parity: `Panel` gained an opt-in `fill` variant (a bounded flex
  column vs the default self-scroll block) so a panel that hosts its own internal layout — the Engine Room's
  3-zone grid — can hold a fixed height while its columns scroll. Backward-compatible; other primitives
  unchanged. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-15T17:00 — Created for slice 5d: the grammar primitives migrated to Panda; new `Panel`
  chrome primitive + `ModeBar` (React Aria). Verification metadata pinned until closeout stamps the
  5d code commit.
