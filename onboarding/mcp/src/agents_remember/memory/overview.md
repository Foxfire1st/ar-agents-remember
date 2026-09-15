# mcp/src/agents_remember/memory/ - Memory Repository Lifecycle And Knowledge Storage Overview

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `mcp/src/agents_remember/memory/` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-09-15T22:40+02:00 |
| lastVerifiedCommitHash |  `60e0820e6cb3b1d160518b9f8c7ac6241323a281`|
| lastVerifiedCommitDate |  2026-09-15T22:46:24+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l01` uncommitted source; base `67b21aeb66df96a971a33ae431a13992f2528b45` |
| governingOverview | `../../../overview.md` |

## Governing Overview

[mcp/overview.md](../../../overview.md)

## What This Area Is

The route owns two distinct responsibilities, and they are deliberately not the same thing:

1. **Memory-repository lifecycle** (`baseline.py`, `carryover.py`, `carryover_authority.py`) — initializing a
   memory repository, adopting an existing onboarding tree as a first ledgered baseline, and carrying richer
   onboarding from a source branch into an open recovery leaf.
2. **Concrete knowledge storage** (`knowledge/`) — the APSW-backed SQLite candidate that holds repository,
   invariant and revision identity. Added by 260915-KS-L1 as an experimental increment; it is a durable record
   store, so it ranks here with the record stores rather than with the application layer that admits its writes.

The two responsibilities share a package rank and a charter paragraph, not a mechanism: nothing in the
lifecycle modules imports `knowledge/`, and nothing in `knowledge/` reads, writes or migrates Markdown onboarding.

## Purpose

`memory/` is the durable-store route. Its members own the on-disk representation of two different things — a
repository's onboarding tree and an authored knowledge candidate — and both are stores that a higher-ranked
admitted authority writes through rather than authors.

## Hot Path Summary

`knowledge/store.py` owns the one insert-only revision operation and its refusals; `knowledge/schema.py` owns the
declaration of the ten STRICT tables, the fifteen immutability triggers and `schema_fingerprint()`;
`knowledge/connection.py` owns the pragma contract and the open-time schema validation; `baseline.py` /
`carryover.py` / `carryover_authority.py` own baseline adoption and branch carryover. The import direction is
enforced: no package ranked below `memory` (rank 12) may import `memory.knowledge`, and `application` (rank 21) is
its only consumer.

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

Seven of the ten canonical tables (family, family revision, family predecessor, source anchor, family member,
realization claim — plus the family/claim surface generally) exist in version 1 with no operations yet. They are
created eagerly and on purpose: a SQLite session changeset can only carry operations for tables both sides
already have, and a table present on one side only is exactly the schema mismatch the merge preflight must
refuse. Later leaves extend behaviour inside a stable schema instead of migrating it.

The lineage rule is the one place where the code states a contract twice on purpose. `create_revision` refuses as
`lineage_cycle` when inserting the candidate would leave **any** revision in the invariant's lineage graph on a
cycle — the candidate itself, or a retained revision reachable from it through predecessors. The guard is
evaluated over the post-insert graph and before any row is written. A revision that merely descends from a stored
cycle is therefore refused even though its own lineage is acyclic, and the refusal says so rather than claiming
self-reachability.

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
  remains operational authority, and L2–L8 behaviour (families and realization links, the admitted batch
  contract, snapshot publication, Git merging, portable roundtrip, selective read and candidate diff) is not
  claimed by this route's storage package.

## Repo-Internal References

The declarations below establish the current behaviour; this inventory is not execution evidence.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The storage home is declared in the memory package charter as a wording addition only. | L206-L222 | [layers.toml](../../../../layers.toml) |
| The canonical table list, column order and required feature set the store is validated against. | L26-L42; L47-L112; L352-L359 | [schema.py](knowledge/schema.py) |
| The declared DDL: ten STRICT tables with explicit NOT NULL keys, composite deferred FKs and the self-edge CHECK. | L117-L266 | [schema.py](knowledge/schema.py) |
| The fifteen immutability triggers whose names the merge preflight compares. | L284-L350 | [schema.py](knowledge/schema.py) |
| The structural manifest and the fingerprint over manifest plus DDL text. | L362-L392 | [schema.py](knowledge/schema.py) |
| The verified pragma contract and the create-versus-validate open. | L37-L84 | [connection.py](knowledge/connection.py) |
| The one atomic insert-only revision operation with its ordered preconditions. | L212-L241; L279-L326 | [store.py](knowledge/store.py) |
| The lineage rule stated once, including its post-insert scope and before-any-write evaluation. | L298-L310 | [store.py](knowledge/store.py) |
| The two-branch cycle enforcement and its Tarjan vertex classification. | L378-L447 | [store.py](knowledge/store.py) |
| The typed refusal vocabulary and the SQLite-error mapping that shares the trigger-message prefix. | L57-L77; L238-L277; L308-L350 | [refusals.py](knowledge/refusals.py) |
| The row codecs, including the read-time seal re-derivation. | L38-L49; L135-L169 | [records.py](knowledge/records.py) |
| The composition seam that assigns provenance and is the only consumer of this storage package. | L46-L66; L104-L165 | [application/knowledge.py](../application/knowledge.py) |
| The shared knowledge vocabulary written by this store. | L1-L8; L55-L88 | [models/knowledge/\_\_init\_\_.py](../models/knowledge/__init__.py) |
| The kernel canonical encoder the seal and the schema fingerprint are computed through. | L16-L37 | [kernel/canonical_json.py](../kernel/canonical_json.py) |
| The branching fixture the storage cases build from. | L90-L133 | [mcp/tests/knowledge_fixture_test_support.py](../../../../mcp/tests/knowledge_fixture_test_support.py) |
| The focused suite, registered in the unit lane, that exercises this route's storage behaviour. | L87-L768 | [mcp/tests/test_knowledge_store.py](../../../../mcp/tests/test_knowledge_store.py) |
| The fixture's registered stable contract and evidence node. | — | [mcp/tests/evidence-lifecycle.toml](../../../../mcp/tests/evidence-lifecycle.toml) |

## Cross-Repo References

No cross-repository authority is established by this route. The store writes one SQLite file inside the code
worktree it was opened against, and the memory-repository lifecycle can address a sibling external-memory
checkout, but neither establishes a boundary contract here.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-15T22:40+02:00 — 260915-KS-L1 curator (uncommitted change set on `ar/260915-ks-l01`, base `67b21aeb`):
  created this route overview because the package gained a new responsibility rather than only new files. It
  records the storage domain as a durable record store inside `memory/`, its ownership boundary against approval,
  task status and Git attribution, the eager ten-table version-1 schema, the insert-only/one-transaction rule, the
  post-insert lineage reach, the one-way import direction, and the explicit non-claims (L2–L8 behaviour, no IAS
  landing). Verification metadata remains empty until closeout stamps the code commit.
