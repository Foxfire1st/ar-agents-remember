# dashboard/src/types/projection.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/types/projection.ts`              |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-01T10:45+02:00                           |
| lastVerifiedCommitHash | `e52edaf5b655f495580efd93306afdf922b19b51`       |
| lastVerifiedCommitDate | 2026-08-01T11:01:51+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src/ overview](../overview.md)

## Purpose

Hand-maintained TypeScript mirror of the served projection contract (`mcp/.../observer/projection.py`, the source of truth — D7: pydantic codegen deferred). camelCase matches the wire form, and because the server dumps with `exclude_none=True`, every `T | None` server field is modelled as optional (`?:`). Slice 5e extends the contract with the enclosure-centered Engine Room process map: `CommitRefNode` / `ProviderBootNode` / `EngineProcessEdge` / `EngineProcessNode`, the `ProcessFactState` / `ProcessHealth` honesty enums, and the `Analytics.engineProcesses` derived surface. Slice 6g mirrors the master-navigation additions: `TaskSubTaskRefNode` (with `linkedLifecycleId`), `TaskSectionNode`, and `subTasks` / `sections` / `masterLifecycleId` on `TaskDocNode`. (6g originally gave `TaskSubTaskRefNode` an optional `createdAt` as well; 260731-EFA-L4 removed it and split the interface — see the L4 subsection below.) Task 17 makes `TaskDocNode.lifecycleId?` optional because runtime lifecycle state is attachment, not the condition for projecting a JSON-primary task document; planning-only leaves and masters can be listed/read before a worktree exists. Task 17 also mirrors `TaskDocNode.id`, the JSON-primary task id used as the authored leaf display number when parent sub-task refs are only fallback rows. The masters surface is still also exposed as `Analytics.series: SeriesNode[]`, carrying folder-keyed master content with `createdAt`, `objective`, sections, decisions, sub-task creation metadata for default oldest-first ordering, and `seriesTokenTotal` for the server-composed leaf-lifecycle token aggregate.

**260731-EFA-L4 changes what kind of file this is.** It is still hand-kept against `projection.py`, but the parts most often hand-copied are now *derived*: the state vocabulary is COMPOSED from its two halves (`LIVE_STATES` L42, `TERMINAL_STATES` L48, spread into `LIFECYCLE_STATES` L59), `State` and `Phase` are types read off exported runtime tuples (`State` L61, `PHASES` L96-L103), the `Metrics` bucket field NAMES are computed from the live half (`StateCountField` L206, `LifecycleStateCounts` L214), and this module now emits **eleven** runtime values a test can enumerate — nine vocabulary lists plus the functions `stateCountField` (L220-L224) and `metricsFor` (L250-L257) — so no consumer has to keep a private list. That change is the fix for this leaf's defect: `State` had stayed five members long while `observer/lifecycle_state.py` declared six, so an `awaiting-developer` lifecycle rendered as healthy and was counted in no `Metrics` bucket at all.

## Code Commentary

### FEUI-L9R Reviewed Candidate Delta

`ServingBuild` now optionally mirrors `dashboardBuild`, the fingerprint of the shipped dashboard
inputs. Like the containing `servingBuild` block, it is app-injected wire truth rather than persisted
`projection.py` reducer state. Absence means a legacy or otherwise non-comparable server and must
remain unknown; it is not evidence of mismatch.

### 260707-HFX2-L13 Task-Body Revision

`TaskDocNode.bodyRevision?` mirrors the server-generated digest of reader-body fields omitted from
the always-on summary. It is optional for compatibility with persisted/older projections. The detail
reader combines it with `docPath` as the on-demand body cache key; summary fields such as identity,
status, progress, steps, sub-task links, and routing metadata remain in the broadcast contract.

### Logic

**No longer a pure type module.** Since 260731-EFA-L4 it emits **eleven** runtime values: eight `as const` vocabulary tuples — `LIVE_STATES`, `TERMINAL_STATES`, `LIFECYCLE_STATES`, `PHASES`, `ATTENTION_SEVERITIES`, `ATTENTION_LANES`, `PROCESS_FACT_STATES`, `PROCESS_HEALTHS` — plus `ACTIVE_STATES` (a `readonly ActiveState[]` bound directly to `LIVE_STATES`, not a tuple of its own) and the functions `stateCountField` and `metricsFor`. Everything else is still type-only. The top-level shape is `WorkspaceProjection`: `version`, `generatedAt`, `lifecycles: LifecycleProjection[]`, `enclosures: EnclosureNode[]`, `providers: ProviderNode[]`, `activeWorktreeGroups: string[]` (required — the worktree-group basenames with a live enclosure lifecycle; the bounded set the Topology filters on, join key = worktree `ProviderNode.worktreeGroup` / basename of `EnclosureNode.worktreeGroup`; always present because the server default is a list, never `exclude_none`-dropped), `metrics: Metrics`, and `analytics: Analytics`. Core nodes — `LifecycleProjection` (state/phase/tokens + `stateEnteredAt`, `tokenSeries`, `actions`), `EnclosureNode`, `ProviderNode` (with `scope` workspace|worktree, `role` code|memory, optional `repoId`, and optional `worktreeGroup`), `Metrics`, plus the analytics children (`DriftSnapshotNode`, `SidecarStaleNode`, `SetupSummaryNode`, `SetupProgressNode`, `RouteCoverageNode`, `ToolReportNode`, `LedgerNode`, the `TaskDocNode` tree, and the reducer-derived `AttentionItem`). Slice 6c adds `GateNode` and the optional `LifecycleProjection.gate` — the durable gate the cockpit reviews (`decisions` = the verbs an open gate can POST). `State` (L61) and `Phase` (L105) are no longer hand-written unions: each is `(typeof <TUPLE>)[number]` over an exported `as const` tuple, so a consumer that needs to *enumerate* the vocabulary reads the one list instead of copying a second.

Slice 5e adds the engine-room process map. `ProcessFactState` (`observed` | `derived` | `planned` | `missing` | `not-applicable`) is the honesty axis and `ProcessHealth` (`nominal` | `running` | `blocked` | `failed` | `stale` | `skipped` | `unknown` | `complete`) the rollup. `CommitRefNode` describes one checkout (branch/commit/path, `exists`, `dirty`, `behindSource`, `factState`); `ProviderBootNode` describes a per-process provider boot (id/role/`runtimeState`/`factState`) and includes `runtimeState="missing"` for expected provider slots whose runtime facts were not observed; `EngineProcessEdge` is a setup-step edge (`fromNode`/`toNode`/`kind`/`state`/`label`). `EngineProcessNode` is the enclosure pod keyed by the contract path (`id` == `EnclosureNode.enclosure`): code/memory source-vs-worktree `CommitRefNode`s, `memoryMode`, ledger + review/closeout/integration/cleanup status, setup phase fields, its `providers`/`edges`/`actions`, `missingFacts` / `sourceFiles`, and the two series-contract identities (`taskName` for the parent series task, `leafId` for the concrete leaf worktree/enclosure). `Analytics.engineProcesses: EngineProcessNode[]` carries the whole derived surface. Slice 5h adds the successful-landing arc mirror: `LandingRefNode` (`kind`/`label`/`state` + the `ProcessFactState` honesty axis + optional `detail`) and two additive `EngineProcessNode` fields — `landing?: LandingRefNode[]` (optional — a pre-5h/persisted projection omits it; a list is never dropped by `exclude_none`, so this `?:` encodes schema evolution, not the omission rule) and optional `integrationStrategy` — kept in lockstep with the `projection.py` source of truth. The 5h coupler popover then mirrors `LedgerRefNode` (`codeCommit`/`memoryCommit`), `LedgerNode.rows` (the official coupler's served window; `closeoutCount` stays the full total), and `EngineProcessNode.ledgerRows`/`ledgerRowCount` (the worktree coupler's window). **5h Tier 2** adds four optional fields to `LedgerRefNode` — `codeSubject?`/`codeDate?`/`memorySubject?`/`memoryDate?` (the per-side commit message + committer ISO date for the popover's 6 columns) — modelled `?:` to mirror the source model's `exclude_none` omission. **Slice 05o added, and 260731-EFA-L4 REMOVED, the refused-conduit signal on `EngineProcessEdge`.** 05o listed a `refused` value in the `state` comment enumeration and declared an optional `refusedPolarity?: "amber" | "red"` field. Neither existed server-side: no Python model declares `refusedPolarity` (and the engine-process models are `extra="forbid"`), and the reducer never emits a `refused` edge state. The field was an invention of the mirror, and its renderer branch shipped permanently dead. Both are gone (`EngineProcessEdge` L574-L585, whose comment now reads `nominal | running | blocked | failed | stale | skipped | complete | planned | unknown` and states that flash polarity is DERIVED in the renderer — `failed` → red fault, `stale` → amber reroute — never carried). `contract.test.ts` pins the removal with an inverted `@ts-expect-error` assertion, which fails `tsc -b` the moment the field comes back, because an unused `@ts-expect-error` is itself a compile error.

Slice 6g extends `TaskDocNode` for navigation/content: `subTasks: TaskSubTaskRefNode[]` — a master's series-index row (`number`/`name`/`file`/`status`/`scope` + optional `linkedLifecycleId`, set when `file` points at another master, the cross-series "→" jump target; **no `createdAt`** — see the L4 subsection) — and `sections: TaskSectionNode[]` — ordered task-document sections (`kind`/`heading`/`body`). `TaskDocNode.id` mirrors the JSON-primary document `id` and is the clean task-specific display number for authored leaf rows; `subTasks[].number` remains a parent-row fallback for unauthored rows. `TaskDocNode.createdAt?` exposes the JSON-primary task document creation time so leaf lists can default to creation order without parsing file names. Task 17 makes `TaskDocNode.lifecycleId?` optional; a missing lifecycle id means "planning/unbound task document", not "not readable." `subTasks` are master-only, while `sections` may also carry authored freeform sections on light/subTask docs; plus `masterLifecycleId?`, the parent master's lifecycle (the "↑ parent" link). 260703-L14 adds `TaskDocNode.orchestrates?: string[]` — the orchestration-command relation (non-empty only on a master doc that IS an orchestration task; the master task names it commands, from which the dashboard derives the orchestration > master > leaf hierarchy). It mirrors a list-default server field (always dumped as `[]`), but is modelled `?:` deliberately so projections **persisted before L14** still parse — the same forward-compat exception as `landing?`, so consumers must guard (`doc.orchestrates ?? []`). `SeriesNode` mirrors folder-keyed masters in `Analytics.series`: it includes master `createdAt`, `objective`, subTasks, done/total counts, `seriesTokenTotal`, sections, decisions, `docPath`, and optional age. Task 23/24/L3 mirrors `AttentionItem.gateId?` for deletion actions and `AgentPickupNode` / `Analytics.agentPickups?` for task-row waiting-for-agent/check-chat feedback, now including sender/recipient role metadata, message kind, artifact path, and hosted-delivery state. FEUI-L7 adds optional owner identity (`ownerRole`/`ownerAgentId`/`ownerLifecycleId`) and redelivery/escalation facts (`attemptCount`/`lastAttemptAt`/`nextAttemptAt`/`escalatedAt`) to that mirror. They stay optional so persisted pre-L7 projections remain readable and their absence stays absent in the Bus pane. Task 28 mirrors `AttentionItem.signalTs?`, the server-computed current-occurrence acknowledgement anchor for lifecycle-scoped dismissals. Task 29 adds `DriftSnapshotNode.checkedAt?`, `sourceRoot?`, `memoryRoot?`, and `reportPath?` so actionable-drift attention rows can identify the affected repo/memory/report and use `checkedAt` as a dismissible occurrence anchor. Optional fields mirror `exclude_none`.

### 260731-EFA-L4 Vocabulary Derivation, Model Split, And LATE MIRROR

**The vocabularies became tuples.** Eight closed vocabularies are now declared as `as const` tuples
with the type derived from them: `LIVE_STATES` (L42), `TERMINAL_STATES` (L48), `LIFECYCLE_STATES`
(L59), `PHASES` (L96-L103), `ATTENTION_SEVERITIES` (L473) / `ATTENTION_LANES` (L477),
`PROCESS_FACT_STATES` (L534-L541) / `PROCESS_HEALTHS` (L545-L554). The reason is
stated in the source and is worth keeping: `projection.py` types every one of these fields as a bare
`str`, so the mirror's closed union is NARROWER than the server by construction, and nothing
type-level can notice — a JSON module import widens the payload's literals to `string`, so a served
`severity: "critical"` assigns to `"alarm" | "warn" | "info"` in silence. Only a runtime membership
check bites, and a runtime check needs a runtime list. `contract.test.ts::VOCABULARIES` (L269-L284)
is the consumer.

**The state vocabulary is now a COMPOSED partition, matching the server.** The halves are written out
first — `LIVE_STATES` (L36-L42) and `TERMINAL_STATES` (L44-L48) — and the whole is assembled from
them: `LIFECYCLE_STATES = [...LIVE_STATES, ...TERMINAL_STATES]` (L59). `State` (L61) derives from that
tuple, `TerminalState` (L63) from the terminal half, `ActiveState` (L70) from the live half, and
`ACTIVE_STATES` (L72) is bound to `LIVE_STATES` **directly**, not by subtraction — mirroring
`projection.py::ACTIVE_STATES = LIVE_STATES` (L227) and for the reason that file gives: a set
difference re-derives the answer from a second list that could itself be wrong.

This replaced the previous shape, which is worth naming because the card used to describe it: one
list of six (`LIFECYCLE_STATES`) plus a SECOND, independent list of two (`TERMINAL_STATES`), with
`ActiveState = Exclude<State, TerminalState>`. Two lists naming one vocabulary can disagree and
nothing noticed — `Exclude` over a member the whole never contained removes nothing, silently, so the
terminal half could have named a state that did not exist and every gate stayed green. Composed from
the halves there is no second list left to disagree: filing a state on a half is what puts it in the
vocabulary at all. Both halves stay exported for the reason the source gives (L28-L34): server-side
the same pair is public, and publishing one half is what invites the next consumer to hand-roll the
missing half beside it — the move that produced the bucket list this change replaced.

**The partition check is real, and it is a compile-time one.** `type FiledOnce<S extends never> = S;`
(L88) with `export type StatesAreFiledOnce = FiledOnce<ActiveState & TerminalState>;` (L90). Disjoint
string-literal unions intersect to `never`, so the constraint holds exactly while the halves are
disjoint. Verified non-vacuous by mutation on a copy of this file, not taken on trust: double-filing
`"completed"` onto `LIVE_STATES` and running the repository's own `tsc` (5.9.3) under the
`tsconfig.app.json` flags fails with
`error TS2344: Type '"completed"' does not satisfy the constraint 'never'.` at L90; the unmodified
file compiles clean. `StatesAreFiledOnce` is exported because it has to be — `noUnusedLocals` rejects
a type alias nothing reads, and an assertion is precisely a declaration nothing reads.

Two of `check_state_partition`'s three server-side refusals are *unrepresentable* here rather than
checked, and asserting them would be a check that cannot fail: a state cannot be on `State` and filed
on neither half (there is nothing else for it to be on), and it cannot be filed yet absent from
`State` (filing is what puts it there).

**What `tsc` still cannot catch, precisely.** A duplicate WITHIN one half. `Literal["a", "a"]`
collapses to one member in Python; a TypeScript tuple keeps both, so
`LIVE_STATES = ["running", "running", …]` compiles clean — confirmed by the same mutation run (exit
0, no diagnostics). It is caught at RUNTIME by `contract.test.ts`, which fails **three** tests on
that mutation: "gives each live state a bucket of its own" (`new Set(buckets).size` vs
`buckets.length`), "counts a lifecycle in each live state into its own bucket" (the duplicated state
counts 2 where 1 is asserted), and "exercises every member of every vocabulary, so the check does not
depend on luck". Weaker than the Python side — import-time refusal there, one test file here — but
not absent. `projection.py` L224-L226 states the same asymmetry from the other side.

**`Metrics` buckets are derived, not listed.** `Camel<S>` (L202-L204) + `StateCountField<S>` (L206)
compute the field name from the state name; `LifecycleStateCounts` (L214) is a mapped type over
`ActiveState`, so `Metrics extends LifecycleStateCounts` (L240-L244) gains a REQUIRED field the day a
live state is filed on `LIVE_STATES` and every object claiming to be a `Metrics` stops compiling until
it counts it. Filing one on `TERMINAL_STATES` adds no field — the filing doing its job, not an
omission. `stateCountField` (L220-L224) is the runtime twin and `metricsFor` (L250-L257) the
client-side mirror of `reducer.py::_metrics`, so a fixture states its lifecycles and gets the metrics
the server would have sent instead of re-listing buckets beside them.

The camel rule has two copies and they were reconciled in this leaf: each segment after the first has
its FIRST character upper-cased and **the tail left alone**. Python used `str.capitalize()`, which
lower-cases the tail, so `awaiting-DEVELOPER` bucketed to `awaitingDeveloperCount` server-side and
`awaitingDEVELOPERCount` here — one rule with two answers. Settled in favour of this spelling
(`projection.py::state_count_field` now does `word[:1].upper() + word[1:]`) because `Capitalize<>`
cannot lower-case a tail at the type level and because lower-casing merges two states differing only
in tail case.

**Two model pairs were un-collapsed.** `TaskSubTaskRefNode` (L368-L375) and `SeriesSubTaskNode`
(L380-L387) are two distinct `extra="forbid"` server models that this mirror had collapsed into one
interface. The collapse invented a `createdAt` on the master row that the server never sends and lent
`linkedLifecycleId` to series rows that never carry it. They share five fields and differ in exactly
one each. `SubTaskRow = TaskSubTaskRefNode | SeriesSubTaskNode` (L391) is the union the sub-task index
renders. `SeriesNode.subTasks` (L449-L464) is now `SeriesSubTaskNode[]`.

`SeriesSectionNode` (L412-L416) is the same situation one model over — a separate `extra="forbid"`
Python model from `TaskSectionNode` (L393-L397) — and the source is explicit about how much less this
one buys: the two declare the same three fields, so TypeScript's structural typing keeps them
interchangeable (`DetailPanel.tsx::seriesAsMasterDoc` assigns one array to the other), no assertion
over any payload can separate them, and `contract.test.ts`'s structural walk never will. It is a NAME
and a SLOT for the day the server adds a field to one of them — not a check. Only per-model codegen
makes it load-bearing.

**`LATE MIRROR` is a new, narrower meaning for `?:`.** Normally `?:` here means "the server omits this
when null" (`exclude_none=True`). Three fields marked `LATE MIRROR` are *always* on the wire — a
non-None default server-side — and are still declared optional as a CLIENT-SIDE TOLERANCE, because
making them required would force every hand-written literal across the test suite to be edited in the
same change: `GateNode.evidenceRefs?` (L125-L126), `LifecycleProjection.stateEnteredAt?` (L143-L147),
`Analytics.expectationRows?` (L671-L672). The header (L7-L12) says so and names codegen as what
removes the distinction. Do not read a `LATE MIRROR` optional as evidence the server may omit the
field.

**Additive fields.** `LandingRefNode.at?` (L597) — the ref's own merge/push timestamp, distinct from
the probe's `observedAt`; `EngineProcessNode.carryoverDoneAt?` (L629) — when memory carryover landed,
absent until it has; `ExpectationRowNode` (L650-L661) — one outstanding supervisor expectation
(`dueAt`/`overdue`), reached from `Analytics.expectationRows?`.

### Invariants And Boundaries

- `projection.py` is the source of truth — change it first, then mirror here in lockstep. This module
  is no longer type-only: it emits eleven runtime values — the eight `as const` vocabulary tuples,
  `ACTIVE_STATES`, and the functions `stateCountField` and `metricsFor`.
- Optional (`?:`) fields encode the server's `exclude_none=True` omission; never assume a `?:` field is present. Two documented exceptions: `landing?` (forward-compat, below) and the three `LATE MIRROR` fields, which the server ALWAYS sends and which are optional here only as client-side tolerance.
- A closed string union in this file is a claim NARROWER than the server, which types the same field as a bare `str`. Adding a member is a mirror-side widening that needs no server change; removing one silently rejects a value the server may still send. The tuples exist so `contract.test.ts` can check the claim at runtime — do not replace one with a hand-written union.
- **Adding a state means filing it on exactly one half — `LIVE_STATES` or `TERMINAL_STATES` — and nothing else.** `LIFECYCLE_STATES` is assembled from them, so filing is what puts a state in the vocabulary; there is no second list to keep in step. Never re-introduce a hand-written `LIFECYCLE_STATES`, and never re-derive `ACTIVE_STATES` as `Exclude<State, TerminalState>`: both moves restore a list that can disagree with the halves, which is the defect this shape removed.
- **Double-filing is refused at compile time; a duplicate within one half is not.** `StatesAreFiledOnce = FiledOnce<ActiveState & TerminalState>` fails `tsc -b` with `TS2344` naming the offending state (verified by mutation, not assumed). But a TypeScript tuple keeps repeated members where Python's `Literal` collapses them, so `["running", "running", …]` compiles clean and is caught only by `contract.test.ts` at runtime (three failing tests, including "gives each live state a bucket of its own"). Do not delete those runtime bucket assertions on the grounds that the type check covers the partition — it covers a different half of it.
- One interface per Python model. `TaskSubTaskRefNode` / `SeriesSubTaskNode` and `TaskSectionNode` / `SeriesSectionNode` are separate because their server models are separate `extra="forbid"` models — not because TypeScript can tell them apart. Structural typing means the second pair is interchangeable and no test can pin it; that is a known limit, not an oversight.
- `stateCountField` is NOT injective (`a-b` and `aB` both bucket into `aBCount`), and a collision does not announce itself — `Metrics` is keyed by field, so the later count silently overwrites the earlier and the rollup under-reports with no field looking wrong. The server refuses the collision where it builds the map (`projection.py::state_count_fields`); this side cannot refuse at runtime (the vocabulary is frozen at build time), so `contract.test.ts` asserts bucket uniqueness instead.
- `EngineProcessEdge` carries no `refusedPolarity` and the reducer emits no `refused` state. Flash polarity is derived in the renderer from `state`. Reintroducing either invents a field the server cannot send.
- `TaskDocNode.id` is required and comes from the JSON-primary task document id. Dashboard consumers use
  it for authored leaf display labels instead of parsing or trusting parent label strings.
- `TaskDocNode.lifecycleId?` is optional runtime binding. Consumers must not hide a task document merely
  because it has not been bound to a lifecycle/enclosure yet.
- `TaskDocNode.sections` means sections from the JSON task-document schema. It is not a projection path
  for `series-contract.md` content.
- `createdAt` is a structured ordering field supplied by the server. Consumers may sort by it when
  present, but must not derive creation order by parsing `number` or filename prefixes.
- `SeriesNode.seriesTokenTotal` is server-derived. Dashboard consumers display it; they do not recompute
  it from lifecycle gauges or task-doc rows.
- `landing?` is the exception (a list, never `exclude_none`-dropped): it is `?:` for **forward-compat** — a projection produced before slice 5h omits the field, so consumers must guard (`node.landing?.…`).
- `engineProcesses` and `attentionQueue` are derived surfaces composed server-side; the client renders them verbatim and preserves server order (no re-sort, no re-derivation).
- `AttentionItem.signalTs?` and `LifecycleProjection.stateEnteredAt?` are server-computed lifecycle acknowledgement anchors. Clients forward ids/kinds only; they do not decide suppression freshness. `stateEnteredAt?` is `LATE MIRROR` — a `str` with a `""` default server-side, so it is always on the wire despite the `?`.
- `DriftSnapshotNode.checkedAt?` is the repo-level acknowledgement anchor for actionable drift; clients render/dismiss it but do not reclassify drift.
- `agentPickups` is also server-derived. Clients render the projected `waiting-for-agent` or `check-chat`
  state, role/message/delivery metadata, and do not run their own pickup TTL timers.
- FEUI-L7's optional pickup owner/redelivery fields are additive compatibility mirrors. Consumers
  display absence as absence; they do not synthesize owner identity, attempt counts, timestamps,
  or escalation state for older persisted rows.
- `EngineProcessNode.id` is the stable enclosure id and the join key to `EnclosureNode.enclosure`; `ProviderNode.worktreeGroup` is the join key to the owning enclosure and takes precedence over `ProviderNode.repoId` in topology parenting.
- Ages (`*Seconds`) and fact-state are server-computed (never `Date.now()`); `nextAction` is display/copy-only until slice 06. Since 260703-L15 the served age fields are also *volatile* to the change gate (excluded from server diff + client merge equality — `data/servedAges.ts`), and displays advance them locally from arrival anchors.
- `servingBuild?` (260703-L15) is the ONE field NOT mirrored from `projection.py`: it is injected app-side (`serving/build_info.py` via `serving/app.py`) onto `/api/state` and the SSE snapshot only, so it is optional here and absent from persisted `latest-state.json` (a pre-L15 server also sends none).
- `supervisorHeartbeat?` (260707-HFX2-L2 R5, expanded by HFX2-L8 R6) is a SECOND app-injected, non-`projection.py` field,
  same posture as `servingBuild?`: `serving/supervisor_heartbeat.py` via `serving/app.py` attaches it
  onto `/api/state` and the SSE snapshot at RESPONSE time, deliberately excluded from the ETag
  change-gate revision (it is a live tick age, not stable content) — so `ageSeconds` can be stale
  relative to the header's cached revision until a real reconnect or another content change forces
  a fresh response. `lastTickAt: null` means the supervisor has never ticked in this workspace
  (opt-in autostart) — that is NOT `stale: true`, and consumers must not treat the two as
  equivalent. The L8 fields (`pendingInboxCount`, `redeliverableInboxCount`,
  `lastSweepDurationSeconds`) are forward storm-pressure signals, not projection-stable content.

### 260712-TRH-L7 landing freshness wire contract

`ProcessFactState` admits `stale`, and `LandingRefNode` carries `observedAt`, `lastAttemptAt`, and `staleSeconds`. These fields are additive projection data consumed by the Engine Room to distinguish stale truth from a fresh observation.

### Conventions

Optional fields preserve compatibility with older persisted or serving payloads; app-injected fields
remain explicitly distinguished from projection-reducer output. Since 260731-EFA-L4 a third reason for
`?:` exists and is marked in-line: `LATE MIRROR` = always on the wire, optional only so existing
hand-written test literals keep compiling. A closed vocabulary is declared tuple-first (`as const`
runtime list, type derived from it) so consumers enumerate rather than copy.

### Todos

Recorded as open, not as done — the derivations above close specific holes and leave these.
(The partition item that stood here is **closed**: the halves-first composition and the compile-time
`StatesAreFiledOnce` check landed in this file, and `projection.py`'s "STATE OF THE MIRROR" comment
was rewritten to say so. What remains of it is the narrower within-half item below.)

- **A duplicate within one half is not a compile-time error.** Composition and `StatesAreFiledOnce`
  rule out an unfiled state and a double-filed one; a TypeScript tuple still admits
  `["running", "running", …]`, which Python's `Literal` would collapse. Only `contract.test.ts`
  catches it, at runtime. Codegen from the pydantic models is what closes the last of it.
- **`SeriesSectionNode` vs `TaskSectionNode` is a slot, not a check.** Same three fields, so
  structural typing keeps them interchangeable and no payload walk can separate them.
- **The mirror↔server link is held by no test.** `contract.test.ts` measures this file against
  `dashboard/src/fixtures/snapshot.json`, which is HAND-maintained — there is no generator. A field
  the server starts sending that neither the snapshot nor this file knows about is invisible to the
  whole chain. Codegen from the pydantic models is the fix and is deferred (header L4-L5;
  `contract.test.ts` "LEFT FOR CODEGEN (R3)").
- **Every closed union here is narrower than the server**, which types the same fields as bare `str`.
  Only the runtime vocabulary checks bite, and only for members the mirror already knows.

### 2026-07-24 Curator Delta

`ServingBuild` now exposes optional `dirty` wire evidence so the frontend can distinguish a base commit
hash from an uncommitted serving checkout. The rest of this round's changes remove task provenance from
comments without changing projection schema semantics.

## Docs References

No relevant documentation was found after checking the configured sources; the wire-shape claims
are proven by repository source and tests.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external or domain documentation was found for this repository-local type mirror. | Source discovery checked | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Header: `projection.py` is the source of truth, `?:` encodes `exclude_none=True`, codegen deferred — and the `LATE MIRROR` exception (always on the wire, optional as client tolerance only). | L1-L12 | [projection.ts](projection.ts) |
| The state vocabulary as a COMPOSED partition: the two halves written out (`LIVE_STATES`, `TERMINAL_STATES`), `LIFECYCLE_STATES` spread from them, and `State` derived from that tuple — with the comment recording that the previous shape was a whole plus a second, independent list. | L14-L61 | [projection.ts](projection.ts) |
| `TerminalState`, `ActiveState` derived from the live half, and `ACTIVE_STATES = LIVE_STATES` bound DIRECTLY rather than by subtraction. | L62-L72 | [projection.ts](projection.ts) |
| The compile-time partition check: `FiledOnce<S extends never>` and `StatesAreFiledOnce = FiledOnce<ActiveState & TerminalState>`, with the comment naming the exact `TS2344` diagnostic and why the two other refusals are unrepresentable rather than checked. | L74-L90 | [projection.ts](projection.ts) |
| `PHASES` / `Phase`, tuple-first for the stated reason that the contract test used to hold its OWN copy of the six phase names. | L91-L105 | [projection.ts](projection.ts) |
| The served docstring: persisted/served contract, camelCase wire convention, `extra="forbid"` keeps it honest. | L1-L9 | [projection.py](../../../mcp/src/agents_remember/observer/projection.py) |
| The partition helper this file's compile-time check mirrors: `check_state_partition` and the `LifecycleVocabularyError` it raises. | `LifecycleVocabularyError` L30-L38; `check_state_partition` L73-L98 | [lifecycle_state.py](../../../mcp/src/agents_remember/observer/lifecycle_state.py) |
| The server-side vocabulary: `LiveState` / `TerminalState` written out as halves, `State = Literal[LiveState, TerminalState]` composed FROM them, `Phase`, and `STATES` / `LIVE_STATES` / `TERMINAL_STATES` built through the partition check. | L101-L146 | [lifecycle_state.py](../../../mcp/src/agents_remember/observer/lifecycle_state.py) |
| The "STATE OF THE MIRROR" comment, rewritten to record that the mirror now holds the same partition in the same shape, that this file refuses double-filing at import while the mirror refuses it at compile time, and that a duplicate WITHIN one half is the one thing the mirror cannot follow (`Literal["a","a"]` collapses; a TS tuple does not) — caught by the dashboard contract test at runtime instead. | comment L194-L226 (the mirror paragraph L208-L226); `ACTIVE_STATES` L227 | [projection.py](../../../mcp/src/agents_remember/observer/projection.py) |
| The bucket-name rule's server copy: `word[:1].upper() + word[1:]`, why `str.capitalize` was abandoned, `state_count_fields` refusing a non-injective mapping, and `STATE_COUNT_FIELDS`. | L230-L273 | [projection.py](../../../mcp/src/agents_remember/observer/projection.py) |
| `Camel<S>` / `StateCountField<S>` / `LifecycleStateCounts`, the runtime twin `stateCountField`, the private `lifecycleStateCounts`, and `Metrics extends LifecycleStateCounts` — one `number` per live state, so a new live state is a REQUIRED field. | L190-L244 | [projection.ts](projection.ts) |
| `metricsFor`, the client-side mirror of the reducer's rollup, so a fixture derives metrics instead of re-listing buckets. | L245-L257 | [projection.ts](projection.ts) |
| `GateNode.evidenceRefs?` and `LifecycleProjection.stateEnteredAt?` — both marked `LATE MIRROR`, both always on the wire. | L118-L147 | [projection.ts](projection.ts) |
| `ProviderNode` comments mirror the served `repoId` and `worktreeGroup` binding semantics consumed by topology. | L177-L189 | [projection.ts](projection.ts) |
| Drift snapshot metadata mirrors the backend provenance fields used by actionable-drift rows. | L258-L269 | [projection.ts](projection.ts) |
| `TaskSubTaskRefNode` (has `linkedLifecycleId`, no `createdAt`), `SeriesSubTaskNode` (has `createdAt`, no `linkedLifecycleId`), and the `SubTaskRow` union — with the comment recording that collapsing them invented a `createdAt` the server never sends. | L360-L391 | [projection.ts](projection.ts) |
| `SeriesSectionNode` declared separately from `TaskSectionNode`, and the note that structural typing keeps the two interchangeable so the split is a NAME and a SLOT, not a check. | L392-L416 | [projection.ts](projection.ts) |
| `TaskDocNode.id`/`createdAt?`/`lifecycleId?` and the master-navigation fields. | L417-L447 | [projection.ts](projection.ts) |
| `SeriesNode` now carries `SeriesSubTaskNode[]` / `SeriesSectionNode[]` alongside `seriesTokenTotal`. | L448-L464 | [projection.ts](projection.ts) |
| `ATTENTION_SEVERITIES` / `ATTENTION_LANES` as tuples, with the note that Python declares both fields as bare `str` so only a runtime check can bite; `AttentionItem` consumes the derived types. | L465-L495 | [projection.ts](projection.ts) |
| FEUI-L7 optional owner identity and redelivery/escalation fields on `AgentPickupNode`. | L496-L524 | [projection.ts](projection.ts) |
| `PROCESS_FACT_STATES` / `PROCESS_HEALTHS` honesty vocabularies, tuple-first for the same reason. | L525-L556 | [projection.ts](projection.ts) |
| `CommitRefNode` / `ProviderBootNode` / `EngineProcessEdge` — the edge comment now excludes `refused` and states that polarity is derived in the renderer. | L557-L585 | [projection.ts](projection.ts) |
| `LandingRefNode.at?` added beside `observedAt` (ref timestamp vs probe timestamp). | L586-L601 | [projection.ts](projection.ts) |
| `EngineProcessNode` enclosure pod, now including `carryoverDoneAt?`. | L602-L645 | [projection.ts](projection.ts) |
| `ExpectationRowNode` and `Analytics.expectationRows?` (`LATE MIRROR`). | L646-L678 | [projection.ts](projection.ts) |
| The Python models the two split pairs mirror: `GateNode.evidenceRefs`, `LifecycleProjection.stateEnteredAt`, `ExpectationRowNode`, `TaskSubTaskRefNode`/`TaskSectionNode`, `SeriesSubTaskNode`/`SeriesSectionNode`, `EngineProcessNode.carryoverDoneAt`, `Analytics.expectationRows`. | L84; L116; L413-L429; L552-L582; L634-L659; L855; L955 | [projection.py](../../../mcp/src/agents_remember/observer/projection.py) |
| `SupervisorHeartbeat` mirrors the app-injected wire shape, not a `projection.py` model. | L693-L709 | [projection.ts](projection.ts) |
| `WorkspaceProjection` top-level shape. | L710-L726 | [projection.ts](projection.ts) |
| The app-side payload builder `SupervisorHeartbeat` mirrors. | L936 | [serving/app.py](../../../mcp/src/agents_remember/serving/app.py) |
| The contract guard that measures this mirror in three directions, derives `VOCABULARIES` from its closed unions, and pins the removed `refusedPolarity` / split sub-task rows. | L24-L73; L269-L284; L471-L526 | [../test/contract.test.ts](../test/contract.test.ts) |
| The RUNTIME half of the partition guard — the three tests a duplicate within one half fails: the vocabulary-exhaustiveness pooling check, and the two bucket assertions that read `ACTIVE_STATES` (`counts a lifecycle in each live state into its own bucket`, `gives each live state a bucket of its own`). | L346-L376; L404-L469 | [../test/contract.test.ts](../test/contract.test.ts) |
| The fixture builders that type every test's wire node against this mirror. | L1-L46 | [../test/fixtures/wire.ts](../test/fixtures/wire.ts) |

## Series-Contract Notes

`EnclosureNode` separates leaf contract identity (`enclosureId` / `leafId`) from the containing `taskRoot`, which lets dashboard views handle root series tasks and leaf worktrees without deriving paths client-side. 260703-L11 adds the required `codeWorktreeExists` / `memoryWorktreeExists` booleans — the server-stat'ed worktree-existence truth (always on the wire: bool defaults are never `exclude_none`-dropped) that `hasLiveWorktree` filters tasks-surface visibility on, replacing every client-side cleanup-state proxy; `cleanup: reopened` means contract-reset-awaiting-restart, not live work.

## Cross-Repo References

No meaningful cross-repository implementation source governs this repository-local type mirror.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The reviewed behavior is wholly repository-local. | Import and task-boundary review | — |

## Update History

- 2026-08-01T10:45+02:00 — 260731-EFA-L4 curator (post-wave source change): the state vocabulary
  adopted the server's partition after the main wave wrote this card, so the card described a shape
  the file no longer has. **Corrected the central claim.** The file now declares `LIVE_STATES` (L42)
  and `TERMINAL_STATES` (L48) as the two halves and COMPOSES `LIFECYCLE_STATES = [...LIVE_STATES,
  ...TERMINAL_STATES]` (L59); `State` (L61), `TerminalState` (L63) and `ActiveState` (L70) are all
  derived, and `ACTIVE_STATES` (L72) is bound to `LIVE_STATES` directly rather than by subtraction —
  mirroring `projection.py::ACTIVE_STATES = LIVE_STATES` (L227) for the reason that file gives.
  Every sentence describing the old whole-plus-second-list shape with
  `ActiveState = Exclude<State, TerminalState>` was rewritten, the invariant telling a reader to
  "cross-check by hand until the halves-first shape lands here" was replaced, and the `Todos` item
  "**The partition is not adopted here**" was **closed** with a note saying so rather than deleted
  silently. Recorded the new compile-time check — `FiledOnce<S extends never>` (L88) /
  `StatesAreFiledOnce` (L90) — and **proved it non-vacuous myself rather than trusting the comment**:
  on a scratch copy of the file, double-filing `"completed"` onto `LIVE_STATES` and running this
  repository's own `tsc` 5.9.3 under the `tsconfig.app.json` flags produces
  `error TS2344: Type '"completed"' does not satisfy the constraint 'never'.` at L90, while the
  unmodified file compiles clean (exit 0). Recorded the honest gap the same way: a duplicate WITHIN
  one half compiles clean (same harness, exit 0, no diagnostics) because a TypeScript tuple keeps
  repeated members where `Literal["a","a"]` collapses, and is caught only at runtime by
  `contract.test.ts` — which I ran against that mutation and which fails exactly **three** tests,
  including "gives each live state a bucket of its own". Fixed two self-contradictory counts: the
  Logic section said "six runtime values" and listed ten, and Purpose said "two"; the file exports
  **eleven** (`grep -cE "^export (const|function) "`), now stated consistently in Purpose, Logic and
  the invariant. **Citation repairs: all 29 rows in the reference table were re-derived against the
  current source and 24 had moved or were wrong** — every `projection.ts` range (the partition rewrite added ~37
  lines above everything else: e.g. `WorkspaceProjection` L674-L689 → L710-L726,
  `EngineProcessNode` L566-L608 → L602-L645, `PROCESS_*` L487-L519 → L525-L556) and every
  `projection.py` range at or after the rewritten comment (a uniform +10: `TaskSubTaskRefNode`
  L542-L568 → L552-L582, `Analytics.expectationRows` L945 → L955, `carryoverDoneAt` L845 → L855).
  Two rows were wrong in kind rather than by offset and were rebuilt: the `lifecycle_state.py`
  partition row cited L101-L146 for `check_state_partition`, which is at **L73-L98** — outside the
  range — so it is now two rows; and the row claiming `projection.py` "states outright that the
  mirror has NOT adopted the partition" cited a comment that has since been rewritten to say the
  opposite. Added three rows (the compile-time check, `PHASES` as its own row, and the runtime
  bucket tests in `contract.test.ts` that catch the within-half duplicate). The five ranges that
  still land unchanged: the `projection.ts` header L1-L12, `projection.py` L1-L9,
  `serving/app.py` L936, `contract.test.ts` L24-L73; L269-L284; L471-L526, and
  `test/fixtures/wire.ts` L1-L46.
  Verification metadata pinned until closeout stamps the L4 commit.

- 2026-08-01T09:05+02:00 — 260731-EFA-L4 curator: body corrected against the landed diff. Removed the
  false claim that this is a pure type module (it now exports eight vocabulary tuples plus
  `stateCountField`/`metricsFor`); removed the false `TaskSubTaskRefNode.createdAt` claim from Purpose,
  Logic and the citation table (the field moved to the new `SeriesSubTaskNode`); rewrote the slice-05o
  paragraph, which described `refusedPolarity` and a `refused` edge state as live wire signals — both
  were mirror inventions with no Python model behind them and are now REMOVED. Added the L4 subsection
  (tuple-first vocabularies, derived `Metrics` buckets, the reconciled camel rule, the two un-collapsed
  model pairs, `LATE MIRROR`, `LandingRefNode.at?` / `EngineProcessNode.carryoverDoneAt?` /
  `ExpectationRowNode`) and six invariants. Recorded three limits rather than flattening them: the
  terminal/live split is NOT a composed partition on this side (`projection.py` L199-L217 says so and
  names the fix), `SeriesSectionNode` is a slot and not a check, and the mirror↔server link is held by
  no test because `snapshot.json` is hand-maintained. Re-derived all 12 pre-existing citations — every
  range had moved (e.g. `WorkspaceProjection` L389-L397 → L674-L689, `EngineProcessNode` L332-L373 →
  L566-L608, `ProcessFactState`/`ProcessHealth` L269-L287 → L487-L519) — and added 17 more. Verification
  metadata pinned to the leaf base until closeout stamps the L4 code commit.

- 2026-07-24T13:17:50Z — Documented optional dirty serving-build evidence and comment-only cleanup.
  Verification hash/date remain pinned to the pre-commit source stamp.

- 2026-07-18T12:43+02:00 — FEUI-L9R: recorded the optional app-injected dashboard fingerprint and
  its unknown-on-absence boundary; verification metadata remains pinned pending closeout.
- 2026-07-17T23:54+02:00 — 260715-FEUI-L7 mirrored optional pickup owner identity and
  redelivery/escalation timestamps/counts. Optionality preserves pre-field persisted projections;
  consumers must not synthesize missing facts. Verification metadata remains pinned to the leaf
  base until closeout.
- 2026-07-12T17:30+02:00 — 260712-TRH-L7: kept the projection wire contract in lockstep by typing stale landing facts and observed/attempt/age freshness fields.

- 2026-07-10T01:14+02:00 — 260707-HFX2-L13 F6: added optional `TaskDocNode.bodyRevision`, the
  cache invalidation token for on-demand reader bodies omitted from the summary broadcast.
  Verification metadata remains pinned until closeout stamps the eventual L13 code commit.

- 2026-07-08T23:59+02:00 — 260707-HFX2-L8 (dead-seat storm observability, R6): extended
  `SupervisorHeartbeat` with `pendingInboxCount`, `redeliverableInboxCount`, and
  `lastSweepDurationSeconds`, matching the app-injected `/api/state` payload. Verification metadata
  pinned until closeout stamps the 260707-HFX2-L8 commit.
- 2026-07-08T18:45+02:00 — 260707-HFX2-L2 (supervisor sweep, R5): added `SupervisorHeartbeat`
  (`lastTickAt: string | null`, `ageSeconds: number | null`, `staleCutoffSeconds: number`,
  `stale: boolean`) and the optional `WorkspaceProjection.supervisorHeartbeat?` — a SECOND
  app-injected, non-`projection.py` field alongside `servingBuild?` (same posture: injected onto
  `/api/state`/the SSE snapshot only, excluded from the ETag revision, absent from persisted
  `latest-state.json`). `lastTickAt: null` (never ticked) is documented as distinct from
  `stale: true`. Verification metadata pinned until closeout stamps the 260707-HFX2-L2 commit.
- 2026-07-07T05:22+02:00 — 260703-L15 S3: added `ServingBuild` (`version`, `bootedAt`,
  `commit?`) and the optional `WorkspaceProjection.servingBuild?` — the app-injected boot-time
  serving stamp (NOT a `projection.py` mirror; wire-only, absent in persisted projections).
  Verification metadata pinned until closeout stamps the L15 commit.
- 2026-07-06T23:57:12+02:00 — 260703-L14 (visual hierarchy + chat grouping): mirrored
  `TaskDocNode.orchestrates?: string[]` — the orchestration-command relation from `projection.py`;
  optional for forward-compat with pre-L14 persisted projections (consumers guard with
  `?? []`). Verification metadata pinned until closeout stamps the L14 commit.
- 2026-07-06T03:00+02:00 — 260703-L11: mirrored the new required
  `EnclosureNode.codeWorktreeExists`/`memoryWorktreeExists` existence-truth flags (stat'ed server-side
  at snapshot time; the tasks-surface visibility rule). Verification metadata pinned until closeout
  stamps the L11 commit.
- 2026-07-04T12:31+02:00 - L3: mirrored the expanded `AgentPickupNode`
  metadata for agent-to-agent inbox delivery state. Verification metadata pinned
  until closeout stamps the L3 commit.
- 2026-06-28T07:32+02:00 — Task 29 S7 follow-up: mirrored drift snapshot provenance fields
  (`checkedAt`, `sourceRoot`, `memoryRoot`, `reportPath`) used for actionable-drift detail and targetless
  dismissal freshness. Verification metadata pinned until closeout stamps the task-29 code commit.
- 2026-06-28T07:30+02:00 — Task 33: mirrored the new required `WorkspaceProjection.activeWorktreeGroups:
  string[]` (the bounded active worktree-group set the Topology filters on; required because the server
  field is a list default, never `exclude_none`-dropped). Verification metadata pinned until closeout
  stamps the code commit.
- 2026-06-28T03:52+02:00 — Task 28 S5.2 after source sync: mirrored
  `LifecycleProjection.stateEnteredAt` / `AttentionItem.signalTs?` as the current-occurrence
  acknowledgement anchors for lifecycle-scoped attention dismissals. Verification metadata pinned until
  closeout stamps the task-28 code commit.
- 2026-06-27T23:08+02:00 — Task 31 provider-state honesty: mirrored `ProviderBootNode.runtimeState="missing"` for expected provider slots with no observed runtime fact. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-26T20:18+02:00 — Task 21 series token rollup: mirrored `SeriesNode.seriesTokenTotal`, the
  server-derived aggregate token count displayed by the master reader. Verification metadata pinned until
  closeout stamps the code commit.
- 2026-06-25T13:20+02:00 — Task 23/24: mirrored `AttentionItem.gateId`, `AgentPickupNode`, and `Analytics.agentPickups` for gate deletion actions and task-row pickup feedback.
- 2026-06-24T18:11+02:00 — Task 17 live-data numbering: mirrored required `TaskDocNode.id`, the
  JSON-primary task id used by dashboard labels for authored leaf rows. Verification metadata pinned
  until closeout stamps the code commit.
- 2026-06-24T16:33+02:00 — Task 17 task-document-first Operations: mirrored optional
  `TaskDocNode.lifecycleId?` and `SeriesNode.createdAt?` from the server projection so planning-only
  documents remain readable and master rows keep structured creation-order metadata. Verification
  metadata pinned until closeout stamps the code commit.
- 2026-06-24T12:21+02:00 — Task 17 projection mirror: added the optional `createdAt` ordering fields
  on task/sub-task rows, the folder-keyed `SeriesNode.objective`/master shape, and `Analytics.series`
  as the master reader surface consumed by `DetailPanel`. Verification metadata pinned until closeout
  stamps the code commit.
- 2026-06-24T08:59+02:00 — Task-document sections correction: clarified that
  `TaskDocNode.sections` mirrors JSON task-document sections, including non-master freeform sections,
  and does not carry `series-contract.md` content. Verification metadata pinned until closeout stamps
  the code commit.
- 2026-06-24T08:09+02:00 — Engine Room leaf identity: mirrored `EngineProcessNode.leafId` from the server projection so dashboard renderers can label concrete leaf enclosures separately from their parent `taskName`. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: `EnclosureNode` gained `enclosureId`, `leafId`, and `taskRoot` so dashboard views can distinguish root task folders, leaf enclosure contracts, and stable leaf identity. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-23T21:46+02:00 — Task 12 S2: clarified `ProviderNode.repoId` as covered-repo metadata for
  workspace providers and owning-repo metadata for worktree providers, with `worktreeGroup` documented as
  the precedence join key. Verification metadata pinned until closeout stamps the S2 code commit.
- 2026-06-22T11:00 — slice 05o refused-conduit signal: added a `refused` member to the `EngineProcessEdge.state` union plus an optional `refusedPolarity?: "amber" | "red"` field (amber = a soft reroute/fallback, red = a fault/conflict), the projection signal that drives the new refused-conduit flash (T9B red, T9C amber, T14C red); lockstep with projection.py (`?:` = the server's `exclude_none` omission). Verification metadata pinned until closeout stamps the 05o code commit.
- 2026-06-21T02:44+02:00 — Slice 6g: mirrored the master-navigation additions from `projection.py` — `TaskSubTaskRefNode` (+`linkedLifecycleId?`), `TaskSectionNode`, and `subTasks`/`sections`/`masterLifecycleId?` on `TaskDocNode`. Verification metadata pinned until closeout stamps the 6g code commit.
- 2026-06-19T06:39+02:00 — engine-room crash fix: relaxed `EngineProcessNode.landing` to optional (`landing?:`) — a pre-5h/persisted projection omits it, and `EnclosureCanvas` was crashing on `node.landing.find`. Forward-compat, not an `exclude_none` change. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T21:25+02:00 — slice 5h Tier 2: mirrored the four optional `LedgerRefNode` fields `codeSubject?`/`codeDate?`/`memorySubject?`/`memoryDate?` (lockstep with projection.py; `?:` = the server's `exclude_none` omission). Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T18:00+02:00 — slice 5h ledger popover: mirrored `LedgerRefNode` + `LedgerNode.rows` + `EngineProcessNode.ledgerRows`/`ledgerRowCount` (lockstep with projection.py). Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T14:05 — Task 6 slice 6c Part A: mirrored `GateNode` + the optional `LifecycleProjection.gate` from `projection.py`. Verification metadata pinned until closeout stamps the 6c Part A code commit.
- 2026-06-18T08:51+02:00 — slice 5h H1: mirrored `LandingRefNode` + the additive `landing[]` / `integrationStrategy?` fields on `EngineProcessNode` (lockstep with projection.py). Verification metadata pinned until closeout stamps the 5h code commit.
- 2026-06-15T19:35 — Created for slice 5e: TS mirror of the served projection contract; slice 5e adds CommitRefNode/ProviderBootNode/EngineProcessEdge/EngineProcessNode + ProcessFactState/ProcessHealth + Analytics.engineProcesses. Verification metadata pinned until closeout stamps the 5e code commit.
