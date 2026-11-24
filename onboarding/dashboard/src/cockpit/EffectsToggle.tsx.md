# dashboard/src/cockpit/EffectsToggle.tsx

## Governing Overview

[Governing overview](../overview.md)

## Purpose

The button controls the dashboard document’s effects preference.

## Code Commentary

The component reads the current document state on mount. Its handler sets `data-effects` on the dashboard document and persists the preference in `calm-cockpit`.

## Relationships

Cockpit mounts the toggle. The explainer frame uses the standalone page binding.

## Evidence

- Dashboard effect state and persistence are owned by the toggle. [1]
