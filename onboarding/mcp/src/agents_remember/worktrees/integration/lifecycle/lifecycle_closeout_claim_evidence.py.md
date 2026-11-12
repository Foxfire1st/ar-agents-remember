# mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_closeout_claim_evidence.py

## Governing Overview

[Governing route overview](overview.md)

## Purpose

Builds the immutable closeout-preview argument map from the accepted operation input. Only enabled
code and memory legs contribute their explicit commit-message fields.

## Code Commentary

### Logic

`closeout_preview_args` emits the contract path and explicit messages for enabled code and memory legs only. It cannot request a ledger subject or turn a cache refresh into mutation authority.

The helper translates one accepted closeout input into the corrected public preview call. It does not
own door ancestry, cancellation release, queue selection, or operation replacement.

### Conventions

Accepted input, exact Git facts, and typed owner results stay distinct from disposable projections.

### Invariants And Boundaries

- Preview arguments are authority-free immutable inputs until the owning transaction validates them.
- Disabled commit legs never acquire synthesized messages.
- Door, queue, cancellation, and replacement authority stay with their owning lifecycle transactions.

### Todos

None recorded for the ledger-retirement boundary.

## Evidence

### Docs References

No external Domain Documentation source is configured for this slice. The current behavior is repository-owned and is supported by the source references below.

No configured external source applies.

### Cross-Repo References

No separately configured cross-repository implementation governs this file; any external-memory repository is addressed by the task contract.

No additional cross-repository evidence applies.

### Repo-Internal References

The following current source boundaries establish the ledger-retirement behavior.

- `closeout_preview_args` renders contract-addressed preview arguments with enabled code/memory messages. [1]
