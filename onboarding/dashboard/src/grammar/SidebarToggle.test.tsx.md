# dashboard/src/grammar/SidebarToggle.test.tsx

## Governing Overview

[Route overview](overview.md)

## Purpose

Specify the shared toggle’s native activation/accessibility and per-page visibility persistence.

## Code Commentary

### Logic

The button case asserts name, expanded/controls/title, side-aware open band, click/Enter/Space activation and closed right-side presentation.

The hook case stores only the chosen knowledge left-side key, restores it on remount, and shows that review right-side remember:false never writes visibility storage.

### Invariants And Boundaries

It covers the shared primitive, while mounted page placement is exercised by sidebarToggle.pages and review-specific tests.

## Evidence

- Button accessibility and activation [1]
- Independent persistence and review exception [2]
