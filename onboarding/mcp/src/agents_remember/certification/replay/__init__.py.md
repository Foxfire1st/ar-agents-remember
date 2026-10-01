# mcp/src/agents_remember/certification/replay/__init__.py

## Governing Overview

[Certification contract overview](../overview.md)

## Purpose

Deliberately small public facade of the CCR-R17 measured-replay subpackage (leaf 260831-CCR-L17, code commit e84c004c37a4bad082e1a7f1bdc4bd062282a185). Consumers enter through freeze compilation and population handling, comparability, span analysis, measured-run reduction, the seventeen mandatory acceptance scenarios, and the pair comparison report without depending on package-private helpers. The module docstring fixes the approved protocol scope: exact replay freeze identities, the append-only three-view incident-baseline population, a deterministic span analyzer over the R16 telemetry span vocabulary, a measured-run reducer over an R16 event export, seventeen mandatory acceptance scenarios projected to machine-readable outcomes, and the baseline-vs-treatment comparison report. Numeric reduction thresholds are intentionally out of scope and never appear in these records.

## Code Commentary

### Logic

The module is a pure re-export facade: six owning-module import blocks plus one closed `__all__`. `compare` (lines 12-15) contributes the pair comparison report and builder; `freeze` (lines 16-29) contributes the freeze, comparability, and population surface; `measure` (lines 30-34) contributes the measured-run reducer; `models` (lines 35-44) contributes the closed vocabulary records; `scenarios` (lines 45-49) contributes the seventeen expectations and their evaluators; and `spans` (lines 50-54) contributes the deterministic span analyzer. `__all__` (lines 56-88) fixes the complete public set in one place.

### Conventions

The facade exposes composition operations only; it never declares a numeric reduction threshold, executes a replay leg, or selects runtime authority.

### Invariants And Boundaries

- Every durable record in the subpackage is a closed immutable FrozenContractModel that digest-verifies its own content.
- No export can carry an approved performance claim: reduction thresholds are deliberately absent.
- Models remain available from their owning module so this facade does not become a second contract catalog.

### Todos

Execution and concrete replay-leg wiring are owned by later consumers, not this facade.

## Evidence

### Docs References

No Domain Documentation source is configured for this memory root. The governing task artifacts (the CCR-R17 approved replay protocol requirement packet and the 17_measured-replay-and-reduction leaf doc) define the measured-replay protocol scope; task artifact paths are not repo-relative citations, so these facts are recorded as prose here.

- The module's declared replay protocol excludes numeric reduction thresholds from its records. [1]

### Repo-Internal References

- The facade re-exports the comparison-report surface from its owning module. [2]
- The facade re-exports the freeze/population surface from its owning module. [3]
- The facade re-exports the measured-run reducer from its owning module. [4]
- The facade re-exports the span analyzer from its owning module. [5]
- `__all__` fixes the complete public replay surface in one place. [6]
- The certification route facade re-exports this whole subpackage. [7]

### Cross-Repo References

No cross-repository implementation boundary is owned here.

Measured replay stays repository-neutral contract evidence inside the certification route.
