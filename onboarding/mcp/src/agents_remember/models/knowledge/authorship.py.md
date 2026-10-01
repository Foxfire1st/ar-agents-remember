# mcp/src/agents_remember/models/knowledge/authorship.py

## Governing Overview

[models route overview](../overview.md)

## Purpose

The provenance envelope stored with every authored knowledge row — who authored a value, under which authority,
in which operation, at which recorded time, and from which explicit source references.

## Code Commentary

### Logic

`Authorship` carries `actor_ref` and `authorization_ref` (nonblank, bounded by `REFERENCE_MAX_LENGTH`), a real
`UUID` `operation_id`, a `recorded_at` string, and `origin_refs: tuple[str, ...] = ()`.

Three validators carry the rules: `_require_nonblank_reference` strips and refuses a blank actor or authorization
reference; `_require_nonblank_origins` strips each origin, refuses a blank entry and refuses a repeated origin
within one envelope; `_require_normalized_utc` parses `recorded_at` with `datetime.fromisoformat`, refuses a naive
instant, converts to UTC and refuses any spelling that is not already the canonical `...+00:00` form.

`ACCEPTED_STATE`, `PROPOSED_STATE`, `Authorship` and `KnowledgeState` are re-exported through `__all__` so a
consumer of the envelope also names the origin states it is compared against.

### Conventions

`operation_id` is typed as a real `UUID` rather than a pattern-constrained string: Pydantic normalizes the
accepted spellings to one value, and the canonical stored text is derived at the storage boundary rather than
validated as text here. `recorded_at` is required to be normalized UTC because a naive or offset-bearing spelling
would make two equal instants compare as different stored text.

### Invariants And Boundaries

- Authorship is **authored input**: the store never manufactures an author, and importing a payload preserves the
  original envelope instead of replacing it with the importer.
- The admitted application assigns `operation_id` and `recorded_at`
  (`application.knowledge.write_authorship`), so a caller cannot back-date a record or claim an operation that
  never happened.
- An empty `origin_refs` tuple means no source was declared — a fact about the record, not permission to infer one.
- This envelope is the shared provenance vocabulary the read/diff contributor is declared to consume; it is not
  the Git commit attribution owner (`kernel/memory_attribution.py` remains that owner, and this leaf copied
  nothing from it).

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The provenance envelope, its three validators and the normalized-UTC rule. [1]
- The application assigns the operation identity and the recorded instant instead of accepting them. [2]
- The envelope is stored as a canonical JSON typed column. [3]
- The envelope is part of the sealed revision payload, so provenance is inside the digest. [4]
- Git commit attribution stays with its existing owner; this leaf read it for context and copied nothing. [5]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
