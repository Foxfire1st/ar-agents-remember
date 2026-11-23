# dashboard/src/cockpit/role-launcher/roleLauncherFields.ts

## Governing Overview

[Dashboard source overview](../../overview.md)

## Purpose

Shared wrapper styles for selectors in the role launcher.

## Code Commentary

The shared field wrapper establishes the grid, auto basis and minimum width. Agent, model and effort wrappers cap at 10rem. The mode wrapper caps at 17rem for the label and source. The variants have the same flex shrink and their own wide-viewport minimum widths.

## Relationships

[RoleLauncher](RoleLauncher.tsx.md) and [ModeOverrideSelect](ModeOverrideSelect.tsx.md) use the wrappers. The launcher grid owns row wrapping. The shared `viewTabLook` selector recipe supplies the control styling.

## Evidence


- The shared field uses a grid wrapper. The two override variants have the same shrink factor, with different caps and wide-viewport minimum widths. [1]


- The row wraps its child controls. [2]
