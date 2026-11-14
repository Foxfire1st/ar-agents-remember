# dashboard/src/cockpit/tabMemory.test.ts

## Governing Overview

[overview](../overview.md)

## Purpose

Checks retained Operations targets against task hydration and exact owner identity.

## Code Commentary

The cases cover retained change-set variants, the three enclosure-scope aliases, missing tasks, surviving enclosures, cross-repository and cross-master identities, and task-bound worktrees. Pending hydration retains a target; a hydrated population without its owner dismisses it.

## Relationships

These assertions call the production tab hook with controlled store state. They record tested behavior, not a browser run or a new execution receipt.

## Evidence

- Checks retained Operations targets against task hydration and exact owner identity. [1]
