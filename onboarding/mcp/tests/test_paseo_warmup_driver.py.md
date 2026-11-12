# mcp/tests/test_paseo_warmup_driver.py

## Governing Overview

[governing overview](overview.md)

## Purpose

After a host start the tree's agents load in the background, before a click (MIK-R145).

## Code Commentary

The suite checks a blocked resume cancels and drains; a new start retires the driving pass; an unreachable host ends the driving pass with its record; the concurrency cap stays two; blocked worker resumes drain on handoff and cap holds; driver handoff waits out blocked workers before successor. Tests assert only their named facets; they do not confer MEMORY, installation, lifecycle or broad performance acceptance.

## Boundaries

Local implementation and executable evidence do not replace requirement authority or the owning transaction. Retained source semantics and explicit unavailable/failure states remain binding.

## Evidence


- After a host start the tree's agents load in the background, before a click (MIK-R145). [1]
