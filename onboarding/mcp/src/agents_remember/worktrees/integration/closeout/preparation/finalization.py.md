# mcp/src/agents_remember/worktrees/integration/closeout/preparation/finalization.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/closeout/preparation/finalization.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T17:14:07+00:00 |
| lastVerifiedCommitHash | |
| lastVerifiedCommitDate | |
| governingOverview | `overview.md` |

## Governing Overview

[Preparation overview](overview.md)

## Purpose

Guarded publication of the original prepared outputs.

## Code Commentary

### Logic

The finalizer reopens the current worker, original preparation/certification objects, raw commit bytes, effective policy, task/source authority, route review and approval. It records mutation intent before exact expected-old ref publication, materializes the deterministic ledger through the existing recovery classifier, and retains commit-proven evidence only after physical/index/ref readback. Genuine existing legs retain their original C/M/L identities without creating empty commits. It finalizes the canonical contract only after the ordered output proofs. This source description is not a claim that the new route has passed tests or CCR acceptance.

### Conventions

Import the owning module directly. Current uncommitted implementation has no commit-based verification stamp.

### Invariants And Boundaries

Prepared objects, selected evidence, publication and approval remain separate facts. Historical acceptance cannot be inferred from this card.

### Todos

No additional source-local TODO is asserted.

## Docs References

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation applies. | N/A | N/A |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| `_output` owns the described behavior. | `_output` | `mcp/src/agents_remember/worktrees/integration/closeout/preparation/finalization.py:62-74` |
| `_materialize_ledger` owns the described behavior. | `_materialize_ledger` | `mcp/src/agents_remember/worktrees/integration/closeout/preparation/finalization.py:235-253` |
| `_publish_leg` owns the described behavior. | `_publish_leg` | `mcp/src/agents_remember/worktrees/integration/closeout/preparation/finalization.py:256-310` |
| `_closed_payload` owns the described behavior. | `_closed_payload` | `mcp/src/agents_remember/worktrees/integration/closeout/preparation/finalization.py:313-323` |
| `finalize_prepared_closeout` owns the described behavior. | `finalize_prepared_closeout` | `mcp/src/agents_remember/worktrees/integration/closeout/preparation/finalization.py:326-350` |
| `resume_prepared_closeout` owns the described behavior. | `resume_prepared_closeout` | `mcp/src/agents_remember/worktrees/integration/closeout/preparation/finalization.py:353-372` |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository source is needed. | N/A | N/A |

## Update History

### 2026-09-06T17:14:07+00:00 — Initial L34 implementation card

Recorded the released implementation without claiming tests, certification or acceptance.
