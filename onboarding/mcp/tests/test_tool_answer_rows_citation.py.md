# mcp/tests/test_tool_answer_rows_citation.py

## Governing Overview

[Owning route overview](overview.md)

## Purpose

Derives citation answer-row cases from converted-memory tool paths and asserts delivery bounds.

## Code Commentary

Temporary paired repositories exercise converted sidecar anchors and citation-table authoring. Missing-path anchors produce ten slim `stale` entries carrying `path` and `message`; a cardless malformed sidecar fails the run with `refusedCount=0`. The two-document helper binds a frozen snapshot. Separate malformed-sidecar authoring checks unreadable results. Each projected result is checked against the authored field/use contract and real choke; pathological long stale paths must trigger the generic over-bound guard. Test presence and retained old results do not establish a new production run.

## Evidence

No Domain Documentation sources are configured; the evidence below is repository implementation or test assertions, not a new execution attestation.


### Current Source-Inspection References

- Converted citation tests assert clean, stale, unreadable-sidecar and two-document projections, plus bounded delivery and pathological overflow control. [1]
