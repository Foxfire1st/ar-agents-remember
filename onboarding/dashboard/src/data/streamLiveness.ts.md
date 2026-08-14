# dashboard/src/data/streamLiveness.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/streamLiveness.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-02T01:42+02:00|
| lastVerifiedCommitHash |  `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`|
| lastVerifiedCommitDate |  2026-08-14T14:36:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[data overview](overview.md)

## Purpose

Judge long-lived open EventSource channels after positive sleep evidence or one bounded silent episode,
without reconnect-storming legitimate idle or hidden-tab streams.

## Code Commentary

### Logic

The watchdog samples wall-clock jumps and frame silence only while its channel is open and the page is
visible. It spends at most one quiet backstop cycle, ignores the replacement handshake as proof of life,
and re-arms only when a later independent frame arrives.

### Conventions

All timers, clock, visibility, and listener hooks are injectable for transport-level tests.

### Invariants And Boundaries

Sleep is positive evidence and may cycle again; ordinary silent channels receive at most one quiet cycle
per observed-life episode. The caller owns close/reopen and whether that cycle changes visible state.

### Todos

None.

## Docs References

No Domain Documentation entries are configured in this memory worktree's source registry.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation is configured. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Liveness tuning, one-shot backstop, and visibility handling. | `startStreamLivenessWatchdog` | dashboard/src/data/streamLiveness.ts:103-176 |
| Conversation and state streams both install this watchdog. | "half-open-wedge" | dashboard/src/data/stream.ts:94-94 |

## Cross-Repo References

No meaningful cross-repository references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| The watchdog is local browser transport policy. | `startStreamLivenessWatchdog` | dashboard/src/data/streamLiveness.ts:103-176 |

## Update History

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B22 curator: replaced the three `n/a`-anchor
  table citations with exact frozen-source anchors and fixer-generated ranges; exact
  non-fixing check returns zero findings.

- 2026-08-02T01:42+02:00 — No content impact: re-derived line range(s) that ended past the end of the file the row names (`memory_quality/style/citations`, `citation_range_out_of_bounds`). Each range was rewritten by reading the cited construct at its current location; no claim was changed to fit a range, and no range was interpolated. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-24T13:17:50Z — Created for one-shot EventSource half-open liveness policy. Verification
  hash/date remain pinned to the pre-commit source stamp.
