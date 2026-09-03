# mcp/src/agents_remember/certification/certificate_invalidation.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/certification/certificate_invalidation.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | 6f10c24d72db6171c0d434b307e6806996e2f11d |
| lastVerifiedCommitDate | 2026-09-02T18:10:52+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Certification contract overview](overview.md)

## Purpose

Deterministic gate invalidation and exact certificate reuse planning: apply the normative
invalidation matrix with downstream dependency closure, then reuse only a current exact prefix and
resume the first unfinished boundary (CCR-R21@v2).

## Code Commentary

### Logic

`InputChangeClass` enumerates the normative change classes from code through
journal/review/approval metadata and `unchanged-interruption`/`unclassified`.
`classify_certificate_invalidation` maps each change to its start gate
(`_change_start_gates`: fixed classes have fixed starts, unclassified fails closed to Gate 1,
runtime/topology classes consume their declared gates) and unions the downstream closure. Only
coherence changes list affected Gate-5 subrecords; topology-intent/journal-review/unchanged always
revalidate finalization.

`plan_certificate_reuse` requires one exact ordered certificate prefix, unions the classified
invalidation with identity-drift closure (`_identity_drift_closure` revalidates each prefix and
invalidates from the first stale certificate), retains the maximal valid tail (revalidated), and
returns the first gate to run with `zeroGateStarts` true only when nothing invalid remains.

### Invariants And Boundaries

- Per-gate downstream closure is a fixed matrix, never caller-invented edges.
- Unclassified input change fails closed for the potential dependency closure.
- Journal/review/route-review/approval metadata never invalidates Gates 1-5 by itself unless a
  consumed semantic byte changed.
- Memory-only repair reuses Gates 1-4 and rebuilds Gate 5; a code repair invalidates Gates 1-5.
- No newest-success or historical lookup substitutes for the exact predecessor edge.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies; CCR-R21@v2 is the governing packet.

| Finding | Anchor | Source |
| --- | --- | --- |
| The R21 packet's normative invalidation matrix governs every change row. | "Normative Invalidation Matrix"; "Failure And Recovery" | ar-coordination/tasks/agents-remember/260831_closeout-certification-reform/requirements/CCR-R21-v2-content-addressed-phase-certificates.md:61-107 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The matrix and downstream closure produce one decision. | `classify_certificate_invalidation`; `_change_start_gates` | mcp/src/agents_remember/certification/certificate_invalidation.py:89-121; mcp/src/agents_remember/certification/certificate_invalidation.py:165-181 |
| Reuse retains only a current exact prefix and names the first gate to run. | `plan_certificate_reuse` | mcp/src/agents_remember/certification/certificate_invalidation.py:124-162 |
| Identity drift from any stale certificate invalidates its downstream closure. | `_identity_drift_closure` | mcp/src/agents_remember/certification/certificate_invalidation.py:184-198 |
| Coherence-only changes scope to affected Gate-5 subrecords. | `CertificateInputChange` | mcp/src/agents_remember/certification/certificate_invalidation.py:40-65 |

## Cross-Repo References

None; this is the repository-neutral invalidation engine.

## Update History

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for
  6f10c24d72db6171c0d434b307e6806996e2f11d (CCR-R21@v2/L21): created the card for the new
  invalidation/reuse planner (normative matrix, downstream closure, exact-prefix reuse,
  zero-gate-starts recovery). Verification is pinned to the owning commit.
