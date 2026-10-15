# dashboard/src/panels/detail-panel/taskBlocks.tsx

## Governing Overview

[Panels overview](../overview.md)

## Purpose

Render task-only Steps and Review blocks from projected state without inventing progress or whole-round counts.

## Code Commentary

`StepsBlock` omits an empty step collection, draws mark/ID/title/state rows and the projected done/total count, and uses model state precedence for the first unfinished top-level step. A done parent remains done; a started or done child promotes an unfinished parent to current before blocked/next fallback. A step's note wins over its outcome and opens through the shared clipped Markdown line. Nested rows retain their own states and Markdown skip reasons; their notes are projected but are not drawn here. Do not claim complete nested-note presentation from the top-level-note contract. Header StepMarks receives the cached major-step list for pointer details; nested rows remain in the full list, not in the mark count. Full-list Pips and the greater-than-twelve aggregate bar do not acquire StepDot tooltips.

`ReviewBlock` is absent when there is no review state or round zero. It uses required `openFindings` and `totalFindings` for the whole round, while showing at most eight open rows from the carried findings. It does not count the flags of a summary slice as the round's total. The all-findings link reaches the hydrated own view; every carried finding retains its open/closed label and honest description preview flag.

## Boundaries

The model determines state/mark mappings and the server determines aggregate counts. An older producer omits the entire review state, not a count inside a present review object. This module does not mutate steps, issue a verdict or broaden source acceptance.

## Evidence


- StepsBlock carries served progress, passes cached major steps to header marks, and retains the full top-level/nested table with model-owned display states. [1]


- Whole-round counts remain authoritative despite the eight-row open-finding preview. [2]
- Nested state/title/skip reasons are shown, but nested notes are not rendered. [3]
