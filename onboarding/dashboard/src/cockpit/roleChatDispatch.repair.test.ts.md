# dashboard/src/cockpit/roleChatDispatch.repair.test.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

Witness acceptance-identity refusal, offline recovery scope and live notification.

## Code Commentary

Production dispatch is exercised with stubbed writers and poll callbacks, including foreign acceptance, unpinned offline task-bound recovery and the notification callback current when acceptance arrives. Negative rejected/hostless cases retain their separate meanings.

## Boundaries

The test poll is not the production Result HTTP transport; no live host or global race proof is claimed.

## Evidence

- The test file asserts the cases and limitations described above. [1]
