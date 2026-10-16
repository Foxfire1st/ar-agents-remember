# dashboard/src/cockpit/roleChatDispatch.repair.test.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

Witness acceptance-identity refusal, offline recovery scope and live notification.

## Code Commentary

Production dispatch is exercised with stubbed writers and poll callbacks, including foreign acceptance, unpinned offline task-bound recovery and the notification callback current when acceptance arrives. Negative rejected/hostless cases retain their separate meanings.

## Boundaries

The test poll is not the production Result HTTP transport; no live host or global race proof is claimed.

## Current scoped contract

The added occupied-seat case protects reasoned `stepUp` transport through `dispatchRoleAction`: its captured start body contains the exact task selection, reason and request ID, with no `agentOverride`. Its dispatch reply is deliberately 409, so this is not successful backend replacement evidence.

## Evidence

- The test file asserts the cases and limitations described above. [1]


- The new case dispatches start from an occupied completed task seat with a stepUp reason, captures the exact role/task/request/action payload and excludes agentOverride even when the stub dispatch returns 409. Existing mismatched-receipt, offline-scope and current-notification cases remain. [2]
