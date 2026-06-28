# mcp/src/agents_remember/controllers/read_files.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/controllers/read_files.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-22T22:33+02:00                     |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1` |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

`read_files.py` is the controller behind the `read_ar_files` MCP tool (slice 07).
It resolves a batch of up to five paired source+onboarding reads of repo-relative
paths inside an AR-managed repo, returning a plain dict the payload module wraps.
Resolution lives here (not in the payload module) so a later dashboard
`GET /api/files` route can reuse the same logic.

## Code Commentary

### Logic

`read_ar_files_tool(config, *, repo_id, files, refresh, _context)` is the entry
point. It resolves the repo through `require_repo` (authority check), rejects a
batch over `MAX_FILES` (5) with `AuthorityError`, parses each entry into a frozen
`_FileRequest`, and resolves the coordination context once via
`resolve_coordination_context` (the `_context` keyword is a test seam that injects
a pre-built `CoordinationContext` to isolate one storage mode). It then reads the
current ambient lifecycle id, runs `_maybe_reset_served`, reads each file, and
assembles the payload, optionally attaching the deduped front-door, and finally
emits a facts-only `read.packet` — passing `repo.repo_id` (slice 07b, so the
packet carries `data.repoId`, the read's repo) alongside the per-file facts.

`_parse_file_request` validates one entry: a non-empty repo-relative `path`; an
`onboarding` flag (default true; only `False` suppresses the lookup); and a
`source` that is either `"full"`/absent (whole file) or a `{startLine, endLine}`
dict. The range is validated up front — both ends must be integers `>= 1` and
`endLine >= startLine` — so an inverted or zero range raises `AuthorityError`
rather than reaching the ranged helper (which would otherwise return `""`, a
silent, confusing result).

`_read_one` does the per-file work: `_confined_rel` confines the path to the code
root, `_read_source` reads the requested slice, and `_resolve_onboarding` looks up
the onboarding status/body. It returns the response entry, the facts-only event
entry, and an `attach_front_door` flag.

`_confined_rel` is the net-new path-confinement guard. It rejects an absolute
path, then `resolve()`s the candidate under the code root (following `..` and
symlinks) and rejects it unless `path_is_relative_to` the code root — so a
traversal token, a symlinked file/dir escaping the repo, or a mid-path `..` that
climbs out is rejected, not just a literal `..`. It returns the posix-relative
form.

`_read_source` reads the full file via `filesystem.read_text` or the requested
range via the net-new `filesystem.read_text_range`. A missing, binary,
non-decodable, malformed-range, or unreadable-but-present file degrades to
source-omitted (`None`, byte count 0) so one bad file never aborts the whole
batch. The returned byte count is the UTF-8 length of what was returned — a fact
for the event, never the content.

`_resolve_onboarding` returns `(status, body, attach)`. With onboarding
suppressed it returns `not_requested` (no front-door). Otherwise it resolves the
storage mode for the path via `resolve_storage_for_source`: `disabled` →
`disabled`; a non-sidecar mode (e.g. `inline`) → `unsupported`; a sidecar mode
(`repo-sidecar`, `memory-repo`, or `external` — this repo's own memory is external
and also writes sidecars) → the route-index lookup. `_route_sidecar_status` walks
the governing route-index chain nearest-first via `_governing_indexes` /
`_load_route_index`, asking `sidecar_status` per index; the first index whose
scope covers the path decides. **Present → `found`** (read the sidecar body via
`_sidecar_body`, which projects to `meaningful_body`); **absent (in-scope,
uncovered) or out-of-scope at every governing index → `missing` without probing
the filesystem** for an unrelated sidecar (the route index is authoritative when
present). When no governing `overview.index.json` exists at all, it falls back to
a direct `mirror_onboarding_path` file probe so a repo with sidecars but no built
index still resolves. A route index that says covered but whose sidecar is
unreadable reports `missing` (don't probe further).

`_attach_front_door` builds the session-deduplicated front-door: the repo overview
(`overview.md` at the onboarding root via `_repo_overview`) plus the governing
route-overview chain for each requested path (`_governing_route_overviews`, nearest
folder first, excluding the repo root which is delivered as `repository_overview`).
Each piece is hashed (`_content_hash`, `sha256:`) and run through `_should_serve`:
with no active lifecycle there is no ledger so everything is served (best effort);
otherwise a piece is served only when `amb.is_served` says it is new or
content-changed, and `amb.record_served` records it. Each request path is
re-`_confined_rel`'d here so the front-door's route derivation never depends on
`_read_one` having confined it first.

`_maybe_reset_served` is the MCP-side **consumer** of the compact-reset marker
(`<observer_root>/workspace/compact-reset.json`, named by `_COMPACT_RESET_MARKER`):
an explicit `refresh=true` or the marker's presence clears the lifecycle's served
set via `amb.reset_served`, and a present marker is unlinked after consuming it
(fire-once, the `read_setup_progress`-style "absent == no signal" idiom). No
producer writes the marker today, and one is **not** planned at the session-hook
level (S5 retarget): compaction-reset is a fresh-worker / lifecycle concern (small
work → new worker → new lifecycle → fresh ledger) deferred to the post-3.0
**agentic-control-plane** follow-up, and `clear` / a new chat already yields a
fresh lifecycle and ledger. Until then `refresh=true` is the working manual reset,
and the consumer + `refresh` path stay as **defensive scaffolding**: if a marker
ever appears it is honored once.

### Invariants And Boundaries

- **Path confinement is the security boundary.** Every requested path — and every
  path used to derive the front-door — runs through `_confined_rel`, which
  resolves real paths before the check, so symlink/traversal escapes are rejected,
  not just literal `..` tokens. Paths must be repo-relative, never absolute.
- **Source presence is independent of onboarding status.** `source` rides its own
  field and is present whenever the file exists and decodes; it is unaffected by a
  `missing` / `disabled` / `unsupported` onboarding status.
- **The route index is authoritative; missing means missing — don't probe.** When
  a governing index covers a path but does not list it, the status is `missing`
  and the controller never probes the filesystem for an unrelated sidecar
  (pre-resolved decision 4). The mirror-path probe is only the fallback when no
  governing index exists.
- **No silent truncation.** A `"full"` request uses `filesystem.read_text`; only a
  range uses `read_text_range`.
- **The `read.packet` carries facts only.** The event entries are
  `{path, lines, status, bytes}`; source/onboarding/overview content never reaches
  the event — the projection is enforced structurally in `ambient.emit_read_packet`.
  The controller passes `repo.repo_id` so the packet's `data.repoId` is the read's
  repo (a fact, distinct from the lifecycle's envelope `repoId`).
- The route-index public surface is consumed read-only here; the small private
  nearest-route prefix walk does not extend it.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The thin payload wrapper that returns this controller's dict through the token choke point. | [mcp/tools/read_files.py](agents-remember/mcp/src/agents_remember/mcp/tools/read_files.py) |
| The strict response contract this dict validates against. | [models/read_files.py](agents-remember/mcp/src/agents_remember/models/read_files.py) |
| Repo-resolution authority guard. | [_guards.py](agents-remember/mcp/src/agents_remember/controllers/_guards.py) |
| The authority-violation error raised on a bad batch/range/path. | [errors.py](agents-remember/mcp/src/agents_remember/errors.py) |
| The full read and the net-new ranged reader (`read_text_range`). | [kernel/filesystem.py](agents-remember/mcp/src/agents_remember/kernel/filesystem.py) |
| Coordination-context resolution and per-path storage-mode resolution. | [coordination_context_resolver.py](agents-remember/mcp/src/agents_remember/kernel/coordination_context_resolver.py) |
| The sidecar `meaningful_body` extractor applied to the onboarding body. | [onboarding_doc.py](agents-remember/mcp/src/agents_remember/kernel/onboarding_doc.py) |
| `sidecar_status`, `INDEX_FILE_NAME`, and `ROUTE_OVERVIEW_NAME` consumed read-only. | [route_index.py](agents-remember/mcp/src/agents_remember/kernel/route_index.py) |
| The mirror sidecar-path helper used for the body read and the no-index probe. | [onboarding_drift_check/discovery.py](agents-remember/mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/discovery.py) |
| The ambient lifecycle: `read.packet` emission and the served-onboarding dedup ledger consumed here. | [observer/ambient.py](agents-remember/mcp/src/agents_remember/observer/ambient.py) |
| The observer-root resolver locating the compact-reset marker. | [observer/paths.py](agents-remember/mcp/src/agents_remember/observer/paths.py) |
| The slice-07 test suite. | [test_read_ar_files.py](agents-remember/mcp/tests/test_read_ar_files.py) |

## Update History

- 2026-06-23T01:40+02:00 — Slice 07b v1: the controller now passes `repo.repo_id` to `emit_read_packet`, so the emitted `read.packet` carries `data.repoId` (the read's repo). Body + invariant note only — verification metadata pinned until closeout stamps the slice-07b code commit.
- 2026-06-23T00:53+02:00 — Slice 07 (S5): retargeted the compact-reset note — the `compact-reset.json` **producer** is **not** a session-hook concern; it is deferred to the post-3.0 agentic-control-plane follow-up (fresh-worker / new-lifecycle = fresh ledger). `_maybe_reset_served` (consumer) + the `refresh=true` path remain as defensive scaffolding; `refresh=true` is the working manual reset. Docstring text only. Verification metadata pinned until closeout stamps the slice-07 code commit.
- 2026-06-22T22:33+02:00 — Created for slice 07 (S2+S3): the `read_ar_files` controller — paired source+onboarding batch reads (≤5 files), the net-new `_confined_rel` path-confinement guard, ranged/full source read, storage-mode + route-index onboarding lookup (present→found, absent→missing without probing, external-as-sidecar), the session-deduped front-door auto-attach (repo overview + governing route chain + sidecar `meaningful_body`), facts-only `read.packet` emission, and the `refresh` + compact-reset-marker consumer (the marker producer is deferred to slice-07 S5 / Probe B). Verification metadata pinned until closeout stamps the slice-07 code commit.
