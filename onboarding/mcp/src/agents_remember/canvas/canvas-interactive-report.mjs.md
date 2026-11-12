# mcp/src/agents_remember/canvas/canvas-interactive-report.mjs

## Governing Overview

[Route overview](../overview.md)

## Purpose

Tooling, not product: the interactive report the renderer runs over a draft.

## Code Commentary

This is build tooling rather than shipped product. It exercises every initially present control of a canvas draft at two widths, by click and by keyboard, and writes the statuses and pictures the render's interaction report carries. If it stops, a draft's dead control ships inside a render that reports itself as exercising everything: the failure surfaces two steps later, in a page a reviewer cannot operate.

## Boundaries

The obligation above is the whole of what this file must keep true; the route account says what the surrounding surface promises.

## Evidence

- Every initially present control is exercised at both widths, so a control that does nothing cannot pass as covered. [1]

- A control found in an earlier pass is not re-exercised at the cost of one never reached. [2]
