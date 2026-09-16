# mcp/src/agents_remember/memory/ - Memory Repository Lifecycle And Knowledge Storage Overview

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `mcp/src/agents_remember/memory/` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-09-16T13:45+02:00 |
| lastVerifiedCommitHash |  `7db50f8f4a67e60f9011266110ad6d0156f1a905`|
| lastVerifiedCommitDate |  2026-09-16T14:02:05+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l05` uncommitted source; base `3332a4ce7029777d49feca22b499350435a9f83c` |
| governingOverview | `../../../overview.md` |

## Governing Overview

[mcp/overview.md](../../../overview.md)

## What This Area Is

The route owns two distinct responsibilities, and they are deliberately not the same thing:

1. **Memory-repository lifecycle** (`baseline.py`, `carryover.py`, `carryover_authority.py`) — initializing a
   memory repository, adopting an existing onboarding tree as a first ledgered baseline, and carrying richer
   onboarding from a source branch into an open recovery leaf.
2. **Concrete knowledge storage** (`knowledge/`) — the APSW-backed SQLite candidate that holds repository,
   invariant, revision, family, anchor, membership and realization identity. Added by 260915-KS-L1 as an
   experimental increment and extended by 260915-KS-L2, 260915-KS-L3 and 260915-KS-L4; it is a durable record
   store, so it ranks here with the record stores rather than with the application layer that admits its writes.

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
declaration of the ten STRICT tables, the fifteen immutability triggers and `schema_fingerprint()`;
`knowledge/connection.py` owns the pragma contract, the one-row reader, the read-only connection every identity
confirmation uses, and the open-time schema validation; `baseline.py` / `carryover.py` / `carryover_authority.py`
own baseline adoption and branch carryover. **The snapshot half** lives in `knowledge/candidate_workspace.py`
(create, resume, clone, disposal verdict), `knowledge/candidate_receipt.py` (the sealed receipt and its binding
comparison), `knowledge/closed_snapshot.py` (the one freeze procedure both publication and cloning use),
`knowledge/publication.py` (atomic, verifiable install under a destination lock), `knowledge/materialization.py`
(the read-side publication gate), and `knowledge/logical.py`'s `dataset_identity` entry point. The import
direction is enforced: no package ranked below `memory` (rank 12) may import `memory.knowledge`, and `application`
(rank 21) is its only consumer.

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

## Invariants And Boundaries

- **Import direction is one-way.** `memory.knowledge` imports `kernel.canonical_json`, `kernel.file_lock` and
  `models.knowledge`; no package ranked below `memory` may import it back. A focused test guards this so a later
  reverse import fails a check rather than passing review.
- **Insert-only, one lock, one transaction.** Every mutation holds the candidate's exclusive file lock and runs
  inside one `BEGIN IMMEDIATE`; a refusal rolls back, so an expected failure never leaves a partial aggregate.
- **The schema is a generation, not a file.** A schema change is `ar-knowledge-sqlite/v2` with
  `SCHEMA_USER_VERSION = 2`, never a silent edit of version 1, because `schema_fingerprint()` and the merge
  preflight both compare it. Opening an existing database validates tables, columns and the full trigger set.
- **Refusals are returned values.** A caller branches on a typed code, never on message text; a storage failure
  with no contract code is reported as a defect (`KnowledgeStorageError`), not as an outcome to handle.
- **Vocabulary is defined where it decides.** Literal states, operation names, refusal codes and version strings
  live in `models.knowledge` and are imported by the decider, never defined by the decider and imported back down.
- **This is an experimental increment on the master's branch pair.** No IAS landing is implied, legacy Markdown
  remains operational authority, and the still-unclaimed behaviour is now L5–L8 (Git merging, portable roundtrip,
  selective read and candidate diff) — snapshot publication is claimed by this route as of `KS-R04@v1`. The admitted batch contract *is* claimed by this route as
  of `KS-R03@v1` — one lock, one transaction, one closed command union and one resolved dataset identity — while the
  `task-candidate` lane deliberately refuses until a later leaf supplies a checkable binding. The graph half is
  claimed as of `KS-R02@v1`: families, anchors, memberships and realization claims are stored and readable from both
  directions, while anchor **resolution** remains `KS-R07`'s and is deliberately absent here.
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
| The merge orchestration: the ordered sequence, the one-lock policy, the conflict taxonomy and the engine-supplied conflict key. | `merge_knowledge_datasets`; `_TAXONOMY`; `_conflict_record`; `_freeze_merged` | mcp/src/agents_remember/memory/knowledge/merge.py:131-163; mcp/src/agents_remember/memory/knowledge/merge.py:608-614; mcp/src/agents_remember/memory/knowledge/merge.py:626-637; mcp/src/agents_remember/memory/knowledge/merge.py:698-734 |
| The base resolution: the closed two-member claim and the two refusals a base claim can earn. | `resolve_merge_base`; `_ancestry_refusal`; `_uniqueness_refusal` | mcp/src/agents_remember/memory/knowledge/merge_base.py:75-105; mcp/src/agents_remember/memory/knowledge/merge_base.py:181-196; mcp/src/agents_remember/memory/knowledge/merge_base.py:199-224 |
| The structural preflight that runs before any session exists, and the declared manifest it compares against. | `require_supported_structure`; `declared_structure`; `compare_structures` | mcp/src/agents_remember/memory/knowledge/merge_schema.py:121-139; mcp/src/agents_remember/memory/knowledge/merge_schema.py:78-88; mcp/src/agents_remember/memory/knowledge/merge_schema.py:142-183 |
| The changeset half: the directional delta build, the aborting application, the old-side conflict key and the coverage replay. | `build_delta`; `apply_changeset`; `_conflicting_key`; `replay_delta` | mcp/src/agents_remember/memory/knowledge/merge_changeset.py:185-220; mcp/src/agents_remember/memory/knowledge/merge_changeset.py:223-263; mcp/src/agents_remember/memory/knowledge/merge_changeset.py:266-289; mcp/src/agents_remember/memory/knowledge/merge_changeset.py:292-331 |
| The postcondition half, including the two call sites this leaf recorded as unreachable by a black-box case. | `require_structural_validity`; `require_immutable_revisions_preserved`; `require_applied_changes` | mcp/src/agents_remember/memory/knowledge/merge_validation.py:73-101; mcp/src/agents_remember/memory/knowledge/merge_validation.py:104-152; mcp/src/agents_remember/memory/knowledge/merge_validation.py:169-211 |
| The merge's refusal vocabulary, one factory per observable failure point. | `schema_mismatch_refusal`; `conflicting_values_refusal`; `duplicate_identity_refusal`; `delete_reference_conflict_refusal` | mcp/src/agents_remember/memory/knowledge/merge_refusals.py:21-45; mcp/src/agents_remember/memory/knowledge/merge_refusals.py:70-94; mcp/src/agents_remember/memory/knowledge/merge_refusals.py:97-121; mcp/src/agents_remember/memory/knowledge/merge_refusals.py:124-151 |
| The two operations and twelve codes the merge added to the shared vocabulary. | `KnowledgeOperation`; `KnowledgeRefusalCode` | mcp/src/agents_remember/models/knowledge/result.py:36-62; mcp/src/agents_remember/models/knowledge/result.py:66-111 |
| The measurement the merge reports, and the merge's own third composition seam. | `MergeCoverage`; `merge_resolved_knowledge_datasets` | mcp/src/agents_remember/models/knowledge/merge.py:243-284; mcp/src/agents_remember/models/knowledge/merge.py:293-346; mcp/src/agents_remember/application/knowledge_merge.py:55-64 |
| The shared case harness registered as `contract:common-base-merge-cases`, and its evidence node. | "test_disjoint_edits_from_both_sides_survive_in_a_closed_published_candidate" | mcp/tests/merge_case_test_support.py:511-571; mcp/tests/test_knowledge_guarded_merge.py:248-312 |
| The governed-artifact row and the exact two-consumer list this leaf registered in the shared catalog. | `contract:common-base-merge-cases` | mcp/tests/evidence-lifecycle.toml:1132-1151 |

| Finding | Citations | Source Path |
| --- | --- | --- |
| The storage home is declared in the memory package charter as a wording addition only. | L206-L222 | [layers.toml](../../../../layers.toml) |
| The canonical table list, column order and required feature set the store is validated against. | L26-L42; L47-L112; L352-L359 | [schema.py](knowledge/schema.py) |
| The declared DDL: ten STRICT tables with explicit NOT NULL keys, composite deferred FKs and the self-edge CHECK. | L117-L266 | [schema.py](knowledge/schema.py) |
| The fifteen immutability triggers whose names the merge preflight compares — and, by their absence, the disclosed `family` identity gap recorded above. | L286-L350 | [schema.py](knowledge/schema.py) |
| The structural manifest and the fingerprint over manifest plus DDL text. | L362-L392 | [schema.py](knowledge/schema.py) |
| The verified pragma contract, the shared one-row reader and the create-versus-validate open. | L38-L85 | [connection.py](knowledge/connection.py) |
| The one atomic insert-only revision operation with its ordered preconditions. | L224-L259; L296-L344 | [store.py](knowledge/store.py) |
| The lineage rule stated once, including its post-insert scope and before-any-write evaluation. | L315-L326 | [store.py](knowledge/store.py) |
| The shared lineage rule both graphs apply, and the family graph's application of it. | L71-L86; L186-L203 | [lineage.py](knowledge/lineage.py) |
| The family owner: identity, sealed revisions, family lineage and the narrow ownership read. | L78-L141; L169-L203; L233-L264 | [families.py](knowledge/families.py) |
| The anchor owner: authored locations stored as recorded, with explicit identity-plus-digest removal. | L49-L112; L145-L189 | [anchors.py](knowledge/anchors.py) |
| The membership owner: one exact pair, both read directions, stale-caller removal. | L59-L122; L123-L175; L201-L232 | [memberships.py](knowledge/memberships.py) |
| The realization owner: the anchored-claim transaction and both read directions over the same rows. | L61-L122; L123-L159; L238-L269 | [realizations.py](knowledge/realizations.py) |
| The shared relation-endpoint check the two relation writes both use. | L25-L56 | [endpoints.py](knowledge/endpoints.py) |
| The typed refusal vocabulary and the SQLite-error mapping, whose failure context now names the caller's operation and table. | L57-L79; L238-L286; L609-L652 | [refusals.py](knowledge/refusals.py) |
| The row codecs, including the read-time seal re-derivation over the stored row and its stored edges. | L56-L69; L153-L189; L327-L356 | [records.py](knowledge/records.py) |
| The composition seam that assigns provenance and is the only consumer of this storage package. | L83-L105; L141-L212; L213-L274 | [application/knowledge.py](../application/knowledge.py) |
| The shared knowledge vocabulary written by this store, including the graph shapes. | L1-L8; L98-L170 | [models/knowledge/\_\_init\_\_.py](../models/knowledge/__init__.py) |
| The kernel canonical encoder the seal and the schema fingerprint are computed through. | L27-L37 | [kernel/canonical_json.py](../kernel/canonical_json.py) |
| The branching fixture — now carrying both the identity and the graph half — the storage and graph cases build from. | L203-L263 | [mcp/tests/knowledge_fixture_test_support.py](../../../../mcp/tests/knowledge_fixture_test_support.py) |
| The graph case support module, with its registered contract and exact consumer set. | L1-L20 | [mcp/tests/knowledge_graph_test_support.py](../../../../mcp/tests/knowledge_graph_test_support.py) |
| The focused suite, registered in the unit lane, that exercises this route's storage behaviour. | L87-L767 | [mcp/tests/test_knowledge_store.py](../../../../mcp/tests/test_knowledge_store.py) |
| The graph suites registered in the unit lane: family revision rules, relation writes, graph reads and the payload seals. | L1-L20 | [test_knowledge_family_revision.py](../../../../mcp/tests/test_knowledge_family_revision.py) |
| The node that isolates the sealed predecessor field on each payload, added by the fix-verification round. | L63-L95 | [test_knowledge_revision_seals.py](../../../../mcp/tests/test_knowledge_revision_seals.py) |
| The fixture's registered stable contract, its evidence node and its five declared consumers. | L1031-L1081 | [mcp/tests/evidence-lifecycle.toml](../../../../mcp/tests/evidence-lifecycle.toml) |

## Cross-Repo References

No cross-repository authority is established by this route. The store writes one SQLite file inside the code
worktree it was opened against, and the memory-repository lifecycle can address a sibling external-memory
checkout, but neither establishes a boundary contract here.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

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
