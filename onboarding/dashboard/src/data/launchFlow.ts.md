# dashboard/src/data/launchFlow.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/launchFlow.ts`               |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-07-18T15:22+02:00 |
| lastVerifiedCommitHash | `31f58834f86c0d98e26b0896e099a2403a8729ee`       |
| lastVerifiedCommitDate | 2026-07-18T15:41:39+02:00|
| governingOverview | `overview.md` |

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

- `LaunchSelectionState` / `EMPTY_SELECTION` (L19-L30) — `{modelKey, effort, vendorDefaults}`;
  `vendorDefaults: true` is the EXPLICIT selectionless choice (send NEITHER knob).
- `launchableEfforts(model)` (L33-L35) — `effortOptions.filter(launchSettable)`; a `filter` only,
  no `.sort()` anywhere (advertised order preserved — reviewer-grepped).
- `chooseModel(snapshot, modelKey)` (L46-L58) — picking a model RE-GATES effort: that row's
  advertised `defaultEffort` only when it is itself in the launch-settable menu, otherwise `null`
  (the flow demands an explicit choice — a non-launch-settable default is never silently
  selected). An unadvertised key returns `EMPTY_SELECTION` (dynamic-only ⇒ not selectable; this
  is also why a corrected-launch prefill can never re-offer a key the live catalog dropped).
- `chooseEffort(snapshot, selection, effortKey)` (L61-L70) — accepts only the CURRENT model's
  advertised launchable menu; anything else leaves the selection unchanged.
- `selectionComplete` (L76-L78) / `launchSelectionBody` (L81-L89) — complete = vendor defaults OR
  both knobs; the body emits `{model, effort}` or `{}` and THROWS on any partial pair
  ("complete the pair or choose vendor defaults") — partiality is unrepresentable.
- `OpenOutcome` (L94-L125) — one normalized outcome per server path, each rendered verbatim by
  the flow: `opened` (200 + session, carrying the REQUESTED pair verbatim — tier 'pending', never
  proof), `launch-selection-invalid` (400, partial-pair/non-native detail),
  `open-refused` (other 400, verbatim status+detail), `leaf-taken` (409, names the owning
  session), `launch-selection-conflict` (409, the LIVE row's retained pair vs attempted —
  provenance never rewritten), `outcome-unknown` (transport/5xx/unrecognized — design §7.1 F9).
- `classifyOpenResponse(httpStatus, body)` (L130-L178) — the pure classifier; `httpStatus: null`
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
| Selection reducers, wire-body rule, classifier, and the classifying open client. | L19-L222 | [launchFlow.ts](launchFlow.ts) |
| The capability wire types the reducers read (snapshot/model/effort rows). | — | [../types/harnessCapabilities.ts](../types/harnessCapabilities.ts) |
| The open-response wire shapes this classifies (200/400/409×2 bodies). | — | [../types/terminalOpen.ts](../types/terminalOpen.ts) |
| The server's synchronous-refusal boundary (split pair / non-native only). | L64-L87 | [harness_control_api.py](../../../mcp/src/agents_remember/serving/harness_control_api.py) |
| The dialog rendering these machines (options exclusively from the envelope). | — | [../panels/session-cockpit/LaunchFlow.tsx](../panels/session-cockpit/LaunchFlow.tsx) |
| Open-response fixtures the classifier is table-tested over. | — | [../test/fixtures/openResponses.ts](../test/fixtures/openResponses.ts) |
| The unit suite (reducer tables, classifier table, POST-body assertions). | — | [launchFlow.test.ts](launchFlow.test.ts) |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Update History

- 2026-07-18T15:22+02:00 — FEUI MX-FIX-2: removed the second browser POST and delegated hosted
  launch to the sole discriminated opener while preserving recognized refusal and unknown-outcome
  reconciliation semantics. Verification metadata remains pinned until closeout.

- 2026-07-18T07:22+02:00 — FEUI-L8 manual route refactor: retargeted this direct data file card
  from the packed dashboard/src parent to the new nearest data authority overview. Source behavior
  is unchanged by this memory-only governance move; verification hash/date remain pinned.

- 2026-07-17T06:10+02:00 — Created for 260715-FEUI-L3 R4/R5 (launch rules + open client): the
  pure selection machines (`launchableEfforts` filter-never-sorts, `chooseModel` re-gate to a
  launch-settable advertised default or explicit choice, `selectionComplete`,
  `launchSelectionBody` both-knobs-or-neither throwing on partials) and the classifying
  `openHostedSession` → `classifyOpenResponse` covering opened / launch-selection-invalid /
  open-refused / leaf-taken / launch-selection-conflict / outcome-unknown (F9, caller-minted id,
  no blind re-POST). Verification metadata pinned to the leaf base until closeout stamps the L3
  code commit.
