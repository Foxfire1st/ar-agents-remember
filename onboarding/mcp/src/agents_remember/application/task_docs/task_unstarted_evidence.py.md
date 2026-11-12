# mcp/src/agents_remember/application/task_docs/task_unstarted_evidence.py

## Governing Overview

[Task-doc application overview](overview.md)

## Purpose

Proves whether a planning leaf is genuinely unstarted before destructive task-document discard.

## Code Commentary

### Logic

The enclosure commit census considers recorded code and memory-content outputs, including
their integrated counterparts. Ledger cache state is not execution evidence and cannot turn an
otherwise unstarted leaf into a started one. Canonical task fields/steps, locator/manifest/journal and contract evidence remain part of the
absence proof. Removed seat and operator-inbox stores are not read.

The A6 owner reads exact binding-addressed task status/steps and execution registrations, the
independent lifecycle locator and its manifest/journals, enclosure contract and recorded code/
memory-content commits. It does not enumerate a reports tree or terminal-seat catalog. A present
terminal archive is addressed through its locator; unreadable canonical authority is ambiguous,
not proof of absence. Recovery follows the actual terminal, operation, contract, locator or task
registration state.

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

- Canonical task, locator/manifest/journal, contract and commit evidence govern the unstarted proof; removed seat and report scans are absent. [1]
