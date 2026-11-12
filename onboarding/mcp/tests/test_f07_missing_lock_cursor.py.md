# mcp/tests/test_f07_missing_lock_cursor.py

## Governing Overview

[mcp/tests route overview](overview.md)

## Purpose

Proves the write-free browser contract for the workspace river read (MIK-R114 rule 7):
a stream with no lockfile reads without creating any observer file, and a read racing a
cut never replays nor loses a row.

## Code Commentary

The module pins the missing-lock branches: interposed cuts between base snapshot, file
read and post-check converge without replay or loss; bursts past the old bound surface
coherently; concurrent cuts during a protected read wait; unopenable or vanished lockfiles
and failed shared locks return no rows with the caller cursor unchanged; and a lockless
clean read returns its first observation only when no writer came into being.

## Evidence

- Missing-lock reads create no observer file and lose no row. [1]
- Failed locks return empty with the cursor unchanged. [2]
