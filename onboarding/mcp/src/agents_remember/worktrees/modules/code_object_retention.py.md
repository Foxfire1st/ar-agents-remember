# mcp/src/agents_remember/worktrees/modules/code_object_retention.py

## Governing Overview

[worktrees/modules route overview](overview.md)

## Purpose

Custody measurement and explicit release of pins earlier comparison freezes created.

## Code Commentary

### Logic

RetainedCodeObject names historical ref/commit/tree/base. No operation creates one. code_object_custody checks only named durable tips and recorded landed commits, not disposable branch sweeps or ancestry. [5] [10]

Observation distinguishes absent from retained/committed history. Release measures custody, checks the current ref still names its recorded commit, deletes with expected-value update-ref and returns the release record. Absent refs converge; moved refs refuse. [11] [13]

Real scratch-repository cases drive release and snapshot deletion owners with exact ref/byte guards. Old deterministic pin-creation and canonical-generation reopen cases do not establish current behavior. [22] [23]

### Invariants And Boundaries

- Custody never releases automatically.
- The caller owns policy, record publication and lifetime.
- Release cannot delete a moved ref.

## Evidence

### Repo-Internal References


- Complete retained pin identity. [5]


- Named-tip custody only. [10]


- Absence is a distinct observation. [11]


- Exact-ref release and absence convergence. [13]


- Real release guards and named custody. [22]


- Exact-byte snapshot deletion, with mismatch refusal. [23]


### Cross-Repo References

No cross-repository contract is established by this file.
