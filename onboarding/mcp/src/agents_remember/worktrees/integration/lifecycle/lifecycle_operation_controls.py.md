# mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_controls.py

## Governing Overview

[Governing route overview](overview.md)

## Purpose

Task-addressed lifecycle controls derived from durable and live evidence.

## Code Commentary

### Logic

The control owner validates the addressed generation and current code and memory evidence. Direct landing is admitted by its own accepted input. The historical closeout and integration kinds route to typed replacement guidance.

The public surface is `LifecycleControlCommand` and `control_operation`. It revalidates the configured contract and generation under lease. Direct cancellation checks the retained receipt and proves that the generation published no Git output before publishing cancellation. Direct recovery uses the admitted input and settles a completed closing receipt in the same call.

For historical closeout and integration, an absent record or an exact matching historical generation receives the retired-operation answer and the corresponding synchronous call. A mismatched generation returns `lifecycle-generation-changed` with the requested and observed generations. Historical records remain available for audit.

### Conventions

Pure classifiers return typed observations; mutation owners publish write-ahead intent and exact evidence before advancing. Public projections carry bounded expected/observed facts and executable task-addressed next actions without leaking private operation identity.

#### Invariants And Boundaries

- The canonical root journal, located through the address-only locator and immutable enclosure manifest, owns normal lifecycle state.
- Accepted input and proven commits are immutable; retry and recovery stay on the same generation until evidence admits a successor.
- Queue rows and mutable task documents are not lifecycle evidence or fallback location authorities.

### Todos

None recorded beyond the explicit terminal-archive boundary recorded by the governing overview.

## Direct-create retry and public recover

A mechanically recoverable interrupted direct-create generation is requeued through its advertised public recovery owner and completed under that same accepted input. Code/ref/history contradictions retain the developer-decision result. This branch does not invent a door, erase memory pairing or allocate another code commit.

## Evidence

### Docs References

No external Domain Documentation source is configured for this slice. The current behavior is repository-owned and is supported by the source references below.

No configured external source applies.

### Repo-Internal References

The following current source boundaries establish the ledger-retirement behavior.



- The direct recovery handler continues its admitted generation inline and settles a completed closing receipt. [1]





The source file is the direct evidence for this file-specific ownership boundary.



- The module defines `LifecycleControlCommand`; `control_operation` as its public seam. [4]



### Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

No additional cross-repository evidence applies.

## Direct generations and historical records

The owner first reads the addressed journal. An absent or matching record of a retired kind returns `lifecycle-operation-retired` before reconciliation. The answer points closeout to `worktree_closeout_apply` and integration to `worktree_integrate`. A mismatched generation returns `lifecycle-generation-changed` with the observed identity. A direct record claims no door. Its completed owner may retire after proving exact ownership and an idle integration claim. Supersede points to a fresh direct call. Recover continues the admitted input and settles the closing receipt.

## Shared Control-Action Vocabulary

`LifecycleControlAction` is owned by `models/lifecycles/operation_kinds.py` alongside the closed
operation-kind vocabulary. This control module consumes that model; it no longer declares its own
action literal/enum or imports action identity from worker-termination evidence. Request parsing,
control classification, and public responses therefore share one exhaustive action type.

## Projection binding

A result added to an operation projection uses the shared envelope binder so the projected identity and state remain tied to the exact record.

- The direct recovery handler continues its admitted generation inline and settles a completed closing receipt. [5]

- The public tool table describes absent, matching and stale generation cases and the replacement calls. [6]
- The operation journal guide describes inline closeout, the historical audit record and generation-bound controls. [7]
- The integration guide describes the inline call and its lack of an operation journal record. [8]
- An absent or matching historical record receives the replacement tool, with record details when present. [9]
- A matching record is checked for retirement before reconciliation. [10]
- The generation check distinguishes absent historical records from a mismatch and binds the mismatch answer to both generations. [11]
