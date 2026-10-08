# mcp/src/agents_remember/worktrees/sync_transaction.py

## Governing Overview

[Nearest governing overview](overview.md)

## Purpose

Contract-addressed driver for resumable source synchronization.

## Code Commentary

### Logic

Input validation and stable journal routing precede mutation. Only merge-memory/skip-memory and continue/cancel are admitted. Dirty moving candidates are parked/restored under their own recorded stash. [1] [2]

Code settles before memory; _paired_code supplies its result for structural memory merge and validation. _continue_resolution selects the retained side and finishes staged merge or parked reapply before automatic progress resumes. Validator refusal leaves phase/staged merge intact and names repair. [4] [6] [9]

Structural report paths survive retained conflicts/conversion. No canonical row conflict, accepted decision list or reconcile-cycling state is authored. [5]

### Invariants And Boundaries

- Pinned journal/Git facts identify one transaction.
- Parked work must be restored or explicitly reported.
- Validator refusal is never committed around.

## Evidence

### Repo-Internal References


- Current input and journal routing. [1]


- Moving candidate park. [2]


- Validator refusal retains repair state. [4]


- Structural report journaling. [5]


- Settled code pairing. [6]


- Current continuation. [9]


- Real content conflict continuation scenario. [18]


### Cross-Repo References

No cross-repository contract is established by this file.
