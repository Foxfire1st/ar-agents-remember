# dashboard/src/data/setClient.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/setClient.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-17T08:33+02:00 |
| lastVerifiedCommitHash | `4293c53b9d6ef2bf0fee7aca11c2677322c4e786` |
| lastVerifiedCommitDate | 2026-07-17T10:26:02+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

The sole live-session set-control I/O driver: exact-session snapshot reads, model/effort POSTs,
serialized pair changes, effort cycling, acknowledgment, and promotion/drift observation.

## Code Commentary

### Logic

- `refreshSessionSnapshot` single-flights GETs by session, mirrors either the whole snapshot or
  the verbatim classified error, and resolves queued/unknown pendings by readback.
- `sendSet` POSTs the exact model/effort route, treats every valid SetResult as evidence, and
  keeps route failures separate. `applySetResult` appends all evidence, supersede-guards the
  current pending, moves effective values only from echo evidence, and performs one automatic
  readback for `unknown`.
- Pair changes serialize model evidence before effort. Route termination records unknown
  effectiveness; SetResult-backed refusal preserves the stronger evidence wording.
- The refcounted promotion watcher re-GETs focused turn-ended sessions, queued/unknown background
  sessions at turn end, and sessions that gain focus.

### Conventions

Pure policy stays in `setAcceptance.ts`, `pairChange.ts`, and `sessionCapabilities.ts`; this module
only sequences I/O and store writes. Announcements are emitted only for the focused session.

### Invariants And Boundaries

No request or in-flight state moves an effective marker. HTTP failures never become SetResults,
and an older response never clears a newer request's pending state.

### Todos

- Reviewer sev-4 observation 5: a `turn-ended` transition that occurs entirely between observed
  session-store snapshots cannot trigger the promotion watcher.
- Reviewer sev-4 observation 8: the automatic unknown readback can join an already in-flight
  exact-session GET rather than force a later post-result GET.

## Docs References

No Domain Documentation source is configured.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No external domain citation applies. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Exact snapshot, set, pair, cycling, acknowledgment, and watcher orchestration. | L1-L433 | [setClient.ts](setClient.ts) |
| Full I/O and transition regression matrix. | L63-L694 | [setClient.test.ts](setClient.test.ts) |
| Acceptance and readback policy. | L1-L250 | [setAcceptance.ts](setAcceptance.ts) |
| Pair serialization machine. | L1-L205 | [pairChange.ts](pairChange.ts) |
| Store state and mutation boundary. | L1-L425 | [sessionCockpitStore.ts](sessionCockpitStore.ts) |

## Cross-Repo References

No meaningful cross-repo boundary is owned here.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repo evidence applies. | — | — |

## Update History

- 2026-07-17T08:33+02:00 — Created for 260715-FEUI-L4 R1–R8 through fix round 3 and final
  reviewer PASS. Sev-4 observations 5 and 8 remain recorded. Verification metadata is pinned to
  the contract base until the uncommitted code lands.
