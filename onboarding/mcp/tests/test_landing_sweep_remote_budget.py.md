# mcp/tests/test_landing_sweep_remote_budget.py

## Governing Overview

[governing overview](overview.md)

## Purpose

MIK-R81 rule 6 (F12): one ls-remote per repository and ref per landing sweep.

## Code Commentary

The suite checks shared origin branches probe once per sweep at two fleet sizes; broken remote fails once per sweep and refreshes next sweep. Tests assert only their named facets; they do not confer MEMORY, installation, lifecycle or broad performance acceptance.

## Boundaries

Local implementation and executable evidence do not replace requirement authority or the owning transaction. Retained source semantics and explicit unavailable/failure states remain binding.

## Evidence

- MIK-R81 rule 6 (F12): one ls-remote per repository and ref per landing sweep. [1]
