# mcp/src/agents_remember/worktrees/integration/closeout/door_evidence.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/closeout/door_evidence.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `fbc89847233b1c5959f56475f2cb51f936d5ef0b` |
| lastVerifiedCommitDate | 2026-09-02T07:47:04+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[Worktree-integration overview](../overview.md)

## Purpose

Captures the exact code, external-memory, ledger, review, and source-base evidence sealed into one
closeout-door generation.

## Code Commentary

The builder requires current source bases, the newest ledger mapping for the exact code base,
exact candidate trees, and complete provenance. Older same-code rows remain valid history; missing
current authority or conflicting provenance refuses publication. Evidence belongs to the declared
generation and cannot be replaced later by queue recomputation.

Under CCR-R03@v1 the review provenance seam now re-requires the current route review
(`require_current_route_review`) before its task intent is rechecked, and fingerprints review
provenance as the review record's own `recordDigest` instead of recomputing a local tuple over the
record and its evidence facts — so the door consumes the record's content-addressed identity
directly; `door-review-provenance-stale` is reported when the route review's evidence bytes changed
cit:([`_review_provenance`], mcp/src/agents_remember/worktrees/integration/closeout/door_evidence.py:228-250).

## Invariants And Boundaries

- Candidate ancestry, review, memory, ledger, and source-base facts are immutable generation input.
- Missing or conflicting provenance fails closed.
- Disposable projections may report this evidence but never become its owner.
- The review provenance fingerprint is the route-review record digest; changing the review evidence
  bytes makes the door provenance stale exactly, without re-hashing the evidence tuple locally.

## Docs References

No configured Domain Documentation source applies to this repository-internal lifecycle seam.

| Finding | Anchor | Source |
| --- | --- | --- |
| The door evidence vocabulary has no external authority. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Door evidence is captured before generation identity is published. | `capture_door_candidate_evidence`; `DoorCandidateEvidence` | mcp/src/agents_remember/worktrees/integration/closeout/door_evidence.py:30-160 |
| Review provenance re-requires current route review and fingerprints its record digest. | `_review_provenance` | mcp/src/agents_remember/worktrees/integration/closeout/door_evidence.py:228-250 |

## Update History

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for fbc89847233b1c5959f56475f2cb51f936d5ef0b (CCR-R03@v1/L03): recorded the route-review currentness re-requirement and the record-digest review provenance fingerprint; prior capture and fail-closed prose preserved.

- 2026-08-26T14:32+02:00 — Corrected stale uniqueness wording to match the source's newest-first
  `find_mapping` authority; no door behavior changed. Verification remains closeout-owned.

- 2026-08-25T08:16+02:00 — 260824-PDLS wave 004: moved this preserved sidecar with its behavior-preserving package split, repointed source evidence, and verified the emergency-landed source path at code commit `cb6623775a04cbdeb0509dc26f08a8268189c3f6`; this is onboarding provenance, not Dagger certification.

- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: created from the final evidence owner. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.