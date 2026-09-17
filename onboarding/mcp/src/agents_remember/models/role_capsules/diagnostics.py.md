# mcp/src/agents_remember/models/role_capsules/diagnostics.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/models/role_capsules/diagnostics.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-16T08:56+02:00 |
| lastVerifiedCommitHash | `d8ed8c21644f96fd1138ae9fd4c0e5e5e93c1c03` |
| lastVerifiedCommitDate | 2026-09-17T10:09:37+02:00|
| governingOverview      | `../overview.md`                           |

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

## Docs References

No external or domain documentation is configured for this memory root
(`system/sources.md` has no entries), so no external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant documentation found after checking live sources. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The content half whose digest must stay independent of these shapes. | `CapsuleCapsule`; `CapsuleCompilationResult` | mcp/src/agents_remember/models/role_capsules/types.py:435-448; mcp/src/agents_remember/models/role_capsules/types.py:451-475 |
| The builder that fills the success-shaped manifest, and the two refusal-shaped builders. | `compiled_manifest`; `refused_manifest`; `manifest_for_error` | mcp/src/agents_remember/models/role_capsules/compiler.py:388-416; mcp/src/agents_remember/models/role_capsules/compiler.py:417-432; mcp/src/agents_remember/models/role_capsules/compiler.py:433-447 |
| The digest document that must not reference any field of this module. | `semantic_digest` | mcp/src/agents_remember/models/role_capsules/compiler.py:225-272 |
| The application outcome that pairs a capsule or a refusal with this manifest. | `CapsuleCompilationOutcome`; `render_explanation` | mcp/src/agents_remember/application/role_capsules/compilation.py:46-88 |
| The conflict kind vocabulary these rows are expressed in. | `CONFLICT_EQUAL_AUTHORITY`; `CONFLICT_DUPLICATE_IDENTITY` | mcp/src/agents_remember/models/role_capsules/types.py:68-78 |

## Cross-Repo References

No sibling-repository contract consumes these shapes.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-09-17T13:05+02:00 — 260915-CAPS-L14 curator: **D7 wrong-form evidence table repaired (memory-layer shape defect).** This card's evidence tables used the legacy header `| Finding | Citations | Source Path |` with the delimiter `| --- | --- | --- |`. The memory-quality checker requires `| Finding | Anchor | Source |` with the identifier alone in **Anchor** and a plain `path:start-end` in **Source** — which is what every row in these tables already carried, so the repair is the header and delimiter only: **no row content, anchor, range, prose or verification stamp was changed.** Each table's width was widened in all three parts together (header, delimiter, rows) as the checker's own guidance requires.

- 2026-09-16T08:56+02:00 — 260915-CAPS-L2 curator: created this card for the diagnostic
  projection added by the deterministic capsule compiler leaf (`CAPS-R02@v1`). Records the
  source/conflict/rejection/options records, the aggregate manifest with its refusal variant and
  bounded summary, and the structural rule that no field here may feed the semantic digest.
  Verification metadata is left at the leaf base commit because the source is uncommitted — the
  governed closeout stamps the real code commit.
