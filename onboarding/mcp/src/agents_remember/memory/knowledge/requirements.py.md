# mcp/src/agents_remember/memory/knowledge/requirements.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**A database home for requirement *meaning*, and never a second task authority.** This module is the
whole operation surface of `RequirementRevision`. It adds no table: a requirement revision is an
envelope record, written through the one payload seam
`record_envelope.validate_record_payload` and stored in the shipped `knowledge_record` /
`record_revision` tables.

**Why the record group has no table of its own.** The delivered envelope already carries every fact a
requirement revision needs — record identity, `kind`, `authority_home`, `lifecycle` and the governing
route on `knowledge_record`; the frozen payload, its content digest and its predecessor on
`record_revision`. `record_revision` has **no** `state_at_origin` / `acceptance_ref` column, so the
payload is the shipped home for that pair, exactly as the generation-1 aggregates carry theirs; and it
**does** have `predecessor_revision_id`, so lineage needs no table either. A table holding
per-revision state would *be* the second revision aggregate `KS-R19@v1` requirement 1.1 forbids.

## Code Commentary

### Logic

- **One write entry point, one lock, one transaction.** `record_requirement_revision` (89-110) runs
  `store.exclusive_candidate_lock` at 99 and `store.within_immediate` at 102-110. Everything inside
  the transaction refuses by **raising `KnowledgeRefused`**, so the whole transaction rolls back: no
  record row, no revision row and no lineage edge survives a refused write.
- The order is deliberate. Scope (`unauthorized_scope`) and governing-route existence
  (`missing_expected_row`) are checked **before** the lock (94-98), so a request that can never be
  admitted does not contend for the candidate lock at all; a lock that cannot be taken returns the
  shipped lock refusals as a receipt (`mcp/src/agents_remember/memory/knowledge/store.py:510-526`), still before any write.
- `_write_revision` (113-159) is the transactional body: the guards run first (122-127), then the
  `knowledge_record` insert (128-140), then the `record_revision` insert (141-153). Payload
  admissibility is delegated once, at 162-174, to `validate_record_payload` — this module never
  validates a payload itself.
- `read_requirement_revisions` (177-205) reads the record and its revisions and answers through
  `requirement_views.revision_scope`; a record nothing stores is `missing_expected_row` with the
  table named, not an empty page.
- `resolve_requirement_reference` (208-262) answers requirement 2.6 in this record group's own terms:
  `resolved` names exactly one record, `unresolved` names none, `ambiguous` names more than one. A
  reference that two records hold is **reported as ambiguous rather than won** by either.
- The five guards are named for the fact each one carries, not for a code:
  `require_promotion_not_attempted` (269-321), `require_acyclic_lineage` (324-362),
  `require_predecessor` (365-399), `require_record_route_unchanged` (402-432),
  `require_governing_route` (435-446).

### Conventions

- **Refusals are one per distinct fact, and all of them are shipped codes.** Re-recording a stored
  `revision_id` so it would read `accepted` where it read `proposed` is `promotion_not_supported`, with
  `expected="proposed"`, `observed="accepted"` and a `next_action` that names the owner; any other
  re-use of a stored revision identity is `duplicate_identity`. A cycle is `lineage_cycle`, a
  predecessor stored elsewhere is `invalid_reference`, a predecessor stored nowhere is
  `missing_expected_row`, and a later revision declaring a different governing route for the same
  record is `immutable_revision`. **No new `KnowledgeRefusalCode` member was added by this leaf**:
  every refusal here is a shipped code.
- Acyclicity is **not** re-implemented. `require_acyclic_lineage` composes the shared
  `lineage.find_cycle` over the stored edges plus this edge, so this record group's lineage graph is
  judged by the same rule as the two lineage graphs the package already has.
- The governing route is **authored once per record**: `None` is the explicit ungoverned state rather
  than a default, a named route must already exist, and a later revision that names a *different* route
  is refused rather than silently ignored — ignoring it would report the record as governed by a route
  the caller did not name.
- `RECORD_OPERATION` / `READ_OPERATION` (85-86) name this record group's two operations once; the
  narrow `RequirementRevisionOperation` literal in `mcp/src/agents_remember/models/knowledge/requirement.py:383-386` is
  asserted to be a subset of `KnowledgeOperation` rather than a second vocabulary.

### Invariants And Boundaries

- **An acceptance is recorded, never produced.** `accepted` is storable — requirement 4.3's whole
  subject is that a stored `accepted` revision *records* an acceptance the owner made — and the write
  path enforces the shipped consistency rule at construction while leaving the envelope's storage
  lifecycle at `proposed`. "No promotion" is enforced by there being **no update path at all**.
- **Nothing here reads as task state.** No returned value carries a task status, a seat owner or a
  lifecycle gate; the owner's consumed resolution travels as payload data and the derived currentness
  reports it as a fact about the stored revision.
- **Reference, never replacement.** The record group stores the owner's three components as data and
  reads them back unchanged; the substrate never derives an identity from the packet's bytes, which is
  what makes a second requirement authority unconstructible rather than merely forbidden.
- **Boundary.** This module does not own the payload vocabulary (`models/knowledge/requirement.py`),
  the row codecs (`requirement_records.py`), the derived views (`requirement_views.py`), the
  task-plane boundary (`requirement_owner.py`), the envelope seam (`record_envelope.py`), the
  envelope's columns (`schema_v2.py`) or the candidate's batch boundary (`candidate.py`).
- **Known reachability gap, recorded rather than implied.** No production module imports this module:
  there is no MCP tool and no serving route for the record group yet, so both operations are reachable
  today only through the module's Python API.

### Todos

None recorded. The two new test modules in `mcp/tests/` are the only callers.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- **The one write entry point, its pre-lock checks and its one immediate transaction.** [1]
- **The transactional body: every guard before either INSERT, so a refusal leaves no row behind.** [2]
- The single payload seam this record group validates through, delegated to rather than restated. [3]
- The read that answers through the derived views and refuses a record nothing stores. [4]
- Requirement 2.6 answered here: resolved names exactly one record, ambiguous names more than one, and neither is won by the substrate. [5]
- Promotion refused as an attempt on a stored revision, with the owner named as the next action. [6]
- **The shared acyclic-lineage rule this record group composes instead of re-implementing.** [7]
- The shared rule itself, decided over the stored predecessor edges plus the new edge. [8]
- A predecessor stored under another record and a predecessor stored nowhere, refused as different facts. [9]
- **The governing route authored once: a later revision cannot repoint the record's sealed association.** [10]
- The pre-lock route check, with the ungoverned state never refused. [11]
- The two operation names this record group declares once, one per operation. [12]
- The read operation name, declared beside the record operation rather than inside the write path. [13]
- The narrow local literal, asserted by the suite to be a subset of the shipped vocabulary rather than a second one. [14]
- The shipped lock and one-immediate-transaction contract whose rollback this module relies on. [15]
- The envelope tables these operations write into, and the immutable-revision trigger behind them. [16]
- **The one-payload-seam entry point this record group calls, with its three refusal paths and one code.** [17]
- The lineage, promotion, reference and namespace cases that pin this module's refusals one by one. [18]
- The route cases: ungoverned as a state, and a sealed association that cannot be repointed. [19]
- The reference-resolution case: unresolved, then resolved to exactly one, then ambiguous over two holders. [20]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
