# mcp/tests/fixtures/l109_tool_answers/read_ar_files_largest.json

## Governing Overview

[Owning route overview](../../overview.md)

## Purpose

Preserve the operation-produced compact reply for the largest-case read_ar_files answer-table scenario.

## Code Commentary

The fixture has twenty governed paths in converted leaf memory. Each compact row records the source path, existence, card status and a brief path relative to the reported memory root. The omission message directs the reader to that brief.

The answer-table tests consume these exact fixture bytes. Production versus recorded provenance and regeneration belong to PROVENANCE.md and the test producer, not manual edits of identities, tokens or output counts. No secret or current operational credential is represented by these static values.

## Evidence





- The twenty compact rows name each source, existence, card status and relative brief pointer with missing freshness. The answer explains how a covering write renews the saved brief. [1]
