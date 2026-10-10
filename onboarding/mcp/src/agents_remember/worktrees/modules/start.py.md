# mcp/src/agents_remember/worktrees/modules/start.py

## Governing Overview

[worktree modules overview](overview.md)

## Purpose

Owns worktree start, attach, status result construction, and startup preparation for external memory and providers. Memory cannot be disabled for a task: every start runs in `external` mode, and a start that names the removed `disabled` mode — or the removed `disabled-memory` recovery answer — is refused by name before any worktree exists.

## Code Commentary

`start_result` refuses removed vocabulary first, at the top, because there it has no worktree, branch, contract, or task binding to unwind: `_removed_vocabulary_result` answers a removed `memory_mode` or `topology` (other than `disabled`) with the `memory-mode-unsupported` typed result and never substitutes `external` for what was asked; `disabled` is refused just below with its own opt-out refusal, never with the `internal` text; and `_unknown_choice_result` answers any other unknown `memory_choice` as an invalid request in the same shape as every mistyped start argument. The CLI no longer offers `disabled-memory` as a choice, so it still parses only so the start can refuse it by name.

A no-directive start still attaches to its live disabled leaf before new-parent admission: `_live_disabled_leaf_attach_result` fires only when the request names no memory directive at all and a live disabled leaf contract already exists at the requested address, returning the existing-contract result instead of letting fresh-contract admission refuse first. Genuinely new leaves, explicit disabled requests, and explicit conversions all keep the build path and its refusals.

The rest is unchanged. `start_result` consumes a request-scoped `StartContractPlan` (leaf contract plus the owner-validated preview-only parent, carried only for dry-run preview) through three stages — existing-contract reuse (a tombstone or reset recreates fresh), pre-creation preflights (stale base, fast-forward rebuild, Windows long-path check), and enclosure creation. Attach reselects and reconciles an atomic leaf's parent series before exposing the workbench; a series contract is never a workbench. The stale-base preflight blocks on `behind`/`diverged` with `choose_stale_base_recovery` (`proceed-stale` or `fast-forward`); `unknown` and `no-upstream` never block. Provider setup launches in the background after the contract is written, with `worktree_status` polling until a terminal state. After writing a leaf contract, start restamps the leaf doc's `lifecycleId`, and enclosure creation makes `<enclosure>/logs/` outside both worktrees and outside Git.

## Evidence

- Removed vocabulary refused before anything is created [16]
- Unknown recovery answer is invalid, never opt-out [17]
- No-directive start keeps its live disabled leaf [18]
- Refusal chain runs before context resolution [19]
- Live contract attaches, tombstone recreates [20]
