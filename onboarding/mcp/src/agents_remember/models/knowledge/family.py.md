# mcp/src/agents_remember/models/knowledge/family.py

## Governing Overview
[models route overview](../overview.md)

## Purpose

Family identity and the immutable family revision aggregate — the vocabulary half of the family graph.
A family is a stable subject whose revision carries an authored **joint guarantee**: a statement about
a set of invariant revisions that hold together. The guarantee is the family's own text and is never
assembled from its members; a member keeps its exact own obligation, and the two are separate authored
claims a reader must not derive from one another.

This module defines values, not rows. It performs no I/O, owns no table and raises no refusal: the
storage owner is `memory/knowledge/families.py`.

## Code Commentary
### Logic

The draft/stored value split keeps a caller-supplied payload digest out of revision authoring. The decoded revision carries its seal and checked sorted predecessor set. Construction refuses duplicate predecessors and self-predecessors. The selected tree's derived state stays outside the authored payload seal.

### Invariants And Boundaries

A changed guarantee names a successor revision; an earlier membership keeps the exact revision it cites. This module performs no I/O. `memory/knowledge/families.py` only reads values from the memory tree's derived index. Canonical family creation, revision encoding and draft-sealing APIs are retired; fixture writers are not production successors.

### Todos

None recorded.

### Logic

- `FamilyDraft` is the identity a caller proposes — `family_id`, `display_label` and the label's own
  `Authorship` — with a non-blank label validator.
- `FamilyIdentity` adds `repository_id` and the expected `row_digest`, so a stored identity can be
  compared against what a caller remembered.
- `FamilyRevisionDraft` carries the family and revision identities, display version, authored guarantee, predecessors and provenance. It includes the derived `state` and has no payload digest field.
- `FamilyRevision` adds `repository_id` and the `payload_digest`; `StoredFamilyRevision` carries the
  decoded `predecessors_sorted` set alongside the revision.
- The predecessor validators refuse duplicates and an edge from a revision to itself.

### Conventions

- Separating `FamilyRevisionDraft` from `FamilyRevision` is what keeps the seal out of a caller's
  hands, exactly as `RevisionDraft`/`InvariantRevision` do on the invariant side.

- Length bounds come from `base.py` (`LABEL_MAX_LENGTH`, `PROSE_MAX_LENGTH`, `REFERENCE_MAX_LENGTH`)
  rather than being re-spelled here, so both revision aggregates share one set of limits.

### Invariants And Boundaries

- **Immutability is structural, not advisory.** The `payload_digest` seals the whole authored payload
  *including the sorted predecessor set*, so a stored family revision identifies exactly one authored
  aggregate: changing the guarantee means authoring a separately identified successor, and an earlier
  membership citing the original still resolves the original text.
- **The guarantee is never derived from members.** Nothing in this vocabulary has a field a reader
  could fill from a member's obligation.

- **Boundary.** This module declares no operation, no table, no SQL and no refusal code; it must not
  grow a validation rule whose only enforcement point is storage, because both revision aggregates are
  validated where they are authored.
- **Not this module's job.** The relation vocabulary (`graph.py`), the payload-digest computation
  (`digest.py`) and the storage operations (`memory/knowledge/families.py`).

## Evidence
### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The separation between the family guarantee and its members' obligations. [1]
- The identity draft and its stored, digest-carrying form. [2]








The requirement this vocabulary's first delivered slice belongs to: requirement packet `KS-R02@v1`, which lives in the coordination root, outside both the code and the memory repository, so the citation grammar cannot address it.

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.

- The sealed revision and its stored read shape. [4]
- The production reader retrieves family identities and exact sealed revisions from the derived index; it writes nothing. [8]

- The payload this revision's digest seals, including the sorted predecessor set. [6]
- The retained family revision decoder verifies the sealed aggregate and sorted predecessors. [7]

- The declared `family` and `family_revision` tables these values map onto. [9]
- The authored aggregate before sealing, with its digest deliberately absent. [3]
