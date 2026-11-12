# mcp/src/agents_remember/certification/replay/freeze.py

## Governing Overview

[Certification contract overview](../overview.md)

## Purpose

Owns the CCR-R17 (leaf 260831-CCR-L17) replay freeze identity, incident population, and pair comparability contracts. A replay leg freezes the exact source revision, candidate digest, R22 profile, R11 plan, configuration, runtime/toolchain/executor/image tuple, machine class, instrumentation posture, and measurement schema before it runs; baseline and treatment are comparable only while those frozen dimensions agree. Observation metadata is deliberately excluded from the frozen identity and can never invalidate a pair. The module also owns the append-only three-view incident population (frozen original generations 1-8, post-analysis tail 9-13, dated supplements 14+) where supplements never enter the primary denominator.

## Code Commentary

### Logic

Frozen records in the certification-domain style, each digest-verifying its own content:

- `ReplayFreezeInput` (lines 39-54) - the exact frozen inputs one replay leg ran under: source revision, candidate digest, profile identity/digest, plan digest, configuration digest, runtime identity, toolchain/executor/image digests, machine class, instrumentation-only posture, and measurement schema. Digest fields enforce the 64-hex pattern and profile identity the lowercase id pattern.
- `ReplayFreeze` (lines 57-71) - one digest-bound freeze whose `freezeDigest` is the content digest of the schema-versioned input (verifier lines 63-70); the literal `measured-replay-freeze/v1` schemaVersion fixes the record type.
- `ReplayComparabilityReport` (lines 74-90) - the comparability verdict for one baseline/treatment pair: comparable only with no change or finding; an incomparable pair requires a typed change or finding (shape validator lines 84-89).
- `ReplayPopulation` (lines 93-116) - the append-only population record with unique generations, digest self-verification, and the per-stratum accessor.

Compiler helpers follow:

- `compile_replay_freeze` (lines 119-124) and `freeze_digest` (lines 127-131) build a freeze and its digest from validated inputs.
- `compare_replay_freezes` (lines 134-157) refuses the pair on any frozen-dimension change: it unions `_identity_changes` (lines 160-225, source/profile/plan/configuration/machine-class/instrumentation/measurement-schema dimensions) with `_runtime_changes` (lines 228-250, the runtime/toolchain/executor/image tuple as one dimension) and produces typed `replay-pair-incomparable` findings.
- `require_comparable_replay_pair` (lines 253-264) raises a `CertificationContractError` for an incomparable pair and never for observation metadata.
- `compile_replay_population` (lines 267-278) orders rows by generation/stratum before digesting; `population_denominator` (lines 281-287) returns only frozen-original and post-analysis-tail generations; the three row accessors (lines 290-308) split the three views.
- `require_append_only_population` (lines 311-336) refuses successor generations that rewrite a frozen baseline row; successors may only append dated supplements at generation greater than the base max.

### Conventions

All records subclass `FrozenContractModel` so extra fields are rejected; every digest-bearing record verifies its own content digest on validation. `FROZEN_DENOMINATOR_LIMIT` (line 36) fixes the frozen plus tail ceiling at generation 13.

### Invariants And Boundaries

- A comparable pair carries no change and no finding; an incomparable pair always names a typed change or finding.
- Observation metadata (review/journal/approval rows) is not part of the frozen identity and cannot make a pair incomparable.
- The population is append-only: dated supplements (14+) are qualitative only and excluded from the denominator; frozen baseline rows are never rewritten.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured for this memory root. The governing task artifacts (the CCR-R17 approved replay protocol requirement packet and the 17_measured-replay-and-reduction leaf doc) fix the frozen-dimension list and the three-view population; task artifact paths are not repo-relative citations, so these facts are recorded as prose here.

- The exact frozen inputs one replay leg ran under. [1]
- Refuse the pair when any frozen dimension changed between the legs. [2]

### Repo-Internal References

- Certification contracts share the closed immutable model base. [3]
- Semantic text is nonblank and unpadded. [4]
- Content digests follow the shared certification digest helper. [5]
- Incomparability findings use the shared typed finding contract. [6]
- Pair refusal raises the shared certification contract error. [7]
- The population row vocabulary lives in the replay models module. [8]
- The public subpackage facade re-exports every freeze owner. [9]

### Cross-Repo References

No cross-repository implementation boundary is owned here.

Freeze identity is repository-neutral and names profiles/plans only by digest.
