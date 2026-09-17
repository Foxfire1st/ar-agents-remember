# mcp/src/agents_remember/memory/ - Memory Repository Lifecycle And Knowledge Storage Overview

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `mcp/src/agents_remember/memory/` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-09-17T19:11+00:00 |
| lastVerifiedCommitHash |  `9c12e8b1ec027b8bb07f4c0cc79ef99a655ff890`|
| lastVerifiedCommitDate |  2026-09-18T01:58:08+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l08` uncommitted source; base `1ff1893f44d875073d58af863238501a6be35288` |
| governingOverview | `../../../overview.md` |

## Governing Overview

[mcp/overview.md](../../../overview.md)

## What This Area Is

The route owns two distinct responsibilities, and they are deliberately not the same thing:

1. **Memory-repository lifecycle** (`baseline.py`, `carryover.py`, `carryover_authority.py`) — initializing a
   memory repository, adopting an existing onboarding tree as a first ledgered baseline, and carrying richer
   onboarding from a source branch into an open recovery leaf.
2. **Concrete knowledge storage** (`knowledge/`) — the APSW-backed SQLite candidate that holds repository,
   invariant, revision, family, anchor, membership and realization identity, and since 260915-KS-L10 also the
   `Route` scope entity and the typed record envelope. Added by 260915-KS-L1 as an experimental increment and
   extended by every leaf through 260915-KS-L10; it is a durable record store, so it ranks here with the record
   stores rather than with the application layer that admits its writes.

The two responsibilities share a package rank and a charter paragraph, not a mechanism: nothing in the
lifecycle modules imports `knowledge/`, and nothing in `knowledge/` reads, writes or migrates Markdown onboarding.

## Purpose

`memory/` is the durable-store route. Its members own the on-disk representation of two different things — a
repository's onboarding tree and an authored knowledge candidate — and both are stores that a higher-ranked
admitted authority writes through rather than authors.

## Hot Path Summary

`knowledge/candidate.py` owns the **one admitted multi-record write boundary** (`change_candidate`): one lock, one
`BEGIN IMMEDIATE`, a closed twelve-command union, and an all-or-nothing refusal. Everything else in the storage
package is composed by it or called through it. `knowledge/batch_preconditions.py` holds every read-only
precondition (including the completed-graph lineage pass), `knowledge/batch_commands.py` is the only module that
applies a batch and the pass that re-proves the rows it left, `knowledge/candidate_records.py` is the identity
vocabulary both read, and `knowledge/merge.py` owns **the guarded common-base merge** — the package's composition of base resolution,
structural preflight, changeset production, coverage replay, aborting application, postcondition validation and
publication, in that order — with `knowledge/merge_base.py` (dataset identity, the closed base claim and its Git
ancestry adjudication), `knowledge/merge_schema.py` (the declared-structure preflight that runs before any session),
`knowledge/merge_changeset.py` (deltas, their materialised operations and the coverage replay),
`knowledge/merge_validation.py` (the result's postconditions and the inputs' integrity) and
`knowledge/merge_refusals.py` (the merge's refusal vocabulary) beneath it; `knowledge/logical.py` owns the canonical logical dataset identity.
`knowledge/store.py` owns the one insert-only single-record revision operation, the package's shared candidate lock
and its one-immediate-transaction wrapper, and the invariant half's tables; `knowledge/{families,anchors,memberships,realizations}.py`
own the four graph concepts and their tables, `knowledge/lineage.py` owns the one acyclic-lineage rule both lineage
graphs apply (including the batch's declared-edge caller), `knowledge/labels.py` owns the two label edits and their
row-digest guard, and `knowledge/endpoints.py` owns the shared relation-endpoint check; `knowledge/schema.py` owns the
declaration of generation 1's ten STRICT tables, its fifteen immutability triggers and the structural manifest and
fingerprint of a *generation record*; `knowledge/schema_generations.py` owns **which generations exist** — generation
1 pinned as data with its fingerprint constant and drift gate, generation 2 = generation 1 plus `knowledge/schema_v2.py`'s
six appended tables — and the dispatch that selects one from the dataset rather than from the running build;
`knowledge/record_envelope.py` owns the one payload-admissibility seam; `knowledge/routes.py` owns the route
confinement rule, the acyclic-hierarchy walk and the route/association write and read operations;
`knowledge/connection.py` owns the pragma contract, the one-row reader, the read-only connection every identity
confirmation uses, and the open-time schema validation; `baseline.py` / `carryover.py` / `carryover_authority.py`
own baseline adoption and branch carryover. **The snapshot half** lives in `knowledge/candidate_workspace.py`
(create, resume, clone, disposal verdict), `knowledge/candidate_receipt.py` (the sealed receipt and its binding
comparison), `knowledge/closed_snapshot.py` (the one freeze procedure both publication and cloning use, and the
shared `require_closed_database` step every producer of a finished database file closes through),
`knowledge/publication.py` (atomic, verifiable install under a destination lock, plus the public admission reading),
`knowledge/materialization.py` (the read-side publication gate), and `knowledge/logical.py`'s `dataset_identity`
entry point. **The portable half** is `knowledge/export_portable.py` (the `ar-knowledge-export/v1` format, its one
encoder and the reader that accepts only that encoder's own rendering), `knowledge/export_import.py` (the export and
import operation, its private stage and its staged sealed-aggregate verification), and
`knowledge/export_refusals.py` (the boundary's refusal vocabulary), with the artifact's header carrying the *same*
logical digest `knowledge/logical.py` defines — there is one digest definition, not two. The import
direction is enforced: no package ranked below `memory` (rank 12) may import `memory.knowledge`, and `application`
(rank 21) is its only consumer. **The read half** is `knowledge/read.py` (the requirement's finite selection policy,
executed once over one snapshot, plus whole-item paging over an already-selected scope),
`knowledge/read_queries.py` (one statement per lookup, all on the caller's connection), `knowledge/read_anchors.py`
(the anchor observation against the requested code tree) and `knowledge/read_refusals.py` (the read's refusal
vocabulary), with `knowledge/logical.py`'s public `cell_value` as the one decoder a read page and the logical
digest share.

## Detailed Route Context

### 260915-KS-L1 Experimental Knowledge Storage Responsibility

This route gained a new responsibility and no new authority. The leaf added `memory/knowledge/` (six modules), its
shared vocabulary `models/knowledge/` (nine modules) and its composition seam `application/knowledge.py`, then
declared the storage home in one *wording* paragraph of `[package.memory]` in `layers.toml` — no rank, order or
sequencing entry moved, which is the narrow charter change the leaf document permits.

What the storage package does and does not own, stated once here because a reader of this route needs the
boundary before the mechanism:

- **Owns:** the versioned SQL schema (`ar-knowledge-sqlite/v1`, `SCHEMA_USER_VERSION = 1`), the row codecs, the
  connection/pragma contract, and one atomic insert-only revision operation with its typed refusals.
- **Does not own:** approval, acceptance, task status, Git resolution or commit attribution. The store
  manufactures no acceptance and exposes no update, delete or upsert path; `kernel/memory_attribution.py` remains
  the Git attribution owner and nothing from it was copied into the store.
- **Serves:** the requirement `KS-R01@v1` — a canonical invariant revision stays immutable and unambiguously
  addressable after successor revisions are added, including concurrent successors carrying the same display
  version.

The four properties and their mechanisms: opaque UUID revision identity separates identity from the friendly
display version (two successors may both display `v2`); the `payload_digest` seal covers the whole authored
aggregate including the sorted predecessor set, so a re-pointed edge fails the read-time recomputation; database
triggers — not only the operation — refuse an update to a sealed row, so a changeset, a repair script or a
forgotten code path still cannot rewrite a citation; and every table keys on `repository_id`, so a foreign
namespace refuses as `unauthorized_scope` before any DML.

### 260915-KS-L2 The Graph Half Of The Knowledge Store

This route's storage package gained its **relation half**: family identity and sealed family revisions, source
anchors, exact-revision memberships and realization claims, plus the reads that answer from both directions. Six
modules were added (`families`, `anchors`, `memberships`, `realizations`, `endpoints`, `lineage`) and four existing
ones changed. `schema.py` was **not** touched: the six tables and their indexes already existed in version 1, so
the schema generation and `schema_fingerprint()` are unchanged. The leaf also repaired two latent L1 defects
(`SourceAnchor.anchor_id` was unconstructible; `map_sqlite_error` reported the wrong operation and table for every
non-invariant caller), and those repairs are recorded in `models/knowledge/source.py.md` and
`knowledge/refusals.py.md` rather than here.

What the graph half owns, stated once because a reader of this route needs the boundary before the mechanism:

- **One canonical stored identity per authored relationship.** `family_member` and `realization_claim` are the only
  owners of the two relations. Their declared unique tuples plus the operations' pre-checks make a second row for
  the same pair a `relationship_constraint` refusal naming the stored identity; there is no second, separately
  maintained list of semantic facts anywhere in the package, and the forward and reverse reads select the same
  table with the same column list. That is why the two directions can be compared by **identity** rather than
  reconciled.
- **A relation cites revisions, not identities.** A membership relates an exact family revision to an exact
  invariant revision, so a newer family revision needs its own explicitly authored membership instead of
  inheriting one through a moving `current` pointer.
- **A graph-valid claim is still only a claim.** The realization role is a closed authored vocabulary with an
  explicit `unclassified` member and the rationale is the author's sentence; no reader infers either from the
  source. Storage and resolution are separate concerns: an anchor records the repository-relative path, the source
  identity and the locator and is written and read back without consulting a filesystem, a Git object or a parser,
  so a missing source changes what a later resolver reports and never retires a stored attribution. Resolution
  belongs to `KS-R07`.
- **Removal is explicit and never repoints.** A removal names the row digest the caller expects, so a stale caller
  is told rather than obeyed; the earlier dataset keeps the removed row, which is what makes a before/after
  comparison meaningful without an always-current pointer.
- **One rule, two graphs.** The acyclic-lineage rule left `store.py` for `knowledge/lineage.py` so the invariant
  lineage and the family lineage apply it once. The reach is deliberately wider than adjacency: a candidate is
  refused when it would be on a cycle **or** when a retained revision reachable from it is already on one, and the
  refusal names which branch applied.

**Disclosed limitation — read this before treating the family identity row like the invariant one.** The `family`
identity table carries **no** immutability trigger, while `invariant` carries both a no-rebind and a no-delete
trigger. `UPDATE family SET display_label …`, `UPDATE family SET label_provenance …` and `DELETE FROM family` on a
row no `family_revision` references are therefore **permitted by the database**; the only protections are the
deferred foreign key from `family_revision` (which protects a family that has revisions) and the operation-level
label check. This matches the v1 design, whose trigger requirement covers revision rows and relation payloads only,
and `KS-R02@v1` forbids none of it — so it is recorded as a **disclosure and a `v2` decision**, not as a v1 defect.
Adding the two triggers changes `schema_fingerprint()`, which the `KS-R05` merge preflight compares, so it needs
the declared `ar-knowledge-sqlite/v2` route and belongs to the owning seat. The same reasoning records that an
anchor's, membership's and claim's **identity** columns are not covered by their payload-only triggers; a repointed
`repository_id` is caught only by the deferred foreign key at `COMMIT`.

All ten canonical tables are now reachable through operations. The six the graph half added are written by the
graph modules rather than by `store.py`, which still writes only `repository`, `invariant`, `invariant_revision`
and `invariant_predecessor`. The eager declaration of the whole schema in version 1 remains deliberate: a SQLite
session changeset can only carry operations for tables both sides already have, and a table present on one side
only is exactly the schema mismatch the merge preflight must refuse. Later leaves extend behaviour inside a stable
schema instead of migrating it.

The lineage rule is the one place where the code states a contract twice on purpose, because it lives in one module
and is applied by two. `store.create_revision` refuses as `lineage_cycle` when inserting the candidate would leave
**any** revision in the invariant's lineage graph on a cycle — the candidate itself, or a retained revision
reachable from it through predecessors — and `families.create_family_revision` applies the same rule over
`family_predecessor`. The guard is evaluated over the post-insert graph and before any row is written. A revision
that merely descends from a stored cycle is therefore refused even though its own lineage is acyclic, and the
refusal says so rather than claiming self-reachability.

### 260915-KS-L3 The One Typed Write Boundary

This route gained the substrate's **single mutation entry point** and no new authority. Six modules were added
(`knowledge/{candidate,candidate_records,batch_preconditions,batch_commands,labels,logical}.py`) and seven changed
(`knowledge/{store,anchors,families,memberships,realizations,lineage,refusals}.py`); `schema.py` was **not**
touched, so the schema stays `ar-knowledge-sqlite/v1`, `PRAGMA user_version = 1`, ten tables, fifteen triggers and
the same `schema_fingerprint()`.

What the batch boundary owns, stated once because a reader of this route needs the boundary before the mechanism:

- **One lock, one transaction, one writer.** `change_candidate` takes the candidate's exclusive lock, opens one
  `BEGIN IMMEDIATE`, and composes the per-concept helpers the single-record operations already use. Those helpers
  are published and assume the caller holds the lock and the transaction — that is what makes a multi-command batch
  possible without nesting a second transaction, and nothing enforces it (the disclosed exposure).
- **All-or-nothing is a measured property, not a promise.** A refusal returns `after == before` and the transaction
  has rolled back; the evidence is a node that fails when the rollback is mutated to a commit, plus refusal cases
  that measure table counts and the logical digest through a separately opened store.
- **Validation is over the completed graph.** A revision may declare a predecessor any command in the same batch
  creates, wherever it sits in the sequence; `lineage.declared_cycle` judges the batch's own declarations through the
  shared rule (`extra_predecessors` is supplied only there), and an intra-batch cycle is refused by name before any
  row exists. The after-integrity pass re-proves both stored graphs.
- **The lane boundary fails closed.** `baseline` is refused by name (`target_not_candidate`) before the lock, and
  `task-candidate` refuses `unauthorized_scope` until a resolved, owner-validated task binding can be required and
  checked — this increment writes **only** `draft-candidate`, and the packet's task-authority sentence is satisfied
  by refusing rather than by trusting a caller's reference.
- **The dataset identity is resolved, never asserted.** `application/knowledge.py` reads it from the live candidate
  and seals it into the context; the operation re-derives the seal and compares the logical digest inside its own
  transaction. A stale batch is refused with both digests named and is never silently rebased.
- **The receipt is factual and closed.** `MutationResult` reports before/after identities and the rows the batch
  wrote or removed, with `state` exactly `written | removed`; a removal is reported with the digest the row had, and
  a command whose effect was already stored contributes no entry. There is no field a semantic verdict could occupy.

**Two carried limitations belong in this account rather than being rediscovered.** The refusal *code* `no_change`
still has no producer — only the *result state* `MutationResult.state == "no_change"` is reachable, and a consumer
must not branch on the code. And `application/knowledge.py` still has **no non-test importer in `mcp/src`**: the
batch boundary exists inside the seam, but the seam is wired to no tool or entry point, which is what the packet
means by "public MCP names and transport wiring are later extensions".

### 260915-KS-L4 The Candidate Lifecycle And Snapshot Publication

This route gained the **snapshot half** and no new authority: six new modules
(`knowledge/{candidate_workspace,candidate_receipt,closed_snapshot,publication,materialization}.py` plus the
second composition seam in `application/knowledge_snapshot.py`), with `connection.py`, `store.py`, `logical.py`
and `refusals.py` changing and `schema.py` **not** touched — the schema stays `ar-knowledge-sqlite/v1`,
`PRAGMA user_version = 1`, ten tables, fifteen triggers and the same `schema_fingerprint()`.

What the snapshot half owns, stated once because a reader of this route needs the boundary before the mechanism:

- **A candidate is a local working object, and its identity is read rather than asserted.** The directory holds one
  writable database plus the sealed receipt that binds it to its admission; the receipt deliberately carries **no**
  dataset digest, so a caller cannot hand-write the identity its publication will be compared against. Creation is
  two-phase (build and verify privately, then expose the complete directory), an occupied destination is refused
  as a resume attempt, and a clone comes from a *closed* representation produced by the same freeze publication
  uses — never from a WAL-dependent main file.
- **A published snapshot is closed, and closedness is proven.** The freeze pins a read view, copies through
  SQLite's own backup so a committed-but-WAL-resident batch is included and an uncommitted writer's rows are not,
  establishes the `delete` journal mode on a fresh connection to the finished copy (a backup destination *inherits*
  the source's mode), reopens it read-only to prove no peer and the pinned dataset, and flushes the file's own data
  before anything renames it.
- **Publication is replace-or-nothing, against an admitted identity.** The destination lock is a hidden `flock`
  resource beside the file it protects, and an identical logical dataset returns `no_change` with the existing
  bytes retained — page layout is not knowledge, and rewriting would dirty a memory tree for nothing observable.
- **A read gates on the comparison and never resolves it.** `materialization.publication_state` reports
  `current` or `candidate_snapshot_unpublished` with both identities and leaves the decision to the caller; no read
  publishes rows or attaches them to an older memory tree.
- **Disposal is a verdict, not a deletion.** A `discard` must name the identity the candidate holds *now* (so an
  authorization cannot be replayed against newer unpublished work) and a `published` disposition must point at a
  database that reopens to that same logical dataset. Removing the directory stays with the enclosure owner.

**The durability correction this leaf carried is the reason two long-standing cards changed.** `store.close()` no
longer unlinks WAL/SHM peers, and `connection.discard_closed_wal_peers` now states a caller precondition instead of
a close-time rule: the unlink could not know whether another connection held the database, a reader holding a read
transaction blocks the checkpoint that would have made it safe, and an unconditional call destroyed a committed
batch. SQLite removes its own peers on the last clean close, so the call was removed rather than made conditional.
`connection` also gained `open_read_only_database` (the connection every identity confirmation uses, so a check
cannot repair what it checks) and `journal_mode`.

**Two carried limitations and one disclosure belong here rather than being rediscovered.** `application/
knowledge_snapshot.py` — like `application/knowledge.py` — has **no non-test importer in `mcp/src`**: the lifecycle
and publication exist inside the seam, with no tool wired to them. `authorization_ref` on a disposal is **carried
but never examined**, because permissibility is this layer's question and the approval chain is the caller's.
And the `kernel/atomic_write.py` directory fsync runs **after** `os.replace`, so a post-rename failure is reported
as a replace failure — which is why a create can answer `destination_occupied` for the destination holding the
complete candidate it just created, and why a publication can return `publication_failed` where
`publication_durability_unconfirmed` would be the honest code. The non-claim narrows again: the still-unclaimed
behaviour is now **L6–L8** (portable roundtrip, selective read and candidate diff): the Git-side merging half
is delivered by the L5 section below.

### 260915-KS-L5 The Guarded Common-Base Merge

This route gained the **merge half** and still no new authority: six new modules
(`knowledge/{merge,merge_base,merge_schema,merge_changeset,merge_validation,merge_refusals}.py`), the third
composition seam in `application/knowledge_merge.py`, and **no change to `schema.py`** — the schema stays
`ar-knowledge-sqlite/v1`, `PRAGMA user_version = 1`, ten tables, fifteen triggers and the same
`schema_fingerprint()`. This is the route's largest increment so far and it is deliberately built as a sequence in
which each step exists because the step before it cannot see what it prevents:

- **The base is proven, never chosen.** A merge is defined by its base, and the failure this route refuses is the
  quiet one: picking *some* commit (an arbitrary `git merge-base` result, or `HEAD` as a stand-in) and producing a
  delta against a base neither side descends from. The claim is a closed two-member union — a caller-supplied
  commit, or a claim the ancestry evidence must confirm as the **unique** common base — and zero bases, several
  bases, or one base that is not the claimed commit all refuse. Nothing here reads a Git object to decide what a
  dataset *is*: the datasets are identified by their own logical digest.
- **The declared structure is checked before a session exists.** SQLite's changeset application can silently skip a
  table it cannot match, so an input that is not this schema generation would produce a green merge over a dropped
  change set. Each input is compared against the one declared manifest (derived from the DDL that creates a
  database rather than from a second description of it), and an input carrying a table outside the manifest is
  refused rather than merged around. There is exactly one comparison per input and no pairwise pass: every accepted
  input is identical to that one declaration, so a second pass could only fire for an input the first had already
  refused.
- **A delta is a changeset, never a patchset, and its coverage is proven by replay.** A patchset carries only the
  new values, so applying it cannot detect that the target row moved; the session is asked for `changeset()` and
  never for `patchset()`, every operation is materialised before the cursor advances, and each delta is replayed
  into a fresh copy of the base, where it must reproduce its side's whole logical dataset. That replay is the only
  place an omitted table is observable: the application reports success either way.
- **Application aborts whole.** `flags=0`, no filter, and a conflict callback that returns
  `SQLITE_CHANGESET_ABORT` unconditionally: the first blocking conflict rolls the whole application back rather
  than continuing with `OMIT` to collect a cosmetically complete list, and neither side is ever preferred.
- **The conflict record names the row the engine refused.** The key is copied out of the change the callback held —
  read from the operation's **old** values, because a changeset omits the columns an operation does not change and
  an `UPDATE`'s key columns are unchanged, so its new side carries the not-supplied marker where the key is — and
  it is never reconstructed from the changeset, because the first operation a changeset carries for a table is not
  necessarily the operation that conflicted. Where the engine genuinely supplies nothing (a foreign-key conflict
  hands the callback no change at all) the record says so and names no row and no count.
- **Publication is the last step and reuses the existing contract.** The merged temporary is frozen through the
  same closed-snapshot procedure the snapshot half uses, under the temporary's own resource lock, and installed
  through the same destination-admitted publication. The two locks are sequential, never nested — this route takes
  one resource lock at a time, which is why the merge never needs a second.

**The result carries no verdict, and that is the contract rather than an omission.** `structurally_merged` is the
only non-refusal state; there is no compatibility, acceptance, approval or "harmless" field, and nothing on this
path decides whether the merged knowledge is *correct*. Two collision shapes are refused even though a weaker
policy would have merged them: a same-identity independent insert on both sides is a conflict **even when the two
payloads are byte-identical** (two authored acts that happen to collide are not one act), while two newly authored
successors of one invariant are **not** a data conflict and both survive — the two shapes are measured separately
rather than lumped together.

**Three facts about this increment belong here rather than being rediscovered.** First, the adapter is
**callable rather than wired**: no Git merge driver, attribute or config is installed anywhere on this path, and
that activation is an explicit later decision. Second, two postcondition guards are recorded as
**non-experiments** — the applied-change check and the merged-candidate immutability check cannot be reached by a
black-box case under this schema, and the freeze's contribution is invisible to a case — so their policies are
exercised directly and their call-site unreachability is stated where the code is, rather than a broken mutation
being scored as a covered guard. Third, two facts about the pinned SQLite build are recorded as **facts, not
excuses**: it supplies no foreign-key conflict row identity or count, and a stale `DELETE` is a silent no-op for
which the operation claims no guard. A merge that skipped a table and reported success — the requirement's own
non-conforming example — is refused by two independent measures, and that is the class this half exists to close.

### 260915-KS-L6 The Portable Logical Artifact

This route gained the **portable half** and still no new authority: three new modules
(`knowledge/{export_portable,export_import,export_refusals}.py`), the fourth composition seam in
`application/knowledge_export.py`, and **no change to `schema.py`** — the schema stays
`ar-knowledge-sqlite/v1`, `PRAGMA user_version = 1`, ten tables, fifteen triggers and the same
`schema_fingerprint()`. Three existing storage modules changed, and each change is small and load-bearing:
`logical.py` gained the shared body constructor, `closed_snapshot.py` gained the shared closure step, and
`publication.py` exposed its admission reading.

**The guarantee this leaf makes true is the thing to read first, and the only form a consumer may rely on:**

> **Every accepted artifact is the canonical rendering of the logical content it carries.** Two artifacts
> that both validate and declare the same `logicalDigest` are therefore the same bytes, and a dataset
> restored from an accepted artifact re-encodes to that artifact byte for byte.

The artifact is a **canonical form**, not a tolerant interchange document, and acceptance is **two** checks
that are both needed for that sentence:

- **The whole-document gate.** `parse_export` re-renders the document it parsed and refuses the text unless
  it is that rendering **exactly** — the envelope's key order, the declared manifest order of the ten tables,
  each row's declared column order, compact separators, no insignificant whitespace, literal Unicode, and the
  sorted keys inside every typed JSON value. A JSON escape that spells the same character, an extra space, a
  reordered header and a reordered table are each a **different document** of one dataset and all are refused
  (`invalid_export`, `record_id == "<canonical document>"`) with a bounded statement of where the text
  diverges. **Nothing is repaired**: normalising would accept a document nobody can reproduce from the bytes
  that were handed over.
- **The header check.** Every header *declaration* must be the one this build implements **and of the type
  this build writes**. `format`, `schema` and `schemaFingerprint` are compared by equality against this
  build's strings, `logicalDigest` and `repositoryId` by an `isinstance` guard, `tables` must be a JSON
  object, and **`userVersion` is compared type-strictly** — so `1.0` and `true`, which Python's `==` calls
  equal to `1`, are refused **by name** as unsupported generations rather than silently compared equal. All
  seven envelope keys respelled with a different JSON type are refused, and each passes the whole-document
  gate, which is what proves the refusal is the header check's.

**What the digest covers, and what the document form covers instead** — a consumer comparing a hash should
know which is which:

| Inside `logicalDigest` | Outside it, pinned by the document form |
| --- | --- |
| the schema fingerprint and every canonical record — all ten tables' rows, in the digest encoding's sorted-key order | the envelope's field order; the declared manifest order of the tables; each row's declared column order; the canonical spelling of every value; **and the JSON type of every header value** |

The digest excludes itself by design, and it does **not** cover the header's types; the reader does. Two
artifacts can share a digest while differing on those axes, and the reader refuses every such artifact —
which is exactly why a byte or content-hash comparison across **accepted** artifacts is sound.
`logical_digest` remains the primary contract and is what to compare when in doubt;
`artifact_digest(text)` is the sha256 of the artifact's exact UTF-8 bytes and is now a function of the
dataset. **A foreign producer must write the canonical form, header types included**; a later leaf that
needs to accept other spellings needs a **new format member with its own reader**, never a tolerant read of
`ar-knowledge-export/v1`.

**The import never patches a live destination, and it proves its stage before publishing.** The artifact is
validated completely *before* any database exists (document shape, manifest, canonical gate, header, declared
column order and types, primary-key uniqueness, namespace binding, recomputed seal); the destination is
admitted before any staging work, as a **closed two-mode choice** (`expected_destination=None` means "expected
absent", so an occupied destination is `destination_occupied`; an explicit identity means "expect exactly
this", so an absent one is `destination_stale`) with no third mode; the stage is a **private** database built
elsewhere, loaded in one transaction with deferred foreign keys, and verified there — foreign-key read,
**every retained revision's `payload_digest` re-derived through the shared decoders**, typed aggregates read
back, the whole logical digest recomputed, and the closure proved through the same
`require_closed_database` the freeze uses. Only then does `publish_prepared_snapshot` install it on exact
digest equality, retaining the existing bytes when they already hold that knowledge.

**One digest definition, not two.** `logical_body_from_tables` / `logical_digest_of_tables` are now the one
body constructor, and the export path seals a table mapping it *decoded from an artifact* through them —
the same value `logical_digest` / `dataset_identity` returns for a dataset, which is what makes the artifact
restorable at all. A second assembly of `body_version`/`schema`/`user_version`/`schema_fingerprint` would
have been a second digest definition, and a difference between the two would produce an export that cannot be
re-imported.

**Four facts about this increment belong here rather than being rediscovered.** First, the encoder has **no
filesystem side effect**: `ExportResult.artifact` is text, and a caller that wants it on disk writes it
through the repository's own atomic write. Second, the import creates **no Git commit and restores no Git
ancestry** — a database-only artifact reconstructs the dataset, not the memory-commit history — and importing
a row whose `state_at_origin` says `accepted` imports that *value* and grants the receiving context no
authority. Third, the destination directory holds the published database **and** L4's `.lock` resource, and
whether a memory-tree capture enumerates files or the directory is L4's open question Q1, carried forward
rather than answered here. Fourth, two staged checks are recorded as **documented non-experiments** rather
than coverage: the staged digest equality cannot be falsified by a black-box case (the rows loaded are the
rows validation already proved produce that digest), and `_binding`'s scalar guard is unreachable behind the
row reader. One guard the leaf does **not** claim is the header's namespace-binding check
(`export_portable.py:911`): reachable and verdict-changing, with no killing node — reported as an observation
for **L9**.



### 260915-KS-L7 The Selective Recorded-Scope Read

This route gained **the read half** and still no new authority: four new modules
(`knowledge/{read,read_queries,read_anchors,read_refusals}.py`), the fifth composition seam in
`application/knowledge_read.py`, and **no change to `schema.py`** — the schema stays
`ar-knowledge-sqlite/v1`, `PRAGMA user_version = 1`, ten tables, fifteen triggers and the same
`schema_fingerprint()`. Two existing storage modules changed, and each change is small and load-bearing:
`logical.py` gained the public `cell_value` (the one decoder a read page and the digest share), and
`base.py` gained `require_plain_git_path` (the one Git-pathspec rule both typed path boundaries apply).

**The selection policy is the requirement's own table, and its stopping rule is the load-bearing design
fact: the containing-family set is frozen *before* membership expansion.** Reading `P`, `I1` or exact `F`
in the packet's `P → I1`, `F → {I1, J1}`, `G → {J1, K1}` graph returns I1's and J1's realizations,
**advertises** J1's `G` membership, and **excludes K1** until `G` is selected explicitly in a subsequent
expansion. The frontier is `memberships_of(I) − F0`, advertised and never traversed — a sibling's
membership in another family is a recorded fact the caller can act on, not permission for this read to walk
that family.

**Three properties a consumer may rely on, each enforced at model construction rather than by discipline:**

- **A page's counts describe the declared selected set, not the remaining tail.** `primary_items_total` is
  the same number on every page of the walk, `primary_items_returned` is the walk's cumulative figure, and
  the slice size is `len(page.items)`. The three satisfy `returned + remaining == total` **at every
  position**, and `KnowledgeReadCounts` refuses its own arithmetic contradiction. Round 1 of this leaf's
  review sealed this as a defect: restating the total as the tail makes page 2 of a 17-item walk report 16
  and the last page 1 — the requirement's own non-conforming example, *"a one-item page implies that the
  invariant has only one implementation"*.
- **A truncated page can never be presentable as a complete family.** `KnowledgeReadPage` refuses to exist
  with `has_more == enumeration_complete`, or with `has_more` disagreeing with the presence of a
  continuation.
- **Nothing in the response can be read as a verdict or a current pointer.** Every statement, role,
  rationale and lifecycle crosses as the authored text it is stored as; the models have **no field** that
  could hold a "current", "accepted", "severity" or "ranked" marker, which is how the requirement's
  *Forbidden Overreach* is enforced structurally. An identity seed returns every retained revision grouped
  by identity, and a display version selects nothing.

**The path-refusal contract is the one review corrected most sharply, and the correction is the interesting
part — a refusal must describe the actual cause.** Git pathspec **magic** is the leading-`:` family
(`:(exclude)`, `:!`, `:(top)`, `:/`) plus `..`, absolute paths, `~`, drive/UNC spellings, backslashes and
NUL; the glob characters `*`, `?` and `[` are **literal characters** to `ls-tree` (measured on
`git 2.54.0`), so a legitimate anchor containing them must be authorable, seedable and resolvable. Round 1
refused them, which made such an anchor un-authorable and reported a file the tree really holds as
`path_absent` — *a false statement about the repository rather than a refusal of a malformed spelling*. The
read path therefore distinguishes **three genuinely different facts**, and a caller must never be told a
path is absent when the real reason is its spelling:

| Outcome | The fact |
| --- | --- |
| `path_absent` | Git answered, and the requested tree holds nothing at that path |
| `unsupported_locator` | the spelling is not addressable, so the tree was never asked; the cause is in `detail` |
| `recorded_object_unavailable` | the lookup did not answer: the tree is absent, or Git ran and failed, or Git could not be run at all |

The same rule was applied to the leaf's other refusal sites — `registration_absent` fires only for a path
with no recorded claim, `selector_absent` only for an identity the snapshot does not hold, and each
`snapshot_unavailable` variant names the comparison that fired.

**Two honest limits belong here rather than in a footnote.** `_tree_entry`'s **non-zero-exit** branch is
reachable by no input on this host and is an **explicitly disclosed unasserted defensive branch** (L9 ledger
**A6**); a published claim that a mutation made it reachable was **withdrawn** by the leaf's own evidence
erratum, because the kill that appeared to prove it also appears with the production line untouched — so it
must never be read as coverage. And `_manifest_digest`'s inclusion of each item's `selection_reasons` is a
**reachable covered gap** with no killing node (L9 ledger **A4**).

**Where the read is addressed and what it never does.** The context names one namespace, one exact logical
snapshot and optionally one exact code tree; all three are verified against the file that was actually
opened, through three separate comparisons where the schema generation is its own statement rather than a
corollary of the digest. `task_ref=None` is a **supported** baseline state — a read during planning needs no
leaf, no enclosure and no fabricated task. The connection is opened **read-only**, so "a refused read
persisted nothing" is a property of the handle rather than a rollback, and the evidence measures it. A
continuation is a **binding**, not a position: snapshot, context, selector, policy and schema are checked
before the file is opened and the manifest and position after the selection exists, and a cursor that binds
something else is refused with **no partial page**. Nothing on this path writes, falls back to a working
tree, to `HEAD` or to Markdown, resolves a symbol locator, or attaches a semantic verdict.

**The leaf's own population and its forward constraint.** 46 leaf cases (21 unit + 25 integration), across
three test modules whose shared fixture is registered as the governed artifact `knowledge-read-scope-cases`
— **L8 must split the unit module before adding cases**, because it sits at 1 163 of the 1 200-line limit.
**L8 paid that constraint rather than waiving it** (see the L8 section below): it added two new modules of
its own and no case to this one, so the read unit module is unchanged.

### 260915-KS-L8 The Baseline-To-Candidate Comparison, And The One Extension To The Read Policy

This route gained **the comparison half** and still no new authority: two new modules
(`knowledge/{diff,diff_display}.py`), the sixth composition seam in `application/knowledge_diff.py`, the
comparison vocabulary in `models/knowledge/diff.py`, and **no change to `schema.py`** — the schema stays
`ar-knowledge-sqlite/v1`, `PRAGMA user_version = 1`, ten tables, fifteen triggers and the same
`schema_fingerprint()`. Two existing storage modules changed, both additively: `read.py` gained
`SelectionQuery.seed_override` (one field, one derived property, and the single seed read the policy uses
— §"the one extension" below), and `read_queries.py` gained five readers (four existence probes and the
predecessor-edge union).

**The comparison's single claim, and everything that follows from it: a comparison is the union of two
independently selected sets, with each item retaining the snapshot it came from.** The selection on each
side is `KS-R07`'s policy, run by its owner on that side's own read-only connection; this half is handed
two already-selected sets and never re-decides relevance. Four consequences are the contract:

- **A relationship only the baseline reached stays in the union**, because the union is built from the
  two selected sets and never from a walk of the candidate. That is why deleting a realization link on
  the candidate cannot make the baseline's code disappear — the requirement's own non-conforming example.
- **A record one snapshot holds and the other side's selection did not reach is
  `present_outside_selection`** — a fact about the selection, reported with the path that reaches it —
  while a record the other snapshot does not hold at all is `absent_from_snapshot`. **Conflating the two
  is the design's own named misreading.**
- **Record changes and source changes are two separate collections.** A **statement-only** change still
  returns the attributed code on both sides; a **source-only** change is reported as a changed source
  observation and **cannot** be rendered as a changed obligation, because no record field changed.
- **No mechanically generated no-consequence judgment exists, by construction** — no field, code path or
  default can emit an invented *strengthening*, *harmlessness* or neutrality verdict. Missing attribution
  remains an advertised **gap** (the unattributed changed paths are listed and counted with their reason)
  rather than being resolved to "no impact".

**The coverage decision is three rules, and the reason is measured rather than argued.** Rule 1 (*did the
other side select another exact revision of this identity?*) is **load-bearing alone** — removing it turns
a missing selection into a real absence. Rule 2 (*do the other side's authored predecessor edges name this
revision?*) **cannot decide a state its neighbours do not**, because an authored edge is a foreign key into
the snapshot that declares it, so it is kept as a **cheap short-circuit over already-loaded lineage**; its
invariant half is asserted through the published read surface and its **family half is unexercised**,
because the fixture authors 0 family edges — a stated gap and not coverage. Rule 3 (*do the other
snapshot's own tables hold this record, by this item's own key?*) is load-bearing in the direction that
**forces its answer present**: forcing it present turns a genuinely deleted realization into a missing
selection (two kills), while forcing it absent changes no asserted state on this population (all 28 nodes
survive). **Collapsing the three into one is wrong because it turns a missing selection into a real
absence** — the reverse of what this leaf first claimed, and the correction is what its source comment now
says.

**The one extension to the read policy, recorded here so it is not re-opened.**
`SelectionQuery.seed_override` exists so that a comparison does **not** need a second selection rule: a
comparison runs R07's policy twice, once per snapshot, and the two sides may address *different exact
revisions of one identity*. `select_recorded_scope` still reads its seed **once** (`read.py:205`), every
later step is computed from that one local, no diff-shaped branch entered the policy owner, and the only
production construction site is the comparison's own `_select_side`. The independent reviewer attacked
the packet's *"R07's policy is the ONLY policy owner"* clause head-on and **could not falsify it**: a
per-side exact-revision address is a **parameterisation of R07's one rule, not a second relevance rule**,
and the override is load-bearing (mutation `R30` kills a named node on an assertion). **The owner recorded
the acceptance.**

**Two honest limits belong here rather than in a footnote.** The comparison's mutation taxonomy leaves
**three covered gaps** on its own lines (`M4` — a same-id pair with differing projected fields; `M8` —
the existence probe's line is reachable, called 3 times, but only its *differing* answer is unobserved;
`M27` — `record_change_only` is true for 0 of 22 items) and **one non-experiment** (`M23` —
`invariant_revision_is_recorded` is called 0 times), each with the input that would close it named. And
**three equivalent mutants are disclosed as equivalences rather than counted as kills** (`M9`, `M12`,
`M21`), each with the measurement that proves the equivalence. None of these is a behavioural defect, and
**the leaf's contested evidence items are carried to `KS-R09`/`L9`** (ledger entries **A9**/**A10**) —
this route claims the comparison's *behaviour*, which five independent review rounds could not falsify,
and not the leaf's evidence prose, which is explicitly contested there.

### 260915-KS-L10 The Generation Registry, The Record Envelope, And `Route` As A Scope Axis

This route's meaning changed in a way that **supersedes** what earlier leaves recorded about the schema, so this
section states the change first and then the contradiction it retires.

**The schema stopped being a build-time singleton and became a registry of frozen, selectable generations.**
`knowledge/schema_generations.py` owns the registry. `SchemaGeneration` is a frozen record of everything one
generation must answer about itself — schema name, `user_version`, the ordered table manifest, and per table the
declared column order, the primary-key tuple and the typed-JSON column set, plus the required-SQLite-feature set,
the table DDL, the index DDL, the trigger set and the structural fingerprint. The key and typed-JSON registries are
part of the pinned structure rather than derivations from DDL: generation 1's DDL never spells `json_valid`, and a
key tuple is declared data the encoder checks *against* the column list.

**Generation 1 is pinned as data, and dispatching to it is a read of the dataset.** `GENERATION_1` delegates every
declaration to `schema.py` — which keeps them verbatim, unchanged — and takes its fingerprint from the recorded
constant `GENERATION_1_FINGERPRINT` (`bae805d6…`, measured at revision `420669c4`, the pre-refactor head).
`require_pinned_generation_1_unchanged()` recomputes that fingerprint from the recorded record and **fails rather
than warns** on drift, raising `KnowledgeSchemaPinError`; the recorded recovery is to correct the change, never to
re-pin the constant to whatever the code now computes. Generation 2 is **composed** as an explicit append —
generation 1's tables plus `schema_v2.APPENDED_TABLES` — and its fingerprint is derived from the composition rather
than recorded.

**Two key spaces, deliberately not interchangeable.** An open SQLite file declares its generation through
`PRAGMA user_version` **alone**, because the application schema name is not stored in the file (the name
`inspect_schema` reports is the *build's*), so `generation_of_database` resolves by version. A portable artifact
carries `schema` as well, so `generation_of_artifact` resolves by the **pair**, and it is **type-strict on the
version before it is a lookup**: `1 == 1.0 == True` in Python, so an equality-keyed lookup would resolve `1.0` and
`true` to generation 1, which the shipped reader deliberately refuses. Selection happens once per operation and
every later digest, manifest, key registry and table-attachment decision in that operation uses the selected
generation.

**Initialization declares; it does not select.** An empty database has no version to read, so
`create_or_validate_schema` declares the newest supported generation (`CURRENT_GENERATION`, `GENERATIONS[-1]`).
This is the only place a build's own generation decides anything, and it decides only what brand-new data
declares. Consequence a reader must not miss: **a store created by this build is generation 2**, so
new tables are reachable only through generation-2 creation, while a generation-1 file stays generation 1.

**What this leaf contradicts in the previously recorded intent.** Two statements that older leaves wrote as
current intent are now false, and they are retired here rather than left to be believed:

1. **"`SCHEMA_USER_VERSION = 2` is how a schema change happens"** (the L1 charter paragraph at *Owns*, and the
   invariant this section previously stated as *the schema is a generation, not a file*). `SCHEMA_USER_VERSION`
   keeps its shipped meaning as **generation 1's** `user_version`, because generation 1's fingerprint is computed
   from it; it is no longer the build's current version and no longer moves when the schema grows. A new schema
   shape is a **new registered generation record** (`GENERATION_2` = `ar-knowledge-sqlite/v2` / `2`), and
   `CURRENT_GENERATION` — not `SCHEMA_USER_VERSION` — is what a created store declares.
2. **"All ten tables participate, because the body is derived from `schema.CANONICAL_TABLES`"**
   (`logical.py`'s invariant). The encoder is now **parameterised over the selected generation**: the body
   projects the table mapping into *that* generation's declared order, so a generation-1 dataset still digests
   over generation 1's ten tables including the empty ones, while a generation-2 dataset digests over sixteen. The
   property that survives, and that is the point, is that **the digest is total over its own generation's
   manifest** — a table that appears or disappears within a generation is still a difference, and no digest is
   ever computed over the intersection of two generations.

**An unchanged version-1 dataset keeps its version-1 identity, exactly, and that is the acceptance test.**
Its `body_version`, its `schema`, its `user_version = 1` and the pinned generation-1 fingerprint all stay what
they were, and opening it under this build reports generation 1. **No migration or cutover operation exists**:
nothing in opening, publishing, merging, exporting or reading upgrades a dataset's generation, and the honest
answer for a version-1 candidate met by generation-2 code is "it is version 1". Generation-2 datasets are
**different datasets with different digests**, never reported as equal to or as a continuation of the
generation-1 digest of the same rows.

**Additive-only, and mechanically checkable.** Generation 2's manifest **begins with** generation 1's ten tables
in generation 1's exact order, carrying generation 1's exact declared columns, keys and typed-JSON sets; it may
only append. `schema_v2.py` therefore expresses the governing-route association as three **new join tables**
(`source_anchor_route`, `invariant_route`, `family_route`), each taking the governed entity's key as its own
primary key, rather than as a `governing_route_id` column added to a generation-1 table — appending a column would
change that table's declared column set while generation 1's record must keep declaring it. A `knowledge_record`
is new in generation 2, so *it* carries `governing_route_id` directly. **No `ALTER TABLE` appears anywhere in the
package**; the phrase occurs once in `schema_v2.py`, inside its own docstring, as the prohibition.

**The record envelope has a real payload seam, and no identity of its own.** `knowledge_record` carries `kind`,
`authority_home`, `lifecycle`, `record_schema`, an optional governing route and provenance — and **no content
address, no logical digest and no fingerprint column**, so it cannot quietly become a second identity authority.
`record_schema` names which frozen shape the revision was written against; it is not a fingerprint. The payload
lives on `record_revision` (`payload` is the typed-JSON column, `TEXT NOT NULL CHECK (json_valid(payload))`, which
is why generation 2 adds `json_functions` to its feature set), and the revision is sealed by immutable triggers.
`knowledge/record_envelope.py` is the **one** place any write path decides admissibility: `PAYLOAD_MODELS` maps the
`(kind, record_schema)` pair to exactly one frozen Pydantic model, `KIND_SCHEMAS` is derived from that registry
rather than restated, and `validate_record_payload(...)` returns the validated model or a refusal with the shipped
code **`invalid_payload`** — no row written, before/after digest unchanged. This leaf registers exactly **one
marked-internal conformance kind** (`internal_conformance` / `internal-conformance/v1`) purely to exercise the
seam; the product kinds are later leaves and are added *beside* it, not by replacing it.

**`Route` is now an operable scope axis, not a table with a constraint.** `knowledge/routes.py` owns the two rules
and the three operations. Confinement walks a nine-entry rule table and refuses the first breached form — a
non-string, a NUL, a backslash, a drive letter, a UNC form, an absolute path, a trailing separator, a spelling that
is not already normalised, and an empty/dot segment or traversal — returning an admitted path **unchanged**:
normalisation is a *comparison*, never a repair, because rewriting is how two spellings become one route while a
caller believes it authored two. Acyclicity is a `UNION`-deduplicated recursive CTE anchored on the **edge**
`(route_id, parent_route_id)`, run inside the caller's transaction after the insertions and before the commit, so a
cycle refuses the whole batch; the one-node cycle is the table's own `CHECK`. `author_route` normalises, returns an
**existing** route's id when one is already authored for that path (writing no second row), refuses an unauthored
parent, inserts, then returns the cycle refusal for the caller to roll back. `set_governing_route` accepts exactly
three governed generation-1 entities, is idempotent when the same association is re-stated, and **refuses a
different route for an already-governed row** rather than re-pointing it. `find_governing_route` returns the
governing id or `None`, and `None` is a fact rather than a default: it is never "the repository root". **Scope is
never inferred** — nothing in this package derives route membership from a name, a folder ancestry, a path prefix
or a symbol string.

**The merge preflight reads each input's generation first and refuses a disagreement before any session exists.**
`merge_schema.selected_generation` names the positional role that disagreed and carries the expected and observed
versions as facts, leaving all three inputs byte-identical; it does not pick a winner, migrate an input or proceed.
The silent failure this closes is shipped and documented: changeset application carries no operation for a table it
never attached, so a table present on only one side is a change set that vanishes while SQLite returns success.
When the inputs *do* agree, **that agreed generation is the operation's selected generation**, and the structural
comparison and the session's table attachment both use it — so **a v1/v1/v1 merge on this generation-2 build still
attaches generation 1's ten tables and is byte-comparable to its pre-refactor result**, which is a required passing
case rather than a conservative default. Nothing here activates or widens a production merge driver; this is input
validation on the existing application-callable path.

**What remains deliberately unbuilt, recorded so it is not assumed.** No migration or cutover operation; no
production merge driver; no product record kinds; no second storage engine or binding. And one honest gap this
route carries: requirement 4.2's confinement rule names "no escaping symlink at resolution", and the module
docstring repeats it, but `normalize_route_path` refuses only the **lexical** forms and performs no symlink
resolution. A reader must not assume the code checks that clause.

### 260915-KS-L11 Generation 3, The Facet Write Path, And The Facet-Specific Selection

This route's storage package gained **generation 3** — the authored-judgment facet tables — plus the write
path, the row codecs and a selection of their own, and its meaning changed in one place that earlier
sections describe the other way round, so this section states the change first.

**The facet record kind does not live on the envelope alone; it is a sub-route of the write boundary.**
`knowledge/facets.py` owns **six authored acts**, each with the shipped pair of entry points: the operation
(`add_facet`, `attach_facet`, `remove_facet_attachment`, `author_explanation`, `add_explanation_revision`,
`designate_explanation`), which owns the candidate lock and one `BEGIN IMMEDIATE` transaction, and the
in-transaction step (`apply_facet_command` dispatching through `_STEPS`), which raises `KnowledgeRefused`
so the batch path rolls the whole batch back. The batch union in `models/knowledge/candidate.py` widened
from **twelve** command kinds to **eighteen**, and the shipped twelve keep their exact kinds.

**Four rules shape that write path, and each is a place a later edit could silently undo a guarantee:**

1. **The payload seam is the only payload decision point.** `record_envelope.validate_facet_payload`
   resolves the `(kind, record_schema)` pair, so an unknown or ninth subtype, an undeclared field, a missing
   meaning and a payload carrying its own `actor_ref` are all the same shipped **`invalid_payload`**
   refusal, raised before any row exists.
2. **Provenance comes from the admission, and `authority_home` from the namespace.** Neither is a field of a
   command, so no part of a submitted payload can become the record's author, authorization or instant.
3. **A facet is authored as proposed origin data.** `require_proposed_origin` refuses an accepted origin at
   **both** entry points with the shipped **`promotion_not_supported`**; the accepted-origin consistency
   rule is inherited from the vocabulary base rather than re-implemented.
4. **Every reference is checked before the row it belongs to.** A facet revision, a typed endpoint, an exact
   statement revision of the subject's own kind, a stored **decision** revision for a supersession, a
   revision of *this* explanation for a designation, and a named governing route are all verified first; a
   dangling reference is refused rather than stored and is never inferred from a name, a path or prose.

**Generation 3 appends four tables and retypes nothing.** `knowledge/schema_v3.py` declares
`facet_attachment`, `facet_decision_supersession`, `explanation` and `explanation_revision` in that
serialization order, with eleven indexes and seven triggers, and `GENERATION_3` composes them onto
generation 2 exactly as generation 2 composes onto generation 1 — so
`GENERATION_3.tables[: len(GENERATION_2.tables)] == GENERATION_2.tables` and generation 3's columns for
each of the first sixteen names are generation 2's. Three shapes are worth naming because they are how the
requirements are enforced structurally rather than by discipline:

- **Endpoint-kind compatibility is a checked foreign-key group per kind**, not a polymorphic
  `(facet_revision_id, endpoint_kind, endpoint_id)` triple: the forbidden shape has **no `endpoint_id`
  column to land in**, and a `CHECK` requires the populated group to match the stored kind.
- **An explanation's subject is the three-column `(repository_id, identity, revision_id)` reference** both
  revision tables already declare a `UNIQUE` key for, so "this revision really is a revision of the
  statement identity it claims" is a constraint of the table rather than a check the write path remembers.
- **`explanation.current_revision_id` is the one mutable field of that row**, and the
  `explanation_no_rebind` trigger names every other column — the exception is authored rather than
  inferred. Supersession adds an edge row and nothing else: the edge table refuses update and delete, so a
  superseded decision keeps its rows, its digest, its revisions and its attachments.

**Facets are reached by their own selection, not by extending `KS-R07@v1`'s.** `knowledge/facet_read.py`
declares its own seeds (a facet record, or an exact statement revision), its own item kinds and its own
declared policy `authored-judgment-facets/v1`, and it shares **no code path** with the recorded-scope read —
which is why a shipped seed's serialized page stays byte-identical, not because a guard prevents an
addition. Two properties of that selection are the contract: it is **complete or it refuses** (a selection
past its declared execution bound raises, and there is no cursor), and **nothing is derived** — an item's
order is fixed by its kind and stable identifiers, every retained revision is served as its own item, and
the only statement about which explanation revision matters is the designation the record *stores*.

**One measured divergence is recorded rather than smoothed over.** `_apply_facet_command` constructs a
`FacetWriteResult` with `state="no_change"` for an empty write, while the receipt model declares
`state: Literal["applied", "refused"]`; the mismatch is reachable only through an empty write, which the
digest-guarded designation and the pre-write reference checks make unreachable on every path this leaf's
cases drive. A later leaf that makes an empty write reachable meets a `ValidationError`, not a third state.

## Invariants And Boundaries

- **A schema generation is data, and dispatch reads the dataset.** `knowledge/schema_generations.py` owns which
  generations exist; `GENERATION_1` is pinned with its fingerprint constant and guarded by a gate that **fails,
  never warns**; `GENERATION_2` is composed as an append. A dataset's generation is selected from what the dataset
  declares (version alone for an open file, the type-strict `(schema, userVersion)` pair for an artifact), and
  every later decision in that operation uses the selected generation. **`SCHEMA_USER_VERSION` is generation 1's
  `user_version`, not the build's current version**; `CURRENT_GENERATION` is what a *created* store declares, and
  creation is a declaration rather than a selection because an empty database has no version to read.
- **Generation 1 is immutable and additive-only.** Its ten tables keep their exact declaration order, columns,
  keys, constraints and triggers, and its recorded fingerprint never moves; a generation that would reorder,
  rename, retype, drop or weaken an earlier generation's declaration is a **schema divergence to escalate**, never
  a member of the registry and never a re-pin. **No `ALTER TABLE` against a generation-1 table exists in this
  package**, which is why the governing-route association lives in generation-2 join tables.
- **An unknown generation is refused, never migrated.** Not repaired, not re-created, and never re-read under a
  different generation to obtain a green result. No operation in this route upgrades a dataset, and an unchanged
  version-1 dataset keeps its version-1 digest byte for byte.
- **Every digest is total over its own generation's manifest.** No digest is computed over the intersection of two
  generations' tables, and no "same knowledge" verdict is returned across a generation boundary. Opening an
  existing database validates *that* generation's tables, columns and full trigger set.
- **Import direction is one-way.** `memory.knowledge` imports `kernel.canonical_json`, `kernel.file_lock` and
  `models.knowledge`; no package ranked below `memory` may import it back. A focused test guards this so a later
  reverse import fails a check rather than passing review.
- **Insert-only, one lock, one transaction.** Every mutation holds the candidate's exclusive file lock and runs
  inside one `BEGIN IMMEDIATE`; a refusal rolls back, so an expected failure never leaves a partial aggregate.
  The route operations follow the same rule: `author_route` and `set_governing_route` insert inside the caller's
  transaction and **return** their refusals rather than rolling back themselves, and the acyclicity walk is what
  makes a cycle a whole-batch rollback rather than a partial hierarchy.
- **Scope is never inferred.** Route membership, family composition and every association between records are
  authored, stored facts: a path prefix, a directory name, a symbol string or a prose mention is never a
  relationship, and a path comparison the read layer performs is a resolution fact rather than authored membership.
- **Refusals are returned values.** A caller branches on a typed code, never on message text; a storage failure
  with no contract code is reported as a defect (`KnowledgeStorageError`), not as an outcome to handle.
- **Vocabulary is defined where it decides.** Literal states, operation names, refusal codes and version strings
  live in `models.knowledge` and are imported by the decider, never defined by the decider and imported back down.
- **This is an experimental increment on the master's branch pair.** No IAS landing is implied, legacy Markdown
  remains operational authority, and the still-unclaimed behaviour is now **L9** (the foundation fix and
  certification pass) — the baseline-to-candidate comparison is claimed by this route as of `KS-R08@v1`, the
  selective recorded-scope read as of `KS-R07@v1`, the portable roundtrip as of
  `KS-R06@v1`, the Git-side merging half as of `KS-R05@v1`, and snapshot publication as of `KS-R04@v1`. The admitted batch contract *is* claimed by this route as
  of `KS-R03@v1` — one lock, one transaction, one closed command union and one resolved dataset identity — while the
  `task-candidate` lane deliberately refuses until a later leaf supplies a checkable binding. The graph half is
  claimed as of `KS-R02@v1`: families, anchors, memberships and realization claims are stored and readable from both
  directions; anchor **resolution** is claimed by this route as of `KS-R07@v1`, in
  `knowledge/read_anchors.py`, and is still deliberately absent from the write path.
- **A refusal describes the actual cause.** No path on this route reports an absence for a spelling it refused,
  and every refusal code names a distinct fact a caller acts on — the rule `KS-R07@v1` established across the read
  path and inherited by L8/L9. A boundary that refuses something must let the caller tell an absence from a
  malformed input.
- **The read half is read-only by construction.** Every statement the read issues is a `SELECT` on a connection
  opened through `open_read_only_database`; "a refused read persisted nothing" is therefore a property of the
  handle, not a rollback the code remembers.
- **A published write helper assumes the caller's lock and transaction.** The batch forced those helpers public; a
  future caller that invokes one outside a transaction would write an autocommitted row silently. Every shipped call
  site satisfies the precondition, and keeping the rule is what the one-lock/one-transaction invariant rests on.

## Repo-Internal References

The declarations below establish the current behaviour; this inventory is not execution evidence.

**The 260915-KS-L5 merge half**, cited in the current `Finding | Anchor | Source` shape. The older rows below remain in the superseded
two-column shape and are recorded as a pre-existing repository-wide migration item in the Update History rather than converted from inside
one leaf's curation pass.

| Finding | Anchor | Source |
| --- | --- | --- |
| The merge orchestration: the ordered sequence, the one-lock policy, the conflict taxonomy and the engine-supplied conflict key. | `merge_knowledge_datasets`; `_TAXONOMY`; `_conflict_record`; `_freeze_merged` | mcp/src/agents_remember/memory/knowledge/merge.py:131-163; mcp/src/agents_remember/memory/knowledge/merge.py:650-655; mcp/src/agents_remember/memory/knowledge/merge.py:668-679; mcp/src/agents_remember/memory/knowledge/merge.py:740-776 |
| The base resolution: the closed two-member claim and the two refusals a base claim can earn. | `resolve_merge_base`; `_ancestry_refusal`; `_uniqueness_refusal` | mcp/src/agents_remember/memory/knowledge/merge_base.py:75-105; mcp/src/agents_remember/memory/knowledge/merge_base.py:181-196; mcp/src/agents_remember/memory/knowledge/merge_base.py:199-224 |
| The structural preflight that runs before any session exists, and the declared manifest it compares against. | `require_supported_structure`; `declared_structure`; `compare_structures` | mcp/src/agents_remember/memory/knowledge/merge_schema.py:226-258; mcp/src/agents_remember/memory/knowledge/merge_schema.py:173-188; mcp/src/agents_remember/memory/knowledge/merge_schema.py:261-305 |
| The changeset half: the directional delta build, the aborting application, the old-side conflict key and the coverage replay. | `build_delta`; `apply_changeset`; `_conflicting_key`; `replay_delta` | mcp/src/agents_remember/memory/knowledge/merge_changeset.py:185-220; mcp/src/agents_remember/memory/knowledge/merge_changeset.py:223-263; mcp/src/agents_remember/memory/knowledge/merge_changeset.py:266-289; mcp/src/agents_remember/memory/knowledge/merge_changeset.py:292-331 |
| The postcondition half, including the two call sites this leaf recorded as unreachable by a black-box case. | `require_structural_validity`; `require_immutable_revisions_preserved`; `require_applied_changes` | mcp/src/agents_remember/memory/knowledge/merge_validation.py:73-101; mcp/src/agents_remember/memory/knowledge/merge_validation.py:104-152; mcp/src/agents_remember/memory/knowledge/merge_validation.py:169-211 |
| The merge's refusal vocabulary, one factory per observable failure point. | `schema_mismatch_refusal`; `conflicting_values_refusal`; `duplicate_identity_refusal`; `delete_reference_conflict_refusal` | mcp/src/agents_remember/memory/knowledge/merge_refusals.py:21-45; mcp/src/agents_remember/memory/knowledge/merge_refusals.py:70-94; mcp/src/agents_remember/memory/knowledge/merge_refusals.py:97-121; mcp/src/agents_remember/memory/knowledge/merge_refusals.py:124-151 |
| The two operations and twelve codes the merge added to the shared vocabulary. | `KnowledgeOperation`; `KnowledgeRefusalCode` | mcp/src/agents_remember/models/knowledge/result.py:36-62; mcp/src/agents_remember/models/knowledge/result.py:66-111 |
| The measurement the merge reports, and the merge's own third composition seam. | `MergeCoverage`; `merge_resolved_knowledge_datasets` | mcp/src/agents_remember/models/knowledge/merge.py:243-284; mcp/src/agents_remember/application/knowledge_merge.py:55-64 |
| **The read half's selection policy: `F0` frozen before membership expansion, the advertised-and-untraversed frontier, and the declared item order.** | `select_recorded_scope`; `_member_revision_ids`; `_frontier_expansions`; `_sort_key` | mcp/src/agents_remember/memory/knowledge/read.py:193-238; mcp/src/agents_remember/memory/knowledge/read.py:342-352; mcp/src/agents_remember/memory/knowledge/read.py:355-390; mcp/src/agents_remember/memory/knowledge/read.py:469-480 |
| Whole-item paging over an already-selected scope. | `page_of_scope` | mcp/src/agents_remember/memory/knowledge/read.py:743-797 |
| **The corrected page counts: the declared total on every page, the walk's cumulative figure, and the slice size in `len(page.items)`.** | `_page_counts` | mcp/src/agents_remember/memory/knowledge/read.py:823-847 |
| The count model that refuses its own arithmetic contradiction at construction. | `KnowledgeReadCounts` | mcp/src/agents_remember/models/knowledge/read.py:404-448 |
| **The three genuinely different facts of a path refusal, and the corrected predicate (`*`, `?`, `[` admitted; leading `:` refused).** | `observe_anchor`; `_confined_posix_relative`; `require_plain_git_path` | mcp/src/agents_remember/memory/knowledge/read_anchors.py:101-172; mcp/src/agents_remember/memory/knowledge/read_anchors.py:308-334; mcp/src/agents_remember/models/knowledge/base.py:59-92 |
| The read's refusal vocabulary, one factory per observable failure point. | `selector_absent_refusal`; `registration_absent_refusal`; `page_budget_too_small_refusal`; `continuation_binding_mismatch_refusal`; `snapshot_unavailable_refusal`; `selection_incomplete_refusal` | mcp/src/agents_remember/memory/knowledge/read_refusals.py:35-57; mcp/src/agents_remember/memory/knowledge/read_refusals.py:60-79; mcp/src/agents_remember/memory/knowledge/read_refusals.py:82-108; mcp/src/agents_remember/memory/knowledge/read_refusals.py:111-135; mcp/src/agents_remember/memory/knowledge/read_refusals.py:138-156; mcp/src/agents_remember/memory/knowledge/read_refusals.py:159-177 |
| **The one decoder a read page and the logical digest share.** | `cell_value` | mcp/src/agents_remember/memory/knowledge/logical.py:240-248 |
| The read's path lookup, which is how a path seed selects. | `fetch_realizations_at_path` | mcp/src/agents_remember/memory/knowledge/read_queries.py:208-244 |
| The edge lookup the directly containing family set is derived from. | `fetch_memberships_of_invariants` | mcp/src/agents_remember/memory/knowledge/read_queries.py:192-207 |
| The read's composition seam and its three boundaries (read-only handle, task-free baseline, cursor-as-binding). | `read_knowledge_scope`; `open_read_context`; `read_row_counts` | mcp/src/agents_remember/application/knowledge_read.py:139-192; mcp/src/agents_remember/application/knowledge_read.py:103-136; mcp/src/agents_remember/application/knowledge_read.py:587-602 |
| **The nodes that measure the requirement's stopping rule, the corrected counts and the three path facts.** | "test_a_path_seed_returns_the_sibling_realizations_and_advertises_the_unreached_family"; "test_a_page_budget_of_one_item_still_advertises_the_second_location"; "test_a_stored_path_that_cannot_be_addressed_is_refused_rather_than_reported_absent" | mcp/tests/test_knowledge_read_scope.py:139-169; mcp/tests/test_knowledge_read_scope.py:547-657; mcp/tests/test_knowledge_read_paths.py:370-444 |
| The shared case harness registered as `contract:common-base-merge-cases`, and its evidence node. | "def test_disjoint_edits_from_both_sides_survive_in_a_closed_published_candidate(" | mcp/tests/test_knowledge_guarded_merge.py:307-376; mcp/tests/evidence-lifecycle.toml:1136-1136 |
| The governed-artifact row and the exact consumer list the L5 leaf registered in the shared catalog, which this leaf extended by two modules. | "id = \"common-base-merge-cases\"" | mcp/tests/evidence-lifecycle.toml:1135-1159 |

**The 260915-KS-L6 portable half**, cited in the same `Finding | Anchor | Source` shape.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The `ar-knowledge-export/v1` format: the one encoder, the canonical-form guarantee, the two acceptance checks and the digest-coverage statement.** | `EXPORT_FORMAT`; `encode_export`; `parse_export`; `canonical_document`; `_validate_header` | mcp/src/agents_remember/memory/knowledge/export_portable.py:116-116; mcp/src/agents_remember/memory/knowledge/export_portable.py:276-301; mcp/src/agents_remember/memory/knowledge/export_portable.py:490-543; mcp/src/agents_remember/memory/knowledge/export_portable.py:366-398; mcp/src/agents_remember/memory/knowledge/export_portable.py:755-812 |
| The whole-document gate, its `<canonical document>` refusal identity and the bounded statement of how the text differs. | `_non_canonical_refusal`; `_canonical_difference` | mcp/src/agents_remember/memory/knowledge/export_portable.py:610-642; mcp/src/agents_remember/memory/knowledge/export_portable.py:645-664 |
| The envelope builder and the declared orders it re-imposes: columns, nested keys and the manifest. | `export_envelope`; `_ordered_rows`; `_plain_tables` | mcp/src/agents_remember/memory/knowledge/export_portable.py:199-238; mcp/src/agents_remember/memory/knowledge/export_portable.py:241-263; mcp/src/agents_remember/memory/knowledge/export_portable.py:418-445 |
| The dataset-level checks: declared column order, declared types, primary-key uniqueness, namespace binding and the recomputed seal. | `validate_export`; `_validate_table_rows`; `_typed_row`; `_validate_dataset` | mcp/src/agents_remember/memory/knowledge/export_portable.py:667-712; mcp/src/agents_remember/memory/knowledge/export_portable.py:839-882; mcp/src/agents_remember/memory/knowledge/export_portable.py:885-925; mcp/src/agents_remember/memory/knowledge/export_portable.py:964-1023 |
| The reachable, verdict-changing namespace guard with no killing node (an observation for L9). | `bound` | mcp/src/agents_remember/memory/knowledge/export_portable.py:981-998 |
| **The export and import operation: validation before any database work, a private stage, the closed two-mode destination admission and publication on exact digest equality.** | `export_knowledge_dataset`; `import_knowledge_dataset` | mcp/src/agents_remember/memory/knowledge/export_import.py:133-192; mcp/src/agents_remember/memory/knowledge/export_import.py:195-244 |
| **The staged sealed-aggregate read: every retained revision's payload re-derived through the shared decoders before publish.** | `_sealed_aggregate_refusal`; `_SEALED_AGGREGATES` | mcp/src/agents_remember/memory/knowledge/export_import.py:463-494; mcp/src/agents_remember/memory/knowledge/export_import.py:127-130 |
| The staged verification, including the documented non-experiment (the digest equality no black-box case can falsify). | `_verify_staged_dataset` | mcp/src/agents_remember/memory/knowledge/export_import.py:408-460 |
| The two-mode destination admission read before any staging, and the private stage that is never the destination. | `_destination_refusal`; `_stage_imported_dataset`; `_private_stage_directory` | mcp/src/agents_remember/memory/knowledge/export_import.py:342-367; mcp/src/agents_remember/memory/knowledge/export_import.py:370-420; mcp/src/agents_remember/memory/knowledge/export_import.py:616-624 |
| The value-or-refusal file reader whose two failures carry different codes. | `read_artifact` | mcp/src/agents_remember/memory/knowledge/export_import.py:257-290 |
| The portable boundary's refusal vocabulary, one factory per observable failure point. | `invalid_export_refusal`; `non_canonical_export_refusal`; `unsupported_schema_refusal`; `destination_occupied_refusal`; `destination_absent_refusal`; `import_validation_failed_refusal` | mcp/src/agents_remember/memory/knowledge/export_refusals.py:26-50; mcp/src/agents_remember/memory/knowledge/export_refusals.py:53-75; mcp/src/agents_remember/memory/knowledge/export_refusals.py:78-102; mcp/src/agents_remember/memory/knowledge/export_refusals.py:105-126; mcp/src/agents_remember/memory/knowledge/export_refusals.py:129-148; mcp/src/agents_remember/memory/knowledge/export_refusals.py:151-172 |
| **The one body constructor the export seals through, so the scan and the artifact cannot define the digest twice.** | `logical_body_from_tables`; `logical_digest_of_tables` | mcp/src/agents_remember/memory/knowledge/logical.py:95-129; mcp/src/agents_remember/memory/knowledge/logical.py:132-135 |
| **The shared "prove this finished file is a closed database" step the import's stage is closed through.** | `require_closed_database` | mcp/src/agents_remember/memory/knowledge/closed_snapshot.py:66-89 |
| The admission reading the import's destination check uses, exported from publication. | `destination_observation` | mcp/src/agents_remember/memory/knowledge/publication.py:260-270 |
| The two portable operations and the one code they added to the shared vocabulary. | `KnowledgeOperation`; `KnowledgeRefusalCode` | mcp/src/agents_remember/models/knowledge/result.py:36-69; mcp/src/agents_remember/models/knowledge/result.py:72-120 |
| The portable wire vocabulary: the request identities, the validation report and the two results. | `ExportRequest`; `ImportRequest`; `PortableValidation`; `ExportResult`; `ImportResult` | mcp/src/agents_remember/models/knowledge/portable.py:36-44; mcp/src/agents_remember/models/knowledge/portable.py:47-63; mcp/src/agents_remember/models/knowledge/portable.py:66-98; mcp/src/agents_remember/models/knowledge/portable.py:101-133; mcp/src/agents_remember/models/knowledge/portable.py:136-176 |
| The fourth composition seam, its five entry points and its two non-claims. | `export_knowledge_artifact`; `import_knowledge_artifact`; `validate_knowledge_artifact`; `canonical_body_of_artifact` | mcp/src/agents_remember/application/knowledge_export.py:60-63; mcp/src/agents_remember/application/knowledge_export.py:66-74; mcp/src/agents_remember/application/knowledge_export.py:77-96; mcp/src/agents_remember/application/knowledge_export.py:112-126 |
| **The node the guarantee rests on: the canonical form is the only form the reader accepts, including all seven header types.** | "test_the_canonical_form_of_the_whole_document_is_the_only_form_the_reader_accepts" | mcp/tests/test_knowledge_portable_boundaries.py:132-258 |
| **The node that proves an artifact whose sealed payload contradicts its digest is refused before publish.** | "test_an_artifact_whose_sealed_payload_contradicts_its_digest_is_refused" | mcp/tests/test_knowledge_portable_boundaries.py:534-582 |
| The node that proves the import's stage is closed before it is published, and the node that proves the freeze's closure on the published destination. | "test_a_stage_opened_in_wal_mode_is_published_as_a_closed_database"; "test_a_frozen_snapshot_of_a_wal_resident_candidate_is_published_closed" | mcp/tests/test_knowledge_portable_boundaries.py:618-650; mcp/tests/test_knowledge_portable_boundaries.py:96-134 |
| The node that proves destination admission refuses before any staging work. | "test_destination_admission_refuses_before_any_staging_work" | mcp/tests/test_knowledge_portable_boundaries.py:656-656 |
| The node that holds the round trip of a populated dataset to an equal logical dataset. | "test_a_populated_dataset_round_trips_to_an_equal_logical_dataset" | mcp/tests/test_knowledge_portable_roundtrip.py:356-427 |
| The registry rows this leaf added: two integration lane rows and the three exact consumer declarations. | "integration = ["; "id = \"knowledge-identity-branching-fixture\""; "id = \"knowledge-snapshot-lifecycle-cases\""; "id = \"common-base-merge-cases\"" | mcp/tests/test-evidence-lanes.toml:158-158; mcp/tests/evidence-lifecycle.toml:1031-1059; mcp/tests/evidence-lifecycle.toml:1110-1133; mcp/tests/evidence-lifecycle.toml:1135-1159 |

**The pre-L6 rows below remain in the superseded two-column shape** and are recorded as a pre-existing repository-wide migration item in the Update History rather than converted from inside one leaf's curation pass.

| Finding | Anchor | Source |
| --- | --- | --- |
| The canonical table list, column order and required feature set the store is validated against. | — | — |
| The declared DDL: ten STRICT tables with explicit NOT NULL keys, composite deferred FKs and the self-edge CHECK. | — | — |
| The fifteen immutability triggers whose names the merge preflight compares — and, by their absence, the disclosed `family` identity gap recorded above. | — | — |
| The structural manifest and the fingerprint over manifest plus DDL text. | — | — |
| The verified pragma contract, the shared one-row reader and the create-versus-validate open. | — | — |
| The one atomic insert-only revision operation with its ordered preconditions. | — | — |
| The lineage rule stated once, including its post-insert scope and before-any-write evaluation. | — | — |
| The shared lineage rule both graphs apply, and the family graph's application of it. | — | — |
| The family owner: identity, sealed revisions, family lineage and the narrow ownership read. | — | — |
| The anchor owner: authored locations stored as recorded, with explicit identity-plus-digest removal. | — | — |
| The membership owner: one exact pair, both read directions, stale-caller removal. | — | — |
| The realization owner: the anchored-claim transaction and both read directions over the same rows. | — | — |
| The shared relation-endpoint check the two relation writes both use. | — | — |
| The typed refusal vocabulary and the SQLite-error mapping, whose failure context now names the caller's operation and table. | — | — |
| The row codecs, including the read-time seal re-derivation over the stored row and its stored edges. | — | — |
| The composition seam that assigns provenance and is the only consumer of this storage package. | — | — |
| The shared knowledge vocabulary written by this store, including the graph shapes. | — | — |
| The kernel canonical encoder the seal and the schema fingerprint are computed through. | — | — |
| The branching fixture — now carrying both the identity and the graph half — the storage and graph cases build from. | — | — |
| The graph case support module, with its registered contract and exact consumer set. | — | — |
| The focused suite, registered in the unit lane, that exercises this route's storage behaviour. | — | — |
| The graph suites registered in the unit lane: family revision rules, relation writes, graph reads and the payload seals. | — | — |
| The node that isolates the sealed predecessor field on each payload, added by the fix-verification round. | — | — |
| --- | — | — |
| The storage home is declared in the memory package charter as a wording addition only. | — | — |
| The fixture's registered stable contract, its evidence node and its five declared consumers. | — | — |

## Cross-Repo References

No cross-repository authority is established by this route. The store writes one SQLite file inside the code
worktree it was opened against, and the memory-repository lifecycle can address a sibling external-memory
checkout, but neither establishes a boundary contract here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T00:25+02:00 — 260915-KS-L11 curator (uncommitted change set on `ar/260915-ks-l11`, base `4904e08f`): recorded **generation 3 and the facet sub-route** — the route's fourth registered generation, the six-act write path with two entry points per act, and the facet-specific selection that does not extend `KS-R07@v1`'s. The section states the four rules shaping the write path (the payload seam as the only payload decision point; provenance from the admission and `authority_home` from the namespace; proposed-origin-only at **both** entry points with the shipped `promotion_not_supported`; and every reference checked before the row it belongs to), the **union widening from twelve command kinds to eighteen** with the shipped twelve unchanged, and the three shapes that make the requirements structural rather than disciplinary: the **per-kind checked foreign-key group** (the forbidden polymorphic shape has no `endpoint_id` column to land in), the **three-column subject reference** that makes a revision's identity claim a table constraint, and `current_revision_id` as the **one mutable field** with the rebind trigger naming every other column while supersession adds an edge row and nothing else. It records the facet selection's own policy name and its two contract properties (complete-or-refused with no cursor; nothing derived, with the stored designation the only currency statement) and why a shipped seed's page stays byte-identical — no shared code path rather than a guard. It also records **one measured divergence** rather than smoothing it over: `_apply_facet_command` constructs `state="no_change"` while the receipt declares only `applied`/`refused`, unreachable on every path the leaf's cases drive. Verification metadata is **not** advanced: the code commit does not exist yet and closeout owns the stamp.
- 2026-09-17T20:39:57+00:00: Generated citation repair: "test_destination_admission_refuses_before_any_staging_work" repointed to mcp/tests/test_knowledge_portable_boundaries.py:656-656. No content impact: mechanical anchor-range projection bound to citation source snapshot b181d6d0b4e4cacc1833ff166c579061a1762313f644c682eec8ffc186d8d42f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T19:11+00:00 — 260915-KS-L10 curator (uncommitted change set on `ar/260915-ks-l10`, base `420669c4`): **reviewed the route because its recorded intent was contradicted, not merely extended.** The leaf removed the premise this route was written on: the schema stopped being one build-time shape whose `SCHEMA_USER_VERSION` moved when the DDL changed, and became a registry of frozen, selectable generations (`knowledge/schema_generations.py` — generation 1 pinned as data with its fingerprint constant and a gate that **fails rather than warns**, generation 2 composed as an append and declared in `knowledge/schema_v2.py`), with dispatch reading the dataset: `PRAGMA user_version` alone for an open file, the type-strict `(schema, userVersion)` pair for an artifact, and creation declaring `CURRENT_GENERATION` because an empty database has no version to read. The body now states that contradiction and retires it explicitly: **`SCHEMA_USER_VERSION = 2` is no longer how a schema change happens**, and **the encoder is no longer derived from `schema.CANONICAL_TABLES`** — it is parameterised over the selected generation, so every digest is total over its own generation's manifest and an unchanged version-1 dataset keeps its version-1 digest byte for byte. It records the additive-only rule and why the governing-route association is three new join tables rather than a column on a generation-1 table (**no `ALTER TABLE` anywhere in the package**), the envelope's payload seam with its one internal conformance kind and the shipped `invalid_payload` code, `Route` as an operable scope axis (nine-entry confinement rule table with normalisation-as-comparison, an acyclicity walk anchored on the edge, `author_route` returning an existing route rather than a second row, `set_governing_route` refusing a different route for an already-governed row, and `find_governing_route`'s `None` as a fact rather than a default), and the mixed-generation merge preflight that refuses before any session exists while **a v1/v1/v1 merge on this build must still pass** under generation 1. The still-unclaimed behaviour narrows from L9 to **L10**, and one honest gap is recorded rather than implied: requirement 4.2's "no escaping symlink at resolution" clause has no implementation — `normalize_route_path` refuses only the lexical forms. Verification metadata: lastUpdated advanced, and the commit fields left at the last real commit because the code commit does not exist and closeout owns the stamp.
- 2026-09-17T07:33:51+00:00: Generated citation repair: `select_recorded_scope`; `_member_revision_ids`; `_frontier_expansions`; `_sort_key` repointed to mcp/src/agents_remember/memory/knowledge/read.py:193-238; mcp/src/agents_remember/memory/knowledge/read.py:342-352; mcp/src/agents_remember/memory/knowledge/read.py:355-390; mcp/src/agents_remember/memory/knowledge/read.py:469-480. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): re-pointed `_frontier_expansions` in the row 605 of this card from mcp/src/agents_remember/memory/knowledge/read.py:469-470 to mcp/src/agents_remember/memory/knowledge/read.py:224, the extent of the construct the claim is about (the checker named line(s) [224, 355] as its live location); re-pointed `_member_revision_ids` in the row 605 of this card from mcp/src/agents_remember/memory/knowledge/read.py:224 to mcp/src/agents_remember/memory/knowledge/read.py:216, the extent of the construct the claim is about (the checker named line(s) [216, 342] as its live location); re-pointed `_sort_key` in the row 605 of this card from mcp/src/agents_remember/memory/knowledge/read.py:216 to mcp/src/agents_remember/memory/knowledge/read.py:444, the extent of the construct the claim is about (the checker named line(s) [444, 469] as its live location)
- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): re-pointed `_frontier_expansions` in the row 605 of this card from mcp/src/agents_remember/memory/knowledge/read.py:193-194 to mcp/src/agents_remember/memory/knowledge/read.py:355-360, the extent of the construct the claim is about (the checker named line(s) [224, 355] as its live location); re-pointed `_member_revision_ids` in the row 605 of this card from mcp/src/agents_remember/memory/knowledge/read.py:355-360 to mcp/src/agents_remember/memory/knowledge/read.py:342-344, the extent of the construct the claim is about (the checker named line(s) [216, 342] as its live location); re-pointed `_sort_key` in the row 605 of this card from mcp/src/agents_remember/memory/knowledge/read.py:342-344 to mcp/src/agents_remember/memory/knowledge/read.py:469-470, the extent of the construct the claim is about (the checker named line(s) [444, 469] as its live location)
- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): re-pointed `_frontier_expansions` in the row 605 of this card from mcp/src/agents_remember/memory/knowledge/read.py:469-470 to mcp/src/agents_remember/memory/knowledge/read.py:355-360, the extent of the construct the claim is about (the checker named line(s) [224, 355] as its live location); re-pointed `_member_revision_ids` in the row 605 of this card from mcp/src/agents_remember/memory/knowledge/read.py:355-360 to mcp/src/agents_remember/memory/knowledge/read.py:342-344, the extent of the construct the claim is about (the checker named line(s) [216, 342] as its live location); re-pointed `select_recorded_scope` in the row 605 of this card from mcp/src/agents_remember/memory/knowledge/read.py:342-344 to mcp/src/agents_remember/memory/knowledge/read.py:193-194, the extent of the construct the claim is about (the checker named line(s) [193] as its live location)
- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): kept one copy of the repeated citation mcp/src/agents_remember/memory/knowledge/read.py:193-194 in the row 605 of this card; the repetition added no pooled evidence
- 2026-09-17T03:15+02:00 — 260915-KS-L8 curator (uncommitted change set on `ar/260915-ks-l08`, base `1ff1893f`): reviewed the route because its meaning changed again — two new `knowledge/diff*.py` modules add **the comparison half** of the experimental knowledge substrate, with `schema.py` untouched (still `ar-knowledge-sqlite/v1`, ten tables, fifteen triggers and the same `schema_fingerprint()`), plus two small additive changes to existing modules (`read.py`'s `SelectionQuery.seed_override` and `read_queries.py`'s five comparison readers). The body records the comparison's **single claim** and its four consequences (a removed before-side realization stays in the union; `present_outside_selection` is not `absent_from_snapshot`; record and source changes are separate collections so a source-only change cannot read as a changed obligation; and **no field, path or default can emit an invented no-consequence judgment**, with missing attribution kept as an advertised gap). It records **the coverage rules with the direction each was measured in** — rule 1 load-bearing alone, rule 2 a short-circuit that cannot decide a state its neighbours do not (its invariant half asserted, its **family half unexercised** because the fixture authors 0 family edges — a stated gap), rule 3 load-bearing in the forced-present direction — and that **collapsing them is wrong because it turns a missing selection into a real absence**, the reverse of the leaf's first claim. **The one extension to the read policy is recorded with the reviewer's evidence so nobody re-opens it**: `seed_override` is a parameterisation of R07's single rule, the policy still reads its seed once, and the mutation that ignores it kills a named node. It also carries the comparison's honest limits (three covered gaps and one non-experiment, each with a named closer; three equivalent mutants disclosed as equivalences) and states plainly that **the leaf's contested items are its evidence prose, carried to `KS-R09`/`L9` (ledger A9/A10), not its behaviour**, which five independent rounds could not falsify. The explicit non-claim narrows from L8 to **L9**. Anchor resolution remains claimed as of `KS-R07@v1`. Verification metadata: lastUpdated advanced, the reviewed candidate moved to `ar/260915-ks-l08`, and the commit fields left at the last real commit because the code commit does not exist and closeout owns the stamp.
- 2026-09-16T23:50+02:00 — 260915-KS-L7 curator (uncommitted change set on `ar/260915-ks-l07`, base `4eb2b199`): reviewed the route because its meaning changed again — four new `knowledge/read_*.py`-family modules add **the read half** of the experimental knowledge substrate, with `schema.py` untouched (still `ar-knowledge-sqlite/v1`, ten tables, fifteen triggers and the same `schema_fingerprint()`), plus two small load-bearing changes to existing modules (`logical.py`'s public `cell_value` as the one decoder a read page and the digest share, and `base.py`'s `require_plain_git_path` as the one Git-pathspec rule). The body records the **stopping rule** (the containing-family set frozen before membership expansion, which is what makes the traversal finite and what produces the packet's `P → I1`, `F → {I1, J1}`, `G → {J1, K1}` result with K1 excluded until `G` is selected explicitly), **three properties a consumer may rely on** (the corrected page counts — the declared total on every page, the walk's cumulative figure, the slice size in `len(page.items)`, enforced by a model validator; a truncated page that cannot be presentable as complete; and a response with **no field** that could hold a current-truth marker, a severity or a ranking), and **the path-refusal contract review corrected most sharply** — pathspec magic is the leading-`:` family plus `..`, absolute paths, `~`, drive/UNC spellings, backslashes and NUL, while `*`, `?` and `[` are literal characters to `ls-tree`, and the read path distinguishes `path_absent`, `unsupported_locator` and `recorded_object_unavailable` **so a caller is never told a path is absent when the real reason is its spelling**. It records the two honest limits rather than burying them — the **withdrawn** mutation claim over `_tree_entry`'s non-zero-exit branch, which stays an explicitly disclosed unasserted defensive branch (L9 **A6**), and `_manifest_digest`'s composition as a reachable covered gap (L9 **A4**) — the read-only/never-falls-back/cursor-as-binding boundaries, and the forward constraint that **L8 must split the 1 163-line unit module before adding cases**. The explicit non-claim narrows from L7–L8 to **L8**, and anchor resolution is now claimed as of `KS-R07@v1` instead of recorded as absent. Verification metadata: lastUpdated advanced, the reviewed candidate moved to `ar/260915-ks-l07`, and the commit fields left at the last real commit because the code commit does not exist and closeout owns the stamp.

- 2026-09-16T17:45+02:00 — 260915-KS-L6 curator (uncommitted change set on `ar/260915-ks-l06`, base `7db50f8f`): reviewed the route because its meaning changed again — three new `knowledge/export_*.py` modules add **the portable half**, the artifact format `ar-knowledge-export/v1` and its import, with no schema change (still `ar-knowledge-sqlite/v1`, ten tables, fifteen triggers and the same `schema_fingerprint()`). The body records the leaf's guarantee in the only form a consumer may rely on — **every accepted artifact is the canonical rendering of the logical content it carries**, so two artifacts that both validate and declare the same `logicalDigest` are the same bytes — and states that acceptance is **two** checks that are both needed: the whole-document gate (the exact rendering, at every level the format declares an order or a spelling for) and the header check (every declaration the one this build implements **and of the type this build writes**, with `userVersion` compared type-strictly so `1.0` and `true` are refused by name). It records what the digest covers and what the document form covers instead, the closed two-mode destination admission, the private stage and its sealed-aggregate verification, the never-patches-a-live-destination rule, the single body constructor that keeps one digest definition, the encoder's missing filesystem side effect, and the destination directory's real contents with **L4's open capture question Q1 carried forward**. Two staged checks are recorded as **documented non-experiments** rather than coverage, and the header namespace-binding guard at `:911` is recorded as a reachable guard with no killing node, reported for **L9**. The still-unclaimed behaviour narrows from L6–L8 to **L7–L8**. Verification metadata: lastUpdated advanced, the reviewed candidate moved to `ar/260915-ks-l06`, and the commit fields left at the last real commit because the code commit does not exist and closeout owns the stamp.
- 2026-09-16T13:45+02:00 — 260915-KS-L5 curator (uncommitted change set on `ar/260915-ks-l05`, base `3332a4ce`): reviewed the route because its meaning changed again — six new `knowledge/merge*.py` modules add **the merge half** of the experimental knowledge substrate with no schema change (still `ar-knowledge-sqlite/v1`, ten tables, fifteen triggers and the same `schema_fingerprint()`). The body records the ordered contract and why each step's position is load-bearing, the closed base claim, the one-comparison-per-input preflight, the changeset-not-patchset and coverage-by-replay rules, the aborting application, and the conflict record's engine-supplied old-side key. It states the two collision shapes a consumer must not flatten (an equal-payload same-ID insert is a conflict; two authored successors are not), the absent verdict, the callable-but-unwired adapter, the two recorded **non-experiments**, and the two pinned-binding facts recorded as facts rather than excuses. The still-unclaimed behaviour narrows from L5–L8 to L6–L8. Verification metadata remains empty until closeout stamps the code commit.

- 2026-09-16T11:30+02:00 — 260915-KS-L4 curator (uncommitted change set on `ar/260915-ks-l04`, base `76c7697c`): reviewed the route because its meaning changed, not only its file list. The storage package gained its **snapshot half** in five new `knowledge/` modules plus a second composition seam, with `schema.py` untouched, and this account records the five boundaries a reader needs before the mechanism: local working identity read rather than asserted (a receipt with no dataset digest), two-phase creation with occupied-destination-as-resume, a clone taken from a closed representation, closedness *proven* after a freeze that has to establish the journal mode on a fresh connection, replace-or-nothing publication against an admitted identity with a `no_change` that retains bytes, and disposal as a verdict whose two grounds are both identity-checked. **The durability correction is recorded as the reason two long-standing cards changed**: `store.close()` no longer unlinks WAL/SHM peers and `discard_closed_wal_peers` is now a caller precondition, because the unlink could not know whether another connection held the database and an unconditional call destroyed a committed batch when a reader blocked SQLite's checkpoint. The Hot Path Summary now names the snapshot modules in the same breath as the batch boundary. Two carried limitations and one disclosure are stated as limitations rather than properties: the new seam has no non-test importer in `mcp/src`, `authorization_ref` is carried but never examined, and the `atomic_write` directory fsync runs after `os.replace` (so a post-rename failure is reported as a replace failure). The explicit non-claim was narrowed from "L4–L8 behaviour" to "L5–L8 behaviour". Verification metadata remains closeout-owned.
- 2026-09-16T10:10+02:00 — 260915-KS-L3 curator (uncommitted change set on `ar/260915-ks-l03`, base `27242ecb`): reviewed the route because its meaning changed, not only its file list. The storage package gained the substrate's **single typed write boundary** in six new modules (`candidate`, `candidate_records`, `batch_preconditions`, `batch_commands`, `labels`, `logical`) with seven changed, and `schema.py` untouched. This account records the one-lock/one-transaction boundary and the published in-transaction helpers, the all-or-nothing property as measured evidence rather than a promise, the completed-graph validation axis with `lineage.declared_cycle` as the only supplier of the batch's declared edges, the fail-closed lane rules (baseline by name, `task-candidate` until a checkable binding exists), the resolved-not-asserted dataset identity, and the factual closed receipt. The explicit non-claim was narrowed from "L3–L8 behaviour" to "L4–L8 behaviour". **Two carried limitations are recorded as limitations rather than properties**: the refusal code `no_change` still has no producer (only the result state is reachable), and `application/knowledge.py` still has no non-test importer in `mcp/src`, so the boundary is not yet wired to any tool. Verification metadata remains empty until closeout stamps the code commit.
- 2026-09-16T08:24+02:00 — 260915-KS-L2 curator (uncommitted change set on `ar/260915-ks-l02`, base `60e0820e`):
  reviewed the route because its meaning changed, not only its file list. The storage package gained its relation
  half — family identity and sealed family revisions, source anchors, exact-revision memberships, realization
  claims and the reads that answer from both directions — in six new modules, with `schema.py` untouched because
  the six tables and their indexes already existed in version 1. Two body claims of the L1 account are
  **superseded**: that seven canonical tables "exist with no operations yet" (all ten are now reachable, and the
  six graph tables are written by the graph modules rather than by `store.py`), and that the lineage enforcement
  lives in `store.py` (the rule left for `knowledge/lineage.py` so both lineage graphs apply it once). The
  explicit non-claim was narrowed from "L2–L8 behaviour" to "L3–L8 behaviour" plus the still-absent anchor
  resolution. **One disclosed limitation is recorded as a disclosure rather than a property**: the `family`
  identity table carries no immutability trigger, so its display label and `label_provenance` are rewritable and
  an unreferenced row is deletable; that matches the v1 design and needs the declared `ar-knowledge-sqlite/v2`
  route because the triggers would change `schema_fingerprint()`. Verification metadata remains empty until
  closeout stamps the code commit.
- 2026-09-15T22:40+02:00 — 260915-KS-L1 curator (uncommitted change set on `ar/260915-ks-l01`, base `67b21aeb`):
  created this route overview because the package gained a new responsibility rather than only new files. It
  records the storage domain as a durable record store inside `memory/`, its ownership boundary against approval,
  task status and Git attribution, the eager ten-table version-1 schema, the insert-only/one-transaction rule, the
  post-insert lineage reach, the one-way import direction, and the explicit non-claims (L2–L8 behaviour, no IAS
  landing). Verification metadata remains empty until closeout stamps the code commit.
