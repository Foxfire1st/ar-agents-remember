# provider_nodes.py

## Governing Overview

[observer overview](overview.md)

## Purpose

`provider_nodes.py` owns the conversion from provider current-state payloads into
served `ProviderNode` objects. It keeps provider projection policy out of
`snapshots.py`, so the snapshot reader remains the file-I/O edge and this module
owns the repo/worktree binding rules.

## Code Commentary

### Logic

`workspace_provider_nodes(providers, *, stale_seconds)` iterates the provider
snapshot map and projects workspace-scoped nodes. CodeGraphContext providers are
special only when the snapshot contains repo watcher evidence: `_cgc_watchers`,
`_repo_entries`, and `_cgc_repo_provider_node` expand `resources.watchers` into one
workspace-scoped `ProviderNode` per repo, with ids shaped as
`<provider-id>:<repo-id>` and `repoId` set for topology parenting. When CGC watcher
evidence is missing or unusable, the provider falls back to a single aggregate
workspace node.

Other workspace providers can also project repo-scoped nodes when current state
declares explicit `targetRepos`. `_target_repo_provider_nodes`,
`_target_repo_ids`, and `_target_repo_provider_node` turn each declared repo target
into a `<provider-id>:<repo-id>` node using the provider-level state, watcher, and
indexing values. This is what lets GrepAI memory roots become repo satellites while
keeping providers without target evidence aggregate. The split is about target
addressability, not process cardinality: one GrepAI provider instance can aggregate
multiple repository memory projects while still exposing per-project targets.

`worktree_provider_node(provider_id, *, group, repo_id, stale_seconds, runtime=None)`
projects one member of an isolated worktree provider stack. Static inventory without
runtime evidence now remains `configured` with `ok=None` and `watcherUp=False`;
Docker-backed runtime summaries can lift the node to ready/degraded/failed by
supplying state, ok, watcher, and indexing facts. Those nodes stay worktree-scoped,
carry the owning `repoId`, and set `worktreeGroup` as the enclosure join key. For
GrepAI, the isolated worktree settings keep the multi-root provider shape and swap
only the active project root to the task memory worktree; unrelated project roots
remain configured to their default locations.

`provider_role(provider_id)` centralizes the simple role convention used by both
workspace and worktree provider nodes: GrepAI/memory providers are `memory`; CGC and
other code providers are `code`.

### Conventions

- CGC repo coverage is emitted only from persisted watcher evidence. Generic workspace
  repo coverage is emitted only from persisted `targetRepos`. The module does not
  infer repo coverage from provider names or workspace strings.
- GrepAI repo coverage comes from current state's configured repository memory-root
  targets. If that field is absent, GrepAI remains an aggregate workspace node.
  When it is present, the topology can draw one dot per addressable target even
  though the runtime provider instance remains aggregate.
- Worktree provider nodes keep their `@<group>` id suffix; workspace CGC repo nodes
  use `:<repoId>` to distinguish coverage rows from aggregate provider ids.
- `ok=None` means no runtime truth was observed for a configured worktree provider;
  consumers must not treat configured inventory as live readiness.

### Invariants And Boundaries

- The module is pure projection policy: it receives already-read dictionaries and
  returns `ProviderNode` models. It does not read files, call providers, or touch git.
- A malformed or absent CGC watcher map, or absent generic `targetRepos`, degrades to
  the pre-existing aggregate workspace provider node instead of creating fake repo
  satellites.
- `worktreeGroup` remains the strongest binding for isolated worktree providers;
  `repoId` is coverage metadata for workspace providers and owning-repo metadata for
  worktree providers.
- Provider nodes are topology bindings. They must not imply that provider-level
  readiness has become per-root readiness unless a provider exposes that health.

### Todos

No file-local todos.

## Evidence

### Docs References

No relevant external documentation was found after checking the repository source
registry. This file implements project-local projection policy.

No relevant external documentation found after checking in-repo design docs for provider projection policy.

### Repo-Internal References

The module consumes the provider current-state shape and emits the served projection
contract used by the dashboard topology.

- CGC current state stores per-repo watcher rows under `resources.watchers`, keyed by repo id. [1]
- GrepAI current state persists configured repository memory-root targets as `targetRepos`. [2]
- Isolated worktree GrepAI settings keep the aggregate multi-root provider shape while replacing only the active project root with the worktree memory root. [3]
- `workspace_provider_nodes` expands CGC watcher rows and generic `targetRepos`, but falls back to aggregate workspace provider nodes when evidence is absent. [4]
- Worktree provider nodes carry `worktreeGroup` and `repoId` while workspace repo-covered provider nodes carry only `repoId`. [5]
- `ProviderNode` is the served schema carrying scope, role, `repoId`, and `worktreeGroup`. [6]

### Cross-Repo References

No meaningful cross-repo references found. The behavior is inside the same provider
current-state to observer projection boundary.

No meaningful cross-repo references found.
