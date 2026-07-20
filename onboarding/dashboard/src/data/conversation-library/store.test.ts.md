# dashboard/src/data/conversation-library/store.test.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/conversation-library/store.test.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-20T22:30+02:00 |
| lastVerifiedCommitHash | `9e6c15d2b2bb663fcd10e26d77d0e4d2795829bd` |
| lastVerifiedCommitDate | 2026-07-20T22:32:02+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[data/conversation-library overview](overview.md)

## Purpose

The R4 open-flow negative-proof suite for the library store — the tests that lock the "focus only on
exact opened proof" contract and the F6 open-flow robustness fixes (caller-stable id, double-dispatch
block, poll-exhaustion re-drive). It drives the real client through an injected `fetch`, so it proves
the store's decisions without a network.

## Code Commentary

### Logic

Helpers: `op(overrides)` builds an `OpenConversationOperation`; `jsonResponse`/`makeFetch` fabricate
route-keyed `Response`s. `beforeEach` resets the store. The seven cases prove:

- **openedForFocus only on opened/opened** (L36-L45): a `phase:"opened", outcome:"opened"` response
  sets `openedForFocus === true` and exposes the new `arSessionId`.
- **no focus on a non-opened terminal** (L47-L55): a `422 unsupported` leaves `openedForFocus === false`
  and surfaces `outcome:"unsupported"`.
- **stable requestId across a pending→opened status poll** (L57-L89): a pending open then an
  `open-status` that opens; every request the fetch saw carried the SAME `req-stable` id (never a
  fresh one).
- **no active-session field exists** (L91-L96): a STRUCTURAL proof — the store's key set contains no
  `activeSessionId`; the library store cannot mark a row live.
- **requestId retained after a transport failure (F6b)** (L98-L105): a dropped POST keeps the
  `requestId`, clears `dispatching`, and records the error so a re-attempt reconciles under the same id.
- **reconcileOpen re-drives open-reconcile under the same id (F6a)** (L107-L127): asserts a
  `/open-reconcile` request under `req-stable` and reaches `openedForFocus`.
- **dispatching from the first call blocks a double-dispatch (F6c)** (L129-L134): a never-resolving
  fetch leaves `dispatching === true` immediately.

### Invariants And Boundaries

- The suite is the durable guard on R4 focus honesty and the F6 fixes; a regression that focuses on a
  non-opened outcome, mints a fresh id on retry, or adds an active-marking field breaks it.
- It uses an injected `setTimeoutImpl` to flush the scheduled poll deterministically (no wall-clock
  waits), matching the store's injectable `pollScheduler`.

## Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries are
configured. This one-to-one card therefore relies on its direct agents-remember source/tests and the
reviewed task evidence for any current behavioral claim.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | `system/sources.md` checked | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The store and orchestration verbs under test. | L3 | [store.ts](store.ts) |
| The open-operation types the fixtures build. | L4 | [types.ts](types.ts) |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Update History

- 2026-07-20T22:30+02:00 — 260718-CHATS-L4 curator: created the sidecar for the R4 open-flow suite —
  focus only on opened/opened, no active-marking field, and the F6a/F6b/F6c robustness proofs
  (stable id across polls, retained id after transport failure, double-dispatch block). Verification is
  pinned to the leaf base (`0be0099`) because the new source file is uncommitted; closeout owns its
  first source stamp.
