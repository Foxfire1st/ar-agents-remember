# dashboard/src/data/setClient.ts

## Governing Overview

[data overview](overview.md)

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

## Evidence

### Docs References

No Domain Documentation source is configured.

No external domain citation applies.

### Repo-Internal References

- Exact snapshot, set, pair, cycling, acknowledgment, and watcher orchestration. [1]
- Full I/O and transition regression matrix. [2]
- Acceptance and readback policy. [3]
- Pair serialization machine. [4]
- Store state and mutation boundary. [5]

### Cross-Repo References

No meaningful cross-repo boundary is owned here.

No cross-repo evidence applies.

## FEUI-L8 Reviewed Candidate Delta

Adds a dev-scenario generation around exact-session snapshot single-flight state. Retired requests may resolve to their caller but cannot write into a successor scenario that reuses the session id.

The reviewed candidate is still uncommitted. Existing verification hash/date remain pinned to the
leaf base; closeout owns commit stamping.
