# dashboard/src/topology/model.ts

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

Pure deterministic Topology model over pre-bound task worktree rows and unbound enclosures: workspace core → source checkouts → active worktrees. There is no separate task/session ring; a bound worktree carries its entry’s shared task status and exact selection key.

CONSTEL_STATUSES declares the canvas palette vocabulary. Unbound worktrees are idle; bound tones map wait to warn, gone to idle and others to ok. Task status is adapted through shared pageParts taskStatusKey/statusTone; this module has no separate lifecycle-state table or inferred-state degradation.

## Code Commentary

### Logic







`activeTopologyInputs(worktrees, activeWorktreeGroups)` filters by normalized worktree group. It does not reconstruct entry membership or match session identities; the caller supplies rows from selectWorktrees.

`buildTopology(worktrees)` deterministically builds workspace/repo/worktree nodes from supplied rows. Repo keys come from each enclosure’s repoName. A bound worktree’s node id is the opaque task entry selection; its status/sub-label use shared task grammar. Unbound worktrees have no invented task target. The workspace label retains checkout/active-worktree counts.

There is no provider ring. A bound worktree node’s `detail` carries the whole served detail of a limit: one line per limited seat, naming its role, agent, provider, window and exact reset. No node claims provider health, per-repo processes or per-root state.

**Worktree-group join — basename normalisation.** `EnclosureNode.worktreeGroup` is a full path, while
the `activeWorktreeGroups` set holds basenames. The `groupKey` helper (`group.split("/").pop()`)
normalises both sides of that join, and `activeTopologyInputs` is the only caller that joins on it. No
provider node carries a worktree group, so there is no second join to key.

### Conventions

Exports remain pure model types, CONSTEL_STATUSES, RF, activeTopologyInputs and buildTopology. ConstelNode.parent is an array index; RF has repo/wt only, with no provider orbit or offset field. No task ring or local lifecycle classification vocabulary is introduced.

### Invariants And Boundaries

- Build only supplied pre-bound/unbound worktree rows; active filtering remains separate.
- Shared task tone decides bound worktree colour without local lifecycle inference.
- The worktree node is the selectable leaf only when an entry is bound; no extra task ring exists.
- Every worktree-group join (enclosure↔active set) goes through `groupKey` so the
  path-vs-basename formats match.
- Node parenting is model-owned; `constel.ts` only draws the nodes around the parent index it receives.
- A worktree’s limit detail is the served seat text; it implies no per-root health and no engine of its own.
- This file must not read the store, DOM, canvas, or browser APIs.

### Todos

No open file-local todos.


**L184 — INV-XZYGEB.** This model chooses the label's text, so the no-clock departure from a countdown is realized here. The obligation this leaf records for this place is stated in the invariant named here; the card's earlier account of this file stands, and this paragraph adds what the change made true.

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
