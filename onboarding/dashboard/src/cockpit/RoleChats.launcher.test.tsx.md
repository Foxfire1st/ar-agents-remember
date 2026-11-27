# dashboard/src/cockpit/RoleChats.launcher.test.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

The suite checks catalog-supported launcher selection, explicit options states, explicit speed-feature and mode dispatch with settings-owned permission-feature display, and feature preservation across model/effort changes.

## Code Commentary

The unoffered-model fixture keeps Start disabled until an offered model is selected. The model-list failure fixture leaves the agent selectable without inventing a model. A launch lock rereads by itself without an ordinary status line — the case asserts no status or alert before and after the reread — while other refusals stay errors until an explicit successful action clears them (MIK-R75 rule 3). The host-offered speed value remains on the role agent across supported model overrides; a known unsupported tier/model disables Start, and another agent displays provider default. The speed-only case submits the explicit speed feature, leaves the mode selector at its first option and shows permission-bearing features as settings-owned chips. The test checks the first mode option and hover for the host label and settings source, and checks the optional Instructions chip and its source and replacement status. The explicit-mode case submits the chosen mode and keeps it through a model change. The dispatch assertions remain the payload-preservation boundary. Fresh-view tests replace same-origin answers rather than merging them. Pending-view tests replace an older display with matching saved inventory. An otherwise eligible Start stays enabled while metadata or shown-model options are pending. The launcher displays no separate catalog-status line before or after settlement.

## Invariants And Boundaries

Fixture validation does not prove native creation, paid-turn speed or permanent model availability. Attach tier proof to the same root-owned backend selection record.

## Evidence

The current source and test assertions below establish the documented ownership; test citations do not claim a rerun in this pass.




- The launcher displays configured tier and foreign default provenance, and marks a known unoffered model for replacement. [7]

- Matching saved inventory keeps eligible Start available during metadata and model-options refresh. The launcher shows no separate catalog-status line before or after settlement. [6]








- Current source owner or exact assertion described above. [3]





- The launcher keeps explicit speed choices separate from effort and waits for the shown model’s Speed control before exercising an override. [4]

- Mounted dispatch carries the explicit mode before and after a model override. [5]




### Clock And Settlement Evidence



- A launch-in-progress options response schedules a 1,500 ms reread, with no status line or alert. Start returns after the reread. [1]
