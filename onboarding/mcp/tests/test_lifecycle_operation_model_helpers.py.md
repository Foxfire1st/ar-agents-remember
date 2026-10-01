# mcp/tests/test_lifecycle_operation_model_helpers.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Lifecycle mutation-proof and worker-binding model invariants.

## Code Commentary

### Logic

The recovery-proof fixture contains only `codeCommit` and `memoryContentCommit`. It still
proves that a recorded output cannot contradict exact commit evidence, including the refusal
when the recorded code SHA changes. Removing the fake `ledgerCommit` attribute aligns this
existing case with the production model; it removes no test scenario.

Mutation history and the irreversible boundary require exact commit proof; recovery commits cannot contradict that proof. Worker PID, lease, fingerprint and termination evidence must form one complete authority rather than independently populated optional facts.

### Conventions

This card describes the current uncommitted LCA-L9 proof-test candidate. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

A model-valid snapshot is not permission to perform a mutation. These tests do not retain all historical migration or legacy-journal cases.

### Todos

No file-local implementation change is requested by this reconciliation.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

- Removed the fake ledgerCommit fixture field while preserving exact recovery-proof assertions. [1]
- Mutation history and irreversible boundary require exact proof. [2]
- Recovery commits cannot contradict commit proof. [3]
- Worker binding and termination evidence are one authority. [4]

### Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

Fixture repositories and protocol doubles do not establish a live external integration.
