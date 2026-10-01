# mcp/src/agents_remember/cli/knowledge_ingest_report.py

## Governing Overview

[overview](../../../overview.md)

## Purpose

Renders the ordinary knowledge-ingest report as JSON or human-readable text. It exposes per-entry outcomes, candidate/source identity, publication selection and independent published-identity readback; an exit status is not a publication result.

## Code Commentary

### Logic

`payload` preserves the report’s typed outcomes and both authored planes. `summary` renders the same facts for a reader, including absent publication and the chosen destination rather than silently treating either as success.

`_family_block` exposes guarantees, membership endpoints, no-family bases and coverage limits. Membership rows include `retainedFromMemberId`: a retained sibling can have state `added` because the successor edge is new while the invariant revision is unchanged. `_family_line` reports the count of retained revisions separately from added/reused/retired edge counts.

The renderer does not recompute the roster or publish knowledge. Null measured counts and recorded/projected/not-recorded states arrive from the coverage owner and retain their meaning. `publishedIdentity` may be absent, confirmed, mismatched or unavailable; those outcomes are not interchangeable.

### Conventions

The CLI entry resolves authorization and destination; this module only renders its report. Family and source report types are imported rather than redefined. JSON field additions propagate the measured vocabulary without introducing a store schema.

### Invariants And Boundaries

- Read every committed, ruling and refused entry; process exit is insufficient.
- Retention provenance identifies an old membership, while edge state describes the new one.
- Projected coverage cannot become a measured zero or publication success.
- Report rendering creates no record, assessment or acceptance authority.

### Todos

No additional work is asserted by this card. Actual project publication and semantic acceptance remain separately evidenced outcomes.

## Evidence

### Docs References

No configured Domain Documentation source applies to this repository-owned contract.

The operative contract is defined by the repository sources cited below.

### Repo-Internal References

These references name the current owners and the behavior they establish.

- Render the complete structured operation and publication outcome. [1]
- Render the human-readable report without inferring acceptance. [2]
- Expose retainedFromMemberId beside each membership’s exact endpoints. [3]
- Count retained revisions separately from added/reused/retired edges. [4]
- Coverage owns the measured sibling arithmetic. [5]

### Cross-Repo References

No sibling repository defines this file's contract.

No meaningful cross-repository implementation dependency.
