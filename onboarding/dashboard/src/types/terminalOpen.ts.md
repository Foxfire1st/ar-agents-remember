# dashboard/src/types/terminalOpen.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/types/terminalOpen.ts`            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T06:10+02:00                           |
| lastVerifiedCommitHash | `b252c42cca200933d5c9c36e26de47a526a569ce`       |
| lastVerifiedCommitDate | 2026-08-07T23:58:52+02:00|
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

- cit:([`TerminalOpenSuccessBody`], dashboard/src/types/terminalOpen.ts:10-26) — 200, opened or idempotently reused: `status: "running"`,
  `controlState` starts at `'starting'` for a native harness; `resolvedModel`/`resolvedEffort`
  are the REQUESTED pair persisted verbatim BEFORE any validation (`terminal_opener.py`
  `_resolved_pair`) — provenance, never proof (the R7 tier machine renders it 'pending').
- cit:([`TerminalOpenSelectionInvalidBody`], dashboard/src/types/terminalOpen.ts:31-34) — 400 `launch-selection-invalid`, the ONLY
  synchronous launch-selection refusal: a partial pair or a non-native harness
  (`harness_control_api.py` `resolve_terminal_open_selection`). Catalog validity is NOT checked
  at open time — an invalid pair opens 200/'starting' and fails asynchronously on every harness
  (the R6 uniform fail-loud premise).
- cit:([`TerminalOpenBadKindBody`], dashboard/src/types/terminalOpen.ts:37-40) — 400 `bad-kind`: unknown kind / unknown or undetected
  harness.
- cit:([`TerminalOpenLeafTakenBody`], dashboard/src/types/terminalOpen.ts:43-47) — 409: the (leaf, role) pair already has a live owner;
  the server NAMES the owning `session`.
- cit:([`TerminalOpenConflictBody`], dashboard/src/types/terminalOpen.ts:51-63) — 409 `launch-selection-conflict`: the session id is live
  with a DIFFERENT launch identity; the body carries the LIVE row's retained pair (process truth)
  — reopening never rewrites provenance.

### Invariants And Boundaries

- Every body is rendered VERBATIM by the flow's classifier (`data/launchFlow.ts`
  `classifyOpenResponse`) cit:([`classifyOpenResponse`], dashboard/src/data/launchFlow.ts:182-195) — no field here may be reworded or synthesized client-side.
- The two `resolvedModel`/`resolvedEffort` carriers mean different things: success = the
  REQUESTED pair, conflict = the LIVE row's retained pair. Confusing them is a provenance
  honesty violation.
- Reuses `HarnessControlState`/`TerminalOpenKind` from `terminalCatalog.ts` cit:([`TerminalOpenKind`], dashboard/src/types/terminalCatalog.ts:7-7) rather than re-declaring the vocabularies.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| All five response-body interfaces. | `TerminalOpenSuccessBody` | dashboard/src/types/terminalOpen.ts:10-26 |
| The route these mirror (`api_terminal_open`, 200/400/409 bodies). | `api_terminal_open` | mcp/src/agents_remember/serving/_app_terminal_routes.py:649-664 |
| The synchronous selection gate (partial pair / non-native only). | `resolve_terminal_open_selection` | mcp/src/agents_remember/serving/harness_control_api.py:156-179 |
| The vocabularies imported instead of re-declared. | `TerminalOpenKind` | dashboard/src/types/terminalCatalog.ts:7-7 |
| The classifier consuming every body verbatim (`classifyOpenResponse`). | `classifyOpenResponse` | dashboard/src/data/launchFlow.ts:182-195 |
| The request-side knobs (`OpenTerminalOptions.model/effort`). | `OpenTerminalOptions` | dashboard/src/data/terminal.ts:382-382 |
| The fixture instances of every body (+ failed rows). | `OPENED_STARTING` | dashboard/src/test/fixtures/openResponses.ts:17-33 |

## Update History
- 2026-08-02T21:18:27+02:00 — 260731-EFA-L6 curator W2-B06: repaired 7 citation claims; scoped result 0 findings.

- 2026-07-17T06:10+02:00 — Created for 260715-FEUI-L3 R5 (open-route wire mirror): the 200
  success body (requested pair as provenance), 400 `launch-selection-invalid` (partial
  pair/non-native — the only synchronous refusal) and `bad-kind`, 409 `leaf-taken` (names the
  owner) and `launch-selection-conflict` (live retained pair, provenance never rewritten) —
  field-for-field against `app.py` per the L3 review. Verification metadata pinned to the leaf
  base until closeout stamps the L3 code commit.
