# mcp/tests/test_review_assessments.py

## Governing Overview

[tests overview](overview.md)

## Purpose

**The unit population for `KS-R15@v1`'s `ReviewAssessment` record, its binding, and the states a read
reports.** These cases protect the record's *decidable* content: which fields a stored assessment must
carry, that its three dispositions are not interchangeable, that its binding is compared for equality
rather than reinterpreted, that absence is never rendered as a favourable disposition, and that the
`knowledgeReview` checklist section is a factual, report-only section of the one artifact.

Nothing here fakes a contract or a store, and no case claims a survival it did not read back. The
integration fixture in `mcp/tests/test_curator_review_assessment_publication.py` uses a real
external-memory leaf enclosure to verify authenticated authorship, the evidence-byte destination and
read-back after the fixture removes the enclosure reports directory.

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
  requires exactly the clause-five inputs; a different candidate Git tree identity marks the binding stale; a missing observation records an unreadable-or-absent gap. The moved-input case asserts the exact disputed identity and both tree IDs.
- `TestEvidenceBytesAreRecordedAsThreeFacts` supplies path, digest and size to the evidence-byte
  fixture and checks that the binding identity records the path and digest. It also checks refusal
  of missing or uncited published bytes and invalid paths.
- `TestReadStates` checks four per-assessment binding states and six subject-summary states,
  including `none-recorded`. It rejects inconsistent counts and statuses and checks that a sibling’s
  measurement leaves an uncovered assessment `not-measured`.
- `TestKnowledgeReviewSection` checks that the unresolved row appears in the report, that the
  report and attestation are the only two files emitted, and that an unresolved row leaves the
  case’s readiness status and actionable count unchanged.

`_Binding` supplies the overrides that `_bound` passes to the assessment builder. `_Published`
pairs one citation with one supplied evidence-byte object for the citation-matching cases.

### Conventions

- Every case uses temporary directories and in-process state. The cases require no integration marker, repository or subprocess.
- The behavioral cases check model inputs, state projections, binding identities, and checklist output.

### Invariants And Boundaries

- The module builds records and projections in process. Checklist cases write and reopen
  temporary report and attestation files.
- Model checks establish shape and state behavior. A stored finding remains the authored claim.

## Evidence

### Repo-Internal References

- The record, its submission shape and the validator the shape cases drive. [2]

- The equality comparison and the stale-marking the binding cases drive. [3]

- The state projection the read cases drive. [4]



- The checklist cases check the report-only assessment row and the unchanged readiness status and actionable count. [5]




## KS-R15@v1 Unit Protection

The following complete passages are retained from the earlier card at memory snapshot `81cfe4a8`. They are the recorded 260915-KS-L15 account: its rationale, historical source coordinates, prior measurements and deliberate omissions. Prior run outcomes remain attributed to that account; this curation adds no execution result. Historical reference labels below are custody text and do not select current sidecar anchors.

The 47-collected and +47 measurements below belong to the creating leaf. The current frozen source has 52 statically counted test definitions; no collection was run for this restoration. The explicit removed-helper qualification in the omission account remains.

**The leaf that created this module.** `KS-R15@v1` §1–§5 and §8.2 are the clauses these 47 cases
carry. The leaf's case-budget measurement records this module alone as `47 tests collected`, and the
combined population delta as `+47 unit` against the base `e963a01c`.

Two clauses are deliberately **not** carried by a case here, and the leaf recorded why rather than
leaving the gap silent: §3.2's "a citation keeps both types" is a structural property (there is no
function taking a signal and returning an assessment), and asserting the absence of an operation
would be a source census rather than a behavioural check; and the leaf recorded §6.9's scope refusal as a pre-existing `_require_leaf_external_memory` rail that its patch did not touch. That is the historical omission rationale, not a current source address for the removed helper.


- The archived KS-R15@v1 packet preserves the creating leaf’s distinct-type requirement, former external-memory scope rail and report-only checklist boundary (§3.2, §6.9 and §8.2). This document supports the historical omission rationale, not a current implementation claim. \[6] [6]

- The `unit-regression` lane selects `mcp/tests/test_review_assessments.py`. [1]
