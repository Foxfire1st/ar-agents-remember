# dashboard/src/topology/model.test.ts

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

`model.test.ts` is focused Vitest coverage for the pure Topology model. It verifies provider
parenting (worktree-scoped → its enclosure, repo-scoped workspace → repo node, unmatched → workspace
core, `worktreeGroup` precedence) and, as of task 33, the active-enclosure reshape: an
`activeTopologyInputs` describe (active-only inclusion, terminal/orphan exclusion), a fold test (the
enclosure `wt` node carries its 1:1 lifecycle's id/status/sub and **no** `task`-kind node is emitted),
and a path-vs-basename provider-join test (enclosure full-path `worktreeGroup` joins a basename
provider `worktreeGroup`). A `lifecycle()` factory supplies `LifecycleProjection` fixtures.

Since 260731-EFA-L4 it also owns the **state → status grammar** coverage: a `lifecycleStatus`
describe and two `buildTopology` cases that drive the whole `LIFECYCLE_STATES` vocabulary rather than
hand-picking states. This is the file that could not see the leaf's headline defect, and the reason
is recorded in the source: it enumerated the one state it already knew about, so a classification
covering five of six states and answering `"ok"` for the sixth passed.

## Code Commentary

### Logic

The test builds minimal `EnclosureNode` and `ProviderNode` fixtures and calls `buildTopology` directly.
It then inspects the returned `ConstelNode[]` instead of rendering a canvas. The assertions cover the
intended worktree join path, the missing-worktree fallback path, the aggregate workspace-provider path,
repo-scoped workspace provider parenting, and `worktreeGroup` precedence over `repoId`.

**The `lifecycleStatus` describe (four cases).**

1. *classifies every state the vocabulary declares* — iterates `LIFECYCLE_STATES` and asserts each is
   a key of `CONSTEL_STATUS_BY_STATE`. `Record<State, ConstelStatus>` already fails `tsc -b` on a
   seventh state; this makes the same gap fail under vitest, so it is visible from either gate
   instead of only from the one someone remembered to run.
2. *classifies a state it has never heard of as the declared unclassified status* — the
   forward-compatibility case. It is pinned **to the value**, not to its negation: the comment records
   that `.not.toBe("ok")` was the whole assertion and that `undefined` satisfies it, so deleting
   `?? UNCLASSIFIED_STATUS` would leave both gates green while the `undefined` reached the renderer's
   palette. The case now asserts `CONSTEL_STATUSES` contains the answer (it is a status, not a hole),
   that it equals `UNCLASSIFIED_STATUS`, and that the declared value is `"warn"`.
3. *still classifies an unknown state when the reducer INFERRED it* — the degrade reads
   `declared === "ok"`, which is false for `undefined` as well as for `warn`, so that branch cannot
   tell "unclassified" from "classified" on its own. Pinned separately.
4. *degrades an inferred healthy state and leaves every other reading alone* — `running`+inferred →
   `warn`, `running` → `ok`, `blocked`+inferred → `crit`, `abandoned`+inferred → `idle`.

`fromANewerServer(state: string): State` is the named, single-site widening the two unknown-state
cases use. `State` is a closed union mirroring a bare `str` server-side, so the mirror is narrower
than the wire by construction; the helper exists so those two cases read as a forward-compatibility
check rather than as loose casts a reader could mistake for a banned pattern.

**Two `buildTopology` grammar cases.** *draws every state in the vocabulary with the status that state
declares* iterates `LIFECYCLE_STATES`, builds a topology per state, and asserts the `wt` node's status
equals `CONSTEL_STATUS_BY_STATE[state]` — which also pins that there is exactly one classification
path, since a second if-chain grown inside `buildTopology` would disagree with the declared grammar.
*does not render an awaiting-developer lifecycle as a healthy node* pins the reported defect by name:
`status` is not `"ok"`, is `"warn"`, and `sub` reads `build · awaiting-developer`.

### Conventions

Tests stay at the pure-model boundary because `ConstelNode.parent` is the behavior contract that the
renderer consumes. Fixture helpers accept partial overrides so each test only names the field under
test. **Iterate, never enumerate**: any assertion over the state vocabulary reads `LIFECYCLE_STATES`
rather than listing states, so a new state fails here instead of passing unnoticed. Assertions about
the unclassified answer are pinned to `UNCLASSIFIED_STATUS` by value — an assertion that only rules a
value out cannot notice the absence of a value at all.

### Invariants And Boundaries

- Tests must not depend on canvas rendering, layout timing, or browser animation state.
- No vocabulary may be hand-copied here. `LIFECYCLE_STATES` and `CONSTEL_STATUSES` are imported and
  iterated; a second local list is the failure mode this file was rewritten to remove.
- The unclassified case must assert the concrete value, not `.not.toBe("ok")`. The negation passes on
  `undefined`, which is precisely the value the fix exists to prevent.
- `fromANewerServer` is the only sanctioned widening in this file and must stay a bare token cast,
  never a shape.
- The worktree-provider test must prove `ProviderNode.worktreeGroup` joins to `EnclosureNode.worktreeGroup`.
- The fallback, workspace, repo-scoped, and precedence cases must remain explicit so backend/provider
  projection changes cannot accidentally change topology parenting semantics.

### Todos

No open file-local todos.

## Evidence

### Docs References

No relevant external documentation was found after checking the repository source registry; this is a
project-local unit test.

No relevant external documentation found.

### Repo-Internal References

This test documents the behavioral contract of the pure topology builder and, since 260731-EFA-L4,
the state → status grammar it reads from.

- The `lifecycleStatus` describe: totality over `LIFECYCLE_STATES`, the unclassified answer pinned to `UNCLASSIFIED_STATUS` by value, the same answer under `inferred`, and the healthy-only degrade. [1]
- `fromANewerServer` — the single named widening the two unknown-state cases share. [2]
- The two vocabulary-driven `buildTopology` cases: every state drawn with its declared status, and `awaiting-developer` explicitly not `"ok"`. [3]
- The grammar under test — `CONSTEL_STATUSES`, `CONSTEL_STATUS_BY_STATE`, `UNCLASSIFIED_STATUS`, `STATUS_BY_DECLARED_STATE`, `lifecycleStatus`. [4]
- The topology builder folds each enclosure's lifecycle through `lifecycleStatus` and parents providers by worktree group, repo id, or workspace core. [5]
- `LIFECYCLE_STATES` — the imported vocabulary the assertions iterate instead of restating; composed from `LIVE_STATES` (L42) + `TERMINAL_STATES` (L48), so the range holds all six names. [6]
- The provider-parenting fixtures and assertions: matching worktree groups, missing groups, aggregate workspace providers, repo-scoped workspace providers, and `worktreeGroup` precedence. [7]

### Cross-Repo References

No meaningful cross-repo references found. The test covers same-repository frontend model logic only.

No meaningful cross-repo references found.

## Series-Contract Notes

Topology tests construct `EnclosureNode` fixtures with the new `enclosureId`, `leafId`, and `taskRoot` fields so provider-parenting expectations run against the current projection shape. Since 260703-L11 the fixture also carries the required existence-truth flags `codeWorktreeExists`/`memoryWorktreeExists` (defaulted `true`); the Topology itself keeps filtering on `activeWorktreeGroups`, not on these flags.
