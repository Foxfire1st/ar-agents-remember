# mcp/src/agents_remember/models/knowledge/digest.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/knowledge/digest.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T22:40+02:00 |
| lastVerifiedCommitHash |  `60e0820e6cb3b1d160518b9f8c7ac6241323a281`|
| lastVerifiedCommitDate |  2026-09-15T22:46:24+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[models route overview](../../../overview.md)

## Purpose

The one owner of what a revision's identity seals: the canonical payload mapping, its SHA-256 digest, and the
sealing operation that turns an authored aggregate into a stored one.

## Code Commentary

### Logic

`REVISION_PAYLOAD_VERSION = "invariant-revision-payload/v1"` is recorded in the payload rather than inferred from
which fields are present, so a changed sealed field set is a different identity computation.

`canonical_revision_payload(revision)` returns the exact mapping the digest covers: `payload_version`,
`repository_id`, `invariant_id`, `revision_id`, `display_version`, `statement`, `applicability`, the ordered
`conditions` and `exclusions` lists, `state_at_origin`, `acceptance_ref`, the JSON-mode `provenance` envelope and
`sorted(predecessors)`. The digest field is deliberately absent, because a digest cannot cover itself.

`revision_payload_digest` hashes that mapping through `kernel.canonical_json.sha256_digest`, and `sealed_revision`
returns `revision.model_copy(update={"payload_digest": ...})`.

### Conventions

The predecessor set enters the digest **sorted**, because the authored set is what is being sealed and the order a
caller happened to write it in is not authored information. Clause order inside `conditions`/`exclusions` is kept,
because that order is the author's.

### Invariants And Boundaries

- The predecessor set is inside the seal, so an edge cannot be edited behind an existing sealed revision: adding or
  removing one changes the aggregate the revision identity stands for. `memory/knowledge/records.py` re-derives
  the digest on read and refuses a row whose stored seal no longer holds.
- The store recomputes rather than trusting a supplied digest: `RevisionDraft` has no digest field at all.
- Changing the sealed field set means a new `REVISION_PAYLOAD_VERSION`, never a silent reinterpretation of stored
  digests.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The exact sealed mapping, including the sorted predecessor set and the excluded digest. | `canonical_revision_payload` | mcp/src/agents_remember/models/knowledge/digest.py:23-45 |
| The digest computation and the single sealing operation. | `revision_payload_digest`; `sealed_revision` | mcp/src/agents_remember/models/knowledge/digest.py:48-59 |
| The recorded payload version, bumped only when the sealed field set changes. | `REVISION_PAYLOAD_VERSION` | mcp/src/agents_remember/models/knowledge/digest.py:18-20 |
| The read path re-derives the seal and refuses a rewritten row. | `decode_revision_row` | mcp/src/agents_remember/memory/knowledge/records.py:135-169 |
| The store seals the draft rather than accepting a caller-supplied digest. | `sealed_revision_from_draft` | mcp/src/agents_remember/memory/knowledge/records.py:172-194 |
| The canonical encoder the digest is computed through. | `sha256_digest` | mcp/src/agents_remember/kernel/canonical_json.py:34-37 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-15T22:40+02:00 — 260915-KS-L1 curator (uncommitted change set on `ar/260915-ks-l01`, base `67b21aeb`): created this one-to-one card for the new revision-payload seal. It records that the predecessor set is inside the digest and that the digest field is the only excluded member. Verification metadata remains empty until closeout stamps the code commit.
