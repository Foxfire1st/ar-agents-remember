# dashboard/src/data/ptyHarvest.test.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/ptyHarvest.test.ts`          |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-07-18T07:22+02:00 |
| lastVerifiedCommitHash | `7b62338310aff67ae8b66a450a52a1f1052137c4`       |
| lastVerifiedCommitDate | 2026-07-17T04:36:24+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[data overview](overview.md)

## Purpose

The unit suite for **legacy-raw harvesting** (260715-FEUI-L6 R7): the pure OSC parsers and the
harvest store — 8 cases pinning that harvested signals are hints only (never fabricated, never
grammar states) while xterm itself stays out of jsdom (the parsers are pure functions; no
terminal is constructed anywhere).

## Code Commentary

### Logic

- **`parseOsc133`** (L11-L23): the mark matrix `A`/`B` → prompt, `C` → command-running, `D;0` →
  command-finished; unknown marks and the empty payload are NEVER fabricated into hints (null).
- **`parseOsc94`** (L25-L37): state 0 → progress-done; active states → progress with the percent
  clamped (`4;1;250` → 100); indeterminate `4;3` → progress without a percent; non-progress OSC 9
  payloads (e.g. notification text) and non-numeric states → null.
- **`turnHintWord`** (L39-L44): the labeled hint words (`command running`, `progress 42%`).
- **Store semantics** (L46-L70): bell sets the pending marker (+`lastBellAt`) and
  `acknowledgeBell` clears it (focus-as-acknowledgment); acknowledging without a pending bell is
  a strict no-op (state identity preserved — no churn); title and turn hints are per-session and
  independent. Store reset per case via `beforeEach` `setState`.

## Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | `system/sources.md` checked | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The module under test. | L13-L126 | [ptyHarvest.ts](ptyHarvest.ts) |
| The DOM-level archetype/bell cases (hooks per archetype, rail marker). | — | [../panels/session-cockpit/PtySurface.test.tsx](../panels/session-cockpit/PtySurface.test.tsx) |
| The rail's L6 block (bell marker + tooltip hints; the dot stays pure grammar). | — | [../panels/session-cockpit/SessionRail.test.tsx](../panels/session-cockpit/SessionRail.test.tsx) |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Update History

- 2026-07-18T07:22+02:00 — FEUI-L8 manual route refactor: retargeted this direct data file card
  from the packed dashboard/src parent to the new nearest data authority overview. Source behavior
  is unchanged by this memory-only governance move; verification hash/date remain pinned.

- 2026-07-17T04:20+02:00 — Created for 260715-FEUI-L6 R7/R9: the 8-case parser + store suite —
  OSC 133 mark matrix, OSC 9;4 progress with clamping and null-on-non-progress, labeled hint
  words, bell/acknowledge (incl. the no-churn no-op), and per-session independence. Verification
  metadata pinned to the leaf base until closeout stamps the L6 code commit.
