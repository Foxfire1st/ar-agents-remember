# dashboard/src/types/projection.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/types/projection.ts`              |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-01T10:45+02:00                           |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb`       |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src/ overview](../overview.md)

## Purpose

Generated TypeScript mirror of the served projection contract. The canonical core input is `WorkspaceProjection.model_json_schema()`, the served-only tail comes from `ServedWorkspaceProjection.model_json_schema()`, and `scripts/sync-projection-types.py --check` fails when either the schema artifact or this file is stale. camelCase matches the wire form, and schema required/nullable/default information determines whether a generated field is required or optional. Slice 5e extends the contract with the enclosure-centered Engine Room process map: `CommitRefNode` / `ProviderBootNode` / `EngineProcessEdge` / `EngineProcessNode`, the `ProcessFactState` / `ProcessHealth` honesty enums, and the `Analytics.engineProcesses` derived surface. Slice 6g mirrors the master-navigation additions: `TaskSubTaskRefNode` (with `linkedLifecycleId`), `TaskSectionNode`, and `subTasks` / `sections` / `masterLifecycleId` on `TaskDocNode`. (6g originally gave `TaskSubTaskRefNode` an optional `createdAt` as well; 260731-EFA-L4 removed it and split the interface — see the L4 subsection below.) Task 17 makes `TaskDocNode.lifecycleId?` optional because runtime lifecycle state is attachment, not the condition for projecting a JSON-primary task document; planning-only leaves and masters can be listed/read before a worktree exists. Task 17 also mirrors `TaskDocNode.id`, the JSON-primary task id used as the authored leaf display number when parent sub-task refs are only fallback rows. The masters surface is still also exposed as `Analytics.series: SeriesNode[]`, carrying folder-keyed master content with `createdAt`, `objective`, sections, decisions, sub-task creation metadata for default oldest-first ordering, and `seriesTokenTotal` for the server-composed leaf-lifecycle token aggregate.

**260731-EFA-L6 changes what kind of file this is.** The generator emits the model declarations plus the runtime vocabulary/metric helpers the dashboard consumes: the state vocabulary is composed from its two halves, `State` and `Phase` derive from exported tuples, and `Metrics` bucket names derive from the live half. This module still emits the enumerable runtime values and `stateCountField`/`metricsFor`; they are generator output now, not hand-copied declarations.

## Code Commentary

### FEUI-L9R Reviewed Candidate Delta

`ServingBuild` now optionally mirrors `dashboardBuild`, the fingerprint of the shipped dashboard
inputs. Like the containing `servingBuild` block, it is app-injected wire truth rather than persisted
`projection.py` reducer state. Absence means a legacy or otherwise non-comparable server and must
remain unknown; it is not evidence of mismatch.

### 260707-HFX2-L13 Task-Body Revision

`TaskDocNode.bodyRevision` mirrors the server-generated digest of reader-body fields omitted from the
always-on summary. It is required by the current generated contract; the detail reader combines it
with `docPath` as the on-demand body cache key. Summary fields such as identity, status, progress,
steps, sub-task links, and routing metadata remain in the broadcast contract.
cit:([`bodyRevision`], dashboard/src/types/projection.ts:439-439)

### Logic

**No longer a pure type module.** Since 260731-EFA-L4 it emits **eleven** runtime values: eight `as const` vocabulary tuples — `LIVE_STATES`, `TERMINAL_STATES`, `LIFECYCLE_STATES`, `PHASES`, `ATTENTION_SEVERITIES`, `ATTENTION_LANES`, `PROCESS_FACT_STATES`, `PROCESS_HEALTHS` — plus `ACTIVE_STATES` (a `readonly ActiveState[]` bound directly to `LIVE_STATES`, not a tuple of its own) and the functions `stateCountField` and `metricsFor`. Everything else is still type-only. The top-level shape is `WorkspaceProjection`: `version`, `generatedAt`, `lifecycles: LifecycleProjection[]`, `enclosures: EnclosureNode[]`, `providers: ProviderNode[]`, `activeWorktreeGroups: string[]` (required — the worktree-group basenames with a live enclosure lifecycle; the bounded set the Topology filters on, join key = worktree `ProviderNode.worktreeGroup` / basename of `EnclosureNode.worktreeGroup`; always present because the server default is a list, never `exclude_none`-dropped), `metrics: Metrics`, and `analytics: Analytics`. Core nodes — `LifecycleProjection` (state/phase/tokens + `stateEnteredAt`, `tokenSeries`, `actions`), `EnclosureNode`, `ProviderNode` (with `scope` workspace|worktree, `role` code|memory, optional `repoId`, and optional `worktreeGroup`), `Metrics`, plus the analytics children (`DriftSnapshotNode`, `SidecarStaleNode`, `SetupSummaryNode`, `SetupProgressNode`, `RouteCoverageNode`, `ToolReportNode`, `LedgerNode`, the `TaskDocNode` tree, and the reducer-derived `AttentionItem`). Slice 6c adds `GateNode` and the optional `LifecycleProjection.gate` — the durable gate the cockpit reviews (`decisions` = the verbs an open gate can POST). cit:([`State`], dashboard/src/types/projection.ts:15-15) and cit:([`Phase`], dashboard/src/types/projection.ts:29-29) are no longer hand-written unions: each is `(typeof <TUPLE>)[number]` over an exported `as const` tuple, so a consumer that needs to *enumerate* the vocabulary reads the one list instead of copying a second.

Slice 5e adds the engine-room process map. `ProcessFactState` includes `observed`, `derived`,
`planned`, `missing`, `stale`, and `not-applicable`; `ProcessHealth` carries the eight rollup states.
The generated declarations include `CommitRefNode`, `ProviderBootNode`, `EngineProcessEdge`, and
`EngineProcessNode`, including required `landing: LandingRefNode[]` and optional
`integrationStrategy`. `EngineProcessEdge` has no `refusedPolarity`; flash polarity remains a
renderer derivation (`failed` → red fault, `stale` → amber reroute), not commentary embedded in the
generated source. `contract.test.ts` retains the inverted pin against reintroducing the field.

Slice 6g extends generated `TaskDocNode` navigation/content with required `subTasks`, `sections`,
`orchestrates`, `id`, and `createdAt` fields; `lifecycleId?` remains an optional runtime binding.
`SeriesNode.createdAt` is required, while `SeriesSubTaskNode.createdAt?` remains optional. `SeriesNode`
carries the folder-keyed master shape. Analytics now
requires `agentPickups`; each `AgentPickupNode` has required `attemptCount` plus optional owner and
attempt/escalation timestamps. `AttentionItem.signalTs?` and drift provenance fields remain optional
where the generated schema permits omission.
cit:([`TaskDocNode`], dashboard/src/types/projection.ts:437-463)
cit:([`SeriesNode`], dashboard/src/types/projection.ts:346-361)
cit:([`SeriesSubTaskNode`], dashboard/src/types/projection.ts:379-386)

### Generated Vocabulary, Model, And Required-Field Structure

**The generator emits vocabularies as tuples.** Eight closed vocabularies are declared as `as const`
tuples with their types derived from them: `LIVE_STATES`, `TERMINAL_STATES`, `LIFECYCLE_STATES`,
`PHASES`, `ATTENTION_SEVERITIES`, `ATTENTION_LANES`, `PROCESS_FACT_STATES`, and
`PROCESS_HEALTHS`. The rationale is recorded here rather than in generated comments: runtime
membership checks need enumerable values, and JSON-module literals widen to `string`.
`contract.test.ts::VOCABULARIES` consumes the tuples for sample coverage.

**The state vocabulary is now a COMPOSED partition, matching the server.** The halves are written out
first — cit:([`LIVE_STATES`], dashboard/src/types/projection.ts:9-9) and cit:([`TERMINAL_STATES`], dashboard/src/types/projection.ts:11-11) — and the whole is assembled from
them: `LIFECYCLE_STATES = [...LIVE_STATES, ...TERMINAL_STATES]`. cit:([`LIFECYCLE_STATES`, `State`, `TerminalState`, `ActiveState`, `ACTIVE_STATES`], dashboard/src/types/projection.ts:13-13; dashboard/src/types/projection.ts:15-15; dashboard/src/types/projection.ts:17-17; dashboard/src/types/projection.ts:19-19; dashboard/src/types/projection.ts:21-21) derives the whole and its halves, with
`ACTIVE_STATES` bound to `LIVE_STATES` **directly**, not by subtraction — mirroring
`projection.py::ACTIVE_STATES = LIVE_STATES` cit:([`ACTIVE_STATES`], mcp/src/agents_remember/observer/projection.py:236-236) and for the reason that file gives: a set
difference re-derives the answer from a second list that could itself be wrong.

This replaced the previous shape, which is worth naming because the card used to describe it: one
list of six (`LIFECYCLE_STATES`) plus a SECOND, independent list of two (`TERMINAL_STATES`), with
`ActiveState = Exclude<State, TerminalState>`. Two lists naming one vocabulary can disagree and
nothing noticed — `Exclude` over a member the whole never contained removes nothing, silently, so the
terminal half could have named a state that did not exist and every gate stayed green. Composed from
the halves there is no second list left to disagree: filing a state on a half is what puts it in the
vocabulary at all. Both halves stay exported so consumers can enumerate the producer partition
without hand-rolling a second list.

**The partition check is real, and it is a compile-time one.** The generator emits
`type FiledOnce<S extends never> = S` and
`export type StatesAreFiledOnce = FiledOnce<ActiveState & TerminalState>`. Disjoint
string-literal unions intersect to `never`, so the constraint holds exactly while the halves are
disjoint. Verified non-vacuous by mutation on a copy of this file, not taken on trust: double-filing
`"completed"` onto `LIVE_STATES` and running the repository's own `tsc` (5.9.3) under the
`tsconfig.app.json` flags fails with
`error TS2344: Type '"completed"' does not satisfy the constraint 'never'.`; the unmodified file
compiles clean. `StatesAreFiledOnce` is exported because `noUnusedLocals` rejects
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
not absent. cit:([`ACTIVE_STATES`], mcp/src/agents_remember/observer/projection.py:236-236) states the same asymmetry from the other side.

**`Metrics` buckets are derived, not listed.** cit:([`Camel`, `StateCountField`, `LifecycleStateCounts`], dashboard/src/types/projection.ts:288-290; dashboard/src/types/projection.ts:292-292; dashboard/src/types/projection.ts:294-294)
computes the field name from the state name; `Metrics extends LifecycleStateCounts` gains a REQUIRED field the day a
live state is filed on `LIVE_STATES` and every object claiming to be a `Metrics` stops compiling until
it counts it. Filing one on `TERMINAL_STATES` adds no field — the filing doing its job, not an
omission. cit:([`stateCountField`, `metricsFor`], dashboard/src/types/projection.ts:296-300; dashboard/src/types/projection.ts:319-326) is the runtime twin and the
client-side mirror of `reducer.py::_metrics`, so a fixture states its lifecycles and gets the metrics
the server would have sent instead of re-listing buckets beside them.

The camel rule has two copies and they were reconciled in this leaf: each segment after the first has
its FIRST character upper-cased and **the tail left alone**. Python used `str.capitalize()`, which
lower-cases the tail, so `awaiting-DEVELOPER` bucketed to `awaitingDeveloperCount` server-side and
`awaitingDEVELOPERCount` here — one rule with two answers. Settled in favour of this spelling
(`projection.py::state_count_field` now does `word[:1].upper() + word[1:]`) because `Capitalize<>`
cannot lower-case a tail at the type level and because lower-casing merges two states differing only
in tail case.

**Two model pairs were un-collapsed.** cit:([`TaskSubTaskRefNode`, `SeriesSubTaskNode`], dashboard/src/types/projection.ts:379-386; dashboard/src/types/projection.ts:494-501) are two distinct `extra="forbid"` server models that this mirror had collapsed into one
interface. The collapse invented a `createdAt` on the master row that the server never sends and lent
`linkedLifecycleId` to series rows that never carry it. They share five fields and differ in exactly
one each. cit:([`SubTaskRow`, `SeriesNode`], dashboard/src/types/projection.ts:346-361; dashboard/src/types/projection.ts:515-515) is the union the sub-task index;
`SeriesNode.subTasks` is now `SeriesSubTaskNode[]`.

cit:([`SeriesSectionNode`], dashboard/src/types/projection.ts:363-367) is the same situation one model over — a separate `extra="forbid"`
Python model from cit:([`TaskSectionNode`], dashboard/src/types/projection.ts:465-469). The two declare the same three fields, so TypeScript's structural typing keeps them
interchangeable (`DetailPanel.tsx::seriesAsMasterDoc` assigns one array to the other), no assertion
over any payload can separate them, and `contract.test.ts`'s structural walk never will. It is a NAME
and a SLOT for the day the server adds a field to one of them — not a check. The generator now emits
both named declarations from their separate schemas, while structural assignment remains possible
until their fields diverge.

**Schema-required fields are required.** Generated `GateNode.evidenceRefs`,
`LifecycleProjection.stateEnteredAt`, and `Analytics.expectationRows` have no `?`; the former
client-tolerance optionality is gone. Hand-written fixtures must supply them through typed builders or
the sampled bases rather than weakening the generated contract.

**Additive fields.** cit:([`LandingRefNode`, `observedAt`], dashboard/src/types/projection.ts:239-249) — the ref's own merge/push timestamp, distinct from
the probe's observation; cit:([`EngineProcessNode`, `carryoverDoneAt`], dashboard/src/types/projection.ts:162-202) — when memory carryover landed,
absent until it has; cit:([`ExpectationRowNode`], dashboard/src/types/projection.ts:204-215) — one outstanding supervisor expectation
(`dueAt`/`overdue`), reached from required `Analytics.expectationRows`.

### Invariants And Boundaries

- The Pydantic projection schema is the source of truth. Change the Python model, run
  `scripts/sync-projection-types.py`, and require `--check` to pass; do not edit this generated file.
  The output includes the runtime vocabulary tuples, `ACTIVE_STATES`, `stateCountField`, and `metricsFor`.
- Optional (`?:`) fields follow schema omission/nullability/compatibility. Required collection/default
  fields remain required, including `landing`, `orchestrates`, `agentPickups`, `expectationRows`,
  `evidenceRefs`, and `stateEnteredAt`.
- Closed vocabularies in this file are generated from producer-side `Literal`/typed aliases exposed as
  Pydantic schema enums. A producer vocabulary change changes the generated tuple/union, and
  `scripts/sync-projection-types.py --check` rejects stale committed output. `contract.test.ts`
  separately checks whether the manual snapshot exercises every generated vocabulary member/path and
  catches a duplicate within a tuple; it is sample coverage, not producer authority
  cit:([`VOCABULARIES`], dashboard/src/test/contract.test.ts:268-293).
  Do not hand-edit a generated tuple or replace it with a hand-written union.
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
- `TaskDocNode.createdAt` and `SeriesNode.createdAt` are required structured ordering fields supplied
  by the server; `SeriesSubTaskNode.createdAt?` is optional. Consumers may sort by the optional field
  only where the schema permits it, and must not derive creation order by parsing `number` or filename
  prefixes. cit:([`TaskDocNode`, `SeriesNode`, `SeriesSubTaskNode`], dashboard/src/types/projection.ts:356-371; dashboard/src/types/projection.ts:379-386; dashboard/src/types/projection.ts:437-463)
- `SeriesNode.seriesTokenTotal` is server-derived. Dashboard consumers display it; they do not recompute
  it from lifecycle gauges or task-doc rows.
- `landing` is a required generated list field; consumers need no mirror-side optionality workaround.
- `engineProcesses` and `attentionQueue` are derived surfaces composed server-side; the client renders them verbatim and preserves server order (no re-sort, no re-derivation).
- `AttentionItem.signalTs?` and required `LifecycleProjection.stateEnteredAt` are server-computed lifecycle acknowledgement anchors. Clients forward ids/kinds only; they do not decide suppression freshness.
- `DriftSnapshotNode.checkedAt?` is the repo-level acknowledgement anchor for actionable drift; clients render/dismiss it but do not reclassify drift.
- `agentPickups` is also server-derived. Clients render the projected `waiting-for-agent` or `check-chat`
  state, role/message/delivery metadata, and do not run their own pickup TTL timers.
- FEUI-L7's optional pickup owner/redelivery fields are additive compatibility mirrors. Consumers
  display absence as absence; they do not synthesize owner identity, attempt counts, timestamps,
  or escalation state for older persisted rows.
- `EngineProcessNode.id` is the stable enclosure id and the join key to `EnclosureNode.enclosure`; `ProviderNode.worktreeGroup` is the join key to the owning enclosure and takes precedence over `ProviderNode.repoId` in topology parenting.
- Ages (`*Seconds`) and fact-state are server-computed (never `Date.now()`); `nextAction` is display/copy-only until slice 06. Since 260703-L15 the served age fields are also *volatile* to the change gate (excluded from server diff + client merge equality — `data/servedAges.ts`), and displays advance them locally from arrival anchors.
- `servingBuild?` (260703-L15) is the ONE field NOT mirrored from `projection.py`: it is injected app-side (`serving/build_info.py` via `serving/app.py`) onto `/api/state` and the SSE snapshot only, so it is optional here and absent from persisted `latest-state.json` (a pre-L15 server also sends none).
- `agentNotifierHeartbeat?` (260707-HFX2-L2 R5, expanded by HFX2-L8 R6) is a SECOND app-injected, non-`projection.py` field,
  same posture as `servingBuild?`: `serving/agent_notifier_heartbeat.py` via `serving/app.py` attaches it
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

Optional fields reflect the generated schema or the explicitly served-only app tail; app-injected
fields remain distinguished from projection-reducer output. Required producer fields are not made
optional to preserve hand-written fixtures. A closed vocabulary is emitted tuple-first (`as const`
runtime list, type derived from it) so consumers enumerate rather than copy.

### Todos

Schema generation closes the former producer-to-TypeScript gap. The remaining limits are properties
of TypeScript or sample coverage, not deferred codegen:

- **A duplicate within one half is not a compile-time error.** Composition and `StatesAreFiledOnce`
  rule out an unfiled state and a double-filed one; a TypeScript tuple still admits
  `["running", "running", …]`, which Python's `Literal` would collapse. Only `contract.test.ts`
  catches it at runtime.
- **`SeriesSectionNode` vs `TaskSectionNode` is a slot, not a check.** Same three fields, so
  structural typing keeps them interchangeable and no payload walk can separate them.
- **The manual snapshot can still under-sample the generated contract.** `contract.test.ts` measures
  this explicitly; it is a fixture-coverage limit, not a producer-schema drift gap.
- **Runtime tuple integrity still needs runtime checks.** TypeScript cannot reject a duplicate inside
  one tuple half, so the vocabulary/bucket assertions remain load-bearing.

### 2026-07-24 Curator Delta

`ServingBuild` now exposes optional `dirty` wire evidence so the frontend can distinguish a base commit
hash from an uncommitted serving checkout. The rest of this round's changes remove task provenance from
comments without changing projection schema semantics.

## Docs References

No relevant documentation was found after checking the configured sources; the wire-shape claims
are proven by repository source and tests.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external or domain documentation was found for this repository-local type mirror. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The generated header names the top-level `WorkspaceProjection` shape. | `WorkspaceProjection` | dashboard/src/types/projection.ts:517-528 |
| The generated state partition declarations: `LIVE_STATES`, `TERMINAL_STATES`, composed `LIFECYCLE_STATES`, and derived `State`. | `LIVE_STATES`, `TERMINAL_STATES`, `LIFECYCLE_STATES`, `State` | dashboard/src/types/projection.ts:9-9; dashboard/src/types/projection.ts:11-11; dashboard/src/types/projection.ts:13-13; dashboard/src/types/projection.ts:15-15 |
| `TerminalState`, `ActiveState`, and `ACTIVE_STATES = LIVE_STATES` are derived from the live/terminal partition. | `TerminalState`, `ActiveState`, `ACTIVE_STATES` | dashboard/src/types/projection.ts:17-17; dashboard/src/types/projection.ts:19-19; dashboard/src/types/projection.ts:21-21 |
| The generated compile-time partition declarations `FiledOnce<S extends never>` and `StatesAreFiledOnce = FiledOnce<ActiveState & TerminalState>`. | `FiledOnce`, `StatesAreFiledOnce` | dashboard/src/types/projection.ts:23-23; dashboard/src/types/projection.ts:25-25 |
| Generated `PHASES` tuple and derived `Phase` type. | `PHASES`, `Phase` | dashboard/src/types/projection.ts:27-27; dashboard/src/types/projection.ts:29-29 |
| The served docstring describes the persisted/served contract, camelCase wire convention, and `extra="forbid"` boundary. | "The projection schema: the resolved state the reducer produces." | mcp/src/agents_remember/observer/projection.py:1-9 |
| The partition helper this file's compile-time check mirrors: `check_state_partition` and the `LifecycleVocabularyError` it raises. | `LifecycleVocabularyError`, `check_state_partition` | mcp/src/agents_remember/observer/lifecycle_state.py:30-38; mcp/src/agents_remember/observer/lifecycle_state.py:73-98 |
| The server-side vocabulary writes `LiveState` and `TerminalState` as halves, composes `State`, and builds phase/state tuples through the partition check (halves/state/phase declared in `models/lifecycle.py` since L9; tuples stay in observer). | "LiveState = Literal["; "TerminalState = EndOutcome"; "State = Literal[LiveState"; "Phase = Literal["; "STATES: tuple[State"; "LIVE_STATES: tuple[LiveState"; "TERMINAL_STATES: frozenset[str] = frozenset(vocabulary_names(" | mcp/src/agents_remember/models/lifecycle.py:16-19; mcp/src/agents_remember/models/lifecycle.py:20-27; mcp/src/agents_remember/observer/lifecycle_state.py:102-104; mcp/src/agents_remember/observer/lifecycle_state.py:105-107; mcp/src/agents_remember/observer/lifecycle_state.py:108-108 |
| The server-side mirror comment records the same partition shape and the runtime duplicate-within-half limit. | `ACTIVE_STATES` | mcp/src/agents_remember/observer/projection.py:236-236 |
| The server bucket-name rule uses the preserved-tail camel transform and rejects non-injective mappings. | `state_count_field`, `state_count_fields`, `STATE_COUNT_FIELDS` | mcp/src/agents_remember/observer/projection.py:239-254; mcp/src/agents_remember/observer/projection.py:257-279; mcp/src/agents_remember/observer/projection.py:282-282 |
| `Camel<S>`, `StateCountField<S>`, `LifecycleStateCounts`, `stateCountField`, `lifecycleStateCounts`, and `Metrics extends LifecycleStateCounts` derive one number per live state. | `Camel`, `StateCountField`, `LifecycleStateCounts`, `stateCountField`, `lifecycleStateCounts`, `Metrics` | dashboard/src/types/projection.ts:288-290; dashboard/src/types/projection.ts:292-292; dashboard/src/types/projection.ts:294-294; dashboard/src/types/projection.ts:296-300; dashboard/src/types/projection.ts:302-311; dashboard/src/types/projection.ts:313-317 |
| `metricsFor` is the client-side mirror of the reducer rollup. | `metricsFor` | dashboard/src/types/projection.ts:319-326 |
| `GateNode.evidenceRefs` is required in the generated contract. | `evidenceRefs` | dashboard/src/types/projection.ts:231-231 |
| `LifecycleProjection.stateEnteredAt` is required in the generated contract. | `stateEnteredAt` | dashboard/src/types/projection.ts:283-283 |
| `Analytics.expectationRows` is required in the generated contract. | `expectationRows` | dashboard/src/types/projection.ts:94-94 |
| Generated `ProviderNode.scope`, `repoId`, and `worktreeGroup` are topology inputs in the wire declaration. | "export interface ProviderNode {" | dashboard/src/types/projection.ts:332-345 |
| Topology uses provider scope to choose workspace/worktree ownership. | `groupKey`, `buildTopology` | dashboard/src/topology/model.ts:99-99; dashboard/src/topology/model.ts:117-221 |
| Generated `ProviderNode.role` is a field in the wire declaration. | `ProviderNode` | dashboard/src/types/projection.ts:325-336 |
| Engine Room labels workspace engines from provider role. | `engineLabel` | dashboard/src/panels/EngineRoom.tsx:68-70 |
| Enclosure canvas selects code/memory engines from provider role. | "role="img"" | dashboard/src/panels/engine-room/EnclosureCanvas.tsx:69-69 |
| Drift snapshot metadata mirrors backend provenance fields used by actionable-drift rows. | `DriftSnapshotNode` | dashboard/src/types/projection.ts:121-131 |
| Generated `TaskSubTaskRefNode` has `linkedLifecycleId` and no `createdAt`; `SeriesSubTaskNode` has `createdAt` and no `linkedLifecycleId`; `SubTaskRow` unites them. | `TaskSubTaskRefNode`, `SeriesSubTaskNode`, `SubTaskRow` | dashboard/src/types/projection.ts:369-376; dashboard/src/types/projection.ts:494-501; dashboard/src/types/projection.ts:515-515 |
| Generated `SeriesSectionNode` and `TaskSectionNode` are separate declarations, with structural typing remaining a documented limit. | `SeriesSectionNode`, `TaskSectionNode` | dashboard/src/types/projection.ts:363-367; dashboard/src/types/projection.ts:465-469 |
| `TaskDocNode.id`, required `createdAt`, optional `lifecycleId`, and master-navigation fields are generated here. | "export interface TaskDocNode {" | dashboard/src/types/projection.ts:437-463 |
| `SeriesNode` carries `SeriesSubTaskNode[]`, `SeriesSectionNode[]`, and `seriesTokenTotal`. | `SeriesNode`, `seriesTokenTotal` | dashboard/src/types/projection.ts:356-371 |
| Generated `ATTENTION_SEVERITIES` / `ATTENTION_LANES` tuples and derived `AttentionItem` fields. | `ATTENTION_SEVERITIES`, `ATTENTION_LANES`, `AttentionItem` | dashboard/src/types/projection.ts:31-31; dashboard/src/types/projection.ts:35-35; dashboard/src/types/projection.ts:95-109 |
| FEUI-L7 optional owner identity and redelivery/escalation fields on `AgentPickupNode`, with required `attemptCount`. | `AgentPickupNode`, `attemptCount` | dashboard/src/types/projection.ts:54-77 |
| `PROCESS_FACT_STATES` is the process-fact honesty vocabulary. | `PROCESS_FACT_STATES` | dashboard/src/types/projection.ts:39-39 |
| `PROCESS_HEALTHS` is the process-health honesty vocabulary. | `PROCESS_HEALTHS` | dashboard/src/types/projection.ts:43-43 |
| Generated `CommitRefNode`, `ProviderBootNode`, and `EngineProcessEdge` declarations carry no `refusedPolarity`. | `CommitRefNode`, `ProviderBootNode`, `EngineProcessEdge` | dashboard/src/types/projection.ts:121-129; dashboard/src/types/projection.ts:162-170; dashboard/src/types/projection.ts:328-333 |
| `LandingRefNode.at?` is distinct from the probe's `observedAt`. | "export interface LandingRefNode {" | dashboard/src/types/projection.ts:233-246 |
| `EngineProcessNode` includes optional `carryoverDoneAt?`. | `EngineProcessNode`, `carryoverDoneAt` | dashboard/src/types/projection.ts:162-202 |
| `ExpectationRowNode` and required `Analytics.expectationRows` form the supervisor expectation surface. | `ExpectationRowNode`, `expectationRows` | dashboard/src/types/projection.ts:94-94; dashboard/src/types/projection.ts:214-225 |
| The Python projection producer defines gate evidence, lifecycle entry time, and expectation rows. | `GateNode`, `LifecycleProjection`, `ExpectationRowNode` | mcp/src/agents_remember/observer/projection.py:76-96; mcp/src/agents_remember/observer/projection.py:99-138; mcp/src/agents_remember/observer/projection.py:422-438 |
| The Python producer defines task sub-task references and task sections. | `TaskSubTaskRefNode`, `TaskSectionNode` | mcp/src/agents_remember/observer/projection.py:575-592; mcp/src/agents_remember/observer/projection.py:595-605 |
| The Python producer defines series sub-tasks and series sections. | `SeriesSubTaskNode`, `SeriesSectionNode` | mcp/src/agents_remember/observer/projection.py:657-672; mcp/src/agents_remember/observer/projection.py:675-682 |
| The Python producer defines engine carryover and analytics expectation projections. | `EngineProcessNode`, `Analytics` | mcp/src/agents_remember/observer/projection.py:832-900; mcp/src/agents_remember/observer/projection.py:956-987 |
| `AgentNotifierHeartbeat` mirrors the app-injected wire shape, not a `projection.py` model. | `AgentNotifierHeartbeat` | dashboard/src/types/projection.ts:54-62 |
| `WorkspaceProjection` is the top-level generated shape. | `WorkspaceProjection` | dashboard/src/types/projection.ts:517-528 |
| The app-side payload builder names the `AgentNotifierHeartbeatPayload` wire shape. | `AgentNotifierHeartbeatPayload` | mcp/src/agents_remember/serving/agent_notifier_heartbeat.py:31-55 |
| The contract guard measures the mirror in three directions and derives `VOCABULARIES`. | `VOCABULARIES` | dashboard/src/test/contract.test.ts:268-293 |

## Series-Contract Notes

`EnclosureNode` separates leaf contract identity (`enclosureId` / `leafId`) from the containing `taskRoot`, which lets dashboard views handle root series tasks and leaf worktrees without deriving paths client-side. 260703-L11 adds the required `codeWorktreeExists` / `memoryWorktreeExists` booleans — the server-stat'ed worktree-existence truth (always on the wire: bool defaults are never `exclude_none`-dropped) that `hasLiveWorktree` filters tasks-surface visibility on, replacing every client-side cleanup-state proxy; `cleanup: reopened` means contract-reset-awaiting-restart, not live work.

## Cross-Repo References

No meaningful cross-repository implementation source governs this repository-local type mirror.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History

- 2026-08-08T22:10+02:00 — 260713-TES-L1 completion round (curator): refreshed this sidecar body for the supervisor -> agent-notifier rename (module paths, identifiers, settings keys, wire keys, prose) and the compat seams; verification metadata pinned until closeout stamps the 260713-TES-L1 commit.
- 2026-08-04T13:01:29+02:00 — 260731-EFA-L6 S18-B04 — same-reviewer semantic correction: reconciled generated projection citations against the frozen source, removed unsupported or duplicate claims, and regenerated scoped citation ranges.

- 2026-08-03T23:26:43+02:00 — 260731-EFA-L6 S18-T3: rewrote the live card for generated
  provenance. Removed the deferred-codegen/`LATE MIRROR` contract, made schema-required fields
  explicit, and stopped attributing historical rationale or diagnostic commentary to generated
  source. New or rewritten source bindings are resolved by the scoped citation fixer.

- 2026-08-01T10:45+02:00 — 260731-EFA-L4 curator: reconciled the state-partition rewrite,
  compile-time uniqueness guard, runtime duplicate coverage, and moved reference ranges against
  the landed source. Corrected stale claims and contradictory counts; verification metadata remains
  pinned until closeout.

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
