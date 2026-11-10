# skills/l-01-agent-lifecycles/reference/bootstrap/foundation-state.md

## Governing Overview

[overview](../../overview.md)

## Purpose

The Bootstrap detail for reporting the knowledge foundation's state and naming the next step. It separates authored knowledge from onboarding cards and the attributed baseline.

## Code Commentary

Bootstrap reads the state from `memory_init`'s `knowledge` block — `not-recorded`, `recorded` with the exact identity, `unusable`, or a refused admission with its own next action — and reports which one it is. The role file points to the "Read the state" section before reading and reporting, and the Bootstrap operation points to "Name the next step" before naming it.

The single next step is to start the Architect: the foundation is the Architect's first regular work through `c-14-knowledge-bootstrap`'s registered-leaf task route, and the Curator creates, extends or resumes it inside that task. Bootstrap does not produce the foundation; the file sends the seat to the role's boundaries for its setup-only authority and authoring prohibitions. A memory repository with a commit may still report `not-recorded` when Bootstrap finishes; the report says setup is complete and the foundation is the Architect's first piece of work, never that Bootstrap created or completed it.

## Evidence

- The foundation is authored records under `knowledge/`, distinct from cards and baseline, and Bootstrap reports one of four states. [1]
- The next step is to start the Architect; the Curator authors the foundation inside the Architect's task, and Bootstrap claims no foundation work. [2]
- The role file points to the state section before reading and reporting. [3]
- The Bootstrap operation points to the next-step section before naming it. [4]
