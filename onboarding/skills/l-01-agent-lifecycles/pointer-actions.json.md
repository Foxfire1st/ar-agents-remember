# skills/l-01-agent-lifecycles/pointer-actions.json

## Governing Overview

[Overview](overview.md)

## Purpose

Declares admitted pointer actions and their authored routing and grouping exceptions.

## Code Commentary

Action identity and exception membership are authoring decisions. The policy does not cache the current sentence text: generated wording is held in pointer-actions-derived.json. Renewal may refresh wording but does not manufacture another admitted action or exception.

## Relationships

The pointer renewal planner validates these declarations and matches their current source actions. Pointer-policy test support projects them into assertion inputs.

## Evidence


- The policy stores authored action admissions and exception groups. [1]
