# mcp/src/agents_remember/certification/replay/spans.py

## Governing Overview

[Certification contract overview](../overview.md)

## Purpose

Owns the CCR-R17 (leaf 260831-CCR-L17) deterministic per-category span reduction over R16 telemetry spans. The analyzer classifies every measured span into exactly one closed category (the R16 `TelemetrySpanKind` vocabulary), unions overlapping wall intervals inside each category so wall time is never double counted, and reduces the whole export to gross wall and active time plus span count. Arithmetic is reproducible: a caller can independently recompute every union from the raw span intervals.

## Code Commentary

### Logic

- `category_wall_union_millis` (lines 26-31) unions the wall intervals of exactly one category.
- `gross_wall_union_millis` (lines 34-36) unions wall intervals across every measured span with no double counting.
- `analyze_span_categories` (lines 39-72) sorts spans by category then start time, buckets them per category, and emits the closed nine-category `SpanReduction` (each category with union wall, summed active time, and count; plus gross wall/active and total count), digesting the reduction content.
- `_interval` (lines 75-76) maps a span to its half-open wall interval; `_wall_union_millis` (lines 79-90) is the standard interval-union sweep (sort by start then end, extend the cursor only past overlap).

### Conventions

The closed category set is iterated from `TelemetrySpanKind.__args__` in sorted order so the record is stable across runs.

### Invariants And Boundaries

- Wall time is never double counted: overlapping and contained intervals contribute their union, not their sum.
- Every measured span falls into exactly one closed category; the reduction always carries all nine categories.
- The analyzer reduces spans only; it never interprets event meaning or certifies a gate.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured for this memory root. The governing task artifacts (the CCR-R17 approved replay protocol requirement packet and the 17_measured-replay-and-reduction leaf doc) define union-wall reduction as the reproducibility requirement; task artifact paths are not repo-relative citations, so these facts are recorded as prose here.

- Reproducible arithmetic: every union can be recomputed from raw span intervals. [1]

### Repo-Internal References

- The analyzer consumes the R16 telemetry span vocabulary. [2]
- The reduction record is defined in the replay models module. [3]
- The measured-run reducer delegates its span fold here. [4]
- Content digests follow the shared certification digest helper. [5]
- The public subpackage facade re-exports the analyzer. [6]

### Cross-Repo References

No cross-repository implementation boundary is owned here.

Span reduction stays repository-neutral over the shared telemetry vocabulary.
