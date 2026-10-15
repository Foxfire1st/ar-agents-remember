# mcp/src/agents_remember/application/knowledge_worklist/linkage.py

## Governing Overview

[Application layer overview](../overview.md)

## Purpose

Measures whether changed files and actual changed hunk lines intersect recorded realization/proof ranges on their own comparison sides.

## Code Commentary

change_linkage constructs one _Linkage over CodeTrees and the two parsed knowledge sides. Each change retains status/content/mode facts and optional rename information. Non-text changes, and the mode fact of a mode change, receive a file-level answer requiring a file-locator entry on either side. Text hunks resolve each side’s stored anchors against that side’s blob; only positive old/new changed-line counts can intersect that side’s spans.

## Invariants And Boundaries

A delete-only hunk cannot borrow a C span; an insertion-only hunk cannot borrow a B span. Non-text linkage requires whole-file coverage rather than any symbol at that path. Resolved recorded ranges are linkage observations, not an authored acceptance or invariant-effect judgment.

## Evidence Scope

This source account is not a test result or an execution, permission, CODE/MEMORY acceptance or landing claim. No Domain Documentation source is configured for this slice; implementation facts are grounded in the concrete source below, with no asserted external-system contract.

## Evidence

- Measures whether changed files and actual changed hunk lines intersect recorded realization/proof ranges on their own comparison sides. A delete-only hunk cannot borrow a C span; an insertion-only hunk cannot borrow a B span. Non-text linkage requires whole-file coverage rather than any symbol at that path. Resolved recorded ranges are linkage observations, not an authored acceptance or invariant-effect judgment. [1]
