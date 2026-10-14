# dashboard/src/data/conversation/format.test.ts

## Governing Overview

[data/conversation overview](overview.md)

## Purpose

Three retained Vitest cases declare the duration-formatting A1/A4 assertions: fixed sensible units, humanization of the two cited large-duration examples, and an em-dash for NaN/negative duration input. This is source assertion coverage, not a test run or whole formatting acceptance. The earlier six-case A1/A4/A5 account belongs to the predecessor formatter.

## Code Commentary

### Logic — what each case proves

- **Humanized durations, fixed precision (A4)** — `800 ms`, `45 s`, `3 m 12 s`, `2 h 5 m`, `6 d 0 h`
  are the exact expected outputs.
- **Never raw minutes / six-decimal seconds** — the developer-cited eyesores (`8638.1m`,
  `518288.173569s`) must humanize to a `d h` form; absent input → `ABSENT`.
- **Em-dash for invalid duration input (A1)** — `Number.NaN` / `-1` → `—`. Historical predecessor tests instead used undefined/unparseable dates with humanizeAge.
- **Historical removed case: `joinChips` dropped empties with one interpunct (A1/A2)** — `["codex", null, "working", undefined, ""]`
  → `"codex · working"`; empty input → `""` (no reassurance-zero cluster).
- **Historical removed case: long-stale degraded to a QUIET tone (A4)** — `freshnessTone("stale", 6-day)` → `stale` (calm),
  a brief lag → `aging`, unknown → `unknown`.
- **Historical removed case: boundary truncation kept the distinguishing tail (A5)** — `truncateMiddle` clips to `max`, keeps
  the ellipsis and the suffix; a short value is returned unchanged.

### Invariants And Boundaries

- Exact example strings and large-value pattern checks pin humanizeDuration only; they do not establish every L4 surface, removed formatting helper or runtime result. jsdom is unnecessary for these pure-function assertions.

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries are
configured. This one-to-one card therefore relies on its direct agents-remember source/tests and the
reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- The retained humanizeDuration presentation convention under test; earlier age/chip/freshness/truncation helpers and their cases are removed. [1]

- Three current source cases assert duration strings, large-value humanization and em-dash for NaN/negative values; this is no execution result. \[2] [2]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.
