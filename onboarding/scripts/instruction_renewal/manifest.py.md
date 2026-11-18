# scripts/instruction_renewal/manifest.py

## Governing Overview

[Overview](../../overview.md)

## Purpose

Derives effective reference steps and audiences from authored reference entries, role reasons and current instruction pointers.

## Code Commentary

The planner first calls `validate_no_step_marks`, which refuses an authored `step: null` on a `step_detail: true` reference before pointer derivation. The refusal tells the author to supply a source action, remove the mark and run `mcp/.venv/bin/python scripts/renew-instructions.py`.

For an ordinary reference, a legal authored `step: null` takes precedence even when pointer-derived actions exist: the generated entry keeps its audience and emits no step. Without that mark, the planner joins derived actions; if neither a mark nor an action exists, it refuses the reference and names the same renewal command. Reference audiences combine pointer-derived roles with roles named in the authored `rolesReason`, ordered by `role_order`.

The planner generates `derived.core.every-role.roles` from authored role entries whose `core` list contains `every-role`, then validates the replacement routing with `compose_manifest`. Reference reader roles and action wording are generated values, while reference topology and legal no-step marks remain authored.

## Relationships

The authored composition manifest retains reference topology, `rolesReason` explanations and legal no-step decisions. The model composition helper takes reference roles and action wording from `derived.references` and replaces core audiences from `derived.core`.

## Evidence

### Repo-Internal References (renewed)

- The planner validates authored no-step marks before derivation, generates reference routing and the shared digest audience, then validates the composed result. [1]
