# dashboard/src/panels/detail-panel/limitTime.ts

## Governing Overview

[Panels overview](../overview.md)

## Purpose

Format a served instant exactly for the dashboard's details and hovers: date, seconds, milliseconds and the reader's time zone.

## Code Commentary

`formatLimitTime(iso)` parses the served ISO string and writes it with `LIMIT_TIME`, an `Intl.DateTimeFormat` in the reader's locale with day, short month, year, 24-hour hour, minute and second, three fractional digits and the short time-zone name. Seconds and milliseconds are kept because served moments are exact: two resets a minute or a millisecond apart read as different times. When the served fraction is finer than a millisecond (`SUB_MILLISECOND`) and its digits past the third are not all zero, the served string is written verbatim after the localized time as `(served <iso>)`, so the producer's precision is never rounded off. An unparsable string is returned as served. The module only formats; it never decides that a limit or a wait exists.

## Relationships

`pageParts.tsx` writes the limited seat lines, a limit's end and the no-clock status title through it; `waitWords.ts` writes a waiting seat's start and check due through it; `tray/TraySent.tsx` writes a held delivery's limit end through it. `limit-time.test.ts` pins its precision, and the limit and wait suites compare their hovers against its output.

## Evidence

- The formatter keeps date, seconds, three fractional digits and the time-zone name. [1]
- A finer, nonzero served fraction is written verbatim beside the localized time; an unparsable string is returned as served. [2]
- The pattern that finds a fraction longer than three digits. [3]
- The limited seat lines write each reset through it. [4]
- The wait lines write the wait's start and check due through it. [5]
- The tray writes a held delivery's limit end through it. [6]
