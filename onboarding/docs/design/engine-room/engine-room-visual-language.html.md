# engine-room-visual-language.html

| Field                  | Value                                                |
| ---------------------- | ---------------------------------------------------- |
| repository             | agents-remember                                      |
| path                   | `docs/design/engine-room/engine-room-visual-language.html` |
| doc_type               | `file-level-onboarding`                              |
| lastUpdated            | 2026-06-21T23:35                                     |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`           |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview      | `overview.md`                                        |

## Governing Overview

[engine-room/ design overview](overview.md)

## Purpose

`engine-room-visual-language.html` is the **canonical living spec** for the engine-room
visual primitives — the single source of truth for the dashboard engine room's colour,
motion, glow, spacing, and timing. It is a self-contained, dependency-free HTML page meant
to be opened in a browser: each primitive (lines, nodes, engines, coupler, packets,
choreography, despawn) is shown as a live, animated example next to the semantic it carries
and the exact parameters (ease, duration, OKLCH colour, glow radius). When a developer wants
to change an engine-room primitive, they point at it **by name** from this page, and the rule
is "change it here first, then mirror it in the React engine room." It exists so the visual
language survives across sessions and stays legible without running the dashboard.

## Code Commentary

### Logic

The page is a `<style>` block + a sectioned `<body>` + a small vanilla `<script>` that drives
each demo with tiny loops (`loopFlow`, `loopFresh`, `loopBind`, `loopBoot`, `loopDissolve`,
`loopChoreo`) so it animates with no library dependency. The sections (numbered in the sticky
TOC) are:

- **§0 How to read this** — the doctrine. The recurring "one rule that keeps getting lost":
  **cyan = the ACTIVE step in-flight** (grows in, holds with a travelling dot, retracts);
  **amber = a SETTLED relationship at rest** (a plain static line, retracts only when the
  relationship is terminated); **mint/green = just changed / landed / booted**;
  **red = fault or blocked**. A line is cyan only while its step is active, then drops to amber.
  Dots and arrow-tips ride only the active cyan flow. The one exception: **engines rest green**
  (healthy), never amber — amber is for settled *relationships*, green is a healthy *engine*.
- **§1 State colours** — the five state colours plus two neutrals as OKLCH swatches
  (`--amber`, `--cyan`, `--mint`, `--alarm`, `--dormant`, `--ink`, `--muted`), copied verbatim.
- **§2 Lines & conduits** — four non-interchangeable line types: active flow (cyan, animated),
  settled wire (amber, static), planned/not-yet (dim dashed), blocked (steady red gate, never flicker).
- **§3 Nodes & boxes** — commit/branch boxes: default (amber), derived/provisional (dashed cyan),
  fresh/landed (mint stroke + glow, event-driven not perpetual), pruned/retired (dormant).
- **§4 Glow scale** — glow is `filter:drop-shadow` only (GPU-cheap, colour-tintable); blur radius
  scales with importance (2px structural → 7px alarm) and the glow colour equals the state colour.
- **§5 Packet & chevron** — the travelling packet (`offset-path`, one per active flow) and the
  chevron tip (`stroke="context-stroke"` so it inherits the path's live colour).
- **§6 Engines** — the provider engine (CGC / GrepAI): a **flat** constant gold bezel (05o — **no glow**; §4's
  glow scale is reserved for the active body + the fault halo, never the frame). The body **fills from the
  middle outward** (`scaleY` from centre) to full turquoise, then flashes up and **dims to green** and rests
  green; the **spine + fanned petals are constant gold** structural line-art (05o — state is the body fill, not
  the frame or petals; only petal *presence* varies). Faults breathe red gently (a red body + halo); reindex
  pulses amber. Includes the note that scanlines are a global CRT overlay, not part of the engine glyph.
- **§7 Coupler / warp-core** — the code⇄memory coupler is the **memory.md ledger link**; a thick
  amber bar with a chain-link glyph (two interlocking rings) that brightens on bind and pumps a
  bidirectional white surge.
- **§8 Choreography** — the eye-leading principle: within a phase, paired elements are staggered
  300–650ms so exactly one focal point moves through the scene; never light two things at once.
- **§9 Retract & despawn** — things leave deliberately (retract / dissolve), never blink out.
- **§10 Failure modes** (05o, net-new — **all eight built + documented**) — when the lifecycle can't just
  proceed it **blocks, gates, recovers** (or terminates). The section is **primitives-first**: one card grid
  pins the six shared primitives — the **scan ring** (cyan pre-block verify sweep, expand+fade ~1.2s,
  transient), the **ghosted lane** (`opacity .32` + `grayscale .45` on a held lane while its sibling proceeds —
  real-but-held, distinct from `planned`), the **engine-dropout halo** (dashed alarm outline over an unlit held
  engine slot — T7b), the **refused-conduit flash** (cyan→white→polarity colour→fade; **red** = fault/conflict,
  **amber** = soft reroute — T9b/T9c/T14c), the **moved badge** (soft cyan ▲ upstream-moved notification —
  T12b), and the **terminal STOP** (the reason banner ABOVE the lane + a gap-sized red bar — T14c). After the
  primitives, **the eight modes** render as a **2-column note grid** — T3b memory/ledger block, T1b stale-base
  block (pruned §3 base node + fleeting §2.1 enclosure), T7b provider-plan block, T9b seed fault, T9c reindex
  reroute (soft amber), T12b live sync (Steady-state panel), T14c integration conflict (terminal), T18 abandon
  (dissolve §9) — each naming its net-new primitive(s); everything else reused from §§1–9. Doctrine: a block is
  steady, a fault flickers — they must never look alike.
- **§11 Timing & easing reference** — the canonical duration/easing table (copy verbatim), plus the
  WCAG AA caption-legibility rule against the dark canvas.
- **§12 Implementation mapping** — maps each CSS technique here to the dashboard's GSAP/Motion API,
  and names where the code lives (`EnclosureCanvas.tsx`, `useEngineTimeline.ts`, `engineRoomStyles.ts`,
  `BootTimeline.tsx`). 05o adds the scan-ring (GSAP `data-fx='scan'`) + ghosted-lane (Panda `ghostedLane`) rows.

### Conventions

- Colours are authored in **OKLCH** as CSS custom properties on `:root` and meant to be copied verbatim
  into the React tokens. The semantic comment beside each token (`/* SETTLED relationship */` etc.) is load-bearing.
- The spec **animates in CSS** purely for portability ("opens anywhere"). This is a deliberate exception
  to the dashboard's no-CSS-animation motion doctrine: the production engine room uses **GSAP timelines +
  Motion**, CSS static-only. §11 is the bridge.
- Every recolour crossfades over `.45s ease` (the global ease on `stroke`/`fill`); nothing hard-cuts.
- Primitive CSS classes mirror the prototype `podstage.html` and the React recipe names (`.flowpath`,
  `.wire`, `.node`, `.prov`, `.coupler-g`, `.e-charge`, `.e-petal`) so the three stay 1:1.

### Invariants And Boundaries

- This file is **the source of truth** for engine-room colour/motion/glow/timing. When a primitive changes,
  it changes **here first**, then the React engine room is updated to match.
- The colour semantics are non-negotiable and the most frequently re-conflated: cyan = active step,
  amber = settled relationship, mint/green = fresh/healthy engine (engines rest green, never amber),
  red = fault (flickers) / blocked (steady). Fault must read differently from a block (flicker vs steady).
- Reduced motion is mandatory: every animated primitive freezes to its end-state under
  `prefers-reduced-motion: reduce` (GSAP `matchMedia` in the dashboard) — motion is never required to read
  state, colour alone is sufficient.
- This is a **design reference document**, not shipped application code; it does not import or run anything
  from the dashboard. It must stay in sync with the React engine room but does not drive it.

### Todos

None tracked outside active task work. The footer states the standing obligation: keep this file, the
dashboard, and the onboarding in sync.

## Docs References

This file is itself the canonical engine-room design reference; the relevant external context is the
animation stack it maps onto in §11. No external documentation was required to describe this self-contained
spec. No relevant documentation found after checking live sources.

| Finding | Anchor | Source |
| --- | --- | --- |
| The §11 implementation mapping names the GSAP/Motion stack (DrawSVG, MotionPath, AnimatePresence, layoutId, matchMedia) the dashboard uses to realise these CSS-authored primitives. | "GSAP DrawSVGPlugin" | docs/design/engine-room/engine-room-visual-language.html:913-913 |

## Repo-Internal References

The spec is the design authority distilled from the `podstage.html` prototype and realised by the React
engine-room renderer. The two cross-links below are the proving pair: the prototype it distils and the
renderer it governs.

| Finding | Anchor | Source |
| --- | --- | --- |
| The companion prototype / scenario player this spec distils into a primitives library; the spec's CSS classes mirror it 1:1. | "h1>Engine Room · Pod Stage</h1>" | docs/design/engine-room/podstage.html:162-162 |
| The React engine-room renderer implements these primitives in `EnclosureCanvas.tsx`. | `EnclosureCanvas` | dashboard/src/panels/engine-room/EnclosureCanvas.tsx:1191-1711 |
| The React engine-room renderer drives the GSAP timeline from `useEngineTimeline.ts`. | "export function useEngineTimeline" | dashboard/src/panels/engine-room/useEngineTimeline.ts:168-168 |
| The React engine-room renderer's static styles live in `engineRoomStyles.ts`. | "Static layout only" | dashboard/src/panels/engine-room/engineRoomStyles.ts:599-599 |
| The React engine-room renderer's boot timeline lives in `BootTimeline.tsx`. | `BootTimeline` | dashboard/src/panels/engine-room/BootTimeline.tsx:155-177 |

## Cross-Repo References

This is an in-repo design reference with no cross-repository or external-system boundary. No meaningful
cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| _None._ | — | — |

## Update History

- 2026-08-02T21:14+02:00 — W2-B03 curator: resolved 6 initial citation findings (3 anchor, 0 prose, 3 source); scoped recheck PASS (0 findings). Verification metadata unchanged.

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->

- 2026-06-22T17:00 — slice 05o doc-debt close: **§10 Failure modes completed** — now documents **all eight**
  modes (T3b/T1b/T7b/T9b/T9c/T12b/T14c/T18), not just the scan-ring + ghosted-lane primitives. Added the four
  net-new primitive cards (engine-dropout halo, refused-conduit flash red/amber, moved badge, terminal STOP)
  and **restructured** the section: a single **Primitives** card grid first, then **the eight modes** as a
  2-column note grid; cross-references flipped to "(above)". CSS gained `.refuse`/`.dropout`/`.stop-*`/`.moved-*`
  + `.grouphead`/`.modegrid`. Verification metadata pinned until closeout stamps the 05o code commit.

- 2026-06-22T10:45 — slice 05o: the **§10 Failure modes** section gained a **Mode 2 — stale-base block (T1b)** note.
  Before the worktree forks, the scan ring sweeps the **code/main lane** (is local main current with upstream?);
  on a behind/diverged base a **fleeting enclosure is born blocked** (§2.1, contract not yet written) with the
  stale **main node pruned** (the §3 dormant register) and two choices — **fast-forward** or **proceed-stale**.
  Its only net-new piece vs Mode 1 is the pruned base node; the scan ring, fleeting block, steady gate, and
  recovery chips already exist. Verification metadata pinned until closeout stamps the 05o code commit.
- 2026-06-22T00:29 — slice 05o: the spec gained a **§10 Failure modes** section (pinning the T3B
  **scan ring** + **ghosted lane** primitives; TOC + the §12 implementation table updated; Timing renumbered
  §10→§11, Implementation §11→§12), and the **§6 Engines** primitive was changed to a **flat gold bezel (no
  glow)** + **constant-gold spine/petals** (the `.e-frame` `drop-shadow` dropped; the `.e-petal` state strokes
  collapsed to a base amber, opacity-only variants) — mirrored into the React engine room (`engineRoomStyles`)
  the same slice per "change it here first". Verification metadata pinned until closeout stamps the 05o code commit.
- 2026-06-21T23:35 — Created. File-level onboarding for the engine-room visual-language living spec
  (the canonical colour/motion/glow/timing source of truth for the dashboard engine room): documented the
  state colour language, the eleven sections, the source-of-truth invariant ("change it here first"), the
  reduced-motion + WCAG rules, the CSS-for-portability / GSAP+Motion-in-production split, and the cross-link
  to the `podstage.html` prototype and the `dashboard/src/panels/engine-room/` renderer. The source file is
  newly added and not yet committed; verification metadata pinned to repo HEAD until a commit stamps it.
