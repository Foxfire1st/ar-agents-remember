# mcp/src/agents_remember/memory/knowledge/requirements.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/requirements.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T06:10+02:00 |
| lastVerifiedCommitHash | `b5a74aee6cdf671c9963f3aba4df6d44b856f697` |
| lastVerifiedCommitDate | 2026-09-18T09:42:44+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l19` uncommitted source; base `e963a01c6804570d597e451eaa069eaba66bd3ec` |
| governingOverview | `mcp/src/agents_remember/memory/overview.md` |

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

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
|**The one write entry point, its pre-lock checks and its one immediate transaction.**|`record_requirement_revision`| mcp/src/agents_remember/memory/knowledge/requirements.py:89-112 |
|**The transactional body: every guard before either INSERT, so a refusal leaves no row behind.**|`_write_revision`| mcp/src/agents_remember/memory/knowledge/requirements.py:113-161 |
|The single payload seam this record group validates through, delegated to rather than restated.|`_admissible_payload`| mcp/src/agents_remember/memory/knowledge/requirements.py:162-176 |
|The read that answers through the derived views and refuses a record nothing stores.|`read_requirement_revisions`| mcp/src/agents_remember/memory/knowledge/requirements.py:177-207 |
| Requirement 2.6 answered here: resolved names exactly one record, ambiguous names more than one, and neither is won by the substrate. | `resolve_requirement_reference` | mcp/src/agents_remember/memory/knowledge/requirements.py:208-268 |
| Promotion refused as an attempt on a stored revision, with the owner named as the next action. | `require_promotion_not_attempted` | mcp/src/agents_remember/memory/knowledge/requirements.py:269-323 |
| **The shared acyclic-lineage rule this record group composes instead of re-implementing.** | `require_acyclic_lineage` | mcp/src/agents_remember/memory/knowledge/requirements.py:324-364 |
| The shared rule itself, decided over the stored predecessor edges plus the new edge. | "def find_cycle(" | mcp/src/agents_remember/memory/knowledge/lineage.py:133-159 |
| A predecessor stored under another record and a predecessor stored nowhere, refused as different facts. | `require_predecessor` | mcp/src/agents_remember/memory/knowledge/requirements.py:365-401 |
| **The governing route authored once: a later revision cannot repoint the record's sealed association.** | `require_record_route_unchanged` | mcp/src/agents_remember/memory/knowledge/requirements.py:402-434 |
| The pre-lock route check, with the ungoverned state never refused. | `require_governing_route` | mcp/src/agents_remember/memory/knowledge/requirements.py:435-453 |
| The two operation names this record group declares once, one per operation. | `RECORD_OPERATION` | mcp/src/agents_remember/memory/knowledge/requirements.py:85-85 |
| The read operation name, declared beside the record operation rather than inside the write path. | `READ_OPERATION` | mcp/src/agents_remember/memory/knowledge/requirements.py:86-86 |
| The narrow local literal, asserted by the suite to be a subset of the shipped vocabulary rather than a second one. | `RequirementRevisionOperation` | mcp/src/agents_remember/models/knowledge/requirement.py:383-386 |
| The shipped lock and one-immediate-transaction contract whose rollback this module relies on. | `exclusive_candidate_lock`; `within_immediate` | mcp/src/agents_remember/memory/knowledge/store.py:467-526 |
| The envelope tables these operations write into, and the immutable-revision trigger behind them. | `record_revision_no_rewrite` | mcp/src/agents_remember/memory/knowledge/schema_v2.py:223-224 |
|**The one-payload-seam entry point this record group calls, with its three refusal paths and one code.**|`validate_record_payload`| mcp/src/agents_remember/memory/knowledge/record_envelope.py:202-246 |
| The lineage, promotion, reference and namespace cases that pin this module's refusals one by one. | "test_a_promotion_attempt_is_refused_and_no_stored_byte_changes"; "test_a_self_predecessor_is_refused_as_a_cycle_and_writes_nothing"; "test_a_dangling_predecessor_is_refused"; "test_a_request_addressed_to_another_namespace_is_refused" | mcp/tests/test_knowledge_requirement_revisions.py:247-276; mcp/tests/test_knowledge_requirement_revisions.py:403-425; mcp/tests/test_knowledge_requirement_revisions.py:448-461; mcp/tests/test_knowledge_requirement_revisions.py:529-547 |
| The route cases: ungoverned as a state, and a sealed association that cannot be repointed. | "test_ungoverned_is_reported_as_a_state_and_never_defaulted"; "test_a_named_route_must_be_authored_and_is_never_repointed" | mcp/tests/test_knowledge_requirement_reference_contract.py:366-383; mcp/tests/test_knowledge_requirement_reference_contract.py:384-434 |
| The reference-resolution case: unresolved, then resolved to exactly one, then ambiguous over two holders. | "test_a_reference_from_another_record_group_resolves_to_this_record_group" | mcp/tests/test_knowledge_requirement_reference_contract.py:528-568 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T07:21:19+00:00: Generated citation repair: `validate_record_payload` repointed to mcp/src/agents_remember/memory/knowledge/record_envelope.py:202-246. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T04:10:00+00:00 — 260915-KS-L19 curator (uncommitted change set on `ar/260915-ks-l19`, base `e963a01c`): created this one-to-one card for the requirement record group's operation surface. It records the four facts a future agent would otherwise have to re-measure: the record group **adds no table and declares no schema generation**, because the delivered envelope already carries every needed fact and a per-revision state table would be the second revision aggregate `KS-R19@v1` requirement 1.1 forbids; the order of the write path (scope and route before the lock, everything else inside the one immediate transaction, so a refused write leaves no row, no revision and no edge); that **no new refusal member was added** — every code this module issues is shipped, with one distinct fact per code; and that acyclicity is **composed from the shared `lineage.find_cycle`** rather than re-implemented, so this record group's lineage graph is judged by the same rule as the package's two older graphs. It also records two boundaries a reader is likely to misread: `accepted` is **storable** and the substrate still never produces an approval (there is no update path at all, so a promotion attempt is `promotion_not_supported`), and the governing route is authored once per record with a later repoint refused as `immutable_revision` rather than silently ignored. The standing reachability gap is recorded rather than implied: no production module imports this record group yet. Verification metadata advances to the leaf's base commit `e963a01c` because the body was read against the current source; the code commit does not exist yet and closeout owns that stamp.
