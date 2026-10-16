# dashboard/src/topology/model.test.ts

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

Pure Topology assertions filter server-admitted active owners, use native bound-task identity/status without a task ring, and retain provider parenting by worktree group/repo/workspace. Lifecycle classification suites are retired.

No lifecycleStatus totality/inferred/unclassified or lifecycle-vocabulary buildTopology cases remain.

## Code Commentary

### Logic

The test builds minimal `EnclosureNode` and `ProviderNode` fixtures and calls `buildTopology` directly.
It then inspects the returned `ConstelNode[]` instead of rendering a canvas. The assertions cover the
intended worktree join path, the missing-worktree fallback path, the aggregate workspace-provider path,
repo-scoped workspace provider parenting, and `worktreeGroup` precedence over `repoId`.

**Bound native task and active groups.**

Active groups come from the server. The bound paused entry pins its qualified key/title, worktree · paused, warn and no task ring; no lifecycle grammar is inferred.





### Conventions

Minimal typed enclosure/provider/native-entry fixtures inspect returned node parents/identity, not canvas rendering or lifecycle vocabulary totality.

### Invariants And Boundaries

- Tests must not depend on canvas rendering, layout timing, or browser animation state.



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

Pure native worktree/task identity and provider-parenting contract; no lifecycle grammar.





- The provider-parenting fixtures and assertions: matching worktree groups, missing groups, aggregate workspace providers, repo-scoped workspace providers, and `worktreeGroup` precedence. [7]

### Cross-Repo References

No meaningful cross-repo references found. The test covers same-repository frontend model logic only.

No meaningful cross-repo references found.

## Series-Contract Notes

Topology tests construct `EnclosureNode` fixtures with the new `enclosureId`, `leafId`, and `taskRoot` fields so provider-parenting expectations run against the current projection shape. Since 260703-L11 the fixture also carries the required existence-truth flags `codeWorktreeExists`/`memoryWorktreeExists` (defaulted `true`); the Topology itself keeps filtering on `activeWorktreeGroups`, not on these flags.
