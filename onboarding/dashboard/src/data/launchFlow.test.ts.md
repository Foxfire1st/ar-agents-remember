# dashboard/src/data/launchFlow.test.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/launchFlow.test.ts`          |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-07-18T15:22+02:00 |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f`       |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[data overview](overview.md)

## Purpose

Unit suite for the launch-flow machines and open client (260715-FEUI-L3 R4/R5/R8) — reducer
tables over the recorded-catalog fixtures plus the classifier table over EVERY open-response
fixture, with POST-body assertions from both directions (complete pair present; vendor defaults
absent).

## Code Commentary

### FEUI MX-FIX-2 Delegation Fixture Update

The hosted-open tests now provide real `Response` text bodies so they exercise the canonical
opener's read/parse boundary. Complete-pair and vendor-defaults requests retain the same one-POST
body assertions and outcome grammar; the fixture change ensures these tests cannot accidentally
pass through the removed direct `response.json()` implementation.

### Logic

- **Selection reducers (R4)** cit:([`chooseModel`, `chooseEffort`, `launchableEfforts`, `launchSelectionBody`, `selectionComplete`, `EMPTY_SELECTION`], dashboard/src/data/launchFlow.ts:27-31; dashboard/src/data/launchFlow.ts:34-36; dashboard/src/data/launchFlow.ts:47-59; dashboard/src/data/launchFlow.ts:62-71; dashboard/src/data/launchFlow.ts:77-79; dashboard/src/data/launchFlow.ts:82-90) — over the recorded Claude/Codex/Pi envelopes:
  Codex `gpt-5.6-sol` re-gates effort to its advertised `low`, switching to `spark` re-gates to
  `high` (never carried over); Claude rows advertise no default ⇒ effort `null`, selection
  incomplete; a `defaultEffort` that is NOT launch-settable is not silently selected (the trap
  case, via `preSessionSnapshot`/`modelRow` builders); an unadvertised model returns
  `EMPTY_SELECTION`; `chooseEffort` accepts only the current model's launchable menu;
  `launchableEfforts` filters WITHOUT reordering (advertised native order pinned); the observed
  Haiku row (no effortOptions) can NEVER form a complete pair; Pi provider-qualified keys are
  verbatim and a bare id matches nothing; `launchSelectionBody` emits both knobs or `{}` and
  throws `/incomplete/` on either partial; the fresh-Claude exact-session snapshot keeps
  `selectedEffort` null with only the model config category.
- **Classifier table (R5/R8)** cit:([`classifyOpenResponse`], dashboard/src/data/launchFlow.ts:182-195) — every open fixture: 200-starting → `opened`
  carrying the requested pair verbatim; 200 vendor-defaults → both knobs null; 400
  `launch-selection-invalid` ×2 (partial pair / non-native, verbatim details); 400 bad-kind →
  `open-refused` with verbatim status+detail; 409 leaf-taken → owning session named; 409
  launch-selection-conflict → the LIVE retained pair, provenance untouched; transport-null / 500
  / 502 / garbage-200 / unrecognized-409 all → `outcome-unknown` (F9).
- **`openHostedSession`** cit:([`openHostedSession`], dashboard/src/data/launchFlow.ts:232-250) — asserts the exact POST URL (`/api/terminal/launch-1`)
  and body `{kind, harness, model, effort, label}` for a complete pair; a vendor-defaults launch
  sends NEITHER knob (`"model" in body === false`); a thrown fetch becomes `outcome-unknown`
  (the caller keeps the id and reconciles).

### Conventions

Pure tables + `vi.stubGlobal("fetch")` for the client cases; fixtures from
`test/fixtures/{capabilityEnvelopes,openResponses}.ts`. Test-only.

### Invariants And Boundaries

The partial-pair throws, the no-reorder pin, the bare-Pi-id refusal, and the vendor-defaults
key-ABSENCE assertion are the launch-rule regression net — each fails loudly if a default is ever
invented, a menu is sorted, a key is normalized, or a lone knob rides the wire.

### Todos

No task-independent technical debt was identified during MX-FIX-2 review.

## Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The machines + client under test. | `launchSelectionBody` | dashboard/src/data/launchFlow.ts:82-90 |
| Recorded-catalog envelope/snapshot builders (incl. the non-launch-settable-default trap). | `modelRow`; `preSessionSnapshot` | dashboard/src/test/fixtures/capabilityEnvelopes.ts:34-52; dashboard/src/test/fixtures/capabilityEnvelopes.ts:156-158 |
| The open-response fixtures the classifier table covers exhaustively. | `OPENED_STARTING`; `OPENED_VENDOR_DEFAULTS`; `INVALID_PARTIAL_PAIR` | dashboard/src/test/fixtures/openResponses.ts:17-33; dashboard/src/test/fixtures/openResponses.ts:36-43; dashboard/src/test/fixtures/openResponses.ts:46-49 |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-03T04:00:52+02:00 — 260731-EFA-L6 W3-B06 curator: curated 9 citation findings, converting 3 legacy prose line references and 3 unanchored/malformed fixture rows into exact citations.

- 2026-07-31T18:05+02:00 — 260731-EFA-L2 curator: re-derived 1 stale self-citation. The
  `openHostedSession` describe block ends at the last line of the file, so its range was corrected
  from the out-of-bounds L199-L247 to L199-L245 (the file is 245 lines); the three cases inside
  (complete-pair POST body, vendor-defaults knob absence, thrown-fetch `outcome-unknown`) are
  unchanged and were read back.

- 2026-07-18T15:22+02:00 — FEUI MX-FIX-2: moved complete-pair, vendor-defaults, and thrown-fetch
  client cases onto the shared authoritative opener response path without changing launch-selection
  or F9 reconciliation expectations. Verification metadata remains pinned until closeout.

- 2026-07-18T07:22+02:00 — FEUI-L8 manual route refactor: retargeted this direct data file card
  from the packed dashboard/src parent to the new nearest data authority overview. Source behavior
  is unchanged by this memory-only governance move; verification hash/date remain pinned.

- 2026-07-17T06:10+02:00 — Created for 260715-FEUI-L3 R4/R5/R8: reducer tables (re-gate,
  non-launch-settable-default trap, advertised-order pin, Haiku effortless, Pi verbatim keys,
  both-or-neither body), the classifier table over every open fixture incl. the F9
  unknown-outcome sweep, and the POST-body assertions (complete pair / vendor-defaults knob
  absence / thrown-fetch reconciliation). Verification metadata pinned to the leaf base until
  closeout stamps the L3 code commit.
