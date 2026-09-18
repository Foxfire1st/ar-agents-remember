# mcp/src/agents_remember/models/knowledge/digest.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/knowledge/digest.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T08:24+02:00 |
| lastVerifiedCommitHash |  `7b1db4e0d73a321ee49df8725f5fe75846cf6c2b`|
| lastVerifiedCommitDate |  2026-09-18T13:43:14+02:00|
| governingOverview | `../overview.md` |

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

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The exact invariant sealed mapping, including the sorted predecessor set and the excluded digest. | `canonical_revision_payload` | mcp/src/agents_remember/models/knowledge/digest.py:30-52 |
| The digest computation and the single sealing operation for the invariant payload. | `revision_payload_digest`; `sealed_revision` | mcp/src/agents_remember/models/knowledge/digest.py:55-58; mcp/src/agents_remember/models/knowledge/digest.py:61-68 |
| The exact family sealed mapping, which seals the joint guarantee and the same sorted predecessor set. | `canonical_family_revision_payload`; `family_revision_payload_digest`; `sealed_family_revision` | mcp/src/agents_remember/models/knowledge/digest.py:71-90; mcp/src/agents_remember/models/knowledge/digest.py:93-96; mcp/src/agents_remember/models/knowledge/digest.py:99-102 |
| The recorded payload versions, separate so one payload's digest cannot be read as the other's. | `REVISION_PAYLOAD_VERSION`; `FAMILY_REVISION_PAYLOAD_VERSION` | mcp/src/agents_remember/models/knowledge/digest.py:26-27 |
| The read path re-derives both seals and refuses a rewritten row or edge. | `decode_revision_row`; `decode_family_revision_row` | mcp/src/agents_remember/memory/knowledge/records.py:153-189; mcp/src/agents_remember/memory/knowledge/records.py:327-356 |
| The store seals the draft rather than accepting a caller-supplied digest, on both aggregates. | `sealed_revision_from_draft`; `sealed_family_revision_from_draft` | mcp/src/agents_remember/memory/knowledge/records.py:190-214; mcp/src/agents_remember/memory/knowledge/records.py:303-326 |
| The node that proves each sealed field is load-bearing rather than incidentally covered. | "test_an_invariant_revision_digest_seals_its_predecessor_set" | mcp/tests/test_knowledge_revision_seals.py:63-95 |
| The canonical encoder the digest is computed through. | `sha256_digest` | mcp/src/agents_remember/kernel/canonical_json.py:34-37 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-16T08:24+02:00 — 260915-KS-L2 curator (uncommitted change set on `ar/260915-ks-l02`, base `60e0820e`): recorded the family payload and its own version constant, extended the read-path rule to both seals (each recomputed over stored rows plus stored predecessor edges), and recorded that the field-isolating evidence for the sealed predecessor set now exists on both payloads. The two versions are separate so a digest can never be read as the other object's identity. Verification metadata remains empty until closeout stamps the code commit.
- 2026-09-15T22:40+02:00 — 260915-KS-L1 curator (uncommitted change set on `ar/260915-ks-l01`, base `67b21aeb`): created this one-to-one card for the new revision-payload seal. It records that the predecessor set is inside the digest and that the digest field is the only excluded member. Verification metadata remains empty until closeout stamps the code commit.
