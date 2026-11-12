# dashboard/src/panels/detail-panel/limit-time.test.ts

## Governing Overview

[panels overview](../overview.md)

## Purpose

The exact-reset detail is an exact served instant: date, seconds, milliseconds and time zone survive formatting.

## Code Commentary

Two resets inside one second must read as two different times, so the formatter keeps every field the server sent and writes any finer precision verbatim rather than rounding it. The case pins the shape of the rendered instant, not the clock that produced it.

**INV-XZYGEB.** The formatter this case exercises, `formatLimitTime` in `limitTime.ts`, is the one the limited hover and detail render, so the precision claim lives in its test.
