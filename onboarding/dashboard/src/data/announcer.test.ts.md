# dashboard/src/data/announcer.test.ts

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
watcher through the live session store. The N1 case
cit:([`controlPendingInteractions`], dashboard/src/data/announcer.test.ts:121-133) pins the fixture for both halves of the
agent-only-blocked coordination — cit:(["Unfocused: the region speaks with the seat-level wording", "Focused: the InteractionBar announces the agent bar itself; the region stays silent."], dashboard/src/data/announcer.test.ts:134-140): UNFOCUSED, the region speaks with the seat-level wording
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

## Evidence

### Docs References

No Domain Documentation source is configured; no external citation applies.

No external domain citation applies.

### Repo-Internal References

- Announcement implementation under test. [1]
- One source for every asserted string. [2]
- The catalog-row fixture builder the seat helper spreads (plural pending flows through `...overrides`). [3]

### Cross-Repo References

No meaningful cross-repo references found.

No cross-repo evidence applies.

## Reviewed Candidate Delta

Adds same-hydration multi-seat coverage: urgent transitions are emitted together so a later synchronous seat cannot overwrite the earlier alert.

The reviewed candidate is still uncommitted. Existing verification hash/date remain pinned to the
leaf base; closeout owns commit stamping.
