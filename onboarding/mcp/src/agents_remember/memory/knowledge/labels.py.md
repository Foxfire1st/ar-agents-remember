# mcp/src/agents_remember/memory/knowledge/labels.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**Friendly-label edits on the two identity rows, and the concurrency guard they carry.** A display label is the
one field of an identity row that may legitimately change: everything that makes the identity an identity — its
ID, its namespace and, for a revision, its sealed payload — is immutable, so a label edit is not a rewrite of the
subject but a change to how a reader displays it. Because it is the one mutable field, it is also the one place a
stored row can differ from the copy a caller read, which is why **every label edit names the exact row it
expects**.

Both identity rows are shaped the same way (identity columns, a label, an authorship envelope), so the guard, the
update and the result shape live here once for both concepts.

## Code Commentary

### Logic

- Each edit has **two entry points**, and the split is the point:
  - `set_invariant_label` / `set_family_label` are the *operations*: they check scope, take the candidate's
    exclusive lock, run `store.within_immediate` with a `SqliteFailureContext` naming the operation, table and
    record, and return the typed `SetInvariantLabelResult`/`SetFamilyLabelResult`.
  - `apply_invariant_label` / `apply_family_label` are the *in-transaction steps*: they raise a typed refusal for
    the caller to map or roll back, and they return **whether a statement ran**.
- The guard order inside an apply step is what makes it correct: read the row (**unknown identity** refuses),
  compare `expected_row_digest` against the stored `row_digest` (**stale caller** refuses, naming expected and
  observed), and only then compare the requested label with the stored one. A requested label that already
  matches returns `False` **before** the UPDATE, so no statement runs and no receipt entry is claimed.
- The digest the caller names is the same value `get_invariant`/`get_family` expose as `row_digest`, so an
  expectation is carried straight from a read instead of being recomputed by a second rule.
- The result models enforce their own consistency: a `labeled` result must carry the label it stored and no
  refusal; a `refused` result must carry its refusal. `_apply_*_label` therefore constructs only the success
  shape, and the two `_*_label_refusal` helpers only the failure shape.

### Conventions

- The two concepts share one shape deliberately: the guard, the UPDATE and the result construction read
  identically for both, and each function names its own table and operation in the refusal it raises.
- The store exposes `set_invariant_label` as a thin method delegating here
  (`OpenedKnowledgeStore.set_invariant_label`), so a caller holding an opened store does not need a second
  import; the family twin is reached through the application seam's `labels.set_family_label`.
- `__all__` lists exactly the four public names.
- **The batch path shares `apply_*` and does not share the operations.** A batch command calls `apply_*` inside
  the batch's own transaction, and uses `False` to omit a receipt row for an edit that wrote nothing.

### Invariants And Boundaries

- **A label edit is not an identity edit.** Nothing here can change an ID, a namespace, a provenance envelope or
  a revision payload; the UPDATE touches `display_label` only.
- **The row digest is the concurrency guard.** A caller that read a row and lost the race is told
  (`stale_precondition`) rather than obeyed — the stored row is left byte-identical.
- **`False` means "no statement ran".** The return value is a receipt fact, not a success flag: a caller that
  treats `False` as failure would be wrong, and a caller that reports a write for it would overstate the receipt.
- **Both entry points are needed for the guard to be load-bearing.** The batch path carries an independent copy
  of the expectation rule in `batch_preconditions._require_identity`, so a case that only drives the batch would
  stay green with this CAS deleted — which is why the standalone operations have their own module of evidence.
- **Boundary.** This module owns the two label edits and their guard. Who may edit (admission) is the
  application seam's, and when a batch may edit is the precondition module's.

### Todos

None recorded for this slice. The two label edits are the only identity edits the store exposes by design; a
future editable identity field would need its own guard here rather than widening the UPDATE.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The invariant label operation: scope, lock, one transaction, typed result. [1]
- The in-transaction step: unknown identity, stale digest, then the no-op return before the UPDATE. [2]
- The family twins, shaped identically. [3]
- The two result constructors, each producing only the shape its model permits. [4]
- The invariant-label result and its consistency validator. [5]
- The family-label result and its consistency validator. [6]
- The request models, each naming the row the caller read. [7]
- The stale-caller refusal wording, shared with the removals. [8]
- The batch command that shares these apply steps and omits a receipt row when nothing was written. [9]
- The batch's own copy of the expectation rule, which is why the standalone path needs its own evidence. [10]
- The standalone operations' entry points in the composition seam. [11]
- The invariant-label result and its consistency validator. [12]
- The family-label result and its consistency validator. [13]
- The request models, each naming the row the caller read. [14]
- The stale-caller refusal wording, shared with the removals. [15]
- The batch command that shares these apply steps and omits a receipt row when nothing was written. [16]
- The batch's own copy of the expectation rule, which is why the standalone path needs its own evidence. [17]
- The standalone operations' entry points in the composition seam. [18]
- The store method that delegates here. [19]
- The six nodes that drive the standalone entry points, including the stale-expectation case the batch path cannot cover. [20]
- The node that pins the no-op label edit inside a mixed batch. [21]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
