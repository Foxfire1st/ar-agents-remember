# mcp/tests/test_tool_answer_guard.py

## Governing Overview

[Owning route overview](overview.md)

## Purpose

Guards bounded delivery, final measurement and shared-log failure handling at the production choke.

## Code Commentary

Cases pin exact envelope stripping, recursive list caps, code validation, fixed short-form fields and recovery arguments. Delivery is remeasured after attaching locations or late logging errors; observers and persisted lines agree with the delivered token count. Short/partial/stalled writes and concurrent writers are checked for complete records, parseable neighbors and counted losses. These tests describe the inherited answer/log contract; their presence supplies no fresh execution receipt.

## Evidence

No Domain Documentation sources are configured; the evidence below is repository implementation or test assertions, not a new execution attestation.

- Shaping and failure preservation are asserted at the choke. [1]
- Final delivered measurements include bookkeeping. [2]
- Partial and concurrent writes preserve record boundaries and counted losses. [3]
