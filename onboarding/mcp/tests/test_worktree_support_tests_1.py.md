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
leaf document's lifecycle ID and enclosure references. Reattach must preserve the enclosure references. Start also asserts inProgress on both the leaf document and exact master row; abandon later asserts abandoned on both. The retained lifecycleId is an enclosure binding, not session activity or heartbeat inference.

The early-closeout helper alters binding facts to prove refusal, then restores the task document.
The queue helper publishes fixture curator evidence, declares a closeout door with priority
judgment and typed admission, then reads the one member’s canonical leaf-task address. The
fixture pairs the memory base with a `Code-Commit` trailer and calls public first conversion
before evidence publication, asserting return 0. It removes the layout marker before abandon;
abandon then leaves the leaf code worktree and code branch absent while the parent series contract and branch remain.

### Conventions

The card describes this retained method rather than restoring earlier split-family tests from
history. Shared support builds temporary Git repositories. The test invokes manager start, attach and abandon, direct closeout entry, the conversion command function and queue tools.

### Invariants And Boundaries

- Starting/attaching the leaf preserves canonical parent and document binding.
- Invalid binding is still refused before closeout work.
- Queue fixture admission uses explicit priority judgment and a typed closeout-door declaration.
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

The earlier working-candidate inspection used L9. The references below describe the retained assertions in W8.
Source declarations and test assertions are distinguished from execution and acceptance evidence.

### Cross-Repo References

The code/memory or fixture-repository boundaries above are established by package-local source.
No additional configured external or sibling-repository evidence is claimed.

No additional configured cross-repository evidence.

### Docs References

No external Domain Documentation source is configured for this internal route; task `260821-CLIVE-L1` and the cited repository source/tests govern this curation.

### Cross-Repo References

This file owns no ambient cross-repository authority. Any external-memory repository it reaches remains explicitly contract-addressed.

### Current Source-Inspection References

- The fixture queue and early refusal helpers retain typed inputs and exact bindings. [1]

- The scenario verifies the start and reattach binding, the abandoned leaf states, removal of the leaf code worktree and branch, and preservation of the parent series contract and branch. [2]

- Shared closeout-input helpers are background support, not called by this retained scenario. [3]
