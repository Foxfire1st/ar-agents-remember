# mcp/tests/test_replay_spans_and_measure.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_replay_spans_and_measure.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T22:23+02:00 |
| lastVerifiedCommitHash | `e84c004c37a4bad082e1a7f1bdc4bd062282a185` |
| lastVerifiedCommitDate | 2026-09-04T22:06:05+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Fully standalone CCR-R17 (leaf 260831-CCR-L17) forcing suite for the span-analysis union arithmetic and the measured-run reducer in `certification/replay/spans.py` and `certification/replay/measure.py`. Span intervals are reduced with union arithmetic so wall time is never double counted, and the measured-run reducer folds an in-memory closeout event stream into per-gate facts (start and zero-start evidence, last complete catalog, decision, finalization, operation terminal, span reduction). Nothing in this module shares certification-run, evidence-lifecycle, or Dagger artifacts.

## Code Commentary

### Logic

- Span union cases (`test_span_gross_wall_unions_overlapping_intervals`, lines 63-70; `test_span_category_wall_is_union_within_category`, lines 73-80; `test_span_reduction_covers_closed_vocabulary_and_digest`, lines 83-100; `test_span_reduction_span_count_equals_per_category_sum`, lines 103-140) pin the deterministic closed nine-category reduction and its digest.
- Reducer refusal and fold cases (`test_measure_refuses_empty_and_diagnostic_exports`, lines 288-305; `test_measure_gate_one_red_records_catalog_and_fail`, lines 308-340; `test_measure_gate_blocked_never_starts_and_zero_start_evidence`, lines 343-367; `test_measure_certificate_publish_and_spans`, lines 370-384; `test_measure_operation_terminal_and_finalization_flags`, lines 387-402) exercise the reducer over in-memory closeout event exports.
- `test_gate_run_measurement_rejects_blocked_and_started_together` (lines 405-413) pins the model shape refusal.

### Conventions

Standalone per the evidence-lifecycle isolation rule; events and spans are constructed here rather than shared.

### Invariants And Boundaries

- Wall time is never double counted: overlapping and contained intervals contribute their union.
- The measured run always folds the exact ordered Gates 1-5 over closeout-generation exports only.
- A blocked gate never starts; zero-start evidence never accompanies a started gate.

### Todos

None recorded.

## Docs References

No external Domain Documentation source is configured for this repository-owned suite.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external source governs this test module. | - | - |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The span analyzer under test. | `analyze_span_categories`; `category_wall_union_millis`; `gross_wall_union_millis` | mcp/src/agents_remember/certification/replay/spans.py:39-72; mcp/src/agents_remember/certification/replay/spans.py:26-31; mcp/src/agents_remember/certification/replay/spans.py:34-36 |
| The measured-run reducer under test. | `measure_replay_run` | mcp/src/agents_remember/certification/replay/measure.py:53-86 |
| The reduction and measurement records under test. | `SpanReduction`; `RunMeasurement`; `GateRunMeasurement` | mcp/src/agents_remember/certification/replay/models.py:150-175; mcp/src/agents_remember/certification/replay/models.py:255-286; mcp/src/agents_remember/certification/replay/models.py:196-252 |
| The explicit unit-regression lane registration. | "mcp/tests/test_replay_spans_and_measure.py" | mcp/tests/test-evidence-lanes.toml:162-162 |

## Cross-Repo References

No cross-repository implementation boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| Same-repository forcing suite; nothing crosses repositories. | - | - |

## Update History

- 2026-09-05T06:39:59+00:00 — L31 scoped citation curation against frozen ea359649: repaired anchor grammar and exact source coordinates while preserving the current behavioral claims. No content impact; source verification metadata was not advanced.

- 2026-09-04T22:23+02:00 - 260831-CCR-L17 Gate-5 memory pass: created for the new CCR-R17 span/measure forcing suite (union-wall arithmetic, closed nine-category reduction, measured-run fold over in-memory closeout exports). Verification stamp is the full leaf code commit `e84c004c37a4bad082e1a7f1bdc4bd062282a185` (tree `f97c4969d7ddb93eed75c80a4936fc05fab8e2eb`).
