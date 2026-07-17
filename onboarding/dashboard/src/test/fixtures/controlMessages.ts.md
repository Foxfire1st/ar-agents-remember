# dashboard/src/test/fixtures/controlMessages.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/test/fixtures/controlMessages.ts` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T21:39+02:00 |
| lastVerifiedCommitHash | `f8196d98982f834d68152d307ff8025ea69440d5`       |
| lastVerifiedCommitDate | 2026-07-17T22:08:10+02:00|
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

- `SUBMISSION_RECEIPTS` (L14-L55): one receipt per acceptance state —
  `immediate` (accepted + vendor correlation id), `queued` ("an active turn is running; the
  prompt is retained"), `rejected`, `unknown` ("response lost — reconcile by requestId, never
  resend"), `unsupported` (no native protocol control endpoint). Only `immediate` carries
  `acceptedAt`/`vendorCorrelationId`.
- `RECONCILIATIONS` (L57-L86): the four states — `accepted`/`rejected`/`unresolved` ("keep the
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

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured live domain-documentation source was available. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The five receipts + four reconciliations. | L14-L86 | [controlMessages.ts](controlMessages.ts) |
| The wire mirrors (`SubmissionReceiptWire`, `ReconciliationResultWire`). | L99-L117 | [../../types/harnessCapabilities.ts](../../types/harnessCapabilities.ts) |
| The Python serializers mirrored (`public_receipt_json`/`public_reconciliation_json`). | L274-L296 | [harness_control_models.py](../../../../mcp/src/agents_remember/serving/harness_control_models.py) |
| The vocabulary-equality suite (five/four by sorted keys, shared requestId). | L141-L160 | [../contractCapabilities.test.ts](../contractCapabilities.test.ts) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| This file implements a repository-local contract. | — | — |

## 260715-FEUI-L5 Reliable Submit Delta

All five receipt fixtures now carry bridge epoch; reconciliation fixtures carry epoch plus the
normalized submission lifecycle state. This keeps frontend tests aligned to generation-bound public
responses and prevents fixtures from silently accepting pre-L5 unversioned shapes.

## Update History

- 2026-07-17T21:39+02:00 — FEUI-L5: added epoch and lifecycle-state coverage to normalized control
  message fixtures.

- 2026-07-17T06:10+02:00 — Created for 260715-FEUI-L3 R3 (reliable-submit fixtures):
  SUBMISSION_RECEIPTS across the five acceptance states and RECONCILIATIONS across the four
  states, all reconciliations keyed to the ambiguous receipt's requestId (resolve-by-id, never
  resend) — the pack L5's composer/submit work consumes. Verification metadata pinned to the
  leaf base until closeout stamps the L3 code commit.
