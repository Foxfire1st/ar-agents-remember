# mcp/src/agents_remember/memory/knowledge/read_owner_revisions.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

Observe one recorded prose owner revision against the memory object store, and report which fact it is
without ever turning the observation into a promotion.

## Code Commentary

### Logic

`OwnerRevisionResolver.observe` addresses exactly one object — the one whose identity the binding
already stored, spelled `<object_id>^{blob}` — through the shipped `run_git` runner, and returns an
`OwnerRevisionObservation` carrying the recorded identity, the path it was recorded at and a status.
`read_recorded_bytes` is the separate, explicit fetch used only when a caller has asked to compare a
written key against the recorded bytes, so a read page stays a facts packet rather than a document
dump. `_root_is_usable` decides the one non-object outcome: with no memory repository requested the
observation is `recorded_object_unavailable` rather than an exception, so "no repository" has a
declared answer instead of an accidental one. `render_owner_revision_basis` renders the recorded basis
(path, identity, state) for the failure direction, and `owner_revision_resolver_for` is the one
constructor.

### Invariants And Boundaries

- **No fallback to the working tree, to `HEAD`, to a branch name, or to a path.** A document that has
  moved on, been rewritten or been deleted is *not* re-read from disk and is not re-resolved from its
  path: the recorded revision is either in the object store or it is not, and the second case is a
  reported state rather than a lookup that quietly succeeds against different bytes.
- **No content is returned for the resolution itself**; the bytes are fetched separately and only
  when a caller has asked to compare a key against them.
- **The stored identity is preserved on every outcome**, including the failures — a missing revision
  is never a reason to retire a stored attribution.
- `OWNER_REVISION_STATES` declares the two states this module can report, so a case can assert it
  reports nothing outside the vocabulary the closure counts.
- **The difference from the shipped anchor reader is what they look at, not a second authority.**
  `read_anchors` resolves a recorded *path* inside a requested tree and reports whether that tree holds
  the recorded blob — the code side, where a path can have moved. Here the identity *is* the address,
  so there is no path to look up and nothing to relocate. The shipped literals are reused verbatim
  anyway, because the facts coincide exactly.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- **The declared states this observation can report, so "no memory repository was requested" has a declared answer.** [1]
- **The one fact about one recorded owner revision: what was addressed, and what answered.** [2]
- The one rendering of the recorded basis, used for the failure direction. [3]
- **The resolver: the one recorded object addressed, and the object-store observation with no path fallback.** [4]
- The separate byte fetch, used only when a caller compares a written key against the recorded revision. [5]
- The one constructor. [6]
- **The recorded owner revision this module resolves — repository, confined document path and the recorded object identity, referenced rather than minted.** [7]
- **The shipped identity the recorded revision is spelled in: the class that declares the one v1 source identity, and the module-level alias the same name carries — which is why this card names both sites.** [8]
- The shipped Git runner the object lookup goes through. [9]
- The shipped anchor reader whose refusal this module's no-fallback rule follows. [10]
- **The boundary case that proves a document present on disk at its recorded path still reports unavailable when the object store cannot produce the recorded revision.** [11]
- The unit case that asserts every recorded binding reports exactly one state from the declared vocabulary. [12]
- The unit case that asserts this module reports only declared states. [13]

### Cross-Repo References

No cross-repository behavior is implemented in this file. The object store it reads is the memory
repository's, and the recorded identity is the only address it ever uses.

No meaningful cross-repo references found.
