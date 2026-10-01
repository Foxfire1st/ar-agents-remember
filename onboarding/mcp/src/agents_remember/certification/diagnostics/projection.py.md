# mcp/src/agents_remember/certification/diagnostics/projection.py

## Governing Overview

[Certification contract overview](../overview.md)

## Purpose

Owns the optional-lane readiness projection for the CCR-R13 non-certifying diagnostic lane (leaf 260831-CCR-L13, code commit 4ba18bb2). CCR-R13 keeps the optional diagnostic lane explicitly separable from the R09 closeout readiness vocabulary: before any request the lane projects not-requested-optional and no diagnostic artifact, Dagger owner, or telemetry envelope is fabricated; after a request the lane projects the newest terminal result for the exact candidate with immutable predecessor links. A current requested failure or abort blocks final certification until a newer terminal result for the same candidate passes or a changed candidate receives its own disposition; historical passes can never override a newer failure; and no number of diagnostic passes can satisfy or be promoted into R14.

## Code Commentary

### Logic

- `DiagnosticLaneProjection` (lines 59-86) is the closed projection record (schema `diagnostic-lane-projection/v1`) with self-verified `projectionDigest`; its validator (lines 71-86) refuses not-requested-optional alongside any requested evidence, refuses a running lane carrying a newest terminal, and routes terminal dispositions through `_require_terminal_projection` (lines 89-98), which mirrors disposition to the newest terminal result and derives `blockingCertification` from disposition plus plan currentness.
- `project_diagnostic_lane` (lines 101-140) projects not-requested-optional only from a completely empty manifest, refuses an empty-lane projection for a candidate that has attempts (`diagnostic-lane-not-optional`, lines 126-132), projects running for a live attempt with no terminal, and otherwise selects the newest terminal result (`_terminal_projection`, lines 169-181). A supplied `current_plan` that differs from the newest result's plan identity stales the result (`currentForPlan=false`) via `_result_is_current` (lines 184-196).
- `diagnostic_blocks_certification` (lines 143-152) is the one boolean closeout consumer: true when the newest terminal result (or its plan staleness) blocks final certification.
- `diagnostic_never_satisfies_certification` (lines 155-166) is a stable false: the R14 final proof requires its own two fresh certifying replications and never consumes diagnostic evidence.
- `_projection` (lines 199-221) computes the blocking flag (newest result non-pass or stale) and constructs the digest-bound record.

### Conventions

The lane is derived, never rewritten: selection always reads the newest terminal result from the store's immutable manifest, and empty-lane projection is represented by absence plus the typed not-requested-optional shape, never by deleting a requested failure.

### Invariants And Boundaries

- not-requested-optional can only be projected from an empty manifest and can never erase a requested failure.
- A requested failure or abort blocks final certification until a newer terminal pass for the same candidate or a changed candidate's own disposition.
- A diagnostic pass never blocks but never satisfies or promotes into R14.
- Plan changes stale the newest result until a newer result binds the current plan identity.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured for this memory root. CCR-R13@v2 (frozen digest f0387b1627c5e8f48073b55d40dc362065e46943c5688f0f863fddb480770d3a) and R09 readiness-vocabulary separation rules in the leaf docs govern this projection; task artifact paths are not repo-relative citations, so they are recorded as prose.

- Diagnostic evidence can never satisfy or promote into the R14 final proof. [1]

### Repo-Internal References

- Reads the durable per-candidate manifest and newest terminal through the isolated store. [2]
- Closed immutable base for registry, plan, and result records. [3]
- Return a stable SHA-256 digest for one JSON-compatible contract value. [4]
- R09 closeout readiness keeps diagnostics explicitly non-certifying through this projection. [5]
- The facade re-exports lane projection helpers for closeout consumers. [6]

### Cross-Repo References

No cross-repository implementation boundary is owned here.

- The projection stays repository-neutral over store and candidate inputs only. [7]
