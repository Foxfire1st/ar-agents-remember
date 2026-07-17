# dashboard/src/panels/session-cockpit/HeaderStrip.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/session-cockpit/HeaderStrip.tsx` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T06:10+02:00                           |
| lastVerifiedCommitHash | `96e1d6db63454438b57a7485382c27784a60776f`       |
| lastVerifiedCommitDate | 2026-07-17T06:28:52+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

The **HeaderStrip** (260715-FEUI-L2 S5, spec §1.2 — R10): the focused seat's stage header line in
the RULED anatomy order — identity → controls → state → leaf/seat → diagnostics. The
ModelEffortControl slot ships EMPTY (L4 fills it; reserving it now keeps the layout stable when
the control arrives). Provenance badges (R7 — moat 1, read-only) ride the diagnostics cluster at
the tier DERIVED from row control-state truth (260715-FEUI-L3: `launchTier(session)` + the
EvidenceBadge glyph — no longer the L2 store default).

## Code Commentary

### Logic

- **Anatomy + elision** (L15-L64, L94-L143): one nowrap flex strip. Identity (label + harness)
  and the state cluster are `flex: none` — they NEVER elide; leaf/seat is `flex: 0 2 auto`;
  diagnostics is `flex: 0 4 auto; min-width:0` — the FIRST segment to elide (highest shrink),
  matching R10's diagnostics-first elision order.
- **Controls slot** (L100-L106): `data-slot="model-effort-control"` — EMPTY by design, reserved
  for L4.
- **State cluster** (L107-L110): `StateDot` + the grammar's state word (`seatVisualState`) — the
  same visuals as the rail row (cross-surface test).
- **Leaf/seat** (L111-L117): `leaf <leaf-id> · seat <role>` from `leafKey`/`spawnRole ?? seatRole`.
- **Freshness honesty (R15)** (L66-L77, L118-L125): `WS_WORDS` — `ws —` when NO pane exists in
  this cockpit yet (the pane lands in L6; absent, never faked), else the real ws state; `quiet
  Xs/Xm` ONLY when an output stamp exists; the tooltip states the 10 s sweep bound on turn-state
  freshness.
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
- The requested pair must NEVER read as effective: the tier word is derived from control-state
  truth via `launchTier` (weakest wins, never promoted without proof); per-knob SET evidence is
  L4's domain (`cockpit.launchEvidence` is written on open but not read here).
- The empty controls slot is a stable reservation — nothing may render into it before L4.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Anatomy, elision factors, freshness words, provenance badges. | L15-L147 | [HeaderStrip.tsx](HeaderStrip.tsx) |
| The grammar + single dot renderer the state cluster uses. | — | [StateDot.tsx](StateDot.tsx) |
| The freshness state consumed (`PerSessionCockpit`). | L56-L81 | [../../data/sessionCockpitStore.ts](../../data/sessionCockpitStore.ts) |
| The pure tier machine the badge tier derives from. | L29-L41 | [../../data/launchEvidence.ts](../../data/launchEvidence.ts) |
| The five-glyph badge rendered inside the provenance chip. | L13-L69 | [../../grammar/EvidenceBadge.tsx](../../grammar/EvidenceBadge.tsx) |
| The stage container mounting this as the always-on header layer. | L62-L87 | [SessionStage.tsx](SessionStage.tsx) |
| The suite: anatomy order, empty slot, grammar word, freshness honesty, derived provenance tiers. | L16-L115 | [HeaderStrip.test.tsx](HeaderStrip.test.tsx) |

## Update History

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
