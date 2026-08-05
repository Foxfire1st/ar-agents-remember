# mcp/src/agents_remember/application/read_files.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/application/read_files.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-02T01:05+02:00                     |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

`read_files.py` is the application entry point behind the `read_ar_files` MCP tool (slice 07).
It resolves a batch of up to five paired source+onboarding reads of repo-relative
paths inside an AR-managed repo, returning a plain dict the payload module wraps.
Resolution lives here (not in the payload module) so a later dashboard
`GET /api/files` route can reuse the same logic.

## Code Commentary

### Logic

The path-confinement guard and the sidecar-pairing helpers were extracted to
`kernel/sidecar_pairing.py` (shared with the dashboard `serving/files.py`); they are
imported here under their former private names (`_confined_rel`,
`_route_sidecar_status`, `_sidecar_body`) and behave exactly as before. The
descriptions below document that imported behavior.

`read_ar_files_tool(config, *, repo_id, files, refresh, _context)` is the entry
point. It resolves the repo through `require_repo` (authority check), rejects a
batch over `MAX_FILES` (5) with `AuthorityError`, parses each entry into a frozen
`_FileRequest`, and resolves the coordination context once via
`resolve_coordination_context` — since 260731-EFA-L2 with
`hints=CoordinationHints(coordination_root=...)` and
`selector=EnclosureSelector(contract_path=...)` rather than loose keywords (the `_context` keyword
is still the test seam that injects a pre-built `CoordinationContext` to isolate one storage mode). It then reads the
current ambient lifecycle id, runs `_maybe_reset_served`, reads each file, and
assembles the payload, optionally attaching the deduped front-door, and finally
emits a facts-only `read.packet` — passing `repo.repo_id` (slice 07b, so the
packet carries `data.repoId`, the read's repo) alongside the per-file facts.

**`FileReadStatus` is declared in `models/read_files.py`** cit:([`FileReadStatus`], mcp/src/agents_remember/models/read_files.py:29-29) — the onboarding-lookup outcome
for one requested path, `found | missing | disabled | unsupported |
not_requested` — with `VALID_FILE_READ_STATUSES` derived from it by `get_args`
cit:([`VALID_FILE_READ_STATUSES`], mcp/src/agents_remember/models/read_files.py:32-32); this module imports the alias
cit:([`FileReadStatus`], mcp/src/agents_remember/application/read_files.py:46-46). 260731-EFA-L4 moved the declaration here from
`models/read_files.py`; the later staged reversal moved it back, because the
alias is served wire vocabulary and the model side owns it (see Update History).
The deciding direction is unchanged: `_resolve_onboarding` is the only function
that decides the value and `_read_one` drops it into an untyped payload dict, so
`test_wire_vocabulary_exhaustiveness` asserts the set this function actually
returns *equals* the declared alias.

`_parse_file_request` cit:([`_parse_file_request`], mcp/src/agents_remember/application/read_files.py:139-160) validates one entry: a non-empty repo-relative `path`; an
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

`_resolve_onboarding` cit:([`_resolve_onboarding`], mcp/src/agents_remember/application/read_files.py:209-238) returns
`tuple[FileReadStatus, str | None, bool]` — `(status, body, attach)`. Since
260731-EFA-L4 the first element is **narrowed to the alias this module imports**
rather than a bare `str`. With onboarding
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
- **`models/read_files.py` owns the `FileReadStatus` vocabulary.** It is declared
  there because the alias is served wire vocabulary; this module imports it and
  `_resolve_onboarding` decides the value. Adding a member is a one-place edit
  in the model, and the exhaustiveness suite fails if
  the declared set and the returned set stop matching in either direction.
- **The route index is authoritative; missing means missing — don't probe.** When
  a governing index covers a path but does not list it, the status is `missing`
  and the application entry point never probes the filesystem for an unrelated sidecar
  (pre-resolved decision 4). The mirror-path probe is only the fallback when no
  governing index exists.
- **No silent truncation.** A `"full"` request uses `filesystem.read_text`; only a
  range uses `read_text_range`.
- **The `read.packet` carries facts only.** The event entries are
  `{path, lines, status, bytes}`; source/onboarding/overview content never reaches
  the event — the projection is enforced structurally in `ambient.emit_read_packet`.
  The application entry point passes `repo.repo_id` so the packet's `data.repoId` is the read's
  repo (a fact, distinct from the lifecycle's envelope `repoId`).
- The route-index public surface is consumed read-only here; the small private
  nearest-route prefix walk does not extend it.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The thin payload wrapper that returns this application entry point's dict through the token choke point. | `read_ar_files_payload` | mcp/src/agents_remember/mcp/tools/read_files.py:13-22 |
| The strict response contract this dict validates against; `FileRead.status` is typed by the `FileReadStatus` alias declared in that model. | `FileReadStatus` | mcp/src/agents_remember/models/read_files.py:29-29 |
| `test_every_onboarding_status_the_read_entry_point_returns_validates` asserts the set `_resolve_onboarding` returns equals `VALID_FILE_READ_STATUSES`. | `test_every_onboarding_status_the_read_entry_point_returns_validates` | mcp/tests/test_wire_vocabulary_exhaustiveness.py:778-785 |
| Repo-resolution authority guard. | `require_repo` | mcp/src/agents_remember/kernel/authority.py:16-24 |
| The authority-violation error raised on a bad batch/range/path. | `AuthorityError` | mcp/src/agents_remember/errors.py:17-23 |
| The full read and the net-new ranged reader (`read_text_range`). | `read_text_range` | mcp/src/agents_remember/kernel/filesystem.py:44-62 |
| Coordination-context resolution and per-path storage-mode resolution. | `resolve_coordination_context` | mcp/src/agents_remember/kernel/coordination_context_resolver.py:131-146 |
| The shared path-confinement + sidecar-pairing helpers, imported under their former private names (`_confined_rel`/`_route_sidecar_status`/`_sidecar_body`). | `confine_rel`, `route_sidecar_status`, `sidecar_body` | mcp/src/agents_remember/kernel/sidecar_pairing.py:35-47; mcp/src/agents_remember/kernel/sidecar_pairing.py:50-65; mcp/src/agents_remember/kernel/sidecar_pairing.py:101-108 |
| `ROUTE_OVERVIEW_NAME` consumed read-only for the front-door route derivation. | `ROUTE_OVERVIEW_NAME` | mcp/src/agents_remember/kernel/route_index.py:17-17 |
| The ambient lifecycle: `read.packet` emission and the served-onboarding dedup ledger consumed here. | `emit_read_packet` | mcp/src/agents_remember/observer/ambient.py:395-422 |
| The observer-root resolver locating the compact-reset marker. | `observer_root` | mcp/src/agents_remember/observer/paths.py:32-34 |
| The slice-07 test suite. | `RangedReadTests` | mcp/tests/test_read_ar_files.py:159-181 |

## Update History

- 2026-08-04T18:16+02:00 — 260731-EFA-L6 S18-B16 curator: resolved the 4 manifest-assigned findings the W1-B10 pass had preserved as Tier 3. The staged reversal has since landed in the frozen source, so the false status-ownership claims were corrected to it: `FileReadStatus`/`VALID_FILE_READ_STATUSES` are declared in models/read_files.py L29/L32 and this module imports the alias at L46 — ownership paragraph, the vocabulary invariant, the models table row, and two history line-spellings now say so. Scoped fixer + non-fixing recheck green under the frozen snapshot; verification metadata unchanged.

- 2026-08-02T16:45:41+02:00 — 260731-EFA-L6 curator W1-B10: repaired 21 citation findings (9 rows/prose pointers); preserved false status-ownership claims as Tier 3; scoped recheck clean except 4 preserved Tier-3 findings.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — 260731-EFA-L6 curator: source moved. `mcp/src/agents_remember/controllers/` was renamed to `application/`, so this sidecar moved with its source; path metadata and every in-body path follow, and the prose adopts "the application layer" / "an application entry point" for what it used to call a controller. The rename itself changed no behavior. **FLAGGED, NOT FIXED — this body is stale for a reason that is NOT the rename, and the curator who owns that change should repair it.** A separate staged change in the same code worktree moved `FileReadStatus` and `VALID_FILE_READ_STATUSES` back OUT of this module into `models/read_files.py` (now L29 and L32 there); this module imports the alias at L43 and declares neither. That reverses the 260731-EFA-L4 decision recorded below, so the "**This module declares `FileReadStatus`** (line 54)" claim in `Code Commentary`, the `VALID_FILE_READ_STATUSES` (line 57) claim, and the L54/L57/L146/L216-L218 anchors are all false against the current worktree. The claims are left verbatim rather than rewritten into something plausible, because the intent behind the reversal belongs to that change, not to this one. `_should_serve` also moved from `amb.is_served`/`amb.record_served` to `amb.served.is_served`/`amb.served.record`, which this card does not mention either way. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-01T09:42+02:00 — 260731-EFA-L4 curator: body updated. This module now DECLARES
  `FileReadStatus` (line 54) and the derived `VALID_FILE_READ_STATUSES` (line 57); the alias moved here
  from `models/read_files.py` because `_resolve_onboarding` is the only function that decides the
  value, and its signature is now `-> tuple[FileReadStatus, str | None, bool]` cit:([`_resolve_onboarding`], mcp/src/agents_remember/application/read_files.py:209-238) instead
  of `-> tuple[str, ...]`. The card had described the status vocabulary only as the returned tuple's
  first element with no type and no owner. Added the ownership paragraph and the matching
  invariant. Citations: `_parse_file_request` L146 and `_resolve_onboarding` L216-L218 pinned; the
  `models/read_files.py` reference row now names `FileRead.status` L35 as the importer, and a row
  was added for the exhaustiveness suite. Verification metadata pinned until closeout stamps the
  L4 commit.
- 2026-07-31T15:31+02:00 — 260731-EFA-L2: the `resolve_coordination_context` call moved onto the
  resolver's `CoordinationHints` / `EnclosureSelector` parameter objects; the rest of the file was
  touched only by the whole-tree `ruff format`. Batch limits, status vocabulary, dedup and the
  `read.packet` emission are unchanged. Verification metadata pinned until closeout stamps the L2
  code commit.
- 2026-06-28T22:41+02:00 — operations-integration L1: extracted the path-confinement guard (`_confined_rel`) and the sidecar-pairing helpers (`_route_sidecar_status`/`_governing_indexes`/`_load_route_index`/`_sidecar_body`) into `kernel/sidecar_pairing.py`, shared with the new dashboard `serving/files.py`; they are now imported here under their former private names. Behavior-preserving — the slice-07 suite is unchanged. References updated (the direct `meaningful_body`/`mirror_onboarding_path`/`sidecar_status` rows now flow through `sidecar_pairing`). Verification metadata pinned until closeout stamps the L1 code commit.
- 2026-06-23T01:40+02:00 — Slice 07b v1: the controller now passes `repo.repo_id` to `emit_read_packet`, so the emitted `read.packet` carries `data.repoId` (the read's repo). Body + invariant note only — verification metadata pinned until closeout stamps the slice-07b code commit.
- 2026-06-23T00:53+02:00 — Slice 07 (S5): retargeted the compact-reset note — the `compact-reset.json` **producer** is **not** a session-hook concern; it is deferred to the post-3.0 agentic-control-plane follow-up (fresh-worker / new-lifecycle = fresh ledger). `_maybe_reset_served` (consumer) + the `refresh=true` path remain as defensive scaffolding; `refresh=true` is the working manual reset. Docstring text only. Verification metadata pinned until closeout stamps the slice-07 code commit.
- 2026-06-22T22:33+02:00 — Created for slice 07 (S2+S3): the `read_ar_files` controller — paired source+onboarding batch reads (≤5 files), the net-new `_confined_rel` path-confinement guard, ranged/full source read, storage-mode + route-index onboarding lookup (present→found, absent→missing without probing, external-as-sidecar), the session-deduped front-door auto-attach (repo overview + governing route chain + sidecar `meaningful_body`), facts-only `read.packet` emission, and the `refresh` + compact-reset-marker consumer (the marker producer is deferred to slice-07 S5 / Probe B). Verification metadata pinned until closeout stamps the slice-07 code commit.
