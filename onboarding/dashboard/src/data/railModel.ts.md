# dashboard/src/data/railModel.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/railModel.ts`                |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-07-18T07:22+02:00 |
| lastVerifiedCommitHash | `e2b99dcd71fb6ca31f642dd61c3c16f3d3d05bf5`       |
| lastVerifiedCommitDate | 2026-07-17T02:52:07+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[data overview](overview.md)

## Purpose

The **session-rail model** (260715-FEUI-L2 S4) — pure, React-free derivations for the RULED
role-driven hierarchy (spec §1.6b, ruled 2026-07-16): architect / orchestrator / manager render as
a FLAT command spine (never spawn-edge nesting); only leaf agents indent, clustered per leaf under
their manager, base order worker → reviewer → curator with the ACTIVE seat sorted to the top;
completed seats fold into a per-master collapsed folder (R17). It consumes the
260713_chat-rail-role-hierarchy analysis (the landed spawn-edge forest in
`SessionList.orderedVisibleMembers` is the diagnosed defect) — that master's formal roll-in stays
pending the developer's call. Also owns the fleet-attention rollup (R12), the projection joins for
gates (R13) / brief column (R8) / critical bus (F11), smart-default focus (R9), and question
triage (R16).

## Code Commentary

### Logic

- **Role codes** (L17-L34): `roleCode` maps the six RULED codes ARC/ORC/MGR/WKR/REV/CUR; known
  extras keep the pattern (STR/DSG/SYS), unknown roles fall back to the first three letters
  uppercased; absent (or chat/terminal) ⇒ no chip (R6).
- **`buildRailModel(sessions, labels)`** (L131-L205): terminated tombstones never render; landed
  rows bucket into per-master `completed` (or `completedUnattached`); managers render flat inside
  their master section (a master-less manager still outranks the leaf level → spine); spine roles
  rank architect → orchestrator → strategist/designer → master-less managers (`SPINE_RANK`,
  matching the 260713 roleRank); leaf agents cluster per `leafKey` under the master
  (`repo/master` from the leaf key). Master sections and clusters sort by key; `masterLabels`
  derives `repo/master → task-doc title` from the projection.
- **`compareClusterSeats`** (L62-L68): active-first (turnState working via `seatVisualState`),
  ties keep worker → reviewer → curator, final tiebreak id — PURE over turnState/role/id, so the
  order changes ONLY when a state changes (no jumpy reflows between identical polls).
- **`railCycleOrder`** (L208-L216): the alt+↑/↓ cycle order — spine → managers → clusters →
  unattached, live rows only.
- **`buildSpawnTree`** (L227-L249): the palette/button-toggled spawn-edge PROVENANCE view (R5) —
  exactly the who-spawned-whom forest the ruled hierarchy replaced as the default.
- **Row anatomy invariants** (L255-L269): `ROW_SEGMENTS = dot|role|title|status|end`,
  `ROW_ELIDABLE_SEGMENTS = [status]`; `railRowTooltip` carries the full untruncated truth (label ·
  role · state word · leaf · landed/retired reasons) the elided chip falls back to.
- **Fleet attention (R12)** (L273-L349): `attentionRollup` (needsInput/failed/unacked/criticalBus/
  working over LIVE rows; unacked + criticalBus are injected joins); `attentionZeroState` — the
  strip renders NOTHING when only `working` is non-empty (working alone is not attention);
  `jumpToAttentionTarget` — priority awaiting-input → failed → unacked → critical bus → OLDEST
  working, and within EVERY class the longest-waiting seat wins (`oldestFirst` over
  `turnStateChangedAt ?? createdAt`; review finding 4 fix); `masterAttentionBadge` — the group
  header's dominant-class badge (❗ input beats ✖ failed).
- **`smartDefaultFocus`** (L357-L373): view-entry focus — oldest awaiting-input → oldest failed →
  most recently active running → null (the stage then renders the EXPLAINED launcher hint).
- **Projection joins** (L378-L438): `heldGatesByLeafKey` — leafKey → taskDoc → lifecycle → gate
  with `state === "open"` (the projection's undecided state; a distinct `decision-pending` word
  would extend HERE — reviewer note); `briefPendingSessionIds` — dispatch-brief pickups in
  `waiting-for-agent`/`check-chat`, joined `deliveredToSession` first then `lifecycleId`,
  deliberately TWO-state (consumed history is not projected; the tri-state is UA-3-gated and must
  never be faked); `criticalBusSessionIds` — pickups at ≥ 80% of ttl or escalated check-chat.
- **Question triage (R16)** (L443-L464): `interactionPromptPreview` — prompt/question/message/title
  keys, clamped, never fabricated; `waitingSeats` — ALL live seats with a pending interaction,
  newest first (the palette triage list).

### Invariants And Boundaries

- PURE module: no React, no store reads — everything arrives as arguments; `SessionsView` derives
  the model ONCE per render and shares it between the rail and the palette commands.
- The default hierarchy is ROLE-driven; `spawnedBySession` may only influence the toggled
  provenance tree, never the default order.
- No render-order comparator may contain per-tick values (timestamps) — determinism is
  test-pinned (identical states ⇒ identical order).
- Never-drop: managers with no resolvable master render on the spine (mirrors 260713 R3).

## Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | `system/sources.md` checked | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Role codes, rail model, comparators, spawn tree, anatomy invariants, attention, joins, triage. | L17-L464 | [railModel.ts](railModel.ts) |
| The one grammar the active-first sort + rollup classify through. | L88-L106 | [stateGrammar.ts](stateGrammar.ts) |
| The renderer consuming the model/rollup as props. | L364-L744 | [../panels/session-cockpit/SessionRail.tsx](../panels/session-cockpit/SessionRail.tsx) |
| The view deriving model + rollup once and wiring palette commands over them. | L206-L344 | [../panels/session-cockpit/SessionsView.tsx](../panels/session-cockpit/SessionsView.tsx) |
| The projection types joined (TaskDocNode, GateNode, AgentPickupNode, LifecycleProjection). | — | [../types/projection.ts](../types/projection.ts) |
| The seat-role resolution (`sessionSeatRole`: binding first, provenance fallback). | — | [sessions.ts](sessions.ts) |
| The unit suite: grouping/ordering, determinism, anatomy, attention priority + tiebreaks, joins, triage. | L34-L344 | [railModel.test.ts](railModel.test.ts) |
| FEUI-L8 duty-transfer and deletion map records the retired grouping model and this module's replacement ownership. | — | [session-cockpit overview](../panels/session-cockpit/overview.md) |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Update History

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
