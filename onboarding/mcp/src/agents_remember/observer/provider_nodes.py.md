# provider_nodes.py

| Field                  | Value                                             |
| ---------------------- | ------------------------------------------------- |
| repository             | agents-remember                                   |
| path                   | `mcp/src/agents_remember/observer/provider_nodes.py` |
| doc_type               | `file-level-onboarding`                           |
| lastUpdated            | 2026-06-27T23:08+02:00                            |
| lastVerifiedCommitHash |                                                   `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`|
| lastVerifiedCommitDate |                                                   2026-06-28T18:49:06+02:00|
| governingOverview      | `overview.md`                                     |

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

## Docs References

No relevant external documentation was found after checking the repository source
registry. This file implements project-local projection policy.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found after checking in-repo design docs for provider projection policy. | n/a | n/a |

## Repo-Internal References

The module consumes the provider current-state shape and emits the served projection
contract used by the dashboard topology.

| Finding | Citations | Source Path |
| --- | --- | --- |
| CGC current state stores per-repo watcher rows under `resources.watchers`, keyed by repo id. | L175-L198 | [providers/current_state.py](../../providers/current_state.py) |
| GrepAI current state persists configured repository memory-root targets as `targetRepos`. | L101-L105; L132-L172 | [providers/current_state.py](../../providers/current_state.py) |
| Isolated worktree GrepAI settings keep the aggregate multi-root provider shape while replacing only the active project root with the worktree memory root. | L36-L67; L146-L167 | [providers/grepai/isolated.py](../providers/grepai/isolated.py) |
| The isolated GrepAI test proves the active repo root points at the target memory worktree while an unrelated repo root stays on its source path. | L583-L657 | [test_provider_setup.py](../../../tests/test_provider_setup.py) |
| `workspace_provider_nodes` expands CGC watcher rows and generic `targetRepos`, but falls back to aggregate workspace provider nodes when evidence is absent. | L16-L39; L75-L177 | [provider_nodes.py](provider_nodes.py) |
| Worktree provider nodes carry `worktreeGroup` and `repoId` while workspace repo-covered provider nodes carry only `repoId`. | L42-L64; L109-L163 | [provider_nodes.py](provider_nodes.py) |
| `ProviderNode` is the served schema carrying scope, role, `repoId`, and `worktreeGroup`. | L139-L165 | [projection.py](projection.py) |

## Cross-Repo References

No meaningful cross-repo references found. The behavior is inside the same provider
current-state to observer projection boundary.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->

- 2026-06-27T23:08+02:00 — Task 31 provider-state honesty: worktree provider nodes now accept runtime summaries while preserving configured-only inventory as `ok=None`/`watcherUp=False`, preventing static provider-state files from masquerading as live readiness. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-23T22:31+02:00 — Clarified the Task 12 GrepAI distinction: `targetRepos` are addressable
  project targets inside an aggregate GrepAI instance, and worktree GrepAI keeps unrelated roots on
  their configured locations while swapping only the active root. Verification metadata will be stamped
  at closeout.
- 2026-06-23T22:09+02:00 — Correction: generic `targetRepos` now project repo-scoped workspace provider
  nodes, so GrepAI memory-root coverage becomes repo satellites when current state supplies the configured
  repo targets. The earlier initial entry below is superseded, not deleted. Verification metadata
  will be stamped at closeout.
- 2026-06-23T21:46+02:00 — Created for dashboard task 12 S2: extracted provider-node projection policy
  from `snapshots.py`, initially expanding CGC `resources.watchers` into repo-scoped workspace provider
  nodes. Later 22:09/22:31 entries document the GrepAI `targetRepos` correction. Verification metadata
  will be stamped at closeout.
