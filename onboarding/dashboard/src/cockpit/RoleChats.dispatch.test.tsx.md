# dashboard/src/cockpit/RoleChats.dispatch.test.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

Witness mounted pane dispatch, Result/report and scope-effect triggers.

## Code Commentary

Mock HTTP drives accepted/refused starts, selected Result/report behavior, settled dispatch and offline-recovery result preservation without a duplicate `/result` read, and delayed options. Equal-scope rerender and feature edits are distinguished from changes that reload scope.

## Boundaries

Component assertions are not real-host qualification or a claim that the whole dashboard suite passed.

## Evidence

- Mounted fixtures exercise Start, Result and metadata rereads. The metadata request count excludes selected-model option requests. [1]
