# mcp/src/agents_remember/serving/scope.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/serving/scope.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-29T15:30+02:00                     |
| lastVerifiedCommitHash | `ad30dd38c3dcfa13fb85f44b281488499e92519a` |
| lastVerifiedCommitDate | 2026-07-03T08:10:19+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[overview.md](overview.md)

## Purpose

`scope.py` is the **shared browse-scope resolution + error map** for the read-only
serving APIs. It was extracted from `serving/files.py` (L1) at operations-integration
L3 so the Change-Set Viewer backend (`serving/changeset.py`) reuses one resolver and
one HTTP error idiom instead of a parallel copy. A `{repo, mainline|enclosure}` request
resolves to a frozen `FileScope` of roots; `run_scoped` runs a domain function over that
scope and maps domain errors to the serving status-string `JSONResponse` idiom.

## Code Commentary

### Logic

`resolve_scope(config, repo_id, scope_id) -> FileScope` (L107-L153) maps
`{repo, mainline|enclosure}` to a frozen `FileScope` (`code_root`,
`onboarding_root | None`, `memory_root | None`, `branch`, `contract_path`). The repo is
gated through `require_repo` (the allow-list authority — `AuthorityError` on an unknown
id). For an enclosure scope it finds the on-disk leaf contract whose `worktree_group`
basename matches and resolves against the contract; otherwise it resolves the mainline.
It then calls `resolve_coordination_context`, taking `code_worktree or
code_repository_root` as the code root, and **degrades to a code-only scope**
(`onboarding_root=None`) on `MissingMemoryError` rather than failing.

`run_scoped(op, config, repo_id, scope_id) -> Response` (L167-L185) is the error mapper
(formerly `files._run`): an unknown repo → `404 unknown-repo`, an unknown enclosure
(`_UnknownScope`, L66-L67) → `404 unknown-scope`, an out-of-root / absolute path
(`AuthorityError` from `confine_rel`) → `400 bad-path`, an absent file
(`FileNotFoundError`) → `404 not-found`; success returns the domain dict at 200.

`_iter_repo_contracts` (L84-L95) / `_find_enclosure_contract` (L98-L104) enumerate the
**active** leaf-enclosure contracts for a repo from
`iter_leaf_enclosure_contracts(coordination_root/"tasks")` — filtered to the allow-listed
`repo_name`, skipping `cleanup=="abandoned"` and any enclosure whose `code_worktree` no
longer exists, tolerating a malformed contract (`ContractError`/`OSError` → skip).
`_resolve_within(root, rel)` (L156-L164) is the per-call confinement: `""`/`"."` is the
root, everything else goes through `confine_rel` (so an absolute or escaping path is
rejected, never silently re-rooted). `language_for(path)` (L61-L63) maps a file extension
to the dashboard language id via `_LANG_BY_EXT` (`text` fallback).

### Conventions

`FileScope` is a frozen dataclass (L70-L81). The module imports the sidecar-pairing
confinement (`confine_rel`) from `kernel/sidecar_pairing.py` and the
`CoordinationContext` bridge from `kernel/coordination_context_resolver.py`; it owns no
HTTP route — only the scope/catalog resolution + the error mapping reused by the route
modules.

### Invariants And Boundaries

- **Security posture (Task-6):** read-only resolution; the repo allow-list is
  `config.allowed_repo_ids` via `require_repo`; every served path is confined to a
  resolved root via `confine_rel` (realpath-checked, symlink-safe).
- **Missing onboarding is never an error** — a memory-less repo resolves to a code-only
  scope (`onboarding_root=None`), never a failure.
- **Enclosure enumeration is on-disk + per-request**, not projection-derived, so a
  newly started or closed worktree resolves without a projector tick.
- Pure resolution: no domain events, no writes; `run_scoped` is the only HTTP shape here.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The L1 files API that now imports + re-exports these helpers. | [serving/files.py](agents-remember/mcp/src/agents_remember/serving/files.py) |
| The L3 change-set API that reuses `FileScope` / `resolve_scope` / `run_scoped` / `language_for`. | [serving/changeset.py](agents-remember/mcp/src/agents_remember/serving/changeset.py) |
| The shared path-confinement helper (`confine_rel`) the scope uses. | [kernel/sidecar_pairing.py](agents-remember/mcp/src/agents_remember/kernel/sidecar_pairing.py) |
| The scope resolver bridge + `MissingMemoryError`. | [coordination_context_resolver.py](agents-remember/mcp/src/agents_remember/kernel/coordination_context_resolver.py) |
| The repo allow-list authority guard (`require_repo`). | [controllers/_guards.py](agents-remember/mcp/src/agents_remember/controllers/_guards.py) |
| The leaf-enclosure contract enumerator the catalog walks. | [worktrees/task_resolver.py](agents-remember/mcp/src/agents_remember/worktrees/task_resolver.py) |
| The `WorktreeContract` (`code_worktree`, `worktree_group`, `cleanup`) + `load_contract`/`ContractError`. | [worktrees/worktree_contract.py](agents-remember/mcp/src/agents_remember/worktrees/worktree_contract.py) |
| The test asserting the extraction (files.py re-exports `FileScope`/`_resolve_within`). | [test_serving_changeset.py](agents-remember/mcp/tests/test_serving_changeset.py) |

## Update History

- 2026-06-29T15:30+02:00 — Created for operations-integration L3: extracted the shared browse-scope layer out of `serving/files.py` — `FileScope`, `resolve_scope`, the `run_scoped` error mapper (was `files._run`), `language_for`/`_LANG_BY_EXT` (was `files._language_for`), the `_iter_repo_contracts`/`_find_enclosure_contract` active-enclosure enumeration, and `_resolve_within` — so the L3 change-set backend (`serving/changeset.py`) reuses one resolver + one 404/400 error map. Behavior is identical to L1; `files.py` re-imports these. Verification metadata pinned to the task base until closeout stamps the L3 code commit.
