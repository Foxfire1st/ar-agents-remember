# skills/l-01-agent-lifecycles/reference/coordination/shared/closeout-recovery.md

## Governing Overview

[overview](../../../overview.md)

## Purpose

Tier-2 shared coordination detail for Architects, Orchestrators, and Managers covering unfinished or blocked closeout recovery, task-edit projection rebuilds, flat-mode direct closeout, Orchestrator recipient switches, and child permission notices.

## Code Commentary

Covers five procedures: recovering unfinished closeout and handling gate refusals (`closeout-gate-blocked`, `curator-coherence-knowledge-gate-refused`, `closeout-door-route-review-blocked`, `knowledge-gate-refused`, `direct-landing-knowledge-gate-refused`) without bypassing gates, using `worktree_status` and `worktree_operation_control` for direct landing, and Manager routine closeout reporting to the coordinating Orchestrator; applying intrinsically valid `task_doc` mutations immediately and relaying incomplete `projectionEffects` to the Orchestrator without patching queue rows; flat-mode direct paired closeout by the owning Architect only under explicit developer commit approval or delegation; switching an existing Manager's reporting recipient to a newly started Orchestrator while keeping its launch parent fixed; and escalating `held` permission prompts or `permission-pending` waits immediately with full seat identifiers (never a bare count), linking `operations/orientation.md#formal-permissions` and `#honor-harness-permission-decisions`.

## Relationships

Referenced as a Tier-2 recovery target by `models/role_capsules/refusal_references.py` (all four Family-5 closeout and operation-control keys point to `#recover-an-unfinished-closeout`). Registered in `composition-manifest.json` (`step_detail: true`) and mirrored under `package_data/runtime/skills/`.

## Evidence

- `#recover-an-unfinished-closeout` defines recovery for interrupted closeout, all five closeout/landing gate refusals, direct-landing `worktree_operation_control`, and Manager closeout notices. [1]
- `#apply-task-edits-and-rebuild-projections` keeps `task_doc` authoritative during closeout scheduling and routes incomplete `projectionEffects` to the Orchestrator. [2]
- Flat-mode direct closeout, Orchestrator recipient switch, and child permission-notice escalation rules specify exact authority and required notice fields. [3]
