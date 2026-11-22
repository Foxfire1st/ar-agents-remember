# mcp/tests/test_agent_eval_adapters.py

## Governing Overview

[governing overview](overview.md)

## Purpose

Native adapter schemas, exact session discovery, host events and dispatch recovery are the subject of this regression module.

## Code Commentary

### Invariants And Boundaries

The source declares controlled assertions and retained-data scenarios. Reading this card establishes neither a fresh test run nor native host or model acceptance.

The archived-Hermes cases construct synthetic SQLite session/message rows. They assert unique archived actions in live and retained replay, active-copy and repeated-archive deduplication, the missing-id call_id alias, malformed-present-id and partial-copy unknowns, archived dispatcher normalization, context-only compaction summaries and active terminal-stop scope. Retained server-placement cases forbid Path.open during replay, preserve raw records/export/source bindings and unrelated failures, and check idempotent direct/opaque placement reconstruction. These source assertions are not a retained native v0.21.7 capture or a fresh test result.

The native identity discovery case creates its project under a short temporary root. Paseo flattens the absolute project path into one filename component, so the case owns that width while exercising fresh, stale and ambiguous records.

## Evidence


- The source defines the adapter fixtures and their asserted boundaries. [1]


- The native identity discovery case creates its project under a short temporary root. Paseo flattens the absolute project path into one filename component, so the case owns that width while exercising fresh, stale and ambiguous records. [2]
