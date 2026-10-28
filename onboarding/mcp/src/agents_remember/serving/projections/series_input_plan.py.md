# mcp/src/agents_remember/serving/projections/series_input_plan.py

## Governing Overview

[Route overview](../overview.md)

## Purpose

Exact work-branch ref inputs for the existing projection watch plan.

## Code Commentary

The watch plan names the exact work-branch ref files a series projection depends on, so a change to another ref does not invalidate the projection and a change to one of these does.

## Boundaries

The detail this module owns stops at its own boundary; the route account above says what the surrounding surface promises.

## Evidence

- work_branch_ref_paths names the exact ref inputs the plan watches. [1]
