# mcp/src/agents_remember/memory_quality/final_certification/certificate.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/final_certification/certificate.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T01:48+02:00 |
| lastVerifiedCommitHash | `16d1a4d6d6f8e8572b4bca10b8a4a84485449604` |
| lastVerifiedCommitDate | 2026-09-04T00:55:21+02:00 |
| governingOverview | `../overview.md` |

## Governing Overview

[memory_quality overview](../overview.md)

## Purpose

R21 Gate-5 semantic-input assembly for the final full memory-coherence certification
(CCR-R08). Derives the canonical coherence subrecord set from the current curator-coherence
authority record and assembles the exact `GateFiveSemanticInputs` bundle the Gate-5
certificate needs, refusing with a typed `FinalCertificationError` whenever the record,
evidence coverage, or input bundle is not exact.

## Code Commentary

### Logic

Module-level surface:

- `coherence_subrecords` (lines 24-66) - one content-addressed subrecord for the immutable
  coherence record itself plus one per judgment evidence byte range the record binds; any
  repair-declared affected subrecord (raw judgment evidence reference or
  `coherence-record`) that the current record does not cover refuses
  (gate-five-affected-coherence-subrecords-uncovered) so coherence-evidence invalidation cannot
  hide behind a stale repair plan. The set is returned deterministically sorted by subrecord id
  and digest.
- `_judgment_subrecord_id` (lines 69-72) - one deterministic subrecord identity per judgment
  evidence reference (`judgment-evidence-<sha256>`).
- `assemble_gate_five_inputs` (lines 75-105) - builds `GateFiveSemanticInputs` from the
  memory tree, affected-closure plan digest, checker-registry digest, coherence subrecords and
  candidate-pair authority digest; empty subrecords and closed validation failures refuse
  through `_refuse` (108-109).

### Conventions

Refusals are typed and carry a legal `next_action` (curator_coherence or
memory_quality_check) instead of raising raw validation errors.

### Invariants And Boundaries

- The Gate-5 certificate requires at least one canonical coherence subrecord.
- The module never mutates code or memory; it only derives identities and assembles inputs.
- Affected subrecords must be covered by the current record, never assumed.

### Todos

None.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Derives the canonical coherence subrecord set from the current authority record. | `coherence_subrecords` | mcp/src/agents_remember/memory_quality/final_certification/certificate.py:24-66 |
| One deterministic subrecord identity per judgment evidence reference. | `_judgment_subrecord_id` | mcp/src/agents_remember/memory_quality/final_certification/certificate.py:69-72 |
| Assembles the exact R21 Gate-5 semantic inputs. | `assemble_gate_five_inputs` | mcp/src/agents_remember/memory_quality/final_certification/certificate.py:75-105 |
| The typed refusal helper. | `_refuse` | mcp/src/agents_remember/memory_quality/final_certification/certificate.py:108-109 |

## Update History

- 2026-09-04T01:48+02:00 — 260831-CCR-L08 Gate-5 memory pass: created this file-level
  onboarding card for the new CCR-R08 R21 Gate-5 semantic-input assembly module delivered in
  code commit 16d1a4d6; anchors and ranges derived from the current worktree source and pinned
  to that commit.
