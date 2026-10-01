# mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_controls.py

## Governing Overview

[Governing route overview](overview.md)

## Purpose

Task-addressed lifecycle controls derived from durable and live evidence.

## Code Commentary

### Logic

Recovery and resume validate the retained generation, exact door, and current code/memory input. The control owner no longer classifies or refuses a ledger byte/tree contradiction, and successor admission composes only code and memory messages. Real Git and publication contradictions still flow through the owning evidence checks.

The public surface is `LifecycleControlCommand`, `control_operation`. The control seam revalidates
the configured contract and generation under lease, reconciles worker exit and control mutations,
and dispatches cancel, retry, recover, resume, retire, or supersede from durable and live evidence.
Cancel terminates the exact worker and proves cancellable Git before publishing its cancelled
outcome and waiting successor. Public closeout resume accepts the fixed candidate and fresh
message fields, then starts at the first failed or stale gate while retaining the passing prefix;
integrate and direct-landing keep their independent recovery semantics.

### Conventions

Pure classifiers return typed observations; mutation owners publish write-ahead intent and exact evidence before advancing. Public projections carry bounded expected/observed facts and executable task-addressed next actions without leaking private operation identity.

#### Invariants And Boundaries

- The canonical root journal, located through the address-only locator and immutable enclosure manifest, owns normal lifecycle state.
- Accepted input and proven commits are immutable; retry and recovery stay on the same generation until evidence admits a successor.
- Queue rows and mutable task documents are not lifecycle evidence or fallback location authorities.

### Todos

None recorded beyond the explicit terminal-archive boundary recorded by the governing overview.

## Evidence

### Docs References

No external Domain Documentation source is configured for this slice. The current behavior is repository-owned and is supported by the source references below.

No configured external source applies.

### Repo-Internal References

The following current source boundaries establish the ledger-retirement behavior.

- `_resume` checks retained generation and exact publication evidence before worker relaunch. [1]
- `_resume_arguments` retains the admitted code/memory messages in the successor correction. [2]
- `_closeout_resume_admission` combines current candidate evidence with code/memory input for resume. [3]

The source file is the direct evidence for this file-specific ownership boundary.

- The module defines `LifecycleControlCommand`; `control_operation` as its public seam. [4]

### Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

No additional cross-repository evidence applies.

## CCR-R12@v5 Current Control Boundary

Lifecycle controls now resume a refused, cancelled, or failed closeout generation under a fresh
successor lease after rechecking current messages, candidate identity, and source provenance.
Resume/recovery is a transaction-control action: it does not imply a rerun of strict code quality,
memory quality, selected certification, curator coherence, or independent review. Explicit approval
and the current contract/door evidence remain required where the operation owner requires them.

## 260821-CLIVE Task-Addressed Control Semantics

Cancel, recover, retry, resume, retire, and supersede operate on canonical door+journal authority.
Cancel stops the worker, ignores retained private preparation as an approval prerequisite, and
publishes the reset/cancelled outcome with its waiting successor after exact worker-exit and Git
proof. Public closeout resume accepts the repaired fixed candidate and starts at the first failed or
stale gate while retaining the exact passing prefix; publication still revalidates the waiting door,
projection, and authority. Integrate and direct-landing retain their independent recovery semantics.
Missing initial doors and competing declarations refuse.

## Shared Control-Action Vocabulary

`LifecycleControlAction` is owned by `models/lifecycles/operation_kinds.py` alongside the closed
operation-kind vocabulary. This control module consumes that model; it no longer declares its own
action literal/enum or imports action identity from worker-termination evidence. Request parsing,
control classification, and public responses therefore share one exhaustive action type.

## CCR-R18@v1 Rebinding Controls And Previews

260831-CCR-L18 routed the control-layer projection rewrites through the envelope binders: `_preview_completed_supersede` now returns `bind_projection_result(operation_projection(record, contract=contract), {...})` for the `would-supersede` dry-run preview, and `_resume_closeout_successor` uses `bind_projection_result` with a `LifecycleRecommendedAction` (`apply-closeout-successor` → `worktree_closeout_apply`) plus guidance instead of mutating a `model_copy` projection. Every rewritten control projection therefore rebinds its component digests to the exact journal revision through the sole validator.
