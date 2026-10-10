# dashboard/src/cockpit/RoleLaunchFeatures.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

Renders host-offered speed controls and visible launch defaults with their provenance for the single role launcher.

## Code Commentary

`FeatureControl` renders one host-provided feature: a permission-bearing feature shows its label, default and a user-settings pointer with no control, while a speed feature offers a select of its host options around the role default. `RoleLaunchFeatures` maps the selected model's features, keeps explicit values in the agent override, and drops the override when no explicit value or identity remains. `RoleLaunchDefaults` shows the applied mode with its source, the agent/model/effort sources, the feature sources and the instruction provenance (baseline replaced or added) once options are ready.

## Evidence

- The permission-bearing feature renders settings-owned text with no override control. [1]
- The speed feature renders the host option select around the role default. [2]
- The defaults line carries mode, choice sources and instruction provenance. [3]
