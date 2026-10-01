# dashboard/src/data/conversation-library/store.test.ts

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

- **openedForFocus only on opened/opened** — cit:(["marks openedForFocus ONLY when phase=opened && outcome=opened"], dashboard/src/data/conversation-library/store.test.ts:37-46): a `phase:"opened", outcome:"opened"` response
  sets `openedForFocus === true` and exposes the new `arSessionId`.
- **no focus on a non-opened terminal** — cit:(["does NOT focus on a non-opened terminal outcome (unsupported)"], dashboard/src/data/conversation-library/store.test.ts:48-56): a `422 unsupported` leaves `openedForFocus === false`
  and surfaces `outcome:"unsupported"`.
- **stable requestId across a pending→opened status poll** — cit:(["keeps the SAME requestId across a pending->opened status poll (never a fresh id)"], dashboard/src/data/conversation-library/store.test.ts:58-90): a pending open then an
  `open-status` that opens; every request the fetch saw carried the SAME `req-stable` id (never a
  fresh one).
- **no active-session field exists** — cit:(["activeSessionId"], dashboard/src/data/conversation-library/store.test.ts:95-95): a STRUCTURAL proof — the store's key set contains no
  `activeSessionId`; the library store cannot mark a row live.
- **requestId retained after a transport failure (F6b)** — cit:(["keeps the requestId after a transport failure so a re-attempt reconciles"], dashboard/src/data/conversation-library/store.test.ts:99-106): a dropped POST keeps the
  `requestId`, clears `dispatching`, and records the error so a re-attempt reconciles under the same id.
- **reconcileOpen re-drives open-reconcile under the same id (F6a)** — cit:(["reconcileOpen re-drives open-reconcile under the SAME requestId (F6a)"], dashboard/src/data/conversation-library/store.test.ts:108-128): asserts a
  `/open-reconcile` request under `req-stable` and reaches `openedForFocus`.
- **dispatching from the first call blocks a double-dispatch (F6c)** — cit:(["marks dispatching from the first call so a double-dispatch is blocked (F6c)"], dashboard/src/data/conversation-library/store.test.ts:130-135): a never-resolving
  fetch leaves `dispatching === true` immediately.

### Invariants And Boundaries

- The suite is the durable guard on R4 focus honesty and the F6 fixes; a regression that focuses on a
  non-opened outcome, mints a fresh id on retry, or adds an active-marking field breaks it.
- It uses an injected `setTimeoutImpl` to flush the scheduled poll deterministically (no wall-clock
  waits), matching the store's injectable `pollScheduler`.

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries are
configured. This one-to-one card therefore relies on its direct agents-remember source/tests and the
reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- The store and orchestration verbs under test. [1]
- The open-operation type the `op` fixture builds, and the branded key the suite passes to every verb. [2]
- The `libraryConversationKey` mint that replaced the inline brand cast. [3]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.
