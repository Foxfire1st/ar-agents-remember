# mcp/tests/test_projection_failure_retry.py

## Governing Overview

[governing overview](overview.md)

## Purpose

F05/F06: real projection reads, publication failures and drained tick retries.

## Code Commentary

The suite checks before and after each reader failure retries complete projection; two sizes two heals recover lost markers through failed full; repeated cancel drains actual tick and retains arrivals and rest. Tests assert only their named facets; they do not confer MEMORY, installation, lifecycle or broad performance acceptance.

## Boundaries

Local implementation and executable evidence do not replace requirement authority or the owning transaction. Retained source semantics and explicit unavailable/failure states remain binding.

## Evidence

- F05/F06: real projection reads, publication failures and drained tick retries. [1]
