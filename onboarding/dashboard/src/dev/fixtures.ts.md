# dashboard/src/dev/fixtures.ts

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

Hand-authored WorkspaceProjection gallery. The bench hydrates scenarios into the store; component suites consume them directly. Engine Room scenes reuse ENGINE_ROOM_SCENARIOS. Invented inputs are neither live producer output nor browser acceptance.

Since 260731-EFA-L4 the split of responsibility is explicit in the file's own header: **the scenarios
are this file's business; the nodes are not.** Every node builder delegates to
`src/test/fixtures/wire.ts`, and `EMPTY_ANALYTICS` is imported from there rather than declared here.
What the gallery keeps is its own *defaults* — fixed gallery identity and header values — passed explicitly to the shared builders; it supplies no task examples, and the shared default projects an empty task list. What it no longer keeps is a second
copy of the required-field list, which is the part that drifts.

## Code Commentary

### Logic

`project` delegates to the shared builder with gallery version/generatedAt defaults. Native task/count bases replace simulated session lifecycles and metricsFor rollups; EMPTY_ANALYTICS retains operational lists, not document/series catalogues. Enclosure and event factories delegate with gallery defaults before caller overrides.

A fixture that type-checks through these builders is a shape **the mirror** (`types/projection.ts`)
can produce. `wire.ts` bases are assembled from `src/fixtures/snapshot.json`, which is **hand-maintained, not a generated snapshot**. `wire.ts`'s own header
carries the full chain and where it stops: fixture ⊆ mirror is held by `tsc` and `contract.test.ts`;
producer-to-mirror conformance is held separately by schema generation and its stale-output check. The snapshot remains manual.

**Slice 5i** extracts the engine-room wrap into an exported
`engineRoomProjection(scenario)` — `project({ analytics: { ...EMPTY_ANALYTICS,
engineProcesses: scenario.processes, ledgers: [OFFICIAL_LEDGER] } })` — the single mapping shared by
**both** the `GALLERY` Engine Room entries and the scenario-player frames (`dev/scenarios.ts`). It
projects the scenario's process facts; the scenario type contains no workspace-provider collection.
Typed node factories retain explicit gallery defaults. `enclosure()` supplies enclosure identity and
worktree/landing defaults, and `evt()` supplies an event timestamp before caller overrides. The
provider factory and `providerRole` helper are removed. `EMPTY_ANALYTICS` is imported from
`test/fixtures/wire.ts`; this wrapper fills its engine-process and ledger collections. Native
tasks/counts are projection-root fields; no `lifecycle()` helper or analytics task-document/series
catalogue remains.

`GALLERY` (typed `GalleryEntry[]`) retains its invented scenario choices and then spreads
`ENGINE_ROOM_SCENARIOS.filter((scenario) => !scenario.name.startsWith('engine-boot-')).map(...)`,
with each retained entry passed through `engineRoomProjection`. The `engine-boot-*` frames stay out
of the gallery tab strip and remain available to the scenario player and component tests. The
`alarm` scene supplies actionable-drift and blocked-start attention items. The Engine Room mapping
sets `analytics.ledgers: [OFFICIAL_LEDGER]` so the OFFICIAL coupler can resolve its repository's ledger;
the `full` cockpit scene supplies hand-authored ledger rows. These remain invented demonstration
data, not observed workspace state.

### Conventions



### Todos

No open file-local todos.

### Invariants And Boundaries



Since 260731-EFA-L4:

- **No node builder may hold its own required-field list** — with one recorded exception: the gallery's four inline attention literals now spell `itemClass`/`dismissible` themselves. Duplication is what that
exception buys: the contextual `Partial<WorkspaceProjection>` type still checks their required fields, so a mirror
change is caught here as a type error rather than silently accepted. Every builder delegates to
  `test/fixtures/wire.ts`; a required field the mirror adds must fail to compile here rather than be
  filled in a second place.
- Shared task/count bases and explicit overrides are fixture construction, not evidence of live counting.
- Gallery *defaults* are legitimate and stay: they are presentation choices (fixed `generatedAt` and identity values), passed explicitly as overrides, not a parallel definition of the shape; tasks come from the shared default, which is an empty list.
- `snapshot.json` behind those builders is hand-maintained and has no generator; a green build here
  claims the **mirror** could produce the shape, not that the server sent it.

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; it has no configured Domain
Documentation entries. This card is verified from its direct source and the shared wire fixtures it
now delegates to.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

The gallery is now a consumer of the shared wire builders rather than a second definition of the wire
shape, so both sides of that delegation are cited.

- `project()` calls `servedProjection`. [2]
- The gallery maps Engine Room scenarios through `engineRoomProjection`. [4]

- The gallery wraps Engine Room process facts and OFFICIAL_LEDGER into analytics; its filtered gallery entries reuse that wrapper. EngineRoomScenario contains a name and processes, with no workspace-provider collection. [7]

- WorkspaceProjection owns analytics as a required field. [9]

### Cross-Repo References

No meaningful cross-repo references found. The projection shapes these fixtures build mirror server
models in `mcp/` inside this same repository; nothing here crosses a repository boundary.

No meaningful cross-repo references found.

## Series-Contract Notes

The dev projection fixture now includes `enclosureId`, `leafId`, and `taskRoot` on each `EnclosureNode`, matching the server projection after leaf enclosure contracts moved under `enclosures/<leaf-id>/series-contract.md`. Since 260703-L11 the `enclosure(...)` factory also defaults the required existence-truth flags `codeWorktreeExists`/`memoryWorktreeExists` to `true`, so the seeded gallery enclosures render as live worktrees on physical-worktree surfaces such as Hangar; Operations task admission is independent of those flags.
