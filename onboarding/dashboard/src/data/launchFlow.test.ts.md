# dashboard/src/data/launchFlow.test.ts

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

- **Selection reducers (R4)** cit:([`chooseModel`, `chooseEffort`, `launchableEfforts`, `launchSelectionBody`, `selectionComplete`, `EMPTY_SELECTION`], dashboard/src/data/launchFlow.ts:31-35; dashboard/src/data/launchFlow.ts:38-40; dashboard/src/data/launchFlow.ts:51-63; dashboard/src/data/launchFlow.ts:66-75; dashboard/src/data/launchFlow.ts:81-83; dashboard/src/data/launchFlow.ts:86-94) — over the recorded Claude/Codex/Pi envelopes:
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
- **Classifier table (R5/R8)** cit:([`classifyOpenResponse`], dashboard/src/data/launchFlow.ts:198-211) — every open fixture: 200-starting → `opened`
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

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- The machines + client under test. [1]
- Recorded-catalog envelope/snapshot builders (incl. the non-launch-settable-default trap). [2]
- The open-response fixtures the classifier table covers exhaustively. [3]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.
