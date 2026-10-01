# mcp/src/agents_remember/application/task_docs/task_unstarted_evidence.py

## Governing Overview

[Task-doc application overview](overview.md)

## Purpose

Proves whether a planning leaf is genuinely unstarted before destructive task-document discard.

## Code Commentary

### Logic

The enclosure commit census considers recorded code and memory-content outputs, including
their integrated counterparts. Ledger cache state is not execution evidence and cannot turn an
otherwise unstarted leaf into a started one. Other task, operation, seat, review, and contract
evidence remains part of the absence proof.

It censuses task steps, enclosure contracts, durable operation projections, seats, review artifacts, and commit evidence, then emits one stable recovery route when any execution authority exists.

It no longer emits a `door` fact. The closeout-door cut (commit `fad9808e`) removed both the
absent-door and present-door `_fact("door", ...)` entries when `contract.closeout_door` stopped
existing; a contract that still carries the front-matter key is not evidence that the leaf started.

### Conventions

Typed records and refusal payloads remain owned at the narrowest stable boundary. Callers consume
the public function or model instead of re-deriving its lower-level state machine.

### Invariants And Boundaries

- Absence must be proven across every canonical evidence plane; unreadable or ambiguous evidence counts as started/blocked and supplies an exact recovery route.
- Missing, unreadable, ambiguous, or conflicting authority fails loudly; this file does not add a
  fallback or compatibility shadow.

### Todos

None recorded.

## Evidence

### Docs References

The configured Domain Documentation registry is empty. No external documentation claim is made.

No external domain source is required to establish this repository-owned implementation.

### Repo-Internal References

The source file is the direct evidence for this unit; its governing overview records adjacent owners.

- The contract census observes actual code/memory and integrated output evidence, with no cache requirement. [1]
- The read-only census collects task, enclosure, operation, seat, artifact, and commit evidence before discard. [2]

### Cross-Repo References

No cross-repository source is allowed by the resolved settings, and this unit owns no external
protocol claim.

No meaningful cross-repository reference applies.
