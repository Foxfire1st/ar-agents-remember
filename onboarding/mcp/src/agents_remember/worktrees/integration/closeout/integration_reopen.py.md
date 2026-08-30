# mcp/src/agents_remember/worktrees/integration/closeout/integration_reopen.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/closeout/integration_reopen.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-30T06:08+02:00 |
| lastVerifiedCommitHash |  `346507af24396ab7b491e02511c4af006ccd3dc5`|
| lastVerifiedCommitDate |  2026-08-30T07:51:57+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Closeout integration overview](overview.md)

## Purpose

Owns the policy that decides whether a closeout must reopen an already completed integration.

## Code Commentary

`preview_integration_reopen` projects whether dirty or prospective code/memory output would need
another plane-owned integration. `completed_integration_reopen` evaluates the exact produced code,
memory-content, and ledger commits against the recorded source branches. It reopens only when new
content is not yet landed; a no-op or already-landed closeout preserves completed state.

The helpers keep code and external-memory decisions separate so coverage and failure evidence name
the affected leg directly. They inspect ancestry but never move a branch, mutate the contract, or
integrate output themselves; the closeout coordinator owns publication of the returned decision.

## Invariants And Boundaries

- Integration status changes only from exact produced-commit and source-ancestry facts.
- A memory-only settings closeout can reopen memory without falsely reopening unchanged code.
- Already-landed or no-op output leaves completed integration intact.
- This module decides; it never mutates Git, contracts, or lifecycle journals.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Preview distinguishes prospective code and memory reopen effects. | `preview_integration_reopen` | mcp/src/agents_remember/worktrees/integration/closeout/integration_reopen.py:13-46 |
| Completed output is evaluated per code and memory leg. | `completed_integration_reopen` | mcp/src/agents_remember/worktrees/integration/closeout/integration_reopen.py:49-81 |
| Memory reopening requires changed content and an unlanded ledger commit. | `_completed_memory_is_unlanded` | mcp/src/agents_remember/worktrees/integration/closeout/integration_reopen.py:97-116 |

## Cross-Repo References

No additional repository is consulted; the admitted worktree contract supplies both repository
and source-branch identities.

## Update History

- 2026-08-30T06:08+02:00 — MCAR-L03 A005: extracted completed-integration reopen policy from the
  closeout coordinator, preserving exact per-leg ancestry behavior while removing its CRAP and
  file-size pressure. Verification remains closeout-owned.
