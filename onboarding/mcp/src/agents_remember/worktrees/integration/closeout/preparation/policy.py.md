# mcp/src/agents_remember/worktrees/integration/closeout/preparation/policy.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/closeout/preparation/policy.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T17:13:06+00:00 |
| lastVerifiedCommitHash | `d36109038b3f2b500c138f9dc1ea9c9f9a247489`|
| lastVerifiedCommitDate | 2026-09-06T22:21:49+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Owning overview](overview.md)

## Purpose

Actual Git configuration, identity environment and hook policy observation.

## Code Commentary

### Logic

The policy hashes effective binary Git configuration and selected identity environment without exposing their values. Only the runner-owned safe.directory authorization is excluded. Hook observation binds regular non-linked file bytes, executable state and before/after identity, then rechecks configuration. require_intent compares the actual observation with the selected intent; conditional or worktree-specific divergence refuses rather than silently using another policy.

### Conventions

Use the named source owners directly. This source was introduced in landed commit `245057ab16e19afdaabd5c188c9576b22e0c0870` and remains byte-identical at the recovery code candidate. Its behavior was re-read against that source during memory recovery; the existing metadata owner still owns the pending verification stamp.

### Invariants And Boundaries

The documented types and paths do not themselves establish execution, certification, delivery or acceptance. Those claims require the corresponding owning runtime evidence.

### Todos

No source-local TODO is asserted here.

## Docs References

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation applies. | N/A | N/A |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| `PreparationPolicyError` owns the corresponding behavior described above. | `PreparationPolicyError` | `mcp/src/agents_remember/worktrees/integration/closeout/preparation/policy.py:38-39` |
| `GitPreparationPolicy` owns the corresponding behavior described above. | `GitPreparationPolicy` | `mcp/src/agents_remember/worktrees/integration/closeout/preparation/policy.py:43-52` |
| `_configuration_digest` owns the corresponding behavior described above. | `_configuration_digest` | `mcp/src/agents_remember/worktrees/integration/closeout/preparation/policy.py:55-74` |
| `_hook_observation` owns the corresponding behavior described above. | `_hook_observation` | `mcp/src/agents_remember/worktrees/integration/closeout/preparation/policy.py:77-107` |
| `_file_identity` owns the corresponding behavior described above. | `_file_identity` | `mcp/src/agents_remember/worktrees/integration/closeout/preparation/policy.py:110-118` |
| `observe_git_preparation_policy` owns the corresponding behavior described above. | `observe_git_preparation_policy` | `mcp/src/agents_remember/worktrees/integration/closeout/preparation/policy.py:121-129` |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository source is needed for this card. | N/A | N/A |

## Update History

### 2026-09-06T17:13:06+00:00 — Initial L34 implementation card

Created from the current source. Verification metadata is intentionally unset until a genuine commit-based verification occurs; no test or acceptance result is asserted.
