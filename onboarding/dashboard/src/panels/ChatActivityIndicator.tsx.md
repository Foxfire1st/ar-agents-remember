# dashboard/src/panels/ChatActivityIndicator.tsx

| Field                  | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/ChatActivityIndicator.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-12T17:50 |
| lastVerifiedCommitHash | `300664e63f2dbb5f0701d37bbc17ff5358960c77` |
| lastVerifiedCommitDate | 2026-07-12T18:11:57+02:00|
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
- Chats owns catalog hydration. This component adds no poller, classifier, or backend projection.

### Todos

Reviewer residuals F1/F2/F4/F5/F6 are follow-up observations: task-axis role semantics, adjacent palette meaning, live-region scale, shared-store poll rerenders, and the deliberate omission of undefined-status sessions.

## Docs References

No relevant domain documentation was configured in the resolved `system/sources.md`; the contract is proved by repository sources and tests.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No domain reference was available for this UI-local state mapping. | — | — |

## Repo-Internal References

The shared session store and Chats surface are the canonical hydration and turn-state owners; Operations only maps the already-served catalog values.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The canonical Chats rail renders the same normalized session-state catalog used here. | SessionRail source and panels overview | [SessionRail.tsx](session-cockpit/SessionRail.tsx); [panels overview](overview.md) |
| Focused tests cover mapping, exact-leaf-first identity, lifecycle fallback, precedence, missing classification, and omission. | L22-L117 | [ChatActivityIndicator.test.tsx](ChatActivityIndicator.test.tsx) |

## Cross-Repo References

No meaningful cross-repository boundary exists; the component is inside the agents-remember dashboard.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repo reference. | — | — |

## Update History

- 2026-07-12T17:50 — 260712-TRH-L6: created onboarding for the new chat-activity join and indicator. Records exact-leaf-first and unclaimed-lifecycle fallback, deterministic multi-seat precedence, shared Chats hydration ownership, omission of missing/terminal seats, and reviewer residuals F1/F2/F4/F5/F6. Candidate source remains uncommitted; metadata is pinned to the current code HEAD until closeout.
