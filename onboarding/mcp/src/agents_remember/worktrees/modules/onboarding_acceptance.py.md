# mcp/src/agents_remember/worktrees/modules/onboarding_acceptance.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/modules/onboarding_acceptance.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-29T18:29+02:00 |
| lastVerifiedCommitHash |  `60e429d17e9fcbca3ab1c02563afcaa5761b8c5a`|
| lastVerifiedCommitDate |  2026-08-29T20:33:10+02:00|
| governingOverview | `overview.md` |

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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Body-gate evidence groups the memory baseline with accepted identities. | `OnboardingBodyGateEvidence` | mcp/src/agents_remember/worktrees/modules/onboarding_acceptance.py:15-21 |
| Sidecar and route decisions can remove only matching stale identities. | `apply_sidecar_no_impact`; `apply_route_no_impact`; `_accept_unchanged` | mcp/src/agents_remember/worktrees/modules/onboarding_acceptance.py:24-69 |

## Update History

- 2026-08-29T18:29+02:00 — Created for the single no-impact application boundary shared by
  closeout preview, admission, and external-memory refresh. Verification remains closeout-owned.
