# dashboard/src/panels/review/explainer/explainerGradeParser.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

The round trip of the reviewer's categories and grades.

## Code Commentary

A category and a grade the reviewer set survive whatever answer shape carried them, and a grade that arrived stale is merged rather than dropped, so a judgment is never silently reset by a refetch.

## Boundaries

The obligation above is the whole of what this file must keep true; the route account says what the surrounding surface promises.

## Evidence

- A grade the reviewer set survives a refetch that carried a staler one, because the two are merged rather than replaced. [1]

- Categories are read out of whichever answer shape carried them, so a shape change does not empty the reviewer's list. [2]
