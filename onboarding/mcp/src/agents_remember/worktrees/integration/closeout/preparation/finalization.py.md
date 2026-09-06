# mcp/src/agents_remember/worktrees/integration/closeout/preparation/finalization.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/closeout/preparation/finalization.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T21:46:58+00:00 |
| lastVerifiedCommitHash | `d36109038b3f2b500c138f9dc1ea9c9f9a247489`|
| lastVerifiedCommitDate | 2026-09-06T22:21:49+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Preparation overview](overview.md)

## Purpose

Guarded publication of the original prepared outputs.

## Code Commentary

### Logic

`_retain_existing_leg` preserves unchanged outputs. `_publication_intent` journals the original physical prestate once; `_observe_proven_leg` reopens published output through its original authority. `_ledger_publication_started` recognizes that ledger publication supersedes the intermediate memory ref, while `_physical_memory` validates exact ledger recovery states and bytes.

The finalizer reopens the current worker, original preparation/certification objects, raw commit bytes, effective policy, task/source authority, route review and approval. It records mutation intent before exact expected-old ref publication, materializes the deterministic ledger through the existing recovery classifier, and retains commit-proven evidence only after physical/index/ref readback. Genuine existing legs retain their original C/M/L identities without creating empty commits. It finalizes the canonical contract only after the ordered output proofs. This source description is not a claim that the new route has passed tests or CCR acceptance.

### Conventions

Import the owning module directly. The implementation is present in landed IAS; this preparation pass does not advance verification stamps.

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
| `_output` owns the described behavior. | `_output` | `mcp/src/agents_remember/worktrees/integration/closeout/preparation/finalization.py:93-105` |
| `_materialize_ledger` owns the described behavior. | `_materialize_ledger` | `mcp/src/agents_remember/worktrees/integration/closeout/preparation/finalization.py:282-300` |
| `_publish_leg` owns the described behavior. | `_publish_leg` | `mcp/src/agents_remember/worktrees/integration/closeout/preparation/finalization.py:373-400` |
| `_closed_payload` owns the described behavior. | `_closed_payload` | `mcp/src/agents_remember/worktrees/integration/closeout/preparation/finalization.py:403-413` |
| `finalize_prepared_closeout` owns the described behavior. | `finalize_prepared_closeout` | `mcp/src/agents_remember/worktrees/integration/closeout/preparation/finalization.py:416-443` |
| `resume_prepared_closeout` owns the described behavior. | `resume_prepared_closeout` | `mcp/src/agents_remember/worktrees/integration/closeout/preparation/finalization.py:446-465` |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository source is needed. | N/A | N/A |

## Update History

- 2026-09-06T21:46:58+00:00 — Reconciled landed IAS helper ownership and source anchors. Verification pins and historical evidence remain unchanged; no certification or delivery is asserted.

### 2026-09-06T17:14:07+00:00 — Initial L34 implementation card

Recorded the released implementation without claiming tests, certification or acceptance.
