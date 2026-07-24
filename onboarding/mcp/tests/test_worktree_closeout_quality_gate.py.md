# mcp/tests/test_worktree_closeout_quality_gate.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_worktree_closeout_quality_gate.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-24T14:31Z |
| lastVerifiedCommitHash |  `842b487b854503d95c9c2d9dce1841198ba93c7d`|
| lastVerifiedCommitDate |  2026-07-24T17:08:25+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

This suite proves the strict worktree closeout quality gate's policy, execution authority, failure
containment, interpreter selection, and ordering before the code commit.

## Code Commentary

### Logic

`CodeQualityGateTests` exercises preview requirements, the exact default wrapper command,
current-worktree `PYTHONPATH` precedence, bounded failure output, and worktree/shared-clone
virtualenv selection. `CloseoutCodeQualityGateTests` uses real temporary external-memory contract
fixtures with mocked gate execution to prove a failure leaves code HEAD, memory HEAD, ledger bytes,
and contract closeout state unchanged, while success records `quality` before `code-commit`.

### Conventions

The tests inject runners and gate functions only at the narrow process boundary. They retain real
worktree contract and Git behavior where mutation ordering is the contract under test.

### Invariants And Boundaries

- Preview requires the gate only for an Agents Remember code commit.
- The executed module must come from the current worktree even when Python is shared.
- Failure evidence is useful but bounded.
- Gate failure precedes every code, memory, ledger, and contract mutation.
- Successful closeout records quality before the first code commit event.

### Todos

No durable follow-up is recorded.

## Docs References

No external Domain Documentation source is configured for this memory repo.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No external documentation is needed for these repository-local regressions. | — | — |

## Repo-Internal References

The suite proves the adapter and its production closeout call site together.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Adapter-focused tests cover applicability, invocation, worktree import authority, bounded failures, and interpreter selection. | L25-L127 | [test_worktree_closeout_quality_gate.py](agents-remember/mcp/tests/test_worktree_closeout_quality_gate.py) |
| Closeout integration tests prove zero mutation on failure and quality-before-commit on success. | L130-L201 | [test_worktree_closeout_quality_gate.py](agents-remember/mcp/tests/test_worktree_closeout_quality_gate.py) |
| The production adapter implements the behavior exercised here. | L21-L131 | [code_quality_gate.py](agents-remember/mcp/src/agents_remember/worktrees/modules/code_quality_gate.py) |

## Cross-Repo References

The tests operate entirely on repository-local temporary fixtures.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repository behavior is asserted. | L25-L201 | [test_worktree_closeout_quality_gate.py](agents-remember/mcp/tests/test_worktree_closeout_quality_gate.py) |

## Update History

- 2026-07-24T14:31Z — 260718-CHATS-L5I incremental curator: created the sidecar for the strict
  closeout-gate policy, linked-worktree interpreter, fail-closed mutation ordering, and success
  ordering regressions. Verification remains blank until the new test source is committed.
