# mcp/src/agents_remember/canvas/explainer_maintenance.py

## Governing Overview

[Route overview](../overview.md)

## Purpose

Updating, inspecting, retiring and cancelling an existing explainer seat.

## Code Commentary

An existing seat is updated, inspected, retired or cancelled here, and the same rules apply to all four: the seat's own manifest is the record of what it holds, and a retire reconciles the grades and counts it leaves behind rather than dropping them. Removal archives the chat and deletes the workspace.

## Boundaries

The detail this module owns stops at its own boundary; the route account above says what the surrounding surface promises.

## Evidence

- _reconcile_grades_and_counts reconciles what a retire leaves behind instead of dropping it. [1]
