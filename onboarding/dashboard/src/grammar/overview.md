# dashboard/src/grammar/ — Shared Primitives Library Overview

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| sourceRoute            | `dashboard/src/grammar/`                         |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

`grammar/` is the shared primitives library: reusable components carry state through colour and distinguishing marks, and give panels and the shell common rendering and presentation recipes. Components use Panda `css()` / `cva()` styling. `ModeBar` is this directory's sole React Aria wrapper; `ExplorerTree` uses Headless Tree for async tree behavior. The directory owns presentation and shared reader behavior, while callers supply their data, selection actions and launch policy.

The preserved table above is descriptive metadata, outside the operative promises below.

## Hot Path Summary

`Markdown.tsx` and `TaskRequirementLinks.tsx` resolve only registered task-local requirement addresses into internal reader actions; external links retain normal anchor behavior. Requirement handling is the no-override default: a caller's own `components.a` (the Knowledge reader supplies one) replaces it, because caller overrides are spread last. Read the provider before changing requirement-link refusal or task-context selection.

## Construction

- `Panel.tsx` supplies a self-scrolling box with no top padding and a sticky header band, so rows scroll under the header. It accepts `title` or a custom `head`, plus a sizing `className`. Its opt-in `fill` variant changes the self-scrolling block into a bounded flex column with hidden overflow. Engine Room uses this variant for its internal layout.
- `ModeBar.tsx` wraps React Aria's `ToggleButtonGroup` with single selection and no empty selection. Its source documents roving focus and arrow-key navigation. Panda selected/focus conditions style its shared `viewTabButton` class; spacing narrows below 40rem.
- `viewTabLook.ts` supplies shared metrics and presentation for `viewTabButton`, `launcherButton`, `launcherSelect` and `launcherChip`; `columnTabButton` carries the same authority at compact Operations scale. Start adopts the selected-tab look and Refresh the unselected look. Selectors preserve source letter case and draw an arrow; callers supply full-value and provenance hover text. These recipes do not resolve launch choices, permission or control availability.
- `ExplorerTree.tsx` is the shared async tree used by File Viewer, Knowledge and Notes. Callers supply the loader, row data, open behavior and optional suffix. A failed load displays an alert containing the loader's error text, without promising a directory name. Revision changes invalidate every loaded branch; an address missing from the cache can trigger a one-shot re-read of its nearest cached ancestor. The selected row is also brought into the viewport once per selected address.
- `Dot.tsx` renders a centred, non-shrinking monospace cell of width `1ch`. Its recipe sets ink colour, without a background or rounded mark, for attention severity only: `alarm` is a filled triangle, `warn` a hollow triangle and `info` an informational mark. It is not a task-stage, host-activity or lifecycle-state sign. Unknown input renders the `muted` base with `?`. `DOT_VARIANTS` is derived from the recipe and `DOT_GLYPHS` is total over that derived type. `Dot.test.tsx` asserts equality with `ATTENTION_SEVERITIES`, distinct resting appearances including unknown input, and known ink different from the unknown base.
- `Affordance.tsx` displays the reducer's precomputed enabled/reason values through ready/off recipes. It always renders `aria-disabled="true"`, supplies a title and has no click action; it does not enforce or perform the action.
- `ProgressFill.tsx` renders a bottom-up cyan charge fill from completed/total props. Its documented intended uses are task-step and provider-seed progress; the current task reader directly renders it for completed steps.
- `Markdown.tsx` is a memoized renderer using react-markdown and remark-gfm. Panda descendant selectors style prose; block-mode GFM tables receive a horizontal-scroll wrapper. Inline mode unwraps paragraphs for list items and decision cells. Memoization avoids unnecessary stable-prop rendering. For text of at least 1000 characters with no caller components override object, the renderer additionally uses the store's `TaskDocumentResources` syntax cache through `remarkCachedParse`. The cache key includes the full source text and `remark-gfm4` grammar spelling; each consumer receives a structured clone before reference-marker or heading transforms, so cached syntax does not retain another view's transformations or callback. Short text and any supplied components override object do not take that syntax-cache path. It configures no raw-HTML plugin. Both modes use a default anchor component that turns registered `requirements/...` addresses into opening buttons and unregistered requirement addresses into refused spans. The provider supplies the listing; the renderer makes no local listing fetch. Caller component overrides are spread last. Knowledge enables `referenceMarkers` and `headingIds` through [`referenceMarkers.ts`](referenceMarkers.ts.md): numbered prose markers become reference links, and headings receive text-derived ids with suffixes for repeated slugs and document typography. Both options default to false.
- `TaskRequirementLinks.tsx` provides the registered requirement listing for the viewed task document. Its effect clears the listing on context changes and ignores responses after cleanup. `open(path)` lifts a `{ kind: "requirements", repo, master, document, path }` target through the caller's callback when a document exists. `Markdown` and `TaskNotes` consume this context so registered packet addresses can open in the internal reader.
- The former RankBadge component and anatomy/size suite were removed with the approved Operations presentation: sprint/master rows carry no rank chevrons. Hierarchy and tier identity remain in the tree; gold/purple colours remain, while dim/ghost tokens and rank-row washes are gone. Historical V4 pip/chevron dimensions are not a supported current primitive.
- `EvidenceBadge.tsx` renders five distinct launch-evidence glyphs: `…` pending, `✓` readback, `◇` model-validated, `·` defaults and `✕` refused. The accessible name includes the tier word at both sizes, and the glyph is aria-hidden. The two direct production rendering locations are in `EvidencePane.tsx` (per-tier, `sm`) and `FailedLaunchBanner.tsx` (`refused`, with the word visible). The badge renders a supplied tier; it does not decide the tier. `EvidenceBadge.test.tsx` asserts glyph distinctness, accessible names at both sizes, glyph hiding, visible words and colour classes.

Knowledge uses the shared tree and Markdown renderer rather than separate copies of those primitives. Its code view delegates rendering to `file-viewer/FilePane.tsx`.

## Invariants And Boundaries

- Visual primitives consume data props. The requirement provider owns one explicit task-context boundary: it reads a listing, ignores stale effect responses and lifts opening actions. It does not author requirements. `ExplorerTree` separately owns tree loading, cache, expansion and selection behavior using caller-supplied data and actions.
- Panda tokens and conditions carry presentation. Within this directory, only `ModeBar` imports React Aria. Its behavior remains distinct from the shared launcher presentation. `Panel` owns its sticky header without requiring an ancestor's descendant rule.
- Motion adds emphasis and must never be a severity's sole identity. Only the `alarm` dot requests the global `pulse` animation and disables it under reduced motion; warning and information dots have no motion recipe. The retained global `pulseSlow` keyframe is not a current Dot dependency. The unlayered `html[data-effects="off"]` rule disables animation and transition with `!important`. The dot test removes animation atoms before comparing appearances, preserving the standing requirement that marks remain distinguishable at rest.
- The known dot vocabulary must come from the recipe, and the glyph table must cover that vocabulary. `DOT_VARIANTS = dot.variantMap.variant` supplies the runtime known set and the `DotVariant` type. The glyph values are explicitly authored in a total `Record<DotVariant, string>`; they are not generated from the recipe. This keeps a missing glyph a type error rather than an ambiguous rendered state.
- The unclassified dot must retain its own treatment rather than borrowing a live variant's. `Dot` accepts a free string, but its current known domain is attention severity, not task stage/activity or a former lifecycle state. The existing test asserts that each variant has an ink class different from the unknown base.
- Topology has its own `CONSTEL_STATUSES` vocabulary. Its current `worktreeStatus` reads the worktree's native task entry: no entry yields `idle`, task tone `wait` yields `warn`, `gone` yields `idle`, and other tones yield `ok`. This is not the former State-to-constellation table, and does not share Dot's severity domain or establish a coupled lifecycle-state-totality obligation.

Test descriptions above report assertions present in source, not test execution or CODE qualification. No lifecycle or acceptance status for this overview is established by these source witnesses.

## Evidence

- The Panda runtime these primitives import (`css`/`cva`/`cx`). [1]
- The React Aria condition reconciliation (data-hovered/-focused). [2]
- The route's React Aria owner wraps the viewport toggle group with the shared visual class. [3]
- ModeBar and the launcher's controls share the visual definition without sharing selection or permission policy. [10]
- The action-availability shape `Affordance` renders. [5]
- Dot covers the queue's attention severities, with a recipe-derived vocabulary, typed glyph table and resting-appearance assertions; not the removed lifecycle-state vocabulary. [6]

- Topology's distinct current native-entry-to-tone mapping does not reinstate its former State table or couple its vocabulary to Dot. [7]

- Alarm Dot uses pulse with reduced-motion suppression; shared CSS defines that pulse and the effects-off freeze, not a current awaiting-developer Dot animation. [8]

- The task column's pivot header mounts AttentionQueue; a severity mark is not an old handoff/lifecycle state mark. [9]


- Eligible large Markdown uses shared retained syntax, clones before later transforms, and opts out for short text or supplied component overrides. [11]
- Cache assertion source checks parse-once across view remounts, transform isolation and the returned view's fresh requirement callback, not execution acceptance. [12]
