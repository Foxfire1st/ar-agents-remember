# mcp/src/agents_remember/serving/paseo/provider_limits.py

## Governing Overview

[Serving overview](../overview.md)

## Purpose

The product's one judgement and one writer of `provider-limits.json`, beside `role-agents.json`.

## Code Commentary

A seat is limited, and until when, by Paseo's usage report for that seat and by nothing else: no chat text, no error string, no turn failure kind. This module judges one read and keeps one fact per report id, which every reader of the file then reads.

The judgement is conservative. A fact is set only by a successful report and an `unavailable` read never clears one; the one exception is Paseo 0.16.2's `lastSuccessful`. An `error` entry can carry the login's latest available report, which the product judges with its own fetch time. A report holds work only on an exhausted account-wide window with a future reset, and an enabled extra usage or a positive credits balance releases the seat.

The file is written whole and atomically under an exclusive lock, so a reader never sees a partial record. Drops are part of the same write: an entry whose `until` has passed, and an agent that left the role record, are not carried forward. Where the settings name no Paseo runtime, nothing is read or written.

A live report is read again when five minutes have passed since its observation or its last recorded attempt. `claim_due_reports` records the attempt under the file lock before the host call, so one claimed report survives a fresh snapshot and a failed read does not postpone the next recheck; a report whose reset has passed is dropped, and an agent that left the role record is pruned with the same write.

An early release is written as a `clearedSeats` entry: the seat, the moment the last live report that held it left the file, and that report's old deadline. The marker stays while the seat is in the role record, while the old deadline plus sixty seconds has not passed, and while no limit holds the seat again; the plugin reads it to release a pending resume or parent flush without waiting for that deadline.

## Evidence

- An error entry can carry the newest available report. The judgment uses that report and its recorded fetch time. [1]

- One due attempt is claimed under the file lock before the read, and a fresh snapshot keeps the claim. [2]
- An early clear names the seat and the old deadline, and is kept only while the seat remains eligible and no limit returns. [3]
