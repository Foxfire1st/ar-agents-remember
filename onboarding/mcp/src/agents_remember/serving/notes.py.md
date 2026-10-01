# mcp/src/agents_remember/serving/notes.py

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

### 260921-ICR-L55 Current Delta — The Listing Resolves Only Symlinks And Walks By Descriptor

The task reader fetches `GET /api/notes/list` every time a task opens, and a series' notes tree holds
thousands of files. The earlier walk ran three `realpath` calls on every entry: `child.resolve()`, then
`path_is_relative_to` resolving the entry and the root again. Each call `lstat`s every path component.
That was about 85% of the listing's cost, and because the work is pure Python between syscalls, a busy
server stretched it to seconds. `ICR-R24@v3` (leaf L55) bounds the listing to **one followed `stat` per
entry**. Path resolution is paid once for the root and once per symlink, whatever the number or size of
the notes. The wire response is unchanged, with one accepted exception described below. No cache, index
or store was added. A directory-mtime cache was considered and rejected: a note that grows in place
changes its size without changing any directory mtime, so a cache would serve stale sizes and break the
live refresh (`ICR-R17`).

How the walk works now:

- `list_notes` resolves the notes root once and opens it as a descriptor (`_DIR_OPEN` =
  `O_RDONLY|O_DIRECTORY|O_NOFOLLOW`). `_walk_notes` lists each directory with `os.scandir(dir_fd)` and
  collects the results in a `_NotesWalk` accumulator. A row's `path` is built from entry names
  (`prefix + name`), not from `relative_to`.
- **Only symlinks are confinement-checked** (`_confined_stat`). A symlink entry keeps the unchanged
  `resolve()` + `path_is_relative_to(…, root)` check, judged on its lexical path through the walk. A
  non-symlink child needs no check, because the walk only enters directories opened beneath the
  confined root. An escaping symlink is never listed. An entry whose stat fails is skipped.
- **Directories are entered through descriptors** (`_open_subdir`, `_walk_subdir`). A plain
  subdirectory is opened relative to its parent's descriptor. An in-root directory symlink is still
  listed under its own lexical path, as before. Its target is re-resolved, re-checked and then opened
  one component at a time from the root descriptor (`_open_below_root`). If a directory was swapped
  for a symlink or a file after the walk saw it, the open fails with `ELOOP`/`ENOTDIR`
  (`_SWAPPED_AWAY`), and the directory is refused rather than followed out of the root. Every other
  open error propagates, as the path-based walk's errors did. This hardening came from review finding
  L55-R1-F2. Under a real concurrent flip it measured 0 leaking listings per 20,000, against 107–156
  for the old walk.
- **The directory-first sort key** (`_is_dir`) treats a followed-stat failure the way `Path.is_dir()`
  did. `ENOENT`, `ENOTDIR`, `EBADF` and `ELOOP` (`_NOT_A_DIR`) mean "not a directory"; every other
  error propagates. So a looping symlink, or one that traverses a file, is skipped and never turns the
  whole listing into HTTP 500 (review finding L55-R1-F1).
- Only regular files are listed, after following an in-root symlink (`S_ISREG`). FIFOs, sockets and
  other non-regular entries are skipped, as before.

**The one accepted deviation from byte identity** (Architect rulings of 2026-09-28T16:30:31 and
16:55:00): a directory that is readable but not searchable (`r` without `x`) now lists without its
children and answers 200. The path-based walk answered HTTP 500 there. This applies whether the
listing reaches the directory directly or through an in-root symlink. It follows the listing's
existing policy of silently skipping unreadable entries. No corpus entry has that mode.

**Residuals the descriptor walk does not cover.** The comment above `_DIR_OPEN` states both.

- (a) If a directory is renamed out of the root while it is being listed, its own entries are still
  listed through the open descriptor. The path-based walk did not do this. It discloses nothing new:
  whoever can move that directory could equally place the same content inside the root.
- (b) A symlink's stat is taken during the sort (`DirEntry` caches it), before its path check. So a
  retarget in between can list one outside file's size under the in-root name. The path-based walk
  had the same single-entry window in the opposite order: check, then stat.

In both cases note reads stay confined by `confine_rel`.

This entry supersedes the earlier description on this card that every walked child is
realpath-checked.

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
serializes for you. The declaration remains the contract. The former broad conformance suite was removed in IAS testing cleanup; this card does not claim that it still validates emitted bodies. Strict model validation rejects undeclared keys when explicitly invoked.

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
`_walk_notes`. Within each directory, files sort before subfolders, by case-folded name. Each entry
is `{name, path (notes-root-relative posix), size, language}`, and the call returns
`{repo, master, notes, truncated}`. A **missing notes folder is an empty list, never an
error** (a young series without notes is normal). Symlink entries are realpath-checked against
the resolved root (`path_is_relative_to`), and a symlink escaping the notes tree is silently
skipped. Other children are confined because the walk enters directories only by descriptor,
beneath the root (see the L55 delta above). Directories deeper than `_MAX_LIST_DEPTH` (4) are
pruned with `truncated: true`, so the listing never lies about completeness. Depth counts the
lexical path, so an in-root directory symlink is listed, and pruned, at its own position.

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
- Every served path stays inside the series' notes root: `confine_rel` on reads, and on
  listing the symlink realpath check plus descriptor-only descent. The rest of the
  coordination tree (task docs, contracts, enclosures) is NOT reachable through this API. The
  listing's two residual windows are stated in the L55 delta above.
- The listing's cost is one followed `stat` per entry. Path resolution is paid once for the root
  and once per symlink, never per note. The listing never opens a note's content, and it keeps no
  state between requests. Keep all three: `mcp/tests/test_notes_listing.py` counts the `realpath`
  calls at two tree sizes and refuses any content open.
- Every directory is entered through `_open_subdir`. Descending any other way reopens symlink
  escape. Only `ELOOP`/`ENOTDIR` may be swallowed there, because widening that set would change
  the error answers the path-based walk gave (a mode-000 directory still answers 500). The sort
  key must keep `_NOT_A_DIR` parity with `Path.is_dir()`.
- A missing notes folder degrades to `[]`; a missing note file is `404 not-found`; the
  status idiom matches the files/change-set APIs — and since **260731-EFA-L4** that shared idiom
  is declared once as `SCOPED_READ_RESPONSES`, so a new status here means adding it to the shared
  table, not widening a per-route one.
- The declared models are the contract, not the runtime guard: these handlers return `Response`
  objects, so a key added to `list_notes` or `read_note` must land in `NotesListing` /
  `NoteContents` in the same change to keep the declared contract accurate.

## Evidence

### Cross-Repo References

No meaningful cross-repo references found.

### Repo-Internal References

- The app factory registers notes routes during app assembly and mounts static assets later; those calls are not an immediately adjacent pair. [1]
- The `confine_rel` realpath confinement this module reuses for reads. [2]
- The repo allow-list authority guard (`require_repo`). [3]
- `McpRuntimeConfig` (`coordination_root`, `allowed_repo_ids`) and `path_is_relative_to` provide configuration and path confinement. [4]
- `language_for` supplies the listing and read `language` field. [5]
- The changeset route's single-segment master confinement helper (moved to the new selection module by 260921-ICR-L13; `changeset.py` imports it). [6]
- The browser client for these endpoints. [7]
- The `list_notes` and `read_note` helper bodies: the listing opens the resolved root once as a descriptor and walks from it; the read confines through `confine_rel`. [8]
- The descriptor-open flags, the swap signature that refuses a directory, and the `Path.is_dir()`-parity errno set, with the source comment stating the two residual windows. [9]
- The per-listing accumulator: the real root and its descriptor, the rows, the prune flag. [10]
- The directory-first sort key that reads looping or file-traversing symlinks as "not a directory". [11]
- Symlink-only confinement: one followed `stat` per entry, and `resolve()` + `path_is_relative_to` only for a symlink. [12]
- Descriptor descent: a plain subdirectory opened relative to its parent, an in-root directory symlink re-resolved and opened component by component from the root, and only `ELOOP`/`ENOTDIR` refused. [13]
- The walk: `scandir` on the descriptor, files before folders, the depth cap, regular files only, row paths built from names. [14]
- The wire contract the listing must keep, unchanged by L55. [15]
- The module's own tests: exact wire bytes over every entry kind, the directory-swap refusal, a `realpath` count that does not grow with the tree, live refresh, and the refusal table. [16]
- The shared `SCOPED_READ_RESPONSES` refusal-table declaration. [17]
