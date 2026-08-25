# PDLS Onboarding Coverage Plan

## Strategy

Reconcile the exact atomic-master diff at its owning routes. Create sidecars for every changed
source unit that lacked one, refresh the body and append history for every existing sidecar, and
add route pillars only where several changed owners share an operating model.

## Route Coverage

| Route | Classification | Outcome |
| --- | --- | --- |
| application/lifecycle | public workflow boundary | overview + 2 file sidecars |
| code_quality | certifying quality workflow | overview + changed owner sidecars |
| models/closeout | disposable projection contract | overview + projection sidecar |
| testing | evidence/bootstrap infrastructure | overview + changed owner sidecars; no facade |
| worktrees/integration/closeout | door/ledger recovery workflow | overview + changed sidecars |
| worktrees/integration/legacy | bounded migration/archive workflow | overview + changed sidecars |
| worktrees/integration/lifecycle | enclosure-root journal workflow | overview + changed sidecars |
| worktrees/queue | disposable scheduling projection | existing overview + changed sidecars |
| mcp/tests | production-bound forcing | existing overview + all 60 changed sidecars refreshed/created |
| dashboard/src/test | independent representative-payload contract guard | existing overview + changed guard sidecar refreshed; dependent snapshot sidecar corrected |

## Evidence Packs

No docs or boundary pack is needed: the configured Domain Documentation registry is empty and
cross-repository reads are disabled. Source, tests, approved requirements, and Dagger reports are
the direct evidence.

## Deferred Routes And Files

None. This atomic master has no onboarding deferrals.

## Validation

Require zero missing sidecars for the exact changed source population, valid governing backlinks,
append-only history, no absolute paths, current generated indexes, and no curator-actionable
memory-quality finding before restoring L12-S4.
