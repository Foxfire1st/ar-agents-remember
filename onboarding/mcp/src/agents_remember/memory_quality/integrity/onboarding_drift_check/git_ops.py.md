# mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/git_ops.py

## Governing Overview

[overview.md](../../../../../overview.md)

## Purpose

`git_ops.py` retains only branch-name lookup through the shared kernel Git runner. It neither computes fingerprints, inventories source, classifies memory nor produces staged/unstaged change notes.

## Code Commentary

### Logic

`current_branch_name` runs `rev-parse --abbrev-ref HEAD` through `kernel.git_command.run_git`. Nonzero return or empty stripped stdout yields `unknown-branch`; no local runner, explicit timeout override or stdin input is supplied.

### Conventions

Git subprocesses still cannot consume MCP stdio transport input, but the guarantee is
`kernel.git_command.run_git`'s: it passes `stdin=subprocess.DEVNULL` unless a caller supplies
`input_text`, and no helper here supplies one.

### Invariants And Boundaries

- Branch observation only: no classification or policy.
- The kernel runner owns repository-selector scrubbing, DEVNULL stdin and its timeout/encoding defaults; this module must not grow a second runner.

## Evidence

### Repo-Internal References




- The sole current_branch_name helper uses the kernel Git runner and yields unknown-branch for failed or empty branch lookup. [3]
