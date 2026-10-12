# dashboard/src/cockpit/roleChatResult.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

Read and apply the selected execution result and recorded report.

## Code Commentary

Per-request reads require the selected UUID; pending not-found reads can retry, and a launch lock is reread rather than treated as final success. Foreign/malformed execution identity is refused. Application preserves uncertain retry state and sticky automatic failures. Report reads check the live identity before and after transport and open the recorded body in the shared reader.

## Boundaries

Result/report transport is separate from start dispatch and rendering. A report exists or a host ends does not mean the task passed review or landed.

## Evidence

- fetchRoleExecutionResult is a current owner of the behavior described above. [1]
- openRoleExecutionReport is a current owner of the behavior described above. [2]
