# mcp/src/agents_remember/certification/replay/spans.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/certification/replay/spans.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T22:23+02:00 |
| lastVerifiedCommitHash | `e84c004c37a4bad082e1a7f1bdc4bd062282a185` |
| lastVerifiedCommitDate | 2026-09-04T22:06:05+02:00 |
| governingOverview | `../overview.md` |

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

## Docs References

No Domain Documentation source is configured for this memory root. The governing task artifacts (the CCR-R17 approved replay protocol requirement packet and the 17_measured-replay-and-reduction leaf doc) define union-wall reduction as the reproducibility requirement; task artifact paths are not repo-relative citations, so these facts are recorded as prose here.

| Finding | Anchor | Source |
| --- | --- | --- |
| Reproducible arithmetic: every union can be recomputed from raw span intervals. | `_wall_union_millis` | mcp/src/agents_remember/certification/replay/spans.py:79-90 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The analyzer consumes the R16 telemetry span vocabulary. | `TelemetrySpan`; `TelemetrySpanKind` | mcp/src/agents_remember/certification/telemetry/models.py |
| The reduction record is defined in the replay models module. | `SpanReduction`; `SpanCategoryTotals` | mcp/src/agents_remember/certification/replay/models.py:150-175; mcp/src/agents_remember/certification/replay/models.py:135-147 |
| The measured-run reducer delegates its span fold here. | `analyze_span_categories` | mcp/src/agents_remember/certification/replay/measure.py:53-86 |
| Content digests follow the shared certification digest helper. | `content_digest` | mcp/src/agents_remember/certification/digests.py:12-22 |
| The public subpackage facade re-exports the analyzer. | `replay.__all__` | mcp/src/agents_remember/certification/replay/__init__.py:56-88 |

## Cross-Repo References

No cross-repository implementation boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| Span reduction stays repository-neutral over the shared telemetry vocabulary. | - | - |

## Update History

- 2026-09-04T22:23+02:00 - 260831-CCR-L17 Gate-5 memory pass: created this card for the new CCR-R17 span analyzer delivered in code commit `e84c004c37a4bad082e1a7f1bdc4bd062282a185` (tree `f97c4969d7ddb93eed75c80a4936fc05fab8e2eb`).
