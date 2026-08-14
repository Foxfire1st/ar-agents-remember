# dashboard/src/panels/session-cockpit/LaunchFlow.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/session-cockpit/LaunchFlow.tsx` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-21T05:30+02:00                           |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`       |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `overview.md`                                   |

## Governing Overview

[panels/session-cockpit overview](overview.md)

## 260731-EFA-L8 Change

The launch-flow dialog parts moved to `launchFlowParts.tsx` and styles to
`launchFlowStyles.ts`; this file keeps the composition and state wiring. Behavior is
unchanged.

## Purpose

The **LaunchFlow dialog** (260715-FEUI-L3 S2/S3, design §7.1): harness → model → effort → open,
with every picker populated EXCLUSIVELY from the daemon — the harness list from
`GET /api/harnesses`, models/efforts from the live capability envelope. No hardcoded menu, no
client fallback, no invented default exists anywhere in this file. It is a fixed viewport overlay
with bounded height and internal scrolling, opened by the palette command `session.launch` registered in
SessionsView, or pre-filled by the failed-launch banner's 'Launch corrected…'. The pair rules
themselves are PURE and live in `data/launchFlow.ts`; this component renders them plus all four
open-response paths and the F9 transport-unknown reconciliation (the session id is CALLER-MINTED,
so "does the row exist" resolves an unanswered POST — never a blind re-POST with a fresh id).

## Code Commentary

### FEUI-L9R Reviewed Candidate Delta

The chooser now uses a fixed `100vw`/`100dvh` viewport overlay. `useHarnessCatalogRead` owns one
catalog request per open, a distinct timeout, abort on close/supersession, one replacement read for
a changed serving boot, and explicit operator Retry. Rendering distinguishes loading, ready, valid
empty, timeout, and network/HTTP/protocol failure. Submit requires a currently advertised detected
harness plus a complete selection; pre-session buttons no longer claim adapter process state.

### Logic

- **Reset + harness load on every open** (cit:(["launch-harness-loading"], dashboard/src/panels/session-cockpit/launchFlowParts.tsx:116-116)): form reset and catalog request ownership are
  separate. The hook performs one live read, revokes it on close or supersession, and exposes
  explicit loading/empty/timeout/error/retry states.
- **Harness buttons** (cit:(["— not installed", "disabled={!harness.detected}"], dashboard/src/panels/session-cockpit/launchFlowParts.tsx:135-135; dashboard/src/panels/session-cockpit/launchFlowParts.tsx:130-130)): detection gates each button (`disabled={!harness.detected}`,
  "— not installed"). The narrow pre-session contract intentionally has no adapter process word.
- **Envelope read** (L192-L195, L221-L224): selecting a harness calls
  `fetchHarnessCapabilities(harnessId)` (single-flighted; a daemon cache hit is cheap) and the
  component subscribes to that harness's `perHarness` entry only.
- **Model/effort pickers — dynamic only** (cit:([`capabilityLoadingCopy`], dashboard/src/data/capabilityCatalog.ts:75-79)): while `loading`/`refreshing`, the
  cost-named `capabilityLoadingCopy` renders and ZERO options exist (cit:(["data-testid=\"launch-cap-loading\"", "{capabilityLoadingCopy("], dashboard/src/panels/session-cockpit/launchFlowParts.tsx:313-314)); an `error` entry
  renders the VERBATIM `status: detail` with a retry button (cit:(["launch-cap-retry"], dashboard/src/panels/session-cockpit/LaunchFlow.test.tsx:211-211)); a loaded envelope renders
  `cacheStatusNote` + a refresh button whose `title` is `capabilityCostNote` (R2 — the same cost
  naming as the miss-loading state, cit:(["launch-cap-refresh"], dashboard/src/panels/session-cockpit/LaunchFlow.test.tsx:394-394)). Hidden rows are FILTERED OUT;
  non-selectable rows render disabled with the catalog's own fact ("— not selectable", cit:(["— not selectable", "— not selectable"], dashboard/src/panels/session-cockpit/launchFlowParts.tsx:190-190));
  keys render VERBATIM (Pi stays provider-qualified, cit:(["launch-model-list"], dashboard/e2e-production/cockpit.production.spec.ts:221-221)). The explicit vendor-defaults
  option (cit:(["launch-vendor-defaults"], dashboard/src/panels/session-cockpit/LaunchFlow.test.tsx:461-461)) selects `chooseVendorDefaults()` — NEITHER knob goes on the wire.
- **Effort rules**: a model with no launch-settable efforts gets the honest
  `launch-effort-none` note (Haiku can never form a pair — "launch with vendor defaults instead",
# dashboard/src/panels/session-cockpit/LaunchFlow.tsx
  and a null re-gated effort demands an explicit choice (`launch-effort-choose`, cit:(["launch-effort-choose"], dashboard/e2e-chats/support/drive.ts:35-35)).
  Model clicks run `chooseModel` (re-gates effort to THAT row's advertised launch default only),
  effort clicks `chooseEffort` — the reducers, not local logic.
- **Prefill** (cit:([`chooseModel`], dashboard/src/data/launchFlow.ts:47-59)): 'Launch corrected…' hands in the refused pair; it is applied
  ONLY where the live catalog still advertises it (`chooseModel` returns empty for an absent row)
  — the flow can never re-offer a key the catalog no longer advertises. Consumed once per open
  via `prefillPairRef`.
- **Launch** (cit:([`selectionComplete`], dashboard/src/data/launchFlow.ts:81-83)): `readyToLaunch` requires a currently advertised detected harness plus
  `selectionComplete`, not posting, and no pending unknown. `launch()` mints the id (`crypto.randomUUID`, cit:([`defaultMint`], dashboard/src/panels/session-cockpit/LaunchFlow.tsx:60-60);
  `mintSessionId` is the test seam) and calls `openHostedSession` (cit:([`openHostedSession`], dashboard/src/data/launchFlow.ts:232-250)). A 200 records the retained
  pair in `sessionCockpitStore.setLaunchEvidence` at the tier `launchTier` derives from the
  RESPONSE controlState ('starting' ⇒ pending — never promoted by the open response itself,
  cit:([`launchTier`], dashboard/src/data/launchEvidence.ts:29-41)), hydrates the catalog, focuses the new row, and closes.
- **Outcome rendering** cit:(["function LaunchOutcome({", "if (outcome.path === \"launch-selection-invalid\") {"], dashboard/src/panels/session-cockpit/launchFlowParts.tsx:499-499; dashboard/src/panels/session-cockpit/launchFlowParts.tsx:511-511): `launch-selection-invalid` and
  `open-refused` render the verbatim detail (cit:(["data-testid=\"launch-outcome-invalid\"", "if (outcome.path === \"open-refused\") {", "outcome: Extract<OpenOutcome, { path: \"seat-taken\" }>;"], dashboard/src/panels/session-cockpit/launchFlowParts.tsx:513-513; dashboard/src/panels/session-cockpit/launchFlowParts.tsx:518-518; dashboard/src/panels/session-cockpit/launchFlowParts.tsx:431-431)); `seat-taken` names the owning session
  with a focus-owner action (cit:(["data-testid=\"launch-focus-owner\"", "outcome: Extract<OpenOutcome, { path: \"launch-selection-conflict\" }>;"], dashboard/src/panels/session-cockpit/launchFlowParts.tsx:447-447; dashboard/src/panels/session-cockpit/launchFlowParts.tsx:467-467)); `launch-selection-conflict` shows the LIVE retained pair
  vs the attempted pair, states "the live process keeps its provenance; nothing was rewritten",
  and offers focus-existing (cit:(["launch-focus-existing"], dashboard/src/panels/session-cockpit/LaunchFlow.test.tsx:615-615)); `outcome-unknown` (F9) has NO retry button at all — it
  names the reconciliation mechanism ("the caller-minted id reconciles on the next poll. No
  re-POST is sent", cit:(["const unknown = await view.findByTestId(\"launch-outcome-unknown\")"], dashboard/src/panels/session-cockpit/LaunchFlow.test.tsx:631-632)).
- **F9 watcher**: the effect watches `sessions` for the minted id — but ONLY while
  `open` (review finding 1): an explicit dismiss ends the watch, so a row the daemon surfaces
  minutes later can never steal focus. `dismiss` (cit:(["data-testid=\"launch-cancel\"", "dismissal handling (Escape + stop-propagation) as ordinary DOM props."], dashboard/src/panels/session-cockpit/launchFlowParts.tsx:33-33; dashboard/src/panels/session-cockpit/launchFlowParts.tsx:417-417), wired to cancel button, overlay
  click, and Escape) ALSO clears `unknownId` immediately (the delta-verify residual: a stale id
  surviving dismissal would fire one late focus steal on the next open's first effect pass).
  While an unknown is pending, the cancel button reads "dismiss (resolves via the catalog)"
[panels/session-cockpit overview](overview.md)
- **Optional input** (cit:(["data-testid=\"launch-label\""], dashboard/src/panels/session-cockpit/launchFlowParts.tsx:365-370)): the launch form accepts an optional display label. Task ownership is supplied by structural context rather than a free-form leaf-key field.
  reads at any width.
- **Visual honesty pass (V7 + RV-3, 260718-CHATS-L5P)**: (a) the disabled `launchButton` primary is
  DEMOTED — `_disabled` drops the amber prominence to `opacity:0.4` + muted color + grid border, so the
  most emphatic control looks armed ONLY when the pair is complete and the harness detected (was styled
  amber-ready while disabled). (b) The launch summary (`noteLine`, `data-testid="launch-summary"`) always
  states WHY it is blocked via `launchBlockReason` (`pick a harness` → `pick a model and effort` → `<name>
  is not installed …`), never a bare `codex · — · —` em-dash chain; it shows `harness · model · effort`
  only when `readyToLaunch`. (c) `launchButton` + `quietButton` gain `flexShrink:0` + `whiteSpace:nowrap`
  so an action never wraps its own label (`launc/h`, `dismiss (resolves via the catal/og)`) — the summary
  span is the only segment that yields.

### Conventions

Co-located Panda `css()` with token names; option buttons carry `aria-pressed` (not radios —
worker flag 5, simpler keyboard story inside the dialog); `data-testid` on every assertable
element (`launch-*`); the dialog stops click propagation and handles its own Escape (cit:(["launch-flow-overlay"], dashboard/src/panels/session-cockpit/launchFlowParts.tsx:587-587)).

### Invariants And Boundaries

- DYNAMIC-ONLY: zero model/effort options may exist before the daemon answers; on a capability
  error the menu is an error surface with retry, NEVER a stale or invented list.
- A partial pair is unrepresentable end-to-end: the submit gate is `selectionComplete`, and
  `launchSelectionBody` (in `data/launchFlow.ts`) throws on any partial.
- The F9 path never re-POSTs (same id or fresh) and never rewrites provenance; reconciliation is
  catalog observation of the caller-minted id, gated on `open`.
- The 409-conflict path writes NO evidence for the live session.
- Advertised order is render order; nothing here sorts, ranks, or emphasizes an effort.

### Todos

No task-independent technical debt was identified during FEUI-L9R review.

## Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant domain documentation was found for this file. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The dialog: reset/load, pickers, pair gating, outcomes, F9 watcher + dismiss. | "launch-flow-overlay" | dashboard/src/panels/session-cockpit/launchFlowParts.tsx:587-587 |
| The pure pair reducers + open classifier this renders (`chooseModel`/`chooseEffort`/`selectionComplete`/`openHostedSession`). | `chooseModel`, `chooseEffort`, `selectionComplete`, `openHostedSession` | dashboard/src/data/launchFlow.ts:51-63; dashboard/src/data/launchFlow.ts:66-75; dashboard/src/data/launchFlow.ts:81-83; dashboard/src/data/launchFlow.ts:248-266 |
| The envelope store + R2 cost/cache copy (`fetchHarnessCapabilities`, `capabilityCostNote`, `capabilityLoadingCopy`, `cacheStatusNote`). | `CapabilityCatalogState` | dashboard/src/data/capabilityCatalog.ts:41-43 |
| The tier machine stamping the retained pair at 'pending' on a 200. | `launchTier` | dashboard/src/data/launchEvidence.ts:29-41 |
| The typed narrow harness catalog read and explicit result states. | `HarnessCatalogRead` | dashboard/src/data/harnessCatalog.ts:13-16 |
| The hook owning timeout, abort, Retry, and one replacement per serving boot. | `useHarnessCatalogRead` | dashboard/src/panels/session-cockpit/useHarnessCatalogRead.ts:22-84 |
| The owner registering `session.launch` and mounting the dialog after the palette. | "session.launch" | dashboard/src/panels/session-cockpit/sessions-view/shell.test.tsx:229-229 |
| The banner handing in the refused-pair prefill. | `FailedLaunchBanner` | dashboard/src/panels/session-cockpit/FailedLaunchBanner.tsx:69-143 |
| The jsdom matrix: dynamic-only, cost parity, pair rules, all response paths, F9 dismiss/reopen. | `renderFlow` | dashboard/src/panels/session-cockpit/LaunchFlow.test.tsx:88-102 |
| The open-response fixtures the classifier paths render. | `INVALID_PARTIAL_PAIR`, `FAILED_LAUNCH_ROWS` | dashboard/src/test/fixtures/openResponses.ts:46-49; dashboard/src/test/fixtures/openResponses.ts:140-144 |

## FEUI-L8 Reviewed Candidate Delta

New hosted chats inherit the selected lifecycle on the server and broadcast catalog creation. A captured catalog authority gates every post-await edge so a launch settling after scenario reset cannot adopt or mutate the successor fixture.

The reviewed candidate is still uncommitted. Existing verification hash/date remain pinned to the
leaf base; closeout owns commit stamping.

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-11T19:58+02:00 — Aligned the current dashboard card for `LaunchFlow.tsx` with its task-document, seat-state, and lifecycle interaction boundaries.
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: recorded the launchFlowParts/launchFlowStyles extraction. Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-03T02:35:50+02:00 — W3-B05 curator: anchored 10 Tier-2 table citations and 25 Tier-2 prose citations with exact source paths; fixer generated all ranges.

- 2026-07-31T19:30+02:00 — 260731-EFA-L2 curator: re-derived 1 stale self-citation. The
  `capabilityLoadingCopy` loading branch moved L359-L365 -> L448-L454 (L359-L365 is now the
  dialog's `role="dialog"`/Escape wiring); the range now covers the whole loading ternary arm that
  proves ZERO options exist while `loading`/`refreshing`. Claim re-verified and unchanged.

- 2026-07-21T05:30+02:00 — 260718-CHATS-L5P curator: recorded the V7 + RV-3 visual-honesty pass — the
  disabled primary is demoted to a muted/inert chip (no longer amber-ready), the summary always names the
  blocking next step (no `codex · — · —` chain), the leaf-key placeholder is shortened (`leaf key
  (optional)`) with the arbitration note moved to `title`, and `launchButton`/`quietButton` gained
  `flexShrink:0` + `nowrap` (no self-wrapping labels). Daemon-only pickers, pair gating, and outcome
  paths unchanged. Verification pinned to the leaf base (`352d5cd`) until closeout stamps the candidate
  commit.
- 2026-07-18T12:43+02:00 — FEUI-L9R: corrected overlay geometry and catalog authority: fixed
  bounded viewport, typed read states, abortable timeout/operator retry, one reread per serving
  boot, detected-row submit gate, and no pre-session adapter projection. Verification metadata
  remains pinned pending candidate closeout.

- 2026-07-18T07:22+02:00 — Curated the final same-reviewer-PASS FEUI-L8 behavior above using direct
  source/test/task evidence; no Domain Documentation source is configured.

- 2026-07-17T06:10+02:00 — Created for 260715-FEUI-L3 S2/S3 (R1/R2/R4/R5, incl. fix rounds 1-2):
  the palette-opened launch dialog with daemon-only pickers (detected-gated harnesses with the
  VISIBLE adapter word — review finding 6), verbatim capability errors + retry, R2 cost-named
  loading/refresh parity, complete-pair gating with advertised-order efforts and vendor-defaults/
  effortless honesty, all four open-response paths, and the F9 unknown-outcome watcher gated on
  `open` with dismiss clearing the watch state (review finding 1 + the delta-verify residual).
  Verification metadata pinned to the leaf base until closeout stamps the L3 code commit.
