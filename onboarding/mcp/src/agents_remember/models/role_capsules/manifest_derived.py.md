# mcp/src/agents_remember/models/role_capsules/manifest_derived.py

## Governing Overview

[Overview](../overview.md)

## Purpose

Composes authored reference topology and legal no-step decisions with generated reference roles, action wording and core audiences for product readers.

## Code Commentary

`validate_no_step_marks` checks authored references independently of generated routing. `compose_manifest` constructs a view without mutating its input and iterates only authored reference entries, so generated entries do not add reference members. It strips authored `roles` and `step` fields from each effective reference and overlays `derived.references`; reference reader roles and action wording therefore come only from the derived part.

An ordinary reference with an authored `step: null` refuses a stale generated step; a reference with neither a no-step mark nor a generated step is refused. A no-step mark on a `step_detail: true` reference and malformed objects are also refused. Each refusal names `mcp/.venv/bin/python scripts/renew-instructions.py` as the corrective command. If `derived.core` is present, composition removes authored core `roles` and overlays the generated core entry, including the shared digest audience.

## Relationships

Manifest consumers use this helper before interpreting reference delivery. The renewal manifest planner produces its generated input. Authored reference membership and legal explicit no-step decisions remain separate from derived reader roles and action wording.

## Evidence

### Repo-Internal References (renewed)

- The composed view retains authored reference membership and legal no-step decisions, reads reference roles and actions from derived values, and overlays derived core audiences; invalid marks and stale or missing steps name the renewal command. [1]
