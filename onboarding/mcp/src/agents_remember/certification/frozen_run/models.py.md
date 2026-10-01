# mcp/src/agents_remember/certification/frozen_run/models.py

## Governing Overview

[Frozen certification run overview](overview.md)

## Purpose

Retains a complete admitted certification run, including its original creation evidence, before gate execution.

## Code Commentary

### Logic

`FrozenCertificationRun` stores the canonical registry, certification plan, repository profile and plan, admission manifest, provenance, and complete-record digest. Validation recompiles admission from those retained owners using the retained provenance and refuses any unequal original manifest. It then recomputes `runDigest` over every serialized field except the digest itself.

`freeze_certification_run` builds this record from the admitted lane and the supplied repository profile, copying the lane admission’s original provenance. It validates the constructed payload instead of manufacturing a new admission or replacing creation evidence.

### Conventions

Freeze the admitted lane with its original provenance; keep complete run identity separate from certificate semantic identity.

### Invariants And Boundaries

- The complete run digest includes provenance; gate-certificate semantic digests continue to exclude creation evidence and lifecycle generations.
- An internally consistent hash alone is insufficient: the original admission must equal the result of compilation from the retained inputs.
- This contract neither executes gates nor selects lifecycle records.

### Todos

None recorded.

## Evidence

### Docs References

No configured Domain Documentation source applies to this repository-owned contract.

No configured domain documentation applies.

### Repo-Internal References

- The retained model recompiles exact authority before validating its complete-record digest. [1]
- Freeze retains the lane admission and original provenance. [2]

### Cross-Repo References

No cross-repository implementation boundary is owned by this file.

No cross-repository reference is required.
