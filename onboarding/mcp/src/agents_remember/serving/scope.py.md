# mcp/src/agents_remember/serving/scope.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/serving/scope.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-02T01:05+02:00                     |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb` |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[overview.md](overview.md)

## Purpose

`scope.py` is the **shared browse-scope resolution + error map** for the read-only
serving APIs. It was extracted from `serving/files.py` (cit:([`resolve_scope`], mcp/src/agents_remember/serving/files.py:18-18)) at operations-integration
L3 so the Change-Set Viewer backend (`serving/changeset.py`) reuses one resolver and
one HTTP error idiom instead of a parallel copy. A `{repo, mainline|enclosure}` request
resolves to a frozen `FileScope` of roots; `run_scoped` runs a domain function over that
scope and maps domain errors to the serving status-string `JSONResponse` idiom.

## Code Commentary

### Logic

L9 review ride-along (L9R-1): the files-API status mapper now also catches `ValueError` from `Path.resolve()` (e.g. an embedded null byte) and answers `400 bad-path` — the notes API inherited its uncaught-500 idiom from here, so both were fixed in the same pass.

`resolve_scope(config, repo_id, scope_id) -> FileScope` (cit:([`resolve_scope`], mcp/src/agents_remember/serving/scope.py:147-193)) maps
`{repo, mainline|enclosure}` to a frozen `FileScope` (`code_root`,
`onboarding_root | None`, `memory_root | None`, `branch`, `contract_path`). The repo is
gated through `require_repo` (the allow-list authority — `AuthorityError` on an unknown
id). For an enclosure scope it finds the on-disk leaf contract whose `worktree_group`
basename matches and resolves against the contract; otherwise it resolves the mainline.
It then calls `resolve_coordination_context`, taking `code_worktree or
code_repository_root` as the code root, and **degrades to a code-only scope**
(`onboarding_root=None`) on `MissingMemoryError` rather than failing.

`run_scoped(op, config, repo_id, scope_id) -> Response` (cit:([`run_scoped`], mcp/src/agents_remember/serving/scope.py:207-227)) is the error mapper
(formerly `files._run`): an unknown repo → `404 unknown-repo`, an unknown enclosure
(`_UnknownScope` (cit:([`_UnknownScope`], mcp/src/agents_remember/serving/scope.py:98-99))) → `404 unknown-scope`, an out-of-root / absolute path
(`AuthorityError` from `confine_rel`) → `400 bad-path`, an absent file
(`FileNotFoundError`) → `404 not-found`; success returns the domain dict at 200.

cit:([`_iter_repo_contracts`], mcp/src/agents_remember/serving/scope.py:116-120) / cit:([`_find_enclosure_contract`], mcp/src/agents_remember/serving/scope.py:138-144) enumerate the
**active** leaf-enclosure contracts for a repo. The tasks-tree walk itself now lives in
cit:([`_iter_active_contracts`], mcp/src/agents_remember/serving/scope.py:117-135) — the L5I single-pass extraction — which reads
`iter_leaf_enclosure_contracts(coordination_root/"tasks")` ONCE, skipping
`cleanup=="abandoned"` and any enclosure whose `code_worktree` no longer exists and
tolerating a malformed contract (`ContractError`/`OSError` → skip); `_iter_repo_contracts`
filters that one pass to the requested `repo_name`.
`_resolve_within(root, rel)` (cit:([`_resolve_within`], mcp/src/agents_remember/serving/scope.py:205-213)) is the per-call confinement: `""`/`"."` is the
root, everything else goes through `confine_rel` (so an absolute or escaping path is
rejected, never silently re-rooted). `language_for(path)` maps a file extension
to the dashboard language id via `_LANG_BY_EXT` (`text` fallback). `decode_capped(raw, cap)
-> (text, truncated)` is the shared read-cap decoder (260703-L18 finding 5): it decodes the
first `cap` bytes as UTF-8 but backward-scans off any partial trailing character first (UTF-8
continuation bytes are `0b10xxxxxx`, a character is ≤4 bytes, so it steps `end` back ≤3 bytes
to a lead byte). This keeps a multi-byte character straddling the cap from raising
`UnicodeDecodeError` and misreporting an oversize TEXT file as empty `binary`; genuinely
non-UTF-8 content still raises (the callers keep classifying that as binary). Both
`serving/notes.py::read_note` and `serving/files.py::read_file`/`_onboarding_doc_body` call it,
staying in lockstep.

### Conventions

`FileScope` is a frozen dataclass (cit:([`FileScope`], mcp/src/agents_remember/serving/scope.py:96-107)). The module imports the sidecar-pairing
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

| Finding | Anchor | Source |
| --- | --- | --- |
| The L1 files API that now imports + re-exports these helpers. | `resolve_scope` | mcp/src/agents_remember/serving/files.py:18-18 |
| The L3 change-set API that reuses `FileScope` / `resolve_scope` / `run_scoped` / `language_for`. | "from agents_remember.serving.scope import FileScope" | mcp/src/agents_remember/serving/changeset.py:46-46 |
| The shared path-confinement helper (`confine_rel`) the scope uses. | `confine_rel` | mcp/src/agents_remember/kernel/sidecar_pairing.py:35-47 |
| The scope resolver bridge + "MissingMemoryError,". | "_resolver.resolve_coordination_context" | mcp/src/agents_remember/kernel/coordination_context_resolver.py:131-146 |
| The repo allow-list authority guard (`require_repo`). | `require_repo` | mcp/src/agents_remember/kernel/authority.py:16-24 |
| The leaf-enclosure contract enumerator the catalog walks. | `iter_leaf_enclosure_contracts` | mcp/src/agents_remember/worktrees/task_resolver.py:80-85 |
| The `WorktreeContract` (`code_worktree`, `worktree_group`, `cleanup`) + `load_contract`/`ContractError`. | `WorktreeContract`; `load_contract`; `ContractError` | mcp/src/agents_remember/worktrees/worktree_contract.py:91-92; mcp/src/agents_remember/worktrees/worktree_contract.py:230-285; mcp/src/agents_remember/worktrees/worktree_contract.py:436-469 |
| The test asserting the extraction (files.py re-exports `FileScope`/`_resolve_within`). | `test_scope_module_exposes_resolver_and_runner` | mcp/tests/test_serving_changeset.py:791-797 |

## 260718-CHATS-L5I Current Delta

Repository scope discovery now supports the single-pass, repository-bucketed file listing used by the serving files API. It preserves repository ownership boundaries while eliminating repeated tree walks.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## 260731-EFA-L2 Current Delta

The coordination-context call now passes the kernel's two parameter objects instead of two loose
keywords: `resolve_coordination_context(..., hints=CoordinationHints(coordination_root=…),
selector=EnclosureSelector(contract_path=…))`. The resolved scope and its fallbacks are unchanged.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## Update History

- 2026-08-02T23:59:26+02:00 — L6 Wave 2 duplicate-range correction: removed 4 repeated path:start-end Citation objects from 1 same-claim citation group(s) at card line(s) 97; retained the first occurrence/order, all non-repeated anchor coverage and source ranges; scoped non-fixing result 0.
- 2026-08-02T20:43+02:00 — W2-B08: anchored 6 scope-module reference claims with exact resolver, contract, and test anchors; ranges remain generated by the scoped fixer. Verification metadata stays pinned until closeout.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-31T17:48+02:00 — 260731-EFA-L2 curator: re-derived 3 stale self-citations and corrected
  where the enclosure walk lives. The L5I single-pass extraction moved the tasks-tree walk and the
  abandoned/worktree-gone/malformed skips out of `_iter_repo_contracts` into `_iter_active_contracts`
  (cit:([`_iter_active_contracts`], mcp/src/agents_remember/serving/scope.py:117-135)); `_iter_repo_contracts` now only filters that one pass by
  `repo_name`. The current self-citations for the moved scope helpers are
  cit:([`_find_enclosure_contract`, `FileScope`, `_UnknownScope`, `resolve_scope`, `_resolve_within`, `run_scoped`], mcp/src/agents_remember/serving/scope.py:98-99; mcp/src/agents_remember/serving/scope.py:102-113; mcp/src/agents_remember/serving/scope.py:144-150; mcp/src/agents_remember/serving/scope.py:153-202; mcp/src/agents_remember/serving/scope.py:205-213; mcp/src/agents_remember/serving/scope.py:216-236). Behaviour is unchanged; ranges are generated by the W2-B08 scoped fixer.
- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator: recorded the `CoordinationHints` / `EnclosureSelector` call shape into the kernel resolver.
- 2026-07-24T13:18:47Z — 260718-CHATS-L5I curator: corrected the source-side behavior record for the current backend/shared delta and preserved the pre-commit verification stamp.

- 2026-07-07T18:40+02:00 — 260703-L18 (review fix batch, finding 5): added the shared
  `decode_capped(raw, cap)` helper — a codepoint-boundary read cap (backward-scan ≤3 bytes) so a
  multi-byte char straddling the 2-MiB cap no longer misdecodes an oversize text/markdown file into
  empty `binary`. `read_note`, `read_file`, and `_onboarding_doc_body` now share it (lockstep).
  Boundary tests live in the notes + files suites. Verification metadata pinned until closeout stamps
  the L18 commit.

- 2026-07-06T09:30+02:00 — L9 adversarial-review ride-along (L9R-1): ValueError (null-byte path) now maps to 400 bad-path in the shared scope status mapper; regression test added. Verification metadata pinned until closeout stamps the L9 commit.

- 2026-06-29T15:30+02:00 — Created for operations-integration L3: extracted the shared browse-scope layer out of `serving/files.py` — `FileScope`, `resolve_scope`, the `run_scoped` error mapper (was `files._run`), `language_for`/`_LANG_BY_EXT` (was `files._language_for`), the `_iter_repo_contracts`/`_find_enclosure_contract` active-enclosure enumeration, and `_resolve_within` — so the L3 change-set backend (`serving/changeset.py`) reuses one resolver + one 404/400 error map. Behavior is identical to L1; `files.py` re-imports these. Verification metadata pinned to the task base until closeout stamps the L3 code commit.
