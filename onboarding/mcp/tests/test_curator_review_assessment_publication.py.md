# mcp/tests/test_curator_review_assessment_publication.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_curator_review_assessment_publication.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T04:20+02:00 |
| lastVerifiedCommitHash | `15fe8678fc0f87eaac4606952f179135ebe392c4` |
| lastVerifiedCommitDate | 2026-09-18T07:49:45+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l15` uncommitted source; base `e963a01c6804570d597e451eaa069eaba66bd3ec` |
| governingOverview | `overview.md` |

## Governing Overview

[tests overview](overview.md)

## Purpose

**The integration population for `KS-R15@v1`'s publication route, the evidence-byte destination and
the read-back.** Every case drives the **production** curator-coherence publication against a real
external-memory leaf enclosure built by the shared lifecycle fixture. Nothing here re-implements the
publication path, fakes a contract, or asserts a survival it did not read back.

The load-bearing properties:

- the `knowledgeReview` surface's source — the record's own assessment collection — is written through
  the `curator_coherence` `publish` action and read back from the canonical authority on disk;
- each cited evidence byte is opened **by the task-root-relative path recorded on the assessment** and
  verified against its recorded digest, which is the read-back the requirement asks for and the
  record's own digest cannot substitute for;
- the survival read-back still resolves after the enclosure's `reports` directory — the one directory
  terminal cleanup removes for a leaf contract — is gone;
- the shipped exact-coverage obligation `_judgments_cover_candidates_exactly` is untouched by a record
  that carries assessments.

## Code Commentary

### Logic

Three test classes:

- `TestPublishedAssessment` — an assessment publishes to the canonical authority and reads back; the
  stored author is whatever the publication path supplied; each cited evidence byte is recorded with
  path, digest and size; the published copy is the cited bytes by content; a citation naming a
  worktree file is published to the surviving tree; the recorded bytes survive removal of the
  enclosure `reports` directory; publishing an assessment does not disturb the exact-coverage
  obligation; a leaf with no assessment publishes and reports `none-recorded`.
- `TestReadStatesOverAStoredCollection` — a measured move marks the stored assessment stale and keeps
  it readable; `unresolved` is reported as its own state rather than as a clearance.
- `TestAssessmentRefusals` — a submission supplying an author is refused as an undeclared field
  **through the application boundary**, so the code asserted is the code a caller receives; a byte
  that does not read back blocks with the destination and the digest; a published byte removed after
  publication is a blocked absent state; a refused submission leaves the canonical authority
  byte-identical.

The module also writes the canonical leaf document and its passing route review in a `_leaf_document`
fixture, because the coherence route resolves the terminal leaf document and a contract alone is not
enough. There is no `test_`-prefixed re-implementation of anything: the fixture builds real state for
the production path to drive.

### Conventions

- Registered in `mcp/tests/test-evidence-lanes.toml` as an **integration** member: it stands up real
  repositories and an external-memory enclosure, which is the population that measures that behaviour.
- Registered in `mcp/tests/evidence-lifecycle.toml` as a **consumer** of the shared support module
  `mcp/tests/curator_coherence_test_support.py` (owner `curator-coherence-test-port`) and of
  `mcp/tests/test_worktree_support.py`. This leaf added a consumer row; it did not add a contract or
  an artifact, so the catalogue's counts stay at 13 contracts / 54 artifacts while its digest moves.
- Refusal assertions are routed through the **application** boundary (`curator_coherence_tool`) rather
  than the domain function, so claimed codes are the codes a caller receives.

### Invariants And Boundaries

- **Survival is read back, never asserted.** The post-cleanup case removes the enclosure `reports`
  directory, asserts it is gone, and only then opens the recorded bytes.
- **The record's own digest is not the bytes' read-back.** Each byte is opened by the path recorded on
  the assessment and compared to the digest recorded beside it.
- **A refused publication leaves the authority byte-identical.** The refusal cases measure the
  canonical file rather than only the raised error.
- **Exact coverage is a preservation boundary.** The case asserts the shipped obligation still refuses
  a mismatched judgment set on a record that carries assessments.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The integration-lane row this module's classification rests on, and the lane header that declares the classification. | "mcp/tests/test_curator_review_assessment_publication.py"; "integration = [" | mcp/tests/test-evidence-lanes.toml:164-164; mcp/tests/test-evidence-lanes.toml:234-234 |
| The shared support module this module is registered as a consumer of. | "mcp/tests/test_curator_review_assessment_publication.py" | mcp/tests/evidence-lifecycle.toml:360-360 |
| The publication wiring the cases drive, including the exact-coverage obligation they leave untouched. | `curator_coherence_action`; `_exact_review_assessments`; `_record` | mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence_publication.py:88-98; mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence_publication.py:248-302; mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence_publication.py:352-451 |
| The destination and read-back the survival and blocked cases measure. | `publish_assessment_evidence_bytes`; `read_back_published_bytes`; `AssessmentEvidenceBlockedError` | mcp/src/agents_remember/worktrees/integration/closeout/curator_assessment_evidence.py:64-96; mcp/src/agents_remember/worktrees/integration/closeout/curator_assessment_evidence.py:152-193; mcp/src/agents_remember/worktrees/integration/closeout/curator_assessment_evidence.py:195-240 |
| The typed collection the publish action accepts and the uniqueness rule it enforces. | `CuratorCoherenceRecord`; `CuratorCoherenceRequest` | mcp/src/agents_remember/models/lifecycles/curator_coherence.py:190-234; mcp/src/agents_remember/models/lifecycles/curator_coherence.py:370-434 |

## KS-R15@v1 Integration Protection

**The leaf that created this module.** `KS-R15@v1` §6, §7 and §10.4 are the clauses these 18 cases
carry. The leaf's case-budget measurement records this module alone as `18 tests collected`, and the
combined population delta as `+18 integration` against the base `e963a01c`; both the unit and the
integration ceilings stay under their declared budgets, so this leaf raised neither.

The governed-inventory consequence, recorded here because a reader of this card is the person most
likely to ask: the module is ordinary `test_`-prefixed test source, so no artifact is promoted and no
new shared support module was written. The evidence-lifecycle catalogue's identity moved only because
a **consumer list** changed, and the catalogue guard validates that change in both directions.

## Update History

- 2026-09-18T06:05+02:00 — 260915-KS-L15 curator (uncommitted change set on `ar/260915-ks-l15`, base
  `e963a01c`): created this card for the leaf's integration module — the four load-bearing properties
  it measures against a real external-memory enclosure, its integration lane and shared-support
  consumer registrations, and the boundary that survival is read back after cleanup rather than
  asserted. Verification metadata remains closeout-owned; no acceptance or certification claim is
  made.
