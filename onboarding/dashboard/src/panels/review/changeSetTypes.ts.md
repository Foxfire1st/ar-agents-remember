# dashboard/src/panels/review/changeSetTypes.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

The shapes the change-set's reading column is built from.

## Code Commentary

The reading column's reads, rows, groups, sorts and counts are one set of shapes, so a group cannot describe a different read from the row inside it. The shapes keep the reviewer's subject and the role label they were given rather than substituting a display name.

## Boundaries

The obligation above is the whole of what this file must keep true; the route account says what the surrounding surface promises.

## Evidence

- A group and its rows describe the same read, because they are shaped together rather than separately. [1]

- The role label a read arrived with is carried, not replaced by a display name. [2]
