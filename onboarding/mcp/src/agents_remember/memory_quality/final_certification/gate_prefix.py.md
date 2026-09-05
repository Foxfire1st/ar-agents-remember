# mcp/src/agents_remember/memory_quality/final_certification/gate_prefix.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/final_certification/gate_prefix.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T01:48+02:00 |
| lastVerifiedCommitHash | `16d1a4d6d6f8e8572b4bca10b8a4a84485449604` |
| lastVerifiedCommitDate | 2026-09-04T00:55:21+02:00 |
| governingOverview | `../overview.md` |

## Governing Overview

[memory_quality overview](../overview.md)

## Purpose

Exact green Gate 1-4 prerequisite adapter for the final Gate-5 certification (CCR-R08). No full
memory scan or coherence publication may start before the exact candidate's Gate 1-4
certificates are green and current: this adapter re-observes the R21 certificate chain and
reuse plan for one exact code candidate and refuses any stale, incomplete, or invalidated
prefix with a typed `FinalCertificationError`.

## Code Commentary

### Logic

Module-level surface:

- `GateFourPrefixProof` (class, lines 29-33) - the exact reusable green Gate 1-4 prefix:
  the reused certificate identities and the content digest of the R21 reuse plan.
- `require_green_gate_prefix` (lines 36-119) - admits one exact current green Gate 1-4
  prefix or refuses. Refusal routes: an ordered certificate set whose gates are not exactly
  (1, 2, 3, 4) is `gate-five-prefix-incomplete`; an admitted code tree that differs from the
  supplied `code_tree` is `gate-five-code-candidate-mismatch` (a code change restarts
  certification at Gate 1); `validate_certificate_chain` refusal is
  `gate-five-prefix-stale`; `plan_certificate_reuse` refusal or a reuse plan that is not
  exactly reuse-1-4 with first gate 5 and invalidation (5,) with no zero-gate start is
  `gate-five-prefix-invalidated`. Only the memory-only Gate-5 start (reuse Gates 1-4, first
  gate to run is 5) passes for the exact admitted code candidate.
- `_refusal_summary` (lines 122-126) - projects one stable refusal code from an R21
  exception's findings for the observed payload.

### Conventions

`plan_certificate_reuse` is the single R21 authority deciding reuse; this adapter never
re-decides reuse policy, it only enforces the exact memory-only start shape.

### Invariants And Boundaries

- Any earlier-gate invalidation, including a code change, refuses before any memory scan or
  coherence publication.
- The proof carries a `certificateReusePlanDigest` so the certification result stays bound
  to the exact reuse decision.

### Todos

None.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The exact reusable green Gate 1-4 prefix proof. | `GateFourPrefixProof` | mcp/src/agents_remember/memory_quality/final_certification/gate_prefix.py:29-33 |
| Admits the exact current green Gate 1-4 prefix or refuses with a typed refusal. | `require_green_gate_prefix` | mcp/src/agents_remember/memory_quality/final_certification/gate_prefix.py:36-119 |
| Stable one-code refusal summary from R21 findings. | `_refusal_summary` | mcp/src/agents_remember/memory_quality/final_certification/gate_prefix.py:122-126 |
| The R21 certificate-chain validator consumed by the adapter. | `validate_certificate_chain` | mcp/src/agents_remember/certification/certificate_authority.py:109-132 |
| The R21 reuse planner is the single reuse authority. | `plan_certificate_reuse` | mcp/src/agents_remember/certification/certificate_invalidation.py:124-162 |

## Update History

- 2026-09-04T01:48+02:00 — 260831-CCR-L08 Gate-5 memory pass: created this file-level
  onboarding card for the new CCR-R08 exact green Gate 1-4 prerequisite adapter module
  delivered in code commit 16d1a4d6; anchors and ranges derived from the current worktree
  source and pinned to that commit.
