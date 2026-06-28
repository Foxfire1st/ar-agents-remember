# dashboard/src/topology/model.ts

| Field                  | Value                                       |
| ---------------------- | ------------------------------------------- |
| repository             | agents-remember                             |
| path                   | `dashboard/src/topology/model.ts`           |
| doc_type               | `file-level-onboarding`                     |
| lastUpdated            | 2026-06-23T22:31+02:00                      |
| lastVerifiedCommitHash |                                             `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`|
| lastVerifiedCommitDate |                                             2026-06-28T18:49:06+02:00|
| governingOverview      | `../overview.md`                            |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

`model.ts` builds the pure, deterministic data model that the Topology canvas renderer draws. It
translates observer projection nodes into a bounded radial constellation: workspace core → source
checkouts (inner ring) → **active** worktree enclosures (outer ring), with provider satellites attached
to the entity they are scoped to. The view shows live work only — there is **no separate lifecycle/task
rim**; each active enclosure node folds in its 1:1 lifecycle (id, status, phase·state).

## Code Commentary

### Logic

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

The file exports the model types/constants, the pure builder, and `activeTopologyInputs`. `ConstelNode.parent`
is an index into the returned node list, not an id string, because the imperative renderer performs
hot-path layout over the array. `rf` selects the ring radius for checkouts/enclosures (`RF = {repo, wt}`,
no task ring); providers use `rf: 0` and orbit their parent via `poff`.

### Invariants And Boundaries

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

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

The model is the adapter between the served projection contract and the imperative canvas renderer. The
focused unit test covers the provider parenting contract directly.

| Finding | Citations | Source Path |
| --- | --- | --- |
| `WorkspaceProjection.activeWorktreeGroups` (worktree-group basenames with a live enclosure lifecycle) is the bounded set `activeTopologyInputs` filters on; `ProviderNode.worktreeGroup` is a basename while `EnclosureNode.worktreeGroup` is a full path. | `activeWorktreeGroups`, `EnclosureNode`, `ProviderNode` | [types/projection.ts](../types/projection.ts) |
| `activeTopologyInputs` keeps only enclosures whose `groupKey(worktreeGroup)` ∈ `activeWorktreeGroups` and the lifecycles bound to them; `buildTopology` folds each enclosure's 1:1 lifecycle into the `wt` node and parents providers by `groupKey` worktree group, then repo id, then workspace core. | `activeTopologyInputs`, `buildTopology`, `groupKey` | [model.ts](model.ts) |
| The backend exposes `activeWorktreeGroups` from `active_enclosure_worktree_groups` (the same admission the Engine Room uses) via `project_workspace`. | `active_worktree_groups` param | [reducer.py](../../../mcp/src/agents_remember/observer/reducer.py); [projection_store.py](../../../mcp/src/agents_remember/observer/projection_store.py) |
| The canvas renderer draws checkout/enclosure rings + provider satellites (no task ring) and positions providers by orbiting their parent node. | ring guides, `layout` | [constel.ts](constel.ts) |
| The topology model test verifies `activeTopologyInputs` filtering, the lifecycle fold (no task nodes), the path-vs-basename provider join, and provider parenting/precedence. | `model.test.ts` | [model.test.ts](model.test.ts) |

## Cross-Repo References

No meaningful cross-repo references found. The behavior is within the `agents-remember` dashboard
projection/model/render boundary.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->

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
