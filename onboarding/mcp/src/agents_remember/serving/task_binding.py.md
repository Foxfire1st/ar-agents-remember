# mcp/src/agents_remember/serving/task_binding.py

## Governing Overview

[serving overview](overview.md)

## Purpose

Owns the single fail-closed task-binding preflight used by both the low-level spawn application and
the shared terminal opener. It prevents settings lookup or host effects from preceding structural
document, role, source-lineage, and reviewer-parent validation.

## Code Commentary

### 260921-ICR-L32 The Taskless Seat Set Admits The Curator

`TASKLESS_SEAT_ROLES` gains `curator` on the developer's **2026-09-24 ruling**, and the commented block above the declaration records why in the product's own terms: a curator whose work is a repository's knowledge foundation has no enclosure and, on a greenfield repository, no task document to bind, yet it still has instructions to receive — and before this ruling no route delivered them. The comment also states what the change is **not**: it is a seat-policy change rather than a consequence of the `c-14-knowledge-bootstrap` procedure, and the curator on the ordinary enclosure route is still task-bound and still arrives through a dispatched brief. Everything else about the gate is unchanged — a taskless role runs no structural altitude check, a supplied document is still resolved and still refused when bad, and an unknown role still takes the structural path. The declaration now sits at `:91` and the gate's read of the set at `:145`.

### Logic

`resolve_task_binding` canonicalizes the requested task and replacement documents, preserving the
exact task-document refusal dialect through `TaskDocumentResolutionFailure`. `_binding_refusal`
then enforces mutual exclusion, structural-role document presence and altitude, current source
lineage, and finally generation-bound reviewer-parent provenance. Lineage is deliberately checked
before reviewer-parent completeness so a stale selected branch reports its actionable sync state
rather than hiding it behind a later provenance defect.

`ResolvedTaskBinding` returns canonical references plus one typed semantic refusal. Consumers map
that same value into their own wire shape; neither consumer reimplements the policy.

### Conventions

Document and role are structural identity. Runtime session ids, settings, and launch selection are
outside this module and cannot influence admission.

### Invariants And Boundaries

- Both optional task references are resolved before the mutual-exclusion check, preserving exact
  missing/invalid/repository-mismatch attribution.
- Structural roles require one role-compatible task document; chat and terminal seats retain their
  non-structural path.
- Stale or unavailable lineage refuses before settings or host creation and carries the strict
  recovery projection.
- Reviewer parent document and role are complete, altitude-valid, and explicit; no owner is guessed.
- The module provides one authority, not a fallback reader or an alternate spawn path.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured.

### Repo-Internal References

- One API resolves canonical references and returns the shared refusal. [1]
- Binding order preserves lineage recovery before reviewer-parent validation. [2]
- Reviewer-parent ownership is explicit and altitude-specific. [3]

### Cross-Repo References

No cross-repository implementation dependency governs this file.
