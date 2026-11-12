# mcp/src/agents_remember/certification/replay/compare.py

## Governing Overview

[Certification contract overview](../overview.md)

## Purpose

Owns the CCR-R17 (leaf 260831-CCR-L17) baseline-vs-treatment replay comparison report. The report binds the exact freeze identity of each leg, the pair comparability verdict, the measured treatment facts, and the machine-readable outcome of every mandatory acceptance scenario. It carries raw measurements only: no numeric reduction threshold appears anywhere in the record.

## Code Commentary

### Logic

- `ReplayComparisonInput` (lines 34-44) - the complete frozen pair plus measured legs one comparison report binds (baseline/treatment freezes, the comparability report, both run measurements, the scenario evidence envelope, optional population, and a note).
- `ReplayComparisonReport` (lines 47-69) - one digest-bound comparison: both freezes, the comparability report, optional population, the exact baseline and treatment leg digests, exactly seventeen ordered scenario outcomes (min/max length 17), and a self-verifying `reportDigest` (validator lines 64-68); the fixed literal `measured-replay-comparison/v1` schemaVersion identifies the record.
- `build_replay_comparison_report` (lines 72-96) copies the measured treatment/baseline into the evidence envelope, evaluates all seventeen scenarios over it, constructs the draft report, digests the content excluding `reportDigest`, and returns a validated report.

### Conventions

The report is a closed immutable `FrozenContractModel` whose digest binds every carried fact; the builder always revalidates the final record.

### Invariants And Boundaries

- The comparison report always carries the exact seventeen ordered scenario outcomes.
- Each leg digest names its freeze digest; the report digest binds both freezes, comparability, population, and outcomes.
- The report records measurements only and never embeds an approved reduction threshold.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured for this memory root. The governing task artifacts (the CCR-R17 approved replay protocol requirement packet and the 17_measured-replay-and-reduction leaf doc) define the pair comparison report; task artifact paths are not repo-relative citations, so these facts are recorded as prose here.

- The report binds exact leg freezes, comparability, measured legs, and all scenario outcomes in one digest. [1]

### Repo-Internal References

- The report binds freeze and population records from the freeze owner. [2]
- The builder projects the mandatory scenarios over the measured evidence. [3]
- The report consumes the measured vocabulary from the replay models module. [4]
- Content digests follow the shared certification digest helper. [5]
- The public subpackage facade re-exports the comparison surface. [6]

### Cross-Repo References

No cross-repository implementation boundary is owned here.

Comparison reporting stays repository-neutral over the measured evidence envelope.
