# mcp/src/agents_remember/serving/files.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/serving/files.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-07T18:40+02:00                     |
| lastVerifiedCommitHash | `575a9a44b71910d151c878eda4da4ebf32bef1cb` |
| lastVerifiedCommitDate | 2026-07-07T01:41:35+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[overview.md](overview.md)

## Purpose

`files.py` is the read-only **files API** (L1 of the operations-integration
series): the serving-layer bridge from the dashboard to the kernel
`CoordinationContext`. It lets the File Viewer (L2) and the Change-Set Viewer
(L3/L4) enumerate repositories and their `{mainline + active worktree
enclosures}`, list a scoped directory level (code + paired onboarding), read one
file's content + onboarding metadata, and resolve the 1:1 code↔onboarding sidecar
pairing in both directions. It is the first serving module to resolve a
`CoordinationContext` (the rest of `serving/` resolves only
`coordination_root`/`workspace_root`).

## Code Commentary

### Logic

**Operations-integration L3** extracted the shared scope layer (`FileScope`,
`resolve_scope`, the `run_scoped` error mapper [was `_run`], `language_for` [was
`_language_for`], `_iter_repo_contracts`/`_find_enclosure_contract`, `_resolve_within`,
`_LANG_BY_EXT`) into the sibling `serving/scope.py` so the L3 change-set backend reuses
it. `files.py` now imports them from `.scope` and **re-exports** `FileScope` +
`_resolve_within` for existing callers/tests. The behaviour described below is unchanged
— it is the same code, now shared with `serving/changeset.py`.

`register_files_routes(app, config)` registers four GET routes and **must** be
called before the greedy static `/` mount in `serving/app.py` (it is, at the tail
of `create_app`). Routes: `GET /api/files/repos` (catalog), `/api/files/list`,
`/api/files/read`, `/api/files/onboarding?direction=forward|reverse`. Each route is
a thin closure over `run_scoped` (in `serving/scope.py`), which resolves the scope and maps domain
errors to the serving status-string `JSONResponse` idiom: an unknown repo →
`404 unknown-repo`, an unknown enclosure → `404 unknown-scope`, an out-of-root /
absolute path → `400 bad-path`, an absent file → `404 not-found`. Success returns a
plain camelCase dict at 200.

`resolve_scope(config, repo_id, scope_id)` maps `{repo, mainline|enclosure}` to a
frozen `FileScope` (`code_root`, `onboarding_root | None`, `memory_root | None`,
branch, contract). The repo is gated through `require_repo` (the allow-list
authority — `AuthorityError` on an unknown id). For an enclosure scope it finds the
on-disk leaf contract whose `worktree_group` basename matches and resolves against
the contract; otherwise it resolves the mainline. It then calls
`resolve_coordination_context`, taking `code_worktree or code_repository_root` as
the code root. **If the repo has no AR memory** (`MissingMemoryError`), it degrades
to a code-only scope (`onboarding_root=None`) rather than failing — code stays
browsable and onboarding resolves uniformly "missing".

`list_repos(config)` is the catalog: every `config.allowed_repo_ids` entry with its
mainline (always) and its active enclosures, enumerated **per request** from
`iter_leaf_enclosure_contracts(coordination_root/"tasks")` via `_iter_repo_contracts`
— filtered to the allow-listed `repo_name`, skipping `cleanup=="abandoned"` and any
enclosure whose `code_worktree` no longer exists, and tolerating a malformed
contract (`ContractError`/`OSError` → skip, never abort).

`list_dir(scope, rel_dir)` lazily lists one level: code children from `code_root`
(each file annotated with `language` and `hasSidecar` via `route_sidecar_status`)
plus the parallel onboarding children from `onboarding_root` when present.
`read_file(scope, rel)` serves a file's content (capped at `_MAX_FILE_BYTES` = 2
MiB with a `truncated` flag; a non-UTF-8 file degrades to `language:"binary"`,
empty content) — since 260703-L18 (finding 5) the cap goes through the shared
`scope.decode_capped`, cutting at a UTF-8 codepoint boundary so a multi-byte char
straddling the cap returns the first ~2 MiB + `truncated:true` instead of empty
`binary` — and `_onboarding_meta` (the drift-bearing
`lastVerifiedCommitHash`/`Date` when a sidecar is present, else `status:"missing"`).
`resolve_onboarding` (forward) returns a code path's sidecar status + body;
`resolve_partner` (reverse) maps a sidecar to its partner code path (with an
`exists` flag for orphans) or classifies an overview-without-code node. An
overview/entities/index doc has **no code partner**, so the reverse node now also
carries its own `"body"` (via `_onboarding_doc_body`) — the File Viewer renders that
markdown directly instead of showing an empty "no code partner" placeholder, so a
route overview is readable, not just an unopenable tree leaf.
`_onboarding_doc_body(scope, rel)` reads that raw text from the onboarding root with the
same guards as `read_file` — confined through `_resolve_within`, capped at `_MAX_FILE_BYTES`
via the same `scope.decode_capped` codepoint-boundary cut, and binary-tolerant — returning
`None` for a missing / unreadable / non-UTF-8 file (the reader then falls back to the
placeholder) and `None` when the scope has no onboarding root.
`_resolve_within(root, rel)` is the per-call confinement: `""`/`"."` is the root,
everything else goes through `confine_rel` (so an absolute or escaping path is
rejected, never silently re-rooted).

### Invariants And Boundaries

- **Security posture (Task-6):** GET-only, read-only, 127.0.0.1-bound, no
  auth/CORS added. The repo allow-list is `config.allowed_repo_ids` via
  `require_repo`; a `repo_name` off a contract that is not allow-listed is never
  trusted. Every served path is confined to a resolved root via `confine_rel` —
  realpath-checked, symlink-safe — so no traversal escapes a code/onboarding root.
- **Missing onboarding is never an error.** A code file with no sidecar →
  `status:"missing"` (the placeholder the File Viewer renders); a repo with no AR
  memory degrades to code-only browsing rather than a 409 that would blank the
  scope. `MissingMemoryError` is a repo-level condition (no durable memory exists),
  never raised per-file.
- **Routes register before the static mount.** The `/` `StaticFiles` mount is
  greedy; `/api/files/*` must be registered first or the SPA index swallows them.
- **The pairing logic is shared, not re-derived.** All sidecar resolution +
  confinement comes from `kernel/sidecar_pairing.py`; this module owns only the
  scope/catalog resolution, the HTTP shape, and the read cap.
- **Enclosure enumeration is on-disk + per-request**, not projection-derived, so a
  newly started or closed worktree appears without a projector tick.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The shared scope layer (`FileScope`, `resolve_scope`, `run_scoped`, `language_for`, `_resolve_within`) extracted to and imported from here (L3). | [serving/scope.py](agents-remember/mcp/src/agents_remember/serving/scope.py) |
| The app factory that calls `register_files_routes(app, config)` immediately before `mount_static`. | [serving/app.py](agents-remember/mcp/src/agents_remember/serving/app.py) |
| The shared, side-effect-free sidecar pairing + path-confinement helpers this module reuses. | [kernel/sidecar_pairing.py](agents-remember/mcp/src/agents_remember/kernel/sidecar_pairing.py) |
| The scope resolver + `CoordinationContext`/`MissingMemoryError` bridged here. | [coordination_context_resolver.py](agents-remember/mcp/src/agents_remember/kernel/coordination_context_resolver.py) |
| The repo allow-list authority guard (`require_repo` → `RepositoryScope`). | [controllers/_guards.py](agents-remember/mcp/src/agents_remember/controllers/_guards.py) |
| `McpRuntimeConfig` (`allowed_repo_ids`, `repositories`) + the `path_is_relative_to` guard. | [mcp/config.py](agents-remember/mcp/src/agents_remember/mcp/config.py) |
| The leaf-enclosure contract enumerator the catalog walks. | [worktrees/task_resolver.py](agents-remember/mcp/src/agents_remember/worktrees/task_resolver.py) |
| The `WorktreeContract` (`code_worktree`, `worktree_group`, `cleanup`) + `load_contract`/`ContractError`. | [worktrees/worktree_contract.py](agents-remember/mcp/src/agents_remember/worktrees/worktree_contract.py) |
| The `table_metadata` drift reader + the `mirror_onboarding_path` sidecar mapper. | [kernel/onboarding_doc.py](agents-remember/mcp/src/agents_remember/kernel/onboarding_doc.py) |
| The test suite for this module. | [test_serving_files.py](agents-remember/mcp/tests/test_serving_files.py) |

## Update History

- 2026-07-07T18:40+02:00 — 260703-L18 (review fix batch, finding 5): `read_file` and
  `_onboarding_doc_body` now cap through the shared `scope.decode_capped`, which cuts at a UTF-8
  codepoint boundary — an oversize text file (or overview) whose multi-byte char straddles the 2-MiB
  cap returns its first ~2 MiB with `truncated:true` instead of misdecoding into empty `binary`.
  Boundary test added to `test_serving_files.py`. Verification metadata pinned until closeout stamps
  the L18 commit.
- 2026-06-30T00:00:00+02:00 — operations-integration L5: the reverse-pairing overview node now carries its own
  markdown `body` via the new `_onboarding_doc_body(scope, rel)` (confined, size-capped,
  binary-tolerant; `None` on missing/unreadable/binary or no onboarding root), so the File Viewer can
  render an opened route overview's prose instead of an empty "no code partner" placeholder. Pinned in
  `test_serving_files.py` (the partnerless overview asserts the markdown `body`). Verification metadata
  pinned until closeout stamps the L5 code commit.
- 2026-06-29T15:30+02:00 — operations-integration L3: extracted the shared scope layer (`FileScope`, `resolve_scope`, the `run_scoped` error mapper [was `_run`], `language_for` [was `_language_for`], `_iter_repo_contracts`/`_find_enclosure_contract`, `_resolve_within`, `_LANG_BY_EXT`) into the sibling `serving/scope.py` so the L3 change-set backend (`serving/changeset.py`) reuses one resolver + 404/400 error map; `files.py` now imports them from `.scope` and re-exports `FileScope` + `_resolve_within` for existing callers/tests (behavior-preserving — L1 tests unchanged). Verification metadata pinned to the task base until closeout stamps the L3 code commit.
- 2026-06-28T22:41+02:00 — Created for operations-integration L1: the read-only `serving/files.py` files API (repo/enclosure catalog, list-dir, read-file, forward/reverse onboarding pairing) bridging the dashboard to the kernel `CoordinationContext`, registered before the static mount in `create_app`. Reuses `kernel/sidecar_pairing.py`; degrades to code-only browsing for memory-less repos (missing onboarding is not an error); confines every path with `confine_rel`. Verification metadata pinned until closeout stamps the L1 code commit.
