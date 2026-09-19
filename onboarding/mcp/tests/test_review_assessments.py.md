# mcp/tests/test_review_assessments.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_review_assessments.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T04:20+02:00 |
| lastVerifiedCommitHash | `7879f5b22c34a912f939e27868786818463c3b9c` |
| lastVerifiedCommitDate | 2026-09-19T20:18:09+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l15` uncommitted source; base `e963a01c6804570d597e451eaa069eaba66bd3ec` |
| governingOverview | `overview.md` |

## Governing Overview

[tests overview](overview.md)

## Purpose

**The unit population for `KS-R15@v1`'s `ReviewAssessment` record, its binding, and the states a read
reports.** These cases protect the record's *decidable* content: which fields a stored assessment must
carry, that its three dispositions are not interchangeable, that its binding is compared for equality
rather than reinterpreted, that absence is never rendered as a favourable disposition, and that the
`knowledgeReview` checklist section is a factual, report-only section of the one artifact.

Nothing here fakes a contract or a store, and no case claims a survival it did not read back. The
publication route's real behaviour — the authenticated caller, the evidence-byte destination and the
post-cleanup read-back — is exercised against a real external-memory leaf enclosure in
`mcp/tests/test_curator_review_assessment_publication.py`; this module is the hermetic half.

## Code Commentary

### Logic

Seven test classes, each owning one property rather than one function:

- `TestAssessmentRecordShape` — a record missing its examined inputs or its provenance does not
  construct; the submission shape has no field for a caller-supplied author; an undeclared field is
  refused; the record is validated structurally and never for truth.
- `TestDispositionVocabulary` — the vocabulary is exactly the three declared values; `unresolved` is
  not a synonym for `no_concern_found`; `no_concern_found` may not carry a finding; an unknown
  disposition is refused.
- `TestSubjectShape` — a family subject names the family's own record and its revisions; the revision
  lists are required for a revision-bearing kind and refused for `comparison`.
- `TestExaminedInputBinding` — the binding uses the shipped contract's two own vocabularies; the policy
  requires exactly the clause-five inputs; a relocated input with identical content is **not**
  equivalent; an input that can no longer be read is a mismatch rather than a pass; a moved input
  marks the binding stale with its exact identity; per-item coverage is not inherited from a sibling.
- `TestEvidenceBytesAreRecordedAsThreeFacts` — each cited byte is recorded with path, digest and size.
- `TestReadStates` — the three recorded states plus `none-recorded` are reported distinctly; a
  projection cannot report a disposition for an absent subject; a count that contradicts its records
  is refused.
- `TestKnowledgeReviewSection` — the section moves no count and adds no finding; it is written into the
  one checklist artifact; an unresolved signal is reported as its own state rather than a clearance.

`_Binding` at the top is the module's own small builder for a well-formed assessment, so each case
varies exactly the field it is about instead of restating the whole record; `_Published` at the bottom
serves the cases that need a stored projection.

### Conventions

- Registered in `mcp/tests/test-evidence-lanes.toml` as a **unit-regression** member: every case is
  hermetic (temporary directories, in-process state, no integration marker, no repository or
  subprocess), so the default unit lane is each one's behaviour-preserving classification.
- Each case names a distinct failure in the leaf's clause envelope; none is a variant of another, and
  no case asserts the *absence* of an operation, which would be a source census rather than a
  behavioural check.

### Invariants And Boundaries

- **No case here claims a survival it did not read back** — that property belongs to the integration
  module, which drives the real publication path.
- **No fake contract and no fake store.** The module builds records and projections in process; it
  never stands up an enclosure.
- **Structural claims only.** A case asserts that a shape is refused or that a state is reported; no
  case asserts that a finding is true.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The lane row this module's classification rests on, and the lane header that declares the classification. | "mcp/tests/test_review_assessments.py"; "unit-regression = [" | mcp/tests/test-evidence-lanes.toml:160-192; mcp/tests/test-evidence-lanes.toml:5-5; mcp/tests/test-evidence-lanes.toml:192-192; mcp/tests/test-evidence-lanes.toml:175-192 |
| The record, its submission shape and the validator the shape cases drive. | `ReviewAssessment`; `ReviewAssessmentRevision`; `_AuthoredAssessmentFields` | mcp/src/agents_remember/models/lifecycles/review_assessment.py:261-324; mcp/src/agents_remember/models/lifecycles/review_assessment.py:326-341; mcp/src/agents_remember/models/lifecycles/review_assessment.py:343-365 |
| The equality comparison and the stale-marking the binding cases drive. | `disputed_dependencies`; `AssessmentCurrentness`; `require_current_assessment_binding` | mcp/src/agents_remember/models/lifecycles/review_assessment_binding.py:92-107; mcp/src/agents_remember/models/lifecycles/review_assessment_binding.py:110-140; mcp/src/agents_remember/models/lifecycles/review_assessment_binding.py:162-188 |
| The state projection the read cases drive. | `assessment_state_for`; `SubjectAssessmentState` | mcp/src/agents_remember/models/lifecycles/review_assessment.py:416-439; mcp/src/agents_remember/models/lifecycles/review_assessment.py:441-501 |
| The report-only section the checklist cases assert. | `knowledge_review_section` | mcp/src/agents_remember/memory_quality/knowledge_review.py:70-135 |

## KS-R15@v1 Unit Protection

**The leaf that created this module.** `KS-R15@v1` §1–§5 and §8.2 are the clauses these 47 cases
carry. The leaf's case-budget measurement records this module alone as `47 tests collected`, and the
combined population delta as `+47 unit` against the base `e963a01c`.

Two clauses are deliberately **not** carried by a case here, and the leaf recorded why rather than
leaving the gap silent: §3.2's "a citation keeps both types" is a structural property (there is no
function taking a signal and returning an assessment), and asserting the absence of an operation
would be a source census rather than a behavioural check; and §6.9's scope refusal is the shipped,
unmodified `_require_leaf_external_memory`, so a case would assert a rail this leaf did not touch.

## Update History

- 2026-09-18T06:05+02:00 — 260915-KS-L15 curator (uncommitted change set on `ar/260915-ks-l15`, base
  `e963a01c`): created this card for the leaf's unit module — the seven properties it protects, its
  hermetic classification and lane registration, and the two clauses the leaf recorded as
  structural-or-shipped rather than case-carried. Verification metadata remains closeout-owned; no
  acceptance or certification claim is made.
