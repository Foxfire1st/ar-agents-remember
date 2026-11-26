# mcp/src/agents_remember/canvas/canvas-interactive-report.mjs

## Governing Overview

[Route overview](overview.md)

## Purpose

Runs the renderer’s advisory sweep over a staged draft.

## Code Commentary

The shipped renderer runs an advisory sweep with click and keyboard at wide and narrow widths. It reports observed outcomes and what the deadline leaves unvisited, keeps available pictures and can resume observations for the same staged draft.

## Boundaries

The obligation above is the whole of what this file must keep true; the route account says what the surrounding surface promises.

## Evidence

- Four advisory width and input-method passes exercise initial controls and record those a deadline left unvisited. [1]

- A matching staged draft can resume completed ordinary passes and retain earlier observed controls from partial passes. Retired effects-off passes are excluded. [2]
