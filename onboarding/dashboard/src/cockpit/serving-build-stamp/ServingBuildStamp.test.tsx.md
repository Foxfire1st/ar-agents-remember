# dashboard/src/cockpit/serving-build-stamp/ServingBuildStamp.test.tsx

## Governing Overview

[overview](../../overview.md)

## Purpose

Component tests for the serving-build stamp: an absent build renders nothing, the boot stamp keeps its legacy text and tooltip, and build currentness updates the stamp without replacing the boot identity.

## Code Commentary

The cases render `ServingBuildStamp` against the shared `dashboardStore`, reset before each case. One case sets only a dirty serving build whose client bundle differs and checks the `hash*` text, the dirty and boot-time tooltip, the mismatch hint and the absence of a currentness attribute. One case feeds `current`, `stale` and `unknown` through the store's `buildCurrentness` delta and checks the state text, the digests, first-seen time, remedy and process id in the tooltip, and that the stored `servingBuild` object is unchanged. One case sets checkout mode with an unknown state and checks that the reason is shown and that no digest is invented.

## Evidence

- An absent build renders nothing; a build alone keeps the legacy stamp and sets no currentness attribute. [1]
- Each currentness state arrives through the store delta and leaves the boot identity unchanged. [2]
- Checkout mode with an unknown state shows the reason and no digest. [3]
