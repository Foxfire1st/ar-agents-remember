# mcp/src/agents_remember/application/knowledge_worklist/leaf_completion.py

## Governing Overview

[Application layer overview](../overview.md)

## Purpose

Completes explicit leaf comparisons with onboarding trace, settles uncovered changes and persists a recomputed worklist through the existing leaf owner.

## Code Commentary

worklist_over obtains the leaf worklist at runtime to avoid the composition import cycle. It returns None for an inapplicable comparison and preserves incomplete runs. Complete runs read changed-path candidate blobs from the worklist’s own recorded candidate tree before adding onboarding items and settling unexplained changes. Settling recalculates the digest/open count and removes answering trace subjects from unnecessaryRows. Trace-side admission retains legacy/non-leaf applicability and names an unestablished converted side as incomplete. recompute_leaf_worklist converts Git and unexpected computation failures into named incomplete documents; a persistence OSError returns the document with no persisted path. LeafWorklistRecompute projects the result through worklist_summary.

## Invariants And Boundaries

Unreadable candidate blobs are not unchanged source. A returned worklist can exist without a persisted enclosure file; None means inapplicability, not a successful empty comparison. This module composes domain owners rather than creating another recomputation route.

## Evidence Scope

This source account is not a test result or an execution, permission, CODE/MEMORY acceptance or landing claim. No Domain Documentation source is configured for this slice; implementation facts are grounded in the concrete source below, with no asserted external-system contract.

## Evidence

- Completes explicit leaf comparisons with onboarding trace, settles uncovered changes and persists a recomputed worklist through the existing leaf owner. Unreadable candidate blobs are not unchanged source. A returned worklist can exist without a persisted enclosure file; None means inapplicability, not a successful empty comparison. This module composes domain owners rather than creating another recomputation route. [1]
