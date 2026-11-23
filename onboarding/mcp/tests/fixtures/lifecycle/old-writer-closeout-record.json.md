# mcp/tests/fixtures/lifecycle/old-writer-closeout-record.json

## Governing Overview

[MCP Tests](../../overview.md)

## Purpose

This recording preserves the schema 3.0 closeout request and journal shape emitted by the older lifecycle models at code commit `fcb1e3645040b00998912e0cfece35ccd116d4a3`.

## Code Commentary

The synthetic closeout keeps its certification and code-leg preparation, including the historical create, materialize and commit commands. The current reader preserves the leg's intent and output and discards the retired command bodies. An addressable record directs callers to the synchronous closeout tool.

## Relationships

`test_lifecycle_operation_journal_retired.py` owns the permanent recording and verifies its digest and decoding. `test_lifecycle_operation_public_boundary.py` uses the same bytes at the registered control boundary. The lifecycle catalog records the old-build provenance and exact consumers.

## Evidence

- The lifecycle catalog pins the recording to the old writer, its digest and its exact consumers. [1]
- The reader keeps the recorded generation and prepared output and drops the command bodies. [2]
