# mcp/tests/test_leaf_agent_archive.py

## Governing Overview

[overview](overview.md)

## Purpose

The focused proof suite for the closed-leaf agent archive. It exercises receipt selection and
settlement, the prepared-start closing mark, debt recovery through the existing observer, truthful
outcomes, bounded budgets and the archive-before-removal ordering.

## Code Commentary

### Logic

`LeafAgentArchiveTests` covers: the closing mark refusing a prepared start and settling a returned
creation; marked same-request replay refusing without creation and keeping debt; the mark covering
other prepared roles before host calls; stale publication keeping archive and only the exact leaf
mark refusing; current/history/retry selection preserving every artifact; predecessor debt surviving
host failure and advancing through automatic recovery; debt-write failure recovering from terminal
truth after restart; the existing observer archiving terminal debt without a person calling
recovery; empty, unreadable and conflicting records being named without host calls; host budget and
receipt settlement bounded at two scales; the automatic scan bounded and not starving the tail; a
preview or rejected admission archiving nobody; a repeated finalize reporting outcomes without
changing the task again; and admitted cleanup and abandon archiving before destructive outputs.

### Invariants And Boundaries

- The suite uses deterministic host substitution; it is not a real-agent witness.
- Each case asserts the archive behavior, not merely that a helper name exists.

## Evidence

- The closing mark refuses an unentered prepared start and settles a returned creation. [1]
- Same-request replay of a marked receipt refuses without creation and keeps debt. [2]
- The mark covers other prepared roles before host calls. [3]
- Stale publication keeps the archive and only the exact leaf mark refuses. [4]
- Current, history and retry selection preserve every artifact. [5]
- Predecessor debt survives host failure and automatic recovery advances it. [6]
- Debt-write failure recovers from terminal truth after restart. [7]
- The existing observer archives terminal debt without a person calling recovery. [8]
- Empty, unreadable and conflicting records are named without host calls. [9]
- Host budget and receipt settlement stay bounded at two scales. [10]
- The automatic scan is bounded and does not starve the tail. [11]
- A preview or rejected admission archives nobody. [12]
- A repeated finalize reports outcomes without changing the task again. [13]
- Admitted cleanup and abandon archive before destructive outputs. [14]
- A rejected terminal archive never calls the host or removes worktrees. [15]
