# mcp/src/agents_remember/serving/notes.py

## Governing Overview

[overview.md](overview.md)

## Purpose

`notes.py` is the read-only **coordination-notes API** (agent-orchestration L9, closing
friction F-M): three endpoints that surface the coordination `notes/` tree — design
records, the friction ledger, worker turn reports, adversarial verdicts — for one series
master, `tasks/<repo>/<master>/notes/` under the coordination root. Since 260928-MIK-L126
the server answers **one folder per request**: the whole-tree `GET /api/notes/list` walk is
removed with no caller remaining. Before it, the files
API served only repo roots + worktree enclosures and the task reader rendered only
`task.json` content, so a task doc's references to notes files were inert strings. It
feeds the task reader's notes line (`dashboard/src/panels/TaskNotes.tsx` via
`dashboard/src/data/notes.ts` and `dashboard/src/data/taskReports.ts`).

## Code Commentary

### 260928-MIK-L126 Current Delta — The Server Answers One Folder Per Request

The task reader fetched `GET /api/notes/list` every time a task opened, and the walk of the
whole tree grew with the notes folder: 72,875 rows in 15 MB on the measured master. `MIK-R126@v1`
(rule 2) replaces it with **one folder per request**. `list_folder` reads only the requested
folder — never its subfolders, so the work does not grow with the number of files under the
notes root — and answers entries in a stable total order (directories first, case-folded name,
exact name breaking ties) in parts of `_FOLDER_PAGE` (200), with `remaining` for the next part.
A missing folder answers empty with the server's reason, never an error. The whole-tree answer
is removed and no caller of it remains.

Confinement is preserved in the one-folder shape:

- The requested folder is opened through held descriptors without following symlinks
  (`_open_confined_dir`): a directory swapped for an escaping link after confinement reads as
  gone instead of listing outside entries (review finding L126-CODE-01). A vanished folder, a
  file path, or an unreadable folder answers empty with its reason (L126-CODE-04); every other
  error propagates, including EACCES from opening or listing the folder itself — a
  searchable-but-unreadable folder and a neither-read-nor-search folder keep the baseline
  500. The one exception is a readable-but-unsearchable folder: listing succeeds and each
  entry's stat failure is skipped, never listed (`_folder_row`), so it answers present
  with no children — zero rows with exists true (INV-413DC8XE).
- Each row is examined without following symlinks (`_folder_row`): only a symlink can escape,
  and an escaping link is never listed while an in-root alias still lists under its own name.
  Non-regular entries are skipped.
- Bare-name resolution never returns an escaping link (`_confined_is_file`, L126-CODE-01).
- Reference resolution is per-token and bounded by reference count (`resolve_notes_references`):
  a token naming an existing note by path (with or without the `notes/` prefix) wins; a bare
  filename resolves only at the notes root, never by a tree walk (Parent ruling L126-REFERENCE-FORMAT-RULING:
  nested-only bare names stay text, L126-CODE-05). Anything else stays plain text.

This entry supersedes the L55 descriptor-walk description on this card: the walk, its sort key,
its per-entry stat economy and its residuals describe a removed endpoint.

### 260731-EFA-L4 Current Delta — Both Routes Now Declare What They Answer With (L126: three routes)

`GET /api/notes/folder` declares `response_model=NotesFolder`, `POST /api/notes/resolve`
declares `response_model=NotesResolutions`, and `GET /api/notes/read` declares
`response_model=NoteContents`, all under the shared `responses=SCOPED_READ_RESPONSES` table.
All come from `serving/response_contract.py`, which is where this module's
one new import lives.

`SCOPED_READ_RESPONSES` is exactly the two statuses `_notes_json` can produce — 400
(`StatusRefusal`: `bad-request` from the single-segment `master` check, `bad-path` from
`AuthorityError` or the `ValueError` L9R-1 case) and 404 (`UnknownRepoRefusal |
UnknownScopeRefusal | MissingPathRefusal`: `unknown-repo` from `require_repo`, `not-found` from
`FileNotFoundError`). The table is shared with the files and change-set routes because the
refusal idiom is shared, not because it is boilerplate.

Nothing on the wire changed and nothing is validated at runtime: both handlers return a
`JSONResponse` they built themselves, and FastAPI applies `response_model` only to values it
serializes for you. The declaration remains the contract. The former broad conformance suite was removed in IAS testing cleanup; this card does not claim that it still validates emitted bodies. Strict model validation rejects undeclared keys when explicitly invoked.

This entry supersedes any earlier description in this sidecar that conflicts with the current
source behavior above; verification metadata stays pinned to the pre-commit source history until
closeout.

### Logic

L9 review follow-up (L9R-1): the shared status mapper now also catches `ValueError` from `Path.resolve()` (e.g. an embedded null byte in `path`) and answers `400 bad-path` instead of an uncaught 500 — malformed input gets the same wire answer as a confinement breach.

`register_notes_routes(app, config)` registers three routes and **must** be called
before the greedy static `/` mount (it is, after `register_changeset_routes` in
`serving/app.py`): `GET /api/notes/folder?repo&master&path&offset`,
`POST /api/notes/resolve` (a `references` list with `repo`/`master`), and `GET
/api/notes/read?repo&master&path`. All go through `_notes_json` — it validates the
`{repo, master}` selector (unknown repo → `404 unknown-repo` via `require_repo`; a
non-single-segment `master` → `400 bad-request` via `_is_single_segment`, the change-set
`master`-key confinement idiom) and maps domain errors to the shared wire idiom
(`AuthorityError` → `400 bad-path`, `FileNotFoundError` → `404 not-found`) so
`data/files.ts`'s error mapping applies unchanged. A negative folder offset is a
`ValueError` → `400 bad-path`: it names no path at all.

`list_folder(config, repo_id, master, rel, offset)` confines `rel` (empty at the root),
answers one part of that folder's entries with `total`/`offset`/`limit`/`remaining`, and
a missing notes folder or gone folder as empty with `exists: false` and the reason —
never an error. Each entry is `{name, path (notes-root-relative posix), kind, size,
language}`; row `path`s are prefixed after the stable sort so independently fetched
offset parts never depend on readdir order (L126-CODE-02).

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

- No mutation surface of any kind: folder and read are GET, resolve is POST with a
  references body, nothing writes.
- Every served path stays inside the series' notes root: `confine_rel` on reads and
  reference paths, held-descriptor opens on folders. The rest of the
  coordination tree (task docs, contracts, enclosures) is NOT reachable through this API.
- A folder answer never grows with the tree: one folder read, at most 200 rows per part,
  reference work bounded by reference count. The folder answer keeps no
  state between requests. Keep both: `mcp/tests/test_notes_folder.py` proves the parts,
  the stable order and the tree-size-independent work, and
  `mcp/tests/test_generated_master_selection_cost.py` proves the bounded selection set
  on the generated master.
- Every directory is entered through `_open_confined_dir`. Descending any other way reopens symlink
  escape. Only swapped-away/vanished/file-path failures answer empty-with-reason; every other
  error propagates.
- A missing notes folder or gone folder answers empty with `exists: false` and the reason;
  a missing note file is `404 not-found`; the
  status idiom matches the files/change-set APIs — and since **260731-EFA-L4** that shared idiom
  is declared once as `SCOPED_READ_RESPONSES`, so a new status here means adding it to the shared
  table, not widening a per-route one.
- The declared models are the contract, not the runtime guard: these handlers return `Response`
  objects, so a key added to `list_folder`, `resolve_notes_references` or `read_note` must land in
  `NotesFolder` / `NotesResolutions` / `NoteContents` in the same change to keep the declared contract accurate.

## Evidence

### Cross-Repo References

No meaningful cross-repo references found.

### Repo-Internal References


- The app factory registers notes routes during app assembly. [1]


- The `confine_rel` realpath confinement this module reuses for reads. [2]


- `McpRuntimeConfig` and `path_is_relative_to` provide configuration and path confinement. [4]


- The browser client for these endpoints. [7]

- The repo allow-list authority guard (`require_repo`). [3]
- `language_for` supplies the listing and read `language` field. [5]
- The changeset route's single-segment master confinement helper (moved to the new selection module by 260921-ICR-L13; `changeset.py` imports it). [6]


- One folder answers in parts with total, offset, limit and remaining. [8]


- Folders open through held descriptors without following symlinks. [9]


- Rows sort directories first, case-folded, exact name breaking ties. [10]


- Each row is examined without following symlinks. [11]


- Bare names never resolve an escaping link. [12]


- Each reference resolves to a notes path or null in one request. [13]


- Bare filenames resolve only at the notes root. [14]


- The part ceiling bounds every folder answer. [15]


- The module's folder tests prove parts, order, confinement and bounds. [16]


- A readable-but-unsearchable folder answers present with no children since failed entry stats are skipped; EACCES from the folder open or listing itself propagates (searchable-unreadable and neither keep baseline 500). [18]

- The shared `SCOPED_READ_RESPONSES` refusal-table declaration. [17]
