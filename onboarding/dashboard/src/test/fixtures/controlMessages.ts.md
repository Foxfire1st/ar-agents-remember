# dashboard/src/test/fixtures/controlMessages.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/test/fixtures/controlMessages.ts` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T21:39+02:00 |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb`       |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
| governingOverview      | `../../overview.md`                              |

## Governing Overview

[dashboard/src overview](../../overview.md)

## Purpose

**Submission-receipt and reconciliation fixtures** (260715-FEUI-L3 R3) — the reliable-submit
halves of the contract pack, mirrored from `serving/harness_control_models.py`
`public_receipt_json` / `public_reconciliation_json`. L5 (composer/submit) consumes these;
founded here because L3 is the first API-consuming leaf.

## Code Commentary

### Logic

- cit:([`SUBMISSION_RECEIPTS`], dashboard/src/test/fixtures/controlMessages.ts:15-61): one receipt per acceptance state —
  `immediate` (accepted + vendor correlation id), `queued` ("an active turn is running; the
  prompt is retained"), `rejected`, `unknown` ("response lost — reconcile by requestId, never
  resend"), `unsupported` (no native protocol control endpoint). Only `immediate` carries
  `acceptedAt`/`vendorCorrelationId`.
- cit:([`RECONCILIATIONS`], dashboard/src/test/fixtures/controlMessages.ts:63-100): the four states — `accepted`/`rejected`/`unresolved` ("keep the
  draft, do not resend")/`unsupported` — EVERY one reusing the ambiguous receipt's
  `requestId` (`req-unknown-1`): reconciliation resolves BY ID, it is never a resend (pinned by
  the conformance suite).

### Invariants And Boundaries

- Detail strings are representative paraphrases of L5-observed behavior marked as fixtures
  (worker decision 11); the field names/shapes mirror the serializers exactly
  (reviewer-verified). Extend against recorded evidence only.
- The `requestId` reuse across all reconciliation fixtures is deliberate contract teaching — a
  new fixture with a fresh id would erode the no-resend lesson.

## Docs References

No Domain Documentation source is configured for this repository; repository code and tests are the authority.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live domain-documentation source was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The five receipts + four reconciliations. | `SUBMISSION_RECEIPTS`; `RECONCILIATIONS` | dashboard/src/test/fixtures/controlMessages.ts:15-61; dashboard/src/test/fixtures/controlMessages.ts:63-100 |
| The wire mirrors (`SubmissionReceiptWire`, `ReconciliationResultWire`). | `SubmissionReceiptWire`; `ReconciliationResultWire` | dashboard/src/types/harnessCapabilities.ts:99-107; dashboard/src/types/harnessCapabilities.ts:120-128 |
| The Python serializers mirrored (`public_receipt_json`/`public_reconciliation_json`). | `public_receipt_json`; `public_reconciliation_json` | mcp/src/agents_remember/serving/harness_control_models.py:217-228; mcp/src/agents_remember/serving/harness_control_models.py:231-242 |
| The vocabulary-equality suite (five/four by sorted keys, shared requestId). | "SetResult / receipt / reconciliation vocabularies" | dashboard/src/test/contractCapabilities.test.ts:120-161 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| This file implements a repository-local contract. | — | — |

## 260715-FEUI-L5 Reliable Submit Delta

All five receipt fixtures now carry bridge epoch; reconciliation fixtures carry epoch plus the
normalized submission lifecycle state. This keeps frontend tests aligned to generation-bound public
responses and prevents fixtures from silently accepting pre-L5 unversioned shapes.

## Update History

- 2026-08-03T02:40:51+02:00 — W3-B01 curator: curated 4 Repo-Internal table citations with exact fixture, wire-type, serializer, and vocabulary-suite anchors. Verification metadata remains unchanged for closeout.
- 2026-07-17T21:39+02:00 — FEUI-L5: added epoch and lifecycle-state coverage to normalized control
  message fixtures.

- 2026-07-17T06:10+02:00 — Created for 260715-FEUI-L3 R3 (reliable-submit fixtures):
  SUBMISSION_RECEIPTS across the five acceptance states and RECONCILIATIONS across the four
  states, all reconciliations keyed to the ambiguous receipt's requestId (resolve-by-id, never
  resend) — the pack L5's composer/submit work consumes. Verification metadata pinned to the
  leaf base until closeout stamps the L3 code commit.
