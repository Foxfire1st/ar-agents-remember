# dashboard/src/tray/trayShell.test.tsx

## Governing Overview

[Route overview](overview.md)

## Purpose

Checks shell tray composition and review-column first-target behavior.

## Code Commentary

### Logic

Tray button stays outside four radio views; dock is beside stable frame; river switches dock to corner without changing generation; Chats uses own column; review pick minimizes without opening column; explicit expansion opens column and resolves default; explicit choice and leaving cancel the pending default.

CockpitShell with stubbed review surface containing a real AddToTray and mocked frame/document-chat/seat reads.

### Invariants And Boundaries

Stand-in review does not establish full review surface behavior or browser geometry; source identity/generation assertions are DOM level.

## Evidence

- Checks shell tray composition and review-column first-target behavior. [1]
- Checks shell tray composition and review-column first-target behavior. [2]
- Checks shell tray composition and review-column first-target behavior. [3]
- Checks shell tray composition and review-column first-target behavior. [4]
