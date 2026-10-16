# dashboard/src/topology/model.ts

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

Pure deterministic Topology model over pre-bound task worktree rows and unbound enclosures: workspace core → source checkouts → active worktrees, with provider satellites. There is no separate task/session ring; a bound worktree carries its entry’s shared task status and exact selection key.

CONSTEL_STATUSES declares the canvas palette vocabulary. Unbound worktrees are idle; bound tones map wait to warn, gone to idle and others to ok. Task status is adapted through shared pageParts taskStatusKey/statusTone; this module has no separate lifecycle-state table or inferred-state degradation.

## Code Commentary

### Logic







`activeTopologyInputs(worktrees, activeWorktreeGroups)` filters by normalized worktree group. It does not reconstruct entry membership or match session identities; the caller supplies rows from selectWorktrees.

`buildTopology(worktrees, providers)` deterministically builds workspace/repo/worktree nodes from supplied rows. Repo keys come from enclosure repoName and repo-covered workspace providers. A bound worktree’s node id is the opaque task entry selection; its status/sub-label use shared task grammar. Unbound worktrees have no invented task target. The workspace label retains checkout/active-worktree counts.

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

Exports remain pure model types, CONSTEL_STATUSES, RF, activeTopologyInputs and buildTopology. ConstelNode.parent is an array index; RF has repo/wt only, providers orbit their parent via poff. No task ring or local lifecycle classification vocabulary is introduced.

### Invariants And Boundaries

- Build only supplied pre-bound/unbound worktree rows; active filtering remains separate.
- Shared task tone decides bound worktree colour without local lifecycle inference.
- The worktree node is the selectable leaf only when an entry is bound; no extra task ring exists.
- Every worktree-group join (enclosure↔provider, enclosure↔active set) goes through `groupKey` so the
  path-vs-basename formats match.
- Provider parenting is model-owned; `constel.ts` only draws providers around the parent index it receives.
- Provider dots express the strongest known topology binding. They do not imply separate per-repo
  provider processes or per-root health unless the backend projection exposes that.
- This file must not read the store, DOM, canvas, or browser APIs.

### Todos

No open file-local todos.

## Evidence

### Docs References

No relevant external documentation was found after checking the repository source registry; this file
implements project-local projection modeling logic.

No relevant external documentation found.

### Repo-Internal References





- The backend exposes `activeWorktreeGroups` from the structural `active_worktree_groups` set via `project_workspace`. [5]
- The projection store passes that structural set through to the served projection. [6]
- `constelColors` keys the canvas palette by `ConstelStatus` declared here, and `col` indexes it with no `??` — the downstream half of the same grammar. [7]
- `Topology.tsx` is the only caller: it runs `activeTopologyInputs` then `buildTopology` before handing the model to `mountConstel`. [9]

### Cross-Repo References

No meaningful cross-repo references found. The behavior is within the `agents-remember` dashboard
projection/model/render boundary.

No meaningful cross-repo references found.
