# mcp/src/agents_remember/worktrees/closeout_preview.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/closeout_preview.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-15T23:38+02:00 |
| lastVerifiedCommitHash | `8bf6edad7e7e65e27cf735be0822f604531d0c8a` |
| lastVerifiedCommitDate | 2026-08-16T10:54:02+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[governing overview](../../../overview.md)

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
| Proposed commit payloads separate leaf mutation from exact series recording. | `proposed_closeout_commits` | mcp/src/agents_remember/worktrees/closeout_preview.py:9-69 |
| Summary and ordering publish the same lifecycle altitude. | `closeout_summary`, `closeout_order` | mcp/src/agents_remember/worktrees/closeout_preview.py:72-125 |

## Documentation References

No configured domain-documentation or cross-repository source applies to this file.

## Update History

- 2026-08-15T23:38+02:00 — 260815-DAG-L4: created closeout preview projection onboarding from the frozen integration-authority candidate. Verification remains closeout-owned.
