# dashboard/src/cockpit/RoleLaunchFeatures.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

Renders host-offered feature controls and mode/instruction chips for the single role launcher, with provenance in each control's hover text rather than a running defaults sentence.

## Code Commentary

`FeatureControl` dispatches permission-bearing features to `PermissionFeatureNote` and other features to `FeatureOverrideSelect`. The selector uses the shared `launcherSelect`, with the role-default option first and the complete selected label plus default provenance in `title`. The permission note is a settings-owned shared `launcherChip`, not an override control. `RoleLaunchFeatures` maps all features of the selected model, keeps explicit values in the agent override, and drops the override only when no explicit value or identity remains.

Once options are ready, `RoleLaunchDefaults` composes `ModeChip` and the optional `InstructionsChip`; the mode chip carries the host-labelled mode; its hover carries mode provenance and the host description. A foreign agent shows `At start`, with the resolution explanation in hover. An `Instructions` chip appears only when notes are present; its hover names their source and whether they replace or add to the baseline. Agent/model/effort provenance belongs to the corresponding selectors in `RoleLauncher`, not to a defaults line here. These are display changes, not permission or payload changes.

## Evidence

- Permission dispatch preserves settings-owned chips; FeatureOverrideSelect owns selectable labels and hover. [1]

- The feature-value updater retains identities and removes only an empty override. [2]

- The ready defaults composition draws the host mode and optional instruction chips. [3]
