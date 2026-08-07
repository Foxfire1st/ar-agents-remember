# docs/design/engine-room/ — Engine Room Design Reference Overview

| Field                  | Value                                       |
| ---------------------- | ------------------------------------------- |
| repository             | agents-remember                             |
| sourceRoute            | `docs/design/engine-room/`                  |
| doc_type               | `route-local-overview`                      |
| lastUpdated            | 2026-06-21T23:35                            |
| lastVerifiedCommitHash | `cf5ef507f2542d6cd2f9d37a6b72148d3b91b340`  |
| lastVerifiedCommitDate | 2026-08-06T13:55:47+02:00|
| governingOverview      | `../overview.md`                            |

## Governing Overview

[docs/design/ overview](../overview.md)

## Purpose

`docs/design/engine-room/` holds the **design reference** for the dashboard engine room — the bird's-eye,
worktree-lifecycle "podracer cockpit" visualization rendered by `dashboard/src/panels/engine-room/`. These
are self-contained, browser-openable HTML documents (no build, no dependencies), kept beside the code as the
durable design authority. The folder pairs a **living spec** (the canonical primitives library) with the
**prototype / scenario player** it was distilled from. The standing rule: when an engine-room visual
primitive changes, change it in the living spec **first**, then mirror it into the React engine room.

## Hot Path Summary

Two HTML design docs for the engine room: `engine-room-visual-language.html` is the canonical living spec
(state colour language — cyan = active step, amber = settled relationship, mint/green = fresh/healthy
engine, red = fault/blocked — plus motion/glow/timing tables, reduced-motion + WCAG rules, and the
GSAP/Motion implementation mapping; the source of truth, "change it here first"). `podstage.html` is the
prototype / scenario player (build-up B0→B5, tear-down D0→D6, and the full failure-mode scene library +
failure-primitive vocabulary) that the React canvas `dashboard/src/panels/engine-room/` was built from.

## Route Model

- `engine-room-visual-language.html` — the canonical living spec / primitives library. Source of truth for
  colour, motion, glow, spacing, and timing. The **§10 Failure modes** section (05o) now documents **all eight
  modes** and is **primitives-first**: one **Primitives** card grid pins the six shared primitives — scan ring,
  ghosted lane, engine-dropout halo, refused-conduit flash (red = fault/conflict, amber = soft reroute), moved
  badge, terminal STOP — then **the eight modes** (T3b/T1b/T7b/T9b/T9c/T12b/T14c/T18) render as a **2-column
  note grid**, each naming its net-new primitive (cross-refs point "(above)" to the cards). §12 maps each CSS
  primitive to the dashboard's GSAP/Motion API. The §6 engine primitive is a **flat gold bezel + constant-gold
  petals** (05o; state on the body fill).
- `podstage.html` — the prototype / scenario player the production React canvas was built from; the
  build-up/tear-down happy paths plus the full failure-mode scene library and failure-primitive CSS vocabulary.

## Invariants And Boundaries

- These are **design reference documents**, not shipped application code; they animate in CSS purely for
  portability (openable anywhere, readable in a future session). The dashboard itself does **not** animate in
  CSS — per the engine-room motion doctrine it uses GSAP timelines + Motion, CSS static-only.
- The **living spec is the source of truth**: a primitive changes here first, then the React engine room is
  updated to match. The prototype is the working scenario library behind the spec.
- The colour state language is non-negotiable and frequently re-conflated; preserve it exactly: cyan = the
  active step in-flight, amber = a settled relationship at rest, mint/green = fresh-and-healthy (engines rest
  green, never amber), red = fault (flickers) / blocked (steady).
- The realising renderer lives at `dashboard/src/panels/engine-room/`; keep this reference and that code in sync.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The React engine-room renderer these design docs govern — the two-world canvas, boot/teardown choreography, and failure overlays built from this prototype. | `EnclosureCanvas` | dashboard/src/panels/engine-room/EnclosureCanvas.tsx:42-93 |
| The parent in-repo design-documentation route this folder is a child of. | "Engine-Room Visual Language" | docs/design/engine-room/engine-room-visual-language.html:6-6 |

## Update History

- 2026-08-02T16:44:57+02:00 — L6 W1-B02 curator: repaired 2 memory-repository citations for the governed renderer overview and parent design route.
- 2026-06-22T17:00 — slice 05o doc-debt close: the living spec `engine-room-visual-language.html` **§10 Failure
  modes** was completed — it now documents **all eight** modes (was only the T3b/T1b primitive notes). Added the
  four net-new primitive cards (engine-dropout halo, refused-conduit flash red/amber, moved badge, terminal STOP)
  and restructured the section **primitives-first** (one card grid) then **the eight modes** as a 2-column note
  grid. `podstage.html` unchanged. Verification metadata pinned until closeout stamps the 05o code commit.
- 2026-06-22T10:45 — slice 05o: the living spec `engine-room-visual-language.html` §10 gained a **Mode 2 — stale-base
  block (T1b)** note pinning the pruned-base node (§3 dormant register), the code/base-lane preflight scan ring,
  and the fleeting born-blocked enclosure (§2.1 provisional) with **fast-forward** / **proceed-stale** choices —
  net-new over Mode 1 is only the pruned base node, the scan ring / fleeting block / steady gate / recovery chips
  already exist. `podstage.html` is unchanged (it already held the T1b scene this slice lifts). Verification
  metadata pinned until closeout stamps the 05o code commit.
- 2026-06-22T00:29 — slice 05o: the living spec `engine-room-visual-language.html` gained a **§10 Failure
  modes** section (the T3B scan-ring + ghosted-lane primitives; Timing/Implementation renumbered §11/§12) and a
  **§6 engine** change to a flat gold bezel (no glow) + constant-gold petals — mirrored into the React engine
  room the same slice ("change it here first"). `podstage.html` is unchanged (it already held the failure-mode
  scenes this slice lifts). Verification metadata pinned until closeout stamps the 05o code commit.
- 2026-06-21T23:35 — Created. Route overview for the engine-room design reference folder: documented the
  living spec ↔ prototype pairing, the "change it here first" source-of-truth rule, the colour state
  language, the CSS-for-portability vs GSAP/Motion-in-production split, and the link to the
  `dashboard/src/panels/engine-room/` renderer these docs govern. Governs `engine-room-visual-language.html`
  and `podstage.html`. The source files are newly added and not yet committed; verification metadata pinned
  to repo HEAD until a commit stamps them.
