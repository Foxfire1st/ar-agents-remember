# mcp/src/agents_remember/canvas/explainer_answer_bounds.py

## Governing Overview

[Route overview](../overview.md)

## Purpose

Each explainer tool's answer bound, and where an answer that passes it goes.

## Code Commentary

Every explainer tool answer is held to the explainer's own bound table, counted with the product's counter the way the general tool answers are counted, and the bound is not changed by this module. An answer over its bound is not cut: it is written whole to the workspace's `scratch/answers/` and the reply names that file, so a long answer costs a path rather than a truncated claim. The explainer surface is four tools - `render`, `define_category`, `remove_category` and `grade` - and no tool that reads the workspace back.

## Boundaries

The detail this module owns stops at its own boundary; the route account above says what the surrounding surface promises.

## Evidence

- answer_tokens and bounded decide the bound and whether an answer passes it. [1]

- write_scratch writes an over-bound answer into the workspace instead of truncating it. [2]

- The four tools it bounds are the whole surface; no read-back tool exists to bound. [3]
