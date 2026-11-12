# mcp/src/agents_remember/worktrees/disabled_memory.py

## Governing Overview

[worktrees route overview](overview.md)

## Purpose

The single place that decides and shapes the refusal for the removed `disabled` memory mode (MIK-R50). No task can start in that mode, and no route that changes or lands a task accepts a contract carrying it. This module picks the refusal's true reason, builds its facts, and publishes one status with the known way out on every surface, asking for no developer decision because the action is known.

## Code Commentary

The module docstring states the four reason shapes: converted knowledge in the configured memory repository makes invariant work mandatory (D5) and the refusal names where it was found; otherwise the mode is refused as removed and unusable with the setup action where the repository is not set up; an unprobable repository names the probe failure and still refuses; a nonexistent memory root means no probe runs and the caller keeps the existing "memory is missing" error.

Reason selection lives in one helper probed against the conventional memory root (`memory-repos/ar-<repo>` under the coordination root). The cutover lock's converted-memory probe decides only which reason the refusal gives, never whether it applies. The raw cell is carried when the mode was read from an empty or unknown cell via the degraded read (`memory_mode='<token>' read as 'disabled'`); an explicit `disabled` token needs none.

Two refusal entry points serve the two subjects. The contract entry refuses a legacy disabled contract on every lifecycle-layer route that changes or lands a task, independently of the configured-authority check, with a leaf or series way out chosen from the contract kind; status, attach and abandon keep reading such contracts and never call it. The start entry answers at the top of `worktree_start` beside the removed-vocabulary refusal — the last point where no contract, branch, worktree, or binding exists to unwind — covering the `memory_mode` argument, the `disabled-memory` choice answer, and both module CLI options, with dry run and real run answering identically. Where the memory root does not exist at all it returns nothing so the start keeps the context-resolution missing-memory error.

## Evidence

- Removed mode, one status, known way out, no developer decision [1]
- Conventional memory root and non-external contract detection [2]
- Reason selection: missing root, probe failure, converted knowledge, unconfigured repo [3]
- Raw cell carried only for degraded empty/unknown-cell reads [4]
- Contract entry refusal scope; status, attach and abandon keep reading [5]
- Start entry placement, full option coverage, missing root returns nothing [6]
