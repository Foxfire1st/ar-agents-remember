# mcp/src/agents_remember/package_data/runtime/skills/c-09-git-worktree-manager/SKILL.md

## Governing Overview

[MCP package overview](../../../../../../overview.md)

## Purpose

This generated runtime skill propagates the canonical root skill's exact-pair landing guidance. It distinguishes leaf rejudgment from the master validator/staleness/chain/history checks and separates public direct recover refusal from the real executor's receipt settlement. Edit the canonical skill and regenerate copies; this file is no second authority.


Documents `c-09-git-worktree-manager`, the Git worktree lifecycle manager for Agents Remember tasks: worktree start, attach/status, external-memory compatibility before start, integration, lifecycle finalization, and cleanup, plus reopening (`task_reopen` resets a fully landed leaf to planning under its exact leaf id). Closeout sequencing belongs to `c-12-closeout`; this skill only supplies the worktree-specific configured leaf path and the integration/finalization follow-up rules.

## Code Commentary

Task identity is settled before worktree creation: a master owns the root `series-contract.md` plus its integration branch, and each build leaf owns its enclosure contract. The Worktree Intent Gate must be explicitly approved before start and must name branch policy, source/work branches, memory mode, landing path, and risks. Standalone/new/final work stops for developer approval, while subordinate accepted-series work continues under recorded series authority.

External memory incompatibility is interactive and offers `reconciliation` or `custom` handling — there is no `disabled-memory` recovery choice. Memory cannot be disabled for a task: a start naming the removed `disabled` mode or the removed `disabled-memory` answer is refused by name (`memory-opt-out-refused`) before any worktree is created. A contract on disk that carries the removed mode is abandoned and started again: save the changes worth keeping, run `worktree_abandon` (dry run first), then `worktree_start` at the same address without `memory_mode`. The common incompatibility trigger remains starting off a freshly-merged gated branch whose PR merge commit the ledger has not mapped; `memory.md` stays an ignored consumer cache whose absence, staleness, or malformed bytes never make an otherwise valid pair incompatible.

Integration follows applicable authority (`ff-only` for unmoved sources, `replay` for parallel work); the recorded `source_branch` is the integration target. Lifecycle finalization proves the landed commit reachable from the recorded local source branch, runs or verifies cleanup, and reconciles task documents to `Completed`. The closeout preview runs no quality/test/memory/certification/review tool but does ask the mandatory invariant gate on converted memory. Atomic-series activation is scoped to the exact canonical series contract; terminal cleanup releases only the exact still-selected contract.

## Evidence

- No `disabled-memory` choice; abandon-and-restart way out [15]
- Removed answer refused by name, never honored [16]
- Removed member refused by name at the vocabulary [17]
