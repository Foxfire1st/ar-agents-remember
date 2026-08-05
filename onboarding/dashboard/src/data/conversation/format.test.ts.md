# dashboard/src/data/conversation/format.test.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/conversation/format.test.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-20T22:30+02:00 |
| lastVerifiedCommitHash | `9e6c15d2b2bb663fcd10e26d77d0e4d2795829bd` |
| lastVerifiedCommitDate | 2026-07-20T22:32:02+02:00|
| governingOverview | `overview.md` |

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

## Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries are
configured. This one-to-one card therefore relies on its direct agents-remember source/tests and the
reviewed task evidence for any current behavioral claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The presentation conventions under test. | `humanizeDuration` | dashboard/src/data/conversation/format.ts:25-37 |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-04T17:52+02:00 — 260731-EFA-L6 S18-B15 curator: resolved 2 citation findings. Re-anchored the
  presentation-conventions row to `humanizeDuration` and normalized its source cell to the exact
  `format.ts:11-86` span. Scoped recheck clean.
- 2026-07-20T22:30+02:00 — 260718-CHATS-L4 curator: created the sidecar for the format convention
  proofs (A1/A4/A5) — exact humanized-duration strings, em-dash absent, interpunct joins, quiet
  long-stale tone, and boundary truncation. Verification is pinned to the leaf base (`0be0099`)
  because the new source file is uncommitted; closeout owns its first source stamp.
