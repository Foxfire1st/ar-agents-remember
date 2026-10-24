# skills/c-05-create-or-update-onboarding-files/workflows/findings-capture-workflow.md

## Governing Overview

[Repository overview](../../../overview.md)

## Purpose

The ordered findings-capture workflow the parent procedure names as its companion: establish the context, verify, qualify, choose the owning durable target, apply the onboarding guardrail, capture, and return a summary.

## Code Commentary

The file is kept verbatim from the retired findings-capture skill, with a one-line comment saying so and pointing the reader at `workflows/findings-capture.md` for the procedure that now owns it. It states its own caller responsibilities — the finding, whether an active task exists, the affected code or documentation surfaces, the evidence already known and the current phase when the finding is task-local — and then the durable capture order. Its seven steps end at a returned capture summary, and it closes with prohibited patterns and completion criteria, so a capture is judged by the artifact it left rather than by the intent to leave one.

## Evidence

- The workflow keeps its caller responsibilities, ordered steps and prohibited patterns, and is read as the companion of the kept findings-capture procedure. [1]
- Capture is complete only against its completion criteria and a returned summary, not by the intention to record the finding. [2]
