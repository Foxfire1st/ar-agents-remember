# dashboard/src/panels/review/compact-l104.fixture.json

## Governing Overview

[Route overview](../overview.md)

## Purpose

A captured compact overview for leaf L104, with its subjects, counts and reason.

## Code Commentary

This is a recorded answer, not an invented one: the shape is what a real open returned for L104, with three keys - state, subjects and reason - and each subject carrying its counts and changed paths. Three tests read it (changeSetOverview.test.ts, worklistSummary.test.ts, ReviewPage.compact.test.tsx), so the counts in it are the values their assertions stand on: changing a number here changes what those tests prove.

## Boundaries

The obligation above is the whole of what this file must keep true; the route account says what the surrounding surface promises.

## Evidence

- The fixture records a real compact answer for L104 rather than a hand-written count, and the tests that read it assert against these recorded values [1]
