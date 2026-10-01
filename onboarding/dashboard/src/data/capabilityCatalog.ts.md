# dashboard/src/data/capabilityCatalog.ts

## Governing Overview

[data overview](overview.md)

## Purpose

The **pre-session capability catalog store** (260715-FEUI-L3 R1, design §4.2): one envelope per
harness, mirrored from `GET /api/harnesses/{h}/capabilities` and NOTHING else. Memory-only vanilla
zustand — no localStorage, no seeded rows, no persistence: a picker is EMPTY until the daemon
answers and a reload starts from scratch (DYNAMIC-ONLY). No fallback catalog exists anywhere in
this module; on ANY error the harness's envelope is **DROPPED**, mirroring the daemon's own
failed-refresh quarantine (`harness_capability_catalog.py` pops the exact evaluated cache entry) —
a stale success must never masquerade as current after the daemon refused to vouch for it
(worker decision 2, reviewer-verified acceptable). Also home to the R2 **miss-cost honesty** copy
exports the launch flow renders.

## Code Commentary

### Logic

- cit:([`CapabilityFetchState`], dashboard/src/data/capabilityCatalog.ts:23-23) — exactly `idle | loading | refreshing | error`; there is no
  "loaded" word: loaded = `idle` + `envelope` present (`fetchedAt` distinguishes never-fetched).
- cit:([`CapabilityCatalogError`], dashboard/src/data/capabilityCatalog.ts:26-31) — the verbatim error surface `{httpStatus, status, detail}`;
  `httpStatus: null` = the fetch itself threw (transport).
- `capabilityCatalogStore` / `useCapabilityCatalog` / cit:([`harnessCapabilities`], dashboard/src/data/capabilityCatalog.ts:54-56) —
  vanilla store + hook selector + imperative read; cit:([`patchHarness`], dashboard/src/data/capabilityCatalog.ts:58-62) replaces one harness's
  entry whole (envelopes are never merged).
- **R2 cost-honesty exports** cit:(["export function capabilityCostNote(", "export function capabilityLoadingCopy(", "export function cacheStatusNote("], dashboard/src/data/capabilityCatalog.ts:70-70; dashboard/src/data/capabilityCatalog.ts:75-75; dashboard/src/data/capabilityCatalog.ts:82-82): `capabilityCostNote(harness)` = ``starts a short-lived
  native ${harness} process`` — GENERIC, no seconds constant anywhere (observed per-harness
  timings are L5 evidence, never UI constants); `capabilityLoadingCopy(harness, mode)` gives the
  initial/miss loading state the SAME cost naming as refresh ("same cost as an explicit
  refresh"); `cacheStatusNote(cacheStatus)` names post-hoc truth per `hit|miss|refreshed` (miss =
  "the daemon ran the same short-lived native discovery as a refresh").
- `isEffortOption`/`isModelRow` (L98-L119, review finding 4) — validate every field a picker
  actually reads per model row (key/displayName/hidden/selectable, `defaultEffort` null|string,
  `effortOptions` array of {key, displayName, launchSettable, sessionSettable}); `isEnvelope`
  cit:(["function isEnvelope(body: unknown): body is CapabilityEnvelope {"], dashboard/src/data/capabilityCatalog.ts:122-122) checks schema = `CAPABILITY_SCHEMA`, harness, `cacheStatus ∈ hit|miss|refreshed`,
  `installFingerprint`, and `models.every(isModelRow)` — a malformed 200 lands in the honest
  schema-mismatch error path (detail names `ar-harness-capabilities/v1`), never adopted, never a
  later render crash.
- `readError` (L137-L151, review finding 2) — default status word is **`transport`**: the
  server's own vocabulary (`capability-unavailable`/`control-unavailable`) renders only when the
  server's JSON body actually said it; a 502 gateway page reads `transport: HTTP 502`. Detail
  defaults to the honest `HTTP <status>` line — never invented.
- cit:([`fetchHarnessCapabilities`], dashboard/src/data/capabilityCatalog.ts:192-268) — the ONE read path. NEVER
  throws; failures land as `fetchState: "error"` with verbatim detail and resolve the returned
  promise with the per-harness entry (also written to the store). Sets `loading` only on the very
  first read of a harness; a refresh or any re-read over an existing snapshot shows `refreshing`
  (both render the same R2 cost naming). `refresh=true` appends `?refresh=true` (daemon-side
  invalidation, the auth/install-change path).
- **Per-harness single-flight with explicit refresh semantics** (L158-L188, review finding 3):
  `InflightRead {promise, refresh}` — a plain read joins ANYTHING in flight; `refresh: true`
  joins only an in-flight REFRESH, and CHAINS behind an in-flight plain read (the chained entry
  replaces the map slot, then recurses once the plain read settles) so daemon invalidation
  genuinely happens — no concurrent double-GET, no silently-stale result. Slot release is
  identity-guarded both ways (L237-L241: plain's `finally` deletes only `=== started`; the chain
  deletes only `=== chained`) so an older read's completion can never delete a chained refresh's
  entry.

### Invariants And Boundaries

- DYNAMIC-ONLY: the store can only ever contain what the daemon actually said. No fallback
  catalog, no persistence, no merging; envelope replaced whole on success, DROPPED on error.
- Error rendering is verbatim `{status, detail}` — never softened, never caught-and-retried with
  a fallback; server vocabulary only when the server said it.
- Miss and refresh carry the SAME generic cost naming (R2); no digits in the copy.
- The single-flight map is module-level state shared by all consumers (LaunchFlow, future L4/L5
  callers); `refresh: true` is a PROMISE of daemon-side invalidation — never silently satisfied
  by a joined plain read.

### 2026-07-24 Curator Delta

Capability reads are now transport-bounded at 10 seconds. A hung per-harness single-flight request
becomes the ordinary transport error and releases its slot, so a later read can retry instead of
leaving that harness permanently loading.

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- The store, cost-honesty copy, envelope validation, and single-flight/refresh machinery. [1]
- The wire mirror the envelope validates against (`CAPABILITY_SCHEMA`, envelope/snapshot/row types). [2]
- The daemon route + quarantine posture this mirrors (failed refresh pops the cache entry). [3]
- The primary consumer (picker options exclusively from the envelope; verbatim error + retry). [4]
- Envelope/error fixtures (all three cacheStatus values; verbatim 404/409/503 bodies). [5]
- The unit suite (state transitions, verbatim errors, drop-on-error, refresh chaining, malformed rows, cost honesty). [6]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.

## FEUI-L8 Reviewed Candidate Delta

`resetCapabilityCatalogForDev` clears rendered and single-flight capability state and advances a generation. A request owned by the prior bench scenario may resolve, but cannot populate or chain into the successor catalog.

The reviewed candidate is still uncommitted. Existing verification hash/date remain pinned to the
leaf base; closeout owns commit stamping.
