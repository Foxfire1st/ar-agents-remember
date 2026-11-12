# mcp/tests/test_serving_owner_units.py

## Governing Overview

[governing overview](overview.md)

## Purpose

F01/F02: concrete projection, event-tail and warmup unit graphs.

## Code Commentary

The suite checks each wake keeps its exact reason, domains and paths on failed ticks; real projection ticks account for success, failure and repeated cancellation; tail reads and serialization have exact units and drain actual readers; warmup shares one ledger across callbacks and drained resumes; landing discovery, probes and publication retain attribution. Startup and teardown share the same ledger, with startup failure and repeated cancellation exercised on retained river compaction. The removed native conversation reader and identity-migration stages are not current cases. Tests assert only their named facets; they do not confer MEMORY, installation, lifecycle or broad performance acceptance.

## Boundaries

Local implementation and executable evidence do not replace requirement authority or the owning transaction. Retained source semantics and explicit unavailable/failure states remain binding.

## Evidence


- Retained projection, event-tail, warmup, landing and startup/teardown cases check executing-thread attribution and drain; startup failure/cancellation uses river compaction, and retired native-conversation/migration stages are absent. [1]
