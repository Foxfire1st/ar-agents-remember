# mcp/src/agents_remember/package_data/paseo_plugin/server/declared_wait_state.ts

## Governing Overview

[Native Paseo plugin](../overview.md)

## Purpose

The declared waits' own state on the turn-end tracker: how one turn end opens, renews or ends a seat's declaration, the rows those events write, when the check falls due, and the view of an open wait the host-activity record publishes. The tracker, its timers and the gates stay in `turn_ended.ts`.

## Code Commentary

`judgeDeclaredEnd` judges one end. An end that declares nothing ends the seat's open wait, and so does a declaring end of a seat the host already reports archived, which opens nothing: no wait outlives its seat. Any other declaring end opens or renews the wait, with the next ordinal and the time the wait first opened kept across renewals, and writes one declared row per wait it names. A wait the seat held that this end no longer declares ends with its own row, so a background-only end ends an open helper wait and the other way round. Past the bound the caller gives (the silent-limit window), the oldest seat's declaration is evicted and that seat is announced as no longer waiting.

`endDeclaredWait` drops a pending check together with the wait it belongs to and writes the wait's ended rows, so no separate cancelled-wait row is written. `checkDelayMs` gives the check delay: the helper delay for helpers, the declared minutes for a background process, and the earlier of the two when both were declared. A check's skip rows are one `<wait>-wait-check-skipped` row per wait it covers; every other wait keeps the row kind its caller gives. `openDeclaredWait` builds the published view of a seat's open wait, and `announceWait` hands it to the tracker's `declaredWait` signal, or `null` once the wait is gone.

## Relationships

`turn_ended.ts` calls `judgeDeclaredEnd` at each turn end and `announceWait` when a turn starts, a check is delivered, a seat is archived and on cleanup, and re-exports `openDeclaredWait`. Row and time formatting come from `turn_log.ts`, wait names and kinds from `background_wait.ts`. The signal reaches `host_activity.ts` through the server entry.

## Evidence

- A check writes one skip row per wait it covers; another wait keeps the kind it is given. [1]
- The published view names the open waits, since when, the due check and the declaration's words. [2]
- Every change of a seat's wait reaches the host-activity signal. [3]
- The check comes at the earlier of the two delays when both waits were declared. [4]
- An undeclared end ends every wait the seat holds and drops its pending check. [5]
- An end that declares nothing, or declares for an archived seat, opens nothing; a declaring end writes one row per wait. [6]
- A renewal keeps the first opening time, ends a dropped wait and evicts the oldest declaration past the bound. [7]
