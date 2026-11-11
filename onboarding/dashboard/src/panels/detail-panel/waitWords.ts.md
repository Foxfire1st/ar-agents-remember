# dashboard/src/panels/detail-panel/waitWords.ts

## Governing Overview

[Panels overview](../overview.md)

## Purpose

Name what a waiting task's seats wait for, in the words its task word and its hover share.

## Code Commentary

`waitWhat(seats)` maps each served `waitsFor` value to its word through `WAIT_NAMES` (`subagent` → `subagents`, `background` → `background`), keeps each word once in first-seen order and joins them with ` and `; with no seats it returns the empty string. `waitLines(seats)` writes one line per served waiting seat: its role (`seat` when none is served), its agent id, `waits for <what> since <time>`, `check due <time>` when a check is served, and the seat's own `detail` when present, joined with ` · `. Times go through `formatLimitTime`. The module formats served `WaitingSeat` facts only; whether a task waits is the server's decision.

## Relationships

`pageParts.tsx` builds the `waiting for <what>` word from `waitWhat` and the word's hover from `waitLines`; `lifecycle-list/rowState.ts` adds `waitLines` to a waiting row's hover. `lifecycle-list/waiting.test.tsx` pins the joined word and the seat line. `WaitingSeat` is the generated type in `types/projection.ts`.

## Evidence

- Wait names map subagent to subagents and background to background. [1]
- The word joins the distinct wait names with and. [2]
- One line per seat: role or seat, agent, what since when, the check due when served and the seat's words. [3]
- The task word reads waiting for the joined names. [4]
- The word's hover is the seat lines when seats are served. [5]
- A waiting row's hover adds the seat lines. [6]
