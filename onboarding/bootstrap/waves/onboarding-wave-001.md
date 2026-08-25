# Onboarding Wave 001 — PDLS Exact Candidate

| Field | Value |
| --- | --- |
| repo | agents-remember |
| task | 260824-PDLS |
| generated | 2026-08-25T16:21:43+02:00 |
| waveType | route-overview + file-onboarding |
| mode | existing-memory-slice-maintenance |
| status | curator-review |

## Goal

Reconcile every changed source unit and the shared routes introduced or materially changed by the
PDLS evidence-system and lifecycle/closeout quality repair.

## Included Population

| Population | Created | Refreshed | Total |
| --- | ---: | ---: | ---: |
| Production sidecars | 35 | 11 | 46 |
| Test/support sidecars | 34 | 26 | 60 |
| Dashboard contract-guard sidecars | 0 | 1 | 1 |
| Dependent unchanged fixture sidecars | 0 | 1 | 1 |
| Route overviews | 7 | 1 parent | 8 |

## Instructions Applied

- Strict one-to-one source mapping and nearest governing overview.
- Body update plus newest append-only history on every refreshed sidecar.
- Empty Domain Documentation and disabled cross-repo sources stated explicitly.
- No task-local design prose promoted as source truth.
- No fallback, compatibility facade, threshold waiver, or direct-evidence elevation.

## Deferred

None.

## Done When

All 107 changed-source sidecars exist, the dependent fixture sidecar is current, route indexes
match the resulting tree, structural/reference checks pass,
and the curator review records zero actionable finding.
