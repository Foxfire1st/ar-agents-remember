# mcp/tests/test_worktree_support_tests_1.py

## Governing Overview

[Nearest governing overview](overview.md)

Working candidate verification: source inspected at 2026-09-15T01:02 UTC against the uncommitted L9 candidate.
The commit fields identify the latest real commit touching this source; they do not identify a future commit for the working changes.

## Purpose

Exercises master/leaf start, attach, early binding refusal, queue projection, and leaf abandon
while preserving the parent series. The single retained scenario uses real temporary repositories
and task/worktree artifacts.

## Code Commentary

### Logic

The scenario creates a sprint with an atomic master and leaf, starts that leaf with external
memory, and checks the exact series/leaf branch and parent-contract relationships. It verifies the
leaf document's lifecycle/enclosure references and checks that reattach preserves them.

The early-closeout helper alters binding facts to prove refusal, then restores the task document.
The queue helper uses normalized code/memory messages and checks that the one member points to the
expected canonical leaf task. It no longer supplies a ledger message. Finally, abandon removes the
leaf enclosure while the parent series contract and its branch remain.

### Conventions

The card describes this retained method rather than restoring earlier split-family tests from
history. Shared support builds the repositories and typed inputs; the case checks public behavior
at its stated boundaries and does not stand in for every closeout route.

### Invariants And Boundaries

- Starting/attaching the leaf preserves canonical parent and document binding.
- Invalid binding is still refused before closeout work.
- Queue fixture intent uses only code and memory outputs.
- Abandoning the leaf must not remove the parent series contract or branch.

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

- The fixture queue and early refusal helpers retain typed inputs and exact bindings. [1]
- The retained lifecycle scenario preserves the parent through start/attach/abandon. [2]
- Shared closeout arguments normalize the two real content messages. [3]

### Cross-Repo References

The code/memory or fixture-repository boundaries above are established by package-local source.
No additional configured external or sibling-repository evidence is claimed.

No additional configured cross-repository evidence.

### Docs References

No external Domain Documentation source is configured for this internal route; task `260821-CLIVE-L1` and the cited repository source/tests govern this curation.

### Cross-Repo References

This file owns no ambient cross-repository authority. Any external-memory repository it reaches remains explicitly contract-addressed.
