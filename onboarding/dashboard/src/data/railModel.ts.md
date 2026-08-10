# dashboard/src/data/railModel.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/railModel.ts`                |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-07-26T15:40+0200 |
| lastVerifiedCommitHash | `a84add4c9422b18a26f1748dedaed16194994ded`       |
| lastVerifiedCommitDate | 2026-08-10T05:11:18+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[data overview](overview.md)

## Purpose

The **session-rail model** — pure, React-free derivations for the RULED
role-driven hierarchy (spec §1.6b, ruled 2026-07-16): architect / orchestrator / manager render as
a FLAT command spine (never spawn-edge nesting); only leaf agents indent, clustered per leaf under
their manager, base order worker → reviewer → curator with the ACTIVE seat sorted to the top;
completed seats fold into a per-master collapsed folder (R17). An earlier
analysis diagnosed the spawn-edge forest rendered by the now-retired
`SessionList`; the session rail superseded that surface. The landed `buildRailModel` derivation is the
canonical hierarchy composed once by `SessionsView` and passed into `SessionRail`. This module also
owns the fleet-attention rollup (R12), the projection joins for
gates (R13) / brief column (R8) / critical bus (F11), smart-default focus (R9), and question
triage (R16).

## Code Commentary

### Logic

L6 changes the command spine into a set of sprint-qualified command groups. `buildRailModel`
partitions bound architect/orchestrator/manager rows by repository+sprint provenance and associates
manager leaf clusters only with that matching group. Unbound command seats are retained in an
explicit legacy section for migration visibility; they do not merge with, own, or reroute a bound
sprint.

- **Role codes** (cit:([`roleCode`], dashboard/src/data/railModel.ts:30-34)): `roleCode` maps the six RULED codes ARC/ORC/MGR/WKR/REV/CUR; known
  extras keep the pattern (STR/DSG/SYS), unknown roles fall back to the first three letters
  uppercased; absent (or chat/terminal) ⇒ no chip (R6).
- **`buildRailModel(sessions, labels)`** (cit:([`buildRailModel`], dashboard/src/data/railModel.ts:212-256)): terminated tombstones never render; landed
  rows bucket into per-master `completed` (or `completedUnattached`); managers render flat inside
  their master section (a master-less manager still outranks the leaf level → spine); spine roles
  rank architect → orchestrator → strategist/designer → master-less managers (`SPINE_RANK`,
  matching the retired rail's roleRank); leaf agents cluster per `leafKey` under the master
  (`repo/master` from the leaf key). Master sections and clusters sort by key; `masterLabels`
  derives `repo/master → task-doc title` from the projection.
- **`compareClusterSeats`** (cit:([`compareClusterSeats`], dashboard/src/data/railModel.ts:62-68)): active-first (turnState working via `seatVisualState`),
  ties keep worker → reviewer → curator, final tiebreak id — PURE over turnState/role/id, so the
  order changes ONLY when a state changes (no jumpy reflows between identical polls).
- **`railCycleOrder`** (cit:([`railCycleOrder`], dashboard/src/data/railModel.ts:259-267)): the alt+↑/↓ cycle order — spine → managers → clusters →
  unattached, live rows only.
- **`buildSpawnTree`** (cit:([`buildSpawnTree`], dashboard/src/data/railModel.ts:257-279)): the palette/button-toggled spawn-edge PROVENANCE view (R5) —
  exactly the who-spawned-whom forest the ruled hierarchy replaced as the default.
- **Row anatomy invariants** (cit:([`ROW_SEGMENTS`], dashboard/src/data/railModel.ts:306-306)): `ROW_SEGMENTS = dot|role|title|status|end`,
  `ROW_ELIDABLE_SEGMENTS = [status]`; `railRowTooltip` carries the full untruncated truth (label ·
  role · state word · leaf · landed/retired reasons) the elided chip falls back to.
- **Fleet attention (R12)** (cit:([`attentionRollup`], dashboard/src/data/railModel.ts:334-349)): `attentionRollup` (needsInput/failed/unacked/criticalBus/
  working over LIVE rows; unacked + criticalBus are injected joins); `attentionZeroState` — the
  strip renders NOTHING when only `working` is non-empty (working alone is not attention);
  `jumpToAttentionTarget` — priority awaiting-input → failed → unacked → critical bus → OLDEST
  working, and within EVERY class the longest-waiting seat wins (`oldestFirst` over
  `turnStateChangedAt ?? createdAt`; review finding 4 fix); `masterAttentionBadge` — the group
  header's dominant-class badge (❗ input beats ✖ failed).
- **`smartDefaultFocus`** (cit:([`smartDefaultFocus`], dashboard/src/data/railModel.ts:408-424)): view-entry focus — oldest awaiting-input → oldest failed →
  most recently active running → null (the stage then renders the EXPLAINED launcher hint).
- **Projection joins** (cit:([`heldGatesByLeafKey`, `briefPendingSessionIds`, "function criticalBusSessionIds("], dashboard/src/data/railModel.ts:429-443; dashboard/src/data/railModel.ts:448-460; dashboard/src/data/railModel.ts:463-463)): `heldGatesByLeafKey` — leafKey → taskDoc → lifecycle → gate
  with `state === "open"` (the projection's undecided state; a distinct `decision-pending` word
  would extend HERE — reviewer note); `briefPendingSessionIds` — dispatch-brief pickups in
  `waiting-for-agent`/`check-chat`, joined `deliveredToSession` first then `lifecycleId`,
  deliberately TWO-state (consumed history is not projected; the tri-state is UA-3-gated and must
  never be faked); `criticalBusSessionIds` — pickups at ≥ 80% of ttl or escalated check-chat.
- **Question triage (R16)** (cit:([`interactionPromptPreview`, `waitingSeats`], dashboard/src/data/railModel.ts:481-491; dashboard/src/data/railModel.ts:494-503)): `interactionPromptPreview` — prompt/question/message/title
  keys, clamped, never fabricated; `waitingSeats` — ALL live seats with a pending interaction,
  newest first (the palette triage list). Per review N1, the filter derives from
  `sessions.ts`'s `sessionHasPendingInteraction` — the singular parent slot OR a non-empty
  multiplexed sub-agent list — so a seat blocked SOLELY on a sub-agent approval is listed instead
  of going dark.

### Invariants And Boundaries

- PURE module: no React, no store reads — everything arrives as arguments; `SessionsView` derives
  the model ONCE per render and shares it between the rail and the palette commands.
- The default hierarchy is ROLE-driven; `spawnedBySession` may only influence the toggled
  provenance tree, never the default order.
- No render-order comparator may contain per-tick values (timestamps) — determinism is
  test-pinned (identical states ⇒ identical order).
- Never-drop: managers with no resolvable master render on the spine (unchanged from the retired rail).

## Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Role codes, rail model, comparators, spawn tree, anatomy invariants, attention, joins, triage. | `roleCode`, `buildRailModel`, `compareClusterSeats`, `railCycleOrder`, `buildSpawnTree`, `ROW_SEGMENTS`, `attentionRollup`, `smartDefaultFocus`, `heldGatesByLeafKey`, `briefPendingSessionIds`, "function criticalBusSessionIds(", `interactionPromptPreview`, `waitingSeats` | dashboard/src/data/railModel.ts:34-40; dashboard/src/data/railModel.ts:67-73; dashboard/src/data/railModel.ts:212-256; dashboard/src/data/railModel.ts:259-267; dashboard/src/data/railModel.ts:278-300; dashboard/src/data/railModel.ts:306-306; dashboard/src/data/railModel.ts:334-349; dashboard/src/data/railModel.ts:408-424; dashboard/src/data/railModel.ts:429-443; dashboard/src/data/railModel.ts:448-460; dashboard/src/data/railModel.ts:463-463; dashboard/src/data/railModel.ts:481-491; dashboard/src/data/railModel.ts:494-503 |
| The one grammar the active-first sort + rollup classify through. | `seatVisualState` | dashboard/src/data/stateGrammar.ts:101-125 |
| The renderer consuming the model/rollup as props. | `SessionRail` | dashboard/src/panels/session-cockpit/SessionRail.tsx:155-235 |
| The view deriving model + rollup once and wiring palette commands over them. | "buildRailModel," | dashboard/src/panels/session-cockpit/sessions-view/sessionsViewController.ts:24-24 |
| The projection types joined (TaskDocNode, GateNode, AgentPickupNode, LifecycleProjection). | `TaskDocNode`, `GateNode`, `AgentPickupNode`, `LifecycleProjection` | dashboard/src/types/projection.ts:54-77; dashboard/src/types/projection.ts:217-227; dashboard/src/types/projection.ts:258-276; dashboard/src/types/projection.ts:437-463 |
| The seat-role resolution (`sessionSeatRole`: binding first, provenance fallback) and the ANY-pending derivation (`sessionHasPendingInteraction`, N1) the triage filter uses. | `sessionSeatRole`, `sessionHasPendingInteraction` | dashboard/src/data/sessions.ts:183-187; dashboard/src/data/sessions.ts:525-532 |
| The unit suite: sprint-local grouping/ordering, determinism, anatomy, attention priority + tiebreaks, joins, and triage (including the N1 agent-only-blocked listing pin). | "buildRailModel (sprint-local command groups and leaf-subordinate clusters)"; "row anatomy invariants (R6)"; "fleet attention (R12)"; "projection joins"; "question triage (R16)" | dashboard/src/data/railModel.test.ts:47-166; dashboard/src/data/railModel.test.ts:197-212; dashboard/src/data/railModel.test.ts:214-297; dashboard/src/data/railModel.test.ts:314-388; dashboard/src/data/railModel.test.ts:390-432 |
| The duty-transfer and deletion map records the retired grouping model and this module's replacement ownership. | `# dashboard/src/panels/session-cockpit/ — Canonical Chats Cockpit Overview` | onboarding/dashboard/src/panels/session-cockpit/overview.md:1-506 |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-10T04:39+02:00 — 260713-TES-L6: documented sprint-qualified command groups and the
  migration-only legacy command-seat bucket. Verification metadata remains pinned until closeout
  stamps the code commit.
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: reviewed this sidecar against the frontend-rail change set (strict-target lint remediation: complexity, max-lines-per-function, react-hooks, jsx-a11y, and import-cycle fixes). No content impact: behavior-preserving refactor; the file's responsibilities and the claims in this card remain current. Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-03T02:35:41+02:00 — W3-B04 curator: curated 8 table citations and 10 prose citations (18 total), supplying exact anchors and paths; the scoped fixer generated all final extents.

- 2026-07-26T15:40+0200 — 260718-CHATS-L7 curator: recorded the fix-round review-N1 triage change.
  `waitingSeats` (the palette's question-triage list) now filters with
  `sessions.ts`'s `sessionHasPendingInteraction` — the singular parent slot OR a non-empty
  multiplexed sub-agent list — so a seat blocked SOLELY on a sub-agent approval is listed instead of
  going dark; newest-first ordering is unchanged. Source is uncommitted; closeout re-stamps
  verification.

- 2026-07-18T16:02+02:00 — FEUI MX-FIX-3: moved the `SessionList` comparison into explicit
  historical provenance and recorded the landed `buildRailModel` → `SessionsView` → `SessionRail`
  ownership chain. Verified against code commit `31f58834f86c0d98e26b0896e099a2403a8729ee`.

- 2026-07-18T07:22+02:00 — FEUI-L8 manual route refactor: retargeted this direct data file card
  from the packed dashboard/src parent to the new nearest data authority overview. Source behavior
  is unchanged by this memory-only governance move; verification hash/date remain pinned.

- 2026-07-17T02:30+02:00 — Created for 260715-FEUI-L2 S4 (R5/R6/R8/R9/R12/R13/R16/R17, incl. the
  review finding-4 fix making the longest-waiting tiebreak hold in every attention class): the
  pure ruled-hierarchy rail model — flat command spine, per-leaf clusters with deterministic
  active-first sort, completed folders, spawn-edge provenance tree, row-anatomy invariants +
  tooltip truth, fleet-attention rollup with zero-state suppression and jump priority, held-gate /
  two-state-brief / critical-bus projection joins, smart-default focus, and question triage.
  Verification metadata pinned to the leaf base until closeout stamps the L2 code commit.
