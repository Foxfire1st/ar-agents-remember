# mcp/src/agents_remember/application/knowledge_snapshot.py

## Governing Overview

[application route overview](overview.md)

## Purpose

**The second composition seam of the knowledge substrate**: the candidate lifecycle (create, clone, open,
disposal authorization) and snapshot publication, as one composed operation beside the single candidate write in
`application/knowledge.py`. Both seams exist so each entry point reads as one intent; nothing here decides
authority and nothing here holds durable state.

It admits a candidate directory plus an explicit resolution into typed values, delegates to
`memory.knowledge`, and returns the typed result **unchanged**. Storage ranks below application, so a lower owner
— the worktree or memory-quality package that captures a published database — receives
`models.knowledge` values and never an import of this module or of the store.

Two non-claims are load-bearing and were deliberate in the ruled design:

- **No Git commit.** The published snapshot is a closed *file*; capturing it into a memory tree is the existing
  candidate-tree owner's operation. This module creates no commit, moves no ref and writes no ledger row.
- **No IAS landing.** The writable candidate belongs to the experimental master; a landing on the parent sprint is
  a separate decision and is not reachable from anything here.

## Code Commentary

### Logic

Nine thin entry points, each a rename of one storage operation onto admitted inputs:

- `admitted_candidate_destination(directory, repository, resolution)` is the constructor the admitted-authority
  path calls after its own checks. It confers no authority by itself; it exists so the lifecycle and publication
  operations receive a typed handle rather than a bare path, which is what keeps a deserialized request from
  becoming admitted input.
- `candidate_write_destination(candidate, authorship)` addresses the single-record and batch write operations at
  this candidate's database. The path is **derived from the layout** rather than passed a second time, so a caller
  cannot write into one database and publish another; the `authorship` envelope is the admitted provenance for the
  writes, and the receipt binds the candidate, not the writer.
- `create_knowledge_candidate` / `clone_knowledge_candidate` / `open_knowledge_candidate` delegate to
  `create_candidate` / `clone_candidate` / `open_candidate`.
- `authorize_knowledge_candidate_disposal` delegates to `authorize_candidate_disposal` and returns the verdict.
- `publish_knowledge_snapshot(candidate, request)` freezes and installs one candidate's point;
  `publish_prepared_knowledge_snapshot(prepared, request)` installs an already-frozen stage through the **same**
  publication contract, so a caller that produced a validated closed database (a merged result, an import, a
  restored artifact) reaches the destination on the same path.
- `knowledge_publication_state(candidate, published_path)` compares a live candidate with the closed snapshot a
  read is about to answer from, and returns the measurement.

### Conventions

- Every function is a pure delegation with a docstring that states the boundary it does not cross; the module
  keeps no state, opens nothing itself and closes nothing.
- The seam returns storage's typed values unchanged, so a caller can branch on `state`/`refusal` without an
  application-level wrapper type — the same shape `application/knowledge.py` uses.
- The docstrings state the two non-claims (no commit, no IAS landing) rather than leaving them to be inferred.

### Invariants And Boundaries

- **Path derivation is one-way.** `candidate_write_destination` derives the database path from the admitted
  candidate, so write and publish cannot name different files.
- **No authority is conferred here.** The admitted destination is a shape, not a grant; approval, acceptance and
  task status are not representable in anything this module returns.
- **No durable state and no Git.** The module creates no commit, moves no ref and writes no ledger row; capturing
  a published snapshot belongs to the candidate-tree owner.
- **Storage ranks below application.** No lower-ranked package may import this module; a lower owner receives
  `models.knowledge` values.
- **The seam is not yet wired to a tool.** Like `application/knowledge.py`, this module has no non-test importer
  in `mcp/src` as of this leaf; transport wiring remains an explicit later extension.

### Todos

None recorded for this slice. The unwired status is a carried limitation of the increment, not a defect this leaf
left open: wiring a public tool name is a later extension by the packet's own statement.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The admitted-destination constructor that confers no authority by itself. [1]
- The write destination derived from the candidate layout rather than passed twice. [2]
- The three lifecycle delegations. [3]
- The disposal-authorization delegation. [4]
- The two publication entry points that share one contract. [5]
- The read-side publication gate. [6]
- The candidate lifecycle this seam delegates to. [7]
- The publication half this seam delegates to. [8]
- The read-side comparison this seam exposes. [9]
- The sibling seam this module sits beside, and the provenance envelope it reuses. [10]
- The vocabulary these entry points take and return. [11]
- The composed-path support module that drives this seam end to end. [12]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
