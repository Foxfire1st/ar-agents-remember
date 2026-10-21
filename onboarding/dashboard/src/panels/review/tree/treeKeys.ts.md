# dashboard/src/panels/review/tree/treeKeys.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

ArrowUp/Down wrap focus across shown tree rows including pinned rows, prevent page focus scroll and reveal row in tree.

## Code Commentary

### Logic

ArrowUp/Down wrap focus across shown tree rows including pinned rows, prevent page focus scroll and reveal row in tree. Enter/Space remain native button selection; block j/k is another owner.

### Invariants And Boundaries

This file consumes comparison and owner state; it does not author knowledge or decide task acceptance.

## Evidence

- ArrowUp/Down wrap focus across shown tree rows including pinned rows, prevent page focus scroll and reveal row in tree. [1]
- ArrowUp/Down wrap focus across shown tree rows including pinned rows, prevent page focus scroll and reveal row in tree. [2]
