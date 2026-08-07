# dashboard/src/data/launchFlow.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/launchFlow.ts`               |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-07-18T15:22+02:00 |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f`       |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
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

- `LaunchSelectionState` / cit:([`EMPTY_SELECTION`], dashboard/src/data/launchFlow.ts:27-31) — `{modelKey, effort, vendorDefaults}`;
  `vendorDefaults: true` is the EXPLICIT selectionless choice (send NEITHER knob).
- cit:([`launchableEfforts`], dashboard/src/data/launchFlow.ts:34-36) — `effortOptions.filter(launchSettable)`; a `filter` only,
  no `.sort()` anywhere (advertised order preserved — reviewer-grepped).
- cit:([`chooseModel`], dashboard/src/data/launchFlow.ts:47-59) — picking a model RE-GATES effort: that row's
  advertised `defaultEffort` only when it is itself in the launch-settable menu, otherwise `null`
  (the flow demands an explicit choice — a non-launch-settable default is never silently
  selected). An unadvertised key returns `EMPTY_SELECTION` (dynamic-only ⇒ not selectable; this
  is also why a corrected-launch prefill can never re-offer a key the live catalog dropped).
- cit:([`chooseEffort`], dashboard/src/data/launchFlow.ts:62-71) — accepts only the CURRENT model's
  advertised launchable menu; anything else leaves the selection unchanged.
- cit:([`selectionComplete`], dashboard/src/data/launchFlow.ts:77-79) / cit:([`launchSelectionBody`], dashboard/src/data/launchFlow.ts:82-90) — complete = vendor defaults OR
  both knobs; the body emits `{model, effort}` or `{}` and THROWS on any partial pair
  ("complete the pair or choose vendor defaults") — partiality is unrepresentable.
- cit:([`OpenOutcome`], dashboard/src/data/launchFlow.ts:95-126) — one normalized outcome per server path, each rendered verbatim by
  the flow: `opened` (200 + session, carrying the REQUESTED pair verbatim — tier 'pending', never
  proof), `launch-selection-invalid` (400, partial-pair/non-native detail),
  `open-refused` (other 400, verbatim status+detail), `leaf-taken` (409, names the owning
  session), `launch-selection-conflict` (409, the LIVE row's retained pair vs attempted —
  provenance never rewritten), `outcome-unknown` (transport/5xx/unrecognized — design §7.1 F9).
- cit:([`classifyOpenResponse`], dashboard/src/data/launchFlow.ts:182-195) — the pure classifier; `httpStatus: null`
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

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Selection reducers, wire-body rule, classifier, and the classifying open client. | `LaunchSelectionState`, `selectionComplete`, `launchSelectionBody`, `classifyOpenResponse`, `openHostedSession` | dashboard/src/data/launchFlow.ts:20-25; dashboard/src/data/launchFlow.ts:77-79; dashboard/src/data/launchFlow.ts:82-90; dashboard/src/data/launchFlow.ts:182-195; dashboard/src/data/launchFlow.ts:232-250 |
| The capability wire types the reducers read (snapshot/model/effort rows). | `CapabilitySnapshotWire`, `ModelCapabilityWire`, `EffortOptionWire` | dashboard/src/types/harnessCapabilities.ts:16-22; dashboard/src/types/harnessCapabilities.ts:25-39; dashboard/src/types/harnessCapabilities.ts:59-65 |
| The open-response wire shapes this classifies (200/400/409×2 bodies). | `TerminalOpenSuccessBody`, `TerminalOpenSelectionInvalidBody`, `TerminalOpenBadKindBody`, `TerminalOpenLeafTakenBody`, `TerminalOpenConflictBody` | dashboard/src/types/terminalOpen.ts:10-26; dashboard/src/types/terminalOpen.ts:31-34; dashboard/src/types/terminalOpen.ts:37-40; dashboard/src/types/terminalOpen.ts:43-47; dashboard/src/types/terminalOpen.ts:51-63 |
| The server's synchronous-refusal boundary (split pair / non-native only). | `resolve_terminal_open_selection` | mcp/src/agents_remember/serving/harness_control_api.py:156-179 |
| The dialog rendering these machines (options exclusively from the envelope). | `LaunchFlow` | dashboard/src/panels/session-cockpit/LaunchFlow.tsx:362-423 |
| Open-response fixtures the classifier is table-tested over. | `OPENED_STARTING`, `INVALID_PARTIAL_PAIR`, `LAUNCH_CONFLICT` | dashboard/src/test/fixtures/openResponses.ts:17-33; dashboard/src/test/fixtures/openResponses.ts:46-49; dashboard/src/test/fixtures/openResponses.ts:72-86 |
| The unit suite (reducer tables, classifier table, POST-body assertions). | "selection reducers — complete pair or vendor defaults, never partial", "200 + session → opened, carrying the REQUESTED pair (starting) verbatim", "POSTs the complete pair and classifies the answer" | dashboard/src/data/launchFlow.test.ts:35-128; dashboard/src/data/launchFlow.test.ts:133-142; dashboard/src/data/launchFlow.test.ts:200-220 |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: reviewed this sidecar against the frontend-rail change set (strict-target lint remediation: complexity, max-lines-per-function, react-hooks, jsx-a11y, and import-cycle fixes). No content impact: behavior-preserving refactor; the file's responsibilities and the claims in this card remain current. Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-04T00:22:04+02:00 — 260731-EFA-L6 S18-B05 curator: repaired and normalised mechanical citation findings with current source anchors and fixer-generated ranges; no semantic claim changes. Verification metadata pinned until closeout stamps the L6 code commit.
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
