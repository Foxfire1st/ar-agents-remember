# mcp/src/agents_remember/models/knowledge/projection_manifest.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/knowledge/projection_manifest.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T15:30+02:00 |
| lastVerifiedCommitHash | `5e4eb651be0691e2d2a90ea59bc662f92050db25` |
| lastVerifiedCommitDate | 2026-09-18T20:35:53+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l20` uncommitted staged source; base `9f88a6de572dc15bbed1802cf08b77c1193fb24c` |
| governingOverview | `mcp/src/agents_remember/models/overview.md` |

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
**`ProjectionRefusalCode` is a namespace of seven literals, and `RefusalCode` restates that same
seven-member closure as one type.** The members are `destination_escape`, `destination_collision`,
`escaping_link`, `unresolved_projection_input`, `manifest_unreadable`, `destination_unavailable` and
`unauthorized_overwrite`; they are deliberately *not* added to
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
  `ProjectionRefusalCode`'s seven members are deliberately not added to `KnowledgeRefusalCode`, which is
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

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no `Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

The whole vault-safety contract is one vocabulary in this file and one behaviour in
`memory/knowledge/managed_projection.py`: the module docstring names the three structural properties
(the manifest as sole ownership authority, the destination as configuration rather than knowledge, the
three recorded values on every artifact) and states what the manifest digest is not, and the writer's
module docstring turns `Doc13:269`'s eight clauses into eight behaviours. Every row below is a real
range in the working candidate: reading them in order walks the ownership model, the confinement rule,
the collision rule, the digest choice, the closure, the retention states and the protocol.

| Finding | Anchor | Source |
| --- | --- | --- |
| The manifest's own file name and format version, the staging directory a render is held in before publication, the accessor that keeps callers from spelling the name themselves, and the staging-and-rename publication that ends by moving the manifest last. | `PROJECTION_MANIFEST_NAME`; `PROJECTION_MANIFEST_FORMAT`; `manifest_relative_path`; `STAGING_DIRECTORY_NAME` | mcp/src/agents_remember/models/knowledge/projection_manifest.py:76-77; mcp/src/agents_remember/models/knowledge/projection_manifest.py:94-94; mcp/src/agents_remember/models/knowledge/projection_manifest.py:429-432; mcp/src/agents_remember/memory/knowledge/managed_projection.py:782-790 |
| The declared sibling formats and the renderer profile/version pair, kept as a real recorded value rather than a package version read at display time. | `PROJECTION_FORMATS`; `PROJECTION_RENDERER_VERSION` | mcp/src/agents_remember/models/knowledge/projection_manifest.py:81-81; mcp/src/agents_remember/models/knowledge/projection_manifest.py:87-88 |
| The four kinds a file on disk can differ from the prior manifest by, and the four reasons a surviving prior output is retained. | `DiscrepancyKind`; `RetentionReason` | mcp/src/agents_remember/models/knowledge/projection_manifest.py:96-96; mcp/src/agents_remember/models/knowledge/projection_manifest.py:97-102 |
| The vault-safety refusal closure — seven members declared as a namespace of literals and restated as one type — the refusal shape whose `code` is that type, and the dataset vocabulary it is deliberately not added to. | `ProjectionRefusalCode`; `RefusalCode`; `ProjectionRefusal`; `code`; `KnowledgeRefusalCode` | mcp/src/agents_remember/models/knowledge/projection_manifest.py:105-123; mcp/src/agents_remember/models/knowledge/projection_manifest.py:126-134; mcp/src/agents_remember/models/knowledge/projection_manifest.py:137-151; mcp/src/agents_remember/models/knowledge/result.py:161-233 |
| One artifact's three recorded values, required rather than defaulted, whose validator refuses a format list that is empty, duplicated or out of the declared sibling order. | `RenderedOutput`; `source_snapshot`; `DestinationProfile`; `_require_a_declared_format` | mcp/src/agents_remember/models/knowledge/projection_manifest.py:168-176; mcp/src/agents_remember/models/knowledge/projection_manifest.py:179-194; mcp/src/agents_remember/models/knowledge/projection_manifest.py:188-194 |
| The plan as a whole — its destination, its outputs, and the per-path authorization that is the sole route to replacing an externally edited file. | `ProjectionPlan`; `authorized_overwrites` | mcp/src/agents_remember/models/knowledge/projection_manifest.py:197-208; mcp/src/agents_remember/models/knowledge/projection_manifest.py:206-208 |
| The manifest entry: five recorded facts plus the digest material and byte count that answer only whether the file on disk has changed since the substrate wrote it — beside the canonical record columns, which declare no content-address, fingerprint or manifest-digest name for it to become. | `ManagedOutput`; `digest_algorithm`; `byte_count`; `CANONICAL_COLUMNS` | mcp/src/agents_remember/models/knowledge/projection_manifest.py:211-229; mcp/src/agents_remember/models/knowledge/projection_manifest.py:226-228; mcp/src/agents_remember/memory/knowledge/schema.py:47-112 |
| The retained state as its own model, keeping the prior generation's whole entry rather than reducing it to a digest. | `RetainedOutput`; `recorded` | mcp/src/agents_remember/models/knowledge/projection_manifest.py:232-249; mcp/src/agents_remember/models/knowledge/projection_manifest.py:244-249 |
| The manifest's declared field set, the public export list it appears in, and the validator that refuses two owners or two states for one file. | `ProjectionManifest`; `__all__`; `_require_one_entry_per_path` | mcp/src/agents_remember/models/knowledge/projection_manifest.py:47-73; mcp/src/agents_remember/models/knowledge/projection_manifest.py:252-259; mcp/src/agents_remember/models/knowledge/projection_manifest.py:261-281 |
| The accessors that make one entry per path safe: the owned-path union, the two keyed lookups, and the digest and identity readers that consult produced first and retained second. | `owned_paths`; `output_for`; `retained_for`; `recorded_digest_for`; `recorded_identity_for` | mcp/src/agents_remember/models/knowledge/projection_manifest.py:283-289; mcp/src/agents_remember/models/knowledge/projection_manifest.py:291-297; mcp/src/agents_remember/models/knowledge/projection_manifest.py:299-311; mcp/src/agents_remember/models/knowledge/projection_manifest.py:313-320; mcp/src/agents_remember/models/knowledge/projection_manifest.py:322-328 |
| The per-path outcome vocabulary of six states, the report whose validator refuses a refused run with no refusal or with a resulting manifest, and the discrepancy record whose two digests are optional because a deleted file has no observed bytes. | `ProjectionOutcome`; `ProjectionReport`; `_require_one_outcome`; `Discrepancy`; `observed_digest` | mcp/src/agents_remember/models/knowledge/projection_manifest.py:331-339; mcp/src/agents_remember/models/knowledge/projection_manifest.py:342-358; mcp/src/agents_remember/models/knowledge/projection_manifest.py:360-371; mcp/src/agents_remember/models/knowledge/projection_manifest.py:374-386; mcp/src/agents_remember/models/knowledge/projection_manifest.py:382-386 |
| The write port as a protocol rather than a base class, whose only operation takes a whole plan and never a bare path. | `ProjectionWriter`; `write` | mcp/src/agents_remember/models/knowledge/projection_manifest.py:389-401; mcp/src/agents_remember/models/knowledge/projection_manifest.py:400-401 |
| The collision record and its refusal, the validator that proves the refusal code, and the case-folded NFC comparison key with the whole-plan detection that reports both paths and both identities before either output is written. | `Collision`; `DestinationCollision`; `_require_the_collision_code`; `canonical_destination`; `detect_destination_collisions` | mcp/src/agents_remember/models/knowledge/projection_manifest.py:404-413; mcp/src/agents_remember/models/knowledge/projection_manifest.py:416-420; mcp/src/agents_remember/models/knowledge/projection_manifest.py:422-426; mcp/src/agents_remember/models/knowledge/projection_manifest.py:435-445; mcp/src/agents_remember/models/knowledge/projection_manifest.py:448-488 |
| Both halves of confinement: the syntactic refusal with the builder every rejected spelling goes through, and the resolving check the docstring names as the real-path comparison a string prefix match is not. | `require_confined_relative_path`; `_escape_refusal`; `resolve_inside_destination` | mcp/src/agents_remember/models/knowledge/projection_manifest.py:491-516; mcp/src/agents_remember/models/knowledge/projection_manifest.py:519-525; mcp/src/agents_remember/memory/knowledge/managed_projection.py:100-123 |
| The written behaviour the vocabulary serves — the guard order that reads the prior manifest, refuses collisions, then escapes, then stages and publishes with one rename per output — its retention classification, and the carried-forward retentions that keep a retained file from becoming unowned. | `write`; `os.replace`; `_retention_reason`; `_carried_retentions` | mcp/src/agents_remember/memory/knowledge/managed_projection.py:271-287; mcp/src/agents_remember/memory/knowledge/managed_projection.py:513-523; mcp/src/agents_remember/memory/knowledge/managed_projection.py:625-646; mcp/src/agents_remember/memory/knowledge/managed_projection.py:672-679 |
| The frozen, extra-forbidden base every shape derives from, its digest pattern and its three bounded-length constants. | `KnowledgeModel`; `SHA256_PATTERN`; `PROSE_MAX_LENGTH`; `REFERENCE_MAX_LENGTH`; `LABEL_MAX_LENGTH` | mcp/src/agents_remember/models/knowledge/base.py:19-19; mcp/src/agents_remember/models/knowledge/base.py:24-26; mcp/src/agents_remember/models/knowledge/base.py:34-37 |
| The cases that measure confinement, collision reporting, the single-owner rule and the collision-refuses-the-plan rule, plus the acceptance case that drives every vault-safety checkpoint in one scenario. | `test_a_path_that_is_not_purely_destination_relative_is_refused`; `test_a_case_collision_names_both_paths_and_both_records`; `test_a_collision_refuses_the_whole_plan_before_either_output_is_written`; `test_the_manifest_refuses_two_owners_for_one_path`; `test_the_vault_safety_contract_holds_for_all_eight_checkpoints_in_one_scenario` | mcp/tests/test_knowledge_views_and_projection.py:353-367; mcp/tests/test_knowledge_views_and_projection.py:370-383; mcp/tests/test_knowledge_views_and_projection.py:540-557; mcp/tests/test_knowledge_views_and_projection.py:662-678; mcp/tests/test_knowledge_projection_vault_safety.py:83-116 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. The manifest, the destination profile, the
refusal closure and the writer protocol are properties of one installation's own destination
configuration and one substrate's bookkeeping about files it wrote there; every identity a shape carries
is a store-local record identity or a caller-supplied destination path, and the module imports no store,
no transport and no other repository's vocabulary.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T19:56:02+02:00 — 260915-KS-L23 residue clearance, seat B (uncommitted change set on `ar/260915-ks-l23`, memory base `59eab7a0`): **cleared the two enforced `citation_anchor_absent_from_range` rows in this document** (one table row, two anchors). The confinement/collision row cited `views_and_projection.py:370-382` for `test_a_case_collision_names_both_paths_and_both_records`, defined at `383`, and `662-676` for `test_the_manifest_refuses_two_owners_for_one_path`, defined at `678`. Both ranges were widened to the definition they name (`370-383`, `662-678`); the `540-557` and vault-safety ranges and the claim are unchanged. No claim was re-worded, no anchor or range was dropped to silence a row, and no verification stamp advanced: the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-18T15:30+02:00 — 260915-KS-L20 curator (uncommitted change set on `ar/260915-ks-l20`, base `9f88a6de`): created this one-to-one card for the managed-external-projection vocabulary. It records the four properties the shapes enforce rather than document — the manifest as the only authority on ownership with no bare-path operation, confinement in its syntactic half with the resolving half owned by `managed_projection`, whole-plan collision detection before either output is written, and the three non-optional recorded values on every artifact — together with the declared staging directory and rename publication, the `sha256` digest choice that confers no identity on the record it projects, the seven-member refusal closure kept out of the dataset vocabulary, the retention states that keep a retained file from becoming unowned, and the two documented absences this candidate actually shows (`UNAUTHORIZED_OVERWRITE` reached by no code path, and one declared retention reason the writer's classification does not construct for a file still on disk). This card carries **no `lastVerifiedCommitHash`**: every construct it cites exists only in this leaf's uncommitted candidate, so no real commit contains the content a stamp would claim to have verified. The `reviewedWorkingCandidate` row states what was actually read, and closeout owns the stamp once the code commit exists.
