# mcp/src/agents_remember/serving/pi_rpc_submissions.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/pi_rpc_submissions.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb` |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

The Pi adapter's bounded prompt-correlation ledger.

## Code Commentary

### Logic

Module-level surface:

- `PiSubmissionEvidence` (class, lines 16-25) — What one submitted prompt is known to be, and the entry cursor it was sent after.
- `PiSubmissionLedger` (class, lines 28-64) — Bounded request-id ledger for Pi prompts, from which only a settled row may be evicted.

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.

### Todos

None.

## Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Defines the class `PiSubmissionEvidence` (lines 16-25) — What one submitted prompt is known to be, and the entry cursor it was sent after.. | `PiSubmissionEvidence` | mcp/src/agents_remember/serving/pi_rpc_submissions.py:16-25 |
| Defines the class `PiSubmissionLedger` (lines 28-64) — Bounded request-id ledger for Pi prompts, from which only a settled row may be evicted.. | `PiSubmissionLedger` | mcp/src/agents_remember/serving/pi_rpc_submissions.py:28-64 |

## Update History

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
