# dashboard/src/cockpit/RoleExecutionStatus.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

The component renders the launcher's one failure line, optionally falls back to stepped-up status when there is no failure, and separately exposes backend-authorized Revive.

## Code Commentary

The line combines an action failure, an unreachable host and an unresolved launch; with no failure it renders StepUpStatus unless showStepUp is false, and a successful explicit action can clear the failure. RoleReviveControl renders only for canRevive=true and delegates to its owner callback with the current enabled flag. Execution detail, reply text and report availability are no longer printed here (MIK-R75 rules 1 to 3).

## Invariants And Boundaries

This file does not poll, launch actors or decide semantic task acceptance. A written report is observation, and revival capability belongs to the backend. The line is independent of any reply, so the bar's height does not follow a message.

## Current Contract

`executionFailure` still combines host-unreachable and unknown-launch recovery text. `RoleExecutionStatus` combines that with action failure and renders one alert when any message exists. With no message it now delegates to `StepUpStatus` by default; `showStepUp=false` suppresses that branch. The launcher sets false because its action row already renders the step-up status. Failure wins over that fallback status. Revive remains separately gated by `canRevive === true` and the caller enabled flag. Neither branch prints a reply or decides task acceptance.


This account is bound to the candidate source, not a claim of a running serving build or a fresh execution/acceptance verdict. Existing historical accounts remain historical.

## Evidence


- Worker/Curator typed review census, record-only exclusion and unknown history. [1]
- Reason admission, threshold and differing-harness/model inheritance boundary. [2]
- File-local implementation of the stated contract; caller-owned effects and governing workflow are separate evidence. [3]
- File-local implementation of the stated contract; caller-owned effects and governing workflow are separate evidence. [4]

The current source and test assertions below establish the documented ownership; test citations do not claim a rerun in this pass.

- Current source owner or exact assertion described above. [5]
- Current source owner or exact assertion described above. [6]
