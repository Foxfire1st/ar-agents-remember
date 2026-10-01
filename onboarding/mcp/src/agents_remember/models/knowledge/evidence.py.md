# mcp/src/agents_remember/models/knowledge/evidence.py

## Governing Overview

[models route overview](../overview.md)

## Purpose

The supporting-record vocabulary: `EvidenceClaimPayload` and `VerificationObservationPayload`, the two
typed subject kinds and the two claimed-coverage endpoints, the closed execution-result vocabulary, the
artifact and publication references, the run environment, and the two commands this leaf appends to the
closed command union.

## Code Commentary

### Logic

Two record kinds and not one "evidence" table, and the separation is the reason the leaf exists. An
evidence claim records an authored assertion about what evidence *covers*; a verification observation
records a mechanical fact about what *ran*. Collapsing them would put a human's coverage assertion in the
same row as a machine's exit status, and the first consumer to read the row would reasonably treat the
whole row as machine-produced. The separation is also what makes the no-sufficiency rule enforceable: if a
passing run lives in a different record from the claim, there is no single row in which "passed" could be
read as "sufficient".

Both payloads are declared under the shipped `KnowledgeModel` base — `extra="forbid"`, frozen — so a field
that is not declared has nowhere to be stored, and neither model has a field for a verdict, a confidence,
a severity, an endorsement or an aggregate. `limitations` is required on a claim and defaults to the empty
string, never `None`: an author declaring no limitations is a recorded fact, not an unstated one.

The subject is a discriminated union of exactly two kinds, `InvariantRevisionSubject` and
`KnowledgeFacetRevisionSubject`, and the discrimination is structural rather than nominal: each kind names
its own join table and its own revision column through `subject_table` and `subject_revision_id`, so the
kind a payload declares is the table its row reaches. The claimed coverage has the same shape —
`RealizationClaimCoverage` and `AnchorCoverage` — and `claimed_coverage_row_identity` is what makes a
duplicate endpoint unrepresentable at construction as well as in the key.

`ResultArtifactReference` is a reference, never the bytes: a confined repository-relative POSIX path, the
sha256 of the artifact's bytes, and the byte size. `PublicationReference` is the sibling for the
interpretable manifest, naming a durable destination, the sha256 of the published bytes and the recorded
instant; its presence or absence is how the record states which retention route it relies on.

`EXECUTION_RESULTS` is the closed five-member vocabulary `passed`, `failed`, `error`, `skipped` and
`not_run`, with `not_run` a member and reported as itself. **No member says what the result means.** The
tuple is also the source the generation's DDL `CHECK` is compared against.

`RunEnvironment` records the run's own toolchain at write time, bounded, so nothing is re-derived from the
reading machine later. `AddEvidenceClaim` and `AddVerificationObservation` are the two authored commands
this leaf appends to `ProposedCommand`, and `EVIDENCE_WRITABLE_TABLES` is the five-table set they may
write.

### Conventions

A vocabulary module declares the typed shape and the closed sets; the write path resolves links and the row
codecs convert. Frozen and extra-forbidden is the default for every payload, so an undeclared field is a
shape error rather than stored data.

### Invariants And Boundaries

- **No semantic conclusion anywhere.** Nothing in either payload asks or answers whether evidence is
  adequate, sufficient, convincing or relevant; nothing grades, ranks, scores or summarises. The absence is
  structural — there is no field for a well-meaning writer to fill in.
- **No second identity authority.** Neither record carries a content address, a logical digest or a
  fingerprint of its own. A revision's seal is `record_revision.content_digest`; the one digest here is the
  sha256 of an external artifact's bytes.
- **The artifact reference never becomes a content store.** There is no bytes column and no BLOB in the
  vocabulary or in generation 7, and the confinement validator refuses an absolute, drive, UNC, backslash,
  NUL, `..` or pathspec spelling.
- **Assessment references are explicit and opaque.** `ReviewAssessment` belongs to a later leaf, so
  `assessment_refs` is present, typed, bounded and never defaulted, dropped or synthesised here; a claim
  with none is served as unassessed rather than as compatible.
- **Evidence results are facts, not verdicts.** `passed` and `failed` are equally facts; nothing in this
  module converts either into a finding, a gate or a lifecycle change.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The two record kinds' kind and schema names, and the one lifecycle value both store. [1]
- The two claimed-coverage endpoints, the union that discriminates them, and the row identity that makes a duplicate endpoint unrepresentable. [2]
- The two subject kinds, each naming its own table and revision column, so the declared kind is the table the row reaches. [3]
- The artifact reference: a confined path, the bytes' sha256 and size — a reference, never a content store. [4]
- The publication reference whose presence states which retention route the record relies on. [5]
- The closed five-member execution vocabulary, with `not_run` a member and no sufficiency member. [6]
- The run's own toolchain, recorded at write time and bounded. [7]
- The claim aggregate: subject, anchor, coverage, explanation, required limitations, assessment references. [8]
- The observation aggregate: recorded candidate, command identity, artifact, execution result, environment, publication. [9]
- The two appended authored commands and the tables they may write. [10]
- The case that asserts the payloads are frozen, extra-forbidden and never default the limitations value. [11]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
