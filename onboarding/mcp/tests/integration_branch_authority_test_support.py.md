# mcp/tests/integration_branch_authority_test_support.py

| Field | Value |
| --- | --- |
| verificationStatus | working-candidate |

The body describes the uncommitted LCA L9 working candidate. The commit fields identify the latest real commit touching this source file; they do not claim that the candidate is committed or accepted.

## Governing Overview

[Nearest governing route overview](overview.md)

## Purpose

Build configured disposable repository/topology and closed-leaf fixtures for integration authority scenarios.

## Code Commentary

### Logic

`_authority_fixture` constructs the exact code/memory repositories, protected branches, task topology, selected profile configuration, and sibling atomic-series contract. External baseline memory is a real content commit with Code-Commit attribution; its ledger is refreshed only as an untracked cache.

`_closed_external_leaf_worktrees` materializes the ordinary leaf worktrees and onboarding root, creates actual code and attributed memory commits, refreshes the disposable cache, and records only the two accepted outputs. `_publish_completed_closeout_fixture` optionally enters the selected/ordinary lifecycle input owner before publishing the fixture's completed state; its explicit final-source override models target changes after admission. `_doc` remains the small task-model builder.

Unused atomic-landing/door/preview builders and their ledger-only commit machinery were removed. Support code itself is not collected scenario coverage.

### Conventions

Helpers build production-shaped inputs for their consumers; synthetic completed fixture state is not an executed acceptance or certification result. Candidate repositories and paths remain explicitly configured and confined to the temporary world.

### Invariants And Boundaries

- Real code/memory objects back the recorded output cells.
- Cache materialization produces no third commit or ledger output field.
- Onboarding-root and canonical task/enclosure identity remain present so tests reach their intended seam.
- No queue row or guessed ambient path substitutes for ref authority.

### Todos

No new file-local follow-up is identified by this source reconciliation.

## Evidence

### Docs References

No domain-documentation source is configured for this slice. The behavior described here is established by current repository source and the authorized LCA L9 change, rather than an invented external reference.

### Repo-Internal References

These current source spans identify the implementation owners and the specific assertions supporting the file's behavior. A test definition is evidence of its assertions, not an execution or certification receipt.

- Closed external leaves are backed by two actual commits and a disposable cache. [1]
- Optional lifecycle admission precedes fixture finalization. [2]
- Configured repository, profile, protected branches, and task topology. [3]
- Consumers retain ownership, cache-independence, and CAS scenarios. [4]

### Cross-Repo References

The operation and fixture boundaries described here are defined by same-repository contracts and Git helpers. No separate cross-repository document is used as evidence for this card.
