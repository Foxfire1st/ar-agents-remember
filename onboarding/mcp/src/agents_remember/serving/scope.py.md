# mcp/src/agents_remember/serving/scope.py

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

`resolve_scope(config, repo_id, scope_id) -> FileScope` (cit:([`resolve_scope`], mcp/src/agents_remember/serving/scope.py:166-215)) maps
`{repo, mainline|enclosure}` to a frozen `FileScope` (`code_root`,
`onboarding_root | None`, `memory_root | None`, `branch`, `contract_path`). The repo is
gated through `require_repo` (the allow-list authority — `AuthorityError` on an unknown
id). For an enclosure scope it finds the on-disk leaf contract whose `worktree_group`
basename matches and resolves against the contract; otherwise it resolves the mainline.
It then calls `resolve_coordination_context`, taking `code_worktree or
code_repository_root` as the code root, and **degrades to a code-only scope**
(`onboarding_root=None`) on `MissingMemoryError` rather than failing.

`run_scoped(op, config, repo_id, scope_id) -> Response` (cit:([`run_scoped`], mcp/src/agents_remember/serving/scope.py:229-249)) is the error mapper
(formerly `files._run`): an unknown repo → `404 unknown-repo`, an unknown enclosure
(`_UnknownScope` (cit:([`_UnknownScope`], mcp/src/agents_remember/serving/scope.py:104-105))) → `404 unknown-scope`, an out-of-root / absolute path
(`AuthorityError` from `confine_rel`) → `400 bad-path`, an absent file
(`FileNotFoundError`) → `404 not-found`; success returns the domain dict at 200.

cit:([`_iter_repo_contracts`], mcp/src/agents_remember/serving/scope.py:122-126) / cit:([`_find_enclosure_contract`], mcp/src/agents_remember/serving/scope.py:157-163) enumerate the
**active** leaf-enclosure contracts for a repo. The tasks-tree walk itself now lives in
cit:([`_iter_active_contracts`], mcp/src/agents_remember/serving/scope.py:129-154) — the L5I single-pass extraction — which reads
`iter_leaf_enclosure_contracts(coordination_root/"tasks")` ONCE, skipping
`cleanup=="abandoned"` and any enclosure whose `code_worktree` no longer exists and
tolerating a malformed contract (`ContractError`/`OSError` → skip); `_iter_repo_contracts`
filters that one pass to the requested `repo_name`.
The shared walk prunes notes and archives. Before liveness filtering, a parsed contract whose
task document resolves outside the repository tasks folder derived from its physical enclosure
position is skipped with a scope warning naming the contract; its recorded roots cannot admit it.
`_resolve_within(root, rel)` (cit:([`_resolve_within`], mcp/src/agents_remember/serving/scope.py:218-226)) is the per-call confinement: `""`/`"."` is the
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

`FileScope` is a frozen dataclass (cit:([`FileScope`], mcp/src/agents_remember/serving/scope.py:108-119)). The module imports the sidecar-pairing
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

## Evidence

### Repo-Internal References

- The L1 files API that now imports + re-exports these helpers. [1]

- The L3 change-set API imports and reuses FileScope, resolve_scope, run_scoped and language_for. [2]

- The shared path-confinement helper (`confine_rel`) the scope uses. [3]
- The scope resolver bridge + "MissingMemoryError,". [4]
- The repo allow-list authority guard (`require_repo`). [5]

- The catalog uses the notes/archive-excluding iterator and names foreign positional nonmembers before liveness filters. [6]


> Retained earlier citation wording: - WorktreeContract retains the code-worktree, group and cleanup fields; its loader and named error own parsing. [7]



## 260718-CHATS-L5I Current Delta

Repository scope discovery now supports the single-pass, repository-bucketed file listing used by the serving files API. It preserves repository ownership boundaries while eliminating repeated tree walks.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## 260731-EFA-L2 Current Delta

The coordination-context call packages `CoordinationHints`, `EnclosureSelector` and
`WorktreeContractReader` inside `request=CoordinationRequest(...)`. The resolved scope and its
missing-memory fallback are unchanged; loose `hints`/`selector` keywords are not the current call.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

- WorktreeContract retains the code-worktree, group and cleanup fields; its loader and named error own parsing.  Anchor: `WorktreeContract` `load_contract` `ContractError` [7]
