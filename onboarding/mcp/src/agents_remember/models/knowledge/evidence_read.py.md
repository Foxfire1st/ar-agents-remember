# mcp/src/agents_remember/models/knowledge/evidence_read.py

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

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The projection's own declared policy name and the bound that makes a selection complete or refused. [1]
- The claim record and revision items, and the subject and coverage items that carry what the claim asserts. [2]
- The observation record and revision items. [3]
- The four distinguishable artifact-resolution states, whose own validator refuses a state that claims bytes it did not read. [4]
- The unassessed state a claim with no assessment reference is served with. [5]
- The two seed kinds and the seed's own identity. [6]
- The item union and its fixed kind order. [7]
- The counts, the page and the result a caller carries away. [8]
- The case that asserts the four states are distinguishable and that a stored reference survives a mismatch unchanged. [9]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
