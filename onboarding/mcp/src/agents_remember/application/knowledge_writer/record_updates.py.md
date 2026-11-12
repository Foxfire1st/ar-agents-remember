# mcp/src/agents_remember/application/knowledge_writer/record_updates.py

## Governing Overview

[Application layer overview](../overview.md)

## Purpose

Preserves stored authorship while updating origin evidence and remapping reconsideration links across alternative reordering.

## Code Commentary

record_origin deep-copies existing origin. Evidence for a foreign owner/task is queued as foreign evidence without rewriting that origin; own evidence is ordered/deduplicated, appended unless replace_evidence explicitly requests replacement, and an empty evidence key is removed. New origins are derived from the operation owner and handoff entry. remap_links runs only when alternatives change without explicit links. Each reconsider_on link is moved by its old alternative’s exact unique option text; missing or ambiguous matches report a problem requiring restated links.

## Invariants And Boundaries

A caller may restate links explicitly rather than relying on automatic remapping. A reorder cannot silently change the option a reconsideration link means, and incoming evidence cannot silently relabel another owner’s provenance.

## Evidence Scope

This source account is not a test result or an execution, permission, CODE/MEMORY acceptance or landing claim. No Domain Documentation source is configured for this slice; implementation facts are grounded in the concrete source below, with no asserted external-system contract.

## Evidence

- Preserves stored authorship while updating origin evidence and remapping reconsideration links across alternative reordering. A caller may restate links explicitly rather than relying on automatic remapping. A reorder cannot silently change the option a reconsideration link means, and incoming evidence cannot silently relabel another owner’s provenance. [1]
