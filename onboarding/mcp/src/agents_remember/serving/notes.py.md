# mcp/src/agents_remember/serving/notes.py

| Field                  | Value                                          |
| ---------------------- | ---------------------------------------------- |
| repository             | agents-remember                                |
| path                   | `mcp/src/agents_remember/serving/notes.py`     |
| doc_type               | `file-level-onboarding`                        |
| lastUpdated            | 2026-08-02T01:05+02:00                         |
| lastVerifiedCommitHash | `7af76249ff1aa728d34a6e81c5f09c8bcb797484`     |
| lastVerifiedCommitDate | 2026-08-09T02:17:45+02:00|
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

### 260731-EFA-L4 Current Delta — Both Routes Now Declare What They Answer With

`GET /api/notes/list` declares `response_model=NotesListing` and `GET /api/notes/read` declares
`response_model=NoteContents`, both under the shared `responses=SCOPED_READ_RESPONSES` table.
All three come from `serving/response_contract.py`, which is where this module's
one new import lives.

`SCOPED_READ_RESPONSES` is exactly the two statuses `_notes_json` can produce — 400
(`StatusRefusal`: `bad-request` from the single-segment `master` check, `bad-path` from
`AuthorityError` or the `ValueError` L9R-1 case) and 404 (`UnknownRepoRefusal |
UnknownScopeRefusal | MissingPathRefusal`: `unknown-repo` from `require_repo`, `not-found` from
`FileNotFoundError`). The table is shared with the files and change-set routes because the
refusal idiom is shared, not because it is boilerplate.

Nothing on the wire changed and nothing is validated at runtime: both handlers return a
`JSONResponse` they built themselves, and FastAPI applies `response_model` only to values it
serializes for you. The declaration is the contract;
`mcp/tests/test_serving_response_conformance.py` is the gate — it drives both routes through the
real app and validates the real body against these models, whose `extra="forbid"` makes an
undeclared key a failure.

This entry supersedes any earlier description in this sidecar that conflicts with the current
source behavior above; verification metadata stays pinned to the pre-commit source history until
closeout.

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
reader shows a placeholder, never raw bytes). Since 260703-L18 (finding 5) the cap is
applied through the shared `scope.decode_capped`, which cuts at a UTF-8 codepoint boundary
(backward-scan) — a multi-byte char straddling the 2-MiB cap no longer misdecodes an oversize
markdown note (the dominant type) into empty `binary`; it returns the first ~2 MiB with
`truncated: true`.

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
  status idiom matches the files/change-set APIs — and since **260731-EFA-L4** that shared idiom
  is declared once as `SCOPED_READ_RESPONSES`, so a new status here means adding it to the shared
  table, not widening a per-route one.
- The declared models are the contract, not the runtime guard: these handlers return `Response`
  objects, so a key added to `list_notes` or `read_note` must land in `NotesListing` /
  `NoteContents` in the same change or the conformance suite fails.

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The app factory registers notes routes during app assembly and mounts static assets later; those calls are not an immediately adjacent pair. | "def register_notes_routes(app: FastAPI, config: McpRuntimeConfig) -> None:", `mount_static` | mcp/src/agents_remember/serving/notes.py:168-168; mcp/src/agents_remember/serving/static.py:112-129 |
| The `confine_rel` realpath confinement this module reuses for reads. | `confine_rel` | mcp/src/agents_remember/kernel/sidecar_pairing.py:35-47 |
| The repo allow-list authority guard (`require_repo`). | `require_repo` | mcp/src/agents_remember/kernel/authority.py:16-24 |
| `McpRuntimeConfig` (`coordination_root`, `allowed_repo_ids`) and `path_is_relative_to` provide configuration and path confinement. | `McpRuntimeConfig`, `path_is_relative_to` | mcp/src/agents_remember/mcp/config.py:113-137; mcp/src/agents_remember/mcp/config.py:635-640 |
| `language_for` supplies the listing and read `language` field. | `language_for` | mcp/src/agents_remember/serving/scope.py:65-67 |
| The changeset route's single-segment master confinement helper. | `_master_task_root` | mcp/src/agents_remember/serving/changeset.py:145-149 |
| The browser client for these endpoints. | `notes` | dashboard/src/data/notes.ts:19-19 |
| The `list_notes` and `read_note` helper bodies. | `list_notes`, `read_note` | mcp/src/agents_remember/serving/notes.py:101-109; mcp/src/agents_remember/serving/notes.py:112-136 |
| The shared `SCOPED_READ_RESPONSES` refusal-table declaration. | `SCOPED_READ_RESPONSES` | mcp/src/agents_remember/serving/response_contract.py:1068-1074 |

## Update History

- 2026-08-04T11:42:15+02:00 — 260731-EFA-L6 S18-B04 — same-reviewer residual correction: narrowed rows 127-128 to the `list_notes`/
  `read_note` helper bodies and the shared refusal-table declaration.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-01T08:40+02:00 — 260731-EFA-L4 curator: recorded the two `response_model`
  declarations and the shared `SCOPED_READ_RESPONSES` table, mapping its 400/404
  entries onto the exact refusals `_notes_json` already produced (`bad-request`, `bad-path`,
  `unknown-repo`, `not-found`). Noted that FastAPI validates neither handler — both return a
  `JSONResponse` directly — so the gate is `test_serving_response_conformance.py`; added that to
  the boundaries and two reference rows. No wire change. Verification metadata pinned until
  closeout stamps the L4 commit.

- 2026-07-07T18:40+02:00 — 260703-L18 (review fix batch, finding 5): `read_note` now caps through the
  shared `scope.decode_capped`, cutting at a UTF-8 codepoint boundary so an oversize markdown note whose
  multi-byte char straddles the 2-MiB cap returns text + `truncated: true` instead of empty `binary`.
  Boundary test added to the notes suite. Verification metadata pinned until closeout stamps the L18 commit.

- 2026-07-06T09:30+02:00 — L9 adversarial-review follow-up (L9R-1): ValueError from Path.resolve() (null-byte input) now maps to 400 bad-path in the status mapper; regression test added. Verification metadata pinned until closeout stamps the L9 commit.

- 2026-07-06T01:10+02:00 — Created for agent-orchestration L9 (friction F-M): the read-only
  coordination-notes API (`/api/notes/list` + `/api/notes/read`) confined to
  `tasks/<repo>/<master>/notes/` via `require_repo` + single-segment `master` +
  `confine_rel`, with the missing-folder empty list, the honest depth-capped subfolder
  walk, and the size-capped binary-tolerant read. Registered in `create_app` before the
  static mount. Verification metadata pinned until closeout stamps the L9 commit.
