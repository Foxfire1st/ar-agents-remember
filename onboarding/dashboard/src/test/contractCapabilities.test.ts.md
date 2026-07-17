# dashboard/src/test/contractCapabilities.test.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/test/contractCapabilities.test.ts` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T06:10+02:00                           |
| lastVerifiedCommitHash | `96e1d6db63454438b57a7485382c27784a60776f`       |
| lastVerifiedCommitDate | 2026-07-17T06:28:52+02:00|
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

- **Capability envelopes** (L31-L118): the pack carries ALL THREE `cacheStatus` values under the
  v1 schema; Claude mirrors the recorded five row keys (`default`/`opus[1m]`/
  `claude-fable-5[1m]`/`sonnet`/`haiku`) with an effortless Haiku (`effortOptions: []`,
  `supportsEffort: false`) and the five-key effort menu on fable; Codex mirrors the recorded
  eight rows with per-row `defaultEffort` (sol=low) and exactly one hidden row
  (`codex-auto-review`); Pi keys keep the provider-qualified `provider/id` form verbatim; the
  fresh Claude exact-session snapshot has NULL `selectedEffort` and only the `model` config
  category; pre-session envelopes carry no selection; the 404/409/503 error fixtures wear the
  verbatim status words per HTTP code.
- **Vocabulary equality** (L120-L161): SetResult fixtures cover EXACTLY the five acceptances,
  receipts exactly five, reconciliations exactly four — asserted by sorted-key equality, so a
  dropped OR added value fails loudly; `queued`/`unknown` never carry an `effectiveValue`
  (the marker must not move early); every reconciliation reuses the ambiguous receipt's
  `requestId` (same id, no resend).
- **Open responses + failed rows** (L163-L200): the 200-starting body echoes the REQUESTED pair
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

| Finding | Citations | Source Path |
| --- | --- | --- |
| The three describe blocks (envelopes / vocabularies / open+failed). | L31-L200 | [contractCapabilities.test.ts](contractCapabilities.test.ts) |
| Envelope/model/SetResult/error fixtures under assertion. | L60-L273 | [fixtures/capabilityEnvelopes.ts](fixtures/capabilityEnvelopes.ts) |
| Receipt/reconciliation fixtures under assertion. | L14-L86 | [fixtures/controlMessages.ts](fixtures/controlMessages.ts) |
| Open-response + failed-row fixtures under assertion. | L17-L178 | [fixtures/openResponses.ts](fixtures/openResponses.ts) |
| The wire mirrors the assertions type against (`SetAcceptance`, schema). | L11-L117 | [../types/harnessCapabilities.ts](../types/harnessCapabilities.ts) |

## Update History

- 2026-07-17T06:10+02:00 — Created for 260715-FEUI-L3 R3 (contract conformance): recorded-L5 row
  keys (effortless Haiku, hidden codex-auto-review + per-row defaults, Pi provider-qualified),
  sorted-key vocabulary equality for SetResult/receipt/reconciliation (five/five/four), and the
  open-response/failed-row honesty facts (requested vs retained pair, alternatives-naming
  bridgeErrors, pending-interaction row). Verification metadata pinned to the leaf base until
  closeout stamps the L3 code commit.
