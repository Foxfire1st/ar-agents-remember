# dashboard/src/tray/trayStore.ts

## Governing Overview

[Route overview](overview.md)

## Purpose

Owns collection admission, first-target decision and send settlement.

## Code Commentary

### Logic

Deduplicates before adding; validates image/count/message bounds before persistence; chooses the first source/shown chat once unless explicit targets override; supports note/removal/close/minimize, and snapshots Send. Full success removes snapshot picks; partial refusal keeps them and selects failed targets; concurrent new picks survive.

### Invariants And Boundaries

No role creation or navigation. Storage errors keep live data with a warning. Later asynchronous held loss is recovered through files/log, not automatic browser restoration.

## Evidence

- Owns collection admission, first-target decision and send settlement. [1]
- Owns collection admission, first-target decision and send settlement. [2]
- Owns collection admission, first-target decision and send settlement. [3]
