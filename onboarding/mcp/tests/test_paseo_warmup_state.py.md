# mcp/tests/test_paseo_warmup_state.py

## Governing Overview

[governing overview](overview.md)

## Purpose

After a host start the tree's agents load in the background, before a click (MIK-R145).

## Code Commentary

The claim cases assert one winner for the same exact host-start identity and admission of a new identity after the first claim closes. The separate injected-run case checks shared loading progress, click priority, and retained loaded/failed reasons without a real host. Tests assert only these named facets; they do not confer MEMORY, installation, lifecycle or broad performance acceptance.

## Boundaries

Local implementation and executable evidence do not replace requirement authority or the owning transaction. Retained source semantics and explicit unavailable/failure states remain binding.

## Evidence

- After a host start the tree's agents load in the background, before a click (MIK-R145). [1]
