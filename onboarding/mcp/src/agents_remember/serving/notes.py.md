# mcp/src/agents_remember/serving/notes.py

| Field                  | Value                                          |
| ---------------------- | ---------------------------------------------- |
| repository             | agents-remember                                |
| path                   | `mcp/src/agents_remember/serving/notes.py`     |
| doc_type               | `file-level-onboarding`                        |
| lastUpdated            | 2026-07-06T09:30+02:00                         |
| lastVerifiedCommitHash | `7c63f64935f362c418e9852bf3820a769a437f45`     |
| lastVerifiedCommitDate | 2026-07-06T01:34:58+02:00|
| governingOverview      | `overview.md`                                  |

## Governing Overview

[overview.md](overview.md)

## Purpose

`notes.py` is the read-only **coordination-notes API** (agent-orchestration L9, closing
friction F-M): two GET endpoints that surface the coordination `notes/` tree — design
records, the friction ledger, worker turn reports, adversarial verdicts — for one series
master, `tasks/<repo>/<master>/notes/` under the coordination root. Before it, the files
API served only repo roots + worktree enclosures and the task reader rendered only
`task.json` content, so a task doc's references to notes files were inert strings. It
feeds the task reader's notes view (`dashboard/src/panels/TaskNotes.tsx` via
`dashboard/src/data/notes.ts`).

## Code Commentary

### Logic

L9 review follow-up (L9R-1): the shared status mapper now also catches `ValueError` from `Path.resolve()` (e.g. an embedded null byte in `path`) and answers `400 bad-path` instead of an uncaught 500 — malformed input gets the same wire answer as a confinement breach.

`register_notes_routes(app, config)` registers two GET routes and **must** be called
before the greedy static `/` mount (it is, after `register_changeset_routes` in
`serving/app.py`): `GET /api/notes/list?repo&master` and `GET
/api/notes/read?repo&master&path`. Both go through `_notes_json` — it validates the
`{repo, master}` selector (unknown repo → `404 unknown-repo` via `require_repo`; a
non-single-segment `master` → `400 bad-request` via `_is_single_segment`, the change-set
`master`-key confinement idiom) and maps domain errors to the shared wire idiom
(`AuthorityError` → `400 bad-path`, `FileNotFoundError` → `404 not-found`) so
`data/files.ts`'s error mapping applies unchanged.

`list_notes(config, repo_id, master)` walks the series' notes root recursively via
`_walk_notes` — per directory files-before-subfolders, each entry
`{name, path (notes-root-relative posix), size, language}` — and returns
`{repo, master, notes, truncated}`. A **missing notes folder is an empty list, never an
error** (a young series without notes is normal). Every walked child is
realpath-checked against the resolved root (`path_is_relative_to`): a symlink escaping
the notes tree is silently skipped, and directories deeper than `_MAX_LIST_DEPTH` (4)
are pruned with `truncated: true` so the listing never lies about completeness.

`read_note(config, repo_id, master, rel)` confines `rel` with `confine_rel` (the realpath
idiom: `..` traversal, absolute paths, and symlink escapes all raise `AuthorityError`),
then serves the file size-capped (`_MAX_FILE_BYTES` = 2 MiB, mirroring `serving/files.py`)
and binary-tolerant (`UnicodeDecodeError` → `language: "binary"`, empty content — the
reader shows a placeholder, never raw bytes).

### Conventions

GET-only, read-only, 127.0.0.1-bound, no auth/CORS — the L1 files-API posture. The repo
comes from `config.allowed_repo_ids` (`require_repo`); the notes root is derived, never
wire-supplied: `coordination_root / "tasks" / repo_id / master / "notes"` with `master`
confined to one honest path segment.

### Invariants And Boundaries

- No mutation surface of any kind: both routes are GET, nothing writes.
- Every served path stays inside the series' notes root (`confine_rel` on reads, the
  per-child realpath check on listing) — the rest of the coordination tree (task docs,
  contracts, enclosures) is NOT reachable through this API.
- A missing notes folder degrades to `[]`; a missing note file is `404 not-found`; the
  status idiom matches the files/change-set APIs.

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The API reads only the local coordination tree; nothing crosses repositories. | — | — |

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The app factory that calls `register_notes_routes(app, config)` immediately before `mount_static`. | [serving/app.py](agents-remember/mcp/src/agents_remember/serving/app.py) |
| The `confine_rel` realpath confinement this module reuses for reads. | [kernel/sidecar_pairing.py](agents-remember/mcp/src/agents_remember/kernel/sidecar_pairing.py) |
| The repo allow-list authority guard (`require_repo`). | [controllers/_guards.py](agents-remember/mcp/src/agents_remember/controllers/_guards.py) |
| `McpRuntimeConfig` (`coordination_root`, `allowed_repo_ids`) + `path_is_relative_to`. | [mcp/config.py](agents-remember/mcp/src/agents_remember/mcp/config.py) |
| `language_for`, reused for the listing + read `language` field. | [serving/scope.py](agents-remember/mcp/src/agents_remember/serving/scope.py) |
| The same single-segment `master` confinement idiom on the change-set routes. | [serving/changeset.py](agents-remember/mcp/src/agents_remember/serving/changeset.py) |
| The browser client for these endpoints. | [data/notes.ts](agents-remember/dashboard/src/data/notes.ts) |
| The test suite for this module (API-layer coverage). | [test_serving_notes.py](agents-remember/mcp/tests/test_serving_notes.py) |

## Update History

- 2026-07-06T09:30+02:00 — L9 adversarial-review follow-up (L9R-1): ValueError from Path.resolve() (null-byte input) now maps to 400 bad-path in the status mapper; regression test added. Verification metadata pinned until closeout stamps the L9 commit.

- 2026-07-06T01:10+02:00 — Created for agent-orchestration L9 (friction F-M): the read-only
  coordination-notes API (`/api/notes/list` + `/api/notes/read`) confined to
  `tasks/<repo>/<master>/notes/` via `require_repo` + single-segment `master` +
  `confine_rel`, with the missing-folder empty list, the honest depth-capped subfolder
  walk, and the size-capped binary-tolerant read. Registered in `create_app` before the
  static mount. Verification metadata pinned until closeout stamps the L9 commit.
