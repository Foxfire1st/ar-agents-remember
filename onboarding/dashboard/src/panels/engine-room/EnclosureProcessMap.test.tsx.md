# dashboard/src/panels/engine-room/EnclosureProcessMap.test.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/engine-room/EnclosureProcessMap.test.tsx` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-27T23:08+02:00                           |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`|
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `overview.md`                                    |

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

`nodeFrom(name)` pulls the first `EngineProcessNode` from a named `ENGINE_ROOM_SCENARIOS` fixture;
`WORKSPACE_ENGINES` is a two-element `ProviderNode[]` (CGC code + GrepAI memory) for the official-line
cases. A `beforeEach` sets `data-effects=off` (freeze GSAP/Motion to the After state); `afterEach` clears
it + RTL `cleanup`.

- "renders a fleeting banner …" — `engine-precontract-blocked` → asserts the `fleeting-banner` contains
  the "contract not yet written" label, the node `summary` reason, and the `nextAction` recovery choice.
- "renders no fleeting banner …, shows the pod-stage canvas" — `engine-bootstrap` (contract-anchored) →
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
  (`data-state=refused`, `data-refused-polarity=amber`, a `data-fx=refuse` flash + a `data-fx=reindex`
  center-out pulse) as a SOFT reroute — no `gate`/`terminal-stop`/`attention`. **T7B provider-plan block**:
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

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| `EnclosureProcessMap` + `EnclosureCanvas` under test (fleeting + scene + decals). | — | [EnclosureProcessMap.tsx](EnclosureProcessMap.tsx) |
| The scenario fixtures it renders. | — | [fixtures.ts](fixtures.ts) |
| The `ProviderNode` shape `WORKSPACE_ENGINES` builds. | L61-L72 | [projection.ts](../../types/projection.ts) |
| The jsdom stubs + determinism freeze. | — | [test/setup.ts](../../test/setup.ts) |

## Update History

- 2026-06-27T23:08+02:00 — Task 31 provider-state honesty: added coverage for `runtimeState="missing"` and a regression proving missing code/memory provider slots render as visible gauges. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-22T11:00 — slice 05o failure-mode primitives: added five render-test `describe` blocks (~11 cases)
  for the remaining failure-mode visuals — the T9B/T9C `refused-conduit` flash (red on the failed
  `grepai-clone` seed + engine fault, none on a clean frame, amber soft-reroute on `cgc-seed` with the
  `reindex` pulse), the T7B node-anchored `provider-block` (gate + `engine-dropout` halos + retry/disabled
  chips, NOT the fleeting box; the verify `scan-ring` at the worktree engine `cx=1084`), the T12B `moved-badge`
  (notification → ghosted-lane gate → cleared on recover), the T14C terminal `terminal-stop` (no recovery
  chips; the pre-STOP red return-lane flash beat), and the T18 `engine-boot-abandoned` dissolve/abandon record
  (matching `engine-abandoned`). Verification metadata pinned until closeout stamps the 05o code commit.
- 2026-06-22T01:10 — slice 05o T1B: added the `EnclosureCanvas — T1B failure primitives` describe — the
  stale-base block case (`engine-boot-stale-blocked`: pruned base node `data-pruned="true"`, the big red
  `fleeting-enclosure` box surfacing BOTH "fast-forward" and "proceed-stale" recovery choices) and the
  code/base-lane scan-ring gate case (`engine-boot-stale-verify`: absent under `data-effects=off`, present on
  `cy="281"` when effects on). Also retargeted the pre-contract fleeting test off the removed HTML
  `fleeting-banner` onto the canvas `fleeting-enclosure` box (BLOCKED title + summary reason + recovery
  choice). Verification metadata pinned until closeout stamps the 05o code commit.
- 2026-06-22T00:29 — slice 05o T3B: added the `EnclosureCanvas — T3B failure primitives` describe — the
  ghosted-lane case (`engine-boot-memory-blocked`: `ledger-map` conduit `data-ghosted="true"`, the code conduit
  not; steady gate + attention + reconciliation chip, no terminal STOP) and the scan-ring gate case
  (`engine-boot-memory-verify`: absent under `data-effects=off`, present with `data-fx="scan"` when effects on).
  Verification metadata pinned until closeout stamps the 05o code commit.
- 2026-06-21T23:35 — updated the sync/worktree-add collinear-conduit geometry assertion to the new column
  coordinates (`M455 281 L 735 281`, was `M480 281 L 698 281`) after the EnclosureCanvas column re-spacing
  (main right edge `COL_MAIN_CX+90` → worktree left edge `COL_WT_CX-100`). Verification metadata pinned
  until closeout stamps the code commit.
- 2026-06-21T02:27+02:00 — slice 05k: added the `EnclosureCanvas — GSAP gate (05f §8.4)` describe — two
  determinism cases that spy on `gsap.context` (added the `gsap` + `vi` imports) asserting **no** GSAP
  context is built under `data-effects=off` and one **is** built when effects are on, pinning that the canvas
  renders no live ticker under the freeze. Verification metadata pinned until closeout stamps the 05k code
  commit.
- 2026-06-19T23:58+02:00 — slice 5i: retargeted the provider-conduit path assertions to the cross-stage clone
  arcs (official→worktree `cgc-seed`/`grepai-clone` cubic paths); flipped the cleanup `dissolve` assertion to
  `toBeNull()` (worktree-side-only de-materialise); removed the three `lane-landing-source` cases (flag gone)
  and retargeted the plain/omitted-landing cases onto `remote-strip`. Verification metadata pinned until
  closeout stamps the code commit.
- 2026-06-19T15:50+02:00 — slice 5h H4 + landing-source fix: added the cleanup-teardown cases (`data-teardown=cleanup`, dissolve, `cleanup-record`, historical + back-into-main seams; abandon kept distinct) and the landing-source honesty cases (unknown/missing refs → no `lane-landing-source`; long branch name truncated with full text on hover). Verification metadata pinned until closeout stamps the code commit.
- 2026-06-19T13:57+02:00 — slice 5h H3: added the remote/PR strip cases — the `remote-strip` + `pr-badge` render on a landing arc; `origin-mem-main` planned→done across `engine-landing-ffonly`→`engine-landing-merged` (D3→D4 order); the PR badge open→merged flip; and the omit/no-throw cases for a plain enclosure and a `landing`-less node. Verification metadata pinned until closeout stamps the 5h H3 code commit.
- 2026-06-19T06:39+02:00 — engine-room crash fix: added a regression case asserting a node with `landing` omitted (pre-5h/persisted projection) renders the canvas with no landing-source flag instead of crashing. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T21:25+02:00 — slice 5h Tier 2: added the 6-column cases — the current row's real message + compact `06-18 18:19` date + 7 `td`s, and the honest empty-message/date fallback for a metadata-less row. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T18:00+02:00 — slice 5h ledger popover: added the popover cases — the `warp-coupler-ledger` button opens `ledger-popover` (highlighted row, collapsed-8 → "show 17 more" → 25 + "+15 more in memory.md"), no-rows → no trigger, and the official coupler via `OFFICIAL_LEDGER`; added `fireEvent`/`screen`. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T15:50+02:00 — slice 5h cleanup pass (feedback): added the conduit-wiring-polish cases — chevron `marker-end` only on a running flow + the `er-chev` `refX=9.6` tip, the provider conduits' box-edge-midpoint → engine-corner path `d`, the `sync`/`worktree-add` collinear centreline, and the six mirrored engine petals. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T13:01+02:00 — slice 5h coupler fix: added the ledger-coupler cases (label is the code⇄memory pair not `contract`; the chain-link glyph + the warp-surge bands render when bound). Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T11:55+02:00 — slice 5h H2: added the landing-arc cases (closeout train 5 beats on closeout-pending; integration conduit straight ff-only vs bent replay; the landing-source flag; absent for a plain enclosure). Verification metadata pinned until closeout stamps the 5h H2 code commit.
- 2026-06-17T22:45 — engine-room visual-parity + G6: added the decal-layer cases (left official-line engines
  from `workspaceEngines` + `official-wire`s + `warp-coupler-official`, none when default-empty; the
  `canopy-frame`; the `lane-ledger` annotation iff external memory) and the G6 backdrop cases (absent under
  `data-effects=off`; an `aria-hidden` `<video>` backdrop when effects on); added the `WORKSPACE_ENGINES`
  fixture. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-17T16:15 — slice 5g G5: added the live + teardown cases (t14c terminal STOP with no recovery
  chips, t12b recoverable sync gate, t18 abandon record + `data-abandoned`); registered the `integration`
  edge kind. Verification metadata pinned until closeout stamps the G5 code commit.
- 2026-06-17T12:47 — slice 5g G1: retargeted the structural cases from the linear lanes to the bird's-eye
  scene — one `conduit` per model edge, the `engine-gauge`s + bound `warp-coupler`, the `branch-node`s, and
  a gauge-runtime-from-model check; dropped the lane/flow-packet cases (the packet returns in G2).
  Verification metadata pinned until closeout stamps the G1 code commit.
- 2026-06-16T03:40 — slice 5f S4: added the power-up flow-packet cases (a `conduit-flow` packet renders only on a running/seeding conduit, T8/T9). Verification metadata pinned until closeout stamps the S4 code commit.
- 2026-06-16T03:05 — Created for slice 5f S2: render test pinning the fleeting (pre-contract blocked-start)
  banner + the SVG conduits, with motion frozen. Verification metadata pinned until closeout stamps the
  S2 code commit.
