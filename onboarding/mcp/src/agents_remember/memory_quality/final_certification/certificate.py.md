# mcp/src/agents_remember/memory_quality/final_certification/certificate.py

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

## Evidence

### Repo-Internal References

- Derives the canonical coherence subrecord set from the current authority record. [1]
- One deterministic subrecord identity per judgment evidence reference. [2]
- Assembles the exact R21 Gate-5 semantic inputs. [3]
- The typed refusal helper. [4]
