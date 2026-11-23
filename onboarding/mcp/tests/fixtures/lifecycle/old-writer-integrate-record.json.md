# mcp/tests/fixtures/lifecycle/old-writer-integrate-record.json

## Governing Overview

[MCP Tests](../../overview.md)

## Purpose

This recording preserves the schema 3.0 integration journal emitted by the old lifecycle store at code commit `fcb1e3645040b00998912e0cfece35ccd116d4a3`.

## Code Commentary

The old writer accepted a synthetic running worker binding and an inconclusive termination outcome. The retained journal is readable as integration history at its recorded generation. After decoding, the public refusal names `worktree_integrate` with the live enclosure contract path.

## Relationships

`test_lifecycle_operation_public_boundary.py` owns the permanent recording and verifies the exact bytes through the journal store and public control. `test_lifecycle_operation_journal_retired.py` uses it in the registered status case. The lifecycle catalog records provenance and exact consumers.

## Evidence

- The lifecycle catalog pins the integration fixture to the old store and documents its synthetic termination outcome. [1]
- The registered boundary test reads the original bytes, checks the refusal and verifies that the journal remains unchanged. [2]
