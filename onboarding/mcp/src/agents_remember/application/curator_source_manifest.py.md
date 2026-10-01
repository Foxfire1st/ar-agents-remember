# mcp/src/agents_remember/application/curator_source_manifest.py

## Governing Overview

[application route overview](overview.md)

## Purpose

**The curator's external-source plane: a bounded manifest, and the origin refs that bind to it
(ICR-R28@v2).** An external source is deliberately **not** a `SourceAnchor` (`:3-10`), because an
anchor names a repository-relative path and an exact Git blob — so recording a URL there would
fabricate a Git identity the repository does not have. Instead the run retains a **bounded,
attributable source manifest** — source URL/document identity, version or retrieval time, the
inspected-content digest when one is available, and the relevant passage/location — and binds the
authored record's existing `Authorship.origin_refs` to that manifest's own digest.

**Three properties are the whole of it (`:12-25`):**

| Property | What it means |
| --- | --- |
| Nothing is invented | A source exists here exactly when the curator declared one. No URL is resolved, no document is fetched, and no digest is computed over bytes this run never saw: the manifest records what the curator **inspected** and says which of those fields were recorded and which were not |
| A declaration is attributable or it is refused | `document`, `location` and one of `version`/`retrieved_at` are required, because a source with none of them cannot be found again; a `content_digest` that is present must be a sha256, and its absence is recorded as `null` rather than filled with a favourable default |
| The manifest is written through the artifact owner the candidate already has | One canonical-JSON file written atomically into the candidate directory beside the allocation journal, read back and verified, and named by its own sha256 — so a reader resolves a record's origin reference to these exact bytes or to nothing |

**The manifest records what the list *declared*, and says so in its own header** (`:27-30`): the run's
report is what says which entries committed. That split is deliberate, because the manifest is written
before the batch that could still refuse, and a record claiming authors it did not reach would be
exactly the kind of false completeness this requirement refuses.

## Code Commentary

### Logic

**Two names and one bound are declared as values rather than implied.** `ENTRY_SOURCES_KEY` (`:64-68`)
is `"external_sources"` and `MAX_SOURCES_PER_ENTRY` is 32 — the comment states why the bound exists: a
manifest is a bounded attributable record, and an unbounded one is a second store wearing a file's
name. `SOURCE_MANIFEST_NAME` (`:70-73`) is `"curator-source-manifest.json"` and
`SOURCE_MANIFEST_SCHEMA` is `"curator-source-manifest/v1"`, so a reader of the file needs no other
document to read it. The two origin-reference prefixes (`:75-79`) are `curator-handoff:v1:` and
`curator-source-manifest:v1:` — spellings of **references**, not paths, so a record's origin is
resolvable without inventing a Git object.

**One declared source carries the fields that make it findable again.** `ExternalSource` (`:91-118`) has
`source_id`, `document`, `location`, an optional `version`, an optional `retrieved_at` and an optional
`content_digest`; `as_record()` is the exact JSON object the manifest stores, with the camel-cased keys
`contentDigest`/`retrievedAt`. `version` and `retrieved_at` are the two ways an external document
identifies the revision that was read.

**The reading refuses rather than repairs.** `_read_entry_sources` (`:178-210`) refuses a non-list
(`external_sources_malformed`), a list over the bound (`external_sources_over_bound`, whose sentence
says an unbounded list is a second store rather than a manifest) and two sources sharing an id
(`external_sources_duplicate_id`, because a record's origin reference would then name two documents).
`_read_source` (`:213-261`) requires id, document and location
(`external_source_malformed`), requires at least one of version/retrieval time
(`external_source_unversioned` — "the document revision it was authored from cannot be found again"),
and refuses a `content_digest` that is not a sha256 (`external_source_digest_malformed`) rather than
recording it as if it identified the content. A present-but-blank field is absent: `_text` (`:446-452`)
is the one definition, and a digest that was simply not taken is stored as `null`.

**`EntrySources` keeps "declared none" apart from "not examined"** (`:121-132`): `examined` is present
exactly when the entry carried the key at all. `SourcePlaneRead` (`:135-157`) holds the entries and the
refusals, with three accessors — `sources_of`, `examined`, `refusal_of` — so a caller never reads the
mapping directly.

**`source_manifest` answers `None` for a list that declares nothing, and that is not an empty
manifest** (`:293-322`): nothing declared means no artifact is written and the run's origin references
name the hand-off list alone, while a written manifest is a real file with a real digest. The payload is
canonical JSON carrying the schema, `declaredBy: "curator-hand-off-list"`, the hand-off list's own
digest, and one entry per declaring entry with its sources in `sorted` order; the manifest's `digest` is
the sha256 of exactly those bytes. `declared`, `with_content_digest` and `without_content_digest`
(`:272-290`) are measured counts over that payload.

**`write_source_manifest` proves the bytes read back** (`:325-335`). It writes through
`atomic_write_bytes` and then compares `path.read_bytes()` with the payload, raising a `ValueError`
whose sentence names the consequence rather than the symptom: the origin references this run records
would name bytes no reader can find.

**`origin_refs` is the whole binding, and it is two references at most** (`:338-352`): the hand-off
list's own digest, and — when the list declared external sources — the manifest's digest. Its docstring
states the boundary in one sentence: a reader resolves the second to the manifest file, whose per-entry
records are where each declaration's document identity, version or retrieval time, content digest and
location live, and **no external source is ever turned into a source anchor**, so nothing claims a Git
identity for a document the repository does not hold.

**The coverage keeps four states apart** (`SourceCoverage` `:366-389`): `recorded` means the manifest
was written and the digest names its exact bytes; `projected` means a planning run would write it and
wrote nothing, so the digest is the one it *would* name; `not-recorded` means no manifest exists, with
`detail` naming why and no path and no digest claimed for it; and every committed entry's own
`examined`/`declared` pair keeps "declared none" and "not examined" apart. `declared` and
`content_digests_recorded` count what the **list** declared, which is a fact about the list in every
state, while `state` is what says whether those declarations were retained.

**`source_coverage` builds the per-entry outcomes and withholds what was not established**
(`:410-443`): the digest is emitted only when the state is `recorded` or `projected`, and the path is
whatever the scope supplies (`None` unless the state is `recorded`). `EntrySourceOutcome` (`:355-363`)
carries one committed entry's `examined` flag, its declared count, how many of its sources carried a
content digest, and their ids; `unexamined` names the committed entries whose external sources this run
did not examine, and `unresolved` is taken from the scope rather than recomputed.
`SourceCoverageScope` (`:392-407`) groups one run's outcome because it is one fact about one run.

### Conventions

This module imports the kernel's atomic write and canonical JSON, the model's reference bound and
sha256 pattern, and nothing else from the application layer. It never touches the family plane: the two
planes are composed by `curator_ingest_planes.py`, which is the only place that holds both.

### Invariants And Boundaries

- An external source is never a `SourceAnchor`; no URL is recorded as a repository path with a blob.
- Nothing is fetched or digested here: the manifest records what the curator inspected.
- `document`, `location` and one of `version`/`retrieved_at` are required for every declared source.
- An absent content digest is stored as `null`, never filled with a favourable default.
- One entry may declare at most 32 sources, and two sources may not share an id.
- The manifest's digest names its exact bytes, and the writer proves the read-back.
- `None` from `source_manifest` means the list declared nothing; it is not an empty manifest.
- The digest is reported only for a `recorded` or `projected` plane, and the path only for `recorded`.

### Todos

None recorded.

## Evidence

### Docs References

No configured Domain Documentation source applies; `BOOTSTRAP-HANDOVER.md` is the process authority
this plane implements, and it is a task-tree document rather than a configured domain source.

No external documentation is required for the bounded source manifest.

### Repo-Internal References

- **The module's own statement of the three properties and of why an external source is not a source anchor.** [1]
- The published surface: the key, the bound, the artifact name, the reading values, the writers and the coverage. [2]
- **The hand-off key and the declared bound, with the comment stating why an unbounded list would be a second store.** [3]
- The one artifact name this plane owns and the schema line its header carries. [4]
- **The two origin-reference prefixes, which are references rather than paths.** [5]
- One entry's source plane refused: the code that names why, and the sentence. [6]
- **One inspected source with the fields that make it findable again, and the exact JSON object the manifest stores for it.** [7]
- **`examined` present exactly when the entry carried the key, so "declared none" and "not examined" are two facts to the report.** [8]
- The whole list's declarations with the three accessors a caller reads them through. [9]
- The reading pass that refuses what is not attributable. [10]
- **The entry-level refusals: not a list, over the bound, and two sources sharing one id.** [11]
- **One source refused unless it names where it was read, when, and a digest that is really a sha256.** [12]
- **The manifest's exact bytes, the digest that names them, and the measured counts over them.** [13]
- **`None` is not an empty manifest: nothing declared means no artifact is written.** [14]
- **The write that proves its own read-back, raising with the consequence rather than the symptom.** [15]
- **The whole binding: two references at most, and no external source turned into a source anchor.** [16]
- One committed entry's external-source coverage, as the run established it. [17]
- **The four non-merging states, and the declaration counts that are a fact about the list in every state.** [18]
- One run's outcome grouped as one value, because it is one fact about one run. [19]
- **The assembly, where a digest is emitted only for a recorded or projected plane and the path only for recorded.** [20]
- The one definition of a declared field as non-blank text, and the bounded refusal constructor. [21]
- The artifact owner the manifest is written through, and the canonical bytes it is made of. [22]
- **The existing origin-reference field an external source binds through, and the Git-bound anchor it deliberately is not.** [23]
- The two bounds this module reads rather than restates. [24]
- The seam that composes this plane with the family plane and owns both coverages together. [25]

### Cross-Repo References

No cross-repository behavior is implemented in this file: it reads no repository at all. An external
source is retained as a declared reference, and the resolved settings' `crossRepo.allow` is empty, so
nothing here names, reads or writes another repository.

No meaningful cross-repo references found.
