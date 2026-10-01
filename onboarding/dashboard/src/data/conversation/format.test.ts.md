# dashboard/src/data/conversation/format.test.ts

## Governing Overview

[data/conversation overview](overview.md)

## Purpose

The proof that `format.ts` honors the developer visual-findings conventions A1/A4/A5 as product
truth, not aspiration. Six vitest cases pin the exact display strings so a regression that reintroduces
raw minutes, six-decimal seconds, dash-chains, or an alarm-toned long-stale value fails the gate.

## Code Commentary

### Logic — what each case proves

- **Humanized durations, fixed precision (A4)** — `800 ms`, `45 s`, `3 m 12 s`, `2 h 5 m`, `6 d 0 h`
  are the exact expected outputs.
- **Never raw minutes / six-decimal seconds** — the developer-cited eyesores (`8638.1m`,
  `518288.173569s`) must humanize to a `d h` form; absent input → `ABSENT`.
- **Em-dash for a genuinely absent value (A1)** — `undefined` / unparseable dates → `ABSENT`, never a
  chain.
- **`joinChips` drops empties with one interpunct (A1/A2)** — `["codex", null, "working", undefined, ""]`
  → `"codex · working"`; empty input → `""` (no reassurance-zero cluster).
- **Long-stale degrades to a QUIET tone (A4)** — `freshnessTone("stale", 6-day)` → `stale` (calm),
  a brief lag → `aging`, unknown → `unknown`.
- **Boundary truncation keeps the distinguishing tail (A5)** — `truncateMiddle` clips to `max`, keeps
  the ellipsis and the suffix; a short value is returned unchanged.

### Invariants And Boundaries

- These are exact-string assertions: they are the contract that every L4 surface renders one product
  vocabulary. jsdom is unnecessary (pure functions).

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries are
configured. This one-to-one card therefore relies on its direct agents-remember source/tests and the
reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- The presentation conventions under test. [1]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.
