# dashboard/src/types/harnessCapabilities.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/types/harnessCapabilities.ts`     |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T21:39+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`       |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

This file declares the TypeScript wire shapes for the pre-session capability envelope, dynamic
catalog, route errors, and the setter/submit/reconcile evidence payloads. The runtime envelope and
snapshot serializers live in the MCP serving package, while this module preserves their camelCase
wire names and keeps catalog values dynamic rather than embedding an install's data.

## Code Commentary

### Logic

- `CAPABILITY_SCHEMA = "ar-harness-capabilities/v1"` and `CapabilityCacheStatus`
  `hit|miss|refreshed` — hit is served from cache; miss and refreshed both ran
  the same short-lived native discovery.
- cit:([`EffortOptionWire`], dashboard/src/types/harnessCapabilities.ts:16-22): one vendor token accepted by one specific model
  (`effort_option_json`) — `launchSettable`/`sessionSettable` booleans gate the launch flow's
  effort menu (R4).
- cit:([`ModelCapabilityWire`], dashboard/src/types/harnessCapabilities.ts:25-39): one dynamically advertised model with its model-gated effort
  menu (`model_capability_json`) — `effortOptions` is the advertised NATIVE order, never reordered
  client-side; `hidden`/`selectable`/`isDefault`/`defaultEffort` are catalog data; provider rows
  keep their provider-qualified key verbatim with `provider` alongside.
- cit:([`SessionConfigOptionWire`], dashboard/src/types/harnessCapabilities.ts:48-56): the ACP Sense 1 select-config SHAPE
  (`config_option_json`, categories `model|thought_level`) — a shape, not an ACP transport.
- cit:([`CapabilitySnapshotWire`], dashboard/src/types/harnessCapabilities.ts:59-65): the full dynamic catalog plus
  nullable current model/effort selections; the wire shape permits `selectedEffort` to be null.
- cit:([`CapabilityEnvelope`], dashboard/src/types/harnessCapabilities.ts:68-75) + cit:([`CapabilityRouteErrorBody`], dashboard/src/types/harnessCapabilities.ts:78-81): the daemon envelope and
  the 404/409/503 error body (`status: capability-unavailable|control-unavailable`, verbatim
  `detail`) the store surfaces unreworded.
- `SetAcceptance` (= `SET_ACCEPTANCE_VALUES`, exactly five words) + `SetResultWire`: honest mutation
  evidence, never a generic success boolean — `effectiveValue` present
  only when the server PROVED the value took effect.
- `SubmissionReceiptWire` (`public_receipt_json`) and `ReconciliationState`/
  `ReconciliationResultWire` (`public_reconciliation_json`): resolve an ambiguous
  submit by requestId, never a resend.

### Invariants And Boundaries

- **DYNAMIC-ONLY: these are SHAPES.** No model key, effort key, or menu from any install may ever
  be copied here as a value — catalogs are live data fetched per install/auth. Fixture values live
  only under `test/fixtures/`.
- The file mirrors the current Python serializer fields and must not invent fields; consumers use
  these shapes without embedding a live catalog.

## Docs References

No Domain Documentation source is configured for this repository; repository code and tests are the authority.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live domain-documentation source was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The capability schema constant. | `CAPABILITY_SCHEMA` | dashboard/src/types/harnessCapabilities.ts:11-11 |
| Capability catalog envelope and route-error shapes. | `CapabilityEnvelope`, `CapabilityRouteErrorBody` | dashboard/src/types/harnessCapabilities.ts:68-75; dashboard/src/types/harnessCapabilities.ts:78-81 |
| Dynamic model, effort, config, and snapshot shapes. | `EffortOptionWire`, `ModelCapabilityWire`, `SessionConfigOptionWire`, `CapabilitySnapshotWire` | dashboard/src/types/harnessCapabilities.ts:16-22; dashboard/src/types/harnessCapabilities.ts:25-39; dashboard/src/types/harnessCapabilities.ts:48-56; dashboard/src/types/harnessCapabilities.ts:59-65 |
| Setter, submission, and reconciliation evidence shapes. | `SetResultWire`, `SubmissionReceiptWire`, `ReconciliationResultWire` | dashboard/src/types/harnessCapabilities.ts:89-96; dashboard/src/types/harnessCapabilities.ts:99-107; dashboard/src/types/harnessCapabilities.ts:120-128 |
| The daemon envelope serializer. | `CapabilityCatalogResult` | mcp/src/agents_remember/serving/harness_capability_catalog.py:49-65 |
| Snapshot and setter serializers plus acceptance vocabulary. | `SET_ACCEPTANCE_VALUES`, `capability_snapshot_json`, `set_result_json` | mcp/src/agents_remember/serving/harness_capabilities.py:21-23; mcp/src/agents_remember/serving/harness_capabilities.py:162-168; mcp/src/agents_remember/serving/harness_capabilities.py:216-225 |
| Public receipt and reconciliation serializers. | `public_receipt_json`, `public_reconciliation_json` | mcp/src/agents_remember/serving/harness_control_models.py:217-228; mcp/src/agents_remember/serving/harness_control_models.py:231-242 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| This file implements a repository-local contract. | — | — |

## 260715-FEUI-L5 Reliable Submit Delta

Prompt receipt and reconciliation types now include the bridge epoch, and the public submission
lifecycle union names the normalized authority states consumed by polling and withdrawal. The union
is deliberately raw-free and does not expose vendor queue details or adapter evidence.

## Update History
- 2026-08-04T08:45:26+02:00 — 260731-EFA-L6 S18-B07 curator correction: narrowed the schema claim to the constant definition; same-reviewer delta pending.

- 2026-07-17T21:39+02:00 — FEUI-L5: documented generation-bound receipt/reconcile types and the
  normalized lifecycle-state union.

- 2026-07-17T06:10+02:00 — Created for 260715-FEUI-L3 R1/R3 (capability wire mirror): the
  envelope (`schema`/`harness`/`cacheStatus hit|miss|refreshed`/`installFingerprint`/
  `capabilities`), model/effort/config snapshot shapes, the 404/409/503 route-error body, and the
  SetResult/receipt/reconciliation evidence shapes for L4/L5 — all hand-mirrored from the Python
  serializers and byte-verified by the L3 review. Verification metadata pinned to the leaf base
  until closeout stamps the L3 code commit.
