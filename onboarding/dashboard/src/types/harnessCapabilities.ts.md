# dashboard/src/types/harnessCapabilities.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/types/harnessCapabilities.ts`     |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T06:10+02:00                           |
| lastVerifiedCommitHash | `96e1d6db63454438b57a7485382c27784a60776f`       |
| lastVerifiedCommitDate | 2026-07-17T06:28:52+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

The TypeScript mirror of the **pre-session capability contract** (260715-FEUI-L3 R1/R3): the
daemon envelope `CapabilityCatalogResult.to_json()`
(`mcp/src/agents_remember/serving/harness_capability_catalog.py`) nesting the normalized snapshot
`capability_snapshot_json()` (`serving/harness_capabilities.py`), served by
`GET /api/harnesses/{h}/capabilities`. The Python serializers are the source of truth — kept in
lockstep BY HAND, camelCase matching the wire form (same posture as `types/terminalCatalog.ts`);
the L3 reviewer verified every field name byte-level against the serializers. Also hosts the live
setter/submit/reconcile evidence shapes (`SetResultWire`, `SubmissionReceiptWire`,
`ReconciliationResultWire`) consumed by the L4/L5 leaves via the fixture pack.

## Code Commentary

### Logic

- `CAPABILITY_SCHEMA = "ar-harness-capabilities/v1"` (L11) + `CapabilityCacheStatus`
  `hit|miss|refreshed` (L13) — hit = served from cache; miss/refreshed both ran the SAME
  short-lived native discovery (the R2 cost-honesty fact the store's copy names).
- `EffortOptionWire` (L16-L22): one vendor token accepted by one specific model
  (`effort_option_json`) — `launchSettable`/`sessionSettable` booleans gate the launch flow's
  effort menu (R4).
- `ModelCapabilityWire` (L25-L39): one dynamically advertised model with its model-gated effort
  menu (`model_capability_json`) — `effortOptions` is the advertised NATIVE order, never reordered
  client-side; `hidden`/`selectable`/`isDefault`/`defaultEffort` are catalog data; Pi rows keep
  the provider-qualified `key` (`provider/id`) verbatim with `provider` alongside (L37-L38).
- `SessionConfigOptionWire` (L48-L56): the ACP Sense 1 select-config SHAPE
  (`config_option_json`, categories `model|thought_level`) — a shape, not an ACP transport.
- `CapabilitySnapshotWire` (L59-L65): the full dynamic catalog + current selection;
  `selectedEffort` is null on a fresh Claude session — stream-json emits no launch-effort echo
  (recorded L5 evidence).
- `CapabilityEnvelope` (L68-L75) + `CapabilityRouteErrorBody` (L78-L81): the daemon envelope and
  the 404/409/503 error body (`status: capability-unavailable|control-unavailable`, verbatim
  `detail`) the store surfaces unreworded.
- `SetAcceptance` (L86, = `SET_ACCEPTANCE_VALUES`, exactly five words) + `SetResultWire`
  (L89-L96): honest mutation evidence, never a generic success boolean — `effectiveValue` present
  only when the server PROVED the value took effect.
- `SubmissionReceiptWire` (L99-L106, `public_receipt_json`) and `ReconciliationState`/
  `ReconciliationResultWire` (L108-L117, `public_reconciliation_json`): resolve an ambiguous
  submit by requestId, never a resend.

### Invariants And Boundaries

- **DYNAMIC-ONLY: these are SHAPES.** No model key, effort key, or menu from any install may ever
  be copied here as a value (module header, L8-L9) — catalogs are live data fetched per
  install/auth. Fixture values live only under `test/fixtures/`.
- Any server field addition lands HERE first, then in consumers; the file must track the Python
  serializers, not invent fields.
- `types/terminalCatalog.ts` was deliberately NOT touched by L3 — new wire shapes go to new files.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Schema constant, cache-status union, and all wire interfaces. | L11-L117 | [harnessCapabilities.ts](harnessCapabilities.ts) |
| The envelope serializer (`CapabilityCatalogResult.to_json()`), source of truth. | L59-L64 | [harness_capability_catalog.py](../../../mcp/src/agents_remember/serving/harness_capability_catalog.py) |
| The snapshot/model/effort/config serializers + `SET_ACCEPTANCE_VALUES`. | L162-L227 | [harness_capabilities.py](../../../mcp/src/agents_remember/serving/harness_capabilities.py) |
| Receipt/reconciliation serializers (`public_receipt_json`/`public_reconciliation_json`). | L274-L296 | [harness_control_models.py](../../../mcp/src/agents_remember/serving/harness_control_models.py) |
| The memory-only store that adopts/refuses envelopes of this shape. | — | [../data/capabilityCatalog.ts](../data/capabilityCatalog.ts) |
| The fixture pack instantiating every shape declared here. | — | [../test/fixtures/capabilityEnvelopes.ts](../test/fixtures/capabilityEnvelopes.ts), [../test/fixtures/controlMessages.ts](../test/fixtures/controlMessages.ts) |
| The conformance suite asserting the pack against the recorded L5 samples. | — | [../test/contractCapabilities.test.ts](../test/contractCapabilities.test.ts) |
| The sibling hand-mirrored wire type this follows the posture of. | — | [terminalCatalog.ts](terminalCatalog.ts) |

## Update History

- 2026-07-17T06:10+02:00 — Created for 260715-FEUI-L3 R1/R3 (capability wire mirror): the
  envelope (`schema`/`harness`/`cacheStatus hit|miss|refreshed`/`installFingerprint`/
  `capabilities`), model/effort/config snapshot shapes, the 404/409/503 route-error body, and the
  SetResult/receipt/reconciliation evidence shapes for L4/L5 — all hand-mirrored from the Python
  serializers and byte-verified by the L3 review. Verification metadata pinned to the leaf base
  until closeout stamps the L3 code commit.
