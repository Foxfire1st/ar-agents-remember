# mcp/src/agents_remember/worktrees/task_resolver.py

| Field                  | Value                                                   |
| ---------------------- | ------------------------------------------------------- |
| repository             | agents-remember                                         |
| path                   | `mcp/src/agents_remember/worktrees/task_resolver.py`     |
| doc_type               | `file-level-onboarding`                                 |
| lastUpdated            | 2026-09-14T19:00+02:00 |
| lastVerifiedCommitHash |                                                         `ea9cf0abeab4fe88961bda10b4f54d30266a9634`|
| lastVerifiedCommitDate |                                                         2026-09-17T23:56:19+02:00|
| governingOverview      | `../../../overview.md`                                  |

## Governing Overview

[mcp/ overview](../../../overview.md)

## Purpose

`task_resolver.py` centralizes task-name and leaf-enclosure path resolution for the series-contract
workflow. It gives application entry points, context resolution, worktree start/load paths, observer snapshots, and
finalization one shared way to find active root tasks, nested task roots, raw leaf
`enclosures/<leaf-id>/` contracts, and completed root-task archive targets. Canonical leaf-ref validation
and normalization live in `worktrees/leaf_refs.py`.

Since 260913-LCA-L5 it is also the **published import site** for the task-layout path vocabulary, not its
owner: the rules themselves (`SERIES_CONTRACT_FILENAME`, `ARCHIVE_DIR`, `ENCLOSURES_DIR`, `slugify`,
`series_contract_path`, `leaf_enclosure_dir`, `leaf_enclosure_path`, `is_archived_path`,
`is_enclosure_contract`, `iter_leaf_enclosure_contracts`) are defined in
`agents_remember.tasks.task_paths` and re-exported here under an explicit `__all__` (`:29-49`), so no
existing caller changes and there is still exactly one definition of each rule.

## Code Commentary

### Logic

The module **re-exports** the filesystem vocabulary for the task layout rather than defining it
(`:16-27`, `__all__` at `:29-49`): `series-contract.md`, `0_archive`, `enclosures/`, `slugify()`, the two
path builders and the two predicates now live in `tasks/task_paths.py`. What this module still defines is
task-*name* resolution: `task_folder_name()` / `legacy_task_folder_name()` and `task_root_candidates()`
keep legacy `-ar` task folders discoverable while the active schema moves to task-name folders.

`iter_active_series_contracts()` (`:79-85`) walks a repository's task tree for root-level
`series-contract.md` files and deliberately excludes archived paths and leaf enclosure contracts.
`resolve_active_task_root()` (`:88-114`) uses that iterator to resolve by `task_name`, optionally
constrained by `parent_task` for nested task folders. It raises `TaskResolutionError` (`:52-53`) when
multiple active task roots share the same name and falls back to the current/legacy deterministic path
only when no active contract exists and fallback is enabled.

`resolve_leaf_enclosure_contract()` (`:117-144`) resolves the parent task root first, then either returns
the requested raw leaf contract path or auto-selects the only leaf contract. Alias-aware legacy lookup
belongs to `leaf_refs.resolve_leaf_enclosure_contract_for_ref()` so this module stays focused on root and
contract path mechanics. Multiple leaves without an explicit `leaf_id` raise `TaskResolutionError`,
forcing callers to disambiguate without asking users for filesystem paths.

`archive_completed_root_task()` (`:147-184`) moves only completed root task folders into
`tasks/<repo>/0_archive/`. It skips nested leaf/task roots, skips roots that still have their own active
`series-contract.md`, blocks if the archive target already exists, and supports dry-run payloads for
finalize previews.

### Conventions

Callers pass human-facing `task_name` and optional `parent_task` / `leaf_id`; this module is the boundary
that turns those names into concrete paths. Archived task folders are excluded from active resolution.
The re-export list is explicit `__all__` rather than implicit star-import, so the published surface is
reviewable and a name cannot silently disappear from it.

### Invariants And Boundaries

- `0_archive` is never searched as active task material.
- Leaf contracts live under `enclosures/<leaf-id>/series-contract.md`; root series contracts live directly
  under their task root.
- **The path vocabulary is defined in `tasks/task_paths.py`, not here.** This module imports and
  re-exports it and redefines none of it: verified with `ast`, each of the ten moved names has exactly
  one definition site in all of `mcp/src` and it is in `tasks/task_paths.py`. The move exists to keep
  `layers.toml`'s `tasks`(9) < `worktrees`(10) order intact while the task package derives its own paths;
  changing a path rule is a change to `task_paths.py`, with this file following.
- Canonical leaf-ref validation, candidate reporting, and legacy alias policy live in `worktrees/leaf_refs.py`.
- User-facing resolution should prefer `task_name` plus optional `parent_task` / `leaf_id`, not raw paths.
- Archiving is root-task-only; leaf cleanup/finalization must not move a parent task folder.

## Docs References

No external documentation is needed for this local task-folder resolver.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation is needed for the local task resolver. | n/a | n/a |

## Repo-Internal References

Same-repository source and tests define the supported task-folder and series-contract behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| The re-export surface: this module publishes the task-layout vocabulary without defining it. | "from agents_remember.tasks.task_paths import ("; `__all__` | mcp/src/agents_remember/worktrees/task_resolver.py:16-27; mcp/src/agents_remember/worktrees/task_resolver.py:29-49 |
| The single definition of every path rule, which this module imports and redefines none of. | `slugify`; `series_contract_path`; `leaf_enclosure_path`; `is_archived_path`; `is_enclosure_contract`; `iter_leaf_enclosure_contracts` | mcp/src/agents_remember/tasks/task_paths.py:25-28; mcp/src/agents_remember/tasks/task_paths.py:31-34; mcp/src/agents_remember/tasks/task_paths.py:43-46; mcp/src/agents_remember/tasks/task_paths.py:49-50; mcp/src/agents_remember/tasks/task_paths.py:53-58; mcp/src/agents_remember/tasks/task_paths.py:61-66 |
| Task-name resolution, which this module still owns: current and legacy folder names plus the candidate list. | `task_folder_name`; `legacy_task_folder_name`; `task_root_candidates` | mcp/src/agents_remember/worktrees/task_resolver.py:56-57; mcp/src/agents_remember/worktrees/task_resolver.py:60-62; mcp/src/agents_remember/worktrees/task_resolver.py:73-76 |
| The error a resolution failure raises, and the current/legacy root builders. | `TaskResolutionError`; `task_root_for`; `legacy_task_root_for` | mcp/src/agents_remember/worktrees/task_resolver.py:52-53; mcp/src/agents_remember/worktrees/task_resolver.py:65-66; mcp/src/agents_remember/worktrees/task_resolver.py:69-70 |
| Active series discovery excludes archived task folders and leaf enclosure contracts; active task resolution can be constrained by `parent_task` and errors on ambiguous task names. | `iter_active_series_contracts`; `resolve_active_task_root` | mcp/src/agents_remember/worktrees/task_resolver.py:79-85; mcp/src/agents_remember/worktrees/task_resolver.py:88-114 |
| Leaf enclosure resolution selects an explicit leaf, auto-selects a single leaf, or errors when several leaves exist. | `resolve_leaf_enclosure_contract` | mcp/src/agents_remember/worktrees/task_resolver.py:117-144 |
| `leaf_refs.py` owns qualified/doc-id/legacy-stem leaf-ref validation and alias-aware legacy enclosure lookup. | "def resolve_leaf_ref" | mcp/src/agents_remember/worktrees/leaf_refs.py:88-88 |
| `start.py` uses the resolver to load a leaf contract from `task_name` / `leaf_id` and to build starts under the resolved parent task root. | "def load_contract_from_args" | mcp/src/agents_remember/worktrees/modules/start.py:115-115 |
| `finalize.py` calls `archive_completed_root_task` after cleanup so completed root tasks move to `0_archive` while leaf finalization skips that move. | `archive_completed_root_task` | mcp/src/agents_remember/worktrees/task_resolver.py:147-184 |
| Worktree support tests pin leaf-start contract placement and branch relationships through `series_contract_path` / `leaf_enclosure_path`. | `WorktreeSupportTests` | mcp/tests/test_worktree_support.py:708-783 |
| The package order that makes `tasks` the correct home for the vocabulary this module re-exports. | "a module in package P may import package Q only when rank(Q) < rank(P)" | layers.toml:25-25 |

## Cross-Repo References

No cross-repo boundary is required to explain this local resolver.

| Finding | Anchor | Source |
| --- | --- | --- |
| No sibling repository boundary is needed to explain this file. | n/a | n/a |

## Update History
- 2026-09-17T20:42:17+00:00: Generated citation repair: "def load_contract_from_args" repointed to mcp/src/agents_remember/worktrees/modules/start.py:115-115. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `WorktreeSupportTests` repointed to mcp/tests/test_worktree_support.py:708-783. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (residue citation pass): re-derived the source
  range of 1 claim(s) whose anchor no longer sat in its cited range and normalised 0 further
  range(s) from their anchors against the frozen source snapshot (`agents-remember memory-citations
  --fix --document`). 2 further claim(s) were declined because the solution they name no longer
  exists in the code tree, so their wording needs a reading curator; they are recorded in the pass
  report. No claim wording was changed to fit an anchor; every rewritten range was read back at its
  current position. Verification metadata remains closeout-owned.
- 2026-09-14T07:05+02:00 — 260913-LCA-L5 curator (uncommitted change set on `ar/260913-lca-l5-ar`, base
  `52875e7a`): corrected the ownership statement this card carried. The module no longer "owns the
  filesystem vocabulary for the new task layout": the ten path rules moved DOWN into the new
  `agents_remember.tasks.task_paths` (task domain) and this module imports and re-exports them under an
  explicit `__all__` of 19 names, redefining none — verified with `ast` over all of `mcp/src`, where each
  moved name has exactly one definition site and it is in `task_paths.py`. The move resolves a measured
  `layers.toml` inversion (`tasks` rank 9 reaching up into `worktrees` rank 10, plus a
  `tasks <-> worktrees` cycle the armed `layering` rail reports) introduced by the first revision of this
  change set; this module stays the published import site so its existing callers are unchanged. Recorded
  what it still owns (task-name resolution, active-series discovery, leaf-enclosure contract resolution,
  root-task archival) and re-derived every reference row against the current source with `ast`
  (`def slugify` 18 and `def series_contract_path` 47 now resolve into `tasks/task_paths.py`;
  `task_root_for` 33 → 65-66, `iter_active_series_contracts` → 79-85, `resolve_active_task_root` →
  88-114, `resolve_leaf_enclosure_contract` → 117-144, `archive_completed_root_task` unchanged at
  147-184). Verification metadata is **not** advanced: the code commit does not exist and closeout owns
  the stamp; no execution or acceptance claim.
- 2026-09-11T22:39:01+00:00: Generated citation repair: "def load_contract_from_args" repointed to mcp/src/agents_remember/worktrees/modules/start.py:105-105. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `WorktreeSupportTests` repointed to mcp/tests/test_worktree_support.py:831-906. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-09T12:22:46+00:00: Generated citation repair: "def load_contract_from_args" repointed to mcp/src/agents_remember/worktrees/modules/start.py:104-104. No content impact: mechanical anchor-range projection bound to citation source snapshot 06f99a0e57ce8b514dd7ed6685874da5285e3ec2e8c4a3f6a5d768b622094451; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-08T16:45:00+02:00 — CCR-L38 final preparation repair: repointed frozen-source citations after the final contract diagnostic; no behavioral prose change, no verification or acceptance claim.
- 2026-09-06T22:41:21+00:00: Generated citation repair: `WorktreeSupportTests` repointed to mcp/tests/test_worktree_support.py:948-1023. No content impact: mechanical anchor-range projection bound to citation source snapshot 250eac92295fa399589ccf1c9726bfb4cd28a1a0b20dca126769403fba09b52d; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B24 curator: replaced the `n/a` rows with exact
  anchors, rebound the archive row to the definition, and converted the history parity citation;
  exact non-fixing check returns zero findings.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 1 cross-file line citation. The two parity
  tests the row names now read at cit:([`ResolverCliTests`], mcp/tests/test_resolver_parity.py:56-251) —
  cit:([`test_parent_task_disambiguates_nested_task_roots`], mcp/tests/test_resolver_parity.py:155-210) and
  `test_active_series_discovery_excludes_archive` (L212-L251, which asserts
  `iter_active_series_contracts` skips the archived folder and that `resolve_active_task_root` raises
  `TaskResolutionError`). Was L146-L234.
- 2026-07-07T20:50+02:00 — 260707-HFX-L4: kept this module focused on active task root, raw leaf
  enclosure path, and root-task archive resolution after the qualified leaf-ref resolver moved to
  `worktrees/leaf_refs.py`. Verification metadata pinned until closeout stamps the 260707-HFX-L4 commit.
- 2026-06-24T06:26+02:00 — Created for the series-contract task resolver: documents active task-name
  resolution, nested parent disambiguation, leaf enclosure contract lookup, archive exclusion, and completed
  root-task archival. Verification metadata will be stamped during closeout after the new source file is
  committed.
