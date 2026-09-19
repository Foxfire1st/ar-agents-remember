# mcp/src/agents_remember/models/lifecycles/review_assessment_store.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/lifecycles/review_assessment_store.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T04:20+02:00 |
| lastVerifiedCommitHash | `65e3791bce458eb6265f752889435a1bcaac5f2e` |
| lastVerifiedCommitDate | 2026-09-18T06:16:59+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l15` uncommitted source; base `e963a01c6804570d597e451eaa069eaba66bd3ec` |
| governingOverview | `overview.md` |

## Governing Overview

[lifecycles overview](overview.md)

## Purpose

**Building, checking and reading the curator-coherence authority's typed assessment collection.**
This module owns the collection itself — the typed family/invariant assessment set that lives on the
*existing* curator-coherence authority — while leaving that authority's source-candidate exact-
coverage obligation untouched and in its own module.

Everything here is a refusal rather than a convention: authorship is taken from the publication path
and never from a caller's submission text; the binding is the exact examined inputs and nothing
decides that a moved input is equivalent; and persisting endorses nothing, because no function reads a
disposition to decide an outcome.

## Code Commentary

### Logic

`AssessmentInputs` carries the exact inputs one assessment examined **as the publication path already
observed them**, so an assessment's binding and the coherence record's binding are two statements
about the same candidate rather than two statements that happen to agree. `scopeManifestRef` is a
recorded fact passed in by the caller and never derived from a name or a path, because route scope is
a recorded scope rather than an inference.

`examined_input_declaration` turns those inputs into an `ar-evidence-dependencies/v1` declaration
under the `review-assessment/v1` policy — the shipped contract rather than a second one — with the
kinds that policy requires: the candidate pair, the code tree, the registered scope, the requirement
identities, the scope manifest and comparison references, the two validator versions, and one
`evidence-bytes` edge per recorded byte so each cited byte's path and digest travel together. The
memory tree edge is added only when the pair has one.

`bind_assessment` stamps the authenticated author and role onto the record and attaches the
declaration. `require_assessments_are_identified` refuses a submitted collection whose assessments are
not individually identified. `assessment_currentness_for_record` and `require_current_assessments` are
the collection-level currentness reads, and `review_record_edges` declares the coherence record's own
edge per stored assessment — `assessment_edge_name` spells that edge — which is what lets a reader
resolve an assessment from the coherence record without parsing a payload. The record cites the
assessment; the assessment never cites the record, which is what keeps the binding out of the
self-invalidating sequence.

`reviewed_bytes` reads the bytes a record's citations name through the shipped evidence resolver.

### Conventions

- `ReviewAssessmentError` carries a status, a detail and a next action, so a refusal is rendered the
  same way every other application-boundary error is.
- The `review-assessment/v1` policy is the required-kind set from `KS-R15@v1` §5.1; the leaf added
  the policy entry and one optional permission on `curator-coherence/v1` (the `review-record` edge),
  and no dependency kind.
- `PublishedEvidenceByte` is a protocol, so the publication path's own value satisfies it without a
  second type being minted here.

### Invariants And Boundaries

- **No caller-supplied authority.** No function here accepts an author from submission text, because
  the submission shape has no such field to accept.
- **Exact-coverage is untouched.** `_judgments_cover_candidates_exactly` stays in the model module and
  is not read, relaxed or re-derived here; the assessment collection sits beside `judgments` with its
  own uniqueness validator.
- **Persisting endorses nothing.** The collection cannot advance, gate or approve anything.
- **The assessed database is not this record's home.** The record persists through the coherence
  authority; no knowledge-store table, column or payload was added for it.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The exact inputs one assessment examined, every field an identity the coherence observation already captured. | `AssessmentInputs` | mcp/src/agents_remember/models/lifecycles/review_assessment_store.py:87-108 |
| The declaration builder and the required-kind policy it validates against. | `examined_input_declaration` | mcp/src/agents_remember/models/lifecycles/review_assessment_store.py:111-157 |
| The persistence entry that stamps the authenticated author and role. | `bind_assessment` | mcp/src/agents_remember/models/lifecycles/review_assessment_store.py:159-196 |
| The collection-level currentness reads and the identification refusal. | `require_assessments_are_identified`; `assessment_currentness_for_record`; `require_current_assessments` | mcp/src/agents_remember/models/lifecycles/review_assessment_store.py:197-214; mcp/src/agents_remember/models/lifecycles/review_assessment_store.py:215-230; mcp/src/agents_remember/models/lifecycles/review_assessment_store.py:231-252 |
| The record's own edge per stored assessment, and the edge-name spelling a reader resolves. | `review_record_edges`; `assessment_edge_name` | mcp/src/agents_remember/models/lifecycles/review_assessment_store.py:287-309; mcp/src/agents_remember/models/lifecycles/review_assessment_store.py:310-327 |
| The evidence-dependency contract and policy registry this module declares against. | `build_evidence_dependencies`; `dependency`; `canonical_sha256` | mcp/src/agents_remember/models/lifecycles/evidence_dependencies.py:243-252; mcp/src/agents_remember/models/lifecycles/evidence_dependencies.py:255-302; mcp/src/agents_remember/models/lifecycles/evidence_dependencies.py:354-358 |

## KS-R15@v1 Assessment Collection

**The leaf that created this module.** `KS-R15@v1` §8.1 makes the leaf the owner of the typed
collection, §5.1 requires identities rather than descriptions with the shipped contract's own
vocabularies, and §6.1/§6.3 require the record to travel through the existing canonical route outside
the assessed database.

Delivery note carried here so a later reader does not have to re-derive it: the declaration a
validator re-checks is the same one a reader resolves the evidence bytes through, which is why the
`evidence-bytes` edges are derived from the recorded bytes rather than from the citations.

## Update History

- 2026-09-18T06:05+02:00 — 260915-KS-L15 curator (uncommitted change set on `ar/260915-ks-l15`, base
  `e963a01c`): created this card for the assessment-collection module the leaf added — the exact
  examined-input declaration under the new `review-assessment/v1` policy, the authenticated-authorship
  stamp, the collection-level currentness reads, the record-side `review-record` edge that keeps the
  binding out of the self-invalidating sequence, and the boundaries that exact coverage stays in the
  model module and persisting endorses nothing. Verification metadata remains closeout-owned; no
  acceptance or certification claim is made.
