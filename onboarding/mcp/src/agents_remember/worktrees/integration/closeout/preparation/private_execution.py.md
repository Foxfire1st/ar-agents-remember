# mcp/src/agents_remember/worktrees/integration/closeout/preparation/private_execution.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/closeout/preparation/private_execution.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T17:13:06+00:00 |
| lastVerifiedCommitHash | |
| lastVerifiedCommitDate | |
| governingOverview | `overview.md` |

## Governing Overview

[Owning overview](overview.md)

## Purpose

At-most-once journal-bound private Git execution.

## Code Commentary

### Logic

Each command start is selected before its single kernel call; actual exit/output hashes or unknown outcome are retained afterward. Live ownership and effective policy are reopened at action boundaries. Successful steps are not rerun, unresolved preparation is retained, and a named committed output is physically reobserved instead of discovering another commit. Shared execution does not advance logical branches.

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
| `_selected_leg` owns the corresponding behavior described above. | `_selected_leg` | `mcp/src/agents_remember/worktrees/integration/closeout/preparation/private_execution.py:37-46` |
| `private_git_binding` owns the corresponding behavior described above. | `private_git_binding` | `mcp/src/agents_remember/worktrees/integration/closeout/preparation/private_execution.py:49-66` |
| `_terminal_record` owns the corresponding behavior described above. | `_terminal_record` | `mcp/src/agents_remember/worktrees/integration/closeout/preparation/private_execution.py:95-115` |
| `_run_once` owns the corresponding behavior described above. | `_run_once` | `mcp/src/agents_remember/worktrees/integration/closeout/preparation/private_execution.py:118-183` |
| `observe_private_output` owns the corresponding behavior described above. | `observe_private_output` | `mcp/src/agents_remember/worktrees/integration/closeout/preparation/private_execution.py:186-200` |
| `prepare_private_output` owns the corresponding behavior described above. | `prepare_private_output` | `mcp/src/agents_remember/worktrees/integration/closeout/preparation/private_execution.py:203-237` |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository source is needed for this card. | N/A | N/A |

## Update History

### 2026-09-06T17:13:06+00:00 — Initial L34 implementation card

Created from the current source. Verification metadata is intentionally unset until a genuine commit-based verification occurs; no test or acceptance result is asserted.
