# dashboard/src/data/capabilityCatalog.test.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/capabilityCatalog.test.ts`   |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T06:10+02:00                           |
| lastVerifiedCommitHash | `96e1d6db63454438b57a7485382c27784a60776f`       |
| lastVerifiedCommitDate | 2026-07-17T06:28:52+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

Unit suite for the pre-session capability store (260715-FEUI-L3 R1/R2) — proves the store can only
ever contain what the daemon actually said: dynamic-only, verbatim errors, drop-on-error, honest
refresh semantics, and miss-cost honesty. Carries the regression tests for review findings 2, 3,
and 4.

## Code Commentary

### Logic

- **State transitions** (L29-L60) — first read observes `loading` mid-fetch then settles
  `idle` + envelope stored whole (cacheStatus `hit`); `refresh: true` sends `?refresh=true`,
  shows `refreshing`, and replaces the envelope whole (`refreshed`).
- **Verbatim errors + drop** (L62-L97) — loops ALL of `CAPABILITY_ERROR_BODIES` (404 not-installed,
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
- **Memory-only** (L177-L180) — a fresh store starts empty; nothing survives a reload.
- **Cost honesty (R2)** (L183-L199) — miss/initial and refresh loading copy carry the SAME
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

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The module under test. | L22-L243 | [capabilityCatalog.ts](capabilityCatalog.ts) |
| The envelope builder + verbatim error-body fixtures the suite loops. | — | [../test/fixtures/capabilityEnvelopes.ts](../test/fixtures/capabilityEnvelopes.ts) |

## Update History

- 2026-07-17T06:10+02:00 — Created for 260715-FEUI-L3 R1/R2/R8: state transitions, verbatim
  404/409/503 + transport errors with envelope drop, schema/model-row refusal (review finding 4),
  shapeless-body `transport` default (finding 2), single-flight + chained-refresh interleaving
  (finding 3), memory-only start, and the no-digits cost-honesty pins. Verification metadata
  pinned to the leaf base until closeout stamps the L3 code commit.
