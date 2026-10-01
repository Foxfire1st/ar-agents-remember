# dashboard/src/types/harnessCapabilities.ts

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

## Evidence

### Docs References

No Domain Documentation source is configured for this repository; repository code and tests are the authority.

No configured live domain-documentation source was available.

### Repo-Internal References

- The capability schema constant. [1]
- Capability catalog envelope and route-error shapes. [2]
- Dynamic model, effort, config, and snapshot shapes. [3]
- Setter, submission, and reconciliation evidence shapes. [4]
- The daemon envelope serializer. [5]
- Snapshot and setter serializers plus acceptance vocabulary. [6]
- Public receipt and reconciliation serializers. [7]

### Cross-Repo References

No meaningful cross-repo references found.

This file implements a repository-local contract.

## 260715-FEUI-L5 Reliable Submit Delta

Prompt receipt and reconciliation types now include the bridge epoch, and the public submission
lifecycle union names the normalized authority states consumed by polling and withdrawal. The union
is deliberately raw-free and does not expose vendor queue details or adapter evidence.
