# dashboard/src/data/launchFlow.test.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/launchFlow.test.ts`          |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-07-18T15:22+02:00 |
| lastVerifiedCommitHash | `31f58834f86c0d98e26b0896e099a2403a8729ee`       |
| lastVerifiedCommitDate | 2026-07-18T15:41:39+02:00|
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

- **Selection reducers (R4)** (L35-L128) — over the recorded Claude/Codex/Pi envelopes:
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
- **Classifier table (R5/R8)** (L132-L197) — every open fixture: 200-starting → `opened`
  carrying the requested pair verbatim; 200 vendor-defaults → both knobs null; 400
  `launch-selection-invalid` ×2 (partial pair / non-native, verbatim details); 400 bad-kind →
  `open-refused` with verbatim status+detail; 409 leaf-taken → owning session named; 409
  launch-selection-conflict → the LIVE retained pair, provenance untouched; transport-null / 500
  / 502 / garbage-200 / unrecognized-409 all → `outcome-unknown` (F9).
- **`openHostedSession`** (L199-L247) — asserts the exact POST URL (`/api/terminal/launch-1`)
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

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | `system/sources.md` checked | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The machines + client under test. | L19-L222 | [launchFlow.ts](launchFlow.ts) |
| Recorded-catalog envelope/snapshot builders (incl. the non-launch-settable-default trap). | — | [../test/fixtures/capabilityEnvelopes.ts](../test/fixtures/capabilityEnvelopes.ts) |
| The open-response fixtures the classifier table covers exhaustively. | — | [../test/fixtures/openResponses.ts](../test/fixtures/openResponses.ts) |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Update History

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
