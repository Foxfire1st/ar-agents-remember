# mcp/tests/test_agent_eval_adapters.py

## Governing Overview

[governing overview](overview.md)

## Purpose

Native adapter schemas, exact session discovery, host events and dispatch recovery are the subject of this regression module.

## Code Commentary

### Invariants And Boundaries

The source declares controlled assertions and retained-data scenarios. Reading this card establishes neither a fresh test run nor native host or model acceptance.

The added archived-Hermes cases construct synthetic SQLite session/message rows. They assert unique archived actions in live and retained replay, active-copy and repeated-archive deduplication, the missing-id call_id alias, malformed-present-id and partial-copy unknowns, archived dispatcher normalization, context-only compaction summaries and active terminal-stop scope. Retained server-placement cases forbid Path.open during replay, preserve raw records/export/source bindings and unrelated failures, and check idempotent direct/opaque placement reconstruction. These source assertions are not a retained native v0.21.7 capture or a fresh test result.

## Evidence

- The source defines this file's responsibility and the boundaries described here. [1]
