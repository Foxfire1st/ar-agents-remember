# dashboard/src/fixtures/snapshot.json

## Governing Overview

[overview](../overview.md)

## Purpose

The dashboard's stand-in for the server: one `WorkspaceProjection` payload shaped like the persisted
`latest-state.json`, plus sampled served-tail fields. Its remaining readers include `test/contract.test.ts` (which measures the
TypeScript mirror against the sample), `test/fixtures/wire.ts` (which takes retained builder
bases from it), and `data/store.test.ts`.

Task entries carry native identity, stage/activity, ordered child keys, counts, nested summaries and bound worktrees. Optional reader, completion, dependency and graph values remain hand-authored shape examples, not native finalization, dependency resolution or scheduling proof.

**It is NOT generated.** This file is a hand-maintained sample. The TypeScript mirror it is checked
against is generated and stale-checked from the Pydantic projection schema, so sample coverage and
producer-to-TypeScript provenance are separate claims. `fixtures/wire.ts` draws that boundary:

```text
observer/projection.py schema  --generated + stale-checked-->  types/projection.ts
                                                                ↑ typed fixture builders
                                                                ↕ measured sample coverage
                                                         snapshot.json (manual)
```

So a green sample-coverage build claims that this manual payload exercises the generated mirror.
The projection generator separately binds that mirror to the producer schema, including fields a
sample could miss because their values are currently null or absent.

The manual sprint/master/leaf examples now use TaskEntry membership and nested TaskSummary content. They exercise qualified navigation without analytics document/series joins; illustrative seats and graph data remain invented samples. The master also samples `names-another-master`, `listed-twice` and `unresolvable-master` disagreements, including the unresolved literal. These are hand-maintained wire-shape examples, not a diagnosis or repair of real records, and they do not exhaust every permitted kind.

The manual sample carries representative lifecycle-operation rows. The sample carries public progress/result/failure/guidance fields
including public identity/component fingerprints and approval state, but no private operation key
or worker PID, preserving the
producer's private-plane boundary while making the generated dashboard contract measurable.

The current sample carries the served-tail fields `watcherHealth`, `checkoutBinding`,
`buildCurrentness` (an installed-mode `stale` example with both Python digests, the first-seen time,
reason and remedy) and `servingProcessId`, and omits `servingBuild`. The contract guard's
`KnownUnsampled` paths are `projection.servingBuild` and `projection.tasks[].providerLimit`; its
vocabulary checks, including the `buildCurrentness` mode and state vocabularies, apply to the current
generated schema.

## Code Commentary

### Logic

Code and memory publication samples are present. The `analytics.ledgers` data represents a
downstream consumer projection.

The serialized root carries tasks and taskCounts instead of session lifecycles and duplicate analytics task-document/series catalogues. Operational enclosures, closeout queues, analytics, metrics and watcherHealth remain sample data; the sample carries no provider records or setup-progress/setup-summary collections.

Native entries and operation meaningfulRevision values are hand-maintained coverage examples.

### Conventions

- The sample combines the persisted projection core with sampled watcherHealth, checkoutBinding, buildCurrentness and servingProcessId. servingBuild is absent and is one of the two contract.test.ts::KnownUnsampled residues, beside a task's providerLimit. The served tail declares servingBuild, watcherHealth, checkoutBinding, buildCurrentness and servingProcessId.
- Non-uniform on purpose. Arrays are keyed by TYPE in the mirror walk, so coverage is accumulated across representative rows. The payload does not have to be uniform; it has to be
  COMPLETE between its rows.
- Timestamps sit in a single fabricated window around `2026-06-14T09:00`, and identifiers are
  `sim-`/`SIM`-prefixed, so nothing in it reads as a captured production workspace.

### Invariants And Boundaries

- **Every declared mirror path must stay sampled.** Deleting a field, or emptying an array, is not a
  neutral edit. **An empty array is worse than a missing field** — it is blindness in both directions at
  once, because `AsJsonModule` accepts `never[]` as assignable to anything and `ServedOnlyPaths<never, …>`
  is `never`. `MirrorOnlyPaths` now names any path that stops being reached, so this is enforced, not
  merely asked for.
- **Every sampled vocabulary value must be legal, and every registered path must be non-vacuous.** This file is also the only place the attention row's `itemClass` vocabulary is exercised end to end: an operational row, a permission-wait action row on a taskless agent and a landed notice row, each beside the task key, agent identity and occurrence identity it opens.
  The fixture is representative rather than exhaustive. New producer enum members flow through schema
  generation and stale-output validation without forcing unrelated full-object rows into this file.
- **Required fixture anchor rows must remain nonempty.** Shared builders require native tasks, enclosures and retained engine-process/attention samples; demandServed refuses a missing anchor rather than spreading undefined.
- This file is the ORACLE, not a scenario. Dev-gallery scenarios live in `src/dev/`; per-suite shapes
  are built with `test/fixtures/wire.ts`. Do not add rows here to make one test convenient — a row added
  here changes what every direction of the contract guard measures.
- Edit it against `observer/projection.py` (and the reducer that fills each field), never against the
  TypeScript mirror. Shaping it from the mirror would make the guard measure the mirror against itself.

### Todos

**What this fixture cannot cover, stated so a clean contract run is not read as more than it is.**

1. **It is a sample, not a schema.** A server field typed `T | None` that happens to be null is *omitted*
   by `exclude_none=True`, so no sampled payload can reveal it. Only the schema can.
2. **It does not establish producer vocabulary.** Schema generation owns exhaustive
   producer-to-mirror vocabulary. This sample proves only that values it carries are legal.
3. **Structural sampling is not nominal identity proof.** A payload walk cannot distinguish field-identical models by their names alone.
4. **The sample remains manual while the mirror is generated.** Do not describe this JSON payload as
   generated, and do not describe its coverage limits as a missing producer-to-TypeScript contract.
5. **Provenance wording must preserve that split.** The remaining `test/fixtures/wire.ts` and
   `contract.test.ts` owners distinguish manual sample coverage from generated mirror provenance.

## Manual direct-grant display samples

The directGrant examples are nested summary data on native entries and carry fabricated developer giver/time evidence. These hand-maintained shape samples exercise display fields in the generated mirror; they are not live external grants, proof of ordinary-start eligibility, or browser authorization. The current sample remains manual, and no new visual/sandbox qualification is claimed for the port.

## Manual Order and Completion Samples

The added fields extend wire coverage only. The fixture remains hand-maintained; no producer run, finalization or same-master dependency join is established by these samples.




## Evidence

### Docs References

No Domain Documentation source is configured in the resolved memory repository. The local
serialization and typecheck contracts are supported by the source references below; this pass
makes no separately verified external-library documentation claim.

No configured external documentation source applies.

### Repo-Internal References

The payload's shape is fixed by pydantic serialization behaviour on this repository's own models —
`model_dump(by_alias=True, exclude_none=True)` — which is what makes a null-valued optional field
absent from the file rather than present as `null`.





- The manual payload retains representative enclosure rows and the activeWorktreeGroups join value; the enclosure carries the same sim-group identity. [5]


- Manual decision and task-reader values are sample data, not source-derived provenance. [6]





- The writer of the persisted payload this file is shaped like: `write_projection` dumps with `by_alias=True, exclude_none=True` into `latest-state.json`. [8]



- The core root plus extracted task DTOs declare strict wire shapes; TaskDependencyNode is display data, distinct from sample values and execution. [9]




- The three-direction guard: `mirror ⊇ served`, `served ⊇ mirror`, and `fixture ⊇ mirror` — the last of which exists because this payload is the oracle. [10]


- The derived `VOCABULARIES` registry and its non-vacuous sampled-value membership assertion. [11]



- INDEX_SIGNATURE_SITES is a closed, exhaustive record naming every current absorbing node with its reason. [12]





- KnownUnsampled names projection.servingBuild and a task's providerLimit; the manual sample carries the other served-tail fields. [13]
- The served tail declares servingBuild, watcherHealth, checkoutBinding, buildCurrentness and servingProcessId. [21]
- The sample carries a stale installed-mode build currentness and a serving process id. [22]



- The snapshot is manual; the projection command generates and stale-checks the schema and TypeScript mirror. Anchor: `generated` [14]
- The narrowing every reader comes through, and why a second `as unknown as` elsewhere would re-open the hole. Anchor: "as unknown as" [16]

- The store suite consumes the manual fixture and explicitly exercises servingBuild, whose absence in the fixture is separately admitted by KnownUnsampled. [17]


### Cross-Repo References

No cross-repository boundary. The payload imitates this repository's own Python serving layer; both
sides live in `agents-remember`.

The producer and fixture both belong to this repository; their implementation evidence is listed above.

## Source-Lineage Samples

Engine Process fixtures now sample aggregate `current`, `blocked`, and
`unavailable` states, every edge relation/side/state, and one
contract-addressed `worktree_sync` recovery. These are wire-contract examples,
not frontend-derived Git facts.


## Fixture Graph View

The sprint fixture (`sim-master` / `sim-master-b` scenario) carries the render-ready `executionGraphView`: a segmented master with a joined title and an early leaf, plus a dependent second master waiting on it with a recorded predecessor reason and judgment id. Those rows remain representative contract examples; complete enum ownership stays with schema generation.


## Source-Relation and Graph-View Samples

The snapshot fixture carries a super-to-leaf source-relation entry (`relation: "super-to-leaf"`, state `current`) and two execution-graph view nodes (a `segment` with `frontierState: "landed"` and a `lump` with `frontierState: "ready"`) as representative dashboard contract examples.

## Fixture Cursor Sample

The hand-kept fixture snapshot seeds `meaningfulRevision: 1` on lifecycle
operation nodes, so dashboard and
wire-fixture consumers have a cursor-carrying sample matching the regenerated schema.

## Product-Record Fixture Flags

Two sampled decisions carry explicit `product_record: false`, so the hand-maintained fixture
exercises the product-record marking the projection serves: authored decisions stay unmarked
while writer constants mark records.



- Manual fixture includes native operation/source-lineage wire samples, not live operation evidence. [19]


- Ledger analytics remain a consumer sample after the retired Git-operation phase is removed. Anchor: `observer`; "ledgers" [1]

- Removed the retired ledger-commit operation sample while preserving downstream ledger analytics and real publication phases. Anchor: `lifecycle`; "commit-approval-pending" [2]


- `exclude_none=True` omits fields whose value is `None` from the serialized output — the rule that makes an omitted key here indistinguishable from a field the server does not have. Anchor: `None` [3]


- The manual master sample carries three disagreement shapes and the unresolvable literal; this is sample coverage, not live membership evidence. [20]

## Dismissible Action Sample

The sampled `permission-wait:agent-7` row carries `dismissible: true`, the value the producer publishes for a live native cause; `itemClass` stays `action`, and the row's agent, prompt and held-message identities are unchanged. The fixture samples a dismissible action row beside the operational and notice rows. Its attention rows stay in hand-authored order and are not a claim about the served newest-first order, and the sample remains a wire shape rather than proof that a dismissal is served.
