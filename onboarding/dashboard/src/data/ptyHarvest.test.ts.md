# dashboard/src/data/ptyHarvest.test.ts

## Governing Overview

[data overview](overview.md)

## Purpose

The unit suite for **legacy-raw harvesting** (260715-FEUI-L6 R7): the pure OSC parsers and the
harvest store — 8 cases pinning that harvested signals are hints only (never fabricated, never
grammar states) while xterm itself stays out of jsdom (the parsers are pure functions; no
terminal is constructed anywhere).

## Code Commentary

### Logic

- **`parseOsc133`** cit:([`parseOsc133`], dashboard/src/data/ptyHarvest.ts:85-91): the mark matrix `A`/`B` → prompt, `C` → command-running, `D;0` →
  command-finished; unknown marks and the empty payload are NEVER fabricated into hints (null).
- **`parseOsc94`** cit:([`parseOsc94`], dashboard/src/data/ptyHarvest.ts:98-110): state 0 → progress-done; active states → progress with the percent
  clamped (`4;1;250` → 100); indeterminate `4;3` → progress without a percent; non-progress OSC 9
  payloads (e.g. notification text) and non-numeric states → null.
- **`turnHintWord`** cit:([`turnHintWord`], dashboard/src/data/ptyHarvest.ts:113-126): the labeled hint words (`command running`, `progress 42%`).
- **Store semantics** cit:([`PtyHarvestState`], dashboard/src/data/ptyHarvest.ts:30-38): bell sets the pending marker (+`lastBellAt`) and
  `acknowledgeBell` clears it (focus-as-acknowledgment); acknowledging without a pending bell is
  a strict no-op (state identity preserved — no churn); title and turn hints are per-session and
  independent. Store reset per case via `beforeEach` `setState`.

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- The module under test. [1]
- The DOM-level archetype/bell cases (hooks per archetype, rail marker). [2]
- The rail's L6 block (bell marker + tooltip hints; the dot stays pure grammar). [3]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.
