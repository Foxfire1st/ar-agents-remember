# PDLS Onboarding Wave 005 — Reopened Evidence-System Curation

| Field | Value |
| --- | --- |
| repo | agents-remember |
| generated | 2026-08-28T06:40+02:00 |
| waveType | verification-route reconciliation, deleted-slice cleanup, missing-card completion |
| mode | existing-memory-slice-maintenance |
| status | curator-reviewed — pass |
| source candidate commit | `71996c35aa1bd8260a84a51e6bc1706637a1437a` |
| source candidate tree | `d854a5ec4ec30edb793290d032fb9d32d4fb691e` |

## Goal

Reconcile durable onboarding to the independently reopened PDLS implementation: make verification
ownership explicit, remove Candidate A and stale fixture memory, complete missing focused test
cards, and preserve the exact distinction between non-accepting route evidence and certification.

## Included Population

| Population | Result |
| --- | --- |
| Path-rule-eligible logical changes | 157 reconciled |
| Deleted pre-existing excluded-fixture sidecars | 3 removed |
| Verification Python route | 50 sources / 50 sidecars |
| Missing focused test sidecars | 6 created |
| Matching high-risk file cards | 6 created |
| Retired Candidate A and product-verification routes | old-path memory removed; no compatibility shadow |

## New Focused Test Cards

| Source | Ownership preserved |
| --- | --- |
| `mcp/tests/test_cadence_runner.py` | cadence selection and non-accepting evidence |
| `mcp/tests/test_causal_failure_localization.py` | exact-node causal suppression |
| `mcp/tests/test_causal_quality_preflight.py` | causal contract admission and safe continuation |
| `mcp/tests/test_evidence_lanes.py` | exhaustive explicit evidence categories |
| `mcp/tests/test_evidence_lifecycle.py` | 34-artifact lifecycle/consumer governance |
| `mcp/tests/test_route_measurement.py` | repeated pure/integration/durability route measurement |

## Additional Reconciliation

- Refreshed every changed eligible source sidecar, including mechanical import moves and explicit
  product/verification fixture classifications.
- Corrected the surviving Claude fixture provenance to 2.1.210/2.1.217 and removed three deleted
  2.1.207 sidecars.
- Corrected the PI RPC smoke-card explanation so its literal fixture path is recognized as an
  observable lifecycle consumer.
- Preserved the 34-artifact inventory, Candidate A retirement, 50/50 verification census, and the
  requirement-attempt journal's separation from queue authority.

## Acceptance

- Exact changed-source-to-sidecar audit reports zero missing and zero unchanged current cards.
- Deleted and moved old paths leave no live sidecars or compatibility routes.
- The six new cards pass cold read and link their nearest governing overview.
- Sanctioned route-index refresh followed by a repeat preview reports no stale index.
- c-02 memory-quality checks report no actionable finding.
- The wave makes no Q9, CodeRabbit, Q11, landing, or closeout claim.

## Current Disposition

Content reconciliation and deterministic validation are complete for the exact successor source
candidate. The final route-index preview reports 76 unchanged indexes and zero stale indexes;
document-shape, history-order, citation-range, citation-claim, and table checks report zero
enforcing findings across 1,999 Markdown files; the entity catalog reports zero findings; and the
added-source audit reports 73 sources with zero missing onboarding pairs. The curator verdict is
recorded in `bootstrap/reviews/onboarding-wave-005.curator.md`. This wave does not claim Q9
acceptance, final Dagger certification, landing, or closeout.
