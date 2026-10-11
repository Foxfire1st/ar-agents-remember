# dashboard/src/cockpit/RoleLaunchFeatures.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

Renders host-offered feature controls and mode/instruction chips for the single role launcher, with provenance in each control's hover text rather than a running defaults sentence.

## Code Commentary

`FeatureControl` uses the shared `launcherSelect` for a non-permission feature, with the role-default option first and the complete selected label plus default provenance in `title`. A permission-bearing feature is a shared `launcherChip` naming its value; its hover points to the user's settings and it offers no override control. `RoleLaunchFeatures` maps all features of the selected model, keeps explicit values in the agent override, and drops the override only when no explicit value or identity remains.

Once options are ready, `RoleLaunchDefaults` renders the host-labelled mode chip; its hover carries mode provenance and the host description. A foreign agent shows `At start`, with the resolution explanation in hover. An `Instructions` chip appears only when notes are present; its hover names their source and whether they replace or add to the baseline. Agent/model/effort provenance belongs to the corresponding selectors in `RoleLauncher`, not to a defaults line here. These are display changes, not permission or payload changes.

## Evidence

- Feature controls share the launcher look; permission values stay settings-owned chips, while selectors retain complete selected labels and default provenance. [1]
- Explicit feature values and identities remain in the override; an empty override is removed. [2]
- Mode and optional instruction chips replace the defaults sentence and carry provenance in hover. [3]
