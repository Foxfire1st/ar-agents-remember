# dashboard/src/panels/detail-panel/directGrantControl.test.tsx

## Governing Overview

[Nearest governing overview](../overview.md)

## Purpose

Pins mounted grant controls on both master rows and directly selected leaf plans.

## Contract

The tests distinguish granted/ungranted badges, giver and give/revoke affordances; assert the developer route body and refusal notice; retain the actual grant after a refused revoke; and exercise live projection and selection changes. Mocked responses are UI witnesses, not store mutations or live-host qualification.

## Evidence

- Pins mounted grant controls on both master rows and directly selected leaf plans [1]
