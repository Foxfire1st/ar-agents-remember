# mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_closeout_claim_evidence.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_closeout_claim_evidence.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T14:43+02:00 |
| lastVerifiedCommitHash | `f95487ec993b58d34911bba0206a7fa6ef9684eb`|
| lastVerifiedCommitDate | 2026-08-24T15:28:18+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[Worktree-integration overview](../overview.md)

## Purpose

Defines immutable closeout preview arguments and resolves the exact claimed predecessor that may
authorize a waiting successor.

## Code Commentary

The helper joins journal and door proof without reconstructing claim ownership from a mutable queue
binding. A successor is eligible only when the retained claimed generation and operation evidence
match exactly.

## Invariants And Boundaries

- Claim evidence is journal-and-door evidence, never queue inference.
- Preview arguments are authority-free immutable inputs until the owning transaction validates them.
- Missing or mismatched predecessor proof refuses successor construction.

## Update History

- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: created from the final claim-evidence helper. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.
