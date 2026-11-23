# mcp/tests/test_mcp_memory_bounded_stdio.py

## Governing Overview

[MCP Tests](overview.md)

## Purpose

Exercises the native stdio tool server's bounded-memory regression through the actual subprocess.

## Code Commentary

The test builds a paired fixture, runs one bound server through 84 calls, verifies the three cycle-specific persisted weakness records and writes a terminal receipt before asserting the memory limits. It measures growth across the final two cycles, maximum post-call resident memory plus swap, and peak resident high-water mark.

## Relationships

The test calls the fixture builder, stdio driver and receipt reader. Its executable node is selected in the stress-durability evidence lane. Release certification selects that lane. The warm-index child and the measured server start without Coverage configuration so instrumentation does not alter the memory readings. [3]

## Evidence

- The test verifies the persisted records from the three applied writes. [1]
- The executable case checks workload completion and memory bounds. [2]

- Release certification selects the stress case. The warm-index child and measured server start without child coverage. \[3] [3]
