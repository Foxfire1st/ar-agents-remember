# dashboard/src/panels/session-cockpit/LaunchFlow.test.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/session-cockpit/LaunchFlow.test.tsx` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-01T10:15+02:00                           |
| lastVerifiedCommitHash | `e52edaf5b655f495580efd93306afdf922b19b51`       |
| lastVerifiedCommitDate | 2026-08-01T11:01:51+02:00|
| governingOverview      | `overview.md`                                   |

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

- **Catalog-body conformance (260731-EFA-L4)** (L121-L131) — the file's own `HARNESSES` fixture is
  asserted to advertise EXACTLY `["detected", "id", "name"]` per row, via `Object.keys(row).sort()`.
  This is the only guarantee in the file that the served catalog body is one the daemon could send,
  and it exists because two cheaper mechanisms cannot provide it. The `HARNESSES` const is now
  annotated `{ harnesses: HarnessInfo[] }` (`data/harnessCatalog.ts` L5-L9), which makes a field added
  to a FRESH row literal fail `tsc -b`; the runtime loop additionally catches a row spread in from
  elsewhere or a key written onto the array afterwards. Neither `tsc` nor `test/wireFixtureGuard.ts`
  covered this before, because `harnessCatalog.ts` carries no `// TypeScript mirror of` header and so
  is not wire vocabulary to the guard. **That blind spot is not closed** — the guard's own note lists
  five live instances (`data/harnessCatalog.ts`, `data/submissionLifecycleClient.ts`,
  `data/changeset.ts`, `data/files.ts`, `data/notes.ts`); this file is guarded, the class is not.
- **Dynamic-only (R1/R4)** (L133-L214) — the gated-promise case proves ZERO model options exist
  BEFORE the daemon answers (the capability response is held behind an unresolved promise while
  the loading state is asserted), then the released envelope populates the five Claude rows in
  advertised order; an undetected harness is disabled, and the chooser is asserted never to say
  "adapter starting" (L167-L178 — note this negative no longer has a plant behind it, see the
  superseded-delta note above); a hidden codex row never renders; a 503 renders
  the VERBATIM `control-unavailable: …` detail with a working retry (L189-L214).
- **Harness-catalog recovery (L216-L386)** — failure, timeout, protocol error, honest empty,
  operator Retry, close/supersession abort, boot-owned replacement, stale completion rejection, and
  SSE-loss independence are separate asserted states.
- **Cost honesty (R2)** (L388-L411) — miss-loading and the explicit refresh carry the SAME
  `capabilityCostNote` naming; the loaded state names the cache truth ("cache miss …same
  short-lived native discovery as a refresh").
- **Complete-pair rules (R4)** (L413-L471) — model selection re-gates effort to THAT row's
  advertised default and re-gates again on switch (sol=low → spark=high); a model with no
  advertised launch default disables submit until an explicit effort choice; efforts render in
  advertised native order (`low…ultra`, asserted as an ordered array); the effortless Haiku row
  states no pair can be formed and submit stays disabled; vendor defaults sends NEITHER knob —
  asserted by key ABSENCE in the parsed POST body (L457-L470).
- **Response paths (R5)** (L473-L652) — 200 ⇒ retained pair recorded at tier `'pending'` in
  `sessionCockpitStore`, new session focused, flow closed; 400 `launch-selection-invalid` ⇒ the
  verbatim detail, nothing retried; 409 leaf-taken ⇒ names the owning session + focus-owner
  action; 409 conflict ⇒ live retained pair vs attempted rendered side by side AND the store is
  asserted to hold NO evidence for the live session; transport loss ⇒ "open outcome unknown —
  checking the catalog", resolved WITHOUT re-POST when the caller-minted id appears in a
  rerendered `sessions` prop (F9).
- **Fix-round regression nets** (L654-L739) — "an explicit dismiss ENDS the unknown-outcome
  watch" (review finding 1): dismiss, then the row surfaces while `open=false` — `onFocusSession`
  never fires and `onClose` stays at one call; "REOPEN after a dismissed unknown outcome starts
  clean" (the delta-verify residual): the row lands while closed, the flow reopens — the stale id
  must not fire on the first effect pass.

### Conventions

`stubFetch(router)` stubs a URL-routing global fetch (L45-L71; `defaultRouter` at L73-L86 wires the
harness list, claude/codex envelopes, and a parameterized open response); `renderFlow` (L88-L113) pins
`mintSessionId={() => "launch-1"}` so the F9 assertions can address the minted id; both stores
reset in `beforeEach`. The `HARNESSES` body `defaultRouter` serves is a TYPE-ANNOTATED const
(L27-L33), not a bare literal — that annotation is half of the conformance guarantee described in the
first Logic bullet. Test-only.

### Invariants And Boundaries

The gated-promise case is the dynamic-only regression net (it fails if ANY option is invented
before the daemon answers, not merely if options eventually differ); the vendor-defaults case
pins wire-level key ABSENCE; the two F9 cases are the fix-round nets and fail against pre-fix
code in exactly the reviewed failure modes.

### Todos

No task-independent technical debt was identified during FEUI-L9R review.

## Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant domain documentation was found for this file. | Source discovery checked | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The dialog under test. | L165-L613 | [LaunchFlow.tsx](LaunchFlow.tsx) |
| The envelope fixtures the routers serve. | L1-L273 | [../../test/fixtures/capabilityEnvelopes.ts](../../test/fixtures/capabilityEnvelopes.ts) |
| The open-response fixtures (200/400/409×2). | L1-L178 | [../../test/fixtures/openResponses.ts](../../test/fixtures/openResponses.ts) |
| The shared row builder used for the F9 appeared-row rerenders. | L10-L27 | [../../test/fixtures/catalogRows.ts](../../test/fixtures/catalogRows.ts) |
| The store the 200-path evidence assertion reads. | — | [../../data/sessionCockpitStore.ts](../../data/sessionCockpitStore.ts) |
| `HarnessInfo` — the three-field type the `HARNESSES` const is annotated with, and its runtime `parseHarness` validator. | L5-L9; L22-L40 | [../../data/harnessCatalog.ts](../../data/harnessCatalog.ts) |
| `DetectedHarness` — the server model that fixes the three fields; `WireResponse` is what makes it `extra="forbid"`. | L88-L100; L355-L366 | [serving/response_contract.py](../../../../mcp/src/agents_remember/serving/response_contract.py) |
| The guard whose vocabulary is discovered from a `// TypeScript mirror of` header, and its own note naming the five unmarked modules `harnessCatalog.ts` is one of. | L40-L63; L108-L112 | [../../test/wireFixtureGuard.ts](../../test/wireFixtureGuard.ts) |

## FEUI-L8 Reviewed Candidate Delta

Adds lifecycle inheritance and create-invalidation assertions plus a deferred-open race proving a launch owned by a retired dev scenario cannot hydrate, focus, close, broadcast, or alter successor poll health.

The reviewed candidate is still uncommitted. Existing verification hash/date remain pinned to the
leaf base; closeout owns commit stamping.

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Update History

- 2026-08-01T10:15+02:00 — 260731-EFA-L4 curator: the card asserted a guarantee the suite no longer
  provides, so it was corrected rather than merely extended. The FEUI-L9R delta ended "a stale legacy
  `control: 'starting'` field is explicitly not rendered"; all three `control: "starting"` keys are
  gone from `HARNESSES` — one per row, and `git diff` over the whole `dashboard/` tree shows these
  three are the only such removals — so the surviving
  `not.toContain("adapter starting")` assertions at L167-L178 have nothing planting the field and can
  no longer fail — the sentence is now flagged superseded, with the reason (`DetectedHarness` declares
  exactly `id`/`name`/`detected` and `WireResponse` sets `extra="forbid"`, so the daemon could never
  send it, and nothing in the dashboard read it). Documented the replacement guarantee as a new Logic
  bullet: the describe at L121-L131 asserts `Object.keys(row).sort()` equals `["detected","id","name"]`
  per row, backed by the new `const HARNESSES: { harnesses: HarnessInfo[] }` annotation which catches
  the fresh-literal case at `tsc -b`. I checked the guard rather than assuming the hole is closed:
  `test/wireFixtureGuard.ts` discovers vocabulary from a `// TypeScript mirror of` first-line marker
  (L108-L112), `harnessCatalog.ts` has none, and the guard's own note (L40-L63) lists five live
  instances — `harnessCatalog.ts`, `submissionLifecycleClient.ts`, `changeset.ts`, `files.ts`,
  `notes.ts` — so the card says this FILE is guarded and the CLASS is not. Suite re-run: passes.
  Citation repairs, all six Logic ranges plus Conventions, each re-anchored on its describe or helper:
  dynamic-only L85-L165 → L133-L214 (inner L151-L162 → L167-L178, L140-L164 → L189-L214); catalog
  recovery L200-L370 → L216-L386; cost honesty L167-L190 → L388-L411; complete-pair L192-L250 →
  L413-L471 (inner L236-L249 → L457-L470); response paths L252-L337 → L473-L652; fix-round nets
  L339-L424 → L654-L739; `stubFetch` L28-L57 → L45-L71 with `defaultRouter` L73-L86 and `renderFlow`
  L88-L113 named separately. Three reference rows added.

- 2026-07-18T15:22+02:00 — FEUI MX-FIX-2: changed the launch-flow router to real HTTP responses so
  the full component matrix exercises the sole authoritative opener. Verification metadata remains
  pinned until closeout.

- 2026-07-18T12:43+02:00 — FEUI-L9R: replaced the retired adapter-word claim with the complete
  catalog timeout/abort/retry/boot-replacement regression matrix; verification metadata remains
  pinned pending candidate closeout.

- 2026-07-18T07:22+02:00 — Curated the final same-reviewer-PASS FEUI-L8 behavior above using direct
  source/test/task evidence; no Domain Documentation source is configured.

- 2026-07-17T06:10+02:00 — Created for 260715-FEUI-L3 S6 (R1/R2/R4/R5, extended in fix rounds 1-2
  with the dismiss-ends-watch and reopen-starts-clean F9 regression cases and the visible
  adapter-status assertion): the full jsdom matrix over dynamic-only pickers, cost parity, pair
  rules, and every open-response path. Verification metadata pinned to the leaf base until
  closeout stamps the L3 code commit.
