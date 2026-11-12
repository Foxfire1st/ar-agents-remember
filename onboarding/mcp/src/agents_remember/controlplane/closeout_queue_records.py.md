# mcp/src/agents_remember/controlplane/closeout_queue_records.py

## Governing Overview

[control-plane overview](overview.md)

## Purpose

Defines the strict off-side build record used to publish one complete disposable closeout
projection.

## Code Commentary

### Logic

`CloseoutProjectionBuild` binds the sprint ref, exact source fingerprint and classification,
members, and build timestamp. The member list carries no item ceiling since 260913-LCA-L6.
Validation requires terminal source classifications to carry
no members and keeps the entire candidate self-contained for one later exact-current publication.

### Conventions

The record inherits the repository durable-record schema and bounds its text fields (`builtAt` is a
bounded string). Its `members` collection carries no item ceiling since 260913-LCA-L6, so how many
leaves a sprint declares never reaches this build guard.

### Invariants And Boundaries

- A build is scratch input, not the survival record for scheduling or lifecycle evidence.
- It contains no claim, commit, blocker, receipt, certification, or task-lock state.
- Prior projection rows are never inputs to a new build.

### Todos

None recorded.

## Evidence

### Docs References

No configured Domain Documentation source applies.

### Repo-Internal References

- The build record is complete off-side projection input. [1]

### Cross-Repo References

No meaningful cross-repository reference applies.

## 260821-CLIVE Final Projection Contract

`CloseoutProjectionBuild` replaces the former queue-owned WAL transaction vocabulary. One build is
a complete off-side projection candidate binding the sprint ref, canonical source fingerprint and
classification, members, and build timestamp. Terminal source classifications require an
empty member set. These records never own claims, commits, lifecycle transitions, certification,
blockers, or task locks; they are disposable publication input only. The member list was bounded to
256 at the time this section was written; 260913-LCA-L6 removed that ceiling, so only the
terminal-classification emptiness rule limits membership today.
