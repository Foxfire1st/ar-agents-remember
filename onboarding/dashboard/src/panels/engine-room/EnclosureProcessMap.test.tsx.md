# dashboard/src/panels/engine-room/EnclosureProcessMap.test.tsx

## Governing Overview

[engine-room overview](overview.md)

## Purpose

Vitest + `@testing-library/react` render test for the Engine Room pod stage: it pins the **fleeting**
(pre-contract blocked-start) promote-in-place rendering plus the **bird's-eye scene** (5g G1) — the flow
conduits, podracer engine gauges, warp coupler, branch nodes, and the visual-parity **decal layer**
`EnclosureCanvas` renders from the model — with motion frozen (`data-effects=off`) so assertions are
deterministic.

## Code Commentary

### Logic

### 260712-TRH-L7 stale landing regression

The focused canvas case renders a stale landing ref with its stale tone, literal state, and age, then asserts no landing-flow packet is active. This pins the contract that unavailable remote truth stays visible without being animated as current.

`nodeFrom(name)` pulls the first `EngineProcessNode` from a named `ENGINE_ROOM_SCENARIOS` fixture;
`WORKSPACE_ENGINES` is a two-element `ProviderNode[]` (CGC code + GrepAI memory) for the official-line
cases. A `beforeEach` sets `data-effects=off` (freeze GSAP/Motion to the After state); `afterEach` clears
it + RTL `cleanup`.

- "renders a fleeting banner …" — `engine-precontract-blocked` → asserts the `fleeting-banner` contains
  the "contract not yet written" label, the node `summary` reason, and the `nextAction` recovery choice.
- "renders no fleeting banner …" — `engine-bootstrap` (contract-anchored) →
  no `fleeting-banner`; `process-map` + `enclosure-canvas` present.
- (05k) `describe("EnclosureCanvas — GSAP gate (05f §8.4 — no ticker under effects=off)")` — two cases that
  spy on `gsap.context` (importing `gsap` + `vi`) to pin the honest-motion gate **both ways**: under
  `data-effects=off` (the `beforeEach` default) rendering the canvas **builds no GSAP context**
  (`expect(spy).not.toHaveBeenCalled()` — deterministic, no live ticker), and with the attribute removed
  (effects on) it **does** (`expect(spy).toHaveBeenCalled()` — proving the gate isn't a vacuous assert). The
  canvas wires `useEngineTimeline` unconditionally, so the gate is what keeps the snapshots stable.
- (5g G1) bird's-eye scene assertions on `engine-bootstrap`: one `conduit` per known model edge; both
  `engine-gauge`s + the `warp-coupler` bound iff external memory; the official + worktree `branch-node`s
  (4 when external); every gauge's `data-runtime` is a valid runtime state (state lives in the model, not
  the class name). Task 31 extends the valid set with `missing` and adds a focused case proving missing
  provider slots render as two visible missing gauges instead of being dropped.
- (visual-parity) decal-layer assertions on `engine-bootstrap`: with `workspaceEngines` supplied the
  official-line engines render on the **left** (gauge count = right + 2) with their `official-wire`s and the
  `warp-coupler-official` (iff external memory); with the default empty `workspaceEngines` there are none
  (gauge count unchanged, no `official-wire`); the `canopy-frame` HUD frame is always present; the
  `lane-ledger` annotation shows iff external memory.
- (5g G5) live + teardown cases: `engine-integration-conflict` renders a `terminal-stop` with **no**
  `recovery-chips` and no thin `gate` (a terminal conflict is human-only) while still raising `attention`;
  `engine-sync-needed` (t12b) shows a recoverable `gate` + a `worktree_sync` chip and **no** `terminal-stop`;
  `engine-abandoned` (t18) marks `process-map[data-abandoned]` and renders the `abandon-record` with no
  chips/attention. `KNOWN_EDGE_KINDS` gained `integration`.
- (5g G6) backdrop: no `backdrop` under `data-effects=off`; with effects on, an `aria-hidden` `backdrop`
  holding a `<video>` mounts.
- (5h H2 → 5i) landing arc: `engine-landing-closeout` plays the `closeout-train` (5 beats); the `integration`
  conduit is straight for `ff-only` (`engine-landing-ffonly`, no `data-strategy`) and bent for `replay`
  (`engine-landing-merged`, `data-strategy=replay`). **5i** removed the `lane-landing-source` assertions (the
  flag is gone — the official-line advance now reads through the dock + flows): a plain (non-landing)
  enclosure now asserts **no `closeout-train` and no `remote-strip`**, and a node whose projection **omits**
  `landing` (pre-5h/persisted data) still renders the `enclosure-canvas` with **no `remote-strip`** (the
  crash-guard regression, retargeted off the removed flag).
- (5h coupler fix) ledger coupler: the coupler labels with its `code ⇄ memory` pair (not `contract`); the
  `warp-link` chain-link glyph + the bound-only `warp-surge` bands render.
- (5h cleanup) conduit wiring polish: a `running` conduit (`engine-setup-running` GrepAI clone) carries the
  `er-chev` `marker-end` while a complete one does not (tips only on an action); the `er-chev` `refX` is
  `9.6` (the arrowhead lands on the line end, no overshoot into the engine); each provider conduit's path
  `d` runs box-edge-midpoint → engine inner corner (`cgc-seed` = `M900 281 L 1057 198`, `grepai-clone` =
  `M900 403 L 1057 452`); the `sync` lane is collinear with `worktree-add` (both `M455 281 L 735 281` after the 2026-06-21
EnclosureCanvas column re-spacing — main right edge `COL_MAIN_CX+90` → worktree left edge `COL_WT_CX-100`;
was `M480 281 L 698 281`); and a
  gauge fans six petals with mirrored flanks (left + right midpoints both `[24, 48, 72]`). **5i retargeted the
provider-conduit path assertions**: the seed/clone now **sweeps across the stage from the official engine to
the worktree engine** (cloned-from, not box-edge→corner) — `cgc-seed` bows over the top
(`M135 150 C 345 34, 847 34, 1057 150`), `grepai-clone` under the bottom (`M135 500 C 345 604, 847 604, 1057 500`).
- (5h ledger popover) clicking a coupler's `warp-coupler-ledger` button opens the `ledger-popover` (portaled,
  via `screen`/`findByTestId`) with this enclosure's row highlighted (`08e9221a`); it starts collapsed at 8
  rows with a "show 17 more" control, extends to the 25-row served window with a "+15 more in memory.md"
  footer, and a coupler with no rows (no `officialLedger`) renders no trigger; the official coupler
  (`warp-coupler-official-ledger`, fed `OFFICIAL_LEDGER`) opens the same way. Uses `fireEvent` + `screen`.
- (5h Tier 2) ledger columns: the popover row renders **6 columns** — the highlighted current row shows the
  real commit message + the compact `06-18 18:19` date and has 7 `td`s (date · msg · hash · ⇄ · hash · msg ·
  date); a row with no probed metadata (a node overridden to a bare `ledgerRows` entry) keeps both hashes
  with empty message/date cells — the honest fallback.
- (5h H3) remote/PR strip: `engine-landing-ffonly` renders the `remote-strip` (containing `origin/main`) and a
  `pr-badge` (`PR #128`); the `origin-mem-main` chip stays `data-tone=planned` while the PR is open and becomes
  `done` once `engine-landing-merged` (the code-first / memory-after D3→D4 order); the `pr-badge` `data-state`
  flips `open` → `merged` on the projection state; a plain enclosure (`engine-bootstrap`) renders **no**
  `remote-strip`, and a node with `landing` deleted still renders the `enclosure-canvas` with no strip (never
  throws).
- (5h H4 → 5i) cleanup teardown: `engine-cleanup-pending` → `process-map[data-teardown=cleanup]`, a
  `cleanup-record` (`✓ Landed`), the `lane-historical` chip and the `lane-back-into-main` seam (`origin/main`);
  NOT an `abandon-record` and `data-abandoned` unset. **5i flips the dissolve assertion to `toBeNull()`** — a
  landed cleanup de-materialises only the worktree side, so it does **not** wrap in the full-dim `dissolve`
  shell (that stays abandon-only; abandon still asserts the dissolve present).
- (5i) the three `lane-landing-source` cases (advance-to-tip, unknown/missing → no flag, long-name truncation)
  were **removed** — the flag no longer exists; the official-line advance reads through the remote dock + the
  directional landing flows instead.
- (05o) `describe("EnclosureCanvas — T3B failure primitives")` — two cases on the new `boot-demo` block
  fixtures. "ghosts the gated memory lane …" renders `engine-boot-memory-blocked` (effects off) and asserts the
  `ledger-map` conduit carries `data-ghosted="true"` while the `worktree-add` (code) conduit does **not**, plus
  the recoverable-block signature (a `gate` + `attention` + a `reconciliation` recovery chip, **no**
  `terminal-stop`). "sweeps the cyan scan ring …" proves the transient ring is gated on `animate`: under the
  `data-effects=off` default `scan-ring` is **absent** (`cleanup()` then) with the attribute removed it renders
  with `data-fx="scan"` — so the verify sweep freezes under reduced-motion like the packet.
- (05o T1B) `describe("EnclosureCanvas — T1B failure primitives")` — two cases on the stale-base `boot-demo`
  fixtures. "prunes the stale base node …" renders `engine-boot-stale-blocked` and asserts the main code
  (base) node reads pruned (`[data-pruned="true"]` present) and that the FLEETING born-blocked
  `fleeting-enclosure` box surfaces **both** recovery choices ("fast-forward" and "proceed-stale"). "sweeps
  the scan ring on the CODE/base lane …" gates the ring on `animate` the same way as T3B but on the base lane:
  absent under the `data-effects=off` default, and with the attribute removed it renders on `cy="281"` (the
  code/base lane, vs the T3B memory verify at `y=403`). This slice also **retargeted** the pre-contract
  fleeting test off the removed HTML `fleeting-banner` onto the canvas `fleeting-enclosure` box — the
  `engine-precontract-blocked` case now asserts the box's `BLOCKED` title, the `node.summary` reason, and the
  `nextAction` recovery choice (and the contract-anchored case asserts **no** `fleeting-enclosure`).
- (05o failure-mode primitives) five further `describe` blocks (~11 cases) pin the remaining failure-mode
  visuals. **T9B/T9C refused-conduit** (effects on): `engine-boot-seed-fault` flashes exactly one
  `refused-conduit` on the failed `grepai-clone` lane with `data-polarity=red` + `data-fx=refuse` while the
  GrepAI engine raises a single `data-fx=fault` (CGC unaffected); a clean `engine-boot-4-seeding` frame shows
  **no** `refused-conduit`; and `engine-cgc-seed-refused` flashes the `cgc-seed` lane **amber**
  (the conduit asserts `data-state=stale` and, positively, `data-refused-polarity` **`toBeNull()`** — the
  polarity is DERIVED by the renderer, so the conduit carries nothing to assert it from; the amber is read
  off the flash's own `data-polarity`, alongside a `data-fx=refuse` flash + a `data-fx=reindex`
  center-out pulse) as a SOFT reroute — no `gate`/`terminal-stop`/`attention`. The null assertion is the
  regression guard: it fails the moment a polarity field is put back on the edge. The test title reads
  "AMBER (stale reroute)". **T7B provider-plan block**:
  `engine-boot-provider-blocked` renders the node-anchored `provider-block` (NOT the `fleeting-enclosure` box —
  that stays T1B/stale-base), the `engine-dropout` halos over the unlit engine slots, a steady `gate` +
  `attention`, and retry/disabled-led `recovery-chips` (the 4th `abandon` is clipped by the 3-chip cap); the
  paired `engine-boot-provider-verify` gates the `scan-ring` on effects (absent under `data-effects=off`,
  present at the worktree CGC engine `cx=1084`/`cy=150` when on). **T12B moved badge**: `engine-sync-moved`
  shows the soft `moved-badge` (the notification before the gate), `engine-sync-memory-blocked` gates +
  ghosts the `ledger-map` lane (`data-ghosted=true`) while `worktree-add` stays solid and offers merge/skip
  `recovery-chips`, and `engine-sync-recovered` clears both `node-block` + `moved-badge`. **T14C terminal**:
  `engine-integration-conflict` renders the steady `terminal-stop` (`data-kind=integration`, "STOP") with NO
  `gate`/`recovery-chips` but still raising `attention`, and the transient `engine-integration-conflict-flash`
  beat flashes red `refused-conduit`s on the `integration`/`integration-mem` return lanes **before** the STOP
  appears (no `terminal-stop` yet on the flash beat). **T18 dissolve/abandon**: the `boot-demo`
  `engine-boot-abandoned` dissolves identically to `engine-abandoned` — a `dissolve` shell,
  `data-abandoned=true`, `data-teardown=abandon`, an `abandon-record`, the `lane-historical` chip, and (a
  decision, not a block/land) no recovery chips, attention, remote strip, or cleanup record.

### Invariants And Boundaries

Pure render assertions (no animation timing) — relies on the shared `test/setup.ts` jsdom stubs
(`matchMedia` for `useShouldAnimate`) and the `data-effects=off` freeze so the canvas mounts at the After
state with no RAF/ticker dependency. The 05k GSAP-gate cases assert that contract directly by spying on
`gsap.context` (not called under effects-off, called when effects are on). Plain
`container.querySelector` / `getByTestId` (no `jest-dom`). The official-line
cases pass `workspaceEngines` explicitly (the prop defaults to `[]`, so the existing scene-count
assertions stay right-world-only).

Assert on states the server can emit. The T9C case reads `data-state=stale` off the conduit because
`stale` is what `_seed_edge_state` returns for a reroute; the previous `data-state=refused` assertion
pinned a value no reducer path produces, so it could only ever have been satisfied by a fixture that
described an impossible payload. Its companion `data-refused-polarity` `toBeNull()` is a deliberate
negative — it is the assertion that would fail if a polarity field were reintroduced on the edge.

## Evidence

### Repo-Internal References

- `EnclosureProcessMap` + `EnclosureCanvas` under test (fleeting + scene + decals). [1]
- The scenario fixtures it renders; `engine-cgc-seed-refused` now seeds `edges({ cgc: "stale", … })`. [2]
- The T9B/T9C refused-conduit describe block, including the `data-state=stale` / `data-refused-polarity` null pair. [3]
- `refusedPolarityOf` — the derivation the test's amber expectation depends on. [4]
- `_seed_edge_state` — why `stale` is the honest reroute state to assert. [5]
- The `ProviderNode` shape `WORKSPACE_ENGINES` builds. [6]
- The jsdom stubs + determinism freeze. [7]

## Current L5I Maintenance

The map suite now drives intersection changes to prove that all GSAP context tweens pause/resume
without rebuilding and that the blueprint video pauses off-screen. It also pins the full-geometry
warp-surge inputs used by transform animation.

## 260727-CHATS-IM-L2 Current Delta

The animated-mode regression asserts that the structural canvas has no repeating `data-fx`
targets and the sparse overlay owns surge and reindex targets. Existing effects-off tests continue
to pin the static scene.
