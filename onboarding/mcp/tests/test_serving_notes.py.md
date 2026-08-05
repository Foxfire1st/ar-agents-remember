# test_serving_notes.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/tests/test_serving_notes.py`          |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-07T18:40+02:00                     |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d` |
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
| governingOverview      | `../overview.md`                           |

## Governing Overview

[../overview.md](../overview.md)

## Purpose

`test_serving_notes.py` is the test suite for the agent-orchestration L9
coordination-notes API (`serving/notes.py`): the `{repo, master}` selector validation,
the `confine_rel` confinement (traversal / absolute / symlink escape), the
missing-notes-folder empty-list degrade, subfolder listing with the honest depth cap,
and the size-capped binary-tolerant read.

## Code Commentary

### Logic

L9 review follow-up adds `test_null_byte_path_is_400_bad_path`: a null byte inside `path` must answer `400 bad-path`, not an uncaught 500 (L9R-1).

One `NotesRouteTests` class, deliberately **API-layer only**: every test drives
`TestClient(create_app(config, cadence=ProjectionCadence(interval=100)))` — the projection
pacing arrives as one `serving.projector.ProjectionCadence` value, not a loose `interval`
keyword — against a temp coordination tree
(`coord/tasks/R/<master>/notes/`) so the confinement and the status idiom are proven at
the real HTTP surface, never against hand-aligned internals. Coverage groups:

- **Listing** — a missing notes folder answers `200` with `notes: []` (never an error);
  seeded notes list files-before-subfolders with notes-root-relative posix paths
  (`reports/…` included); a tree deeper than `_MAX_LIST_DEPTH` keeps the at-cap file,
  drops the beyond-cap file, and reports `truncated: true`; a symlink pointing outside
  the notes tree is skipped from the listing entirely.
- **Reading** — a markdown note round-trips content + `language: "markdown"`; a nested
  `reports/` note reads; a binary blob answers `language: "binary"` with empty content
  and the true `size`; an oversize file truncates at `_MAX_FILE_BYTES` while reporting
  the full size; an absent note is `404 not-found`. **260703-L18 (finding 5):**
  `test_read_oversize_multibyte_boundary_returns_text_not_binary` seeds an oversize markdown
  note whose multi-byte char straddles the cap and asserts `language: "markdown"` (NOT
  `binary`) with non-empty content — the codepoint-boundary cut.
- **Confinement + selector** — `../` traversal and an absolute path are `400 bad-path`;
  a symlink escape on read is `400 bad-path`; an unknown repo is `404 unknown-repo`; a
  multi-segment / dot-prefixed / empty `master` is `400 bad-request` (subTest sweep);
  `POST` to the GET-only route is `405`.

### Conventions

Mirrors `test_serving_files.py`'s harness: `sys.path.insert` of `mcp/src` before the
package import, `tempfile.TemporaryDirectory` per test, a `McpRuntimeConfig` built
inline with one allow-listed repo `R`.

### Invariants And Boundaries

The suite writes only inside its temp dir; the symlink tests create the escape target
inside the same temp dir (never a real host path), so the suite stays hermetic.

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| The suite exercises only the local temp coordination tree. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History
2026-08-04T13:47:55+02:00 — 260731-EFA-L6 S18-B11 same-reviewer correction: deleted the three rangeless internal rows; no unsupported anchored-route disposition retained. Verification metadata unchanged.

- 2026-07-31T16:50+02:00 — 260731-EFA-L2 curator: the shared client builder now calls
  `create_app(config, cadence=ProjectionCadence(interval=100))`, so the Logic paragraph's quoted
  harness call was rewritten and the new `serving.projector.ProjectionCadence` parameter object
  is named where the old loose `interval=100` keyword used to be. The route, confinement,
  depth-cap, and binary/oversize coverage claims are unaffected; the only other source change in
  this file was a `ruff format` reflow of one multi-line `assertEqual` in the listing test.

- 2026-07-07T18:40+02:00 — 260703-L18 (review fix batch, finding 5): added
  `test_read_oversize_multibyte_boundary_returns_text_not_binary` — an oversize markdown note with a
  multi-byte char straddling the 2-MiB cap reads back as `markdown` + non-empty content, pinning the
  codepoint-boundary cut. Verification metadata pinned until closeout stamps the L18 commit.
- 2026-07-06T09:30+02:00 — L9 adversarial-review follow-up: null-byte path regression test added (L9R-1). Verification metadata pinned until closeout stamps the L9 commit.

- 2026-07-06T01:20+02:00 — Created for agent-orchestration L9: 15 API-layer tests over
  `/api/notes/{list,read}` covering confinement (traversal, absolute, symlink escape),
  selector validation (allow-list repo, single-segment master), the missing-folder
  empty list, the depth-capped subfolder walk, and binary/oversize reads.
  Verification metadata pinned until closeout stamps the L9 commit.
