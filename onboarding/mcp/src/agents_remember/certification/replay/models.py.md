# mcp/src/agents_remember/certification/replay/models.py

## Governing Overview

[Certification contract overview](../overview.md)

## Purpose

Owns the closed immutable vocabulary of the CCR-R17 (leaf 260831-CCR-L17) measured-replay protocol: freeze identity dimensions, the three-view incident-baseline population rows, span category reductions, measured-run gate facts, the seventeen mandatory acceptance-scenario expectations, and the evidence envelope scenarios are projected against. Every durable record is a `FrozenContractModel` that digest-verifies its own content, and no field in this module can carry an approved numeric reduction threshold.

## Code Commentary

### Logic

Type-level vocabulary first: `MeasuredSpanCategory` aliases the R16 `TelemetrySpanKind` (line 32); `ReplayStratum` (lines 34-39) fixes the three-view strata (frozen-original / post-analysis-tail / incident-baseline / dated-supplement); `ScenarioState` (line 41) fixes green/red/refused/not-applicable; digest, id, and semantic-version patterns plus the seventeen r17-scenario ids follow (lines 43-71); `_require_semantic_text` (lines 73-77) backs `ReplayScenarioId` and `ProfileReference` (lines 79-81).

Frozen contract records:

- `ReplayScenarioExpectation` (lines 83-89) - one mandatory acceptance scenario (id, title, requirement, up to 16 views).
- `ScenarioOutcome` (lines 92-105) - machine outcome: a green carries no finding; any non-green carries one (validator lines 99-104).
- `ReplayLegIdentity` (lines 108-112) - baseline or treatment role bound to one freeze digest.
- `PopulationGeneration` (lines 115-132) - one immutable population row whose stratum fixes its generation window (validator lines 121-131).
- `SpanCategoryTotals` (lines 135-147) - union wall/active/count for one category, active never above wall (validator lines 142-146).
- `SpanReduction` (lines 150-175) - the closed nine-category reduction with gross wall/active, span count, and self-verifying `reductionDigest`; uniqueness plus length fix closed-set coverage, and span count must equal the per-category sum (validator lines 160-174).
- `ReplayFreezeInputChange` (lines 178-193) - one typed frozen-dimension change (source/profile/plan/configuration/population/runtime-toolchain-executor-image/machine-class/instrumentation/measurement-schema/fault-injection) with reason.
- `GateRunMeasurement` (lines 196-252) - per-gate measured facts: start evidence, last complete catalog and disposition, final decision, blocked/zero-start/invalidation flags, rail census, plus the `failedRails` / `blockedRails` / `terminalRails` properties; shape validator (lines 229-240) refuses inconsistent combinations.
- `RunMeasurement` (lines 255-286) - the deterministic per-run record: exact ordered Gates 1-5, admitted/refused, span reduction, finalization evidence, operation terminal class, certificate counts, self-verifying `measurementDigest`, and the `gate` accessor.

Evidence and profile records (imported re-exports): `ReplayRailPlacement` (lines 313-340, class-to-gate contract enforced), `ReplayDependencyEdge` (lines 343-347), `ReplayProfileSnapshot` (lines 350-359, repository fixture profile with `placements_for_gate`), and `ReplayScenarioEvidence` (lines 362-385, measured treatment/baseline, placements, peer placements, profiles, fault/companion/offender rails, dependency edges, change classes; with gate/rail/baseline placement helpers).

### Conventions

All records subclass `FrozenContractModel`, so extra fields are rejected; every digest-bearing record verifies its own content digest on validation. The measured-replay schema versions are fixed literals (`measured-replay-run/v1`, `measured-replay-span-reduction/v1`).

### Invariants And Boundaries

- Numeric reduction thresholds are deliberately absent: no field can carry an approved performance claim.
- A run measurement always carries the exact ordered Gates 1-5; a gate can never be both started and blocked or both admitted and refused.
- Span categories are unique and the reduction span count equals the per-category sum; category active time never exceeds its union wall.
- A green scenario outcome carries no findings; a non-green one always carries a typed finding.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured for this memory root. The governing task artifacts (the CCR-R17 approved replay protocol requirement packet and the 17_measured-replay-and-reduction leaf doc) define the mandatory scenario ids and evidence vocabulary; task artifact paths are not repo-relative citations, so these facts are recorded as prose here.

- The protocol fixes seventeen mandatory acceptance scenarios and refuses numeric reduction thresholds in the vocabulary. [1]

### Repo-Internal References

- Certification contracts share the closed immutable model base. [2]
- Semantic text is nonblank and unpadded. [3]
- Gate identity is the closed literal vocabulary 1 through 5. [4]
- Rail identity combines its declared id and version. [5]
- Certification refusals use the shared typed finding contract. [6]
- Span categories alias the R16 telemetry vocabulary, and replay catalogs reuse the telemetry rail records and counts. [7]
- Content digests follow the shared certification digest helper. [8]
- The public subpackage facade re-exports the full vocabulary. [9]
- The freeze owner consumes the population rows and change records defined here. [10]

### Cross-Repo References

No cross-repository implementation boundary is owned here.

The vocabulary stays repository-neutral; profiles enter by snapshot only.
