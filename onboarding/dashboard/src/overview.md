# dashboard/src/ — Mission-Control Cockpit Frontend Overview

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| sourceRoute            | `dashboard/src/`                                 |
| doc_type               | `route-local-overview`                           |
| lastUpdated | 2026-09-06T21:58:28+00:00 |
| lastVerifiedCommitHash | `ea35964985f30080488270e71ac81657ac40682b` |
| lastVerifiedCommitDate | 2026-09-05T06:48:29+02:00 |
| governingOverview      | `../../overview.md`                              |

## Hot Path Summary

The cockpit composes projected task and lifecycle state, while `data/` owns server transport and stores and `panels/` owns task/artifact views. For CCR, start with `data/taskArtifacts.ts`, the notes/requirements reader discriminator, and the versioned lifecycle projection with its server-owned meaningful revision.

## Governing Overview

[agents-remember root overview](../../overview.md)

## Current Structural Chats Contract

Operations and Chats project the same real sprint/master/leaf task hierarchy. Hosted seats bind by
task-document reference plus role; runtime session ids identify only the current occupant. The rail
keeps one stable row across replacement, while spawn ancestry is available only as a separate
diagnostic projection. Long live labels remain single-line CSS ellipsis.

ARSPAWN-L2 adds optional `dispatchBriefEntryId` to the terminal-catalog row as private diagnostic
evidence that the current generation completed its durable one-call dispatch transaction. The
frontend does not use it as identity or addressing authority. `TaskDocumentRef` is declared locally
in the dashboard contract (it is neither imported nor generated), and the producer/consumer
conformance suite pins the final 66-field catalog projection in both directions.

## L23 Lifecycle Operation Projection

Operations now receives a task-addressed lifecycle-operation projection for closeout and
integration. Hangar and enclosure rows show queued/running/input-required/completed/failed state,
phase, bounded current command, heartbeat age, and guidance without learning a private operation
key or worker PID. Hangar now renders the exact durable command in a one-line ellipsized badge and
keeps the full value in `title`, so viewport pressure cannot create line breaks or require a brittle
character-count cutoff. This is observation only: the dashboard does not become operation authority.

## Purpose

TES-L6 makes sprint provenance a cross-dashboard projection invariant. The data layer preserves
`spawnRepo`/`spawnSprint`, flow models keep equal role names distinct across sprints, and the
session cockpit renders one command group per sprint while isolating unbound legacy rows.

The dashboard frontend is the operator-facing React cockpit. It projects server-composed observer,
task, provider, terminal-catalog, adapter, and control evidence into Operations, Chats, Detail,
Engine Room, file/notes/change-set readers, and supporting panels.

FEUI-L8 deliberately separates strategic ownership:

- [data overview](data/overview.md) — catalog/session state, reliable submit and withdrawal,
  lifecycle cleanup, controls, announcements, and authority boundaries.
- [panels overview](panels/overview.md) — shared panel composition.
- [session-cockpit overview](panels/session-cockpit/overview.md) — the sole full-page Chats product.
- Existing focused child overviews under data, grammar, and panels own their routes. The bounded
  `cockpit/` and `dev/` source slices remain governed here rather than gaining thin overview files.
- [e2e-chats overview](../e2e-chats/overview.md) — the durable, opt-in Chats end-to-end suite
  (260718-CHATS-L5F R7/FB5) is a **sibling** route to `dashboard/src/` (it lives at
  `dashboard/e2e-chats/`, not under `src/`): it boots an isolated real dashboard daemon from the
  worktree and drives the real installed harnesses through this cockpit. Governed by its own route
  overview under the root; linked here for discoverability.

## FEUI-L9R Runtime Truth Repair

Runtime identity crosses this route in three separate ways. The server advertises the fingerprint
of its shipped dashboard while the executing bundle carries its own build-time fingerprint; only a
definite mismatch offers an explicit reload, and absence remains unknown. A new serving boot may
cause exactly one chooser catalog reread and one explicit terminal-socket reattach, but neither is
coupled to SSE loss or a background retry loop. Reattach preserves the mounted xterm and durable
tmux session; transport close alone is not terminal exit.

ARSPAWN-L4 extends that same generated serving-build wire identity with optional Python-source
digest, exact interpreter, and package root. The frontend remains a diagnostic consumer; it gains
no package-update or candidate-selection authority.

## FEUI-MX-FIX-2 Authoritative Session Open

Every browser create entrance now converges on `data/terminalOpen.ts`, the sole client for
`POST /api/terminal`. The opener validates exact request/response identity and accepts only the
server row it returns; raw responses that claim harness/control state are contradictions. The
session store commits and broadcasts only an accepted row, while callers display typed failures and
withhold focus, readiness, submit, and contextual delivery. Request-shaped local rows are not an
alternate success path.

The dev cockpit scenarios replace transport with request-matched raw and harness responses through
the real client seam. They remain fixtures governed by this route overview, not a production
authority — `dev/` remains governed by this overview, including its expanded fixture and probe inventory.

## 260731-EFA-L2 — `dev/` Is A Contract Between Two TypeScript Projects

`dev/` is not only fixtures. `/dev/bench` and `/dev/pty-bench` install probes on `window` so the
Playwright drivers under `e2e/`, `e2e-chats/`, `e2e-production/` and `perf/` can read what the app
actually did — which makes those globals **an interface between two TypeScript programs**: the app
installs them, the drivers read them, and the drivers compile under their own tsconfig project.

`dev/benchProbes.ts` is that interface, declared once. It holds `CockpitBenchProbe`,
`CockpitBenchRequest`, `CockpitBenchTransition`, `CockpitResetAudit`, `PtyFrameStats`,
`PtySerializeProbe` and the `Window` augmentation for `__ptyBench` / `__ptyBenchCols`;
`cockpitScenarios.ts` and `PtyRenderBench.tsx` now import those types rather than each declaring
its own copy. **The module has no imports on purpose** — `tsconfig.driver.json` names it directly,
so the driver program gains the `Window` augmentation without pulling the app's module graph in
behind it. Adding an import to `benchProbes.ts` would drag the app graph into the driver build.

`tsconfig.driver.json` is a new project reference (added to the root `tsconfig.json` alongside
`tsconfig.node.json`) covering `src/dev/benchProbes.ts`, the four e2e/perf suites and the four
Playwright configs under the same `strict` / `noUnusedLocals` / `noUnusedParameters` settings the
app uses. Before it, the driver sources were type-checked by nothing. `tsconfig.node.json` also
picked up `panda.config.ts`, which was likewise unchecked.

The rule this establishes: **a value the browser hands a driver is declared in `benchProbes.ts`.**
Hand-copying a probe field into a spec, or re-declaring `Window`, is how the two halves drift — and
the drift is invisible, because the driver side simply reads `any`.

No production cockpit behaviour, panel, store or authority boundary changed in this leaf.

## 260731-EFA-L4 — Wire Contracts And Typed Vocabularies

This leaf is about what the dashboard's server contract is actually pinned by. Read the first
subsection before writing anything anywhere that cites `fixtures/snapshot.json` or
`types/projection.ts`.

### Generated producer contract, manually sampled fixtures

`dashboard/src/fixtures/snapshot.json` remains a hand-maintained sample. The TypeScript mirror is no
longer hand-maintained: `scripts/sync-projection-types.py` emits the schema artifact and
`types/projection.ts` from `WorkspaceProjection.model_json_schema()` plus the served projection tail,
and its `--check` mode fails drift. The chain therefore separates generated authority from sampled
coverage:

```text
models/projections/workspace.py schema --A--> generated types/projection.ts
                                      ↑ type-checked fixture builders
                                      ↕ measured sample coverage
                               fixtures/snapshot.json
```

- **Producer schema → generated mirror.** Enforced by the projection generator, its Python
  regressions, and `scripts/sync-projection-types.py --check`.
- **Fixture builders against the mirror.** Enforced by `tsc -b`. Every base in
  `test/fixtures/wire.ts` is assembled from `snapshot.json` **and annotated with its mirror type**,
  so it is pinned from both sides: a required field the mirror gains fails to compile until it is
  filled, and it can only be filled from a served row. Call-site overrides go through
  `Overrides<O, Node>` rather than `Partial<Node>`. `test/wireFixtureGuard.test.ts` refuses the
  one-token moves by which a fixture opts out of the mirror altogether.
- **Generated mirror against the sampled payload.** Enforced by `test/contract.test.ts`, and it
  is **not** a one-way containment. Three type-level directions: the mirror declares everything the
  sample carries (`ServedOnlyPaths` fed to `mirrorMustDeclare`, which fails naming the missing
  path); the sample carries everything the mirror declares (`asServedProjection`, whose *parameter*
  type is the check); and the sample **reaches** every path the mirror declares (`fixtureMustSample`
  — the oracle checking itself, because a path the sample never touches, or an empty array, is
  invisible to the other two). Plus runtime `VOCABULARIES` assertions for the closed string unions
  that `resolveJsonModule` widens to `string`, which nothing type-level on this side can see.
The snapshot itself is not generated, so a green sample-coverage test says the manual sample
exercises the generated contract. The generator separately says the TypeScript contract matches the
producer schema. Keep those claims distinct: sample provenance is manual; producer-to-TypeScript
provenance is generated and stale-checked.

### What `wireFixtureGuard.ts` guards, and exactly where its coverage ends

An AST + type-checker sweep over `src/`, `e2e/`, `e2e-production/`, `e2e-chats/` and `perf/`
(`SCANNED_ROOTS`), answering one question: can a test assert against a payload the server could never
send? `tsc` alone cannot, because every opt-out is one token wide (`as Wire`, `as unknown as Wire`,
`as never`, a `@ts-expect-error`, a literal that lost freshness through a variable, `Object.assign`,
`JSON.parse`). Five rules. Rule 1 — an assertion naming a wire type — runs over every scanned file.
Rules 2–5 run over the **fixture surface** only: files ending `.test.ts(x)` / `.spec.ts(x)`, a path
segment named `fixture(s).ts(x)` or a `fixture(s)/` directory, everything under `src/test/` and
`src/dev/`, any top-level directory whose name starts with `e2e`, and `perf/` (`isFixtureSurface`,
which the guard's test pins with worked examples on both sides). Outside that
surface a cast to a wire type is the decode boundary trusting the server, a different and legitimate
act; those sites live in the test's `SANCTIONED_WIRE_SITES` registry with a written reason, counted
exactly and reconciled in both directions (an entry that stops matching fails too).

**How it discovers the vocabulary, and the blind spot that follows.** It holds no list. `isWireModule`
admits a module when its path starts with `src/types/` **or** its first line matches `MIRROR_MARKER`
— `// TypeScript mirror of` or `// Browser mirror of` (`declaresItselfAMirror`). Seven modules carry
the marker today and `wireFixtureGuard.test.ts` pins that exact set, so a mirror that **loses** its
marker fails loudly. The discovery is fail-closed in one direction only: a module that **never**
carried a marker never enters the vocabulary, and the assertion still passes. Live instances, named
in the guard header and in the test's KNOWN GAP note: `data/harnessCatalog.ts`,
`data/submissionLifecycleClient.ts`, `data/changeset.ts`, `data/files.ts`, `data/notes.ts` — API
clients that declare wire-shaped response types inline beside client-side option and handler types.
Fixtures for those routes are unguarded, and both impossible fixtures this leaf deleted (a `control`
field on the harness-catalog row, a `bridgeEpoch` on `WithdrawalResultWire`) lived in that gap.
Widening the rule to "the header cites a `.py` file" was measured and rejected — it sweeps up the
option types too. The fix is to move those response types into a marker-carrying module: app-code
refactor, not fixture work, and not done here.

Four further holes are recorded in the guard's header rather than left to be inferred from a clean
run: rule 4 reads only `Identifier` / `CallExpression` / `PropertyAccessExpression` / object literal,
so `rows[0]`, `await`, `new` and `rows.at(0)!` escape it; one generic helper defeats rules 1 and 4
together; type predicates and assertion functions narrow with no `as` anywhere; and every rule
measures property **names**, so a correct name carrying an explicit `undefined` is invisible to all
five (which is what `test/fixtures/overrides.ts` exists to cover).

### The state vocabulary — generated from the projection schema and stale-checked

`observer/lifecycle_state.py` **composes** the server's `State` from named halves
(`LiveState` / `EndOutcome` → `TerminalState`), and `check_state_partition` refuses at import any
state filed on neither side, so "which states exist" and "which states are terminal" cannot become
two lists that disagree.

`types/projection.ts` now declares the same partition in the same shape: `LIVE_STATES` and
`TERMINAL_STATES` are written out as the two halves, `LIFECYCLE_STATES` is spread from them
(`[...LIVE_STATES, ...TERMINAL_STATES]`), `State` and `ActiveState` are derived, and `ACTIVE_STATES`
is bound to `LIVE_STATES` **directly** rather than as `Exclude<State, TerminalState>` — so the
second list that could disagree is gone on this side too. It replaced exactly the whole-plus-second-
list shape the Python side had stopped having, which `projection.py`'s "STATE OF THE MIRROR" comment
used to name as not done and now records as done.

**Where the two sides differ is what each can REFUSE, and only in the server's favour.** Composition
makes two of `check_state_partition`'s three refusals unrepresentable on either side. The third —
one state filed on BOTH halves — Python refuses at import; TypeScript refuses at compile time, via
`StatesAreFiledOnce = FiledOnce<ActiveState & TerminalState>` with `FiledOnce<S extends never>`, so
`tsc -b` fails naming the offender (`TS2344`). What TypeScript **cannot** refuse is a duplicate
within one half: `Literal["a", "a"]` collapses to one member in Python, while a tuple keeps both, so
`LIVE_STATES = ["running", "running", …]` type-checks clean and is caught only at runtime by
`test/contract.test.ts` (three failures, including "gives each live state a bucket of its own").
Weaker than the server's gate, not absent.

The producer/consumer agreement is now generated rather than maintained as two independent lists.
On producer import, `check_state_partition` refuses invalid state filing and `state_count_fields`
refuses bucket-name collisions. The generator's `_state_partition` then reads the producer `State`
enum and already-validated `Metrics` bucket fields, rejects unmatched mappings, and `_vocabulary_block`
emits the TypeScript partition and enumerable tuples from those schema enums.
`stale_generated_files` compares both committed generated targets with fresh output, so the documented
`scripts/sync-projection-types.py --check` command fails after either a producer-only change or a hand
edit on the TypeScript side, until the artifacts are regenerated cit:(["def check_state_partition(", "def state_count_fields(", "def _state_partition(", "def _vocabulary_block(", "def stale_generated_files("], mcp/src/agents_remember/observer/lifecycle_state.py:74-74; mcp/src/agents_remember/observer/projection.py:267-267; mcp/test_support/agents_remember_test_support/code_quality/projection_types.py:439-439; mcp/test_support/agents_remember_test_support/code_quality/projection_types.py:475-475; mcp/test_support/agents_remember_test_support/code_quality/projection_types.py:602-602).
The separate `contract.test.ts` vocabulary suite still measures whether the manual `snapshot.json`
sample covers every generated member/path and catches a duplicate within one TypeScript tuple; it is
not the cross-language authority.

The sixth state `awaiting-developer` is the notify-and-continue turn end: non-terminal, neither
healthy nor a fault, so every state→colour surface owes it a "your move" treatment rather than a
fall-through to running/ok.

`Metrics` no longer lists buckets. It extends `LifecycleStateCounts`, a mapped type keyed by
`StateCountField<S>` over `ActiveState`, so adding a state adds a **required** field and every object
claiming to be a `Metrics` stops compiling until it counts the new one. That derivation is what the
former hand-written three-bucket list could not do, and why `awaiting-developer` was counted nowhere.
`stateCountField()` is its runtime twin; `metricsFor()` builds the whole rollup from a lifecycle
list, so fixtures state lifecycles instead of re-listing buckets. The camelCase rule is duplicated by
construction (`Camel<>` here, `projection.py::state_count_field` there) and the Python side was moved
to `word[:1].upper() + word[1:]` to agree, because `Capitalize<>` cannot lower-case a tail.

`cockpit/Cockpit.tsx`'s top bar appends a `N awaiting you` segment to the task-metrics chip only
while `metrics.awaitingDeveloperCount > 0` — never a standing `0 awaiting you`, and it does not
displace the running/blocked/tokens rhythm. Before it, the bucket rode the wire and no surface read
it.

Other mirror repairs in the same file: `TaskSubTaskRefNode` and the new `SeriesSubTaskNode` are split
back to one interface per Python model (the collapse had invented a `createdAt` the server never
sends and lent `linkedLifecycleId` to series rows that never carry it); `SeriesSectionNode` gets a
name and a slot while being honest that it is field-identical to `TaskSectionNode` and therefore
structurally interchangeable — it buys a landing place for a future divergence, not a check.
`EngineProcessEdge.refusedPolarity` and its `refused` state are **removed**; the renderer derives
flash polarity from `state`. `ATTENTION_SEVERITIES`, `ATTENTION_LANES`, `PROCESS_FACT_STATES` and
`PROCESS_HEALTHS` became tuples with derived types, because runtime membership checks need
enumerable values. Schema generation now emits `GateNode.evidenceRefs`,
`LifecycleProjection.stateEnteredAt`, and `Analytics.expectationRows` as required fields, matching
their producer schemas rather than preserving the former optional client-tolerance gap.

### Totality replaces defaults in `topology/`

`topology/model.ts` replaced an if-chain ending in `return "ok"` with
`CONSTEL_STATUS_BY_STATE: Record<State, ConstelStatus>` — total by type, so a seventh state stops
that object literal compiling. `CONSTEL_STATUSES` is the tuple `ConstelStatus` derives from, and `UNCLASSIFIED_STATUS` is
the declared answer (`"warn"`) for a state from a newer server.

The subtle part is `STATUS_BY_DECLARED_STATE`, a `Partial<Record<string, ConstelStatus>>` **read
view** over the same table. Indexing `Record<State, …>` directly types the miss away — `tsc` hands
back `ConstelStatus`, never `undefined` — which would make `?? UNCLASSIFIED_STATUS` in
`lifecycleStatus()` read as deletable dead code. The read view is what makes that fallback
load-bearing: delete the `??` and `tsc -b` fails at that line. Remove the alias instead and the
compiler goes quiet while an unclassified state's `undefined` flows onward.
`noUncheckedIndexedAccess` would say the same thing project-wide; it is not on (measured: 601 errors
across 81 files).

`topology/constel.ts` closed the other half of the same defect: the palette was
`Record<string, string>` read through `COLORS[status] ?? COLORS.ok`, so an unclassified state came
out cyan — the healthy fill. It is now `constelColors(cssVar): Record<ConstelStatus, string>`,
extracted out of `mountConstel` so `constel.test.ts` can prove totality without a canvas, with **no**
fallback at the lookup because that key really is a value this package produced.

### Fixture ergonomics: the two type-level devices worth knowing

- `test/servedProjection.ts` — `resolveJsonModule` widens every literal in the payload (`"running"`
  becomes `string`, `3` becomes `number`), so `snapshot.json` can never be *assigned* to a mirror
  that types its vocabularies as literal unions. The old reflex was a double cast
  (`snapshot as unknown as WorkspaceProjection`), which turned off assignability and
  excess-property checking together.
  `AsJsonModule<T>` applies exactly the import's widening to the mirror and nothing else, so
  `asServedProjection()` is a full structural check of everything widening does not touch. Every
  test reading `snapshot.json` must come through it; a second `as unknown as` elsewhere silently
  re-opens the hole for that file.
- `test/fixtures/overrides.ts` — `Overrides<O, T>` replaces `Partial<T>` in the builders because
  `exactOptionalPropertyTypes` is **not set** on this project, so a `Partial<T>` slot admits an
  explicit `undefined` and `lifecycle({ state: undefined })` compiles a required field into absence
  with no cast for the guard to find. `Overrides` binds at the call site, in whichever tsconfig
  project the caller sits in. Its limits are stated in its own header: the override must stay a
  fresh literal, it reaches one level deep, and it binds only `fixtures/wire.ts` and
  `fixtures/conversationWire.ts`. Turning the flag on project-wide was measured at 222 errors across
  71 files and deliberately not attempted here.
- `dev/fixtures.ts` now delegates every node builder to `test/fixtures/wire.ts` and derives `metrics`
  through `metricsFor()`; the gallery keeps its own display defaults by passing them explicitly, and
  no longer keeps a second copy of the required-field list. `dev/cockpitScenarios.ts`'s
  `/api/harnesses` stub uses `satisfies HarnessInfo[]` precisely because `data/harnessCatalog.ts` is
  one of the unmarked modules the guard cannot see. `dev/` remains fixtures, not a production
  authority.

### Checking this route

`dashboard/tsconfig.json` is a **solution-style** config (`"files": []` plus three project
references). `tsc --noEmit` there compiles nothing and exits 0 vacuously — it is evidence of nothing.
The real gate is `npm run typecheck` (`tsc -b`), which is what every "stops compiling" claim above
means. Most of this leaf's guarantees are type-level and free at runtime, so a green `vitest run`
alone does not exercise them.

## Layered Architecture

1. Projection types are generated and stale-checked from the server's Pydantic schema; the separate
   hand-maintained snapshot is measured for fixture coverage.
2. Data modules normalize, reconcile, and retain browser projection state around explicit server
   authorities.
3. Grammar primitives provide shared state words, badges, panels, and markdown treatment.
4. Panels compose focused operator surfaces over the shared stores.
5. CockpitShell owns navigation, persistent keep-alive layers, selection routing, and shell-wide
   drivers.

The terminal catalog and adapter/control routes remain authoritative. Browser state may cache and
project them, but is not a replacement conversation-history database.

## Route Model

### Operations

Operations remains the initial destination. Its task list, detail reader, attention, diagnostics,
and contextual RailChat retain their existing contracts. RailChat is useful task-local context, not
a second full-page chat destination.

### Chats

FEUI-L8 removes the legacy Chats/SessionList path and the separate Sessions navigation concept.
CockpitShell exposes one Chats item backed by the persistent session-cockpit layer. That layer keeps
the mechanics built through L1–L7 — role/spawn rail, reliable composer and authoritative pop-back,
interaction answers, lifecycle controls, evidence/capabilities/bus, and status — while adding L8
hardening, accessibility, scenarios, and product-duty transfer.

Since 260718-CHATS-L4 the controlled-session stage body is the structured `ConversationSurface`, not
a PTY: `ChatsStageBody` selects the structured surface (default), the in-stage history library, or
the legacy-raw PTY, and owns the default-off read-only terminal-diagnostics drawer. The exact-turn
interrupt is wired into the WorkingLine as the `conversation.stop` chord. The inspector is
supplementary evidence, closed by default, toggleable, and responsive without overwriting deliberate
user intent. The stage is the primary space.

### Other Full-Page Surfaces

Detail/Operations takeovers, Engine Room, File Viewer, Notes Reader, Change-Set Viewer, and dev-only
design/bench routes retain their existing focused overviews. The L8 split does not introduce another
production view.

## Product Truth And Conversation Boundary (structured renderer landed in 260718-CHATS-L4)

The canonical Chats stage now renders the **structured conversation surface** for controlled
sessions: a harness-neutral grammar over a reconstructable browser projection of the landed L1/L2/L3
adapter-normalized contracts. The controlled runner line-log survives only as the default-off
read-only terminal-diagnostics drawer; legacy raw sessions still host the vendor TUI. This is the one
shared visual message roof across Claude, Codex, and Pi, with visible harness identity and
capability reasons.

The two capabilities are both served and stay distinct: the **active transcript**
([data/conversation](data/conversation/overview.md) + the `conversation/` grammar) and the
**previous-conversation library/index** ([data/conversation-library](data/conversation-library/overview.md) +
the `conversation-library/` browser). Both obtain normalized history/index/resume from the server
contracts and hold only a projection/cache — no durable browser conversation database (R1). UA-1 is
no longer absent. Two forward constraints remain L5 hardening: interrupt capability gating is
attempt-and-reflect on the L3 evidence until a control-capabilities GET or L1-view refresh lands, and
the measured virtualization/scale baseline plus the E1/E2 environmental faults are enumerated in the
`conversation/` L5-Facing Register.

Harness sub-agents are now a first-class additive layer on both capabilities. The active-transcript
data plane carries per-item agent refs (evidence-bound identity, absent on parent items) and keeps
the operator's agent-lane focus outside the projection so it survives LRU eviction and is
re-validated against the live roster. The library groups sub-agent conversations as child rows
under their parent and renders the server's verbatim `agentsNote` when agent history is (partially)
unavailable. Pending interactions are multiplexed: an additive plural wire slot carries sub-agent
approvals alongside the parent's singular slot, and every attention surface — rail badge,
announcer, seat visual grammar, and the palette's question triage — derives from the combined set
via one shared predicate, so a seat blocked solely on a sub-agent approval never goes dark; the
adapter-bound agent label names who is asking, never a fabricated name.

User submissions, agent-to-agent bus messages, lifecycle/control commands, and adapter-interaction
answers remain distinct paths. The original orchestration failure mode was collisions caused by
routing agent communication through the same paste/input channel as operator typing; the dashboard
must not recreate that coupling.

## Invariants And Boundaries

- Operations is the default and there is exactly one full-page Chats destination.
- The shell owns one catalog poll/reconciler for its lifetime. Views do not create competing feeds.
- Focus/inspection may name a landed row; only a live row owns action routing and reload preference.
- Reliable submit and withdrawal preserve request/epoch identity and never blind-resend or locally
  fake an authoritative result.
- Session open is accepted-response-authoritative: failed requests cause no registry row, focus
  movement, readiness transition, or dependent delivery.
- PTYs stay mounted across focus and transient handoff gaps; ended rows never create a live socket.
- Inspector visibility is optional presentation. Core Chats actions remain usable with it closed.
- State words and evidence remain explicit; absent transport/capability/history facts are not
  inferred.
- No Domain Documentation source is configured; direct source/tests, reviewed task evidence, and
  recovered same-repository history are the authority for FEUI-L8 curation.

## Child Route Onboarding Map

| Child route | Governing overview |
| --- | --- |
| `data/` | [Cockpit state and authority](data/overview.md) |
| `panels/` | [Panel composition](panels/overview.md) |
| `grammar/` | [Grammar](grammar/overview.md) |
| `cockpit/` | File cards governed by this overview; shell ownership starts at [Cockpit.tsx](cockpit/Cockpit.tsx.md). |
| `dev/` | File cards governed by this overview; dev scenario authority starts at [cockpitScenarios.ts](dev/cockpitScenarios.ts.md). |
| root ambient types | [vite-env.d.ts](vite-env.d.ts.md) declares the dashboard build fingerprint consumed by the data layer. |

## Docs References

The curator checked `system/sources.md`; it contains no configured Domain Documentation entries.
The L8 architecture statements were verified from repository-local source/tests, task/reports, and
the recovered same-repository history pack.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant domain documentation was found for `dashboard/src`. | — | — |

## Cross-Repo References

No cross-repository implementation is imported as the dashboard authority. Historical Toad/T3
references informed product framing only; current code truth stays in agents-remember.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository implementation source governs this route. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Shell navigation, default, persistent layers, and shared drivers. | `CockpitShell` | dashboard/src/cockpit/Cockpit.tsx:385-666; dashboard/src/cockpit/Cockpit.tsx:850-850 |
| State and authority architecture. | `# dashboard/src/data/ — Cockpit State And Authority Overview` | onboarding/dashboard/src/data/overview.md:1-405 |
| Panel composition. | `# dashboard/src/panels/ — Cockpit Panels Overview` | onboarding/dashboard/src/panels/overview.md:1-745 |
| Sole Chats route, deletion map, and future boundary. | `# dashboard/src/panels/session-cockpit/ — Canonical Chats Cockpit Overview` | onboarding/dashboard/src/panels/session-cockpit/overview.md:1-506 |
| Dev scenario authority and end-to-end states. | `COCKPIT_SCENARIOS` | dashboard/src/dev/cockpitScenarios.ts:108-205 |
| Fixture-honesty sweep, its five rules, its scanned roots, and the unmarked-module blind spot. | "five rules"; `SCANNED_ROOTS`; "no dashboard test asserts against a payload the server cannot produce" | dashboard/src/test/wireFixtureGuard.ts:1-63; dashboard/src/test/wireFixtureGuard.ts:136-136; dashboard/src/test/wireFixtureGuard.test.ts:266-467 |
| State/phase/severity vocabularies and the derived `Metrics` bucket fields. | `Metrics` | dashboard/src/types/projection.ts:459-475 |
| Total state-to-status and status-to-colour grammars; the load-bearing unclassified fallback. | `UNCLASSIFIED_STATUS`; `constelColors` | dashboard/src/topology/model.ts:68-68; dashboard/src/topology/constel.ts:31-39 |
| JSON-module widening and the override type that survives `exactOptionalPropertyTypes` being off. | `AsJsonModule`; `Overrides` | dashboard/src/test/servedProjection.ts:22-32; dashboard/src/test/fixtures/overrides.ts:60-66 |

## 260718-CHATS-L5I Current Route Impact

The cockpit now treats a focused chat or terminal as a persistent operator surface rather than disposable tab content: switch and hidden-view transitions preserve mounted identity, scroll/selection/geometry state, and only resume visible-only work when appropriate. Its global data consumers also adopt bounded stream/watchdog, single-flight, timeout, build-identity, and wake-lock behavior. Detailed mechanics remain owned by the existing `data/`, `panels/`, and nested session-cockpit overviews; this route records only the shared frontend consequence.

Selection-driven panels also preserve stable external-store snapshot identity when no task-document
projection exists. In particular, `HighlightComposer` uses one shared empty task-document value
rather than allocating an empty array during every snapshot read, preventing a React
`useSyncExternalStore` render loop without changing selection or injection authority.

## 260727-CHATS-IM-L2 No Route-Level Architecture Impact

This leaf changes internals inside existing children: roster identity in `data/conversation/`,
selected-child projection in `panels/session-cockpit/conversation/`, and effect isolation in
`panels/engine-room/`. The dashboard source layering and ownership model described here are
unchanged.

## 260731-EFA-L7 — Conversation-Timeline Wiring

The dashboard route absorbed the L7 live-thinking change on top of the L8 split: the conversation-timeline family now renders one coalesced live `thinking` indicator per active turn (`collapse.ts` stable-row refactor + `ThinkingItem` animated indicator), with acceptance pins in `liveThinking.test.tsx` and `collapse.test.ts`. No dashboard file is over the file-size hard limit; the detector's `dashboard/src` TS/TSX scope is enforced by the project wrapper.

### 260713-TES-L5 Route Impact — Regenerated Projection Schema

The 260713-TES-L5 change set regenerated `dashboard/src/types/projection.schema.json`: the
`AgentPickupNode.description` now surfaces "pending / not yet landed" (N16 turn-boundary
landing; `operator_inbox_consume` attribution-only; sweep predicates never read the
projection).

## L23 Lineage Visibility

The dashboard consumes strict source-lineage projection types, schema, and
fixtures from the server contract. Engine Room shows the aggregate admission
state and full summary; it does not compare branches or choose a sync locally.

## 260815-DAG-L4 L4 Projection Contract

The dashboard projection adds the organizational `super-to-leaf` lineage relation and remains generated from the server schema. Organizational direct-super and atomic super-to-master-to-leaf topology therefore use one closed, parity-tested wire vocabulary.

## 260815-DAG-L14 Dashboard Route

The task-document projection types carry sprint structure: `TaskDocNode.seats` (`TaskSeatNode`)
and optional `TaskSubTaskRefNode.masterRef`; the detail panel threads `docPathForRef` so sprint
rows open their commanded master document.


## 260815-DAG-L12 Route Impact

The sprint execution graph is viewable when present: `types/projection.ts` (+ schema) carry the render-ready `TaskExecutionGraphView`/`TaskExecutionNodeView`/`TaskExecutionPredecessorNode` wire shapes and optional `TaskDocNode.executionGraphView`; `panels/sprint-graph/` is the wave-grid view route; `dev/DevApp.tsx` exposes `/dev/sprint-graph` for mounted-UI evidence; and `fixtures/snapshot.json` exercises the node vocabularies (L12-R1/R2/R4-R7). The sprint-scoped closeout projection is mounted independently, so a valid graph-less atomic-sequential sprint retains scheduling visibility.

## 260821-CLIVE Disposable Scheduling And Discard Audit

The generated projection now exposes closeout scheduling as disposable exact-current state:
service/source condition, bounded source problems with repair actions, and generation-keyed members
with producer-owned classification, priority, order, and reasons. The dashboard renders this view
without owning claims, lifecycle, commit, certification, recovery, or terminal evidence.

Task projections also retain audited discard-before-start history. Detail surfaces show the discarded
identity, reason, timestamp, and proof separately; Operations appends a distinct discarded count to
live progress. A discarded item never increments completion. The JSON Schema remains runtime
authority for numeric, string, fingerprint, and collection refinements; generated TypeScript carries
deterministic refinement documentation rather than pretending those constraints are structural types.


## 260815-DAG Master Full-Gate Repair Route Impact

`fixtures/snapshot.json` extended with a super-to-leaf source-relation entry and two execution-graph view nodes (segment + lump with frontier states) for dashboard vocabulary coverage.

## 260824-PDLS Final Projection Reconciliation

The generated dashboard contract removes the impossible `not-created` invalidation outcome and
the contract suite now forces parity with the producer's always-materialized invalid-empty state.
This keeps the browser on the projection plane: file absence never becomes queue or lifecycle
authority.

## Python 3.13 Generated-Schema Representation

The canonical schema now represents named attention and process `Literal` vocabularies as local
`$defs` enums referenced by their model properties. Their values and the generated TypeScript
surface are unchanged; the dashboard remains a consumer of one server-owned generated contract.

## 260831-CCR-L23 Notes Takeover Widen

The cockpit takeover now distinguishes the artifact kind it opens: the notes reader view marker is
`notes-reader` for a notes target and `requirements-reader` for a task-local requirement
packet, with the shared `TaskArtifactReaderTarget` imported from `data/taskArtifacts.ts`.
Route-shape, takeovers, and layer retention are unchanged; detail lives in the Cockpit.tsx sidecar.

## CCR-R18@v1 Lifecycle Envelope Mirror

260831-CCR-L18 regenerated the lifecycle-operation projection surface consumed by the dashboard: `types/projection.ts` and `types/projection.schema.json` now carry `schemaVersion`/`stateMatrixVersion`, the `incoherent` status, and the identity/componentBindings/worker/approval/recommendedAction envelope cells; `fixtures/snapshot.json` gained the matching fixture samples; `test/contract.test.ts` registers the new signature site and vocabularies. File-level detail lives in the route sidecars.

## Lifecycle Wait Cursor Mirror

`types/projection.ts` carries optional `meaningfulRevision` and `taskIntent` in the versioned lifecycle
operation envelope. The revision is a server-owned observation cursor and the intent is a canonical task digest; neither is a browser-produced activity
counter. `fixtures/snapshot.json` includes the matching sample alongside the coherent projection
fields; the task-artifact takeover remains independently discriminated by notes/requirements.

| Finding | Anchor | Source |
| --- | --- | --- |
| The generated lifecycle mirror carries the cursor beside coherent identity and version fields. | "export interface LifecycleOperationProjection {" | dashboard/src/types/projection.ts:335-360 |
| The fixture supplies a meaningful revision for the sample operation. | "\"meaningfulRevision\": 1," | dashboard/src/fixtures/snapshot.json:1225-1225 |


## Integrated IAS Recovery Contract

The generated lifecycle phase union and schema now include `recovering-private-preparation`. This is a server-owned recovery state projected through the existing lifecycle view; it adds no frontend command or recovery authority. Keep the schema and TypeScript mirror generated from the same producer.

## Update History

- 2026-09-06T21:58:28+00:00 — Reconciled this route against the source delta from `245057ab16e19afdaabd5c188c9576b22e0c0870` to `d36109038b3f2b500c138f9dc1ea9c9f9a247489`. Updated current ownership and policy claims; prior verification commit/date and history remain unchanged. Source inspection only; no test, review or acceptance claim.




- 2026-09-05T07:24+00:00 — L31 cumulative source review at `ea35964985f30080488270e71ac81657ac40682b`: Removed stale dev-file census, corrected schema owner and added normative intent to the current lifecycle mirror account. Verification records source review, not execution or acceptance.
- 2026-09-05T06:12+00:00 — Composed retained CCR route contributions without replacing sibling knowledge; preserved prior source-verification metadata and historical entries.

- 2026-09-04T20:19:44+02:00 — 260831-CCR-L15 Gate-5 memory pass for e375f2ebdc87f6843bc76168b646d606fa79caec: types coverage refreshes the generated `LifecycleOperationProjection` wire mirror with the optional `meaningfulRevision` cursor (interface, schema, fixture sample); route index regenerated.


- 2026-09-04T10:05+02:00 — 260831-CCR-L18 Gate-5 route impact: recorded the regenerated lifecycle operation envelope mirror, fixture samples, and contract vocabulary registrations. File-level detail in the dashboard/src sidecars.


- 2026-09-04T01:06+02:00 — 260831-CCR-L23 Gate-5 route impact: recorded the notes-takeover kind distinction (notes vs requirements reader) in the cockpit shell route.


- 2026-08-30T15:15:36+02:00 — ARSPAWN-L4 route impact: regenerated the diagnostic serving-build
  mirror with exact Python candidate provenance. Verification remains closeout-owned.

- 2026-08-29T19:04+02:00 — Reconciled the Python 3.13 named-literal `$defs` representation without
  changing the dashboard wire vocabulary or frontend ownership. Verification remains closeout-owned.

- 2026-08-26T12:30+02:00 — 260821-ARSPAWN-L2 final curation: recorded the dashboard-local
  `TaskDocumentRef` declaration and final 66-field producer/consumer parity while keeping the brief
  receipt diagnostic-only. No test execution is claimed.

- 2026-08-26T12:30+02:00 — 260821-ARSPAWN-L2 route impact: the terminal-catalog projection accepts
  the private pinned-brief receipt without changing the task-document-plus-role chat identity.
  Verification remains closeout-owned.

- 2026-08-26T10:44:52+02:00 — No route impact: refreshed exact projection-schema and generated-mirror citation anchors after source movement; the dashboard source-layer architecture is unchanged.

- 2026-08-25T17:21+02:00 — Reconciled the final invalidation outcome and contract-forcing change.
  Verification remains closeout-owned.

- 2026-08-24T15:04+02:00 — Added the final CLIVE disposable scheduling and discard-audit route
  contract, corrected graph-less queue visibility, and retained the newer root-journal lifecycle
  operation projection boundary.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair route impact: the snapshot fixture gained a super-to-leaf relation entry and two execution-graph view nodes. Verified at code commit e5cb139f.



- 2026-08-20T10:45+02:00 — 260815-DAG-L12:   L12 render-ready sprint graph view types, the new sprint-graph panel route, the dev evidence surface, and the fixture vocabulary. Verified at code commit b7f2c8e2.

- 2026-08-20T05:06+02:00 — 260815-DAG-L14 route impact: the dashboard task projection gains
  `seats` + typed `masterRef`; detail-panel rows open the commanded master directly. Verified at
  code commit 8071a644.


- 2026-08-18T13:00+02:00 — No route impact: 260815-DAG-L8 added the closeout-queue projection surface; route purpose unchanged.

- 2026-08-15T23:38+02:00 — 260815-DAG-L4: reconciled this governing route with the frozen integration-authority implementation and forcing surface. Verification remains closeout-owned.

- 2026-08-15T02:16:50+02:00 — 260815-DAG-L1 route impact: generated dashboard projection types and
  fixtures now expose explicit master nature, the persisted reasoned sprint graph, and derived waves.
  This leaf adds visibility contracts only; it does not yet add queue or graph UI judgment.

- 2026-08-14T06:25+02:00 — L23 final candidate review: the dev scenario server now models accepted
  interaction consumption/replay/attention behavior and uses the shared fleet task-document fixture;
  cockpit route ownership is unchanged. Verification provenance remains closeout-owned.

- 2026-08-13T12:26+02:00 — L23 live-progress clarification: recorded the Hangar rendering of the
  already-durable lifecycle command as a responsive one-line ellipsized projection with full title,
  without adding operation authority or identity to the frontend. Verification provenance remains
  closeout-owned.
- 2026-08-13T07:53+02:00 — 260731-EFA-L23 super-line reconciliation: re-reviewed this card and its Repo-Internal citation targets after absorbing the super-integration memory line. Retained claims remain supported by the current tree. Verification is pinned to real code HEAD `1580f92715ff93c988f9a15439ad9bec60ef4c5d`; the new-line memory mapping remains closeout-owned.
- 2026-08-12T20:20+02:00 — L23 curator: documented dashboard ownership of read-only lineage visibility and contract parity; verification remains closeout-owned.
- 2026-08-12T15:19+02:00 — L23 curator: added the task-addressed lifecycle-operation status projection used by Hangar and enclosure rows; verification provenance remains closeout-owned.

- 2026-08-12T04:15+02:00 — 260731-EFA-L22 dashboard repair: recorded the route-wide consequence
  of stable empty external-store snapshots in selection-driven panels; child panel cards own the
  exact regression and implementation.

- 2026-08-11T19:58+02:00 — 260731-EFA-L19 curator: reconciled the dashboard route with
  plane-owned seat routing, document-addressed role control, and the corresponding projection and
  cockpit changes; detailed evidence remains in the affected child-route cards.

- 2026-08-10T04:39+02:00 — 260713-TES-L6: recorded the dashboard-wide sprint-provenance projection
  invariant. Verification metadata remains pinned until closeout.

- 2026-08-09T22:22+02:00 — No route impact: the master integration repair changes only
  scroll-memory test timer hygiene under the existing conversation-timeline route. Dashboard
  runtime behavior and source layout are unchanged.

- 2026-08-09T13:59+02:00 — 260713-TES-L5 route impact: recorded the regenerated projection
  schema (`AgentPickupNode` landing semantics; attribution-only consume). Verification
  metadata pinned until closeout stamps the 260713-TES-L5 commit.
- 2026-08-08T21:20+02:00 — 260713-TES-L1 route impact: the top-bar badge and store field were
  renamed to `AgentNotifierHeartbeatBadge` / `agentNotifierHeartbeat` with
  `agent-notifier ok/stale` wording and `data-testid="agent-notifier-heartbeat"`; the store
  accepts the legacy `supervisorHeartbeat` wire key as a fallback during the rename window.
  Per-file detail lives in the `Cockpit.tsx` and `data/store.ts` sidecars. Verification metadata
  pinned until closeout stamps the 260713-TES-L1 commit.

- 2026-08-07T23:35:00+02:00 — 260731-EFA-L7 route impact (trace delta): recorded the live-thinking wiring and the file-size scope for `dashboard/src`. Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: added the Frontend Rail section for this route. Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-04T18:00+02:00 — 260731-EFA-L6 S18-B17 curator: resolved the S18-T3 leftover `:1-1`
  placeholders and the malformed route rows. The projection-provenance prose cit and table row now
  carry exact frozen-source ranges for all nine anchors (`check_state_partition`,
  `state_count_fields`, `workspace_projection_schema`, `_state_partition`, `_vocabulary_block`,
  `stale_generated_files`, the codegen staleness test, and the two fixture-comment literals — the
  wire.ts anchor re-spelled to the verbatim "BE PRECISE ABOUT WHAT PINS WHAT"); the seven remaining
  route rows gained anchors and plain path:line-line sources (three sibling overview cards cited as
  `onboarding/...` with their `#` heading anchors); the L4 history entry's superseded parenthesized
  L59/L72 spellings were rewritten as cit forms against the regenerated `types/projection.ts` lines
  13 and 21. No claim wording changed.
- 2026-08-03T23:26:43+02:00 — 260731-EFA-L6 S18-T3: replaced the obsolete four-node/no-generator
  account with the current split: Pydantic schema → generated/stale-checked TypeScript mirror, plus
  independently measured manual sample coverage. New ranges are explicit `:1-1` curator input.

- 2026-08-01T10:50+02:00 — 260731-EFA-L4 curator, **fixture-provenance label repair**. The chain
  bullets said `fixture ⊆ mirror` — enforced / `mirror ⊆ server` — enforced by nothing, and the
  first bullet's *body* then correctly described three directions including the opposite
  containment. Everything after the label was right; the label is the part that travels, and three
  other cards copied the two-set shorthand and lost the middle link entirely. The chain is now
  stated as **four nodes and three links** (`test/fixtures/wire.ts` →A→ `types/projection.ts` →B→
  `fixtures/snapshot.json` →C→ `observer/projection.py`) with one bullet per link, each labelled by
  its two endpoint files rather than by a set relation: A enforced by `tsc -b` (mirror-annotated
  bases, `Overrides<O, Node>`, `wireFixtureGuard.test.ts`), B enforced by `contract.test.ts` in
  three type-level directions (`ServedOnlyPaths`/`mirrorMustDeclare`, `asServedProjection`,
  `fixtureMustSample`) plus runtime `VOCABULARIES`, C enforced by nothing. Added the one-letter
  trap explicitly: `mirror ⊆ served` **is** enforced (by `asServedProjection`) while
  `mirror ⊆ server` is not. Restated the no-generator negative at the strength the evidence
  supports — seven files reference `snapshot.json` and all seven are readers, no script writes it,
  `package.json`'s `codegen` is `panda codegen`, neither dependency set carries a schema-to-type
  tool — which establishes **no in-repo generator and no in-repo mechanism keeping the two sides in
  step** and cannot exclude a generator outside this repository. Re-pointed the Repo-Internal
  References row and the state-vocabulary section's closing line from `mirror ⊆ server` to link C,
  and added there that nothing enforces the two partitions' agreement in either direction. Marked
  the two clauses in the 09:33 entry that the post-wave source change falsified (the two-set
  shorthand; "the TypeScript side did **not** adopt the partition") in place rather than rewriting
  them, so the historical record stands and the false reading cannot be picked up by grep. The
  partition body itself had already been corrected by the 10:45 entry below; independently
  re-verified here — double-filing `"completed"` onto `LIVE_STATES` fails with
  `error TS2344: Type '"completed"' does not satisfy the constraint 'never'`, a duplicate *within*
  one half compiles clean (exit 0), and that duplicate then fails three assertions in
  `contract.test.ts` (3 failed / 12 passed). Verification metadata pinned until closeout.
- 2026-08-01T10:45+02:00 — 260731-EFA-L4 curator (post-wave source change), **one corrected section
  only**: `types/projection.ts` adopted the server's partition after the 09:33 entry below was
  written, so "The state vocabulary — parallel to the server, not tied to it, and not the same
  shape" was describing a file that no longer exists. It said the mirror declares `LIFECYCLE_STATES`
  as one tuple of six with `TERMINAL_STATES` as a second tuple beside it and `ActiveState` as the
  subtraction `Exclude<State, TerminalState>`; verified against the current file, the halves are
  written out first (`LIVE_STATES` L42, `TERMINAL_STATES` L48), `LIFECYCLE_STATES` is spread from
  them cit:([`LIFECYCLE_STATES`], dashboard/src/types/projection.ts:13-13), and `ACTIVE_STATES = LIVE_STATES` cit:([`ACTIVE_STATES`], dashboard/src/types/projection.ts:21-21) with no subtraction anywhere. The heading and
  the paragraph were corrected, and the section now states the ONE asymmetry that survives, because
  "same shape" on its own would overclaim: TypeScript refuses double-filing at compile time
  (`StatesAreFiledOnce`, verified by mutation to fail with `TS2344`) but cannot refuse a duplicate
  within one half, which `Literal` collapses and a tuple does not — `contract.test.ts` catches that
  at runtime with three failing tests. The 09:33 entry below records the pre-change reading and is
  left as written. Nothing else on this route was touched.
- 2026-08-01T09:33+02:00 — 260731-EFA-L4 (wire contracts and typed vocabularies; 22 governed files
  under `dashboard/src/`, nine of them new): added the `260731-EFA-L4` body section and amended
  Layered Architecture point 1. The load-bearing addition is a provenance statement this card had
  never made in any form: `fixtures/snapshot.json` is **hand-maintained** and no generator exists
  (verified by search — nothing under `mcp/`, `scripts/` or `dashboard/`, and no `package.json`
  script, writes it; no Python source or test reads it or the mirror — `projection.py` and
  `test_observer_projection.py` only *describe* the mirror in comments and docstrings), so
  `fixture ⊆ mirror` is
  enforced by `test/wireFixtureGuard.test.ts` + `test/contract.test.ts` while `mirror ⊆ server` is
  enforced by nothing and codegen is what would close it.
  **[Corrected 2026-08-01T10:50 — two things. That two-set shorthand is what this entry got wrong,
  and it is what three other cards copied: it reads as one link where the chain has three, and
  `contract.test.ts` is a link of its own (link B), not a co-enforcer of the first. And read "no
  generator exists" above as "no generator exists *in this repository*" — the search is exhaustive
  over this tree and cannot speak to anything outside it. See the body section, which now names the
  four nodes, all three links, and the exact strength of the negative.]** Also recorded, each with the mechanism
  that breaks if it is undone: what `wireFixtureGuard.ts` scans (`SCANNED_ROOTS`), the fixture
  surface rules 2–5 are confined to, the `SANCTIONED_WIRE_SITES` registry, and the precise coverage
  boundary — `isWireModule` discovers the vocabulary from a `// TypeScript mirror of` /
  `// Browser mirror of` first line, which is fail-closed only against a mirror that *loses* its
  marker, so the five unmarked `data/` API clients (`harnessCatalog`, `submissionLifecycleClient`,
  `changeset`, `files`, `notes`) are a real, reproduced blind spot; the sixth `awaiting-developer`
  state, and the fact — checked against `projection.py`'s own "STATE OF THE MIRROR" comment — that
  the TypeScript side did **not** adopt the server's new partition shape but keeps
  `LIFECYCLE_STATES` and a separate `TERMINAL_STATES` that can silently disagree
  **[NO LONGER TRUE — a worker landed the partition in `types/projection.ts` after this entry was
  written; `projection.py`'s "STATE OF THE MIRROR" comment was updated with it and now records the
  mirror as holding the same partition in the same shape. Read the body section, not this clause.]**;
  `Metrics extends
  LifecycleStateCounts` deriving one required bucket per `ActiveState` (plus `stateCountField()` /
  `metricsFor()`); the `TaskSubTaskRefNode` / `SeriesSubTaskNode` split, the new `SeriesSectionNode`,
  the removal of `EngineProcessEdge.refusedPolarity`, the tuple-derived attention/process
  vocabularies, and the three `LATE MIRROR` fields; `topology/` totality
  (`CONSTEL_STATUS_BY_STATE: Record<State, ConstelStatus>`, `UNCLASSIFIED_STATUS`, the
  `STATUS_BY_DECLARED_STATE` read view that makes `?? UNCLASSIFIED_STATUS` load-bearing to `tsc -b`,
  and `constelColors()` replacing `COLORS[status] ?? COLORS.ok`); the conditional `awaiting you`
  top-bar segment in `cockpit/Cockpit.tsx`; `asServedProjection()` and `Overrides<O, T>` with the
  measured reason `exactOptionalPropertyTypes` stays off; and the checking note that this project's
  solution-style `tsconfig.json` makes `tsc --noEmit` vacuous, so `tsc -b` is the only real
  typecheck. Per-file detail belongs to the file cards under `test/`, `topology/`, `types/`,
  `cockpit/` and `dev/`; `data/`, `panels/`, `grammar/` and `fixtures/snapshot.json` are owned by
  their own cards and are referenced here only where the architecture requires it. Verification
  metadata pinned until closeout stamps the L4 commit.
- 2026-07-31T00:00+02:00 — 260731-EFA-L2: no production cockpit change. `dev/` gained
  `benchProbes.ts`, the single declaration of the browser→driver probe contract (and the `Window`
  augmentation), deliberately import-free so the new `tsconfig.driver.json` project can name it
  without pulling in the app module graph; `cockpitScenarios.ts` and `PtyRenderBench.tsx` import
  those types instead of duplicating them. The e2e/perf suites and Playwright configs are now
  type-checked at all, as is `panda.config.ts`. Corrected the stale "two files" claim about `dev/`.
  Verification metadata pinned until closeout stamps the L2 commit.
- 2026-07-30T12:51+02:00 — No route-level architecture change for
  260727-CHATS-IM-L2. Roster identity narrowing is owned by `data/conversation/`; the sparse
  Engine Room effects overlay is owned by `panels/engine-room/`; structured child-history
  selection remains in `panels/session-cockpit/conversation/`. Verification metadata remains
  pinned until closeout.

- 2026-07-26T18:30+02:00 — 260718-CHATS-L7 curator: added one paragraph to the Product Truth And
  Conversation Boundary section covering the sub-agent surface — additive per-item agent refs and
  the LRU-surviving agent-lane focus in the conversation data plane, library child rows plus the
  verbatim `agentsNote`, and multiplexed pending interactions feeding all attention chrome through
  one shared predicate with the adapter-bound agent label. No route composition or authority model
  changed; detail lives in the `data/` and `panels/session-cockpit/` child overviews. Verification
  metadata remains pre-commit; closeout re-stamps.

- 2026-07-24T13:18:47Z — 260718-CHATS-L5I curator: updated the shared dashboard/src route for the whole frontend change without modifying nested overview ownership. Verification metadata remains pre-commit.

- 2026-07-21T11:30+02:00 — 260718-CHATS-L5F curator: added a discoverability pointer to the new
  sibling [e2e-chats overview](../e2e-chats/overview.md) — the durable, opt-in Chats E2E suite
  (R7/FB5) that boots an isolated real dashboard daemon from the worktree and drives the real
  installed harnesses through this cockpit. The suite lives at `dashboard/e2e-chats/` (a sibling of
  `src/`, governed by its own route overview under the root); the `dashboard/src/` route model is
  otherwise unchanged. Verification metadata pinned; the L5F change is uncommitted and closeout
  re-stamps.
- 2026-07-21T05:30+02:00 — No route impact: the `dashboard/src` route model
  (`cockpit/`/`grammar/`/`panels/`/`data/`) is unchanged by 260718-CHATS-L5P (cockpit chrome visual
  polish, PASS-WITH-NOTES; dashboard-only, zero backend edits). The two app-wide `dashboard/src/`-direct
  CSS/token changes are captured at the child/sidecar level, not in this route body (which has no styling
  section): (1) `index.css` gained an unlayered `word-break: normal` root override on `html, body,
  [data-view="sessions"]` that neutralizes `@webtui/css`'s inherited `word-break: break-all` app-wide
  (RV-1, LOAD-BEARING — a third-party scoped reset in a lower layer silently defeated every
  component-level `overflow-wrap` patch; the test is computed-value verification; raw-id spans keep
  explicit `break-all`) — recorded in the `index.css` sidecar and the `panels/session-cockpit/` overview's
  "Cockpit chrome conventions" section; (2) `styles/tokens.css` + `panda.config.ts` gained the `well`
  (`#070b0f`) terminal-well token (the xterm pty inset, FB7.1) — recorded in the `tokens.css` sidecar. The
  regenerated `package_data/dashboard/` bundle is shipped output governed by the mcp overview's sync
  mechanism, not an mcp source contract. Verification metadata unchanged.
- 2026-07-20T22:30+02:00 — 260718-CHATS-L4 route impact (structured Chats renderer; reviewer FINAL
  PASS, 26/26 findings closed): `data/` gains the reconstructable `conversation/` and
  `conversation-library/` projection child routes; `panels/session-cockpit/` gains `ChatsStageBody`
  and the `conversation/` + `conversation-library/` grandchild renderer routes (structured
  `ConversationSurface` is the controlled-session default; the runner line-log is demoted to the
  default-off read-only terminal-diagnostics drawer + legacy-raw body; the exact-turn interrupt rides
  the WorkingLine as the `conversation.stop` chord). Rewrote the Product-Truth/Conversation-Boundary
  and Chats sections: UA-1 history/index/resume is now landed as a reconstructable projection with no
  durable browser conversation index. Additive edits also touched `SessionsView`/`WorkingLine`/
  `ChatContextBar`/`PtySurface`/`SessionComposer`/`data/keymap` (detail in those sidecars). The
  synchronized `package_data/dashboard/` bundle is regenerated shipped output governed by the mcp
  overview's sync mechanism, not an mcp source contract. Verification metadata remains pinned pending
  L4 candidate closeout.

- 2026-07-18T15:22+02:00 — FEUI-MX-FIX-2: recorded the sole authoritative browser opener,
  accepted-server-row-only materialization, contradiction handling, and request-matched dev fixture
  seam; corrected route ownership so bounded cockpit/dev files remain governed here. Verification
  metadata remains pinned pending candidate closeout.

- 2026-07-18T12:43+02:00 — FEUI-L9R: added bundle comparison, bounded boot-owned reread/reattach,
  explicit reload, and durable-session transport boundaries. Verification metadata remains pinned
  pending candidate closeout.

- 2026-07-18T07:22+02:00 — 260715-FEUI-L8 strategic refactor: split data authority and canonical
  Chats detail into focused child overviews, recorded one Chats/Operations-default product truth,
  and preserved the future adapter-normalized conversation/history boundary without claiming UA-1.
  Metadata remains pinned to the leaf base.

- 2026-07-17T23:54+02:00 — 260715-FEUI-L7 route impact: the existing
  `panels/session-cockpit/` child route gains the stable-mounted three-pane inspector, complete
  evidence/capability/Bus surfaces, sender-only reverse reply, shared accessible virtualization,
  and honest StatusLine; `types/projection.ts` gains optional pickup owner/redelivery facts and
  `test/fixtures/busScenarios.ts` adds coherent/legacy wire cases. Detailed organization remains
  in the focused child overview rather than further loading this packed root file. Verification
  metadata remains pinned to the leaf base until closeout.
- 2026-07-17T21:39+02:00 — 260715-FEUI-L5 curator: replaced stub/paste current-state claims with
  the shared CodeMirror reliable-submit path, central evidence fold, epoch/request transport,
  authoritative status/withdraw/pop-back, revision-safe recovery, and bounded retention. Recorded
  `dashboard/src/data` route pressure for the final master route-architecture pass rather than
  inventing a non-mirrored route during this leaf.
- 2026-07-17T08:33+02:00 — 260715-FEUI-L4 route impact (live set controls; final reviewer PASS
  after three fix rounds): `data/` gains the exact-session capability, five-state acceptance,
  serialized pair, sole I/O driver, chip/copy, and announcer modules; the cockpit store gains
  typed snapshot/echo/route/pair evidence; `panels/session-cockpit/` gains the live control,
  accepting chip, ledger/rail attention, persistent background toasts, queued hint, and dual live
  regions; capability fixtures gain clamp/queue/unknown readback sequences. Six nonblocking sev-4
  observations remain preserved in file cards. Verification metadata is pinned to the contract
  base until code commit.
- 2026-07-17T06:25+02:00 — 260715-FEUI-L3 route impact (capability catalog client and launch
  flow; review FINAL PASS after two fix rounds; 66 files / 753 tests green): `data/` gains the
  launch layer — `capabilityCatalog.ts` (memory-only envelope store, drop-on-error, verbatim
  errors, honest refresh semantics), `launchEvidence.ts` (the pure tier machine; Claude launch
  pairs never readback), `launchFlow.ts` (pure launch machines + the classifying open client),
  all + suites; `types/` gains `harnessCapabilities.ts` + `terminalOpen.ts` (the capability and
  open wire mirrors; `terminalCatalog.ts` untouched); `grammar/` gains `EvidenceBadge.tsx`
  (+ test); `test/fixtures/` gains the R3 contract pack (`capabilityEnvelopes`,
  `controlMessages`, `openResponses`) + `test/contractCapabilities.test.ts`;
  `panels/session-cockpit/` gains `LaunchFlow` + `FailedLaunchBanner` and derives the R7
  evidence tier from control-state truth (see that overview); `data/terminal.ts` extends the
  open POST with the model/effort selection. Upstream ask: an operator retire actor identity if
  provenance-recording retire is wanted from the dashboard. Verification metadata pinned to the
  leaf base until closeout stamps the L3 code commit.
- 2026-07-17T04:20+02:00 — 260715-FEUI-L6 route impact (PTY stage surface, structured
  interactions, session lifecycle actions; review FINAL PASS after a 1×sev-3 + 5×sev-4 fix
  round, all CLOSED): `data/` gains the interaction/lifecycle layer — `interactionAnswer.ts`
  (the SOLE gate-channel answer path), `sessionLifecycle.ts` (detailed terminate/cleanup +
  residual notice store + the focus-independent retire-residual sweep), `ptyHarvest.ts`
  (client-side legacy-raw OSC/bell/title harvesting), all + suites; `actions.ts` gains
  `postGateDecisionDetailed`, `terminal.ts` the additive `onSocketState`;
  `panels/session-cockpit/` gains PtySurface/InteractionBar/WorkingLine/StopResidualNotes/
  lifecycleCopy (see that overview); `panels/Terminal.tsx` gains additive optional props (DOM
  default, lazy webgl escalation, live screenReaderMode, harvesting hooks, named `role="group"`
  landmark); `test/fixtures/catalogRows.ts` appends the `L6_*` rows (FLEET byte-identical);
  `dev/` gains `/dev/pty-bench` (`PtyRenderBench.tsx` + `lineLogFixture.ts`; driver at
  `dashboard/e2e/ptyRenderBench.mjs`). Two exact-pinned deps entered `package.json`:
  `@xterm/addon-webgl` (lazy escalation chunk, loaded only if the renderer constant flips) and
  `@xterm/addon-serialize` (bench probe only — evaluated cheap-enough, deliberately NOT adopted
  in product code until an LRU cap or the pane-freeze repaint package defines the discipline).
  Verification metadata pinned to the leaf base until closeout stamps the L6 code commit.
- 2026-07-17T02:30+02:00 — 260715-FEUI-L2 route impact (session data layer, rail, and stage
  container; review FINAL PASS): `data/` gains the sessions-cockpit data layer —
  `catalogPoll.ts` (the poll driver hoisted OUT of Chats; Chats is now a consumer),
  `seatEvents.ts` (the gated `/api/events` seat reconciler; poll stays authoritative),
  `stateGrammar.ts` (the one dot grammar + 2.4 s pulse ruling), `railModel.ts` (the ruled
  hierarchy/attention/joins), `sessionCockpitStore.ts` (per-seat honesty-invariant client state),
  all + suites; `types/` gains `terminalCatalog.ts` (the full catalog wire mirror,
  `data/terminal.ts` re-exports); `test/fixtures/` is the new shared-fixture home
  (`catalogRows.ts`); `panels/session-cockpit/` gains the rail/stage/inspector components (see
  that overview); `sessions.ts`/`stream.ts`/`commands.ts`/`index.css` extended as their sidecars
  describe; plus a reviewer-accepted one-line defensive fix in `panels/file-viewer/FileViewer.tsx`.
  Open sev-3 developer ruling: status-chip vocabulary width (`stale`/`exited`/`retired`/
  `starting`). Verification metadata pinned to the leaf base until closeout stamps the L2 code
  commit.
- 2026-07-17T00:30+02:00 — 260715-FEUI-L1 route impact (view shell, WebTUI spike, keyboard/palette
  foundation): the cascade gained the `webtui` layer slot (S1, OQ-D = adopt — `styles/webtui.css`
  is the one mapping file, build-time scoped under `[data-view="sessions"]`, spike assertions kept
  in `test/webtuiSpike.test.ts`); `cockpit/Cockpit.tsx` registered the full-bleed keep-alive
  **Sessions** view; `panels/` gained the **`session-cockpit/`** child route and `data/` gained
  `commands.ts`, `sessionLayout.ts`, and the **`keymap/`** child route (the PTY reserved set with
  the R6 chord replacement Ctrl+Alt+[ / ] → Ctrl+Alt+PageUp/PageDown and five-source verification
  records); `styles/tokens.css` gained `--muted`. Four exact-pinned deps entered `package.json`
  (`@webtui/css@0.1.9`, `cmdk@1.1.1`, `tinykeys@4.0.0`, dev `postcss-prefix-selector@2.1.1`).
  Detail lives in the `panels/session-cockpit/` + `data/keymap/` overviews and the touched
  sidecars. Verification metadata pinned to the task base until closeout stamps the L1 code
  commit.
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: reviewed route impact for the accepted hosted cutover.
- 2026-07-12T18:00+02:00 — 260712-TRH-L7: paired the landing-freshness body update with this history entry; projection landing refs remain visible and age-labeled when stale, while Engine Room motion is limited to observed refs and remote observation stays server-side.

- 2026-07-12T16:45+02:00 — 260712-TRH-L1 reopened-memory refresh: clarified stable path/revision
  request identity, separate body storage plus current-summary merge, late-response discard,
  terminal failure semantics, composition regression coverage, and the pre-existing scalar
  staleness window. Verification metadata remains blank until closeout stamps the code commit.

- 2026-07-12T13:36+02:00 — No route impact: 260712-TRH-L2 body review confirms the changeset refinements remain inside the existing `data/changeset` and `panels/changeset` surfaces; the `dashboard/src` route model and top-level organization are unchanged. Verification metadata remains pinned until closeout.
- 2026-07-12T12:55+02:00 — No additional route impact from 260712-TRH-L2: its changeset refinements stay inside the existing `data/changeset` and `panels/changeset` surfaces; the dashboard/src route model and top-level organization remain unchanged. Verification metadata pinned until closeout stamps the L2 code commit.
- 2026-07-12T12:07+02:00 — 260712-TRH-L1 dashboard-source route impact: added the focused
  `data/useTaskDocumentBody.ts` state seam and documented complete visible task content as the first
  reader request priority. Notes and change-set counters resume after success or fallback; no new
  frontend route was created. Verification metadata remains pinned until closeout.

- 2026-07-10T21:59+02:00 — 260707-HFX2-L21 dashboard-source route impact: documented the
  persisted, bounded Chats sidebar and its pointer/keyboard separator. The behavior stays inside the
  existing `panels/` route and preserves terminal working width without animating direct manipulation.
  Verification metadata remains pinned until closeout.

- 2026-07-10T15:07+02:00 — 260707-HFX2-L17 dashboard-source route impact: documented explicit
  role claim, binding-first client identity, pair-scoped assignment/rendering, and the
  source/build/serve package boundary. Verification metadata remains pinned until closeout.

- 2026-07-10T13:41+02:00 — 260707-HFX2-L16 route impact: documented repo-qualified sprint
  grouping, complete spawn-edge forest rendering, bounded/hover-complete rail rows, honest on-demand
  task-body fallback, and single-rendered implementation steps. No new route was created.
  Verification metadata stays pinned until closeout stamps the eventual L16 code commit.

- 2026-07-10T01:14+02:00 — 260707-HFX2-L13 F6 route impact: added the on-demand task-document data
  adapter and `bodyRevision` wire field; full reader bodies no longer ride the always-on projection.
  Verification metadata remains pinned until closeout stamps the eventual L13 code commit.

- 2026-07-09T14:05+02:00 — No route impact: 260707-HFX2-L11 (landed chat archive + group cleanup)
  extends `data/{sessionGroups,sessions,terminal}.ts` (new `"landed"` status, landing provenance
  fields, `cleanupLandedTerminalSessions()`) and `panels/{Chats,SessionList,Terminal}.tsx` (landed
  archive group, group-cleanup control, read-only landed terminals). This is data-shape and panel
  behavior content, not a change to this route's own module layout or routing; per-file detail lives
  in the already-updated `dashboard/src/data/` and `dashboard/src/panels/` sidecars/sub-overview.
  Verification metadata pinned until closeout stamps the 260707-HFX2-L11 commit.
- 2026-07-08T23:59+02:00 — 260707-HFX2-L8 route impact (dead-seat storm observability, R6):
  `SupervisorHeartbeat` now includes pending/redeliverable inbox backlog counts and last sweep
  duration; `data/store.ts` compares those fields in `heartbeatEquals`; and
  `cockpit/Cockpit.tsx` renders them in the top-bar `SupervisorHeartbeatBadge` beside heartbeat age.
  Verified with dashboard typecheck and `src/data/store.test.ts`. Verification metadata pinned until
  closeout stamps the 260707-HFX2-L8 commit.
- 2026-07-08T18:45+02:00 — 260707-HFX2-L2 route impact (supervisor sweep, R5): `cockpit/Cockpit.tsx`
  gains `SupervisorHeartbeatBadge` in the `TopBar` (beside `ServingBuildStamp`); `data/store.ts`
  gains the `supervisorHeartbeat` field, deliberately excluded from the change-gate `unchanged`
  check so the live tick age still applies on a content-unchanged reconnect; `types/projection.ts`
  gains the `SupervisorHeartbeat` type and optional `WorkspaceProjection.supervisorHeartbeat?` — a
  second app-injected, non-`projection.py` field alongside `servingBuild?`. No route/component-tree
  shape change beyond the one new top-bar badge. **Known limitation (builder-flagged, unverified
  in this environment):** these TS changes are unverified by `tsc`/a build (no `dashboard/
  node_modules` installed); a follow-up should run the dashboard's own build/test suite once
  available. Verification metadata pinned until closeout stamps the 260707-HFX2-L2 commit.
- 2026-07-07T23:55+02:00 — 260707-HFX-L6 route impact: the `data/sessionGroups`
  model and terminal data mirror now include architect/curator role provenance so Chats grouping and
  row chips can represent the split developer-facing architect, backend orchestrator, and curator
  closeout seat without changing the cockpit route structure. Verification metadata pinned until
  closeout stamps the HFX-L6 commit.
- 2026-07-07T14:00+02:00 — agent-orchestration L17 route impact: `panels/` gains the **`notes-reader/`**
  child route (the Notes Reader takeover, reusing the File Viewer `DualPane` over the unchanged L9
  `/api/notes/*` API), and `cockpit/Cockpit.tsx` gains a second full-bleed takeover hosting it (retained
  mounted-hidden after Back so selection survives back/forward). `panels/TaskNotes.tsx` becomes the compact
  entry surface (inline reader retired) and `panels/LifecycleList.tsx`'s gate chip drops the wait-loop `ask`
  fallback. Details in the `panels/` + `panels/notes-reader/` overviews and the touched sidecars.
  Verification metadata pinned until closeout stamps the L17 commit.
- 2026-07-07T05:38+02:00 — 260703-L15 route impact (long-session memory): `data/` gains
  `servedAges.ts` (+ suite; the volatile-age mirror, stable equality, arrival anchors, display
  ticker); `store.ts` apply paths became identity-preserving/change-gated (zero writes on idle
  payloads) and carry `servingBuild`; `types/projection.ts` mirrors the app-injected
  `ServingBuild`; `cockpit/Cockpit.tsx` renders the muted serving-build stamp; the four
  age-display panels advance served ages locally. NOTE: `data/` has no route overview of its own —
  this file governs it directly, so the genuine body update lives here (same call as L14).
  Verification metadata pinned until closeout stamps the L15 commit.
- 2026-07-06T23:57:36+02:00 — 260703-L14 route impact (visual hierarchy + chat grouping): `data/` gains
  `sessionGroups.ts` (+ unit suite, the G1 command-tree derivation) and `taskHierarchy.ts` gains the
  orchestration-command helpers; `grammar/` gains `RankBadge.tsx` (+ test, the V4 chevron insignia);
  `types/projection.ts` mirrors `TaskDocNode.orchestrates?`; `styles/tokens.css` gains the six
  gold/purple tier vars (mirrored as Panda tokens in `panda.config.ts`). Behavior detail lives in the
  `panels/`/`grammar/` overviews and the changed sidecars. Verification metadata pinned until closeout stamps the L14 commit.
- 2026-07-06T15:40+02:00 — No route impact: 260703-L12's dashboard change is content-only inside `panels/` — `flowModels.ts` gains the STRATEGIST model (8-model census) and loop-doctrine lines, `FlowTab.test.tsx` grows to 11 cases; the dashboard/src route model, data layer, and grammar this overview describes are unchanged — detail lives in the `panels/` overview and the two file sidecars. Verification metadata pinned until closeout stamps the L12 commit.
- 2026-07-06T12:10+02:00 — No route impact: 260703-L10's dashboard change is a single phase-label string inside `panels/flowModels.ts` (designer `frame` → `reframe`); the dashboard/src route model, data layer, and grammar this overview describes are unchanged — detail lives in the `panels/` overview and the `flowModels.ts` sidecar. Verification metadata pinned until closeout stamps the L10 commit.
- 2026-07-06T03:25+02:00 — 260703-L11 route impact: `data/selectors.ts` gains the shared
  `hasLiveWorktree` tasks-surface visibility rule and `types/projection.ts` mirrors the new required
  `EnclosureNode.codeWorktreeExists`/`memoryWorktreeExists` flags; `dev/fixtures.ts` and the
  `topology`/`panels` test fixtures default them `true`. The Hangar/LifecycleList behavior change is
  documented at the panels route. Verification metadata pinned until closeout stamps the L11 commit.
- 2026-07-06T03:00+02:00 — 260703-L9 route impact (friction F-M): `data/` gains `notes.ts` (+ unit
  suite), the third serving read client — `listNotes`/`readNote` over the shared `getJson`/`qs`
  transport plus the pure `resolveNoteReference` — feeding the new task-reader notes view
  (`panels/TaskNotes.tsx`); the `data/` route-model bullet now names it beside `files.ts` and
  `changeset.ts`. Verification metadata pinned until closeout stamps the L9 commit.
- 2026-07-05T19:55+02:00 — No route impact: the dashboard/src route model is unchanged — the cycle-7 manager-raise-node enclosure addition is documented at the panels route (260703-L8 cycle 7).
- 2026-07-05T19:10+02:00 — No route impact: the dashboard/src route model is unchanged — the cycle-6 seam-node prose update is documented at the panels route (260703-L8 cycle 6).
- 2026-07-05T18:24+02:00 — No route impact: dev-only index label aligned with the converged canvas (DevApp.tsx); no production route or component change (260703-L8 cycle 5).
- 2026-07-05T16:32+02:00 — No route impact: the dashboard/src route model is unchanged — the FlowTab redraw is documented at the panels route (260703-L8 cycle 4).
- 2026-07-04T12:31+02:00 - L3 route impact: dashboard data/types now mirror
  agent-to-agent inbox metadata and hosted-delivery state for `AgentPickupNode`
  and `/api/operator-inbox`. Verification metadata pinned until closeout stamps
  the L3 commit.
- 2026-07-04T10:05+02:00 — 260703-L0 route impact (small): `dev/` gained the `/dev/flows` lifecycle-design
  canvas route (DevApp mounts the generalized `panels/FlowTab` over the new `panels/flowModels.ts` registry);
  detail lives in the `panels/` overview and the file sidecars. Verification metadata pinned until closeout
  stamps the L0 commit.
- 2026-07-03T00:35+02:00 — L11 route impact: reopened leaves render as planned doc rows via the stable leaf id; abandoned enclosures leave the active operations rows (see panels/LifecycleList).
- 2026-07-02T20:15+02:00 — L8 route impact (small): `data/selection.ts` selections now carry the
  qualified `leafKey` when anchored inside a task reader marked `data-task-leaf-key`, and
  `cockpit/Cockpit.tsx` threads `viewedLeafKey` + `leafChatActive` into `HighlightComposer` so the
  direct leaf-chat paste path can resolve its target. The route structure is otherwise unchanged;
  behavior detail lives in the `panels/` overview and file sidecars. Verification metadata pinned until
  closeout stamps the L8 commit.
- 2026-07-02T17:04+02:00 — No route impact: L9 extends the existing `data/sessions.ts` and
  `panels/Chats.tsx` / `RailChat.tsx` routes so hosted chats can move between durable leaves after
  creation, and open dashboard tabs rehydrate `"leaf"` catalog invalidations or polling refreshes. The
  `dashboard/src/` route model is unchanged; detail lives in the `panels/` overview and changed sidecars.
  Verification metadata pinned until closeout stamps the L9 commit.
- 2026-07-02T16:35+02:00 — No route impact: the reopened-L6 wheel/paste fixes stay inside `panels/` and
  `data/`. `panels/Terminal.tsx` yields wheel to xterm mouse reporting when the app tracks the mouse;
  `data/terminal.ts` gained `pasteAndConfirm` (echo-confirmed, boot-deadline-retried draft paste) and
  `data/sessions.ts`'s `pasteDraftToSession` delegates to it. The `dashboard/src/` route model is
  unchanged. Verification metadata pinned until closeout stamps the follow-up commit.
- 2026-07-02T15:03+02:00 — No route impact: the L6 alternate-buffer wheel follow-up stays inside the
  existing shared `Terminal` wrapper under `panels/`. Normal-buffer scrollback still uses xterm viewport
  scrolling, while alternate-buffer hosted agent TUIs receive PageUp/PageDown wheel steps instead of
  xterm Up/Down history input. The `dashboard/src/` route model is unchanged. Verification metadata
  pinned until closeout stamps the follow-up commit.
- 2026-07-02T13:16+02:00 — Reopened L6 route impact/no route impact: the follow-up stays inside the
  existing `cockpit/` + `panels/` + `data/` model, but `data/sessions.ts` now separates leaf-context
  draft paste from submit so `RailChat` can place context in the selected hosted chat without pressing
  Enter. Chat scrollback remains documented in the `panels/` overview and `Terminal.tsx` sidecar. The
  `dashboard/src/` route model is unchanged; verification metadata pinned until closeout stamps the L6
  follow-up commit.
- 2026-07-01T01:19+02:00 — No route impact: L6 adds bind-time leaf context handoff inside the existing
  `cockpit/` + `panels/` + `data/` model. `CockpitShell` passes `analytics.engineProcesses` to the existing
  right-rail `RailChat`, and `RailChat` injects a projected leaf context package when a chat is started on a
  displayed leaf or a free chat is successfully attached. The `dashboard/src/` route model is unchanged;
  detail lives in the `panels/` overview and the `Cockpit.tsx`/`RailChat.tsx`/`RailChat.test.tsx` sidecars.
  Verification metadata pinned until closeout stamps the L6 commit.
- 2026-06-30T00:00:00+02:00 — No route impact: L5 (Sidebar chat) adds leaf-keyed attachment + a right-rail River⇄Chat
  toggle. The change lives in `cockpit/Cockpit.tsx` (a `railView` toggle + `selectedLeafKey` derivation),
  `data/` (`sessions.ts` leaf binding, `terminal.ts` `attach-leaf` client, `taskIdentity.ts` leaf-key
  helpers), and `panels/` (the new `RailChat.tsx`, plus `Chats.tsx`/`SessionList.tsx` leaf-attach + name
  label) — all within the already-documented `panels/` route. The `dashboard/src/` route model
  (`cockpit/`/`grammar/`/`panels/`/`data/`/`dev/`) is unchanged; detail lives in the `panels/` overview
  and the `cockpit/`/`data/`/`panels/` file sidecars. Verification metadata pinned until closeout stamps
  the L5 commit.
- 2026-06-29T23:00+02:00 — No route impact: L4a refines the already-documented `panels/changeset/`
  sub-route (leaf committed/working change-set views, a diff-highlight rectangle, a live working-view
  auto-refresh), adds the doc-reader change-set bars in `panels/DetailPanel.tsx` + leaf helpers in
  `data/changeset.ts`, and changes `cockpit/Cockpit.tsx` so the change-set takeover overlays (rather than
  replaces) the railed body so the back link returns to the leaf it was opened from. The `dashboard/src/`
  route model (`cockpit/`/`grammar/`/`panels/`/`data/`/`dev/`) is unchanged; detail lives in the `panels/`
  + `panels/changeset/` overviews and the `Cockpit.tsx`/file sidecars. Verification metadata pinned until
  closeout stamps the L4a commit.
- 2026-06-29T17:00+02:00 — No route impact: the L4 follow-up refines the already-documented `panels/changeset/` sub-route — the series/master change-set is now the NET inspectable diff (was accumulated-only) — plus shared code-view polish (`codemirrorTheme` comment/punctuation readability, `DiffPane` split-diff scroll). The `dashboard/src/` route model (`cockpit/`/`grammar/`/`panels/`/`data/`/`dev/`) is unchanged; detail lives in the `panels/changeset/` overview + the file sidecars. Verification metadata pinned until closeout stamps the L4 follow-up commit.
- 2026-06-29T16:40+02:00 — Operations Integration L4 (Change-Set Viewer) route impact: `cockpit/Cockpit.tsx`
  gained a `changeSet` **TAKEOVER** (a `DetailPanel` change-set button replaces the railed Operations body
  with a full-bleed `<ChangeSetViewer>`; a back link restores it); a new **`panels/changeset/`** sub-route
  lands — the Change-Set Viewer screen (a read-only `@codemirror/merge` diff over the L3 `/api/changeset/*`
  API, reusing the L2 `FilePane`); and `data/` gains the `changeset.ts` serving client (sharing `files.ts`'s
  `getJson`/`qs`/`FilesApiError`). Detail in the `panels/` + new `panels/changeset/` overviews and sidecars.
  Verification metadata pinned to the task base until closeout stamps the L4 code commit.
- 2026-06-29T09:06+02:00 — Operations Integration L2 (File Viewer) route impact: `cockpit/Cockpit.tsx`
  registers a new full-bleed **File Viewer** view (`"files"` in the `View` union + the `fullBleed` set, a
  `VIEWS` tab between Operations and Engine Room), **kept mounted** (CSS-hidden) like Chats so its
  repo/scope/open-file/tree state survives a tab switch; and a new **`panels/file-viewer/`** sub-route
  lands — a read-only code+onboarding dual-pane (two Headless Tree explorers, a read-only CodeMirror 6
  pane, bidirectional code↔onboarding pairing) that is the first consumer of the L1 read-only files API,
  plus the reusable `FilePane`/`DualPane` for the L4 Change-Set Viewer. Detail in the `panels/` + new
  `panels/file-viewer/` overviews and sidecars. Verification metadata pinned until closeout stamps the L2
  code commit.
- 2026-06-28T16:17+02:00 — Task 35 route impact: `panels/LifecycleList.tsx` reopen-task nesting — the
  Operations list admits a reopened leaf's suffixed enclosure by shared lifecycle + suffixed-leaf shape and
  nests doc-less enclosure-backed runtime rows under their master, ending the standalone-phantom row. No
  other `dashboard/src` route structure changed. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-28T13:54+02:00 — Task 34 route impact: the raw Event River store (`data/store.ts`) now keeps a
  bounded **sliding window** of the newest ~2000 rows (memory-bounded rather than the unbounded
  session-growth the prior text described), which `EventRiver` virtualizes over so there is still no hard
  display cap. Refreshed the `data/` Route Model bullet's event-store description. Verification metadata
  pinned until closeout stamps the task-34 code commit.
- 2026-06-28T07:45+02:00 — Task 33 route impact: the `topology/` view became an active-enclosure constellation
  (lifecycle/task rim removed, each enclosure folds in its 1:1 lifecycle, `activeTopologyInputs` filters to
  the served active set, basename `groupKey` join fixes the latent task-12-S1 provider join); `types/projection.ts`
  mirrors the new required `activeWorktreeGroups`, and `data/store.ts` + `data/stream.ts` thread it through.
  Verification metadata pinned until closeout stamps the code commit.
- 2026-06-28T07:43+02:00 — Task 29 S7 route impact: the cockpit now hides the former Lifecycle Flow
  tab, the raw Event River waits for the backend `ready` event before rendering an empty history, and
  frontend storage no longer truncates received Event River rows. Attention queue dismiss/clear actions
  optimistically suppress visible rows while the backend physically removes or acknowledges the source,
  including targetless actionable-drift notices. Verification metadata pinned until closeout stamps the
  task-29 code commit.
- 2026-06-28T03:21+02:00 — Task 31 route impact: projection types now mirror the provider boot-node
  `missing` state, letting Engine Room render expected-but-absent provider roles distinctly from
  configured/observed provider rows. Operations task grouping also accepts the authored task-document id
  when matching a leaf document to its enclosure, so leaf 31 stays nested under the browser-dashboard
  master even when the task JSON file stem is descriptive. Verification metadata pinned until closeout
  stamps the task-31 code commit.
- 2026-06-27T18:43+02:00 — Task 26 route impact: `cockpit/Cockpit.tsx` registers a new full-bleed
  **Lifecycle Flow** view — `"flow"` in the `View` union + the `fullBleed` set, a `VIEWS` tab second
  after Operations, and a `ViewBody` case rendering `<FlowTab />` from `panels/FlowTab.tsx`. FlowTab is
  a /dev-stage diagnostic visualizing the build-job lifecycle (the task-27 next-step engine spec); the
  production bundle was not rebuilt this task. Verification metadata pinned until closeout stamps the
  task-26 code commit.
- 2026-06-27T03:04+02:00 — Task 22 follow-up: `data/sessions.ts` removed the hidden-label reservation
  state with the Hide UI path, and terminal catalog create/terminate broadcasts now carry the changed
  `sessionId` so other tabs can remove ended rows deterministically.
- 2026-06-27T01:25+02:00 — Task 22 follow-up: `data/sessions.ts` now broadcasts backend-persisted
  terminal catalog create/terminate invalidations across browser tabs, while `data/terminal.ts` exposes a
  nullable catalog fetch so receivers can distinguish empty success from fetch failure.
- 2026-06-27T01:03+02:00 — Task 22 follow-up: `data/sessions.ts` now allocates session labels from the
  lowest available live per-prefix ordinal, then releases End/terminated labels.
- 2026-06-27T00:25+02:00 — Task 22 follow-up: the Chats view now mounts restored sessions on first
  selection and keeps visited terminals mounted while hidden, avoiding broken hidden xterm hydration for
  restored Claude/Codex sessions after refresh without losing tab-switch buffers.
- 2026-06-26T23:15+02:00 — Task 22 route impact: the Chats data/panel route now hydrates
  dashboard-owned terminal sessions from `/api/terminal/sessions`, tracks running/exited/terminated
  catalog status, restores the last active session, and routes explicit End through backend terminate.
  Verification metadata pinned until closeout stamps the code commit.
- 2026-06-26T20:18+02:00 — Task 21 route impact: frontend projection types mirror
  `SeriesNode.seriesTokenTotal`, and DetailPanel master readers display the server-composed aggregate.
  Verification metadata pinned until closeout stamps the code commit.
- 2026-06-26T19:40+02:00 — Task 20 reopened route impact: `data/taskIdentity.ts`
  now participates in Event River lifecycle-label fallback by exposing direct
  task-document title labels for lifecycle-only history rows. Detailed behavior
  lives in the data helper and panel formatter sidecars. Verification metadata
  pinned until closeout stamps the reopened task-20 code commit.
- 2026-06-26T18:23+02:00 — No route impact: task 20 adds Event River readable-feed
  formatting inside `dashboard/src/panels/` (`EventRiver.tsx`, `eventSummary.ts`, and tests). The
  `dashboard/src/` route model remains cockpit/grammar/panels/data/dev; detailed behavior lives in
  the panels overview and file sidecars. Verification metadata pinned until closeout stamps the code
  commit.
- 2026-06-25T14:02+02:00 — Task 24 reopened: frontend data/panels now support gate-id-only Clear for stale gate rows while keeping normal decisions lifecycle-targeted.
- 2026-06-25T13:20+02:00 — Task 23/24: frontend route now includes gate dismissal, attention clear, inbox-warning deletion, and `AgentPickupNode` projection types.
- 2026-06-25T07:26+02:00 — Task 19 gate interaction polish: `dashboard/src/` now treats Gate Respond as
  three explicit paths — Yes/No record targeted durable gate decisions through `data/actions`, while Chat
  remains message-only through hosted chat or the operator inbox. The data route also adds
  `actions.test.ts` coverage. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-24T18:11+02:00 — Task 17 route correction: `TaskDocNode.id` is now mirrored in the projection
  types and used by `data/taskHierarchy.ts`, `LifecycleList`, and `DetailPanel` as the authored leaf
  display number; parent sub-task `number` remains fallback data. Verification metadata pinned until
  closeout stamps the code commit.
- 2026-06-24T18:02+02:00 — Task 17 route correction: `data/taskHierarchy.ts`, `LifecycleList`, and
  `DetailPanel` now use structured task metadata for visible leaf labels while keeping creation
  metadata as the ordering source. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-24T17:51+02:00 — Task 17 Operations hierarchy route update: added `data/taskHierarchy.ts` as
  the shared structured parent-series helper behind BY REPO leaf indentation and direct leaf parent
  backlinks. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-24T16:39+02:00 — Task 17 Operations route correction: dashboard selection is now typed
  (`taskdoc:` / `series:` / `lifecycle:`), task documents can be listed/read before lifecycle binding,
  and projection types mirror optional `TaskDocNode.lifecycleId`. Detail lives in `data/taskIdentity.ts`,
  `LifecycleList.tsx`, `DetailPanel.tsx`, and `types/projection.ts` sidecars. Verification metadata
  pinned until closeout stamps the code commit.
- 2026-06-24T12:21+02:00 — Task 17 route impact: projection types now mirror task/series
  `createdAt`, `SeriesNode`, and `Analytics.series`, and dev fixtures default `series: []` in the
  analytics shape. DetailPanel-specific behavior is recorded in the panels overview and sidecars.
  Verification metadata pinned until closeout stamps the code commit.
- 2026-06-24T08:59+02:00 — Data route addition: added `taskIdentity.ts` to the route model as the
  shared lifecycle label/direct-task-document helper used by Operations and Detail. Verification
  metadata pinned until closeout stamps the code commit.
- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: dashboard projection types now carry explicit `enclosureId`, `leafId`, and `taskRoot` fields, and Engine Room renders the projected integration/source branch instead of hardcoding `main`. Detail lives in the `types/projection.ts`, engine-room fixture, and `EnclosureCanvas.tsx` sidecars. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-23T22:31+02:00 — Clarified Task 12 S2 topology wording: repo-scoped GrepAI dots come from
  addressable `targetRepos` inside one aggregate provider instance, while worktree providers remain
  bound by `worktreeGroup`. Verification metadata pinned until closeout stamps the S2 code commit.
- 2026-06-23T21:46+02:00 — Task 12 S2 route impact: `topology/model.ts` now includes repo-covered
  workspace providers in the repo ring and parents provider satellites by `worktreeGroup`, then `repoId`,
  then workspace core; `types/projection.ts` clarifies the binding comments and `model.test.ts` covers
  repo-scoped parenting plus precedence. Verification metadata pinned until closeout stamps the S2 code
  commit.
- 2026-06-23T16:02+02:00 — Task 12 S1 route impact: `topology/model.ts` now records worktree
  groups while building topology nodes and parents worktree-scoped providers to the owning worktree
  node, with fallback/workspace providers staying on the workspace core. `topology/model.test.ts`
  adds pure-model coverage for matching, fallback, and workspace-provider behavior. No backend
  projection shape change; per-repo main-stack provider placement remains deferred to S2.
- 2026-06-23T15:05+02:00 — Task 10 dashboard fallback: `data/operatorInbox.ts` joined the data route and `GateResponder` now falls back to `POST /api/operator-inbox` for lifecycles without a hosted chat session, preserving the agent-owned gate-release model. Verification metadata pinned until closeout stamps the task-10 code commit.
- 2026-06-23T14:31+02:00 — Task 11 route impact: `dashboard/src/` now treats gate response as a
  hosted-chat direct-inject surface instead of the old developer gate-decision `/api/actions` drawer.
  `cockpit/Cockpit.tsx` threads selected lifecycle identity into Chats and HighlightComposer,
  `data/sessions.ts` owns lifecycle-tagged hosted sessions, and `panels/GateResponder.tsx` is the shared
  Respond control used by DetailPanel plus secondary engine-room/Hangar gate surfaces.
- 2026-06-23T13:35+02:00 — No route impact: slice-12 topology render-robustness — `topology/constel.ts` gained a file sidecar (the renderer now paints synchronously on resize/update, not rAF-only) and `panels/Topology.tsx` made the canvas absolutely-positioned + the `Panel` `fill`. Behaviour-preserving render/layout fixes within the existing `dashboard/src` route model; no structural change.
- 2026-06-22T11:00+02:00 — No route impact: slice 05o T7B–T18's `dashboard/src/`-direct changes are `dev/scenarios.ts`
  gaining six more failure-mode timelines (`seed-fault` T9B, `reindex-reroute` T9C, `provider-block` T7B,
  `live-sync` T12B, `integration-conflict` T14C, `abandon` T18) and `types/projection.ts` gaining the
  `refusedPolarity` edge field + a `refused` state — both additive within the existing `dev/`/`data/` route model
  (named `erFrame`-wrapped `Scenario`s + projection-type fields, not a shape change). The renderer primitives
  (refused-conduit flash, moved-badge, engine-dropout) and the six wirings are internal to `panels/engine-room/`
  (its overview + sidecars). The `dashboard/src/` route model (`cockpit/`/`grammar/`/`panels/`/`data/`/`dev/`) is
  unchanged. Verification metadata pinned until closeout stamps the 05o code commit.
- 2026-06-22T01:40+02:00 — No route impact: slice 05o T1B's only `dashboard/src/`-direct change is the `dev/`
  scenario player — `dev/scenarios.ts` gains the `stale-base` preflight→fast-forward failure-mode timeline (F0→F8,
  + `dev/scenarios.test.ts` a case) — which is data within the existing `dev/` route model, not a shape change.
  The T1B renderer primitives (the pruned `main` node), the indicator anchoring / z-order fixes, the
  `FleetingEnclosure` box, and the alert transitions are internal to `panels/engine-room/`, and the §10 spec note
  is under the sibling `docs/design/engine-room/`; the `dashboard/src/` route model
  (`cockpit/`/`grammar/`/`panels/`/`data/`/`dev/`) is unchanged — detail in those overviews + sidecars.
  Verification metadata pinned until closeout stamps the 05o code commit.
- 2026-06-22T00:29+02:00 — No route impact: slice 05o T3B's only `dashboard/src/`-direct change is the `dev/`
  scenario player — `dev/scenarios.ts` gains the `memory-block` failure-mode timeline (+ `dev/scenarios.test.ts`
  a case) — which is data within the existing `dev/` route model, not a shape change. The failure-mode renderer
  primitives (scan ring, ghosted lane), fixtures, and the engine-gauge polish are internal to
  `panels/engine-room/`, and the §10 spec section is under the sibling `docs/design/engine-room/`; the
  `dashboard/src/` route model (`cockpit/`/`grammar/`/`panels/`/`data/`/`dev/`) is unchanged — detail in those
  overviews + sidecars. Verification metadata pinned until closeout stamps the 05o code commit.
- 2026-06-21T23:35+02:00 — slice 05k tear-down + design-review refinements: the only `dashboard/src/`-direct
  change is `index.css` deleting the `@keyframes powerup` (the last engine-room canvas keyframe — the
  indexing→nominal engine flash, now a Motion opacity pulse on the charge rect). All the rest — the tear-down
  dispose sequence + power-down diagnostics, the second-loop engine-fill fix, the three-column re-spacing, the
  closeout-train breadcrumb, and the memory integration arrow — is internal to `panels/engine-room/` (its
  overview + sidecars). The `cockpit/`/`grammar/`/`panels/`/`data/`/`dev/` route model is unchanged. (Separately,
  `docs/design/` was brought into onboarding scope — a sibling route, not under `dashboard/src/`.) Verification
  metadata pinned until closeout stamps the code commit.
- 2026-06-21T09:57+02:00 — slice 05n (engine-room DrawSVG/MotionPath migration): the only `dashboard/src/`-direct
  change is `test/setup.ts` adding a jsdom **SVG-geometry stub** (`getBBox`/`getTotalLength`/`getPointAtLength`)
  so the engine-room GSAP DrawSVG/MotionPath plugins construct under the effects-on GSAP-gate test. The render
  rework (draw-on → DrawSVG one-shot, packet → MotionPath, the `flowConduit` recipe) is internal to
  `panels/engine-room/` (its overview + sidecars). The `dashboard/src/` route model
  (`cockpit/`/`grammar/`/`panels/`/`data/`/`dev/`) is unchanged. Verification metadata pinned until closeout
  stamps the 05n commit.
- 2026-06-21T02:44+02:00 — slice 6g: the cockpit gained **task-document navigation** — `panels/DetailPanel` renders a series **master** (overview + clickable sub-task index) with in-panel **drill-in** into each slice (the back/parent up-link in the sticky panel header), **markdown-rendered** task prose via the new `grammar/Markdown` primitive, and **cross-master "→" navigation** that jumps between series lifecycles (`onOpenLifecycle`). Detail in the `grammar/` + `panels/` overviews. Verification metadata pinned until closeout stamps the 6g code commit.
- 2026-06-21T02:26+02:00 — slice 05k (engine-room motion → GSAP/Motion): the only `dashboard/src/`-direct
  change is `index.css` deleting the nine engine-room canvas `@keyframes` (`chargeSweep`/`conduitDraw`/`pktRun`/
  `attnBreath`/`stopFlash`/`closeoutSweep`/`warpSurgeUp`/`warpSurgeDown`/`landingIn`) that prior slices parked
  in the effects layer; the engine-room canvas motion now runs on GSAP timelines (`useEngineTimeline`) + Motion,
  CSS static (the app-wide `crt-overlay`/`flicker`/`pulse` keyframes stay). The render rework + the new hook are
  internal to `panels/engine-room/` (its overview + sidecars). The `cockpit/`/`grammar/`/`panels/`/`data/`/`dev/`
  route model is unchanged. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-19T23:58+02:00 — slice 5i: the `dev/` sub-route gained the **scenario player** — new
  `dev/scenarios.ts` (timeline model) + `dev/ScenarioPlayer.tsx` (transport) + `dev/scenarios.test.ts`, with
  `dev/Bench.tsx` reworked from the static gallery into a scenario picker + player and `dev/fixtures.ts`
  extracting the shared `engineRoomProjection` wrap; `dev/Bench.tsx` also gained a sidecar (a prior gap). The
  only other `dashboard/src/`-direct change is the `index.css` `landingIn` keyframe (engine-room landing-tail
  detail). The engine-room render rework is internal to `panels/engine-room/` (its overview + sidecars). The
  `cockpit/`/`grammar/`/`panels/`/`data/` route model is otherwise unchanged. Verification metadata pinned
  until closeout stamps the code commit.
- 2026-06-19T15:59+02:00 — Task 6 slice 6f-1: the cockpit gained the **highlight → context-package** composer — `panels/HighlightComposer.tsx` (mounted in `CockpitShell`) + the `data/selection.ts` selection hook; a text selection raises it to send the selection + a message into a chat session's stdin (the `data/sessions` store became the cockpit-wide inject seam; `data/terminal.ts` buffers pre-open stdin for create-then-send). No silent action; reuses the live B2 channel (not ACP). Detail in the `panels/` + `data/` sidecars. Verification metadata pinned until closeout stamps the 6f-1 code commit.
- 2026-06-19T14:05+02:00 — Task 6 slice 6e-4: terminal/session **hardening** — the open-session registry moved into a new `data/sessions` Zustand store, and a live terminal now survives both a cockpit *view* switch (`cockpit/Cockpit.tsx` keeps `<Chats>` mounted, hidden via CSS) and a *session-tab* switch (`panels/Chats.tsx` keeps every session's `<Terminal>` mounted) instead of being unmounted; the backend PTY spawn (`serving/terminal.py`) gained a controlling terminal so tmux honors resize, and `data/terminal.ts` replays the first winsize on socket open. Detail in the `data/` + `panels/` sidecars. Verification metadata pinned until closeout stamps the 6e-4 code commit.
- 2026-06-19T06:39+02:00 — No route impact: an engine-room crash fix relaxes `EngineProcessNode.landing` to optional (`landing?:`) in `types/projection.ts` so the canvas tolerates a pre-5h/persisted projection that omits it; the `dashboard/src/` route model (`cockpit/`/`grammar/`/`panels/`/`data/`/`dev/`) is unchanged — detail in the `types/projection.ts` sidecar. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-19T05:48+02:00 — Task 6 slice 6e-3: the **Chats** terminal gained **context injection** — a `SessionComposer` (React Aria `TextField`/`TextArea` + `Button`) docked below the terminal injects a block of text into the active session's stdin as a bracketed paste (the on-ramp to 6f). Refreshed the Behavior layer. Verification metadata pinned until closeout stamps the 6e-3 code commit.
- 2026-06-19T04:38+02:00 — Task 6 slice 6e-2c: the **Chats** view's open sessions moved into a dedicated left-rail **`SessionList`** switcher (a React Aria `GridList` — single-select = active session, per-row close ✕), replacing the horizontal tab strip; the launch controls stay in the top strip and the harness buttons now share ＋ Terminal's golden look. Refreshed the Behavior layer (the switcher's `GridList`) + the `panels/` route-model line. Verification metadata pinned until closeout stamps the 6e-2c code commit.
- 2026-06-18T21:27+02:00 — No route impact: a dev-bench review-ergonomics pass collapsed the `/dev/bench` gallery strip into a compact `<select>` picker + trimmed the 6 `engine-boot-*` step tabs and the unused `engine-empty` fixture (mirroring task 5's `b3f2491`). All internal to the DEV-only `dev/` harness (dropped from the production bundle); the `dashboard/src/` route model (`cockpit/`/`grammar/`/`panels/`/`data/`/`dev/`) this overview describes is unchanged — detail in the `dev/` sidecars. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T21:27+02:00 — Task 6 slice 6e-2b: the **Chats** view gained per-harness launch buttons — `data/terminal.ts` `fetchHarnesses` (`GET /api/harnesses`) drives a detection-driven button per *installed* harness (Claude Code / Codex / Pi.dev) beside ＋ Terminal. Detail in the `panels/` overview + the `Chats.tsx`/`terminal.ts` sidecars. Verification metadata pinned until closeout stamps the 6e-2b code commit.
- 2026-06-18T21:25+02:00 — No route impact: slice 5h Tier 2's only `dashboard/src/`-direct change is mirroring the four optional `LedgerRefNode` fields (`codeSubject?`/`codeDate?`/`memorySubject?`/`memoryDate?`) in `types/projection.ts`; the 6-column popover render lives in `panels/engine-room/` (its overview + sidecars). The `dashboard/src/` route model (`cockpit/`/`grammar/`/`panels/`/`data/`/`dev/`) is unchanged. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T18:00+02:00 — No route impact: slice 5h's ledger popover mirrors `LedgerRefNode` + the additive `LedgerNode.rows` / `EngineProcessNode.ledgerRows`/`ledgerRowCount` fields in `types/projection.ts` and wires the demo `analytics.ledgers` in `dev/fixtures.ts`; the `dashboard/src/` route model (`cockpit/`/`grammar/`/`panels/`/`data/`/`dev/`) is unchanged — detail lives in the `engine-room/` overview + the `types/projection.ts` sidecar. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T17:40+02:00 — Task 6 slice 6e-2a: the **Chats** view became a **create** surface — "＋ Terminal" spawns a dashboard-owned session via the new `data/terminal.ts` `openTerminalSession` → the `POST /api/terminal` opener (no longer just attaching to a store lifecycle). Detail in the `panels/` overview + the `Chats.tsx`/`terminal.ts` sidecars. Verification metadata pinned until closeout stamps the 6e-2a code commit.
- 2026-06-18T16:50+02:00 — Task 6 slice 6e-1: the cockpit gained its first **interactive terminal** — a full-bleed **Chats** view (`panels/Chats.tsx` + the lazy `panels/Terminal.tsx` xterm wrapper) over the new `data/terminal.ts` Mode B2 WebSocket client (binary PTY bytes in, `{type:stdin|resize}` out), reachable from the cockpit mode bar. **Corrected the stale "Read-only — no POST" invariant** (write surfaces have existed since 6c; 6e adds the bidirectional terminal). Dev bench supplies a mock socket so it renders without a backend; the real launch is 6e-2. Verification metadata pinned until closeout stamps the 6e-1 code commit.
- 2026-06-18T15:50+02:00 — No route impact: the 5h cleanup pass's only `dashboard/src/`-direct change is `dev/fixtures.ts` filtering the `engine-boot-*` frames out of the bench gallery tab strip (a DEV-harness curation); the rest is render polish internal to `panels/engine-room/` (conduit wiring + backdrop vignette + a dropped fixture). The `dashboard/src/` route model (`cockpit/`/`grammar/`/`panels/`/`data/`/`dev/`) is unchanged — detail lives in the `engine-room/` overview + sidecars. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T15:00+02:00 — Task 6 slice 6c Part B: the cockpit gained its **one write** — `DetailPanel`'s Gate Review drawer POSTs a developer gate decision to `/api/actions` via the new `data/actions.ts` (+ a `gate-review` bench scene in `dev/fixtures.ts`). The rest stays read-only. Verification metadata pinned until closeout stamps the 6c Part B code commit.
- 2026-06-18T14:05+02:00 — No route impact: task 6 slice 6c Part A only extended the projection **type mirror** (`types/projection.ts` gained `GateNode` + the optional `LifecycleProjection.gate`); the `dashboard/src/` route model (`cockpit/`/`grammar/`/`panels/`/`data/`) is unchanged. The gate review **drawer** (`panels/DetailPanel.tsx` + `data/`) lands in 6c Part B — surfaced here then. Verification metadata pinned until closeout stamps the 6c Part A code commit.
- 2026-06-18T13:01+02:00 — No route impact: the 5h coupler fix's only `dashboard/src/`-direct change is the `index.css` `warpSurgeUp`/`warpSurgeDown` keyframes (the coupler warp-core surge, frozen by `effects=off`); the render lives in `panels/engine-room/`. The `dashboard/src/` route model is unchanged. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T11:55+02:00 — No route impact: slice 5h H2's only `dashboard/src/`-direct change is the `index.css` `closeoutSweep` keyframe (the closeout-train fill, frozen by the `effects=off` rule); the render lives in `panels/engine-room/` (its overview + sidecars). The `dashboard/src/` route model (`cockpit/`/`grammar/`/`panels/`/`data/`) is unchanged. Verification metadata pinned until closeout stamps the 5h H2 code commit.
- 2026-06-18T08:51+02:00 — No route impact: slice 5h H1 mirrors `LandingRefNode` + the additive `EngineProcessNode.landing` / `integrationStrategy` fields in `types/projection.ts` (and adds landing fixtures under `panels/engine-room/`); the `dashboard/src/` route model (`cockpit/`/`grammar/`/`panels/`/`data/`) this overview describes is unchanged — detail lives in the `engine-room/` overview + the `types/projection.ts` sidecar. Verification metadata pinned until closeout stamps the 5h code commit.
- 2026-06-17T22:45+02:00 — No route impact: the engine-room visual-parity pass (the 5g G6 blueprint backdrop + the
  cockpit Effects/Calm toggle, the `engine-room/` SVG decal layer, and the `grammar/Panel` `fill` height fix)
  is internal to those sub-routes; the `dashboard/src/` route model (`cockpit/`/`grammar/`/`panels/`/`data/`)
  this overview describes is unchanged — detail lives in those overviews + sidecars.
- 2026-06-17T16:15+02:00 — No route impact: slice 5g G5 lands the Engine Room live/teardown states
  (t12b/t14c/t18) + a green=active engine palette + a left-rail scroll fix — all internal to
  `panels/engine-room/` — plus an `index.css` `stopFlash` keyframe. The `dashboard/src/` route model
  (`panels/`/`grammar/`/`data/`/`cockpit/`) is unchanged; detail lives in the `engine-room/` overview +
  sidecars. Verification metadata pinned until closeout stamps the G5 code commit.
- 2026-06-17T14:00+02:00 — No route impact: `index.css` gained the `attnBreath` keyframe (the failure-overlay
  attention-badge breathing, 5g G3). Engine-room detail (surfaced in the `panels/engine-room` overview);
  the dashboard/src architecture this overview describes is unchanged. Verification metadata pinned until
  closeout stamps the G3 commit.
- 2026-06-17T13:30+02:00 — No route impact: `index.css` gained the Engine Room pod-stage motion keyframes
  (`chargeSweep` / `conduitDraw` / `pktRun`, 5g G2) + a `conduit-packet` freeze rule. These are engine-room
  detail (surfaced in the `panels/engine-room` overview); the dashboard/src architecture this overview
  describes is unchanged. Verification metadata pinned until closeout stamps the G2 commit.
- 2026-06-16T02:30+02:00 — slice 5f S1: the cockpit shell's machine-map views (Engine Room / Topology) go
  full-bleed (rails hidden, §4.1); added the dashboard suite's first component-render test
  (`cockpit/Cockpit.test.tsx`) and the shared jsdom stubs in `test/setup.ts`. The `dashboard/src/`
  route model is otherwise unchanged (detail in the `cockpit/` + `engine-room/` sidecars/overviews).
  Verification metadata pinned until closeout stamps the S1 code commit.
- 2026-06-15T19:35+02:00 — No route impact: slice 5e adds the `panels/engine-room/` sub-route (its own route overview + file sidecars) plus `types/projection.ts` / `dev/fixtures.ts` changes; the `dashboard/src/` route model this overview describes (the `panels/` / `grammar/` / `data/` / `cockpit/` split) is unchanged — detail lives in the `panels/` + `engine-room/` overviews and the file sidecars.
- 2026-06-15T17:00+02:00 — Created for slice 5d: the frontend re-architecture (Panda + React Aria,
  layered). Documents the layered styling architecture, the grammar/panels split, and the read-only
  boundary. Verification metadata pinned until closeout stamps the 5d code commit.
