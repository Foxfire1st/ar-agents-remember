# mcp/src/agents_remember/certification/certificate_invalidation.py

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

## Evidence

### Docs References

No configured Domain Documentation source applies; CCR-R21@v2 is the governing packet.

- Certificate input changes are classified and their downstream invalidation closure is computed before reuse. [1]

### Repo-Internal References

- The matrix and downstream closure produce one decision. [2]
- Reuse retains only a current exact prefix and names the first gate to run. [3]
- Identity drift from any stale certificate invalidates its downstream closure. [4]
- Coherence-only changes scope to affected Gate-5 subrecords. [5]

### Cross-Repo References

None; this is the repository-neutral invalidation engine.
