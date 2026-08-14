# dashboard/src/test/contractCapabilities.test.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/test/contractCapabilities.test.ts` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T06:10+02:00                           |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`       |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

The **R3 conformance suite** (260715-FEUI-L3): asserts the contract fixture pack against the
RECORDED L5 live-conformance samples (`260716-ACPUI-L5-{claude,codex}-live-conformance.md`,
`-pi-live-and-resource-proof.md`) so the fixtures later leaves consume (L4 setters, L5
submit/reconcile, L6 interactions) stay pinned to observed harness truth. The values it asserts
are test evidence ONLY — the dynamic-only invariant forbids them from production code.

## Code Commentary

### Logic

- **Capability envelopes** (cit:(["capability envelopes"], dashboard/src/test/contractCapabilities.test.ts:31-118)): the pack carries ALL THREE `cacheStatus` values under the
  v1 schema; Claude mirrors the recorded five row keys (`default`/`opus[1m]`/
  `claude-fable-5[1m]`/`sonnet`/`haiku`) with an effortless Haiku (`effortOptions: []`,
  `supportsEffort: false`) and the five-key effort menu on fable; Codex mirrors the recorded
  eight rows with per-row `defaultEffort` (sol=low) and exactly one hidden row
  (`codex-auto-review`); Pi keys keep the provider-qualified `provider/id` form verbatim; the
  fresh Claude exact-session snapshot has NULL `selectedEffort` and only the `model` config
  category; pre-session envelopes carry no selection; the 404/409/503 error fixtures wear the
  verbatim status words per HTTP code.
- **Vocabulary equality** (cit:(["SetResult / receipt / reconciliation vocabularies"], dashboard/src/test/contractCapabilities.test.ts:120-161)): SetResult fixtures cover EXACTLY the five acceptances,
  receipts exactly five, reconciliations exactly four — asserted by sorted-key equality, so a
  dropped OR added value fails loudly; `queued`/`unknown` never carry an `effectiveValue`
  (the marker must not move early); every reconciliation reuses the ambiguous receipt's
  `requestId` (same id, no resend).
- **Open responses + failed rows** (cit:(["open responses + failed rows"], dashboard/src/test/contractCapabilities.test.ts:163-200)): the 200-starting body echoes the REQUESTED pair
  verbatim and the vendor-defaults body carries null/null; the conflict body carries the LIVE
  row's retained pair; leaf-taken names the owning session; failed rows exist for ALL THREE
  harnesses, retain the refused pair, and their `bridgeError` names the advertised alternatives;
  the pack carries a `controlPendingInteraction` row for the interaction leaves.

### Invariants And Boundaries

- This suite is the contract net between the fixture pack and the recorded L5 evidence: fixture
  drift (renamed key, changed menu, lost vocabulary value) fails HERE even if every consumer
  test still passes.
- Placed at `src/test/` (beside `setup.ts`), not with the unit suites — it tests the pack, not a
  module.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The three describe blocks (envelopes / vocabularies / open+failed). | "capability envelopes"; "SetResult / receipt / reconciliation vocabularies"; "open responses + failed rows" | dashboard/src/test/contractCapabilities.test.ts:31-118; dashboard/src/test/contractCapabilities.test.ts:120-161; dashboard/src/test/contractCapabilities.test.ts:163-200 |
| Envelope/model/SetResult/error fixtures under assertion. | `ENVELOPES_BY_CACHE_STATUS`; `SET_RESULTS`; `CAPABILITY_ERROR_BODIES` | dashboard/src/test/fixtures/capabilityEnvelopes.ts:175-179; dashboard/src/test/fixtures/capabilityEnvelopes.ts:211-247; dashboard/src/test/fixtures/capabilityEnvelopes.ts:336-358 |
| Receipt/reconciliation fixtures under assertion. | `SUBMISSION_RECEIPTS`; `RECONCILIATIONS` | dashboard/src/test/fixtures/controlMessages.ts:15-61; dashboard/src/test/fixtures/controlMessages.ts:63-100 |
| Open-response + failed-row fixtures under assertion. | `OPENED_STARTING`; `OPENED_VENDOR_DEFAULTS`; `SEAT_TAKEN`; `LAUNCH_CONFLICT`; `FAILED_LAUNCH_ROWS`; `PENDING_INTERACTION_ROW` | dashboard/src/test/fixtures/openResponses.ts:17-33; dashboard/src/test/fixtures/openResponses.ts:36-43; dashboard/src/test/fixtures/openResponses.ts:64-71; dashboard/src/test/fixtures/openResponses.ts:72-86; dashboard/src/test/fixtures/openResponses.ts:140-144; dashboard/src/test/fixtures/openResponses.ts:164-178 |
| The wire mirrors the assertions type against (`SetAcceptance`, schema). | `SetAcceptance` | dashboard/src/types/harnessCapabilities.ts:86-86 |

## Update History

- 2026-08-11T19:58+02:00 — Aligned the current dashboard card for `contractCapabilities.test.ts` with its task-document, seat-state, and lifecycle interaction boundaries.
- 2026-08-02T16:56+02:00 — 260731-EFA-L6 curator W1-B06: anchored 7 citation claims
  (3 Logic citations and 4 Repo-Internal reference rows); scoped result 0 findings.

- 2026-07-17T06:10+02:00 — Created for 260715-FEUI-L3 R3 (contract conformance): recorded-L5 row
  keys (effortless Haiku, hidden codex-auto-review + per-row defaults, Pi provider-qualified),
  sorted-key vocabulary equality for SetResult/receipt/reconciliation (five/five/four), and the
  open-response/failed-row honesty facts (requested vs retained pair, alternatives-naming
  bridgeErrors, pending-interaction row). Verification metadata pinned to the leaf base until
  closeout stamps the L3 code commit.
