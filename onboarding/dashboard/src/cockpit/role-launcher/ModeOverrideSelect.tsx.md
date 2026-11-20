# dashboard/src/cockpit/role-launcher/ModeOverrideSelect.tsx

## Governing Overview

[Dashboard source overview](../../overview.md)

## Purpose

The role launcher’s permission-mode selector displays the chosen harness’s offers and carries an explicit mode as a launch override.

## Code Commentary

The empty first option names the mode the start takes when the operator makes no choice and identifies its source. An explicit choice selects its harness mode ID and leaves the first option intact. An explicit ID that disappears from the offers remains visible as “no longer listed”. The selector is disabled while options are unavailable or loading, no agent resolves, the launcher is busy, or a retry locks the row.

## Relationships

[roleLauncherDisplay](roleLauncherDisplay.ts.md) supplies the default and offers. A mode change preserves the selected agent, model, effort and feature overrides through [roleLaunchModel](../roleLaunchModel.ts.md). The host judges whether the requested mode applies.

## Evidence

- The first option labels the default and its source. The selected value and missing-offer option retain an explicit mode. [1]
- Changing the mode updates the launch override and carries the model, effort and feature values. [2]
