# dashboard/src/panels/ChatActivityIndicator.tsx

## Governing Overview

[panels overview](overview.md)

## Purpose

Pure summary of live hosted-chat turn activity consumed by the Operations task row. It keeps chat activity separate from durable task/lifecycle progress and inbox delivery acknowledgment.

## Code Commentary

### Logic

`summarizeChatActivity` filters the shared `OpenSession` catalog to live harness sessions. A resolved qualified leaf key wins; only when no exact-leaf session exists does an unclaimed session with the row's lifecycle id qualify. `turnState` maps `awaiting-input` to `needs input`, `working` to `working`, `turn-ended` to `idle`, and stale, missing, or unknown values to `unknown`. Multiple seats aggregate by needs-input, working, unknown, then idle, while detail is deterministic by seat role and session id. The JSX marker and local styles were removed. rowState and LifecycleList render the summary as a priority word and complete seat hover; this module creates no DOM, live region, poller or animation.

### Conventions

This module is a pure mapping seam over OpenSession and the existing sessionSeatRole vocabulary.

### Invariants And Boundaries

- It must not infer activity from lifecycle state, task progress, inbox age, terminal status, labels, position, or selection.
- Only live `kind="harness"`, `status="running"` sessions count; plain terminals, landed/exited sessions, and missing seats produce no summary.
- Exact qualified leaf identity is isolated before lifecycle fallback; a session claiming another leaf must not leak through a shared lifecycle id.
- CockpitShell owns catalog hydration through catalogPoll; the pure summary adds no poller, classifier or backend projection. LifecycleList consumes the summary and separately owns row rendering.

### Todos

Historical observations on the removed marker, not current obligations inferred from deletion: task-axis role semantics, adjacent palette meaning, live-region scale, shared-store poll rerenders, and the deliberate omission of undefined-status sessions.

### 2026-07-24 Curator Delta

A fresh ready harness seat with no turn claim now summarizes as calm idle. A starting seat remains
unknown, preserving the difference between booting evidence and a fabricated completed turn.

## Evidence

### Docs References

No relevant domain documentation was configured in the resolved `system/sources.md`; the contract is proved by repository sources and tests.

No domain reference was available for this UI-local state mapping.

### Repo-Internal References

`CockpitShell`/`catalogPoll` hydrate the shared session store, and Operations `LifecycleList` maps
those already-served values through this pure summary. The full-page `SessionRail` is a peer renderer of
the same normalized catalog, not this summary's hydration owner.


- `CockpitShell` is the sole catalog driver/reconciler owner for the shared store. [1]


- `LifecycleList` is the pure summary's Operations consumer. [2]

- `SessionRail` is a peer renderer of the same normalized session-state catalog. [3]

- Focused tests cover mapping, exact-leaf-first identity, lifecycle fallback, precedence, missing classification, and omission. [4]


### Cross-Repo References

No meaningful cross-repository boundary exists; the component is inside the agents-remember dashboard.

No cross-repo reference.
