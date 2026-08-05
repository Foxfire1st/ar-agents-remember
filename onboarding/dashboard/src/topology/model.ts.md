# dashboard/src/topology/model.ts

| Field                  | Value                                       |
| ---------------------- | ------------------------------------------- |
| repository             | agents-remember                             |
| path                   | `dashboard/src/topology/model.ts`           |
| doc_type               | `file-level-onboarding`                     |
| lastUpdated            | 2026-08-01T10:30+02:00                      |
| lastVerifiedCommitHash |                                             `e52edaf5b655f495580efd93306afdf922b19b51`|
| lastVerifiedCommitDate |                                             2026-08-01T11:01:51+02:00|
| governingOverview      | `../overview.md`                            |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

`model.ts` builds the pure, deterministic data model that the Topology canvas renderer draws. It
translates observer projection nodes into a bounded radial constellation: workspace core → source
checkouts (inner ring) → **active** worktree enclosures (outer ring), with provider satellites attached
to the entity they are scoped to. The view shows live work only — there is **no separate lifecycle/task
rim**; each active enclosure node folds in its 1:1 lifecycle (id, status, phase·state).

It also **owns the state → status grammar** for the whole constellation surface: the exported
`CONSTEL_STATUSES` vocabulary, the total `CONSTEL_STATUS_BY_STATE` table, the declared
`UNCLASSIFIED_STATUS`, and the exported `lifecycleStatus` that reads them. `constel.ts` keys its
palette off the same vocabulary, so there is exactly one place a lifecycle state acquires a colour.

## Code Commentary

### Logic

**The state → status grammar (260731-EFA-L4 — the leaf's headline defect).** `lifecycleStatus` was an
if-chain that named five of the six declared states and ended in `return "ok"`. `awaiting-developer`
— the NOTIFY-AND-CONTINUE turn end, where the turn is back with the developer — was the sixth, so a
lifecycle waiting on a person drew as a **healthy** node on the one surface a developer scans for work
owed to them. The chain is now four declarations:

- `CONSTEL_STATUSES = ["core","ok","warn","crit","idle"] as const`, with `ConstelStatus` **derived**
  from the tuple, so the vocabulary is one list readable at runtime (tests iterate it; `constel.ts`
  keys its palette by it) rather than a union only `tsc` can see.
- `CONSTEL_STATUS_BY_STATE: Record<State, ConstelStatus>` — total by construction. A seventh entry in
  `LIFECYCLE_STATES` stops this object literal compiling until someone rules on it. The rulings:
  `blocked → crit`; `awaiting-developer → warn`; `paused → warn`; `abandoned → idle`;
  `running`/`completed → ok`.
- `UNCLASSIFIED_STATUS: ConstelStatus = "warn"` — what a state this build has never heard of (a newer
  server, or a projection persisted by one) renders as. Never `ok` (the exact wrong answer, the one
  that caused the defect), never `crit` (that would claim a fault the server never reported).
- `STATUS_BY_DECLARED_STATE: Partial<Record<string, ConstelStatus>>` — a **read view** over the same
  table. `lifecycle.state` is typed `State`, but that is a claim about a process this build does not
  control; indexing `Record<State, …>` directly types the miss away, so `?? UNCLASSIFIED_STATUS`
  would read as dead code that anyone could delete for zero new `tsc` errors. The alias makes the
  miss typed, so removing the `??` fails `tsc -b` here. (`noUncheckedIndexedAccess` would say the
  same for every index in the project; the file records it as measured-and-not-on — 601 errors across
  81 files, 33 non-test — so the guard is applied at the one seam where the key is wire data.)

`lifecycleStatus(lifecycle)` takes `Pick<LifecycleProjection, "state" | "inferred">` (it needs nothing
else, so a test can call it with a two-field literal). It reads the declared status through the view,
then applies one degrade: `inferred` downgrades a **healthy** reading only — `declared === "ok" &&
lifecycle.inferred ? "warn" : declared`. It never upgrades `warn`/`crit`/`idle`, because `inferred`
means the reducer derived the state (stale heartbeat → paused, dormant fleeting → abandoned) rather
than reading a written transition; an inferred blocked lifecycle is still a fault.

`activeTopologyInputs(lifecycles, enclosures, activeWorktreeGroups)` is the exported pure seam that
bounds the view to active work: it keeps only enclosures whose worktree group is in
`activeWorktreeGroups` (the server's active-enclosure admission), then keeps only the lifecycles bound to
one of those surviving enclosures. The caller (`Topology.tsx`) runs this before `buildTopology`; the
shared store collections keep all-time history for other views.

`buildTopology(lifecycles, enclosures, providers)` creates `ConstelNode[]` in a stable order over
whatever inputs it is given (it does not filter — that is `activeTopologyInputs`' job). It collects repo
keys from enclosure `repoName`s and repo-covered workspace provider `repoId`s (lifecycles no longer
contribute repo keys of their own), adds the workspace node, and adds source-checkout repo nodes around
the inner ring. It then groups enclosures by repo and spreads each repo's active worktrees across that
repo's angular span. Each enclosure binds 1:1 to its lifecycle (`EnclosureNode.lifecycleId` ↔
`LifecycleProjection.enclosure`), built via an `lcByEnclosure` map, so the `wt` (enclosure) node IS the
selectable leaf: it carries the lifecycle's `id` (click-through), `lifecycleStatus` colour, and
`phase · state` sub. The WORKSPACE sub-label reads `N checkouts · M active worktrees`.

Provider nodes use the same pure model: `engineState(provider)` maps provider health into constellation
status, and the provider parent is selected from `ProviderNode.worktreeGroup` first, then from
`ProviderNode.repoId`, and finally the workspace core. Worktree-scoped providers therefore still orbit
their owning enclosure, repo-covered workspace providers orbit the covered checkout, and aggregate
workspace providers stay on the core. This is visual binding, not provider process counting.

**Worktree-group join — basename normalisation.** `EnclosureNode.worktreeGroup` is a full path, while
the worktree-scoped `ProviderNode.worktreeGroup` and the `activeWorktreeGroups` set are basenames. The
`groupKey` helper (`group.split("/").pop()`) normalises both sides of every worktree-group join
(`wtIdxByGroup` keys, provider parenting, and `activeTopologyInputs`). This fixes a latent task-12-S1
bug: previously the enclosure side keyed by full path and the provider side looked up by basename, so on
real served data the join never matched and worktree providers fell back to the workspace core.

### Conventions

The file exports the model types/constants, the pure builder, `activeTopologyInputs`, and — since
260731-EFA-L4 — the classification grammar (`CONSTEL_STATUSES`, `CONSTEL_STATUS_BY_STATE`,
`UNCLASSIFIED_STATUS`, `lifecycleStatus`). Vocabularies are declared as `as const` tuples with the
type derived, matching `LIFECYCLE_STATES`/`PHASES` in `types/projection.ts`: a table only the type
system can see is a table no runtime assertion can prove total. `ConstelNode.parent`
is an index into the returned node list, not an id string, because the imperative renderer performs
hot-path layout over the array. `rf` selects the ring radius for checkouts/enclosures (`RF = {repo, wt}`,
no task ring); providers use `rf: 0` and orbit their parent via `poff`.

### Invariants And Boundaries

- **No unrecognised state may render as `ok`.** `UNCLASSIFIED_STATUS` is `warn` and the
  `?? UNCLASSIFIED_STATUS` in `lifecycleStatus` is load-bearing — it is reachable only because
  `STATUS_BY_DECLARED_STATE` re-types the lookup as partial. Deleting either the alias or the `??`
  restores the original defect end-to-end (the `undefined` flows to `constel.ts`'s palette).
- `CONSTEL_STATUS_BY_STATE` must stay total over `State`; a new `LIFECYCLE_STATES` member is a `tsc`
  failure here (and a vitest failure in `model.test.ts`) until it is classified.
- There is exactly ONE classification path. `buildTopology` calls `lifecycleStatus`; it must not grow
  a second if-chain that can disagree with the declared grammar.
- `inferred` degrades only. It turns `ok` into `warn` and leaves `warn`/`crit`/`idle` untouched.
- The builder stays pure and deterministic so unit tests can assert topology behavior without a canvas.
- `buildTopology` renders the enclosures/lifecycles it is given; active-scope filtering lives in
  `activeTopologyInputs`, so the two are independently testable.
- The enclosure (`wt`) node is the selectable leaf and carries its 1:1 lifecycle's id/status/sub; there
  is no `task`-kind node and no `RF.task` ring.
- Every worktree-group join (enclosure↔provider, enclosure↔active set) goes through `groupKey` so the
  path-vs-basename formats match.
- Provider parenting is model-owned; `constel.ts` only draws providers around the parent index it receives.
- Provider dots express the strongest known topology binding. They do not imply separate per-repo
  provider processes or per-root health unless the backend projection exposes that.
- This file must not read the store, DOM, canvas, or browser APIs.

### Todos

No open file-local todos.

## Docs References

No relevant external documentation was found after checking the repository source registry; this file
implements project-local projection modeling logic.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

The model is the adapter between the served projection contract and the imperative canvas renderer. It
is also where the state vocabulary crosses from the wire mirror into a colour-bearing one, so both
ends of that crossing are cited below: `LIFECYCLE_STATES`/`State` upstream, `constelColors` downstream.

| Finding | Anchor | Source |
| --- | --- | --- |
| `LIFECYCLE_STATES` is the `as const` tuple with `State` derived from it — the six states `CONSTEL_STATUS_BY_STATE` must be total over, and the list `model.test.ts` iterates instead of hand-copying. It is now COMPOSED from the two declared halves (`LIVE_STATES` + `TERMINAL_STATES`), so the six names are read off L42/L48. | `LIFECYCLE_STATES` | dashboard/src/types/projection.ts:13-13 |
| `WorkspaceProjection.activeWorktreeGroups` (worktree-group basenames with a live enclosure lifecycle) is the bounded set `activeTopologyInputs` filters on; `ProviderNode.worktreeGroup` is a basename while `EnclosureNode.worktreeGroup` is a full path. | `activeTopologyInputs` | dashboard/src/topology/model.ts:105-115 |
| `CONSTEL_STATUSES` + the derived `ConstelStatus`, the total `CONSTEL_STATUS_BY_STATE`, the declared `UNCLASSIFIED_STATUS`, the `STATUS_BY_DECLARED_STATE` partial read view, and `lifecycleStatus` with its inferred-degrades-healthy-only rule. | `lifecycleStatus` | dashboard/src/topology/model.ts:85-93 |
| `activeTopologyInputs` keeps only enclosures whose `groupKey(worktreeGroup)` ∈ `activeWorktreeGroups` and the lifecycles bound to them; `buildTopology` folds each enclosure's 1:1 lifecycle into the `wt` node via `lifecycleStatus` and parents providers by `groupKey` worktree group, then repo id, then workspace core. | `activeTopologyInputs`, `buildTopology`, `groupKey` | dashboard/src/topology/model.ts:99-99; dashboard/src/topology/model.ts:105-115; dashboard/src/topology/model.ts:117-221 |
| The backend exposes `activeWorktreeGroups` from the structural `active_worktree_groups` set via `project_workspace`. | `project_workspace` | mcp/src/agents_remember/observer/reducer.py:126-179 |
| The projection store passes that structural set through to the served projection. | `active_worktree_groups` | mcp/src/agents_remember/observer/projection_store.py:245-245 |
| `constelColors` keys the canvas palette by `ConstelStatus` declared here, and `col` indexes it with no `??` — the downstream half of the same grammar. | `constelColors` | dashboard/src/topology/constel.ts:31-39 |
| `model.test.ts` pins the grammar: totality over `LIFECYCLE_STATES`, the unclassified answer pinned to `UNCLASSIFIED_STATUS` by value, the inferred degrade, and `buildTopology` driven over the whole vocabulary. | "classifies every state the vocabulary declares" | dashboard/src/topology/model.test.ts:94-102 |
| `Topology.tsx` is the only caller: it runs `activeTopologyInputs` then `buildTopology` before handing the model to `mountConstel`. | `Topology` | dashboard/src/panels/Topology.tsx:82-155 |

## Cross-Repo References

No meaningful cross-repo references found. The behavior is within the `agents-remember` dashboard
projection/model/render boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->

- 2026-08-02T21:00:19+02:00 — 260731-EFA-L6 curator W2-B10: repaired 16 citation findings (8 reference rows); scoped recheck clean.

- 2026-08-01T10:30+02:00 — 260731-EFA-L4 curator (citation pass): `types/projection.ts` adopted the
  server's state partition — `LIVE_STATES` and `TERMINAL_STATES` are declared halves and
  `LIFECYCLE_STATES` is now `[...LIVE_STATES, ...TERMINAL_STATES] as const` — which moved every anchor
  below it. Re-anchored the two rows citing that file: `LIFECYCLE_STATES` L21-L30 → L42-L61 (the halves
  at L42/L48, the composed tuple at L59, `State` at L61) and noted that the six names are now read off
  the halves; `EnclosureNode`/`ProviderNode` L121-L154 → L156-L189 and
  `WorkspaceProjection.activeWorktreeGroups` L683-L684 → L711-L721. No body claim changed —
  `LIFECYCLE_STATES` is still an `as const` tuple with `State` derived from it.
- 2026-08-01T09:20+02:00 — 260731-EFA-L4 curator: documented the leaf's headline defect and its fix.
  `lifecycleStatus` was an if-chain covering five of six `LIFECYCLE_STATES` and returning `"ok"` for
  the rest, so an `awaiting-developer` lifecycle — the turn handed back to the developer — drew as a
  healthy constellation node. It is now four declarations: the `CONSTEL_STATUSES` tuple with
  `ConstelStatus` derived from it, the total `CONSTEL_STATUS_BY_STATE: Record<State, ConstelStatus>`
  (a seventh state stops the literal compiling), `UNCLASSIFIED_STATUS = "warn"`, and the
  `STATUS_BY_DECLARED_STATE: Partial<Record<string, ConstelStatus>>` read view that makes
  `?? UNCLASSIFIED_STATUS` load-bearing to `tsc`. `lifecycleStatus` is now exported, takes
  `Pick<LifecycleProjection, "state" | "inferred">`, and degrades only a healthy reading when
  `inferred`. Added the invariants (no unrecognised state may read `ok`; one classification path;
  inferred never upgrades) and rebuilt the Repo-Internal citations — the previous rows carried symbol
  names in the `Citations` column instead of line ranges, and are now exact ranges containing
  `LIFECYCLE_STATES`, `EnclosureNode`/`ProviderNode`, `CONSTEL_STATUS_BY_STATE`, `constelColors`, and
  `activeTopologyInputs`/`buildTopology` respectively. Verification metadata left pinned; closeout
  stamps the code commit.
- 2026-06-28T07:30+02:00 — Task 33: reshaped the model to an active-enclosure view. Removed the lifecycle/task
  rim (`task` kind + `RF.task` gone; `RF` is now `{repo:0.3, wt:0.62}`) and folded each enclosure's 1:1
  lifecycle (id/click-through, `lifecycleStatus`, `phase·state`) into the `wt` node. Added the exported
  pure `activeTopologyInputs` seam that filters to `activeWorktreeGroups` and drops orphan lifecycles, and
  a `groupKey` basename helper that normalises every worktree-group join — fixing a latent task-12-S1 bug
  where worktree providers fell back to the core (enclosure full-path key vs provider basename lookup
  never matched on real data). `repoKeys` no longer include lifecycle `repoId`; WORKSPACE sub-label is now
  `N checkouts · M active worktrees`; the `RANK` constant was removed with the rim. Verification metadata
  pinned until closeout stamps the code commit.
- 2026-06-23T22:31+02:00 — Clarified that provider satellites are binding projections: a single
  aggregate GrepAI instance can appear as repo-scoped target dots, while isolated worktree providers
  still orbit their worktree by `worktreeGroup`. Verification metadata pinned until closeout stamps the
  S2 code commit.
- 2026-06-23T21:46+02:00 — Task 12 S2: `buildTopology` now includes repo-covered workspace providers in
  the repo ring and parents providers by `worktreeGroup` first, then `repoId`, then workspace core. This
  lets CGC repo coverage orbit repo nodes while preserving S1 worktree-provider behavior. Verification
  metadata pinned until closeout stamps the S2 code commit.
- 2026-06-23T15:08+02:00 — Created for task 12 S1: documents the pure Topology model and the new
  provider-parenting rule where worktree-scoped providers orbit their owning worktree node via
  `worktreeGroup`; workspace providers intentionally remain on the workspace core until the backend
  per-repo projection slice lands. Verification metadata will be stamped at closeout.
