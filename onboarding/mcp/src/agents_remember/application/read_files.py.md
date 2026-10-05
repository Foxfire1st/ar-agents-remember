# mcp/src/agents_remember/application/read_files.py

## Governing Overview

[overview.md](overview.md)

## Purpose

`read_files.py` is the application entry point behind the `read_ar_files` MCP tool (slice 07).
It resolves a batch of up to five paired source+onboarding reads of repo-relative
paths inside an AR-managed repo, returning a plain dict the payload module wraps.
Resolution lives here (not in the payload module) so a later dashboard
`GET /api/files` route can reuse the same logic.

Since 260921-ICR-L19@v1 the same call is also the ordinary route to the repository's **published
intent**: the payload carries a `published_intent` block beside `files`, resolved from the same
`CoordinationContext` and read through the shipped selective read at the dataset's own snapshot. The
selection, the seeds and the named absences belong to `application/published_intent.py`; this module
only carries the block.

Reads paired source and onboarding and attaches the existing published-intent and front-door context.

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

**The payload also carries `published_intent`** cit:([`published_intent_block`], mcp/src/agents_remember/application/published_intent.py:464-479), attached at
the assembly from the same context and the paths this call was addressed at cit:(["published_intent", `memory_format`, `legacy_published_intent`], mcp/src/agents_remember/application/read_files.py:162-170) and imported from its owning module
cit:([`published_intent_block`], mcp/src/agents_remember/application/read_files.py:36-36). The key is present on **every** call, including when the
repository publishes nothing yet, because "nothing is recorded" is an answer a fresh planner needs and an
omitted block is indistinguishable from a route that never ran; every one of its failures is carried
inside the block, so it can never cost the caller the source and onboarding bytes this call exists to
return. The block's three decisions, its named states and its bounds are documented in
`application/published_intent.py.md`.

**Since MIK-R24 (rules 5 and 9) what the block holds depends on the memory tree's format**
(`application/read_files_format.py`). The format is `text/v2` exactly when the memory root (the
onboarding root's parent) holds `knowledge/layout.json`.

- **Converted tree.** `published_intent_block` runs as described above, and each file result that has
  onboarding also gets `format: "text/v2"`, the card's sidecar and its resolved references
  (`converted_card_parts`).
- **Unconverted tree.** The block is `legacy_published_intent`: `state: "legacy-format"`, the memory root,
  and a detail naming both conversion routes. No knowledge section is read, and each file result that
  has onboarding is marked `format: "legacy-format"`, with the Markdown returned as it is. The old format
  is never misread as the new one.

**The legacy-format read is active in this build (architect ruling, 2026-09-29).** It therefore changes
what this build's `read_ar_files` returns on today's unconverted trees: the database publication is no
longer served through this route. This build is not installed before MIK-R37. The ICR-R19 route cases
(`tests/test_read_ar_files.py`) now measure the database block through `published_intent_block` directly,
and the converted-tree route is covered through `read_ar_files` itself
(`tests/test_knowledge_conversion_toolchain.py`). The taskless `knowledge_read`, `knowledge_diff` and
`knowledge_project` tools are unchanged.

**`FileReadStatus` is declared in `models/read_files.py`** cit:([`FileReadStatus`], mcp/src/agents_remember/models/read_files.py:29-29) — the onboarding-lookup outcome
for one requested path, `found | missing | disabled | unsupported |
not_requested` — with `VALID_FILE_READ_STATUSES` derived from it by `get_args`
cit:([`VALID_FILE_READ_STATUSES`], mcp/src/agents_remember/models/read_files.py:32-32); this module imports the alias
cit:(["from agents_remember.models.read_files import FileReadStatus"], mcp/src/agents_remember/application/read_files.py:73-73). 260731-EFA-L4 moved the declaration here from
`models/read_files.py`; the later staged reversal moved it back, because the
alias is served wire vocabulary and the model side owns it (see Update History).
The deciding direction is unchanged: `_resolve_onboarding` is the only function
that decides the value and `_read_one` drops it into an untyped payload dict, so
`test_wire_vocabulary_exhaustiveness` asserts the set this function actually
returns *equals* the declared alias.

`_parse_file_request` cit:([`_parse_file_request`], mcp/src/agents_remember/application/read_files.py:187-208) validates one entry: a non-empty repo-relative `path`; an
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

`_resolve_onboarding` cit:([`_resolve_onboarding`], mcp/src/agents_remember/application/read_files.py:262-291) returns
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

`_attach_front_door` builds the front-door deduplicated by lifecycle and resolved code/onboarding roots: the repo overview
(`overview.md` at the onboarding root via `_repo_overview`) plus the governing
route-overview chain for each requested path (`_governing_route_overviews`, nearest
folder first, excluding the repo root which is delivered as `repository_overview`).
Each piece is hashed (`_content_hash`, `sha256:`) and run through `_should_serve`:
with no active lifecycle there is no ledger so everything is served (best effort);
otherwise `_overview_scope_key` hashes the resolved code and onboarding roots into the
repo/route overview kind, and a piece is served only when `amb.is_served` says it is new or
content-changed for that lifecycle and root pair; `amb.record_served` records that same identity. Each request path is
re-`_confined_rel`'d here so the front-door's route derivation never depends on
`_read_one` having confined it first.

**Since MIK-R05 the block has one rendering here: `served_earlier`** (rule 4). On a converted tree the
assembly wraps `published_intent_block(...)` in `_chain_rendered(block, amb, lifecycle_id)`, which calls
`knowledge_leaf.chain.shorten_served` with a callable over the same `_should_serve` ledger the front-door
uses, under a distinct kind, `_KIND_CHAIN_FAMILY` = `knowledge_chain_family`, keyed by family ID. A
`chain_family` row already served to this lifecycle, and unchanged since, comes back as a `served_earlier`
reference row in the same position, so the block's counts, manifest and continuations are those of the full
selection. The selection is not changed here, and `knowledge_read` never shortens. A chain entry returned
through `knowledge_read` does not count as served; `refresh=true` and the compact-reset marker re-serve it,
and with no active lifecycle every row is served in full, exactly like the overviews. The unconverted branch
(`legacy_published_intent`) is not wrapped, so unconverted reads are unchanged.

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
- **The published-intent block is additive and never fatal.** It is resolved from the same context and
  attached on every call, and it answers with a named `state` (`recorded` / `not-recorded` / `unusable`)
  instead of raising, so the paired source+onboarding bytes this entry point exists to return are never
  lost to a missing, corrupt or foreign publication. The block's selection is not made here:
  `application/published_intent.py` owns it, and this module must not re-derive a dataset path or a seed.
- **Only this entry point deduplicates chain entries, and only by rendering** (MIK-R05 rule 4): the shortened
  row still counts, and overview attachment is unchanged (MIK-R05 Preservation; the front-door dedup tests
  pass unchanged). The chain kind is distinct from `_KIND_REPO_OVERVIEW` and `_KIND_ROUTE_OVERVIEW`.
- **A requested path is carried into the block unchanged.** The block is seeded with `request.path` for
  every parsed request, so a path this entry point accepted is the path the intent read is asked about;
  path confinement and the intent seed are one spelling, not two.

### Role Runtime and Scope

Overview dedup now keys each lifecycle entry by both resolved code root and onboarding root through _overview_scope_key. Identical relative overview paths/content from different admitted leaves no longer suppress each other. The published-intent chain shortening and the MIK knowledge projection remain their existing separate logic.

## Evidence

### Repo-Internal References

- The thin payload wrapper that returns this application entry point's dict through the token choke point. [1]
- **The published-intent half this entry point attaches: the owning module's public surface, the import it arrives through, and the assembly line it is attached at.** [2]
- **The format switch (MIK-R24 rules 5 and 9): a converted tree's file results carry the sidecar and resolved references, and an unconverted tree's are marked `legacy-format`.** [3]
- The import of the format helpers. [4]
- **MIK-R05: a chain entry already served to this lifecycle is shortened to `served_earlier` through the served ledger, under its own kind; the rendering is imported from the chain module.** [5]
- The strict response contract this dict validates against; `FileRead.status` is typed by the `FileReadStatus` alias declared in that model. [6]

| Repo-resolution authority guard. | `require_repo` | mcp/src/agents_remember/kernel/authority.py:16-24 |
| The authority-violation error raised on a bad batch/range/path. | `AuthorityError` | mcp/src/agents_remember/errors.py:110-116 |
| The full read and the net-new ranged reader (`read_text_range`). | `read_text_range` | mcp/src/agents_remember/kernel/filesystem.py:44-62 |
| Coordination-context resolution and per-path storage-mode resolution. | "_resolver.resolve_coordination_context" | mcp/src/agents_remember/kernel/coordination_context_resolver.py:131-146 |
| The shared confinement helper resolves the requested path and refuses a repository escape; read_files imports it as _confined_rel. | "def confine_rel(" | mcp/src/agents_remember/kernel/sidecar_pairing.py:37-49 |
| The shared sidecar status helper consults governing indexes and falls back to a mirrored file probe; read_files imports it as _route_sidecar_status. | "def route_sidecar_status(" | mcp/src/agents_remember/kernel/sidecar_pairing.py:91-106 |
| The shared sidecar body helper returns meaningful text or None for absent/unreadable content; read_files imports it as _sidecar_body. | "def sidecar_body(" | mcp/src/agents_remember/kernel/sidecar_pairing.py:142-149 |
| `ROUTE_OVERVIEW_NAME` consumed read-only for the front-door route derivation. | `ROUTE_OVERVIEW_NAME` | mcp/src/agents_remember/kernel/route_index.py:17-17 |
| The ambient lifecycle: `read.packet` emission and the served-onboarding dedup ledger consumed here. | `emit_read_packet` | mcp/src/agents_remember/observer/ambient.py:426-453 |
| The observer-root resolver locating the compact-reset marker. | `observer_root` | mcp/src/agents_remember/serving/projections/paths.py:32-34 |

### Runtime Source References

- Frozen implementation of _overview_scope_key supporting the stated file behavior. [7]
- Frozen implementation of _attach_front_door supporting the stated file behavior. [8]
