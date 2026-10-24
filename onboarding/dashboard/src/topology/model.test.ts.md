# dashboard/src/topology/model.test.ts

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

Pure Topology assertions filter server-admitted active owners, use native bound-task identity/status without a task ring, and build only workspace, checkout and enclosure rings. Provider satellites and their parenting cases are removed. Lifecycle classification suites are retired.

No lifecycleStatus totality/inferred/unclassified or lifecycle-vocabulary buildTopology cases remain.

## Code Commentary

### Logic

The test builds minimal `EnclosureNode` and native task-entry fixtures and calls `buildTopology` directly. It inspects returned nodes instead of rendering a canvas. The current cases assert only `ws`, `repo` and `wt` node kinds, no `poff` key, one checkout per repository with an active enclosure, and each enclosure parented to its own checkout. The separate limit case uses the hosted model-provider limit supplied on a task entry; that field does not restore search-provider nodes.

**Bound native task and active groups.**

Active groups come from the server. The bound paused entry pins its qualified key/title, worktree · paused, warn and no task ring; no lifecycle grammar is inferred.





### Conventions

Minimal typed enclosure/native-entry fixtures inspect returned node parents/identity and the served limit label, not canvas rendering or lifecycle vocabulary totality.

### Invariants And Boundaries

- Tests must not depend on canvas rendering, layout timing, or browser animation state.



- Search-provider satellites remain absent: the fixture result has only workspace, checkout and enclosure kinds, and no `poff` key.
- Every active enclosure is parented to a checkout node for its repository; repositories with no active enclosure add no checkout ring node.

### Todos

No open file-local todos.


**L184 — INV-XZYGEB.** The topology model is where the label's text is chosen, so its test holds the no-clock form. The obligation this leaf records for this place is stated in the invariant named here; the card's earlier account of this file stands, and this paragraph adds what the change made true.

## Evidence

### Docs References

No relevant external documentation was found after checking the repository source registry; this is a
project-local unit test.

No relevant external documentation found.

### Repo-Internal References

Pure native worktree/task identity, hosted-limit label, checkout-ring membership and enclosure-parenting contract; no search-provider satellites or lifecycle grammar.










### Cross-Repo References

No meaningful cross-repo references found. The test covers same-repository frontend model logic only.

No meaningful cross-repo references found.

## Series-Contract Notes

Topology tests construct `EnclosureNode` fixtures with `enclosureId`, `leafId` and `taskRoot` fields. Since 260703-L11 the fixture also carries the required existence-truth flags `codeWorktreeExists`/`memoryWorktreeExists` (defaulted `true`); active-group admission remains separate from those fixture flags. The current suite uses these fixtures for native task and checkout/enclosure identity, not former provider parenting.

## Historical provider-parenting test account

These former current claims are retained as history, not as instructions or present implementation evidence.

> Pure Topology assertions filter server-admitted active owners, use native bound-task identity/status without a task ring, and retain provider parenting by worktree group/repo/workspace. Lifecycle classification suites are retired.
>
> The test builds minimal `EnclosureNode` and `ProviderNode` fixtures and calls `buildTopology` directly.
> It then inspects the returned `ConstelNode[]` instead of rendering a canvas. The assertions cover the
> intended worktree join path, the missing-worktree fallback path, the aggregate workspace-provider path,
> repo-scoped workspace provider parenting, and `worktreeGroup` precedence over `repoId`.
>
> Minimal typed enclosure/provider/native-entry fixtures inspect returned node parents/identity, not canvas rendering or lifecycle vocabulary totality.
>
> - The worktree-provider test must prove `ProviderNode.worktreeGroup` joins to `EnclosureNode.worktreeGroup`.
> - The fallback, workspace, repo-scoped, and precedence cases must remain explicit so backend/provider
>   projection changes cannot accidentally change topology parenting semantics.
>
> Pure native worktree/task identity and provider-parenting contract; no lifecycle grammar.
>
> The provider-parenting fixtures and assertions: matching worktree groups, missing groups, aggregate workspace providers, repo-scoped workspace providers, and `worktreeGroup` precedence.
>
> Topology tests construct `EnclosureNode` fixtures with the new `enclosureId`, `leafId`, and `taskRoot` fields so provider-parenting expectations run against the current projection shape. Since 260703-L11 the fixture also carries the required existence-truth flags `codeWorktreeExists`/`memoryWorktreeExists` (defaulted `true`); the Topology itself keeps filtering on `activeWorktreeGroups`, not on these flags.

- The current topology tests cover native task/worktree identity and status, shared limits, active groups and repository parenting, and assert only ws/repo/wt node kinds with no provider satellites. [7]
