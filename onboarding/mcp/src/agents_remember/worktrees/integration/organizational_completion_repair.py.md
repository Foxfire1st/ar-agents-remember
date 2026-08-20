# mcp/src/agents_remember/worktrees/integration/organizational_completion_repair.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/organizational_completion_repair.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-21T00:45+02:00 |
| lastVerifiedCommitHash | `e5cb139f66abbd6502d4dcc4be883eb5f49770fe` |
| lastVerifiedCommitDate | 2026-08-21T00:28:23+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[governing overview](../../../overview.md)

## Purpose

Owns the queue-owned repair transition after a final organizational quality-gate failure: it retires the failed candidate and reopens only that leaf's closeout.

## Code Commentary

### Logic

`record_organizational_completion_repair` persists the exact reset generation at the gate-failure seam together with the terminal failure. `organizational_completion_repair_evidence` binds operation identity, contract/task identity, sprint/candidate/master documents, exact code/memory/ledger commits, and the SHA-256 of the only permitted reset contract. `prepare_organizational_completion_repair` reloads the canonical cancelled `integrate` WAL and requires `cancelled`, `cancelRequested`, and `finishedAt` before validating the failure result, repair evidence, operation identity, integration authority, queue binding, and commit tuple; then it retires the candidate and publishes the reset contract.

### Invariants And Boundaries

- The mutating repair owner accepts no caller-supplied lifecycle record.
- Cancellation persists the cancelled WAL before invoking the repair mutator.
- Only the exact failed final-leaf integration owner may reopen the closeout.
- Repair refuses if the code or memory super moved after the failed gate.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Reset generation is persisted at the exact gate-failure seam. | `record_organizational_completion_repair` | mcp/src/agents_remember/worktrees/integration/organizational_completion_repair.py:61-84 |
| Durable exact reset identity is built before first publication. | `organizational_completion_repair_evidence` | mcp/src/agents_remember/worktrees/integration/organizational_completion_repair.py:87-115 |
| Failed candidate is retired and only its leaf closeout reopened. | `prepare_organizational_completion_repair` | mcp/src/agents_remember/worktrees/integration/organizational_completion_repair.py:118-210 |
| Operation identity and code/memory integration authority are re-validated. | `_require_operation_identity` | mcp/src/agents_remember/worktrees/integration/organizational_completion_repair.py:299-372 |
| Reset contract clears the closed leaf back to not-started. | `_quality_repair_contract` | mcp/src/agents_remember/worktrees/integration/organizational_completion_repair.py:435-472 |

## Documentation References

No configured domain-documentation or cross-repository source applies to this file.

## Update History

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: source moved to `mcp/src/agents_remember/worktrees/integration/organizational_completion_repair.py` (new package route); the citation fixer repointed in-body references; import paths updated inside the module. Verified at code commit e5cb139f.


- 2026-08-17T12:09+02:00 — 260815-DAG-L5: created onboarding for the organizational completion repair WAL and crash recovery.