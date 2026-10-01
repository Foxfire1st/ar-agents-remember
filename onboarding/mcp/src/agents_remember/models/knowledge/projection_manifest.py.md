# mcp/src/agents_remember/models/knowledge/projection_manifest.py

## Governing Overview

[models route overview](../overview.md)

## Purpose

The vocabulary of managed external projection: the destination manifest and its per-path entries, the
machine-specific destination profile, one rendered artifact carrying its three recorded values, the
projection plan and its per-path overwrite authorization, the per-path outcome and typed report, the
four-kind discrepancy record, the seven-member vault-safety refusal closure, the collision records,
and the `ProjectionWriter` protocol that is the only write path an artifact may take. It deliberately
does **not** have the behaviour: nothing here stages, renames, deletes, reads a directory, or touches a
filesystem — that is `agents_remember.memory.knowledge.managed_projection`, and the operation that
renders and then calls it is `agents_remember.application.knowledge_projection`. It also has no
knowledge identity: the manifest digest is projection bookkeeping about a file on disk, confers no
identity on the record it projects, and nothing in the substrate reads it as one. There is no
constructor for a rendered artifact missing its stable identity, its source snapshot or its
renderer/profile version, no operation that takes a bare destination path, and no field anywhere that
could hold a verdict about a record's meaning.

## Code Commentary

### Logic

**The manifest is the only authority on what the substrate owns, and the writer has no bare-path
operation.** `ProjectionManifest` declares `manifest_format`, a `generation` of at least one, the
`renderer_version`, the produced `outputs` and the `retained` entries — and nothing else, so
"does the substrate own this file" is answered by the manifest or not at all. `owned_paths()` is the
union of both tuples as a `frozenset`, `output_for(path)` and `retained_for(path)` are the keyed
lookups, and `recorded_digest_for(path)` and `recorded_identity_for(path)` read *produced first, then
retained*, so a retained file keeps its recorded digest and stays covered by the unchanged and
externally-edited tests while a path the manifest does not list answers `None` — which is exactly what
makes it not the substrate's to write over. `_require_one_entry_per_path` refuses a manifest that
records one produced path twice, one retained path twice, or one path as both produced *and* retained,
because a path present in both states would make the next generation's unchanged test depend on which
entry a reader happened to consult. `ProjectionWriter` is a `@runtime_checkable` `Protocol` with the
single member `write(plan) -> ProjectionReport`: a producer that needed a subclass could add a second
write path beside it, and a write path that took a bare destination path could reach a file the
manifest never listed.

**Every produced entry carries five recorded facts plus digest material, and the artifact shape is
where a missing input dies.** `ManagedOutput` requires `destination_relative_path`, `stable_identity`,
`record_kind`, `format`, `source_snapshot` (pattern-bound to `SHA256_PATTERN`), `renderer_version`, a
`digest_algorithm` fixed to `DIGEST_ALGORITHM`, the `digest` itself under the same pattern, a
non-negative `byte_count` and the `authorized_overwrite` flag. `RenderedOutput` requires the same
identity triple plus the renderer's `text` with no defaults, so "rendered but missing its identity"
has no constructor and the `unresolved_projection_input` failure state is enforced by the type rather
than by a check a later edit could drop. `RetainedOutput` is requirement 5.6's `retained-with-reason`
state as its own model rather than an absence from `outputs`: it carries the path, a `RetentionReason`,
a `detail` and `recorded`, which is the prior generation's own `ManagedOutput` entry kept whole rather
than reduced to its digest. That last field is load-bearing — a retained file must stay covered by the
externally-edited and unchanged tests when a later projection produces it again, and it must be
restorable as a managed output if that projection withholds the write; otherwise a retained path would
look unowned on the next run and would be overwritten.

**Confinement is two halves, and the module owns the syntactic one.** `require_confined_relative_path`
refuses an empty or whitespace-padded spelling (`candidate != relative_path`), a leading `/` or `\`, any
`""`, `"."` or `".."` segment after normalizing `\` to `/`, and a path whose first of two or more
segments is `STAGING_DIRECTORY_NAME`; every refusal is built by `_escape_refusal` as a
`ProjectionRefusal` with the code `destination_escape`, the offending path, a `next_action` and the
`detail` naming the reason — and with `resolved_root` deliberately left unset here. The resolving half
is `resolve_inside_destination` in `memory/knowledge/managed_projection.py`, and the caller fills
`resolved_root` in with `model_copy` so a caller always learns both halves requirement 5.2 asks for:
both the path *and* the resolved root, because a caller that cannot see the root the substrate
resolved cannot tell whether its own configuration or the path was wrong. The docstring is explicit
that string prefix comparison is not the check: `Path.resolve()`-based resolution is what catches a
symlinked intermediate directory, a final component that is itself a link, or a case-folded alias.

**Collisions are detected over the whole plan before either output is written.** `canonical_destination`
is `unicodedata.normalize("NFC", path).casefold()`, and `detect_destination_collisions` groups every
`RenderedOutput` by that canonical form, then reports a `Collision` in two cases: two or more members
that differ as written (`len(distinct) > 1`), and two members that share one identical path. The second
branch exists because two records projecting to one *identical* path is the same failure with no case
folding involved, and it is reported through the same channel rather than as one record's artifact
silently overwriting another's. A `Collision` names the sorted destination paths, the shared
`canonical_form` and the `stable_identities` of the records involved, and `DestinationCollision` binds a
collision to its refusal with `_require_the_collision_code` proving the code is
`destination_collision`. The comparison is over the *destination*, never over a record's own identity
or its symbol name, and the substrate does not pick one, overwrite one with the other, or resolve the
collision by appending a suffix the manifest did not record.

**The staging directory and the digest algorithm are declarations here, and both are chosen rather than
convenient.** `STAGING_DIRECTORY_NAME` is one directory *inside* the destination, which is what makes a
publication a rename within one filesystem; the shipped writer stages each artifact under it, moves one
rename per output with `os.replace`, and publishes the manifest last through the same discipline. The
module also refuses a destination-relative path that names that directory as a published output, so the
staging area cannot be reached as content. `DIGEST_ALGORITHM` is the single-member literal `"sha256"`,
chosen because `SHA256_PATTERN` already governs every digest that crosses the knowledge boundary, and
`ManagedOutput.digest_algorithm` defaults to it so an entry cannot claim an algorithm the substrate
does not compute. `PROJECTION_MANIFEST_NAME` is `projection-manifest.json` and
`PROJECTION_MANIFEST_FORMAT` is `projection-manifest/v1`; `manifest_relative_path()` is the accessor
that keeps callers from spelling the name themselves, and the reader refuses an unreadable or
format-mismatched manifest rather than treating the destination as unowned. The refusal closure is
separate from that name, and it is the second declaration the module states twice:
**`ProjectionRefusalCode` is a namespace of eight literals, and `RefusalCode` restates that same
eight-member closure as one type.** The members are `destination_escape`, `destination_collision`,
`escaping_link`, `unresolved_projection_input`, `manifest_unreadable`, `destination_unavailable`,
`unauthorized_overwrite` and, since 260928-MIK-L02 (MIK-R02), `oversized_row`: a view row (or its header)
that renders past the 20,000-character artifact bound even alone, which `knowledge_projection._parts`
refuses by name instead of raising or cutting it short. The widening is additive. They are deliberately *not* added to
`agents_remember.models.knowledge.result.KnowledgeRefusalCode`, because that literal is an earlier
leaf's closed wire vocabulary for dataset operations and a projection refusal is not a dataset
operation — it is a filesystem fact about a directory the substrate does not own, so widening the
shipped vocabulary would change a contract this leaf is required to preserve. `ProjectionRefusal`
carries the code, a non-blank `detail`, the `offending_path` and `next_action`, plus optional
`resolved_root`, `expected` and `observed` so a refusal can name both what was expected and what was
seen. The closure is narrower than the *paths* it describes: six of the seven codes are produced by the
shipped writer (three `manifest_unreadable` paths, two `destination_unavailable` paths, and one each of
`escaping_link`, `unresolved_projection_input`, `destination_collision` and `destination_escape`),
while `UNAUTHORIZED_OVERWRITE` is declared and exported and reached by no code in the candidate,
because an unauthorized overwrite is withheld and reported as a `modified` discrepancy plus a
`retained-with-reason` outcome rather than raised as its own refusal.

**Retention is classified by why the file survived, and only three of the four declared reasons are
produced — while the outcome vocabulary beside it stays exhaustive per path.** `RetentionReason`
declares `edited-since-last-projection`, `unreadable`, `replaced` and `not-owned-by-prior-manifest`: the
shipped writer produces the first for a changed file, `unreadable` for a file that was unchanged but
could not be removed, and `replaced` / `unreadable` / `not-owned-by-prior-manifest` from
`_retention_reason` for a path that has gone absent or been replaced, while nothing in `memory/` or
`mcp/` constructs `not-owned-by-prior-manifest` for a file that is still present. Each reason travels
beside a `detail` and the prior `recorded` entry, and `ProjectionOutcome.state` has six members —
`published`, `unchanged`, `removed`, `retained-with-reason`, `reported`, `refused` — so a caller reads
what happened to a path rather than inferring it from a total. `ProjectionReport` ties the whole run to
one outcome: `state` is `projected` or `refused`, and `_require_one_outcome` refuses a refused report
that carries no refusal or that carries a resulting manifest, and refuses a projected report that
carries a refusal at all — a refused projection writes nothing, so it has no new manifest to show.

**The four discrepancy kinds are distinguished because they call for different caller action.**
`DiscrepancyKind` is `modified`, `replaced`, `deleted` and `unreadable`, and `Discrepancy` carries the
path, the kind, the recorded and observed digests under `SHA256_PATTERN` and a `detail`. Both digests
are optional by necessity rather than by omission: a deleted file has no observed bytes and an
unreadable one has no observed digest, so the kind is what the caller acts on while the digests are what
makes the report checkable. `ProjectionOutcome` and `Discrepancy` are read *per path*, which is what
lets a single hostile destination entry be reported while the remaining outputs continue, and what
keeps a run's report from being a summary a caller has to trust. `DestinationProfile` sits beside all
of this as configuration rather than knowledge: `profile_id`, the resolved absolute `destination_root`,
the `formats` tuple and a `renderer_version`, validated by `_require_a_declared_format` to be non-empty,
duplicate-free and in the declared sibling order of `PROJECTION_FORMATS`. It is never stored in the
dataset and never returned as a recorded fact, and changing it changes no identity and no digest.

### Conventions

Every shape derives from `KnowledgeModel`, so `extra="forbid"` and `frozen=True` are what refuse a
payload arriving with an undeclared field — a verdict, a fifth discrepancy kind, a second refusal code
namespace. Bounded text reuses the base constants instead of literals: `PROSE_MAX_LENGTH` for a
`detail` or a `next_action`, `REFERENCE_MAX_LENGTH` for a destination path, a stable identity, a
canonical form or a resolved root, `LABEL_MAX_LENGTH` for a profile id, a record kind or a renderer
version. Digest- and snapshot-valued fields are validated with the base's `SHA256_PATTERN` rather than
a locally re-spelled regular expression. Declarations that must agree are one declaration: the
`manifest_format` annotation repeats the value of `PROJECTION_MANIFEST_FORMAT`, `digest_algorithm`
defaults to `DIGEST_ALGORITHM`, `_require_the_collision_code` compares against
`ProjectionRefusalCode.DESTINATION_COLLISION` rather than a string, and `_require_a_declared_format`
orders `formats` by `PROJECTION_FORMATS.index`, so the profile and the module cannot disagree about the
sibling views. Redundant structured material is stored as a whole model: `RetainedOutput.recorded` is a
prior `ManagedOutput`, and `DestinationCollision.collision` is a whole `Collision`, rather than each
being flattened into loose fields. Module functions call each other inside the file —
`detect_destination_collisions` groups by `canonical_destination`, and `require_confined_relative_path`
builds every refusal through `_escape_refusal` — so each rule has exactly one spelling. `__all__` names
the twenty-four public names this module adds (seven constants, thirteen model or protocol classes, four
functions), and the module's only non-stdlib import is pydantic plus four constants and the base from
`models/knowledge/base.py`; it imports no store, no application module and no sibling behaviour module,
which is what keeps the dependency pointing from behaviour toward vocabulary and never back.

### Invariants And Boundaries

- **The manifest is the only authority on ownership, and there is no bare-path operation.** Every
  accessor answers from `outputs` and `retained`, `owned_paths()` is their union, and `ProjectionWriter`
  declares only `write(plan)` — so a file the manifest does not list is not reachable by any operation
  this vocabulary declares.
- **One state per file, and duplicates are refused rather than resolved.**
  `_require_one_entry_per_path` rejects a repeated produced path, a repeated retained path, and any path
  present as both; a duplicate would make the next generation's unchanged test depend on which entry a
  reader happened to consult.
- **A path is confined or refused, and the refusal names both the path and the resolved root.** The
  syntactic half refuses absolute, drive-relative, empty, padded, `.`/`..`-bearing and
  staging-directory-naming spellings; `resolved_root` is filled by the resolving caller so requirement
  5.2's "path and root" are both reported.
- **Every collision is reported before either output is written, and no suffix is invented.** Detection
  runs over the whole plan, not as each output is staged, and the two branches catch case- or
  normalization-equivalent paths *and* two records on one identical path; the substrate does not pick a
  winner, does not overwrite, and does not rename around the problem.
- **A rendered artifact cannot exist without its three recorded values.** `RenderedOutput` requires
  `stable_identity`, `source_snapshot` and `renderer_version` with no default, so requirement 4.3's rule
  is a constructor invariant rather than a downstream check.
- **The digest is bookkeeping and not an identity.** `DIGEST_ALGORITHM` is `sha256` and confers no
  identity on the record it projects; the manifest's `digest` and `byte_count` answer only whether the
  file on disk has changed since the substrate wrote it, and no record table declares a
  content-address, logical-digest, fingerprint or manifest-digest column.
- **The refusal closure stays separate from the dataset refusal vocabulary.**
  `ProjectionRefusalCode`'s eight members are deliberately not added to `KnowledgeRefusalCode`, which is
  why the module restates its own closure twice (namespace and `RefusalCode`) instead of widening a
  contract another leaf owns — and `UNAUTHORIZED_OVERWRITE` is declared but unreached by the shipped
  writer in this candidate.
- **The retention vocabulary is wider than the retained reasons the writer produces.**
  `not-owned-by-prior-manifest` names the class of a prior path rather than a case the candidate's
  retention classification constructs for a file still on disk, while the three produced reasons each
  carry a `detail` and the prior `ManagedOutput` kept whole.
- **This module performs no I/O and holds no filesystem behaviour.** It imports neither `os` nor `pathlib`,
  stages nothing and renames nothing; its only side-effect-free helpers are `manifest_relative_path`,
  `canonical_destination`, `detect_destination_collisions` and `require_confined_relative_path`, of which
  `manifest_relative_path` is called by no module or test in the candidate and `canonical_destination` is
  reached only from within this file.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no `Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

The whole vault-safety contract is one vocabulary in this file and one behaviour in
`memory/knowledge/managed_projection.py`: the module docstring names the three structural properties
(the manifest as sole ownership authority, the destination as configuration rather than knowledge, the
three recorded values on every artifact) and states what the manifest digest is not, and the writer's
module docstring turns `Doc13:269`'s eight clauses into eight behaviours. Every row below is a real
range in the working candidate: reading them in order walks the ownership model, the confinement rule,
the collision rule, the digest choice, the closure, the retention states and the protocol.

- The manifest's own file name and format version, the staging directory a render is held in before publication, the accessor that keeps callers from spelling the name themselves, and the staging-and-rename publication that ends by moving the manifest last. [1]
- The declared sibling formats and the renderer profile/version pair, kept as a real recorded value rather than a package version read at display time. [2]
- The four kinds a file on disk can differ from the prior manifest by, and the four reasons a surviving prior output is retained. [3]
- The vault-safety refusal closure — eight members since MIK-R02 added `oversized_row`, declared as a namespace of literals and restated as one type — the refusal shape whose `code` is that type, and the dataset vocabulary it is deliberately not added to. [4]
- One artifact's three recorded values, required rather than defaulted, whose validator refuses a format list that is empty, duplicated or out of the declared sibling order. [5]
- The plan as a whole — its destination, its outputs, and the per-path authorization that is the sole route to replacing an externally edited file. [6]
- The manifest entry: five recorded facts plus the digest material and byte count that answer only whether the file on disk has changed since the substrate wrote it — beside the canonical record columns, which declare no content-address, fingerprint or manifest-digest name for it to become. [7]
- The retained state as its own model, keeping the prior generation's whole entry rather than reducing it to a digest. [8]
- The manifest's declared field set, the public export list it appears in, and the validator that refuses two owners or two states for one file. [9]
- The accessors that make one entry per path safe: the owned-path union, the two keyed lookups, and the digest and identity readers that consult produced first and retained second. [10]
- The per-path outcome vocabulary of six states, the report whose validator refuses a refused run with no refusal or with a resulting manifest, and the discrepancy record whose two digests are optional because a deleted file has no observed bytes. [11]
- The write port as a protocol rather than a base class, whose only operation takes a whole plan and never a bare path. [12]
- The collision record and its refusal, the validator that proves the refusal code, and the case-folded NFC comparison key with the whole-plan detection that reports both paths and both identities before either output is written. [13]
- Both halves of confinement: the syntactic refusal with the builder every rejected spelling goes through, and the resolving check the docstring names as the real-path comparison a string prefix match is not. [14]
- The written behaviour the vocabulary serves — the guard order that reads the prior manifest, refuses collisions, then escapes, then stages and publishes with one rename per output — its retention classification, and the carried-forward retentions that keep a retained file from becoming unowned. [15]
- The frozen, extra-forbidden base every shape derives from, its digest pattern and its three bounded-length constants. [16]
- The cases that measure confinement, collision reporting, the single-owner rule and the collision-refuses-the-plan rule, plus the acceptance case that drives every vault-safety checkpoint in one scenario. [17]

### Cross-Repo References

No cross-repository behavior is implemented in this file. The manifest, the destination profile, the
refusal closure and the writer protocol are properties of one installation's own destination
configuration and one substrate's bookkeeping about files it wrote there; every identity a shape carries
is a store-local record identity or a caller-supplied destination path, and the module imports no store,
no transport and no other repository's vocabulary.

No meaningful cross-repo references found.
