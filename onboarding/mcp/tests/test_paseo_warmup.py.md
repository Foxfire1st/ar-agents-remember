# mcp/tests/test_paseo_warmup.py

## Governing Overview

[governing overview](overview.md)

## Purpose

After a host start the tree's agents load in the background, before a click (MIK-R145).

## Code Commentary

The suite checks a failed intake does not consume the start; a restart then poll reruns and a repeat poll does not; a new server id starts without any outage; a restart after completion requalifies and a reread does not; a different process birth requalifies without an outage; one successor per restart across two servers. Tests assert only their named facets; they do not confer MEMORY, installation, lifecycle or broad performance acceptance.

## Boundaries

Local implementation and executable evidence do not replace requirement authority or the owning transaction. Retained source semantics and explicit unavailable/failure states remain binding.

## Evidence

- After a host start the tree's agents load in the background, before a click (MIK-R145). [1]
