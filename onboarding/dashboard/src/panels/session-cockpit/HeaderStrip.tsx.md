# dashboard/src/panels/session-cockpit/HeaderStrip.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/session-cockpit/HeaderStrip.tsx` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-07-24T13:17:17Z |
| lastVerifiedCommitHash | `842b487b854503d95c9c2d9dce1841198ba93c7d`       |
| lastVerifiedCommitDate | 2026-07-24T17:08:25+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

The **HeaderStrip** (260715-FEUI-L2 S5, spec §1.2 — R10): the focused seat's stage header line in
the RULED anatomy order — identity → controls → state → leaf/seat → diagnostics. The
controls slot now hosts FEUI-L4's single `ModelEffortControl`; an optional controlled-popover
bridge lets palette commands open that same surface. Provenance badges (R7 — moat 1, read-only)
ride the diagnostics cluster at
the tier DERIVED from row control-state truth (260715-FEUI-L3: `launchTier(session)` + the
EvidenceBadge glyph — no longer the L2 store default).

## Code Commentary

### Logic

- **Anatomy + elision** (L15-L64, L94-L143): one nowrap flex strip. Identity (label + harness)
  and the state cluster are `flex: none` — they NEVER elide; leaf/seat is `flex: 0 2 auto`;
  diagnostics is `flex: 0 4 auto; min-width:0` — the FIRST segment to elide (highest shrink),
  matching R10's diagnostics-first elision order.
- **Identity dedup (R10, 260718-CHATS-L5P)** (L112-L120): the harness label is DROPPED when it merely
  repeats the session label case-insensitively (a raw terminal literally named after its harness), so
  the header no longer stutters `codex codex` / `claude claude` — it renders the single distinct name.
- **Controls slot** (L119-L133): `data-slot="model-effort-control"` mounts the one live
  `ModelEffortControl`. It can shrink after diagnostics, clips overflowing chips, and preserves
  the trigger's identity words; `controlPopover` optionally makes its open state view-controlled.
- **State cluster** (L107-L110): `StateDot` + the grammar's state word (`seatVisualState`) — the
  same visuals as the rail row (cross-surface test).
- **Leaf/seat** (L111-L117): `leaf <leaf-id> · seat <role>` from `leafKey`/`spawnRole ?? seatRole`.
- **Freshness honesty (R15 + R3, 260718-CHATS-L5P)** (L66-L77, L150-L162): `WS_WORDS` for the real ws
  state; `quiet Xs/Xm` ONLY when an output stamp exists; the tooltip states the 10 s sweep bound on
  turn-state freshness. **R3:** the diagnostics segment now filters absent parts — the `ws` word shows
  only when a pane actually reports a ws state (`freshness.ptyWs !== "none"`), so a paneless seat no
  longer prints the bare `ws —` placeholder (it collapses; the last-output age still shows when known).
- **Provenance badges (R7, L3-derived)** (L93-L95, L130-L143): the launch tier comes from the
  PURE tier machine on catalog row truth — `evidenceTier = launchTier(session)` (L95), never from
  the open response or the L2 store default, so the header is honest for rows launched by ANY
  actor. The model chip renders `model <resolvedModel> · <effort>` + an
  `<EvidenceBadge tier size="sm">` glyph + the tier word (`pending` reads as "(requested)", else
  the tier itself, e.g. "(model-validated)" for a ready Claude pair — stream-json emits no
  launch-effort echo, so Claude's pair ceiling is model-validated); plus `spawnLevel
  (spawnLevelSource)`; hand-opened sessions with no provenance render NO chips (absent, never
  invented).

### Invariants And Boundaries

- Identity and state never elide; diagnostics always elides first — layout-pinned by the flex
  factors, order-pinned by the anatomy test.
- The requested launch pair must NEVER read as effective: its tier word derives from control-state
  truth via `launchTier`; the adjacent L4 control separately renders per-knob snapshot/echo/set
  evidence.
- There is one model/effort control in the stable header slot. Palette actions control this same
  popover rather than mounting a second surface.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Anatomy, elision factors, freshness words, provenance badges. | L15-L147 | [HeaderStrip.tsx](HeaderStrip.tsx) |
| The grammar + single dot renderer the state cluster uses. | — | [StateDot.tsx](StateDot.tsx) |
| The freshness state consumed (`PerSessionCockpit`). | L56-L81 | [../../data/sessionCockpitStore.ts](../../data/sessionCockpitStore.ts) |
| The pure tier machine the badge tier derives from. | L29-L41 | [../../data/launchEvidence.ts](../../data/launchEvidence.ts) |
| The five-glyph badge rendered inside the provenance chip. | L13-L69 | [../../grammar/EvidenceBadge.tsx](../../grammar/EvidenceBadge.tsx) |
| The stage container mounting this as the always-on header layer. | L62-L87 | [SessionStage.tsx](SessionStage.tsx) |
| The live exact-session model/effort control mounted in the slot. | L148-L383 | [ModelEffortControl.tsx](ModelEffortControl.tsx) |
| The suite: anatomy order, mounted control, grammar word, freshness honesty, derived provenance tiers. | L16-L117 | [HeaderStrip.test.tsx](HeaderStrip.test.tsx) |

## Current L5I Maintenance

The compact header no longer duplicates model/effort provenance or a seat-role fact already owned by
the control/inspector. An unclassified state is exposed to assistive technology as unavailable
without painting a false visible state word; model/effort remains one plain current pair in its
dedicated control.

## Update History

- 2026-07-24T13:17:17Z — Curator: documented header decluttering and unavailable-state accessibility
  copy; verification fields remain pre-commit.

- 2026-07-21T05:30+02:00 — 260718-CHATS-L5P curator: recorded R10 identity dedup (harness label dropped
  when it case-insensitively equals the session label — no `codex codex` stutter) and the R3 diagnostics
  collapse (the `ws` word shows only with a real pane; no bare `ws —` on a paneless seat). Anatomy,
  controls slot, provenance badges unchanged. Verification pinned to the leaf base (`352d5cd`) until
  closeout stamps the candidate commit.
- 2026-07-17T08:33+02:00 — 260715-FEUI-L4 R2 filled the reserved controls slot with the sole
  `ModelEffortControl`, added the controlled-popover bridge used by palette commands, and gave
  its chips bounded shrink/overflow behavior without changing header anatomy. Verification
  metadata is pinned to the contract base until code commit.
- 2026-07-17T06:10+02:00 — 260715-FEUI-L3 (R7): the launch tier now DERIVES from row
  control-state truth (`launchTier(session)` — starting⇒pending/"(requested)", ready Claude
  pair⇒"(model-validated)", failed⇒refused) instead of the L2 store default, and the provenance
  chip gains the `<EvidenceBadge size="sm">` glyph beside the tier word; testids/segments
  unchanged. Verification metadata pinned to the leaf base until closeout stamps the L3 code
  commit.
- 2026-07-17T02:30+02:00 — Created for 260715-FEUI-L2 S5 (R7/R10/R15): the §1.2 header anatomy
  with diagnostics-first elision and never-eliding identity/state, the reserved EMPTY
  ModelEffortControl slot, the shared-grammar state cluster, honest per-pane freshness (`ws —`,
  quiet age, sweep-bound tooltip), and requested-tier provenance badges. Verification metadata
  pinned to the leaf base until closeout stamps the L2 code commit.
