# dashboard/src/panels/ChatActivityIndicator.tsx

| Field                  | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/ChatActivityIndicator.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-18T16:02+02:00 |
| lastVerifiedCommitHash | `31f58834f86c0d98e26b0896e099a2403a8729ee` |
| lastVerifiedCommitDate | 2026-07-18T15:41:39+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[panels overview](overview.md)

## Purpose

Operations-only presentation of live hosted-chat turn activity for a task row. It keeps chat activity separate from durable task/lifecycle progress and inbox delivery acknowledgment.

## Code Commentary

### Logic

`summarizeChatActivity` filters the shared `OpenSession` catalog to live harness sessions. A resolved qualified leaf key wins; only when no exact-leaf session exists does an unclaimed session with the row's lifecycle id qualify. `turnState` maps `awaiting-input` to `needs input`, `working` to `working`, `turn-ended` to `idle`, and stale, missing, or unknown values to `unknown`. Multiple seats aggregate by needs-input, working, unknown, then idle, while detail is deterministic by seat role and session id. `ChatActivityIndicator` renders a compact marker with a `role="status"`, accessible label, title, and no polling or animation.

### Conventions

The component is a pure mapping/presentation seam over `OpenSession`; it uses the local Panda `css`/`cva` styles and the existing `sessionSeatRole` vocabulary.

### Invariants And Boundaries

- It must not infer activity from lifecycle state, task progress, inbox age, terminal status, labels, position, or selection.
- Only live `kind="harness"`, `status="running"` sessions count; plain terminals, landed/exited sessions, and missing seats produce no indicator.
- Exact qualified leaf identity is isolated before lifecycle fallback; a session claiming another leaf must not leak through a shared lifecycle id.
- `CockpitShell` owns catalog hydration through `catalogPoll`; this component adds no poller,
  classifier, or backend projection. `LifecycleList` is its sole production renderer.

### Todos

Reviewer residuals F1/F2/F4/F5/F6 are follow-up observations: task-axis role semantics, adjacent palette meaning, live-region scale, shared-store poll rerenders, and the deliberate omission of undefined-status sessions.

## Docs References

No relevant domain documentation was configured in the resolved `system/sources.md`; the contract is proved by repository sources and tests.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No domain reference was available for this UI-local state mapping. | — | — |

## Repo-Internal References

`CockpitShell`/`catalogPoll` hydrate the shared session store, and Operations `LifecycleList` maps
those already-served values through this component. The full-page `SessionRail` is a peer renderer of
the same normalized catalog, not this component's hydration or rendering owner.

| Finding | Citations | Source Path |
| --- | --- | --- |
| `CockpitShell` is the sole catalog driver/reconciler owner for the shared store. | L366-L370 | [Cockpit.tsx](../cockpit/Cockpit.tsx); [catalogPoll.ts](../data/catalogPoll.ts) |
| `LifecycleList` is this component's sole production consumer. | L42-L46; L341 | [LifecycleList.tsx](LifecycleList.tsx) |
| `SessionRail` is a peer renderer of the same normalized session-state catalog. | L442-L463 | [SessionRail.tsx](session-cockpit/SessionRail.tsx) |
| Focused tests cover mapping, exact-leaf-first identity, lifecycle fallback, precedence, missing classification, and omission. | L22-L117 | [ChatActivityIndicator.test.tsx](ChatActivityIndicator.test.tsx) |

## Cross-Repo References

No meaningful cross-repository boundary exists; the component is inside the agents-remember dashboard.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repo reference. | — | — |

## Update History

- 2026-07-18T16:02+02:00 — FEUI MX-FIX-3 / missing FEUI-L8 history repair: replaced retired Chats
  hydration ownership with `CockpitShell`/`catalogPoll`, named `LifecycleList` as the sole production
  consumer, and kept `SessionRail` as a peer catalog renderer only. This explicitly repairs the
  FEUI-L8 body/reference edit that had no matching history entry. Verified against code commit
  `31f58834f86c0d98e26b0896e099a2403a8729ee`.

- 2026-07-12T17:50 — 260712-TRH-L6: created onboarding for the new chat-activity join and indicator. Records exact-leaf-first and unclaimed-lifecycle fallback, deterministic multi-seat precedence, shared Chats hydration ownership, omission of missing/terminal seats, and reviewer residuals F1/F2/F4/F5/F6. Candidate source remains uncommitted; metadata is pinned to the current code HEAD until closeout.
