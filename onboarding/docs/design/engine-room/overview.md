# docs/design/engine-room/ — Engine Room Design Reference Overview

| Field                  | Value                                       |
| ---------------------- | ------------------------------------------- |
| sourceRoute            | `docs/design/engine-room/`                  |

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

## Evidence

### Repo-Internal References

- The React engine-room renderer these design docs govern — the two-world canvas, boot/teardown choreography, and failure overlays built from this prototype. [1]
- The parent in-repo design-documentation route this folder is a child of. [2]
