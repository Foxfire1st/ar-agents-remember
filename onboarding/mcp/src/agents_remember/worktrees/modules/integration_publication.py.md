# mcp/src/agents_remember/worktrees/modules/integration_publication.py

## Governing Overview

[governing overview](overview.md)

## Purpose

Carries typed preflight state from integration planning into the irreversible publication step.

## CCR-R12@v5 Current Transaction Boundary

`IntegratePreview` and `IntegrationPublication` carry the source-pair, completion, handover, and
ref-safety facts that publication must recheck. They do not carry a planned normal-operation
quality gate or certification result. Integration applies the prepared pair with the existing
authority and compare-and-swap/ref-publication controls; full suites remain an explicit developer
request.

## Code Commentary

### Logic

`IntegratePreview` holds the evaluated seam guard and optional handover warning. `IntegrationPublication`
bundles every preflight fact the protected publication must re-verify: the contract, worktree args,
locked args, integration sources, integrated commits, and the handover warning.

The closeout-door cut (commit `fad9808e`) removed two members from this module: the
`intent: IntegrationPublicationIntent` field and the `publish_journaled_organizational_completion`
helper that consumed it. Integration no longer builds or publishes a completion intent, so this module
no longer imports `organizational_completion` and no longer publishes a master task document.

### Invariants And Boundaries

- These are dependency-light value types; each has exactly one implementation owner and is imported directly by `integrate.py`.
- No compatibility shim or implicit fallback exists.

## Evidence

### Repo-Internal References

- Evaluated seam guard and planned quality gate for preview. [1]
- Every preflight fact the irreversible publication re-verifies. [2]

### Documentation References

No configured domain-documentation or cross-repository source applies to this file.

## 260821-CLIVE-L2 Current Contract

The current source seams are `IntegratePreview` and `IntegrationPublication` — two frozen value types
and nothing else. The `protected_integration_decision` seam named by the original L2 reconciliation
exists nowhere in the tree (the closeout-door cut removed it), and the same cut removed
`IntegrationPublication`'s `intent` field. Integration still transfers authority from the
waiting-door projection into the journal, revalidates configured contract and protected refs at the
mutation boundary, and records publication evidence; source-ref movement must reconcile or complete
the same generation.

### Reconciled Source Evidence

- The current module exposes two value types at this ownership boundary — `IntegratePreview` and `IntegrationPublication`. The earlier `protected_integration_decision` no longer exists anywhere in the tree, so the reconciliation that named it is superseded; the closeout-door cut (`fad9808e`) also removed `IntegrationPublication`'s `intent` field. [3]
