# mcp/src/agents_remember/models/lifecycles/responses.py

## Governing Overview

[lifecycles overview](overview.md)

## Purpose

Retains the lifecycle state and phase Literal vocabulary, not lifecycle-signal response DTOs.
The declared vocabulary is consumed by observer lifecycle state/reducer code; retaining it
does not restore session lifecycle hosting or public signal tools.

## Code Commentary

`LiveState` names running, paused, blocked and awaiting-developer. `EndOutcome` names completed
and abandoned; `TerminalState` aliases it, and `State` combines live/terminal sets. `Phase` names
request, trust-checkpoint, reframe-research, decide, build and close. The source contains no
`LifecycleResponse`, signal/turn-notification subclasses, token envelope or gate DTO.

## Invariants And Boundaries

These are type vocabulary, not registered model-facing lifecycle operations, emitted events or
implementation acceptance. Removed signal response/builders are historical, not lower-level
compatibility promises.

## Evidence

- Shared state/phase Literals remain, while lifecycle-signal response classes and builders are absent. [1]
