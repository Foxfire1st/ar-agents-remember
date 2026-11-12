# mcp/tests/closeout_input_test_support.py

## Governing Overview

[Nearest governing overview](overview.md)

Working candidate verification: source inspected at 2026-09-15T01:02 UTC against the uncommitted L9 candidate.
The commit fields identify the latest real commit touching this source; they do not identify a future commit for the working changes.

## Purpose

Provides shared typed closeout inputs, operation setup, mutation evidence recording/builders,
and finalization fixtures. It composes production models rather than parallel test-only input shapes.

## Code Commentary

### Logic

`closeout_operation_input` and `closeout_worktree_args` normalize explicit code/memory messages
through the production input boundary. Unknown fixture keywords are rejected; there is no ledger
message default or ledger parameter. The arguments retain the repository-owned certification
profile default where that fixture needs one.

`start_closeout_operation` maps enabled messages into canonical admission. Legacy journal-plane
fixtures may obtain a deliberately synthetic waiting generation and bypass only its first-ready
scheduling assertion; a fixture with real scheduling evidence keeps that fence. The synthetic
current generation no longer carries ledger memory/provenance/dependency fields.

`MutationEvidenceRecorder` checks monotonic intent/proven transitions and stable before/expected
trees. The builders construct intent, reconciled-unchanged, and commit-proven typed evidence for the
remaining legs. Running/terminal helpers advance explicit fixture records through their store.
`publish_closeout_finalization` projects actual code and memory content commits into recovery cells,
without a ledger output.

### Conventions

The support is a test composition boundary, not production admission authority. Its narrowly
scoped scheduling patch must stay visible in callers' evidence claims. Queue fixtures and operation
input/evidence fixtures retain separate responsibilities.

### Invariants And Boundaries

- Enabled real outputs cross the same message normalization used by production.
- No helper synthesizes a ledger leg or accepts an obsolete ledger keyword.
- Mutation builders retain exact generation and before/expected/proven evidence shapes.
- Fixture setup or a consumer declaration is not execution or certification evidence.

### Todos

No new implementation or live-state operation is authorized by this documentation pass.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository. No external domain documents
were available through the configured registry to consult; the current claims are grounded in the
working source and package-local evidence below. The registry is discovery input, not a citation.

No configured external domain-documentation evidence.

### Repo-Internal References

These repository-relative targets and exact ranges were checked against the L9 working source.
Source declarations and test assertions are distinguished from execution and acceptance evidence.

- The recorder verifies typed progress transitions. [1]
- Canonical setup passes only enabled code/memory messages. [2]
- Finalization publishes code/memory recovery cells. [3]
- Input and WorktreeArgs builders share production normalization. [4]
- Evidence builders retain the explicit durable states. [5]

### Cross-Repo References

The code/memory or fixture-repository boundaries above are established by package-local source.
No additional configured external or sibling-repository evidence is claimed.

No additional configured cross-repository evidence.
