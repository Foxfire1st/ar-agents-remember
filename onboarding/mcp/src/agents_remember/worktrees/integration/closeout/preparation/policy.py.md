# mcp/src/agents_remember/worktrees/integration/closeout/preparation/policy.py

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

## Evidence

### Docs References

No configured domain documentation applies.

### Repo-Internal References

- `PreparationPolicyError` owns the corresponding behavior described above. [1]
- `GitPreparationPolicy` owns the corresponding behavior described above. [2]
- `_configuration_digest` owns the corresponding behavior described above. [3]
- `_hook_observation` owns the corresponding behavior described above. [4]
- `_file_identity` owns the corresponding behavior described above. [5]
- `observe_git_preparation_policy` owns the corresponding behavior described above. [6]

### Cross-Repo References

No cross-repository source is needed for this card.
