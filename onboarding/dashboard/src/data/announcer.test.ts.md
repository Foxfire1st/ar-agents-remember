# dashboard/src/data/announcer.test.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/announcer.test.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-26T15:40+0200                           |
| lastVerifiedCommitHash | `4e5fbcf872bbc1ec2566a6ccb17276a6bad80c7f` |
| lastVerifiedCommitDate | 2026-07-26T18:40:37+02:00|
| governingOverview | `overview.md`                                   |

## Governing Overview

[data overview](overview.md)

## Purpose

Pins the single-copy-source announcement contract, repeat sequencing, transition-only fleet
announcements, and the focused-question deduplication rule — extended (N1) to the
plural-pending case: a seat blocked SOLELY on a multiplexed sub-agent approval.

## Code Commentary

### Logic

The suite checks every SetResult/promotion/state string, verifies sequence increments for repeated
text, exhausts the pure state-entry detector's seed/steady/transition cases, and drives the wired
watcher through the live session store. The N1 case (L119-L141) pins both halves of the
agent-only-blocked coordination: UNFOCUSED, the region speaks with the seat-level wording
(`sessionAwaitingInputAnnouncement`) and never claims the question is the parent's; FOCUSED, the
InteractionBar announces the agent bar itself and the region stays silent — the fixture builds the
plural-only row with the adapter-bound `raw: { threadId, agentLabel }`.

### Conventions

Assertions use the exported copy functions rather than duplicating prose fixtures.

### Invariants And Boundaries

This is test-only; it deliberately does not claim coverage of the reviewer's split-poll-beat sev-4
edge.

### Todos

Add a staggered turn-state/interaction-payload regression if sev-4 observation 9 is taken up.

## Docs References

No Domain Documentation source is configured; no external citation applies.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No external domain citation applies. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Announcement implementation under test. | L1-L112 | [announcer.ts](announcer.ts) |
| One source for every asserted string. | L1-L127 | [setControlsCopy.ts](setControlsCopy.ts) |
| The catalog-row fixture builder the seat helper spreads (plural pending flows through `...overrides`). | L10-L26 | [../test/fixtures/catalogRows.ts](../test/fixtures/catalogRows.ts) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repo evidence applies. | — | — |

## Reviewed Candidate Delta

Adds same-hydration multi-seat coverage: urgent transitions are emitted together so a later synchronous seat cannot overwrite the earlier alert.

The reviewed candidate is still uncommitted. Existing verification hash/date remain pinned to the
leaf base; closeout owns commit stamping.

## Update History

- 2026-07-26T15:40+0200 — 260718-CHATS-L7 curator: recorded the N1 agent-only-blocked pin — a seat
  whose plural `controlPendingInteractions` carries a sub-agent permission (singular slot absent)
  announces seat-level "awaiting input" when unfocused and stays silent when focused (the
  InteractionBar announces the agent bar itself). Verification stays pinned; the L7 change is
  uncommitted and closeout re-stamps.

- 2026-07-18T07:22+02:00 — Curated the final same-reviewer-PASS FEUI-L8 behavior above using direct
  source/test/task evidence; no Domain Documentation source is configured.

- 2026-07-17T08:33+02:00 — Created for 260715-FEUI-L4 R8/R9 after final reviewer PASS;
  verification metadata is pinned to the uncommitted leaf's contract base pending closeout.
