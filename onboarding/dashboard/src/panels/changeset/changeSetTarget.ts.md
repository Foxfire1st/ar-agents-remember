# dashboard/src/panels/changeset/changeSetTarget.ts

## Governing Overview

[overview](overview.md)

## Purpose

Defines the change-set target and viewer prop types shared by workspace and tab selection.

## Code Commentary

Targets retain repository and scope, leaf/master qualifiers, working or committed mode, numbered comparison and master generation pins. The review field selects Cockpit's review dispatch; an empty review object selects current task context and historical identifies a recorded review.

## Relationships

ChangeSetViewer re-exports the target type. changeSetSelection derives requests; the target declaration itself performs no read and grants no revision authority.

## Evidence

- Defines the change-set target and viewer prop types shared by workspace and tab selection. [1]
