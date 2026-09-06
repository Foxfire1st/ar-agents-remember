# mcp/src/agents_remember/certification/diagnostics/projection.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/certification/diagnostics/projection.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T17:50+02:00 |
| lastVerifiedCommitHash | `4ba18bb23ba90e201bb37341d61c0efc64161fcf` |
| lastVerifiedCommitDate | 2026-09-04T17:23:11+02:00 |
| governingOverview | `../overview.md` |

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

## Docs References

No Domain Documentation source is configured for this memory root. CCR-R13@v2 (frozen digest f0387b1627c5e8f48073b55d40dc362065e46943c5688f0f863fddb480770d3a) and R09 readiness-vocabulary separation rules in the leaf docs govern this projection; task artifact paths are not repo-relative citations, so they are recorded as prose.

| Finding | Anchor | Source |
| --- | --- | --- |
| Diagnostic evidence can never satisfy or promote into the R14 final proof. | `diagnostic_never_satisfies_certification` | mcp/src/agents_remember/certification/diagnostics/projection.py:152-163 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Reads the durable per-candidate manifest and newest terminal through the isolated store. | `manifest`; `newest_terminal` | mcp/src/agents_remember/certification/diagnostics/store.py:63-70 |
| Closed immutable base for registry, plan, and result records. | "class FrozenContractModel" | mcp/src/agents_remember/models/certification/base.py:30-33 |
| Return a stable SHA-256 digest for one JSON-compatible contract value. | "def content_digest" | mcp/src/agents_remember/certification/digests.py:12-22 |
| R09 closeout readiness keeps diagnostics explicitly non-certifying through this projection. | `compile_closeout_readiness` | mcp/src/agents_remember/certification/readiness.py:43-89 |
| The facade re-exports lane projection helpers for closeout consumers. | `__all__`; `DiagnosticLaneProjection`; `diagnostic_blocks_certification`; `diagnostic_never_satisfies_certification`; `project_diagnostic_lane` | mcp/src/agents_remember/certification/diagnostics/__init__.py:31-37; mcp/src/agents_remember/certification/diagnostics/__init__.py:43-67 |

## Cross-Repo References

No cross-repository implementation boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| The projection stays repository-neutral over store and candidate inputs only. | `project_diagnostic_lane` | mcp/src/agents_remember/certification/diagnostics/projection.py:98-137 |

## Update History
- 2026-09-06T22:41:21+00:00: Generated citation repair: `diagnostic_never_satisfies_certification` repointed to mcp/src/agents_remember/certification/diagnostics/projection.py:152-163. No content impact: mechanical anchor-range projection bound to citation source snapshot 250eac92295fa399589ccf1c9726bfb4cd28a1a0b20dca126769403fba09b52d; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-06T22:41:21+00:00: Generated citation repair: `project_diagnostic_lane` repointed to mcp/src/agents_remember/certification/diagnostics/projection.py:98-137. No content impact: mechanical anchor-range projection bound to citation source snapshot 250eac92295fa399589ccf1c9726bfb4cd28a1a0b20dca126769403fba09b52d; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-05T06:39:59+00:00 — L31 scoped citation curation against frozen ea359649: repaired anchor grammar and exact source coordinates while preserving the current behavioral claims. No content impact; source verification metadata was not advanced.

- 2026-09-04T17:50+02:00 - 260831-CCR-L13 Gate-5 memory pass: created this card for the new CCR-R13@v2 optional-lane readiness projection delivered in code commit 4ba18bb2; anchors and ranges derived from the current worktree source and pinned to that commit (tree 631145bf3e0d5899b1dcbccf8c0d4a8257821f0d).
