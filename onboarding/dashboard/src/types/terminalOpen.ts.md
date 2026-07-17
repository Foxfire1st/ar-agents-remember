# dashboard/src/types/terminalOpen.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/types/terminalOpen.ts`            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T06:10+02:00                           |
| lastVerifiedCommitHash | `96e1d6db63454438b57a7485382c27784a60776f`       |
| lastVerifiedCommitDate | 2026-07-17T06:28:52+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

The TypeScript mirror of the **`POST /api/terminal/{session}` response bodies** (260715-FEUI-L3
R5): every outcome of `serving/app.py` `api_terminal_open` — 200 opened, both 400 refusals, both
409 refusals — so the launch flow can render each path verbatim. The Python route is the source of
truth, kept in lockstep by hand; the L3 reviewer verified the bodies field-for-field against
`app.py`. The REQUEST side (the `model`/`effort` knobs on the POST body) lives on
`data/terminal.ts` `OpenTerminalOptions`; `types/terminalCatalog.ts` was untouched — L3 wire
shapes went to new files.

## Code Commentary

### Logic

- `TerminalOpenSuccessBody` (L10-L26) — 200, opened or idempotently reused: `status: "running"`,
  `controlState` starts at `'starting'` for a native harness; `resolvedModel`/`resolvedEffort`
  are the REQUESTED pair persisted verbatim BEFORE any validation (`terminal_opener.py`
  `_resolved_pair`) — provenance, never proof (the R7 tier machine renders it 'pending').
- `TerminalOpenSelectionInvalidBody` (L31-L34) — 400 `launch-selection-invalid`, the ONLY
  synchronous launch-selection refusal: a partial pair or a non-native harness
  (`harness_control_api.py` `resolve_terminal_open_selection`). Catalog validity is NOT checked
  at open time — an invalid pair opens 200/'starting' and fails asynchronously on every harness
  (the R6 uniform fail-loud premise).
- `TerminalOpenBadKindBody` (L37-L40) — 400 `bad-kind`: unknown kind / unknown or undetected
  harness.
- `TerminalOpenLeafTakenBody` (L43-L47) — 409: the (leaf, role) pair already has a live owner;
  the server NAMES the owning `session`.
- `TerminalOpenConflictBody` (L51-L63) — 409 `launch-selection-conflict`: the session id is live
  with a DIFFERENT launch identity; the body carries the LIVE row's retained pair (process truth)
  — reopening never rewrites provenance.

### Invariants And Boundaries

- Every body is rendered VERBATIM by the flow's classifier (`data/launchFlow.ts`
  `classifyOpenResponse`) — no field here may be reworded or synthesized client-side.
- The two `resolvedModel`/`resolvedEffort` carriers mean different things: success = the
  REQUESTED pair, conflict = the LIVE row's retained pair. Confusing them is a provenance
  honesty violation.
- Reuses `HarnessControlState`/`TerminalOpenKind` from `terminalCatalog.ts` (L5) rather than
  re-declaring the vocabularies.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| All five response-body interfaces. | L10-L63 | [terminalOpen.ts](terminalOpen.ts) |
| The route these mirror (`api_terminal_open`, 200/400/409 bodies). | L956-L1046 | [app.py](../../../mcp/src/agents_remember/serving/app.py) |
| The synchronous selection gate (partial pair / non-native only). | L64-L87 | [harness_control_api.py](../../../mcp/src/agents_remember/serving/harness_control_api.py) |
| The vocabularies imported instead of re-declared. | L7-L15 | [terminalCatalog.ts](terminalCatalog.ts) |
| The classifier consuming every body verbatim (`classifyOpenResponse`). | — | [../data/launchFlow.ts](../data/launchFlow.ts) |
| The request-side knobs (`OpenTerminalOptions.model/effort`). | — | [../data/terminal.ts](../data/terminal.ts) |
| The fixture instances of every body (+ failed rows). | — | [../test/fixtures/openResponses.ts](../test/fixtures/openResponses.ts) |

## Update History

- 2026-07-17T06:10+02:00 — Created for 260715-FEUI-L3 R5 (open-route wire mirror): the 200
  success body (requested pair as provenance), 400 `launch-selection-invalid` (partial
  pair/non-native — the only synchronous refusal) and `bad-kind`, 409 `leaf-taken` (names the
  owner) and `launch-selection-conflict` (live retained pair, provenance never rewritten) —
  field-for-field against `app.py` per the L3 review. Verification metadata pinned to the leaf
  base until closeout stamps the L3 code commit.
