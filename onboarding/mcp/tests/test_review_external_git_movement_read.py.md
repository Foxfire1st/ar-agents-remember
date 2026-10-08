# mcp/tests/test_review_external_git_movement_read.py

## Governing Overview

[mcp tests route overview](overview.md)

## Purpose

Raw Git movement is measured from retained commit evidence, with absent work-head proof kept unmeasured.

## Code Commentary

### Logic

An uncommitted candidate is a tree, not an observed branch head: the report remains not-measured, has no transition and fabricates no generation UUID. The live production read carries that measurement; historical comparisons carry no live movement. [5]

Commit-bound cases distinguish untouched, advanced and rewritten branches; source-history replacement, branch switch and unreadable channels retain distinct states. Validator forgeries use the real published value. [6] [7] [8] [14]

The shared TreeReceiptFixture constructs the enclosure and its exact comparison rather than the removed ReviewSyncFixture. [2]

### Invariants And Boundaries

- A tree cannot stand in for observed commit proof.
- Unavailable is neither movement nor agreement.

## Evidence

### Repo-Internal References


- Current shared enclosure fixture. [2]


- Uncommitted tree supplies no observed work-head proof. [5]


- Source replacement without fabricated UUID. [6]


- Leaving the declared branch is a switch. [7]


- Commit-bound ancestry states remain distinct. [8]


- Model rejects state contradictions. [14]


- Current managed-sync sibling cases. [25]


### Cross-Repo References

No cross-repository contract is established by this file.
