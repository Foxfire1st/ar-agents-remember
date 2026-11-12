# mcp/src/agents_remember/models/task_retirement.py

## Governing Overview

[models overview](overview.md)

## Purpose

The strict, bounded schema of the proof that a master was retired. A sprint keeps the proof on the plain row it leaves
for the retired master, and a master retired without a sprint keeps it in its own folder. A repeated retirement request
is compared with this proof.

## Code Commentary

### Logic

`MasterRetirementProof` (version `master-retirement/v1`, `extra="forbid"`) holds the master's reference and the archive
reference `0_archive/<folder>/task.json`, the trimmed nonblank reason, the retirement time (`retiredAt`, which must carry
a timezone), the removed `orchestrates` entries, the number of removed graph nodes, the removed edges
(`SprintExecutionEdge`), the edges the request affirmed, and the SHA-256 of the master's JSON and, when it exists, its
Markdown. `RetirementEdgeSelection` is one predecessor and successor pair, each a document reference or an endpoint.

### Conventions

- Every list is length-bounded, and the digests are lowercase hexadecimal of 64 characters.
- The docstring states the recovery rule: the sprint row is the durable owner, and the presence of the folder at its live
  or archive location says how far the retirement got.

### Invariants And Boundaries

- A proof with a blank reason or a time without a timezone is invalid.
- The proof is an audit record; its fields are classified as audit in `tasks/document_field_effects.py`.

## Evidence

- The proof records the master, the archive, the reason, the time, the removed linkage, the affirmed edges and the master's source digests. [1]

- The reason is trimmed and a blank one is refused; the time must carry a timezone. [2]
- An edge selection names one predecessor and one successor. [3]
