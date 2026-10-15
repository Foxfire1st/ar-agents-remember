# mcp/src/agents_remember/application/knowledge_writer/refresh_restoration.py

## Governing Overview

[Application layer overview](../overview.md)

## Purpose

Restores an obsolete leaf-owned reconsideration refresh when its original base link is current again and no corresponding fired item remains.

## Code Commentary

Only leaf owners participate. _refreshed_subjects scans this leaf’s history for still_rejected rows; restore_refreshes subtracts the operation’s current reconsideration subjects, resolves the decision and base record, and examines corresponding links. Restoration requires matching relation/alternative and unchanged target path/locator, plus current code content equal to the original anchor content. Changed decisions are placed through the existing record owner and an explanatory note is emitted.

## Invariants And Boundaries

This is not arbitrary reset-to-base. Nonmatching links, absent records, changed path/locator or AnchorResolutionError leave the link untouched. Authored link changes and surviving reconsideration items are not erased to clear a finding.

## Evidence Scope

This source account is not a test result or an execution, permission, CODE/MEMORY acceptance or landing claim. No Domain Documentation source is configured for this slice; implementation facts are grounded in the concrete source below, with no asserted external-system contract.

## Evidence

- Restores an obsolete leaf-owned reconsideration refresh when its original base link is current again and no corresponding fired item remains. This is not arbitrary reset-to-base. Nonmatching links, absent records, changed path/locator or AnchorResolutionError leave the link untouched. Authored link changes and surviving reconsideration items are not erased to clear a finding. [1]
