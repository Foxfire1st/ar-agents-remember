# mcp/src/agents_remember/worktrees/queue/closeout_preview.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/queue/closeout_preview.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-21T00:45+02:00 |
| lastVerifiedCommitHash | `e5cb139f66abbd6502d4dcc4be883eb5f49770fe` |
| lastVerifiedCommitDate | 2026-08-21T00:28:23+02:00 |
| governingOverview | `overview.md` |

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
| Proposed commit payloads separate leaf mutation from exact series recording. | `proposed_closeout_commits` | mcp/src/agents_remember/worktrees/queue/closeout_preview.py:9-69 |
| Summary and ordering publish the same lifecycle altitude. | `closeout_summary`, `closeout_order` | mcp/src/agents_remember/worktrees/queue/closeout_preview.py:72-96; mcp/src/agents_remember/worktrees/queue/closeout_preview.py:99-125 |

## Documentation References

No configured domain-documentation or cross-repository source applies to this file.

## Update History

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: source moved to `mcp/src/agents_remember/worktrees/queue/closeout_preview.py` (new package route); the citation fixer repointed in-body references; import paths updated inside the module. Verified at code commit e5cb139f.


- 2026-08-15T23:38+02:00 — 260815-DAG-L4: created closeout preview projection onboarding from the frozen integration-authority candidate. Verification remains closeout-owned.