# mcp/src/agents_remember/worktrees/integration/closeout_door_evidence.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/closeout_door_evidence.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T14:43+02:00 |
| lastVerifiedCommitHash | `f95487ec993b58d34911bba0206a7fa6ef9684eb`|
| lastVerifiedCommitDate | 2026-08-24T15:28:18+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Worktree-integration overview](overview.md)

## Purpose

Captures the exact code, external-memory, ledger, review, and source-base evidence sealed into one
closeout-door generation.

## Code Commentary

The builder requires current source bases, a unique ledger mapping, exact candidate trees, and
complete provenance. Any ambiguity or blocker refuses publication. Evidence belongs to the declared
generation and cannot be replaced later by queue recomputation.

## Invariants And Boundaries

- Candidate ancestry, review, memory, ledger, and source-base facts are immutable generation input.
- Missing or conflicting provenance fails closed.
- Disposable projections may report this evidence but never become its owner.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Door evidence is captured before generation identity is published. | `build_closeout_door_evidence` | `mcp/src/agents_remember/worktrees/integration/closeout_door_evidence.py` |

## Update History

- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: created from the final evidence owner. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.
