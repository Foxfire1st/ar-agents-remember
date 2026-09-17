# mcp/src/agents_remember/memory/knowledge/candidate_receipt.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/candidate_receipt.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T11:30+02:00 |
| lastVerifiedCommitHash | `420669c459aab3650cdaa5b3e5271e71d7d94c0e`|
| lastVerifiedCommitDate | 2026-09-17T10:54:08+02:00|
| governingOverview | `mcp/src/agents_remember/memory/overview.md` |

## Governing Overview

[memory route overview](../overview.md)

## Purpose

The immutable local receipt, read and written as **one object**: the candidate database carries knowledge, the
receipt carries *which candidate* it is (namespace, lane, exact code and memory inputs, schema generation,
candidate reference). Neither is recoverable from the other, which is why the receipt is never inferred from a
path.

The module owns three things and nothing else: canonical bytes for writing the receipt, a read that turns every
failure into a `KnowledgeStorageError` naming the exact path, and the binding comparison that decides whether an
existing candidate is the one this admission presented.

## Code Commentary

### Logic

- `write_candidate_receipt` encodes the receipt through `canonical_json_bytes` rather than a pretty-printed dump,
  so the same receipt always has the same file content and a digest over the file is a digest over the binding
  itself; it publishes through `atomic_write_bytes`, so a reader sees the old receipt or the new one.
- `read_candidate_receipt` validates on read. A read failure, non-UTF-8/ambiguous JSON, and a receipt that does
  not seal itself all raise `KnowledgeStorageError` — a receipt that cannot be read is **not** a candidate this
  package will operate on, and the caller turns that into the `selected_input_unavailable` refusal that names the
  exact path.
- `build_receipt_for_candidate(destination, schema)` derives a receipt from the admitted resolution and the schema
  the database actually carries. It is a thin adapter over `models.knowledge.snapshot.build_candidate_receipt`, so
  there is exactly one constructor of seals.
- `receipt_binding_refusal` performs **three comparisons that answer three different questions**, and the
  distinction is the point:
  1. **against the database** — is the stored namespace the admission's? A database bound elsewhere is not a stale
     receipt but a different knowledge namespace, and answering `candidate_binding_changed` is what keeps a rebind
     from happening by accident;
  2. **against the schema generation** — was this candidate created under the generation this code declares? The
     check is the recorded **fingerprint**, because a database can pass the current table manifest while having
     been written by a different generation's rules;
  3. **against the admission** — were these the lane, the exact code and memory inputs, the snapshot/candidate/task
     references this candidate was admitted with?
- The expected binding is rebuilt through the same constructor a new candidate uses (with the receipt's own
  recorded schema generation, since that has already been verified), so the comparison cannot drift from the value
  a creation would write. `_BINDING_FIELDS` is that compared set, and `_render` names only the differing fields in
  the refusal's `expected`/`observed` so a caller is told what actually differs rather than given two full
  receipts.

### Conventions

- The expected-binding derivation deliberately reuses `build_candidate_receipt` instead of comparing fields by
  hand: a hand-written comparison is a second definition of the binding, and the two would drift.
- Refusals are **values** (`KnowledgeRefusal | None`), while unreadable/unsealable receipts are **defects** raised
  as `KnowledgeStorageError`. The caller decides which refusal vocabulary a defect maps into; this module does not
  invent one.

### Invariants And Boundaries

- **The receipt is content-addressed and validated on read.** A receipt edited in place, or written by a different
  admission, is detected and answered with a typed refusal — the working database is never re-initialized,
  repaired or partially trusted to make a later step succeed.
- **The write is atomic and canonical.** Same receipt, same bytes; the digest over the file is a digest over the
  binding.
- **Schema identity is compared by fingerprint, not by table manifest.** A generation can share a manifest and
  differ in rules.
- **Boundary.** This module owns receipt bytes and the binding comparison. It does not open a database, decide the
  candidate lifecycle, or choose a refusal code for an unreadable file.

### Todos

None recorded for this slice.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The admission-derived field set compared when a candidate is reopened. | `_BINDING_FIELDS` | mcp/src/agents_remember/memory/knowledge/candidate_receipt.py:38-46 |
| The canonical, atomic receipt write. | `write_candidate_receipt` | mcp/src/agents_remember/memory/knowledge/candidate_receipt.py:49-58 |
| The validating read that turns every failure into a defect naming the path. | `read_candidate_receipt` | mcp/src/agents_remember/memory/knowledge/candidate_receipt.py:61-86 |
| The one adapter that derives a receipt from an admitted destination. | `build_receipt_for_candidate` | mcp/src/agents_remember/memory/knowledge/candidate_receipt.py:89-99 |
| The three-comparison binding check and its refusal. | `receipt_binding_refusal` | mcp/src/agents_remember/memory/knowledge/candidate_receipt.py:102-160 |
| The differing-field rendering used in a refusal's facts. | `_render` | mcp/src/agents_remember/memory/knowledge/candidate_receipt.py:163-166 |
| The sealed receipt model and its read-time seal validator. | `CandidateReceipt`; `receipt_digest`; `build_candidate_receipt` | mcp/src/agents_remember/models/knowledge/snapshot.py:109-141; mcp/src/agents_remember/models/knowledge/snapshot.py:144-148; mcp/src/agents_remember/models/knowledge/snapshot.py:151-185 |
| The canonical encoder and the atomic publisher this module writes through. | `canonical_json_bytes`; `atomic_write_bytes` | mcp/src/agents_remember/kernel/atomic_write.py:51-70; mcp/src/agents_remember/kernel/canonical_json.py:27-31 |
| The refusal this module returns for a receipt that is not this admission's. | `candidate_binding_changed_refusal` | mcp/src/agents_remember/memory/knowledge/refusals.py:904-928 |
| The lifecycle caller that reads both candidate inputs before anything else. | `_candidate_inputs` | mcp/src/agents_remember/memory/knowledge/candidate_workspace.py:430-454 |
| The schema identity the fingerprint comparison is made against. | `inspect_schema`; `KnowledgeSchemaIdentity` | mcp/src/agents_remember/memory/knowledge/connection.py:106-123; mcp/src/agents_remember/models/knowledge/context.py:24-30 |
| The node that proves a candidate the admission cannot verify is refused with its bytes intact. | "test_a_candidate_the_admission_cannot_verify_is_refused_with_its_bytes_intact" | mcp/tests/test_knowledge_candidate_workspace.py:137-162 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-17T06:49:47+00:00: Generated citation repair: `canonical_json_bytes`; `atomic_write_bytes` repointed to mcp/src/agents_remember/kernel/canonical_json.py:27-31; mcp/src/agents_remember/kernel/atomic_write.py:51-70. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-16T11:30+02:00 — 260915-KS-L4 curator (uncommitted change set on `ar/260915-ks-l04`, base `76c7697c`): created this one-to-one card for the new receipt module. It records the three comparisons a reopen actually makes (database namespace, schema *fingerprint* generation, admission binding) and why they are not one comparison, the deliberate reuse of the one receipt constructor so the expected value cannot drift, the canonical-atomic write, and the defect-versus-refusal split (an unreadable receipt is a storage error the caller maps, not a refusal invented here). Verification metadata remains empty until closeout stamps the code commit.
