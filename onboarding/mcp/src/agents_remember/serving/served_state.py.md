# mcp/src/agents_remember/serving/served_state.py

## Governing Overview

[serving overview](overview.md)

## Purpose

Declares the workspace state body emitted by `/api/state` and SSE snapshots: the observer projection plus serving-process identity, response-time notifier heartbeat facts, and the observer stage's own health reading.

## Code Commentary

### Logic

`ServedWorkspaceProjection` extends the observer projection with four optional keys: `servingBuild`, `agentNotifierHeartbeat`, the retained `supervisorHeartbeat` rename alias, and `terminalObserverHealth` (`LOCR-R17@v1`). `SERVED_TAIL_FIELDS` lists exactly that extension. `served_state_tail` emits both heartbeat names from the same payload, and it emits the observer-health payload under the `servingBuild` rule rather than the heartbeat rule: a caller with no valid record for the CURRENT serving lifetime has nothing honest to report, so the key is ABSENT rather than null, and no other served field changes value or meaning. Once present, that payload carries its own explicit nulls (`lastAttemptAt: null` is a reported fact about this lifetime). An absent build or absent heartbeat object likewise emits no corresponding key; inside an existing heartbeat payload, unknown/never-ticked fields remain explicit nulls. Build fields use `exclude_none=True`. cit:([`ServedWorkspaceProjection`, `SERVED_TAIL_FIELDS`, `served_state_tail`], mcp/src/agents_remember/serving/served_state.py:50-109).

### Invariants And Boundaries

- The tail is computed at serve time and merged onto a copy of the memoized projection dump.
- It does not enter `WorkspaceProjection` or persisted `latest-state.json`.
- Response-time age changes do not change the content revision/ETag, preserving body-free 304 responses. The observer-health tail is per-response arithmetic on a persisted row, so it must never enter the memoized body or the projector's content revision either.
- Only full SSE snapshots receive the tail; per-entity delta events carry none.
- The separate dumps preserve omitted build facts and explicit heartbeat nulls without re-parsing the entire projection on every request.
- `terminalObserverHealth` is additive and omissive: absence is the declared answer whenever no valid record for the current serving lifetime exists, and a served read never rewrites, repairs, creates or deletes that record. With the key present, every pre-existing served field stays byte-identical — the change is exactly one extra key.
- The historical dedicated conformance matrix was removed by the retained-test cleanup; its old enforcement claim is not current protection. That gap is now partly re-covered for this tail: `mcp/tests/test_terminal_observer_health.py::TerminalObserverHealthServedTailTests` drives the real `_state_response` handler and the real `stream_events` generator, including the ETag/304 branch and the snapshot/delta asymmetry.

### Conventions

These are declared wire names. The module composes existing build and heartbeat payload types rather than owning their measurements.

## Evidence

### Repo-Internal References

- Serving-only fields extend the observer model and remain outside its persisted shape. [1]
- One assembly point preserves both omission and null semantics, including the observer-health key's absent-versus-null rule. [2]
- The tail's exact key list, so assembly and contract cannot drift apart silently. [3]
- The declared wire form of the fourth key. [4]
- The served-tail cases that drive this assembly through the production route handler and stream generator. [5]

### Docs References

No Domain Documentation source is configured.

### Cross-Repo References

No external repository boundary governs this assembly.
