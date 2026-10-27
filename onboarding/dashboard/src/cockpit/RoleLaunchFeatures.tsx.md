# dashboard/src/cockpit/RoleLaunchFeatures.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

Renders host-offered feature controls and mode/instruction chips for the single role launcher, with provenance in each control's hover text rather than a running defaults sentence.

## Code Commentary

`FeatureControl` dispatches permission-bearing features to `PermissionFeatureNote` and other features to `FeatureOverrideSelect`. The selector uses the shared `launcherSelect`, with the role-default option first and the complete selected label plus default provenance in `title`. The permission note is a settings-owned shared `launcherChip`, not an override control. In ordinary mode, `RoleLaunchFeatures` maps all features of the selected model, keeps explicit values in the agent override, and drops the override only when no explicit value or identity remains. Its basePreview branch instead renders noninteractive Base chips, explicitly not applied-choice claims for the stepped-up execution.

Once options are ready, ordinary `RoleLaunchDefaults` composes `ModeChip` and the optional `InstructionsChip`; its basePreview branch instead emits explicitly non-applied Base mode/instruction chips; the mode chip carries the host-labelled mode; its hover carries mode provenance and the host description. A foreign agent shows `At start`, with the resolution explanation in hover. An `Instructions` chip appears only when notes are present; its hover names their source and whether they replace or add to the baseline. Agent/model/effort provenance belongs to the corresponding selectors in `RoleLauncher`, not to a defaults line here. These are display changes, not permission or payload changes.

## Current Contract

`basePreview` defaults false on both exports. Ordinary feature/default rendering and override cleanup stay unchanged. With a stepped-up execution the caller passes true: every listed base feature becomes a noninteractive Base chip; mode and optional Instructions become Base chips too. Hover explicitly says these are not applied choices of the stepped-up execution. Feature/default labels match the host's option IDs or labels without case; service-tier preview uses the configured value without a built-in fast-to-priority conversion. The receipt reports the stepped-up model, not its applied mode, features or user instructions; user settings remain the permission owner.


This account is bound to the candidate source, not a claim of a running serving build or a fresh execution/acceptance verdict. Existing historical accounts remain historical.

## Evidence


- Worker/Curator typed review census, record-only exclusion and unknown history. [4]
- Reason admission, threshold and differing-harness/model inheritance boundary. [5]
- RoleLaunchFeatures retains settings-owned permissions and non-applied Base previews; feature labels match host IDs or labels without a built-in speed alias. [6]

- File-local implementation of the stated contract; caller-owned effects and governing workflow are separate evidence. [7]


- Permission dispatch preserves settings-owned chips; FeatureOverrideSelect owns selectable labels and hover. [1]


- The feature-value updater retains identities and removes only an empty override. [2]



- The ordinary ready defaults composition draws the host mode and optional instruction chips; basePreview labels them as non-applied Base previews. [3]
