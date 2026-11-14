# dashboard/src/cockpit/tabMemory.ts

## Governing Overview

[overview](../overview.md)

## Purpose

Keeps the Operations view when the reader visits another bottom tab and validates that view when the reader returns.

## Code Commentary

Pressing Operations while already there returns to the task view. A round trip through another tab retains the task, change set, review or notes document. After task hydration, a missing owner dismisses its retained view. Membership in the served task population establishes existence; a surviving enclosure alone does not. Pending hydration retains the view.

## Relationships

The shell supplies its current view and setters. Review addresses are parked while another tab is visible and restored on return. These callbacks preserve in-session state; they do not add browser-reload persistence.

## Evidence

- Keeps the Operations view when the reader visits another bottom tab and validates that view when the reader returns. [1]
