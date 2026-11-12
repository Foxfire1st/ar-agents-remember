# mcp/src/agents_remember/serving/paseo/provider_limits.py

## Governing Overview

[Serving overview](../overview.md)

## Purpose

The product's one judgement and one writer of `provider-limits.json`, beside `role-agents.json`.

## Code Commentary

A seat is limited, and until when, by Paseo's usage report for that seat and by nothing else: no chat text, no error string, no turn failure kind. This module judges one read and keeps one fact per report id, which every reader of the file then reads.

The judgement is conservative. A fact is set only by a successful report and an `unavailable` read never clears one; the one exception is Paseo's `lastSuccessful` (0.12.0 to 0.15.4), where an `error` entry carries the newest available report of that login and that report is judged as itself. A report holds work only on an exhausted account-wide window with a future reset, and an enabled extra usage or a positive credits balance releases the seat.

The file is written whole and atomically under an exclusive lock, so a reader never sees a partial record. Drops are part of the same write: an entry whose `until` has passed, and an agent that left the role record, are not carried forward. Where the settings name no Paseo runtime, nothing is read or written.
