# dashboard/src/data/launchFlow.ts

## Governing Overview

[data overview](overview.md)

## Purpose

The **launch-flow state machines and classifying open client** (260715-FEUI-L3 R4/R5), pure so
vitest tables can be exhaustive (R8). Encodes the LAUNCH RULES: a selection is a COMPLETE pair or
vendor defaults (both omitted) — a partial pair is unrepresentable on the wire; effort menus are
the selected model's advertised menu filtered `launchSettable` in advertised NATIVE order (never
reordered, never emphasized — decoy-anchor discipline); keys are used verbatim (Pi's
provider-qualified `provider/id` form is never stripped); no default is ever invented client-side.
The UI shell that renders these machines is `panels/session-cockpit/LaunchFlow.tsx`.

## Code Commentary

### FEUI MX-FIX-2 Sole-Opener Delegation

`openHostedSession` no longer performs its own fetch or JSON read. It delegates the complete
harness request to `terminalOpen.openTerminalSession`: accepted server row facts map to `opened`,
recognized HTTP/harness refusals retain the existing launch classifier grammar, and
network/protocol/missing-response failures map to the existing `outcome-unknown` reconciliation
path. This preserves the caller-minted-id catalog watch without creating a second opener.

### Logic

- `LaunchSelectionState` / cit:([`EMPTY_SELECTION`], dashboard/src/data/launchFlow.ts:27-31) — `{modelKey, effort, vendorDefaults}`;
  `vendorDefaults: true` is the EXPLICIT selectionless choice (send NEITHER knob).
- cit:([`launchableEfforts`], dashboard/src/data/launchFlow.ts:38-40) — `effortOptions.filter(launchSettable)`; a `filter` only,
  no `.sort()` anywhere (advertised order preserved — reviewer-grepped).
- cit:([`chooseModel`], dashboard/src/data/launchFlow.ts:47-59) — picking a model RE-GATES effort: that row's
  advertised `defaultEffort` only when it is itself in the launch-settable menu, otherwise `null`
  (the flow demands an explicit choice — a non-launch-settable default is never silently
  selected). An unadvertised key returns `EMPTY_SELECTION` (dynamic-only ⇒ not selectable; this
  is also why a corrected-launch prefill can never re-offer a key the live catalog dropped).
- cit:([`chooseEffort`], dashboard/src/data/launchFlow.ts:62-71) — accepts only the CURRENT model's
  advertised launchable menu; anything else leaves the selection unchanged.
- cit:([`selectionComplete`], dashboard/src/data/launchFlow.ts:81-83) / cit:([`launchSelectionBody`], dashboard/src/data/launchFlow.ts:82-90) — complete = vendor defaults OR
  both knobs; the body emits `{model, effort}` or `{}` and THROWS on any partial pair
  ("complete the pair or choose vendor defaults") — partiality is unrepresentable.
- cit:([`OpenOutcome`], dashboard/src/data/launchFlow.ts:95-126) — one normalized outcome per server path, each rendered verbatim by
  the flow: `opened` (200 + session, carrying the REQUESTED pair verbatim — tier 'pending', never
  proof), `launch-selection-invalid` (400, partial-pair/non-native detail),
  `open-refused` (other 400, verbatim status+detail), `leaf-taken` (409, names the owning
  session), `launch-selection-conflict` (409, the LIVE row's retained pair vs attempted —
  provenance never rewritten), `outcome-unknown` (transport/5xx/unrecognized — design §7.1 F9).
- cit:([`classifyOpenResponse`], dashboard/src/data/launchFlow.ts:198-211) — the pure classifier; `httpStatus: null`
  = the fetch threw. Unrecognized 200s/409s/5xx all fall through to `outcome-unknown` with an
  honest detail line.
- `openHostedSession(sessionId, request, base)` — delegates to the sole opener with
  `kind: "harness"` + `launchSelectionBody(selection)` (+ optional label/leafKey/lifecycleId),
  then maps its typed result into the established launch response paths. The session id is
  **CALLER-minted**, so an unknown outcome reconciles against the catalog BY ID (does the row
  exist on a later poll) — never a blind re-POST with a fresh id.

### Conventions

State transitions remain pure and table-testable. The open adapter preserves canonical launch copy
while delegating transport and accepted-row validation to `terminalOpen.ts`.

### Invariants And Boundaries

- A partial pair cannot leave this module: `selectionComplete` gates the submit,
  `launchSelectionBody` throws, and `chooseEffort` refuses off-menu keys — tested from both
  directions.
- Advertised NATIVE order is preserved end-to-end; nothing here sorts or ranks efforts.
- Catalog validity is NOT checked at open time by the server (`resolve_terminal_open_selection`
  raises only for non-native kind/harness and split pairs) — a bad-but-complete pair opens
  200/'starting' and fails asynchronously; that path belongs to the tier machine + banner.
- On `outcome-unknown` the caller keeps the selection and the minted id; resolution is the
  ordinary catalog poll (F9).

### Todos

No task-independent technical debt was identified during MX-FIX-2 review.

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- Selection reducers, wire-body rule, classifier, and the classifying open client. [1]
- The capability wire types the reducers read (snapshot/model/effort rows). [2]
- The open-response wire shapes this classifies (200/400/409×2 bodies). [3]
- The server's synchronous-refusal boundary (split pair / non-native only). [4]
- The dialog rendering these machines (options exclusively from the envelope). [5]
- Open-response fixtures the classifier is table-tested over. [6]
- The unit suite (reducer tables, classifier table, POST-body assertions). [7]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.
