# dashboard/src/panels/detail-panel/limit-time.test.ts

## Governing Overview

[panels overview](../overview.md)

## Purpose

The exact-reset detail is an exact served instant: date, seconds, milliseconds and time zone survive formatting.

## Code Commentary

Two resets inside one second must read as two different times, so the formatter keeps every field the server sent and writes any finer precision verbatim rather than rounding it. The case pins the shape of the rendered instant, not the clock that produced it.

**L184 — INV-XZYGEB.** The formatter this case exercises is the one the limited hover and detail render, so the precision claim lives in its test. The obligation this leaf records for this place is stated in the invariant named here; the card's earlier account of this file stands, and this paragraph adds what the change made true.
