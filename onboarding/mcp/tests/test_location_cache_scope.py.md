# mcp/tests/test_location_cache_scope.py

## Governing Overview

[governing overview](overview.md)

## Purpose

MIK-R81 rule 3 (F14): the warm location cache authenticates what it serves.

## Code Commentary

The suite checks wrong root never serves another checkout; a fill racing manifest deletion can return its already-resolved location, while the subsequent read refuses the missing manifest; locator created after adoption required is seen; served locations are copies; mid read rewrite retries to consistent bytes; persistent mid read change fails closed. Tests assert only their named facets; they do not confer MEMORY, installation, lifecycle or broad performance acceptance.

## Boundaries

Local implementation and executable evidence do not replace requirement authority or the owning transaction. Retained source semantics and explicit unavailable/failure states remain binding.

## Evidence

- MIK-R81 rule 3 (F14): the warm location cache authenticates what it serves. [1]
