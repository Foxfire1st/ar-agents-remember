# mcp/tests/test_mcp_memory_bounded_stdio.py

## Governing Overview

[MCP Tests](overview.md)

## Purpose

Exercises the native stdio tool server's bounded-memory regression through the actual subprocess.

## Code Commentary

The test builds a paired fixture and runs one bound server through 84 calls in three cycles. It verifies that preview records are absent, matches the three applied weaknesses to the owning leaf history, and checks that the generated source brief exists and is excluded by the effective `/briefs/` rule. It writes a terminal receipt before asserting the existing limits for growth across the final two cycles, maximum post-call resident memory plus swap, and peak resident high-water mark.

## Relationships

The test calls the fixture builder, stdio driver and receipt reader. Its executable node is selected in the stress-durability evidence lane. Release certification selects that lane. The warm-index child and the measured server start without Coverage configuration so instrumentation does not alter the memory readings. [3]

## Evidence

- The test matches each of the three distinct applied weakness records to its cycle, revision, writer stamp and content digest in the owning leaf history. [1]
- The executable case checks workload completion, absent preview records, effective brief exclusion from Git and the existing memory bounds. [2]

- Release certification selects the stress case. The warm-index child and measured server start without child coverage. \[3] [3]
