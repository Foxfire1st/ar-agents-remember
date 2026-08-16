# mcp/src/agents_remember/worktrees/atomic_series_seal.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/atomic_series_seal.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-15T23:38+02:00 |
| lastVerifiedCommitHash | `8bf6edad7e7e65e27cf735be0822f604531d0c8a` |
| lastVerifiedCommitDate | 2026-08-16T10:54:02+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[governing overview](../../../overview.md)

## Purpose

Refuses new or reopened atomic child leaves once the parent series closeout edge has begun.

## Code Commentary

`require_series_accepting_leaves` treats only a not-started closeout, integration, and cleanup lifecycle as open for child admission. The path form reloads the exact parent contract at the mutation boundary, closing the race between an earlier preflight and start or task-reopen publication.

## Invariants And Boundaries

- Series closeout is the irreversible child-admission seal.
- Missing or mismatched parent contracts fail closed.
- Start and reopen must recheck the seal under repository authority immediately before mutation.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Lifecycle cells define whether a series still accepts leaves. | `require_series_accepting_leaves` | mcp/src/agents_remember/worktrees/atomic_series_seal.py:14-28 |
| The path helper reloads the exact parent contract for boundary revalidation. | `require_series_path_accepting_leaves` | mcp/src/agents_remember/worktrees/atomic_series_seal.py:31-43 |

## Documentation References

No configured domain-documentation or cross-repository source applies to this file.

## Update History

- 2026-08-15T23:38+02:00 — 260815-DAG-L4: created atomic series child-admission seal onboarding from the frozen integration-authority candidate. Verification remains closeout-owned.

