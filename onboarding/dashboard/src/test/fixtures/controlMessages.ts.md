# dashboard/src/test/fixtures/controlMessages.ts

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

## Evidence

### Docs References

No Domain Documentation source is configured for this repository; repository code and tests are the authority.

No configured live domain-documentation source was available.

### Repo-Internal References

- The five receipts + four reconciliations. [1]
- The wire mirrors (`SubmissionReceiptWire`, `ReconciliationResultWire`). [2]
- The Python serializers mirrored (`public_receipt_json`/`public_reconciliation_json`). [3]
- The vocabulary-equality suite (five/four by sorted keys, shared requestId). [4]

### Cross-Repo References

No meaningful cross-repo references found.

This file implements a repository-local contract.

## 260715-FEUI-L5 Reliable Submit Delta

All five receipt fixtures now carry bridge epoch; reconciliation fixtures carry epoch plus the
normalized submission lifecycle state. This keeps frontend tests aligned to generation-bound public
responses and prevents fixtures from silently accepting pre-L5 unversioned shapes.
