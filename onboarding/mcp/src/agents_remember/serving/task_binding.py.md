# mcp/src/agents_remember/serving/task_binding.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/task_binding.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-31T12:00+02:00 |
| lastVerifiedCommitHash | `f2b7c648f540efb9d64ceea22e11e651cb5cc914` |
| lastVerifiedCommitDate |  2026-08-31T15:32:32+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving overview](overview.md)

## Purpose

Owns the single fail-closed task-binding preflight used by both the low-level spawn application and
the shared terminal opener. It prevents settings lookup or host effects from preceding structural
document, role, source-lineage, and reviewer-parent validation.

## Code Commentary

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

- 2026-08-31T12:00+02:00 — Created during ARSPAWN-L5 A005 review repair to replace duplicated,
  late task-binding validation with one pre-settings and pre-host authority. Verification remains
  closeout-owned.
