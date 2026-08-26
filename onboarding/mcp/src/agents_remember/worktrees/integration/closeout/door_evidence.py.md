# mcp/src/agents_remember/worktrees/integration/closeout/door_evidence.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/closeout/door_evidence.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-26T14:32+02:00 |
| lastVerifiedCommitHash | `7833df0b219bba560f67f6e1158c3f4f155e1ce6` |
| lastVerifiedCommitDate | 2026-08-26T15:02:28+02:00|
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

## Invariants And Boundaries

- Candidate ancestry, review, memory, ledger, and source-base facts are immutable generation input.
- Missing or conflicting provenance fails closed.
- Disposable projections may report this evidence but never become its owner.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
- 2026-08-26T14:32+02:00 — Corrected stale uniqueness wording to match the source's newest-first
  `find_mapping` authority; no door behavior changed. Verification remains closeout-owned.

| Door evidence is captured before generation identity is published. | `capture_door_candidate_evidence`; `DoorCandidateEvidence` | mcp/src/agents_remember/worktrees/integration/closeout/door_evidence.py:30-160 |

## Update History

- 2026-08-25T08:16+02:00 — 260824-PDLS wave 004: moved this preserved sidecar with its behavior-preserving package split, repointed source evidence, and verified the emergency-landed source path at code commit `cb6623775a04cbdeb0509dc26f08a8268189c3f6`; this is onboarding provenance, not Dagger certification.

- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: created from the final evidence owner. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.
