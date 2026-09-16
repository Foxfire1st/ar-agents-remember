# mcp/src/agents_remember/application/knowledge.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T08:24+02:00 |
| lastVerifiedCommitHash | `27242ecbefd79f2e8fbc6db32e02013fa8298ba3`|
| lastVerifiedCommitDate | 2026-09-16T08:41:27+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[application route overview](../overview.md)

## Purpose

The composition seam between admitted authority and the concrete knowledge store. This is where a destination
becomes an authorized handle and where the required provenance envelope is actually assigned.

## Code Commentary

### Logic

`write_authorship` builds the `Authorship` envelope for one admitted write and **assigns** `operation_id` (a fresh
`uuid4`) and `recorded_at` (UTC now, unless the caller passes one) rather than accepting them from the payload.

`admitted_knowledge_destination` is the constructor the admitted authority path calls after its own checks; it
binds a resolved `database_path`, the `RepositoryIdentity` and an `Authorship` into an
`AdmittedKnowledgeDestination`.

`admitted_revision_request` attaches one authored `RevisionDraft` to its destination: the caller supplies what was
authored, while the repository identity and the provenance envelope come from the destination.

`initialize_knowledge_namespace` refuses an **occupied** destination outright with `destination_occupied` (an
existing path is a resume attempt, never permission to initialize over it), otherwise opens the store, calls
`create_repository` and closes it in a `finally`.

`open_admitted_knowledge_store` opens for reads only, without creating or repairing, and documents that the caller
owns the returned store and must close it.

`create_knowledge_revision` opens the admitted destination and delegates to `OpenedKnowledgeStore.create_revision`,
closing in a `finally`. It refuses rather than repairs: a foreign namespace, an identity reuse, a lineage
violation and an unrecognized schema all return a typed refusal with the row count unchanged.

**The graph half now has its own request builders and operations at the same seam**, in the same two-part shape.
The builders (`admitted_family_request`, `admitted_family_revision_request`, `admitted_anchor_request`,
`admitted_member_request`, `admitted_claim_request`, and the three `admitted_*_removal` variants) all attach the
destination's `authorship` and `repository_id`, so every graph write inherits the provenance rule rather than
restating it. The operations (`create_knowledge_family`, `create_knowledge_family_revision`,
`create_knowledge_anchor`, `remove_knowledge_anchor`, `create_knowledge_family_member`,
`remove_knowledge_family_member`, `create_knowledge_realization_claim`, `remove_knowledge_realization_claim`)
each open the admitted destination, delegate to the owning graph module, and close in a `finally`.

`admitted_claim_request` is the one builder that takes an extra parameter: the anchor endpoint, because naming an
existing anchor and recording a new one in the same transaction are different inputs and the seam must not
collapse them.

`__all__` declares the twenty-four served names.

### Conventions

The direction matters and the module docstring states it: storage ranks below application, and the worktree and
memory-quality owners rank below storage, so a lower owner receives `models.knowledge` values — never an import of
this module or of the store. This module is the only place the admitted authority and the concrete store are
wired together. It holds no schema and no durable state: it admits, delegates and returns the typed result
unchanged.

Each graph implementation is three lines of the same shape (open, delegate, close), which is deliberate: the seam
exists to attach authority and provenance, and a rule that belongs to a graph module must not be duplicated here
to save a call.

### Invariants And Boundaries

- Provenance is **not a parameter**: `admitted_revision_request` overwrites the draft's provenance from the
  destination, so a request cannot claim an actor or an authorization the admission did not establish. Every
  graph builder enforces the same rule through the same helper.
- No acceptance or promotion operation exists anywhere in this module: the store manufactures no acceptance, and
  `state_at_origin` plus `acceptance_ref` remain authored data.
- **This module decides no authority.** The destination is built by the admitted-authority path after its own
  checks, and namespace enforcement happens downstream in each store operation, which refuses a foreign
  namespace with `unauthorized_scope`.
- **Every operation re-opens the destination, and that is honest here.** `open_admitted_knowledge_store` →
  `open_existing_knowledge_store` re-validates the schema and refuses a missing path, so a per-call open is the
  correct shape for a seam with no resident process rather than a performance accident.
- **No non-test importer exists in `mcp/src` today.** `application/knowledge.py` is reachable only from the two
  test modules that drive it (`test_knowledge_store.py`, `test_knowledge_relation_rules.py`); the typed write
  boundary that will consume it is `KS-R03`. A later reader must not read the seam's tests as evidence that it is
  wired into any tool or entry point.
- Every opened store is closed in a `finally`; the read path returns the caller-owned store deliberately so a
  multi-read flow does not pay a reopen per read.
- This module is the only permitted consumer of `memory.knowledge` (rank 12) from `application` (rank 21); the
  layer direction is verified by a focused test, so a later reverse import fails a check rather than passing
  review.

### Todos

None recorded. The admitted-authority path that calls `admitted_knowledge_destination` and the typed write
boundary that consumes the graph operations are `KS-R03`'s composition work; this leaf exposes the seam and proves
it with a focused test.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The provenance envelope is assigned here, not accepted from the payload. | `write_authorship` | mcp/src/agents_remember/application/knowledge.py:83-105 |
| The admitted-destination constructor that confers no authority by itself. | `admitted_knowledge_destination` | mcp/src/agents_remember/application/knowledge.py:106-124 |
| Provenance and namespace come from the destination, so a request cannot assert them. | `admitted_revision_request` | mcp/src/agents_remember/application/knowledge.py:125-140 |
| Initialization refuses an occupied destination as a resume attempt. | `initialize_knowledge_namespace` | mcp/src/agents_remember/application/knowledge.py:141-173 |
| The read open and the delegating insert, both closing in a `finally`. | `open_admitted_knowledge_store`; `create_knowledge_revision` | mcp/src/agents_remember/application/knowledge.py:174-187; mcp/src/agents_remember/application/knowledge.py:188-212 |
| The graph request builders, all attaching the destination's authorship and namespace. | `admitted_family_request`; `admitted_anchor_request`; `admitted_member_request`; `admitted_claim_request` | mcp/src/agents_remember/application/knowledge.py:213-225; mcp/src/agents_remember/application/knowledge.py:237-248; mcp/src/agents_remember/application/knowledge.py:249-259; mcp/src/agents_remember/application/knowledge.py:260-274 |
| The anchor-endpoint parameter that keeps naming an anchor distinct from recording one. | `admitted_claim_request`; `NewAnchor`; `AnchorReference` | mcp/src/agents_remember/application/knowledge.py:260-274; mcp/src/agents_remember/models/knowledge/result.py:190-207 |
| The eight graph operations that open, delegate and close in a `finally`. | `create_knowledge_family`; `create_knowledge_family_revision`; `create_knowledge_anchor`; `create_knowledge_family_member`; `create_knowledge_realization_claim`; `remove_knowledge_realization_claim` | mcp/src/agents_remember/application/knowledge.py:309-320; mcp/src/agents_remember/application/knowledge.py:321-332; mcp/src/agents_remember/application/knowledge.py:333-344; mcp/src/agents_remember/application/knowledge.py:357-368; mcp/src/agents_remember/application/knowledge.py:381-392; mcp/src/agents_remember/application/knowledge.py:393-402 |
| The store operation this seam delegates to. | `create_revision` | mcp/src/agents_remember/memory/knowledge/store.py:224-259 |
| The graph modules the new operations delegate to. | `create_family`; `create_source_anchor`; `create_family_member`; `create_realization_claim` | mcp/src/agents_remember/memory/knowledge/families.py:78-95; mcp/src/agents_remember/memory/knowledge/anchors.py:49-70; mcp/src/agents_remember/memory/knowledge/memberships.py:59-80; mcp/src/agents_remember/memory/knowledge/realizations.py:61-83 |
| The layer charter that keeps this composition one-directional. | "[package.memory]" | layers.toml:206-222 |
| The focused cases that prove the seam, the composed graph path and the layer direction. | `test_application_seam_initializes_and_extends_one_namespace`; `test_lower_ranked_owners_do_not_import_the_memory_domain`; "test_the_application_seam_authors_a_graph_through_an_admitted_destination" | mcp/tests/test_knowledge_store.py:696-767; mcp/tests/test_knowledge_relation_rules.py:566-680 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-16T08:24+02:00 — 260915-KS-L2 curator (uncommitted change set on `ar/260915-ks-l02`, base `60e0820e`): recorded the graph half's arrival at this seam — eight request builders that attach the destination's authorship and namespace exactly as the revision builder does, eight operations of the same open/delegate/close shape, and the one builder that takes an extra parameter (the anchor endpoint, because naming an anchor and recording one are different inputs). Also recorded the boundary a later reader most needs: the seam still has **no non-test importer in `mcp/src`**, so the typed write boundary that consumes it is `KS-R03`'s and the seam's tests are not wiring evidence. Verification metadata remains empty until closeout stamps the code commit.
- 2026-09-15T22:40+02:00 — 260915-KS-L1 curator (uncommitted change set on `ar/260915-ks-l01`, base `67b21aeb`): created this one-to-one card for the new application composition seam. It records that provenance is assigned rather than parameterized, that initialization refuses an occupied destination, and that no acceptance/promotion operation exists. Verification metadata remains empty until closeout stamps the code commit.
