# mcp/src/agents_remember/worktrees/integration/closeout/integration_reopen.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/closeout/integration_reopen.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T00:53 |
| lastVerifiedCommitHash |  `7cbda30d9a9a4c2944382fbef46ac58b85329935`|
| lastVerifiedCommitDate |  2026-09-15T05:15:42+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Governing route overview](overview.md)

## Purpose

Owns the policy that decides whether a closeout must reopen an already completed integration.

## Code Commentary

### Logic

Completed external-memory reopening compares the newly accepted memory-content commit with its previous value and tests that same commit against the recorded memory source branch. A cache refresh cannot reopen integration because it supplies no produced commit.

`preview_integration_reopen` projects whether dirty or prospective code/memory output would need
another plane-owned integration. `completed_integration_reopen` evaluates the exact produced code and
memory-content commits against the recorded source branches. It reopens only when new
content is not yet landed; a no-op or already-landed closeout preserves completed state.

The helpers keep code and external-memory decisions separate so coverage and failure evidence name
the affected leg directly. They inspect ancestry but never move a branch, mutate the contract, or
integrate output themselves; the closeout coordinator owns publication of the returned decision.

### Conventions

Accepted input, exact Git facts, and typed owner results stay distinct from disposable projections.

### Invariants And Boundaries

- Integration status changes only from exact produced-commit and source-ancestry facts.
- A memory-only settings closeout can reopen memory without falsely reopening unchanged code.
- Already-landed or no-op output leaves completed integration intact.
- This module decides; it never mutates Git, contracts, or lifecycle journals.

### Todos

None recorded for the ledger-retirement boundary.

## Repo-Internal References

The following current source boundaries establish the ledger-retirement behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| `completed_integration_reopen` evaluates the two actual output commits against their source branches. | L49-L76 | [mcp/src/agents_remember/worktrees/integration/closeout/integration_reopen.py](mcp/src/agents_remember/worktrees/integration/closeout/integration_reopen.py) |
| `_completed_memory_is_unlanded` tests changed memory content and ancestry of that same content commit. | L94-L112 | [mcp/src/agents_remember/worktrees/integration/closeout/integration_reopen.py](mcp/src/agents_remember/worktrees/integration/closeout/integration_reopen.py) |

| Finding | Citations | Source Path |
| --- | --- | --- |
| Preview distinguishes prospective code and memory reopen effects. (`preview_integration_reopen`) | L13-L46 | [mcp/src/agents_remember/worktrees/integration/closeout/integration_reopen.py](mcp/src/agents_remember/worktrees/integration/closeout/integration_reopen.py) |
| Completed output is evaluated per code and memory leg. (`completed_integration_reopen`) | L49-L76 | [mcp/src/agents_remember/worktrees/integration/closeout/integration_reopen.py](mcp/src/agents_remember/worktrees/integration/closeout/integration_reopen.py) |
| Memory reopening requires changed content and an unlanded memory-content commit. (`_completed_memory_is_unlanded`) | L94-L112 | [mcp/src/agents_remember/worktrees/integration/closeout/integration_reopen.py](mcp/src/agents_remember/worktrees/integration/closeout/integration_reopen.py) |

## Cross-Repo References

No additional repository is consulted; the admitted worktree contract supplies both repository
and source-branch identities.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No additional cross-repository evidence applies. | — | — |

## Docs References

No external Domain Documentation source is configured for this slice. The current behavior is repository-owned and is supported by the source references below.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured external source applies. | — | — |

## Update History

- 2026-09-15T00:53 UTC — LCA-L9 working-candidate curation: retired ledger Git authority in this file-specific boundary; preserved real Git and lifecycle safeguards and prior history. Source and diff reviewed, source-sha256=fded29f92acd5273cbe1236bcf3071649d3eb9d16056e573e5a4ad88028b798f. Existing verification commit/date remain unchanged until an actual source commit is available; no test or acceptance claim.


- 2026-08-30T06:08+02:00 — MCAR-L03 A005: extracted completed-integration reopen policy from the
  closeout coordinator, preserving exact per-leg ancestry behavior while removing its CRAP and
  file-size pressure. Verification remains closeout-owned.
