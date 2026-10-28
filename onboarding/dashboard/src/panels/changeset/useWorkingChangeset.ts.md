# dashboard/src/panels/changeset/useWorkingChangeset.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

Keeping the changeset of the file the reviewer has open current.

## Code Commentary

While a file is open the working changeset is re-read, so what the reviewer sees keeps up with what they did; a read that fails is surfaced as a failure rather than left as older data that looks current.

## Boundaries

The obligation above is the whole of what this file must keep true; the route account says what the surrounding surface promises.

## Evidence

- An open file's changeset keeps being read, so what the reviewer sees keeps up with what they changed. [1]
