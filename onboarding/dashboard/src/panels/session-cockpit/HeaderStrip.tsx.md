# dashboard/src/panels/session-cockpit/HeaderStrip.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/session-cockpit/HeaderStrip.tsx` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-08-04T00:41+02:00|
| lastVerifiedCommitHash | `842b487b854503d95c9c2d9dce1841198ba93c7d`       |
| lastVerifiedCommitDate | 2026-07-24T17:08:25+02:00|
| governingOverview      | `overview.md`                                    |

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
- **Identity dedup (R10, 260718-CHATS-L5P)** cit:(["codex codex"], dashboard/src/panels/session-cockpit/HeaderStrip.tsx:108-108): the harness label is DROPPED when it merely
  repeats the session label case-insensitively (a raw terminal literally named after its harness), so
  the header no longer stutters `codex codex` / `claude claude` — it renders the single distinct name.
- **Controls slot** cit:(["model-effort-control"], dashboard/src/panels/session-cockpit/HeaderStrip.tsx:118-118): `data-slot="model-effort-control"` mounts the one live
  `ModelEffortControl`. It can shrink after diagnostics, clips overflowing chips, and preserves
  the trigger's identity words; `controlPopover` optionally makes its open state view-controlled.
- **State cluster** cit:(["header-dot"], dashboard/src/panels/session-cockpit/HeaderStrip.tsx:132-132): `StateDot` + the grammar's state word (`seatVisualState`) — the
  same visuals as the rail row (cross-surface test).
- **Leaf context:** when `leafKey` exists, the header renders `leaf <leaf-id>` through
  `leafIdFromKey`. It intentionally renders no seat-role suffix; the focused test asserts that
  the leaf segment does not contain `seat`.
- **Freshness honesty (R15 + R3, 260718-CHATS-L5P)** cit:([`WS_WORDS`, `quiet`], dashboard/src/panels/session-cockpit/HeaderStrip.tsx:81-86; dashboard/src/panels/session-cockpit/HeaderStrip.tsx:102-102): `WS_WORDS` for the real ws
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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| HeaderStrip renders identity, one model/effort control, state, leaf-only context, and diagnostics with freshness plus optional spawn-level provenance. | `HeaderStrip`; `header-leaf`; `header-provenance-level` | dashboard/src/panels/session-cockpit/HeaderStrip.tsx:88-169 |
| Focused tests assert that leaf context omits seat-role text, model/effort is not duplicated with evidence badges or tier words, and spawn-level provenance is conditional. | "renders the §1.2 anatomy in order: identity → controls → state → leaf → diagnostics"; "one plain pair (260723): the control carries model · effort; diagnostics never duplicate it"; "renders no provenance chips for a hand-opened session — absent, never invented" | dashboard/src/panels/session-cockpit/HeaderStrip.test.tsx:17-25; dashboard/src/panels/session-cockpit/HeaderStrip.test.tsx:85-108; dashboard/src/panels/session-cockpit/HeaderStrip.test.tsx:110-115 |
| The grammar + single dot renderer the state cluster uses. | `StateDot` | dashboard/src/panels/session-cockpit/StateDot.tsx:38-61 |
| The freshness state consumed (`PerSessionCockpit`). | `PerSessionCockpit` | dashboard/src/data/sessionCockpitStore.ts:113-153 |
| The stage container mounting this as the always-on header layer. | `SessionStage` | dashboard/src/panels/session-cockpit/SessionStage.tsx:46-102 |
| The live exact-session model/effort control mounted in the slot. | `ModelEffortControl` | dashboard/src/panels/session-cockpit/ModelEffortControl.tsx:149-379 |
| The suite pins anatomy order, the mounted control, the grammar state, freshness honesty, absence of duplicated model/effort provenance, and conditional spawn-level/source provenance. | "HeaderStrip (R10)" | dashboard/src/panels/session-cockpit/HeaderStrip.test.tsx:16-116 |

## Current L5I Maintenance

The compact header no longer duplicates model/effort provenance or a seat-role fact already owned by
the control/inspector. An unclassified state is exposed to assistive technology as unavailable
without painting a false visible state word; model/effort remains one plain current pair in its
dedicated control.

## Update History

- 2026-08-04T02:20:03+02:00 — 260731-EFA-L6 S18-B06 curator delta: repaired the scoped citations against the frozen source snapshot; generated ranges were inspected and the managed index remained warm/frozen with zero source reads, tokenization, parsing, and build.

- 2026-08-04T00:41:58+02:00 — 260731-EFA-L6 S18-SR1 worker: removed both B06 semantic-residual
  scaffolds. Live prose now records leaf-id-only context with no seat-role suffix and the
  one-plain-model/effort-pair rule: diagnostics omit model evidence badges/tier words while
  retaining only optional spawn-level/source provenance. Replaced obsolete `launchTier` and
  `EvidenceBadge` ownership rows with provisional current component/test bindings; preserved the
  prior curator entry and did not run citation mechanics. Verification metadata remains pinned until
  closeout stamps the L6 code commit.
- 2026-08-04T00:28:23+02:00 — 260731-EFA-L6 S18-B06 curator: repaired current HeaderStrip citations and retained the stale seat/provenance statements as semantic residuals; final exact frozen-snapshot check is clean.
- 2026-08-02T16:55+02:00 — 260731-EFA-L6 W1-B08 curator: repaired 8 citation claims; preserved 4 Tier 3 stale provenance/seat claims and verification metadata.

- 2026-08-02T01:42+02:00 — No content impact: re-derived line range(s) that ended past the end of the file the row names (`memory_quality/style/citations`, `citation_range_out_of_bounds`). Each range was rewritten by reading the cited construct at its current location; no claim was changed to fit a range, and no range was interpolated. Verification metadata pinned until closeout stamps the L6 code commit.
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
