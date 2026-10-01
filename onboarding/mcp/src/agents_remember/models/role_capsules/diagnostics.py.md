# mcp/src/agents_remember/models/role_capsules/diagnostics.py

## Governing Overview

[models overview](../overview.md)

## Purpose

The **explanation half** of the frozen role-capsule contract: what was considered during a
compilation and why, kept beside — not inside — the content half. A consumer that only
delivers a capsule never has to construct any of it; a consumer that has to explain a refusal,
or audit which source revision a block came from, reads exactly these shapes.

## Code Commentary

### Logic

cit:([`CapsuleSourceRecord`], mcp/src/agents_remember/models/role_capsules/diagnostics.py:38-58) is one considered source with its root, path,
identity, revision, and whether it was selected.
cit:([`CapsuleConflictRecord`], mcp/src/agents_remember/models/role_capsules/diagnostics.py:59-72) is one structured contradiction row.
cit:([`CapsuleRejection`], mcp/src/agents_remember/models/role_capsules/diagnostics.py:73-96) carries a refusal's status, detail, and remedy with its own
cit:([`render`], mcp/src/agents_remember/models/role_capsules/diagnostics.py:90-94) one-line projection, and
cit:([`CapsuleRefusalOptions`], mcp/src/agents_remember/models/role_capsules/diagnostics.py:97-104) carries the options a stopped conflict can offer.

cit:([`CapsuleManifest`], mcp/src/agents_remember/models/role_capsules/diagnostics.py:105-217) is the aggregate: who the seat was, the operation,
which sources were admitted and which were composed, the digest, the records, and the
rejection when there is one. cit:([`for_refusal`], mcp/src/agents_remember/models/role_capsules/diagnostics.py:139-173) builds the refusal-shaped
variant and cit:([`summary`], mcp/src/agents_remember/models/role_capsules/diagnostics.py:174-210) is its bounded serializable projection.

**The structural rule this module exists for:** nothing here is an input to
`CapsuleCapsule.semantic_digest`. It carries the ephemeral facts a digest must ignore —
sources considered and not selected, collapsed duplicates, refusal text, and run-specific
provenance. Keeping the two halves in separate modules is the structural version of that rule,
which is why a "helpful" import of a diagnostic field into the digest is a contract violation
rather than a refactor.

### Conventions

Every shape is a frozen slotted dataclass whose `__post_init__` refuses a blank required field.
A refusal is represented as data here (never as a raised shape), so a caller can render and
report it without re-raising.

### Invariants And Boundaries

- **Diagnostics never feed the semantic digest.** `semantic_digest` lives on the content half
  precisely because it must be computable without any of this.
- A refusal and a success share the manifest shape; `result is None`-style branching belongs to
  the application outcome, not here.
- A conflict row is structured (kind plus the identities involved), not a formatted string, so
  a caller can branch on it.
- `summary()` is a bounded projection for transport. Do not add unbounded source content to it.

### Todos

None recorded.

## Evidence

### Docs References

No external or domain documentation is configured for this memory root
(`system/sources.md` has no entries), so no external documentation claim is made.

No relevant documentation found after checking live sources.

### Repo-Internal References

- The content half whose digest must stay independent of these shapes. [1]
- The builder that fills the success-shaped manifest, and the two refusal-shaped builders. [2]
- The digest document that must not reference any field of this module. [3]
- The application outcome that pairs a capsule or a refusal with this manifest. [4]
- The conflict kind vocabulary these rows are expressed in. [5]

### Cross-Repo References

No sibling-repository contract consumes these shapes.

No meaningful cross-repo references found.
