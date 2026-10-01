# mcp/src/agents_remember/worktrees/integration/integration_operation_authority.py

| Field | Value |
| --- | --- |
| verificationStatus | working-candidate |

The body describes the uncommitted LCA L9 working candidate. The commit fields identify the latest real commit touching this source file; they do not claim that the candidate is committed or accepted.

## Governing Overview

[Nearest governing route overview](overview.md)

## Purpose

Re-prove that a final integration output is the exact closeout pair recorded on its contract.

## Code Commentary

### Logic

`require_authorized_integration_commits` compares `(code_commit, memory_content_commit)` with the contract's two accepted closeout outputs. A mismatch refuses publication and requires a new closeout after conflict resolution. This check reads contract output facts; current source tips and ancestry belong to the separate ref-preparation boundary.

### Conventions

The retained WorktreeArgs parameter is not an alternate authority source. This module neither reads a journal to choose a candidate nor consults cache data.

### Invariants And Boundaries

- No unrecorded replay result may substitute for the accepted pair.
- There is no ledger output slot or dummy ledger identity.
- Matching output cells do not bypass the caller's ownership, source-tip, ancestry, and CAS checks.

### Todos

No new file-local follow-up is identified by this source reconciliation.

## Evidence

### Docs References

No domain-documentation source is configured for this slice. The behavior described here is established by current repository source and the authorized LCA L9 change, rather than an invented external reference.

### Repo-Internal References

These current source spans identify the implementation owners and the specific assertions supporting the file's behavior. A test definition is evidence of its assertions, not an execution or certification receipt.

- Final output authority is the contract's exact accepted pair. [1]
- Source and ref proof remain at the prepared movement boundary. [2]

### Cross-Repo References

The operation and fixture boundaries described here are defined by same-repository contracts and Git helpers. No separate cross-repository document is used as evidence for this card.
