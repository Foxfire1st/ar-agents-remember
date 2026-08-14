# mcp/src/agents_remember/serving/harness_submission_ledger.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/harness_submission_ledger.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

What one submission authority retains about its operations, and what it can say about them.

## Code Commentary

### Logic

Module-level surface:

- `OperationRecord` (class, lines 58-252) — One ordinary operation's whole life: its state, its evidence, and what it answers with.
- `SubmissionLedger` (class, lines 255-437) — The bounded, epoch-stamped record store one submission authority admits into and reads from.
- `ref_key` (function, lines 440-441)

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
| Defines the class `OperationRecord` (lines 58-252) — One ordinary operation's whole life: its state, its evidence, and what it answers with.. | `OperationRecord` | mcp/src/agents_remember/serving/harness_submission_ledger.py:58-252 |
| Defines the class `SubmissionLedger` (lines 255-437) — The bounded, epoch-stamped record store one submission authority admits into and reads from.. | `SubmissionLedger` | mcp/src/agents_remember/serving/harness_submission_ledger.py:255-437 |
| Defines the function `ref_key` (lines 440-441). | `ref_key` | mcp/src/agents_remember/serving/harness_submission_ledger.py:444-445 |

## Update History

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
