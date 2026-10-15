# mcp/tests/test_background_accounting.py

## Governing Overview

[governing overview](overview.md)

## Purpose

The always-on background account (MIK-R81 rule 1): per-owner processor time and every wake.

## Code Commentary

The suite checks recorded unit lands in totals and window; unknown owner is kept not refused; negative samples clamp to zero; every wake is recorded with reason domains and paths; wake log is bounded and counts its drops; measured records thread cpu and wall. Tests assert only their named facets; they do not confer MEMORY, installation, lifecycle or broad performance acceptance.

The accounting-cost case measures calling-thread CPU with `time.thread_time()` for exactly 10,000 recorded units under the unchanged 0.5-second bound. It excludes scheduler waiting and does not establish installed processor share or a wall-time ceiling.

## Boundaries

Local implementation and executable evidence do not replace requirement authority or the owning transaction. Retained source semantics and explicit unavailable/failure states remain binding.

## Evidence

- The always-on background account (MIK-R81 rule 1): per-owner processor time and every wake. [1]

- The accounting-cost case measures calling-thread CPU with `time.thread_time()` for exactly 10,000 recorded units under the unchanged 0.5-second bound. It excludes scheduler waiting and does not establish installed processor share or a wall-time ceiling. [2]
