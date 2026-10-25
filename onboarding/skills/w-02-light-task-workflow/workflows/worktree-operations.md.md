# skills/w-02-light-task-workflow/workflows/worktree-operations.md

## Governing Overview

[Repository overview](../../../overview.md)

## Purpose

The seat's worktree procedure kept by this skill: intake and intent, start/attach/status, mid-task sync, closeout hand-off, integration, finalization and cleanup, and reopening, under the `worktree_*` family's own authority.

## Code Commentary

The file is the surviving owner of the worktree procedure; its opening comment records that the retired `## MCP Tools` table named two tools no server exposes and was dropped with them, so the `worktree_*` family's own descriptions are the authority now. It wraps the existing light-task or external workflow without replacing the implementation, and it says plainly that closeout belongs to its sibling `closeout.md`, to which it supplies the contract path and the integration and finalization follow-up rules.

The current text reads each task's recorded branch edge instead of assuming one stack. An atomic master owns a root `series-contract.md` and one pushable integration branch, its leaf enclosures branch from that integration branch and integrate back into it, and a nested atomic master takes its child integration branch from the parent's. An organizational master is a logical owner: it carries no series contract and no integration branch of its own, and its leaves branch from and land on the recorded super branch, with a start refusing an organizational task root that still carries a live atomic series contract. Lineage is proved along those recorded edges rather than a fixed super → master → leaf ancestry, an integration branch is never a repair workbench, and `stale_base_choice="proceed-stale"` can override remote-tracking freshness but never ancestry along the recorded edges. Working intake runs context resolution, this skill's task-start drift check (now `c-05-create-or-update-onboarding-files`), the memory-content commit before any worktree when onboarding was refreshed, and the Worktree Intent Gate naming the branch, the leaf worktree and `leaf_id`, the memory mode, the landing path and its risks. Developer-gated starts, integrations and finalizations hold the action at the relay and follow `../../l-01-agent-lifecycles/operations/orientation.md` for the turn instead of ending it.

## Evidence



- The kept procedure owns intake and intent, start/attach/status, sync, closeout hand-off, integration, finalization, cleanup and reopening, with the `worktree_*` family as its authority. [1]



- Atomic and organizational masters are read from the task's recorded nature and edge: an organizational master adds no series contract or integration branch, and its leaves use the recorded super branch. [2]



- Intake order keeps context resolution, the task-start drift check, the pre-worktree memory commit and the Worktree Intent Gate, and a developer-gated step holds its action while the turn follows the orientation operation. [3]
