# `mcp/src/agents_remember/models/lifecycles/operation_projection.py`

## Governing Overview

[lifecycles overview](overview.md)

## Purpose

Revision-bound public lifecycle-operation projection contracts (CCR-R18): the versioned state
matrix and the atomic public envelope `LifecycleOperationProjection` that one exact
operation kind, public generation, monotonic journal revision, and candidate/plan binding project.
Coherent result, approval, recommendation and legal-control observations bind that envelope or are omitted. An incoherent composition returns a bounded typed finding instead of splicing individually valid facts.

## Code Commentary

### Logic

Running, direct-landing, and input-required phase sets contain no ledger publication phase.
An interrupted memory commit remains representable under `memory-commit`; cache regeneration
does not create a retained Git step. The exhaustiveness check continues to bind these sets to
the canonical phase vocabulary.

`LifecycleProjectionStateRule` holds the per-kind state matrix; `classify_result`
and `validate_projection_state` check a record's cells against it, and
`validate_state_matrix_is_exhaustive` proves the matrix covers the full kind/phase/status
vocabulary. `LifecycleProjectionIdentity` carries the public identity (kind, generation,
record revision, fingerprint, contract binding); `LifecycleProjectionComponentBindings`
holds the coherent component set; envelope validators refuse unreadable projections that advertise
authority, envelopes whose components disagree with the identity, and task addresses that leave the
admitted contract scope.

### Conventions

The envelope is a strict response model with camel-case wire names and forbids extra fields.
Nested observations bind the envelope identity or are omitted — never free-standing.

### Invariants And Boundaries

- The public envelope never carries an operation key, worker PID, or lease.
- A projection is internally valid only when identity, components, and task addresses agree.
- CCR-R15: the envelope carries `meaningfulRevision`, the durable meaningful-state cursor
  of the exact journal snapshot it projects (adapters populate it for record-bound envelopes;
  unreadable journal refusals carry no record and omit it).

### Todos

None.

### CCR private preparation boundary

The phase matrix can represent the retained `recovering-private-preparation` state for queued, running and input-required envelopes. The vocabulary is for readable observations, including records left by earlier builds.

- The current `_RUNNING_PHASES` boundary implements the preparation contract above. [1]
- The current `_INPUT_REQUIRED_PHASES` boundary implements the preparation contract above. [2]

- The public matrix maps status, result and action cells. [3]


## Evidence

### Docs References

No configured external Domain Documentation source governs these internal wire contracts.

No configured external source governs this strict projection vocabulary.

### Repo-Internal References

- Running, direct, and input-required phase sets use the canonical code/memory-only publication vocabulary. [4]

- The atomic public envelope and its per-kind state matrix. [5]

- CCR-R15 meaningful-state cursor on the envelope. [6]

- Projection component bindings, coherent state and recommendation use the same generation identity. [7]

- The durable record whose meaningful revision the envelope projects. [8]
- The wait vocabulary that consumes the cursor. [9]

### Cross-Repo References

No cross-repository projection contract is defined here.


- The envelope is a same-repository task-lifecycle wire contract. [10]


## 260831-CCR-L15 Meaningful Revision On The Envelope

The envelope gained the optional `meaningfulRevision` cursor (int | None, ge=1, default
None): adapters populate it from the exact durable record's meaningful revision for record-bound
envelopes, so a status-change waiter compares the cursor it waited on against the cursor of the
envelope it receives; unreadable journal refusals carry no record and omit the field.

## Controls for the current route

Historical closeout and integration projections retain recorded evidence for audit. The runtime projector removes execution advice and legal controls. Typed replacement guidance belongs to the addressed control refusal. Available direct controls come from the current direct generation.

- The runtime producer dispatches historical kinds to audit projection. Control of a retired kind refuses with the matching synchronous replacement. [11]
