# dashboard/src/data/streamLiveness.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/streamLiveness.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-24T13:17:50Z |
| lastVerifiedCommitHash |  `842b487b854503d95c9c2d9dce1841198ba93c7d`|
| lastVerifiedCommitDate |  2026-07-24T17:08:25+02:00|
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

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation is configured. | Source discovery checked | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Liveness tuning, one-shot backstop, and visibility handling. | L47-L176 | [streamLiveness.ts](streamLiveness.ts) |
| Conversation and state streams both install this watchdog. | L1-L240 | [stream.ts](stream.ts) |

## Cross-Repo References

No meaningful cross-repository references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The watchdog is local browser transport policy. | L1-L176 | [streamLiveness.ts](streamLiveness.ts) |

## Update History

- 2026-07-24T13:17:50Z — Created for one-shot EventSource half-open liveness policy. Verification
  hash/date remain pinned to the pre-commit source stamp.
