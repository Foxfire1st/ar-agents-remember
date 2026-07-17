# dashboard/src/panels/session-cockpit/LaunchFlow.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/session-cockpit/LaunchFlow.tsx` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T06:10+02:00                           |
| lastVerifiedCommitHash | `96e1d6db63454438b57a7485382c27784a60776f`       |
| lastVerifiedCommitDate | 2026-07-17T06:28:52+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

The **LaunchFlow dialog** (260715-FEUI-L3 S2/S3, design §7.1): harness → model → effort → open,
with every picker populated EXCLUSIVELY from the daemon — the harness list from
`GET /api/harnesses`, models/efforts from the live capability envelope. No hardcoded menu, no
client fallback, no invented default exists anywhere in this file. It is a dedicated overlay
dialog (non-portal, absolutely positioned inside the `[data-view="sessions"]` scope root — the
same posture as the palette) opened by the palette command `session.launch` registered in
SessionsView, or pre-filled by the failed-launch banner's 'Launch corrected…'. The pair rules
themselves are PURE and live in `data/launchFlow.ts`; this component renders them plus all four
open-response paths and the F9 transport-unknown reconciliation (the session id is CALLER-MINTED,
so "does the row exist" resolves an unanswered POST — never a blind re-POST with a fresh id).

## Code Commentary

### Logic

- **Reset + harness load on every open** (L198-L218): each open clears all selection/outcome
  state and re-fetches `/api/harnesses` via `fetchHarnessesOrNull` — live data, never a kept
  snapshot; a `null` result renders as the harness-list error line (L326-L329), not an empty menu.
- **Harness buttons** (L331-L354): detection GATES the button (`disabled={!harness.detected}`,
  "— not installed"); the server's adapter `control` word renders VISIBLY inside the button
  (`adapter <word>`, L348-L350 + the `adapterWord` css L96-L98) — review finding 6 replaced the
  hover-only `title` (invisible to keyboard/touch); the word is the server's own, verbatim.
- **Envelope read** (L192-L195, L221-L224): selecting a harness calls
  `fetchHarnessCapabilities(harnessId)` (single-flighted; a daemon cache hit is cheap) and the
  component subscribes to that harness's `perHarness` entry only.
- **Model/effort pickers — dynamic only** (L356-L473): while `loading`/`refreshing`, the
  cost-named `capabilityLoadingCopy` renders and ZERO options exist (L359-L365); an `error` entry
  renders the VERBATIM `status: detail` with a retry button (L366-L381); a loaded envelope renders
  `cacheStatusNote` + a refresh button whose `title` is `capabilityCostNote` (R2 — the same cost
  naming as the miss-loading state, L384-L396). Hidden rows are FILTERED OUT (L398-L399);
  non-selectable rows render disabled with the catalog's own fact ("— not selectable", L406/L417);
  keys render VERBATIM (Pi stays provider-qualified, L415-L416). The explicit vendor-defaults
  option (L420-L432) selects `chooseVendorDefaults()` — NEITHER knob goes on the wire.
- **Effort rules** (L433-L469): a model with no launch-settable efforts gets the honest
  `launch-effort-none` note (Haiku can never form a pair — "launch with vendor defaults instead",
  L434-L438); otherwise efforts render in ADVERTISED native order with zero emphasis (L441-L460),
  and a null re-gated effort demands an explicit choice (`launch-effort-choose`, L461-L466).
  Model clicks run `chooseModel` (re-gates effort to THAT row's advertised launch default only),
  effort clicks `chooseEffort` — the reducers, not local logic.
- **Prefill** (L36-L42, L227-L236): 'Launch corrected…' hands in the refused pair; it is applied
  ONLY where the live catalog still advertises it (`chooseModel` returns empty for an absent row)
  — the flow can never re-offer a key the catalog no longer advertises. Consumed once per open
  via `prefillPairRef`.
- **Launch** (L252-L299): `readyToLaunch` = harness + `selectionComplete` + not posting + no
  pending unknown (L254-L255). `launch()` mints the id (`crypto.randomUUID`, L163;
  `mintSessionId` is the test seam) and calls `openHostedSession`. A 200 records the retained
  pair in `sessionCockpitStore.setLaunchEvidence` at the tier `launchTier` derives from the
  RESPONSE controlState ('starting' ⇒ pending — never promoted by the open response itself,
  L277-L289), hydrates the catalog, focuses the new row, and closes.
- **Outcome rendering** (`LaunchOutcome`, L525-L613): `launch-selection-invalid` and
  `open-refused` render the verbatim detail (L539-L552); `leaf-taken` names the owning session
  with a focus-owner action (L553-L578); `launch-selection-conflict` shows the LIVE retained pair
  vs the attempted pair, states "the live process keeps its provenance; nothing was rewritten",
  and offers focus-existing (L579-L602); `outcome-unknown` (F9) has NO retry button at all — it
  names the reconciliation mechanism ("the caller-minted id reconciles on the next poll. No
  re-POST is sent", L603-L611).
- **F9 watcher** (L242-L248): the effect watches `sessions` for the minted id — but ONLY while
  `open` (review finding 1): an explicit dismiss ends the watch, so a row the daemon surfaces
  minutes later can never steal focus. `dismiss` (L257-L263, wired to cancel button, overlay
  click, and Escape) ALSO clears `unknownId` immediately (the delta-verify residual: a stale id
  surviving dismissal would fire one late focus steal on the next open's first effect pass).
  While an unknown is pending, the cancel button reads "dismiss (resolves via the catalog)"
  (L517).
- **Optional inputs** (L475-L493): label + leaf key — the leaf-key input makes the 409 leaf-taken
  path genuinely reachable from this surface; the placeholder says the server arbitrates
  ownership.

### Conventions

Co-located Panda `css()` with token names; option buttons carry `aria-pressed` (not radios —
worker flag 5, simpler keyboard story inside the dialog); `data-testid` on every assertable
element (`launch-*`); the dialog stops click propagation and handles its own Escape (L306-L319).

### Invariants And Boundaries

- DYNAMIC-ONLY: zero model/effort options may exist before the daemon answers; on a capability
  error the menu is an error surface with retry, NEVER a stale or invented list.
- A partial pair is unrepresentable end-to-end: the submit gate is `selectionComplete`, and
  `launchSelectionBody` (in `data/launchFlow.ts`) throws on any partial.
- The F9 path never re-POSTs (same id or fresh) and never rewrites provenance; reconciliation is
  catalog observation of the caller-minted id, gated on `open`.
- The 409-conflict path writes NO evidence for the live session.
- Advertised order is render order; nothing here sorts, ranks, or emphasizes an effort.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The dialog: reset/load, pickers, pair gating, outcomes, F9 watcher + dismiss. | L165-L613 | [LaunchFlow.tsx](LaunchFlow.tsx) |
| The pure pair reducers + open classifier this renders (`chooseModel`/`chooseEffort`/`selectionComplete`/`openHostedSession`). | L33-L222 | [../../data/launchFlow.ts](../../data/launchFlow.ts) |
| The envelope store + R2 cost/cache copy (`fetchHarnessCapabilities`, `capabilityCostNote`, `capabilityLoadingCopy`, `cacheStatusNote`). | L69-L243 | [../../data/capabilityCatalog.ts](../../data/capabilityCatalog.ts) |
| The tier machine stamping the retained pair at 'pending' on a 200. | L29-L41 | [../../data/launchEvidence.ts](../../data/launchEvidence.ts) |
| The harness list fetch (`fetchHarnessesOrNull`, `HarnessInfo.control`). | — | [../../data/terminal.ts](../../data/terminal.ts) |
| The owner registering `session.launch` and mounting the dialog after the palette. | L287-L296, L687-L693 | [SessionsView.tsx](SessionsView.tsx) |
| The banner handing in the refused-pair prefill. | L127-L143 | [FailedLaunchBanner.tsx](FailedLaunchBanner.tsx) |
| The jsdom matrix: dynamic-only, cost parity, pair rules, all response paths, F9 dismiss/reopen. | L85-L425 | [LaunchFlow.test.tsx](LaunchFlow.test.tsx) |
| The open-response fixtures the classifier paths render. | L1-L178 | [../../test/fixtures/openResponses.ts](../../test/fixtures/openResponses.ts) |

## Update History

- 2026-07-17T06:10+02:00 — Created for 260715-FEUI-L3 S2/S3 (R1/R2/R4/R5, incl. fix rounds 1-2):
  the palette-opened launch dialog with daemon-only pickers (detected-gated harnesses with the
  VISIBLE adapter word — review finding 6), verbatim capability errors + retry, R2 cost-named
  loading/refresh parity, complete-pair gating with advertised-order efforts and vendor-defaults/
  effortless honesty, all four open-response paths, and the F9 unknown-outcome watcher gated on
  `open` with dismiss clearing the watch state (review finding 1 + the delta-verify residual).
  Verification metadata pinned to the leaf base until closeout stamps the L3 code commit.
