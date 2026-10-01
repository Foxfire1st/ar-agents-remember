# dashboard/src/panels/session-cockpit/HeaderStrip.tsx

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

The **HeaderStrip** (260715-FEUI-L2 S5, spec §1.2 — R10): the focused session's compact stage
header in the ruled anatomy order — identity → controls → state → leaf context → diagnostics.
The controls slot hosts the single `ModelEffortControl`; an optional controlled-popover bridge
lets palette commands open that same surface. The leaf segment renders only the leaf id, not a
duplicated seat-role fact. Diagnostics carry freshness plus optional spawn-level/source
provenance; model/effort values and their evidence are not duplicated outside the control.

## Code Commentary

### Logic

- **Anatomy + elision** (L15-L64, L94-L143): one nowrap flex strip. Identity (label + harness)
  and the state cluster are `flex: none` — they NEVER elide; leaf context is `flex: 0 2 auto`;
  diagnostics is `flex: 0 4 auto; min-width:0` — the FIRST segment to elide (highest shrink),
  matching R10's diagnostics-first elision order.
- **Identity dedup (R10, 260718-CHATS-L5P)** cit:(["codex codex"], dashboard/src/panels/session-cockpit/HeaderStrip.tsx:156-156): the harness label is DROPPED when it merely
  repeats the session label case-insensitively (a raw terminal literally named after its harness), so
  the header no longer stutters `codex codex` / `claude claude` — it renders the single distinct name.
- **Controls slot** cit:(["model-effort-control"], dashboard/src/panels/session-cockpit/HeaderStrip.tsx:165-165): `data-slot="model-effort-control"` mounts the one live
  `ModelEffortControl`. It can shrink after diagnostics, clips overflowing chips, and preserves
  the trigger's identity words; `controlPopover` optionally makes its open state view-controlled.
- **State cluster** cit:(["header-dot"], dashboard/src/panels/session-cockpit/HeaderStrip.tsx:179-179): `StateDot` + the grammar's state word (`seatVisualState`) — the
  same visuals as the rail row (cross-surface test).
- **Leaf context:** when `leafKey` exists, the header renders `leaf <leaf-id>` through
  `leafIdFromKey`. It intentionally renders no seat-role suffix; the focused test asserts that
  the leaf segment does not contain `seat`.
- **Freshness honesty (R15 + R3, 260718-CHATS-L5P)** cit:([`WS_WORDS`, `quiet`], dashboard/src/panels/session-cockpit/HeaderStrip.tsx:80-85; dashboard/src/panels/session-cockpit/HeaderStrip.tsx:146-146): `WS_WORDS` for the real ws
  state; `quiet Xs/Xm` ONLY when an output stamp exists; the tooltip states the 10 s sweep bound on
  turn-state freshness. **R3:** the diagnostics segment now filters absent parts — the `ws` word shows
  only when a pane actually reports a ws state (`freshness.ptyWs !== "none"`), so a paneless seat no
  longer prints the bare `ws —` placeholder (it collapses; the last-output age still shows when known).
- **Diagnostics provenance:** model/effort appears only as the plain pair in
  `ModelEffortControl`; diagnostics render no model provenance chip, `EvidenceBadge`, or tier
  word. An independent `spawnLevel (spawnLevelSource)` chip renders when that topology
  provenance exists. Hand-opened sessions with no spawn level render no provenance chip.

### Invariants And Boundaries

- Identity and state never elide; diagnostics always elides first — layout-pinned by the flex
  factors, order-pinned by the anatomy test.
- Model/effort truth belongs to `ModelEffortControl`; HeaderStrip diagnostics must not duplicate
  the pair or add a model evidence badge/tier. Optional spawn-level provenance is a separate fact.
- There is one model/effort control in the stable header slot. Palette actions control this same
  popover rather than mounting a second surface.

## Evidence

### Repo-Internal References

- HeaderStrip renders identity, one model/effort control, state, leaf-only context, and diagnostics with freshness plus optional spawn-level provenance. [1]
- Focused tests assert that leaf context omits seat-role text, model/effort is not duplicated with evidence badges or tier words, and spawn-level provenance is conditional. [2]
- The grammar + single dot renderer the state cluster uses. [3]
- The freshness state consumed (`PerSessionCockpit`). [4]
- The stage container mounting this as the always-on header layer. [5]
- The live exact-session model/effort control mounted in the slot. [6]
- The suite pins anatomy order, the mounted control, the grammar state, freshness honesty, absence of duplicated model/effort provenance, and conditional spawn-level/source provenance. [7]

## Current L5I Maintenance

The compact header no longer duplicates model/effort provenance or a seat-role fact already owned by
the control/inspector. An unclassified state is exposed to assistive technology as unavailable
without painting a false visible state word; model/effort remains one plain current pair in its
dedicated control.
