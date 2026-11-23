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

`_closed_external_leaf_worktrees` materializes the ordinary leaf worktrees and onboarding root, creates the converted knowledge marker and authored no-impact coverage, then commits code and attributed memory. It refreshes the disposable cache and records two output cells. When requested, `_publish_completed_closeout_fixture` binds fixture services, loads the contract, and writes and reloads the completed fixture with the same output pair. The optional branch override varies the recorded final code source. `_doc` builds the task model.

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

Closed fixture commits also carry actual-tree Commit-Check-Pass trailers with hook=none. Those trailers are synthetic fixture inputs; their presence is not an executed repository-hook or acceptance result.

## Evidence

### Docs References

No domain-documentation source is configured for this slice. The behavior described here is established by current repository source and the authorized LCA L9 change, rather than an invented external reference.

### Repo-Internal References

These current source spans identify the implementation owners and the specific assertions supporting the file's behavior. A test definition is evidence of its assertions, not an execution or certification receipt.



- Closed external leaves are backed by two actual commits and a disposable cache. [1]





- The fixture publisher writes and reloads an already-completed contract with the retained output pair and optional final-source override. [2]





- Configured repository, profile, protected branches, and task topology. [3]



- Consumers retain ownership, cache-independence, and CAS scenarios. [4]


### Cross-Repo References

The operation and fixture boundaries described here are defined by same-repository contracts and Git helpers. No separate cross-repository document is used as evidence for this card.

- Closed fixture commits also carry actual-tree Commit-Check-Pass trailers with hook=none. Those trailers are synthetic fixture inputs; their presence is not an executed repository-hook or acceptance result. [5]
