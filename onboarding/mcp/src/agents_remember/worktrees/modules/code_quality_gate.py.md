# mcp/src/agents_remember/worktrees/modules/code_quality_gate.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/modules/code_quality_gate.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-24T14:31Z |
| lastVerifiedCommitHash |  `842b487b854503d95c9c2d9dce1841198ba93c7d`|
| lastVerifiedCommitDate |  2026-07-24T17:08:25+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[worktrees/modules overview](overview.md)

## Purpose

This module is the narrow policy and process adapter that makes the repository-owned source-quality
wrapper a mandatory, fail-closed gate before an Agents Remember worktree closeout creates a code
commit.

## Code Commentary

### Logic

`requires_strict_code_quality` limits the gate to closeouts that would create an `agents-remember`
code commit. `code_quality_gate_preview` exposes that decision and the canonical wrapper command
without mutation. `run_strict_code_quality_gate` requires the wrapper to exist, selects an
interpreter, executes the current worktree's `agents_remember.code_quality.check`, and raises with a
bounded output tail on any non-zero result.

`quality_python` prefers the worktree virtualenv, then the linked primary clone's shared virtualenv,
then the active server interpreter. `quality_environment` always puts the current worktree's
`mcp/src` first on `PYTHONPATH`, so a shared interpreter cannot measure the primary clone by mistake.

### Conventions

The interpreter search is necessary linked-worktree support: linked worktrees intentionally may not
carry their own `.venv`. It is an ordered authority chain, not a command fallback or an escape from
the project-owned wrapper.

### Invariants And Boundaries

- The only deliberate skip is a closeout that would not create an Agents Remember code commit.
- A missing wrapper, missing interpreter, or non-zero wrapper result refuses before closeout mutation.
- The default wrapper command is used as-is; no additional threshold-enforcement flag is required.
- Failure output is bounded to the last 40 lines while preserving the actionable exit status.

### Todos

No task-independent follow-up is recorded.

## Docs References

No external Domain Documentation source is configured for this memory repo.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation is configured for this repository-local gate. | — | — |

## Repo-Internal References

Closeout owns sequencing, while the quality wrapper owns the actual Ruff, Pyright, Radon, pytest,
coverage, and CRAP checks.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The module decides gate applicability, executes the strict wrapper, preserves current-worktree imports, and bounds failure output. | L21-L131 | [code_quality_gate.py](agents-remember/mcp/src/agents_remember/worktrees/modules/code_quality_gate.py) |
| Closeout previews the gate and runs it before `commit_if_dirty`. | L282-L335; L588-L596 | [closeout.py](agents-remember/mcp/src/agents_remember/worktrees/modules/closeout.py) |
| Focused regressions cover preview, worktree source precedence, bounded failures, interpreter selection, and mutation ordering. | L25-L201 | [test_worktree_closeout_quality_gate.py](agents-remember/mcp/tests/test_worktree_closeout_quality_gate.py) |

## Cross-Repo References

This gate acts only on the current Agents Remember code worktree.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repository authority participates in the gate decision. | L21-L36 | [code_quality_gate.py](agents-remember/mcp/src/agents_remember/worktrees/modules/code_quality_gate.py) |

## Update History

- 2026-07-24T14:31Z — 260718-CHATS-L5I incremental curator: created the sidecar for mandatory
  pre-code-commit quality enforcement, linked-worktree interpreter selection, current-worktree
  import precedence, and fail-closed bounded error reporting. Verification remains blank until the
  new source is committed.
