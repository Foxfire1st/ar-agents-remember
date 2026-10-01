# dashboard/src/data/capabilityCatalog.test.ts

## Governing Overview

[data overview](overview.md)

## Purpose

Unit suite for the pre-session capability store (260715-FEUI-L3 R1/R2) — proves the store can only
ever contain what the daemon actually said: dynamic-only, verbatim errors, drop-on-error, honest
refresh semantics, and miss-cost honesty. Carries the regression tests for review findings 2, 3,
and 4.

## Code Commentary

### Logic

- **State transitions** cit:(["first read: idle → loading → envelope stored whole (cacheStatus hit)"], dashboard/src/data/capabilityCatalog.test.ts:40-55) — first read observes `loading` mid-fetch then settles
  `idle` + envelope stored whole (cacheStatus `hit`); `refresh: true` sends `?refresh=true`,
  shows `refreshing`, and replaces the envelope whole (`refreshed`).
- **Verbatim errors + drop** cit:(["renders 404/409/503 errors with the VERBATIM status + detail and DROPS the envelope"], dashboard/src/data/capabilityCatalog.test.ts:73-91) — loops ALL of `CAPABILITY_ERROR_BODIES` (404 not-installed,
  409 capability-unavailable, 503 control-unavailable): `fetchState: "error"`, error equals the
  verbatim `{httpStatus, status, detail}`, and the previously-held envelope is GONE from both the
  resolved entry and the store (the quarantine mirror). A thrown fetch is
  `{httpStatus: null, status: "transport"}` — never a fallback catalog. A 200 that is not the v1
  envelope is refused, not adopted.
- **Malformed model rows** (L99-L126, review finding 4) — three malformed 200 shapes
  (`models: [null]`, missing fields, non-array `effortOptions`) all land in the honest
  v1-mismatch error path with no envelope adopted.
- **Shapeless error body** (L128-L141, review finding 2) — a non-JSON 502 wears
  `{status: "transport", detail: "HTTP 502"}`, never a server status word.
- **Single-flight + refresh chaining** (L143-L175, review finding 3) — concurrent plain reads
  share ONE request; a gated-promise interleaving proves `refresh: true` never silently joins an
  in-flight plain read: it chains a REAL refresh (exactly 2 fetches, second `?refresh=true`), a
  second refresh joins the chained refresh (no stampede), and refresh callers resolve with the
  `refreshed` envelope.
- **Memory-only** cit:(["snapshots are memory-only"], dashboard/src/data/capabilityCatalog.test.ts:213-216) — a fresh store starts empty; nothing survives a reload.
- **Cost honesty (R2)** cit:(["miss/initial loading and explicit refresh carry the SAME generic cost naming"], dashboard/src/data/capabilityCatalog.test.ts:220-228) — miss/initial and refresh loading copy carry the SAME
  generic `capabilityCostNote`, with a no-digits regex (`/\d+\s*(s|sec|second)/` must not match)
  pinning that no seconds constant ever creeps into the treatment; `cacheStatusNote` names
  whether discovery actually ran (miss reads like refresh).

### Conventions

`vi.stubGlobal("fetch", …)` response stubs (`ok`/`err` literal helpers); the store reset in
`beforeEach`; fixtures from `test/fixtures/capabilityEnvelopes.ts`. Test-only.

### Invariants And Boundaries

The drop-on-error loop and the refresh-chaining interleaving are the regression net for the
dynamic-only ruling and review finding 3: they must keep failing if an error branch ever retains a
stale envelope or a demanded refresh is satisfied by a plain read.

### 2026-07-24 Curator Delta

The suite now drives an abort-aware hung socket through the capability timeout, asserting the normal
transport error and a successful fresh retry after the single-flight slot releases.

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- The module under test. [1]
- The envelope builder + verbatim error-body fixtures the suite loops. [2]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.
