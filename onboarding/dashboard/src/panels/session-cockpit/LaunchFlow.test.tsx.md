# dashboard/src/panels/session-cockpit/LaunchFlow.test.tsx

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

The LaunchFlow jsdom matrix (260715-FEUI-L3 S2/S3/S6): dynamic-only pickers, miss/refresh
cost-naming parity, complete-pair gating with default re-gating, advertised-order rendering, all
four open-response paths, and the F9 unknown-outcome catalog reconciliation — including the two
fix-round regression nets (dismiss ends the watch; reopen starts clean).

## Code Commentary

### FEUI MX-FIX-2 Canonical Response Fixture

The URL router now returns real `Response` text bodies rather than a partial object with only
`json()`. Existing chooser, refusal, conflict, and unknown-outcome cases therefore cross the sole
opener's body-read/parser boundary without changing their launch-flow expectations.

### FEUI-L9R Reviewed Candidate Delta

The suite now proves first-read failure and operator retry, held-read timeout/abort, malformed-200
protocol errors, honest empty state, one replacement read per changed or first-observed serving boot,
rejection of a late superseded completion, close-time abort, and independence from SSE loss.

**Superseded by 260731-EFA-L4 — read this before trusting the sentence it replaces.** This section
used to end "a stale legacy `control: "starting"` field is explicitly not rendered because no adapter
process exists before open." That is no longer what the suite does. The `control: "starting"` key is
gone from all three `HARNESSES` rows, because `serving/response_contract.py::DetectedHarness` declares
exactly `id`/`name`/`detected` and is `extra="forbid"` — the daemon could never have sent it, and no
dashboard code read it. The `not.toContain("adapter starting")` assertions at L167-L178 remain, but
with nothing planting the field they no longer catch anything; the guarantee they used to carry now
lives in the describe below.

### Logic

- **Catalog-body conformance (260731-EFA-L4)** cit:(["Object.keys(row).sort()"], dashboard/src/panels/session-cockpit/LaunchFlow.test.tsx:128-128) — the file's own `HARNESSES` fixture is
  asserted to advertise EXACTLY `["detected", "id", "name"]` per row, via `Object.keys(row).sort()`.
  This is the only guarantee in the file that the served catalog body is one the daemon could send,
  and it exists because two cheaper mechanisms cannot provide it. The `HARNESSES` const is now
  annotated `{ harnesses: HarnessInfo[] }` cit:(["export interface HarnessInfo"], dashboard/src/data/harnessCatalog.ts:5-5), which makes a field added
  to a FRESH row literal fail `tsc -b`; the runtime loop additionally catches a row spread in from
  elsewhere or a key written onto the array afterwards. Neither `tsc` nor `test/wireFixtureGuard.ts`
  covered this before, because `harnessCatalog.ts` carries no `// TypeScript mirror of` header and so
  is not wire vocabulary to the guard. **That blind spot is not closed** — the guard's own note lists
  five live instances (`data/harnessCatalog.ts`, `data/submissionLifecycleClient.ts`,
  `data/changeset.ts`, `data/files.ts`, `data/notes.ts`); this file is guarded, the class is not.
- **Dynamic-only (R1/R4)** cit:(["LaunchFlow — dynamic-only pickers (R1/R4)"], dashboard/src/panels/session-cockpit/LaunchFlow.test.tsx:133-214) — the gated-promise case proves ZERO model options exist
  BEFORE the daemon answers (the capability response is held behind an unresolved promise while
  the loading state is asserted), then the released envelope populates the five Claude rows in
  advertised order; an undetected harness is disabled, and the chooser is asserted never to say
  "adapter starting" (L167-L178 — note this negative no longer has a plant behind it, see the
  superseded-delta note above); a hidden codex row never renders; a 503 renders
  the VERBATIM `control-unavailable: …` detail with a working retry cit:(["capability-route errors render the VERBATIM status+detail with a retry (never an empty menu)"], dashboard/src/panels/session-cockpit/LaunchFlow.test.tsx:189-213).
- **Harness-catalog recovery** cit:(["LaunchFlow — owned harness-catalog recovery (L9R R3/R4)"], dashboard/src/panels/session-cockpit/LaunchFlow.test.tsx:216-386) — failure, timeout, protocol error, honest empty,
  operator Retry, close/supersession abort, boot-owned replacement, stale completion rejection, and
  SSE-loss independence are separate asserted states.
- **Cost honesty (R2)** cit:(["LaunchFlow — cost honesty (R2)"], dashboard/src/panels/session-cockpit/LaunchFlow.test.tsx:388-411) — miss-loading and the explicit refresh carry the SAME
  `capabilityCostNote` naming; the loaded state names the cache truth ("cache miss …same
  short-lived native discovery as a refresh").
- **Complete-pair rules (R4)** cit:(["LaunchFlow — complete-pair rules (R4)"], dashboard/src/panels/session-cockpit/LaunchFlow.test.tsx:413-471) — model selection re-gates effort to THAT row's
  advertised default and re-gates again on switch (sol=low → spark=high); a model with no
  advertised launch default disables submit until an explicit effort choice; efforts render in
  advertised native order (`low…ultra`, asserted as an ordered array); the effortless Haiku row
  states no pair can be formed and submit stays disabled; vendor defaults sends NEITHER knob —
  asserted by key ABSENCE in the parsed POST body cit:(["vendor defaults sends NEITHER knob on the wire"], dashboard/src/panels/session-cockpit/LaunchFlow.test.tsx:457-470).
- **Response paths (R5)** cit:(["LaunchFlow — response paths (R5)"], dashboard/src/panels/session-cockpit/LaunchFlow.test.tsx:473-740) — 200 ⇒ retained pair recorded at tier `'pending'` in
  `sessionCockpitStore`, new session focused, flow closed; 400 `launch-selection-invalid` ⇒ the
  verbatim detail, nothing retried; 409 leaf-taken ⇒ names the owning session + focus-owner
  action; 409 conflict ⇒ live retained pair vs attempted rendered side by side AND the store is
  asserted to hold NO evidence for the live session; transport loss ⇒ "open outcome unknown —
  checking the catalog", resolved WITHOUT re-POST when the caller-minted id appears in a
  rerendered `sessions` prop (F9).
- **Fix-round regression nets** cit:(["an explicit dismiss ENDS the unknown-outcome watch — a late row never steals focus (review finding 1)", "REOPEN after a dismissed unknown outcome starts clean — the stale id never fires (delta-verify residual)"], dashboard/src/panels/session-cockpit/LaunchFlow.test.tsx:654-695; dashboard/src/panels/session-cockpit/LaunchFlow.test.tsx:697-739) — "an explicit dismiss ENDS the unknown-outcome
  watch" (review finding 1): dismiss, then the row surfaces while `open=false` — `onFocusSession`
  never fires and `onClose` stays at one call; "REOPEN after a dismissed unknown outcome starts
  clean" (the delta-verify residual): the row lands while closed, the flow reopens — the stale id
  must not fire on the first effect pass.

### Conventions

`stubFetch(router)` stubs a URL-routing global fetch (L45-L71; `defaultRouter` at L73-L86 wires the
harness list, claude/codex envelopes, and a parameterized open response); cit:([`renderFlow`], dashboard/src/panels/session-cockpit/LaunchFlow.test.tsx:88-102) pins
`mintSessionId={() => "launch-1"}` so the F9 assertions can address the minted id; both stores
reset in `beforeEach`. The `HARNESSES` body `defaultRouter` serves is a TYPE-ANNOTATED const
cit:(["const HARNESSES: { harnesses: HarnessInfo[] }"], dashboard/src/panels/session-cockpit/LaunchFlow.test.tsx:27-27), not a bare literal — that annotation is half of the conformance guarantee described in the
first Logic bullet. Test-only.

### Invariants And Boundaries

The gated-promise case is the dynamic-only regression net (it fails if ANY option is invented
before the daemon answers, not merely if options eventually differ); the vendor-defaults case
pins wire-level key ABSENCE; the two F9 cases are the fix-round nets and fail against pre-fix
code in exactly the reviewed failure modes.

### Todos

No task-independent technical debt was identified during FEUI-L9R review.

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

No relevant domain documentation was found for this file.

### Repo-Internal References

- The dialog under test. [1]
- The envelope fixtures the routers serve. [2]
- The open-response fixtures (200/400/409×2). [3]
- The shared row builder used for the F9 appeared-row rerenders. [4]
- The store the 200-path evidence assertion reads. [5]
- `HarnessInfo` — the three-field type the `HARNESSES` const is annotated with, and its runtime `parseHarness` validator. [6]
- `DetectedHarness` — the server model that fixes the three fields; `WireResponse` is what makes it `extra="forbid"`. [7]
- The guard whose vocabulary is discovered from a `// TypeScript mirror of` header, and its own note naming the five unmarked modules `harnessCatalog.ts` is one of. [8]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.

## FEUI-L8 Reviewed Candidate Delta

Adds lifecycle inheritance and create-invalidation assertions plus a deferred-open race proving a launch owned by a retired dev scenario cannot hydrate, focus, close, broadcast, or alter successor poll health.

The reviewed candidate is still uncommitted. Existing verification hash/date remain pinned to the
leaf base; closeout owns commit stamping.
