# mcp/src/agents_remember/models/knowledge/evidence_read.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/knowledge/evidence_read.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T06:20+02:00 |
| lastVerifiedCommitHash |  `b5a74aee6cdf671c9963f3aba4df6d44b856f697`|
| lastVerifiedCommitDate |  2026-09-18T09:42:44+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l12` uncommitted source; base `e963a01c6804570d597e451eaa069eaba66bd3ec` |
| governingOverview | `mcp/src/agents_remember/models/overview.md` |

## Governing Overview

[models route overview](../overview.md)

## Purpose

The declared contract of the evidence read projection: its seeds, its item kinds, its counts, its page
and its result, plus the four artifact-resolution states and the assessment-reference state a claim is
served with.

## Code Commentary

### Logic

This is a **third** selection with its own seeds, item kinds, counts and declared policy name. It shares no
policy name with the recorded-scope selection or the facet selection, and no code path is shared with
either, so a shipped seed's page stays byte-identical not by a guard but because nothing here is reachable
from it.

Two seed kinds: `EvidenceClaimSeed` selects one claim's aggregate, `ObservationCandidateSeed` selects every
observation whose recorded tested candidate is the exact candidate named. `evidence_seed_digest` is the
seed's identity, and the two kind literals are the closed seed vocabulary.

`ArtifactResolution` is the read-time statement about an artifact, with four distinguishable states —
verified, mismatch, absent and not-checked — and its own validator refuses a state that claims bytes it
did not read, so "equal" cannot be reported from an unread path. `AssessmentReferenceState` is the sibling
for the assessment references: a claim with none is served as the explicit unassessed state, never with a
defaulted "compatible" or "complete".

Limitations are part of the claim, and an empty one is a fact: `limitations` is required on the served item,
so a summary that drops it is not constructible. The empty string is served as the empty string — a reader
is told the author declared no limitations, never that they are unknown.

`EVIDENCE_SELECTION_ITEM_LIMIT` is the bound, and `EVIDENCE_ITEM_LIMIT_REASON` states why a selection that
reaches it raises rather than emitting a partial page: there is no cursor, so there is no continuation
contract to bind and no position that could be read as a different selection.

### Conventions

Item order is fixed by item kind and by stable identifiers, never by an authored label, an insertion order
or a timestamp; `evidence_item_sort_key` and `_EVIDENCE_KIND_ORDER` are the one place that order is
stated. Every retained revision is served as its own item.

### Invariants And Boundaries

- **No field could carry a verdict.** There is no status, grade, score, confidence, severity or aggregate
  in any model here, and both item models are frozen and extra-forbidden, so a page cannot be extended with
  one. A passing run is served exactly as a failing one is: as a fact about what happened.
- **Absence is served as absence.** An absent artifact and an absent assessment each have their own
  explicit state; neither is defaulted into a reassuring value.
- **The projection derives nothing.** Counts are the selected set's own arithmetic and nothing more.
- **This selection is disjoint from the two shipped selections.** It declares its own policy version and
  appears in neither of their responses, which is what keeps their serialized pages unchanged.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The projection's own declared policy name and the bound that makes a selection complete or refused. | `EVIDENCE_SELECTION_POLICY_VERSION`; `EVIDENCE_SELECTION_ITEM_LIMIT`; `EVIDENCE_ITEM_LIMIT_REASON` | mcp/src/agents_remember/models/knowledge/evidence_read.py:55-55; mcp/src/agents_remember/models/knowledge/evidence_read.py:60-60; mcp/src/agents_remember/models/knowledge/evidence_read.py:62-64 |
| The claim record and revision items, and the subject and coverage items that carry what the claim asserts. | `EvidenceClaimRecord`; `EvidenceClaimRevision`; `ClaimSubject`; `ClaimCoverage` | mcp/src/agents_remember/models/knowledge/evidence_read.py:73-90; mcp/src/agents_remember/models/knowledge/evidence_read.py:93-103; mcp/src/agents_remember/models/knowledge/evidence_read.py:106-116; mcp/src/agents_remember/models/knowledge/evidence_read.py:119-130 |
| The observation record and revision items. | `VerificationObservationRecord`; `VerificationObservationRevision` | mcp/src/agents_remember/models/knowledge/evidence_read.py:133-139; mcp/src/agents_remember/models/knowledge/evidence_read.py:142-152 |
| The four distinguishable artifact-resolution states, whose own validator refuses a state that claims bytes it did not read. | `ArtifactResolution` | mcp/src/agents_remember/models/knowledge/evidence_read.py:166-198 |
| The unassessed state a claim with no assessment reference is served with. | `AssessmentReferenceState` | mcp/src/agents_remember/models/knowledge/evidence_read.py:207-230 |
| The two seed kinds and the seed's own identity. | `EvidenceClaimSeed`; `ObservationCandidateSeed`; `evidence_seed_digest` | mcp/src/agents_remember/models/knowledge/evidence_read.py:241-245; mcp/src/agents_remember/models/knowledge/evidence_read.py:248-272; mcp/src/agents_remember/models/knowledge/evidence_read.py:281-284 |
| The item union and its fixed kind order. | `EvidenceReadItem`; `evidence_item_sort_key` | mcp/src/agents_remember/models/knowledge/evidence_read.py:333-338; mcp/src/agents_remember/models/knowledge/evidence_read.py:359-362 |
| The counts, the page and the result a caller carries away. | `EvidenceReadCounts`; `EvidenceReadPage`; `EvidenceReadResult` | mcp/src/agents_remember/models/knowledge/evidence_read.py:384-405; mcp/src/agents_remember/models/knowledge/evidence_read.py:409-431; mcp/src/agents_remember/models/knowledge/evidence_read.py:447-478 |
| The case that asserts the four states are distinguishable and that a stored reference survives a mismatch unchanged. | "def test_the_four_artifact_resolution_states_are_distinguishable(" | mcp/tests/test_knowledge_evidence_observations.py:461-623 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T06:20+02:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): created this one-to-one card for the evidence read projection's declared contract. It records the third selection's disjointness from the two shipped selections, the four artifact-resolution states, the unassessed state, and the rule that limitations are served visibly with an empty value reported as a fact. This card carries **no `lastVerifiedCommitHash`**: every construct it cites exists only in this leaf's uncommitted candidate, so no real commit contains the content a stamp would claim to have verified. Naming the base commit there would be a verification claim about a tree the code never had; the `reviewedWorkingCandidate` row states what was actually read, and closeout owns the stamp once the code commit exists.
