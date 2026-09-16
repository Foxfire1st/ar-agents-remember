# mcp/src/agents_remember/memory/ - Memory Repository Lifecycle And Knowledge Storage Overview

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `mcp/src/agents_remember/memory/` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-09-16T10:10+02:00 |
| lastVerifiedCommitHash |  `76c7697ca275a8d2764729145c950c166f3f9ec3`|
| lastVerifiedCommitDate |  2026-09-16T10:27:28+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l03` uncommitted source; base `27242ecbefd79f2e8fbc6db32e02013fa8298ba3` |
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
   experimental increment and extended by 260915-KS-L2; it is a durable record store, so it ranks here with the
   record stores rather than with the application layer that admits its writes.

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
vocabulary both read, and `knowledge/logical.py` owns the canonical logical dataset identity.
`knowledge/store.py` owns the one insert-only single-record revision operation, the package's shared candidate lock
and its one-immediate-transaction wrapper, and the invariant half's tables; `knowledge/{families,anchors,memberships,realizations}.py`
own the four graph concepts and their tables, `knowledge/lineage.py` owns the one acyclic-lineage rule both lineage
graphs apply (including the batch's declared-edge caller), `knowledge/labels.py` owns the two label edits and their
row-digest guard, and `knowledge/endpoints.py` owns the shared relation-endpoint check; `knowledge/schema.py` owns the
declaration of the ten STRICT tables, the fifteen immutability triggers and `schema_fingerprint()`;
`knowledge/connection.py` owns the pragma contract, the one-row reader and the open-time schema validation;
`baseline.py` / `carryover.py` / `carryover_authority.py` own baseline adoption and branch carryover. The import
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
  remains operational authority, and the still-unclaimed behaviour is now L4–L8 (snapshot publication, Git merging,
  portable roundtrip, selective read and candidate diff). The admitted batch contract *is* claimed by this route as
  of `KS-R03@v1` — one lock, one transaction, one closed command union and one resolved dataset identity — while the
  `task-candidate` lane deliberately refuses until a later leaf supplies a checkable binding. The graph half is
  claimed as of `KS-R02@v1`: families, anchors, memberships and realization claims are stored and readable from both
  directions, while anchor **resolution** remains `KS-R07`'s and is deliberately absent here.
- **A published write helper assumes the caller's lock and transaction.** The batch forced those helpers public; a
  future caller that invokes one outside a transaction would write an autocommitted row silently. Every shipped call
  site satisfies the precondition, and keeping the rule is what the one-lock/one-transaction invariant rests on.

## Repo-Internal References

The declarations below establish the current behaviour; this inventory is not execution evidence.

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
