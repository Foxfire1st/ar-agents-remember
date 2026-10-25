# docs/design/engine-room/ — Engine Room Design Reference Overview

| Field | Value |
| --- | --- |
| sourceRoute | `docs/design/engine-room/` |

## Governing Overview

[Design overview](../overview.md)

## Purpose

`docs/design/engine-room/` holds the browser-openable design references for the dashboard's bird's-eye worktree-lifecycle visualization: an official-line workspace and a worktree enclosure, with branch/commit nodes, conduits and code↔memory couplers. The folder pairs the canonical visual-primitives library with the prototype / scenario player from which it was distilled. The living spec directs authors to change a visual primitive there first, then mirror it into the React engine room at `dashboard/src/panels/engine-room/`.

Both HTML documents explicitly retire provider-engine specimens and their associated fault, seed/clone, retry and reindex scenarios as descriptions of the shipped room. Their retained demonstrations explain design history; they do not establish current renderer behavior or available public provisioning commands.

## Hot Path Summary

`engine-room-visual-language.html` is the living spec for colour, motion, glow, spacing and timing, with animated examples, reduced-motion and caption-legibility rules, and a CSS-to-GSAP/Motion implementation mapping. `podstage.html` is the choreography prototype / scenario player, retaining build-up B0→B5, tear-down D0→D6 and eight failure-mode scenes. Read the retirement notices before treating any provider-related specimen as an implementation requirement.

## How It Is Built

The design documents embed their styles and demonstration scripts and require no application build or JavaScript library imports. Their demos use CSS animation and small vanilla JavaScript drivers. The prototype also references `/assets/blueprint-boomerang.mp4` for its decorative video backdrop, so that asset is not embedded in the HTML.

The visual-language document organizes its primitives into state colours, lines/conduits, nodes, glow, packets/chevrons, engines, couplers, choreography, despawn, failure modes, timing and implementation mapping. Its failure section places six shared primitive cards first: scan ring, ghosted lane, engine-dropout halo, refused-conduit flash, moved badge and terminal STOP. A two-column note grid then describes T3b, T1b, T7b, T9b, T9c, T12b, T14c and T18. This is the retained specimen inventory, not proof that all eight scenes ship.

The retired engine specimen uses a flat gold bezel without glow, constant-gold spine and flank petals, and a body fill that carries state. Petal presence varies with state; their colour does not. The specimen describes cyan charging followed by a mint flash and steady green, red fault treatment and amber reindex treatment.

The implementation mapping points readers to `EnclosureCanvas.tsx` for the canvas, `useEngineTimeline.ts` for animation, and the boot/teardown panel. The current canvas composes scene layers and derives state through `resolveScene`. Its official-line layer renders an external-memory coupler and omits it when memory is absent. Its worktree layer retains a warp coupler whose bound state follows external-memory presence and whose visibility follows memory-worktree materialization. Neither layer renders provider engines or their wiring.

## Invariants And Boundaries

These HTML files are design references, not shipped application code. Keep the applicable living-spec primitives and their React realization in sync, while respecting the explicit retirement notices. Retained provider implementations, configuration vocabulary and historical fixtures do not restore removed public tools or provisioning routes.

Preserve the reference colour language: cyan denotes the active step in flight; amber denotes a settled relationship; mint denotes a fresh change; red denotes fault or blocked state. Active-flow dots and arrow tips belong to cyan flow. The retired engine vocabulary additionally distinguishes steady healthy green from amber relationships, flickering faults from steady blocks, and a red refused-conduit fault/conflict from an amber soft reroute.

The HTML specimens use CSS for portable demonstrations. The current canvas assigns stroke draw-ons and travelling packets to GSAP and node transitions to Motion, with CSS for static styling. The living spec requires reduced-motion end states: drawn lines remain drawn, packets hide and surges stop. The current animation hook consults `useShouldAnimate`; it creates no animation context when animation is disabled, including when the operating system requests reduced motion.

The living spec requires functional text to meet WCAG AA contrast against the canvas: at least 4.5:1 for body text and 3:1 for large/bold text. Its muted-caption floor is `oklch(0.74 0.03 250)`; faint blueprint decals are decoration rather than readable labels. These are design requirements, not a claim of independently measured implementation compliance.

The source documents disclose that mounted screenshot/video proof of these states was not captured. Reading source supplies no new test, native-host, whole-build, landing or memory acceptance. Historical citations do not establish currentness by themselves.

The retained specimens still contain contradictions: the failure-section introduction says all eight modes are built in the dashboard despite the retirement notice, and the timing table describes bottom-up engine charging and a cyan→mint→amber sweep despite the engine specimen's centre-out charge and steady-green endpoint. Treat these as unresolved design-document corrections rather than current renderer authority.

## Evidence


- The React engine-room renderer realizes the two-world canvas and lifecycle overlays, but its current official-line and worktree layers retain couplers rather than provider engines. [1]

- The Engine-Room Visual Language document declares its living-spec purpose, colour and motion doctrine, retirement boundary, specimen organization, timing/legibility rules and implementation mapping; the companion prototype preserves its scenarios with a retirement notice. [2]
