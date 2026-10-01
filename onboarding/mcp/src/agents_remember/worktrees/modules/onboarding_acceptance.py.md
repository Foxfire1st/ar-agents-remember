# mcp/src/agents_remember/worktrees/modules/onboarding_acceptance.py

## Governing Overview

[worktree modules overview](overview.md)

## Purpose

Applies exact candidate-bound no-content-impact and no-route-impact decisions to the existing
onboarding body classifications without weakening the untraced-content gate.

## Code Commentary

`OnboardingBodyGateEvidence` keeps the memory baseline and accepted no-impact identities together
at public body-gate boundaries. `apply_sidecar_no_impact` and `apply_route_no_impact` can move only
an already-`stale` identity into `attested_no_impact`. They never clear `untraced`, invent a
decision, reinterpret evidence, or turn an extra judgment into a passing classification.

## Invariants And Boundaries

- Semantic judgments originate in the validated curator-coherence authority, not this module.
- No-impact can accept byte-unchanged stale content only; authored untraced content remains a
  refusal until its body and Update History agree.
- The transformation is pure and deterministic, so preview, preflight, and refresh can share it.

## Evidence

### Repo-Internal References

- Body-gate evidence groups the memory baseline with accepted identities. [1]
- Sidecar and route decisions can remove only matching stale identities. [2]
