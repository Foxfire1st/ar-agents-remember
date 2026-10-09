# mcp/tests/test_tool_event_river.py

## Governing Overview

[mcp/tests route overview](overview.md)

## Purpose

The retained unit-regression surface for the host-path Event River feed (MIK-R114):
first-call write with caller and facts, read-once caller, no content leakage, the 120-char
omission, target roles, single legacy write, drop carry-then-clear, failed removal, the
per-append bound, oversized-row refusal, packet constants, one cut function, and the
silent-stream last feed.

## Code Commentary

`ToolEventRiverTests` pins each feed behavior against the workspace river: the bound
first call writes one event with caller and facts; the caller snapshot stays fixed; no
argument, answer or message text reaches an event; role tools name the started or
addressed role including id-addressed receipts; an active lifecycle writes once with no
second river row; failed writes answer as written while the count rides the next event
and clears after success; every append lands at or under the 16 MiB ceiling with the
shared age/size cut; and a connected stream changes no file while naming the last feed.

## Evidence

- The river test class pins each feed behavior end to end. [1]
- Bound first call writes one event with caller and facts. [2]
- Every append lands at or under the ceiling. [3]
