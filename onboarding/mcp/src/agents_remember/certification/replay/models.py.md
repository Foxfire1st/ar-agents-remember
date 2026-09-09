# mcp/src/agents_remember/certification/replay/models.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/certification/replay/models.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T22:23+02:00 |
| lastVerifiedCommitHash | `602143bd1d48226f4d53b83ff7c5002a695dcdff` |
| lastVerifiedCommitDate | 2026-09-09T00:26:24+02:00|
| governingOverview | `../overview.md` |

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

## Docs References

No Domain Documentation source is configured for this memory root. The governing task artifacts (the CCR-R17 approved replay protocol requirement packet and the 17_measured-replay-and-reduction leaf doc) define the mandatory scenario ids and evidence vocabulary; task artifact paths are not repo-relative citations, so these facts are recorded as prose here.

| Finding | Anchor | Source |
| --- | --- | --- |
| The protocol fixes seventeen mandatory acceptance scenarios and refuses numeric reduction thresholds in the vocabulary. | `_REPLAY_SCENARIO_IDS` | mcp/src/agents_remember/certification/replay/models.py:52-71 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Certification contracts share the closed immutable model base. | "class FrozenContractModel" | mcp/src/agents_remember/models/certification/base.py:30-33 |
| Semantic text is nonblank and unpadded. | "SemanticText = Annotated[str, AfterValidator(_require_semantic_text)]" | mcp/src/agents_remember/models/certification/base.py:27-27 |
| Gate identity is the closed literal vocabulary 1 through 5. | "GateId = Literal[1, 2, 3, 4, 5]" | mcp/src/agents_remember/models/certification/base.py:9-9 |
| Rail identity combines its declared id and version. | "class RailIdentity" | mcp/src/agents_remember/models/certification/base.py:36-42 |
| Certification refusals use the shared typed finding contract. | "class CertificationContractFinding" | mcp/src/agents_remember/certification/models.py:146-149 |
| Span categories alias the R16 telemetry vocabulary, and replay catalogs reuse the telemetry rail records and counts. | "class CatalogCounts(FrozenContractModel)"; "class CatalogRailRecord(FrozenContractModel)"; "MeasuredSpanCategory = TelemetrySpanKind" | mcp/src/agents_remember/certification/telemetry/models.py:296-307; mcp/src/agents_remember/certification/telemetry/models.py:310-317; mcp/src/agents_remember/certification/replay/models.py:20-32 |
| Content digests follow the shared certification digest helper. | `content_digest` | mcp/src/agents_remember/certification/digests.py:12-22 |
| The public subpackage facade re-exports the full vocabulary. | `__all__`; `ReplayFreeze`; `ReplayPopulation`; `SpanReduction`; `RunMeasurement`; `ReplayScenarioExpectation` | mcp/src/agents_remember/certification/replay/__init__.py:56-88 |
| The freeze owner consumes the population rows and change records defined here. | "class PopulationGeneration(FrozenContractModel)"; "class ReplayFreezeInputChange(FrozenContractModel)" | mcp/src/agents_remember/certification/replay/models.py:115-132; mcp/src/agents_remember/certification/replay/models.py:178-193 |

## Cross-Repo References

No cross-repository implementation boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| The vocabulary stays repository-neutral; profiles enter by snapshot only. | - | - |

## Update History

- 2026-09-09T02:49:53+02:00 — CCR-L38 bounded inherited claim reconciliation: repointed the freeze-owner claim to the unique population and change-record declarations in this model source. Source hashes: mcp/src/agents_remember/certification/replay/models.py=d03eb308bc966d86d9463fde0674f96b9574bf8ee305f9f32d736152b8ebf22b; verification metadata remains unchanged.

- 2026-09-09T02:49:53+02:00 — CCR-L38 bounded inherited claim reconciliation: replaced ambiguous type-use anchors with exact catalog declarations and the replay alias assignment. Source hashes: mcp/src/agents_remember/certification/replay/models.py=d03eb308bc966d86d9463fde0674f96b9574bf8ee305f9f32d736152b8ebf22b, mcp/src/agents_remember/certification/telemetry/models.py=482cc098f1f2cae2165a6beb91e524251af79a7c1bfc31071f63a928da255cf6; verification metadata remains unchanged.

- 2026-09-09T02:42:21+02:00 — CCR-L24 inherited/current-source reconciliation 2026-09-09: Re-read the current card claims against the frozen candidate source and repaired exact citation coordinates (CatalogCounts/MeasuredSpanCategory→20-32; freeze imports→22-26; ReplayFreezeInputChange use→74-79). Preserved claim prose; source-sha256=d03eb308bc966d86d9463fde0674f96b9574bf8ee305f9f32d736152b8ebf22b; verification metadata remains unchanged because commit-owned realization is pending.


- 2026-09-05T06:39:59+00:00 — L31 scoped citation curation against frozen ea359649: repaired anchor grammar and exact source coordinates while preserving the current behavioral claims. No content impact; source verification metadata was not advanced.

- 2026-09-04T22:23+02:00 - 260831-CCR-L17 Gate-5 memory pass: created this card for the new CCR-R17 measured-replay vocabulary delivered in code commit `e84c004c37a4bad082e1a7f1bdc4bd062282a185` (tree `f97c4969d7ddb93eed75c80a4936fc05fab8e2eb`).
