# mcp/src/agents_remember/worktrees/named_ref_memory.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/named_ref_memory.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-15T23:38+02:00 |
| lastVerifiedCommitHash | `8bf6edad7e7e65e27cf735be0822f604531d0c8a` |
| lastVerifiedCommitDate | 2026-08-16T10:54:02+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[governing overview](../../../overview.md)

## Purpose

Loads `memory.md` from the exact local memory source ref instead of the ambient repository checkout.

## Code Commentary

`load_named_ref_ledger` resolves a canonical local branch, reads the ledger blob directly from that ref, and parses it through the shared memory ledger model. Start admission, landing evidence, carryover guidance, and cleanup therefore evaluate the same task-derived memory history that integration owns.

## Invariants And Boundaries

- The branch is canonicalized before reading.
- Ambient checkout contents are never accepted as source-ref evidence.
- Missing or malformed exact-ref ledgers fail closed.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Exact-ref blob loading and parsing have one shared boundary. | `load_named_ref_ledger` | mcp/src/agents_remember/worktrees/named_ref_memory.py:12-20 |

## Documentation References

No configured domain-documentation or cross-repository source applies to this file.

## Update History

- 2026-08-15T23:38+02:00 — 260815-DAG-L4: created named-ref memory ledger reader onboarding from the frozen integration-authority candidate. Verification remains closeout-owned.

