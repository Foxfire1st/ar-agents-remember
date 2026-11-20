# dashboard/src/cockpit/RoleLaunchFeatures.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

Renders host-offered feature controls, instruction chips and non-applied Base previews for the single role launcher, with provenance in each control's hover text rather than a running defaults sentence.

## Code Commentary

`FeatureControl` dispatches permission-bearing features to `PermissionFeatureNote` and other features to `FeatureOverrideSelect`. The selector uses the shared `launcherSelect`, with the role-default option first and the complete selected label plus default provenance in `title`. The permission note is a settings-owned shared `launcherChip`, not an override control. In ordinary mode, `RoleLaunchFeatures` maps all features of the selected model, keeps explicit values in the agent override, and keeps the selected mode when editing a feature on a launcher-created override. Its basePreview branch instead renders noninteractive Base chips, explicitly not applied-choice claims for the stepped-up execution.

Once options are ready, ordinary `RoleLaunchDefaults` renders the optional `InstructionsChip`. Its `basePreview` branch explicitly labels the Base mode and instructions as non-applied. The adjacent [mode selector](role-launcher/ModeOverrideSelect.tsx.md) owns the ordinary mode control. An `Instructions` chip appears only when notes are present; its hover names their source and whether they replace or add to the baseline. Agent/model/effort provenance belongs to the corresponding selectors in `RoleLauncher`, not to a defaults line here. These are display changes, not permission or payload changes.

## Current Contract

`basePreview` defaults false on both exports. Ordinary feature rendering and feature-override cleanup keep their existing behavior. The ready ordinary defaults component renders only the optional Instructions chip. The adjacent selector presents the ordinary permission-mode choice. With a stepped-up execution the caller passes true: every listed base feature becomes a noninteractive Base chip; mode and optional Instructions become Base chips too. Hover explicitly says these are not applied choices of the stepped-up execution. Feature/default labels match the host's option IDs or labels without case; service-tier preview uses the configured value without a built-in fast-to-priority conversion. [StepUpStatus](role-launcher/StepUpControl.tsx.md) presents the receipt model and any observed mode. The preview chips describe the base selection.


This account is bound to the candidate source, not a claim of a running serving build or a fresh execution/acceptance verdict. Existing historical accounts remain historical.

## Evidence


- Worker/Curator typed review census, record-only exclusion and unknown history. [4]

- The backend checks the explicit reason and the configured failed-review threshold. A step-up reads mode from its own settings row. Other launch fields follow the same-harness and model inheritance rule. [5]

- RoleLaunchFeatures retains settings-owned permissions and non-applied Base previews; feature labels match host IDs or labels without a built-in speed alias. [6]

- The instruction chip appears when notes are present and identifies their source and baseline treatment. [7]


- Permission dispatch preserves settings-owned chips; FeatureOverrideSelect owns selectable labels and hover. [1]


- The feature-value updater retains identities and removes only an empty override. [2]



- Ready ordinary defaults render the instructions chip. The preview branch labels the base mode and optional instructions as non-applied. [3]
