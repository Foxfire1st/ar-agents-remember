# mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/summary.py

## Governing Overview

[overview.md](../../overview.md)

## Purpose

`summary.py` produces bounded converted validator/reference measurements for context/drift callers. Nonconverted memory returns `status: error` via `legacy_format_refusal`; it is never silently classified as checked zero. Public quality dispatch calls the converted checker directly, not a legacy summary-packet wrapper.

## Code Commentary

### Landing-report scope

The converted summary explicitly calls the shared converted checker with `include_landing=False`. It remains a validator/reference-state summary; the landing census belongs to quality-check callers rather than this drift-summary route; admitted leaf callers carry their leaf base. Skipping landing acquisition here changes no summary count, filing mode, reference-state classification or existing validator refusal.


- The converted drift summary suppresses landing acquisition while preserving validator/reference measurements. [13]




### Logic

`run_drift_summary` refuses an absent onboarding root and an unreadable converted onboarding directory. Converted trees delegate to `_run_converted_summary`; nonconverted trees return a format-refusal error. `not_checked` returns only `status: notChecked`. Explicit `output.write_report=False` files neither report nor observer snapshot.

Explicit report-producing calls also persist `actionableFingerprint` over the complete converted stale-reference finding population, not the bounded preview, counts or a clock. `_actionable_fingerprint` canonicalizes each row and sorts before hashing. An unreadable converted sidecar leaves that identity unknown (`None`). Current discovery is the converted checker, not removed legacy classification through `drift.py`.

The retained summary builders return `DriftSummaryPacket`. `DriftStatus` is declared in `models/drift.py`; checked, error and notChecked share a single status vocabulary with the wire models. Optional keys depend on status and output mode rather than being invented to make an unread result look measured.

`_write_converted_snapshot` persists the already measured converted packet with current/stale/violation counts, stale actionableCount, bounded sampled rows, checkedAt, branch and source/memory/report provenance. Its shared schema and `drift_snapshot_path` keep producer, reader, pruning and cleanup aligned. The snapshot is best-effort: `OSError` is suppressed and cannot fail the measurement.

The concrete snapshot filename is derived by the shared `drift_snapshot_path` helper, never reconstructed locally.

`DriftSummaryOutput` makes optional filing and full-row materialization explicit. Its default `write_report=True` is report-producing; `False` suppresses Markdown, snapshot and reportPath together. Converted measurement remains unchanged. `include_rows=True` adds complete stale findings and refusing validator findings while ordinary packets retain bounded samples.

### Invariants And Boundaries

- Converted measurement delegates only to `converted_knowledge_check(..., include_landing=False)`; legacy discovery/classifiers do not run.
- `models/drift.py` owns status vocabulary; the packet reuses it.
- Checked packets retain exact current/stale/refusing/report-only counts, roots and unreadable sidecars with bounded samples. Errors carry reasons without fabricated counts.
- Filing mode controls report, snapshot and reportPath together; complete rows are separate opt-in material.
- Report paths remain operational, outside durable memory. Snapshot writes suppress OSError and use shared schema/path helpers; provenance comes from the measured context, not observer inference.

## Evidence

### Repo-Internal References

- Context-packet composition calls the converted-only bounded drift summary without filing a report. [1]


- The drift-snapshot dir + schema the b1 write targets (shared with the reader). [6]

- The shared drift-snapshot filename helper now used by the producer. [7]


- The observer reader that consumes the persisted snapshot. [8]



- The converted snapshot persists current/stale/violation counts and source/memory/report provenance from the measured packet. [9]


- A converted tree takes `_run_converted_summary`: `status: checked` with `basis: converted-references`,
  the two roots, `sidecarCount`, `count` over observed code/test anchors, `states: {current, stale}`,
  `actionableCount` as the stale count with a bounded `actionableSample`, `violationCount` with a
  bounded `violationSample` of refusing findings, `reportOnlyCount`, and `unreadableSidecars`. Counts
  are exact; only the samples are bounded. A tree that cannot be read returns `status: error` with the
  reason and no counts. An optional `KnowledgeBasePort` base selects the comparison base; the memory
  layer owns no base, the application callers that own a contract bind it.

- A converted tree is measured from the converted check alone; legacy discovery never runs there. [10]


- The converted summary exposes measured counts, roots and unreadable sidecars; zero alone does not prove the entire memory tree was readable. [11]



- The converted branch gates report, observer snapshot and reportPath together; unfiled reads retain the same measured packet. [12]



- DriftSummaryPacket imports the canonical DriftStatus owner and retains optional converted measurement fields; the classification set is removed. [3]

- The context-packet wire model that validates this packet's `status` — the one that used to lack `error`. [4]

- The tool response model that validates the same packet. [5]

## Current source evidence



- Explicit snapshots fingerprint complete actionable findings, with unknown identity for unreadable converted sidecars. [14]


- Current source account and its stated boundaries. [15]
