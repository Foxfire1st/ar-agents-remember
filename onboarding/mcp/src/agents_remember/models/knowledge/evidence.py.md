# mcp/src/agents_remember/models/knowledge/evidence.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/knowledge/evidence.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T06:20+02:00 |
| lastVerifiedCommitHash |  `b5a74aee6cdf671c9963f3aba4df6d44b856f697`|
| lastVerifiedCommitDate |  2026-09-18T09:42:44+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l12` uncommitted source; base `e963a01c6804570d597e451eaa069eaba66bd3ec` |
| governingOverview | `mcp/src/agents_remember/models/overview.md` |

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

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The two record kinds' kind and schema names, and the one lifecycle value both store. | `EVIDENCE_CLAIM_KIND`; `EVIDENCE_CLAIM_SCHEMA`; `VERIFICATION_OBSERVATION_KIND`; `VERIFICATION_OBSERVATION_SCHEMA`; `EVIDENCE_RECORD_LIFECYCLE` | mcp/src/agents_remember/models/knowledge/evidence.py:75-75; mcp/src/agents_remember/models/knowledge/evidence.py:76-76; mcp/src/agents_remember/models/knowledge/evidence.py:78-78; mcp/src/agents_remember/models/knowledge/evidence.py:79-79; mcp/src/agents_remember/models/knowledge/evidence.py:83-83 |
| The two claimed-coverage endpoints, the union that discriminates them, and the row identity that makes a duplicate endpoint unrepresentable. | `RealizationClaimCoverage`; `AnchorCoverage`; `CoverageEndpoint`; `claimed_coverage_row_identity` | mcp/src/agents_remember/models/knowledge/evidence.py:97-101; mcp/src/agents_remember/models/knowledge/evidence.py:104-108; mcp/src/agents_remember/models/knowledge/evidence.py:114-116; mcp/src/agents_remember/models/knowledge/evidence.py:658-666 |
| The two subject kinds, each naming its own table and revision column, so the declared kind is the table the row reaches. | `InvariantRevisionSubject`; `KnowledgeFacetRevisionSubject`; `subject_table`; `subject_revision_id` | mcp/src/agents_remember/models/knowledge/evidence.py:131-135; mcp/src/agents_remember/models/knowledge/evidence.py:138-149; mcp/src/agents_remember/models/knowledge/evidence.py:173-178; mcp/src/agents_remember/models/knowledge/evidence.py:167-170 |
| The artifact reference: a confined path, the bytes' sha256 and size — a reference, never a content store. | `ResultArtifactReference` | mcp/src/agents_remember/models/knowledge/evidence.py:185-223 |
| The publication reference whose presence states which retention route the record relies on. | `PublicationReference` | mcp/src/agents_remember/models/knowledge/evidence.py:236-270 |
| The closed five-member execution vocabulary, with `not_run` a member and no sufficiency member. | `EXECUTION_RESULTS` | mcp/src/agents_remember/models/knowledge/evidence.py:295-300 |
| The run's own toolchain, recorded at write time and bounded. | `RunEnvironment` | mcp/src/agents_remember/models/knowledge/evidence.py:314-352 |
| The claim aggregate: subject, anchor, coverage, explanation, required limitations, assessment references. | `EvidenceClaimPayload` | mcp/src/agents_remember/models/knowledge/evidence.py:359-412 |
| The observation aggregate: recorded candidate, command identity, artifact, execution result, environment, publication. | `VerificationObservationPayload` | mcp/src/agents_remember/models/knowledge/evidence.py:415-468 |
| The two appended authored commands and the tables they may write. | `AddEvidenceClaim`; `AddVerificationObservation`; `EVIDENCE_WRITABLE_TABLES` | mcp/src/agents_remember/models/knowledge/evidence.py:481-530; mcp/src/agents_remember/models/knowledge/evidence.py:533-548; mcp/src/agents_remember/models/knowledge/evidence.py:569-576 |
| The case that asserts the payloads are frozen, extra-forbidden and never default the limitations value. | "def test_the_claim_payload_is_frozen_extra_forbidden_and_never_defaults_limitations(" | mcp/tests/test_knowledge_evidence_claims.py:149-190 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T06:20+02:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): created this one-to-one card for the supporting-record vocabulary. It records the two-kind separation and why it exists, the structural subject discrimination, the closed execution vocabulary with no sufficiency member, the artifact reference that is never a content store, and the absence of any field that could carry a verdict. This card carries **no `lastVerifiedCommitHash`**: every construct it cites exists only in this leaf's uncommitted candidate, so no real commit contains the content a stamp would claim to have verified. Naming the base commit there would be a verification claim about a tree the code never had; the `reviewedWorkingCandidate` row states what was actually read, and closeout owns the stamp once the code commit exists.
