# mcp/src/agents_remember/application/knowledge_evidence.py

## Governing Overview

[application route overview](overview.md)

## Purpose

The application seam for the evidence-specific selection: one explicit context, one seed, one complete
page. It decides no authority and holds no durable state.

## Code Commentary

### Logic

`read_evidence_scope` is the narrow API a caller uses. It is the seventh application seam beside the
knowledge, snapshot, merge, export, read, facet and detection surfaces, and like them it admits a context,
delegates selection to the memory layer and returns the typed result unchanged.

Three boundaries this module owns, each because getting it wrong is a different kind of wrong:

1. **The read is read-only, and that is how a refusal persists nothing.** The connection is opened through
   the shipped read-only opener, so the strongest statement available to this operation is a `SELECT`. "A
   refused evidence read left the file byte-identical" is therefore a property of the handle rather than a
   rollback this code has to remember.
2. **The declared snapshot is verified before anything is selected.** `_read_inside_snapshot` requires the
   file to be bound to the requested namespace, to implement the schema generation the context declares, and
   to hold the declared logical dataset — the same three comparisons the recorded-scope read and the facet
   read make, for the same reason: a context describing another dataset is refused by name rather than
   answered from whatever bytes the path happens to hold.
3. **The artifact resolution is a read-time fact and never a rewrite.** A caller may declare a local
   artifact root so a recorded repository-relative path can be resolved against real bytes; the resolution
   is reported as its own state and the stored record is served exactly as it was written, whatever the
   resolution says.

`_absence_refusal`, `_snapshot_identity_refusal`, `_unusable_snapshot` and `_refused` are the seam's own
refusal shapes, so every failure leaves through the shipped `KnowledgeRefusal` vocabulary rather than as an
exception.

This operation does not touch the recorded-scope selection or the facet selection in any way: it does not
call either, shares no policy name with either, and appears in neither's response.

### Conventions

One function per operation, with the private helpers below it and `_OPERATION` naming the operation in every
refusal the seam itself builds. The module's `__all__` is the seam's public surface.

### Invariants And Boundaries

- **No authority is decided here.** The context is admitted by the caller's own boundary; this module
  verifies identity and selects, and never authenticates.
- **A refused read writes nothing**, by construction of the handle rather than by a compensating action.
- **The seam is thin on purpose**: selection logic belongs to the memory layer and the declared contract to
  the models; this file only admits, delegates and refuses.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The one operation this seam exposes. [1]
- The three identity comparisons made before anything is selected, and the refusals that name them. [2]
- The absent-selection refusal and the refusal builder the seam's own failures leave through. [3]
- The read-only open that makes "a refused read persists nothing" a property of the handle. [4]
- The selection this seam delegates to. [5]
- The case that asserts the read refuses a database that is not the selected snapshot. [6]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
