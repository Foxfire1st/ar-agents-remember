# mcp/src/agents_remember/application/record_standing_answers.py

## Governing Overview

[Governing overview](overview.md)

## Purpose

Projects a selected memory index's record state and writer into knowledge-reader answers.

## Code Commentary

Record summaries expose recordState and a writer with role, harness and model. Source-context rows use a compact role/model writer and keep their source currentness under state. The single-record reply also carries compact standing fields at the top level, where they remain available in its bounded answer.

## Relationships

The reader supplies the selected knowledge index. Summary links use a batched standing lookup, and each source-context projection reuses standings already read while sizing the page.

## Evidence

- The full record representation carries the separate revision state and writer fields. [1]
- The record answer repeats both in compact top-level fields. [2]
- Row projection reuses the index results for records it has already seen. [3]
