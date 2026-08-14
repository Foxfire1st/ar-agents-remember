# dashboard/src/data/ptyHarvest.test.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/ptyHarvest.test.ts`          |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-07-18T07:22+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`       |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
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

## Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module under test. | `parseOsc133` | dashboard/src/data/ptyHarvest.ts:85-91 |
| The DOM-level archetype/bell cases (hooks per archetype, rail marker). | "two archetypes (R1)", "bell acknowledgment (R7)" | dashboard/src/panels/session-cockpit/PtySurface.test.tsx:53-92; dashboard/src/panels/session-cockpit/PtySurface.test.tsx:226-234 |
| The rail's L6 block (bell marker + tooltip hints; the dot stays pure grammar). | "a harvested bell renders the rail attention marker with a text equivalent (R7)" | dashboard/src/panels/session-cockpit/SessionRail.test.tsx:776-784 |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-02T20:42:42+02:00 — 260731-EFA-L6 curator W2-B10: repaired 10 citation findings (4 prose pointers and 3 reference rows); scoped recheck clean.

- 2026-07-18T07:22+02:00 — FEUI-L8 manual route refactor: retargeted this direct data file card
  from the packed dashboard/src parent to the new nearest data authority overview. Source behavior
  is unchanged by this memory-only governance move; verification hash/date remain pinned.

- 2026-07-17T04:20+02:00 — Created for 260715-FEUI-L6 R7/R9: the 8-case parser + store suite —
  OSC 133 mark matrix, OSC 9;4 progress with clamping and null-on-non-progress, labeled hint
  words, bell/acknowledge (incl. the no-churn no-op), and per-session independence. Verification
  metadata pinned to the leaf base until closeout stamps the L6 code commit.
