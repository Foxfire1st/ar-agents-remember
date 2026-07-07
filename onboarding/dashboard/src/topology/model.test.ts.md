# dashboard/src/topology/model.test.ts

| Field                  | Value                                       |
| ---------------------- | ------------------------------------------- |
| repository             | agents-remember                             |
| path                   | `dashboard/src/topology/model.test.ts`      |
| doc_type               | `file-level-onboarding`                     |
| lastUpdated            | 2026-07-06T03:20+02:00                      |
| lastVerifiedCommitHash |                                             `e358c4ac520d94ae2e597ae3cbe186e07a4d1063`|
| lastVerifiedCommitDate |                                             2026-07-07T05:26:14+02:00|
| governingOverview      | `../overview.md`                            |

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

## Code Commentary

### Logic

The test builds minimal `EnclosureNode` and `ProviderNode` fixtures and calls `buildTopology` directly.
It then inspects the returned `ConstelNode[]` instead of rendering a canvas. The assertions cover the
intended worktree join path, the missing-worktree fallback path, the aggregate workspace-provider path,
repo-scoped workspace provider parenting, and `worktreeGroup` precedence over `repoId`.

### Conventions

Tests stay at the pure-model boundary because `ConstelNode.parent` is the behavior contract that the
renderer consumes. Fixture helpers accept partial overrides so each test only names the field under
test.

### Invariants And Boundaries

- Tests must not depend on canvas rendering, layout timing, or browser animation state.
- The worktree-provider test must prove `ProviderNode.worktreeGroup` joins to `EnclosureNode.worktreeGroup`.
- The fallback, workspace, repo-scoped, and precedence cases must remain explicit so backend/provider
  projection changes cannot accidentally change topology parenting semantics.

### Todos

No open file-local todos.

## Docs References

No relevant external documentation was found after checking the repository source registry; this is a
project-local unit test.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

This test documents the behavioral contract of the pure topology builder.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The topology builder records worktree groups, includes repo-covered workspace providers in repo nodes, and parents providers by worktree group, repo id, or workspace core. | L49-L58; L80-L124 | [model.ts](model.ts) |
| The test fixtures and assertions cover matching worktree groups, missing groups, aggregate workspace providers, repo-scoped workspace providers, and worktreeGroup precedence. | L6-L100 | [model.test.ts](model.test.ts) |

## Cross-Repo References

No meaningful cross-repo references found. The test covers same-repository frontend model logic only.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Series-Contract Notes

Topology tests construct `EnclosureNode` fixtures with the new `enclosureId`, `leafId`, and `taskRoot` fields so provider-parenting expectations run against the current projection shape. Since 260703-L11 the fixture also carries the required existence-truth flags `codeWorktreeExists`/`memoryWorktreeExists` (defaulted `true`); the Topology itself keeps filtering on `activeWorktreeGroups`, not on these flags.

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->

- 2026-07-06T03:20+02:00 — 260703-L11: the `enclosure(...)` fixture defaults the new required
  `codeWorktreeExists`/`memoryWorktreeExists` flags to `true`, matching the projection contract; no
  assertion change — topology admission still keys on `activeWorktreeGroups`. Verification metadata
  pinned until closeout stamps the L11 commit.
- 2026-06-28T07:30+02:00 — Task 33: added an `activeTopologyInputs` describe (active-only inclusion,
  terminal/orphan exclusion), a lifecycle-fold test (enclosure node carries id/status/sub, no task-kind
  node), and a path-vs-basename provider-join test; added a `lifecycle()` fixture factory. Verification
  metadata pinned until closeout stamps the code commit.
- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: topology fixtures now include `enclosureId`, `leafId`, `taskRoot`, and the leaf `series-contract.md` enclosure path required by the projection schema. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-23T21:46+02:00 — Task 12 S2: extended pure-model coverage for repo-scoped workspace provider
  parenting and `worktreeGroup` precedence over `repoId`, while preserving S1 fallback/core behavior.
  Verification metadata pinned until closeout stamps the S2 code commit.
- 2026-06-23T15:08+02:00 — Created for task 12 S1: covers worktree-provider parenting, unmatched
  worktree fallback, and workspace-provider core parenting for `buildTopology`. Verification metadata
  will be stamped at closeout.
