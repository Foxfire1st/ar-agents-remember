# mcp/src/agents_remember/models/knowledge/digest.py

## Governing Overview

[models route overview](../overview.md)

## Purpose

The one owner of what a revision's identity seals: the canonical payload mappings, their SHA-256 digests, and the
sealing operations that turn an authored aggregate into a stored one. There are **two** payloads — the invariant
one and the family one — and each has its own version constant so a digest can never be mistaken for the other
object's identity.

## Code Commentary

### Logic

`REVISION_PAYLOAD_VERSION = "invariant-revision-payload/v1"` and
`FAMILY_REVISION_PAYLOAD_VERSION = "family-revision-payload/v1"` are recorded in their payloads rather than
inferred from which fields are present, so a changed sealed field set is a different identity computation.

`canonical_revision_payload(revision)` returns the exact mapping the digest covers: `payload_version`,
`repository_id`, `invariant_id`, `revision_id`, `display_version`, `statement`, `applicability`, the ordered
`conditions` and `exclusions` lists, `state_at_origin`, `acceptance_ref`, the JSON-mode `provenance` envelope and
`sorted(predecessors)`. The digest field is deliberately absent, because a digest cannot cover itself.

`canonical_family_revision_payload(revision)` seals the family aggregate's own field set: `payload_version`,
`repository_id`, `family_id`, `revision_id`, `display_version`, `joint_guarantee`, `state_at_origin`,
`acceptance_ref`, `provenance` and `sorted(predecessors)`. The only structural differences from the invariant
payload are the version string, the object identity field and the authored text fields — `predecessors` is inside
**both**, which is what makes the two graphs' sealing behaviour identical without either one restating it.

`revision_payload_digest` / `family_revision_payload_digest` hash those mappings through
`kernel.canonical_json.sha256_digest`, and `sealed_revision` / `sealed_family_revision` return
`model_copy(update={"payload_digest": ...})`.

### Conventions

The predecessor set enters the digest **sorted**, because the authored set is what is being sealed and the order a
caller happened to write it in is not authored information. Clause order inside `conditions`/`exclusions` is kept,
because that order is the author's.

### Invariants And Boundaries

- The predecessor set is inside both seals, so an edge cannot be edited behind an existing sealed revision:
  adding or removing one changes the aggregate the revision identity stands for. `memory/knowledge/records.py`
  re-derives the digest on read — over the stored row **plus the stored predecessor edges** — and refuses a row
  whose stored seal no longer holds.
- The store recomputes rather than trusting a supplied digest: neither `RevisionDraft` nor
  `FamilyRevisionDraft` has a digest field at all.
- Changing a sealed field set means a new payload version, never a silent reinterpretation of stored digests; the
  two constants are separate for exactly that reason.
- **These functions compute; they do not read or write.** The read-path verification and the storage boundary live
  in `records.py`, and a rule that belongs to storage must not migrate here.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The exact invariant sealed mapping, including the sorted predecessor set and the excluded digest. [1]
- The digest computation and the single sealing operation for the invariant payload. [2]
- The exact family sealed mapping, which seals the joint guarantee and the same sorted predecessor set. [3]
- The recorded payload versions, separate so one payload's digest cannot be read as the other's. [4]
- The read path re-derives both seals and refuses a rewritten row or edge. [5]
- The store seals the draft rather than accepting a caller-supplied digest, on both aggregates. [6]
- The node that proves each sealed field is load-bearing rather than incidentally covered. [7]
- The canonical encoder the digest is computed through. [8]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
