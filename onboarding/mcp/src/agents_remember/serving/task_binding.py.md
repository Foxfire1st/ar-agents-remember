# mcp/src/agents_remember/serving/task_binding.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/task_binding.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-31T12:00+02:00 |
| lastVerifiedCommitHash | `86639933d61528387ce106dbd4d7a334bd468671` |
| lastVerifiedCommitDate |  2026-09-24T18:51:31+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| One API resolves canonical references and returns the shared refusal. | `resolve_task_binding` | mcp/src/agents_remember/serving/task_binding.py:60-87 |
| Binding order preserves lineage recovery before reviewer-parent validation. | `_binding_refusal` | mcp/src/agents_remember/serving/task_binding.py:100-125 |
| Reviewer-parent ownership is explicit and altitude-specific. | `_validate_structural_parent` | mcp/src/agents_remember/serving/task_binding.py:128-171 |

## Cross-Repo References

No cross-repository implementation dependency governs this file.

## Update History
- 2026-09-24T17:20:00+02:00 — 260921-ICR-L32 curator (uncommitted change set on `ar/260921-icr-l32-ar`, code base `71a170796f5380bd3a5b65a5c3323ca4f92b0cc0` plus the working-tree delta; gate `verify-l32-round2.md` = `pass`): **body update — the D56 admission.** A new subsection records the new membership, the operator's own words the comment quotes, what the change is explicitly not (a seat-policy change, not a consequence of the procedure), and that the rest of the gate's behaviour is unchanged; the declaration's and the read's current lines are stated. No verification stamp was advanced: the candidate is uncommitted, so no commit carries this body, and the governed closeout owns the real stamp.

- 2026-08-31T12:00+02:00 — Created during ARSPAWN-L5 A005 review repair to replace duplicated,
  late task-binding validation with one pre-settings and pre-host authority. Verification remains
  closeout-owned.
