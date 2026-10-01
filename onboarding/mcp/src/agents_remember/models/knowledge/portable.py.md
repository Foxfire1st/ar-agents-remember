# mcp/src/agents_remember/models/knowledge/portable.py

## Governing Overview

[models route overview](../overview.md)

## Purpose

**The portable export/import vocabulary, and the boundary it draws around external input.**

Three splits carry this module's contract, and each exists because collapsing it would make a statement the
code cannot support:

- **A request versus an admitted identity.** `ExportRequest` carries the exact logical identity the caller
  admitted for the database it names. Storage re-reads it before encoding, so an export cannot silently
  describe a dataset that moved between the caller's check and the read.
- **A validated artifact versus a published dataset.** `PortableValidation` reports what was **checked**;
  `ImportResult` reports what now **exists**. Neither can carry a semantic judgement about whether the
  knowledge is correct, and neither can grant acceptance.
- **A staging fact versus a destination fact.** An import can validate perfectly and still not publish, so
  the result reports a verified logical identity separately from the state of the destination it did or did
  not reach.

## Code Commentary

### Logic

`ExportFormat` / `EXPORT_FORMAT` declare the one format member this package writes and reads
(`ar-knowledge-export/v1`). It is declared **here** rather than in the encoder so a caller can name the
format without importing the storage module that implements it — the same direction rule the rest of
`models.knowledge` follows.

`ExportRequest(database_path, expected_identity)` — `expected_identity` is **required**: an export is
addressed at *a dataset*, not at whatever a path currently holds, and the identity is what makes the two
the same object.

`ImportRequest(artifact, destination_path, expected_destination=None, expected_repository_id=None)` —
`expected_destination` is a closed choice in effect: the exact identity the caller observed, or `None` for
"the destination is expected to be absent". **There is no third mode.** `expected_repository_id` is
optional and only narrows; it rests on the same fact the repository table already declares (a dataset is
bound to exactly one namespace), so it admits nothing — it refuses an artifact that is internally valid but
belongs elsewhere.

`PortableValidation(state, ...)` — `row_counts` covers every canonical table including the empty ones,
because "present and empty" is the fact that separates a complete export from one that dropped a
collection. Its validator enforces the two-state contract: a `refused` validation must carry its refusal
and **reports no logical identity** (a refused artifact established none), while a `validated` one carries
no refusal and must name the namespace it is bound to and the digest its records produce.

`ExportResult` — the artifact is carried as **text**, not written, because the encoder has no filesystem
side effect at all; `row_counts` and the result's `notes` (`PORTABLE_NOTES`) travel with it. A `refused`
export carries its refusal and reports no artifact and no identity; an export that was produced carries no
refusal and must report the artifact, its format and the identity it seals.

`ImportResult(state, verified_identity, destination_identity, publication, ...)` — `state` is `installed`,
`no_change` (the destination already held the artifact's exact logical dataset, so no bytes were rewritten)
or `refused`. `verified_identity` is carried **independently of the state**, because a validated artifact
that failed to publish has an identity worth naming, and `publication` is `None` in that case rather than a
state. The validator enforces the rest: a refused import reports no destination identity and no publication
state, and an import that was not refused must name both identities **and** they must agree on the logical
digest.

### Conventions

- Models extend `KnowledgeModel` and use the shared `SHA256_PATTERN` and `PATH_MAX_LENGTH` from
  `models/knowledge/base.py`, so a malformed digest or an over-long destination ref is refused at
  construction rather than at use.
- Every consistency rule is an `@model_validator(mode="after")` — the same shape the rest of the knowledge
  vocabulary uses, so an internally inconsistent outcome is caught at the returning call site.
- The three-argument/three-state shapes are named for the caller's decision, not for the storage step that
  produced them.

### Invariants And Boundaries

- **Nothing here can carry a verdict or grant authority.** A row whose `state_at_origin` says `accepted`
  crosses as that stored value; no field in this module can promote it, and none can record whether the
  imported knowledge is *correct*.
- **A refused artifact has no identity to report.** That is why `PortableValidation` refuses a
  `logical_digest` on a refused validation rather than leaving the field open.
- **A destination that was reached must hold exactly what was verified.** `ImportResult` refuses to
  construct when `verified_identity.logical_digest != destination_identity.logical_digest`.
- **Boundary.** This module owns the wire vocabulary and its consistency rules. It holds no SQL, no file
  access, no Git resolution and no authorization decision; the reader/encoder live in
  `memory/knowledge/export_portable.py` and the operation in `memory/knowledge/export_import.py`.
- **Not re-exported from the package root.** `models/knowledge/__init__.py` does not import this module, so
  a consumer reaches it as `agents_remember.models.knowledge.portable`; the merge vocabulary follows the
  same convention, and the handoff names the full path for the next leaves.

### Todos

None recorded for this slice.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The three splits that carry this module's contract, in the form a consumer reads them. [1]
- The one portable format member, declared here so a caller can name it without importing storage. [2]
- **The export request whose admitted identity is required rather than optional.** [3]
- **The import request: the closed two-mode destination admission, with no third mode, and the namespace narrowing that admits nothing.** [4]
- **The validation report: all tables counted including the empty ones, and no identity for a refused artifact.** [5]
- **The export result: the artifact carried as text because the encoder has no filesystem side effect.** [6]
- **The import result: the verified identity carried independently of the state, and the two must agree.** [7]
- The shared pattern and length constants every field is validated against, and the model base. [8]
- The identity shape both requests and both results carry. [9]
- The refusal shape a refused validation or result carries. [10]
- The operation that consumes this vocabulary. [11]
- The reader, validator and encoder this vocabulary describes. [12]
- The nodes that hold the round trip, the preservation rule and the destination behaviour to this vocabulary. [13]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
