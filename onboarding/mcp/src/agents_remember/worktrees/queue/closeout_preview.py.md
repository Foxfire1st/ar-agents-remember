# mcp/src/agents_remember/worktrees/queue/closeout_preview.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/queue/closeout_preview.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-22T10:39+02:00 |
| lastVerifiedCommitHash | `eb7ea60ab9919f009fef58f81afe5861aa1709da` |
| lastVerifiedCommitDate | 2026-08-22T11:44:33+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[governing overview](overview.md)

## Purpose

Builds response-only proposed commits, summaries, and ordering without mutating worktrees or protected refs.

## Code Commentary

`proposed_closeout_commits` distinguishes ordinary leaves from exact named-ref atomic series. Series previews describe already-recorded code and external-memory commits and do not promise ambient refresh or ledger writes that apply will not perform. Summary and ordering helpers keep preview and apply handoffs aligned.

## Invariants And Boundaries

- Preview never writes Git, contract, queue, or memory state.
- Series facts are named-ref/candidate facts, not ambient checkout facts.
- Proposed work and ordering must remain executable by the corresponding apply route.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Proposed commit payloads separate leaf mutation from exact series recording. | `proposed_closeout_commits` | mcp/src/agents_remember/worktrees/queue/closeout_preview.py:9-69 |
| Summary and ordering publish the same lifecycle altitude. | `closeout_summary`, `closeout_order` | mcp/src/agents_remember/worktrees/queue/closeout_preview.py:72-96; mcp/src/agents_remember/worktrees/queue/closeout_preview.py:99-125 |

## Documentation References

No configured domain-documentation or cross-repository source applies to this file.

## 260821-CLIVE-L1 Preview Parity

Preview now requires normalized `effectiveInput` and renders each leg's typed intent. It includes a `message` only for enabled legs and never generates a ledger subject. The same value is fingerprinted, journaled, rehydrated, recovered, and consumed by apply. This module describes proposed writes; it neither selects candidates nor owns lifecycle evidence.

## Update History

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: curated against accepted candidate tree `4241908c`; verification metadata remains pinned until governed closeout stamps the landed code commit.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: source moved to `mcp/src/agents_remember/worktrees/queue/closeout_preview.py` (new package route); the citation fixer repointed in-body references; import paths updated inside the module. Verified at code commit e5cb139f.


- 2026-08-15T23:38+02:00 — 260815-DAG-L4: created closeout preview projection onboarding from the frozen integration-authority candidate. Verification remains closeout-owned.
## Docs References

No external Domain Documentation source is configured for this internal route; task `260821-CLIVE-L1` and the cited repository source/tests govern this curation.

## Cross-Repo References

This file owns no ambient cross-repository authority. Any external-memory repository it reaches remains explicitly contract-addressed.
