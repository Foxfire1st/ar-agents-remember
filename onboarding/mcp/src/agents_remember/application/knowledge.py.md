# mcp/src/agents_remember/application/knowledge.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T10:10+02:00 |
| lastVerifiedCommitHash | `420669c459aab3650cdaa5b3e5271e71d7d94c0e`|
| lastVerifiedCommitDate | 2026-09-17T10:54:08+02:00|
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

**The candidate-write boundary now reaches this seam, and its three entry points each attach authority rather
than accepting it.** `resolve_candidate_context(destination, resolution)` opens the admitted destination
read-only, reads the identity the candidate actually holds (`store.snapshot_identity()`) and seals the whole
resolution — so a caller can only *resolve* the dataset identity its batch will be compared against, never write
one down. `build_candidate_context(snapshot, resolution)` is the pure sealing step it uses, exported so a caller
that already holds a snapshot does not have to re-open the store. `change_knowledge_candidate(destination, batch)`
opens the destination, delegates to `memory.knowledge.candidate.change_candidate` and closes in a `finally`,
passing `destination.authorship` as the operation's keyword argument — the provenance envelope comes from the
admission, never from the batch or from any draft inside it. `set_knowledge_invariant_label` and
`set_knowledge_family_label` are the same open/delegate/close shape over the two label edits.

`__all__` declares the twenty-seven served names.

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
  graph builder enforces the same rule through the same helper, and `change_knowledge_candidate` does the same
  for a whole batch by passing `destination.authorship` into the operation rather than reading it from the
  payload.
- No acceptance or promotion operation exists anywhere in this module: the store manufactures no acceptance, and
  `state_at_origin` plus `acceptance_ref` remain authored data.
- **This module decides no authority.** The destination is built by the admitted-authority path after its own
  checks, and namespace enforcement happens downstream in each store operation, which refuses a foreign
  namespace with `unauthorized_scope`.
- **Every operation re-opens the destination, and that is honest here.** `open_admitted_knowledge_store` →
  `open_existing_knowledge_store` re-validates the schema and refuses a missing path, so a per-call open is the
  correct shape for a seam with no resident process rather than a performance accident.
- **No non-test importer exists in `mcp/src` today, and `KS-R03` did not change that.** The candidate-change
  operation now exists *inside* this module and its cases drive it end to end, but adding a function to a module
  does not give the module an importer: a `grep` over `mcp/src` for importers of `application.knowledge` is still
  empty. The seam's tests are therefore behaviour evidence about the boundary, not evidence that it is wired into
  any tool or entry point — and the packet makes transport wiring an explicitly later extension. A worker report
  at this leaf claimed the boundary "resolved" that observation; the claim was false and the reviewer withdrew it.
- **A context's dataset identity is read, never supplied.** `CandidateResolution` deliberately has no
  dataset-identity field, so `resolve_candidate_context` is the only way to build a batch's precondition from
  this seam; an operation that accepted a caller-written digest would make the comparison meaningless.
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
| The provenance envelope is assigned here, not accepted from the payload. | `write_authorship` | mcp/src/agents_remember/application/knowledge.py:102-123 |
| The admitted-destination constructor that confers no authority by itself. | `admitted_knowledge_destination` | mcp/src/agents_remember/application/knowledge.py:125-142 |
| Provenance and namespace come from the destination, so a request cannot assert them. | `admitted_revision_request` | mcp/src/agents_remember/application/knowledge.py:144-158 |
| Initialization refuses an occupied destination as a resume attempt. | `initialize_knowledge_namespace` | mcp/src/agents_remember/application/knowledge.py:160-191 |
| The read open and the delegating insert, both closing in a `finally`. | `open_admitted_knowledge_store`; `create_knowledge_revision` | mcp/src/agents_remember/application/knowledge.py:193-205; mcp/src/agents_remember/application/knowledge.py:207-221 |
| The two standalone label operations the seam now exposes. | `set_knowledge_invariant_label`; `set_knowledge_family_label` | mcp/src/agents_remember/application/knowledge.py:224-238; mcp/src/agents_remember/application/knowledge.py:240-250 |
| The candidate context resolution and its pure sealing step — the only way a batch's dataset precondition is built from this seam. | `resolve_candidate_context`; `build_candidate_context` | mcp/src/agents_remember/application/knowledge.py:252-273; mcp/src/agents_remember/application/knowledge.py:275-301 |
| The batch operation that takes the destination's authorship rather than the payload's. | `change_knowledge_candidate` | mcp/src/agents_remember/application/knowledge.py:303-315 |
| The graph request builders, all attaching the destination's authorship and namespace. | `admitted_family_request`; `admitted_anchor_request`; `admitted_member_request`; `admitted_claim_request` | mcp/src/agents_remember/application/knowledge.py:327-338; mcp/src/agents_remember/application/knowledge.py:351-361; mcp/src/agents_remember/application/knowledge.py:363-372; mcp/src/agents_remember/application/knowledge.py:374-387 |
| The anchor-endpoint parameter that keeps naming an anchor distinct from recording one. | `admitted_claim_request`; `NewAnchor`; `AnchorReference` | mcp/src/agents_remember/application/knowledge.py:374-386; mcp/src/agents_remember/models/knowledge/result.py:266-270; mcp/src/agents_remember/models/knowledge/result.py:273-281 |
| The graph operations that open, delegate and close in a `finally`. | `create_knowledge_family`; `create_knowledge_family_revision`; `create_knowledge_anchor`; `remove_knowledge_anchor`; `create_knowledge_family_member`; `remove_knowledge_family_member`; `create_knowledge_realization_claim`; `remove_knowledge_realization_claim` | mcp/src/agents_remember/application/knowledge.py:423-433; mcp/src/agents_remember/application/knowledge.py:435-445; mcp/src/agents_remember/application/knowledge.py:447-457; mcp/src/agents_remember/application/knowledge.py:459-469; mcp/src/agents_remember/application/knowledge.py:471-481; mcp/src/agents_remember/application/knowledge.py:483-493; mcp/src/agents_remember/application/knowledge.py:495-505; mcp/src/agents_remember/application/knowledge.py:507-516 |
| The store operation this seam delegates to. | `create_revision` | mcp/src/agents_remember/memory/knowledge/store.py:231-265 |
| The batch operation and the lane rules the seam's entry point reaches. | `change_candidate`; `require_writable_lane` | mcp/src/agents_remember/memory/knowledge/candidate.py:61-80; mcp/src/agents_remember/memory/knowledge/candidate.py:83-102 |
| The graph modules the new operations delegate to. | `create_family`; `create_source_anchor`; `create_family_member`; `create_realization_claim` | mcp/src/agents_remember/memory/knowledge/families.py:79-96; mcp/src/agents_remember/memory/knowledge/anchors.py:49-70; mcp/src/agents_remember/memory/knowledge/memberships.py:88-109; mcp/src/agents_remember/memory/knowledge/realizations.py:61-83 |
| The layer charter that keeps this composition one-directional. | "[package.memory]" | layers.toml:206-222 |
| The focused cases that prove the seam, the composed graph path, the candidate batch and the layer direction. | `test_application_seam_initializes_and_extends_one_namespace`; `test_lower_ranked_owners_do_not_import_the_memory_domain`; "test_the_application_seam_authors_a_graph_through_an_admitted_destination"; "test_a_late_invalid_command_rolls_back_every_earlier_insert_in_the_batch" | mcp/tests/test_candidate_batch_transaction.py:62-62; mcp/tests/test_knowledge_relation_rules.py:566-566; mcp/tests/test_knowledge_store.py:736-786; mcp/tests/test_knowledge_store.py:789-807 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-17T06:49:47+00:00: Generated citation repair: `admitted_claim_request`; `NewAnchor`; `AnchorReference` repointed to mcp/src/agents_remember/application/knowledge.py:374-386; mcp/src/agents_remember/models/knowledge/result.py:273-281; mcp/src/agents_remember/models/knowledge/result.py:266-270. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T06:49:47+00:00: Generated citation repair: `test_application_seam_initializes_and_extends_one_namespace`; `test_lower_ranked_owners_do_not_import_the_memory_domain`; "test_the_application_seam_authors_a_graph_through_an_admitted_destination"; "test_a_late_invalid_command_rolls_back_every_earlier_insert_in_the_batch" repointed to mcp/tests/test_knowledge_store.py:736-786; mcp/tests/test_knowledge_store.py:789-807; mcp/tests/test_knowledge_relation_rules.py:566-566; mcp/tests/test_candidate_batch_transaction.py:62-62. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): clamped mcp/src/agents_remember/application/knowledge.py:507-517 to mcp/src/agents_remember/application/knowledge.py:507-516, the range the cited construct now occupies
- 2026-09-16T10:10+02:00 — 260915-KS-L3 curator (uncommitted change set on `ar/260915-ks-l03`, base `27242ecb`): **recorded the candidate-write boundary arriving at the seam, and that the seam's wiring boundary did not move with it.** This module gained `resolve_candidate_context` and `build_candidate_context` (the only way a batch's dataset precondition is built: the application *reads* the identity the candidate holds and seals it, because `CandidateResolution` deliberately has no dataset-identity field), `change_knowledge_candidate` (open, delegate, close, passing `destination.authorship` so a batch cannot supply its own provenance) and the two label operations; `__all__` is now twenty-seven names. **The boundary that did not move is the one a later reader most needs:** adding a function inside `application/knowledge.py` does not give it an importer, so the seam still has **no non-test importer in `mcp/src`**, the worker report's "resolved" claim about that observation was false, and the reviewer withdrew it. Citation ranges were re-derived. Verification metadata remains closeout-owned.
- 2026-09-16T08:24+02:00 — 260915-KS-L2 curator (uncommitted change set on `ar/260915-ks-l02`, base `60e0820e`): recorded the graph half's arrival at this seam — eight request builders that attach the destination's authorship and namespace exactly as the revision builder does, eight operations of the same open/delegate/close shape, and the one builder that takes an extra parameter (the anchor endpoint, because naming an anchor and recording one are different inputs). Also recorded the boundary a later reader most needs: the seam still has **no non-test importer in `mcp/src`**, so the typed write boundary that consumes it is `KS-R03`'s and the seam's tests are not wiring evidence. Verification metadata remains empty until closeout stamps the code commit.
- 2026-09-15T22:40+02:00 — 260915-KS-L1 curator (uncommitted change set on `ar/260915-ks-l01`, base `67b21aeb`): created this one-to-one card for the new application composition seam. It records that provenance is assigned rather than parameterized, that initialization refuses an occupied destination, and that no acceptance/promotion operation exists. Verification metadata remains empty until closeout stamps the code commit.
