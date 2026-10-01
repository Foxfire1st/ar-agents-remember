# mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_identity.py

## Governing Overview

[Governing route overview](overview.md)

## Purpose

Derives a stable fingerprint of the lifecycle cells that change only when a sequential operation advances, so repair can prove the exact accepted contract state.

## Code Commentary

### Conventions

Accepted input, exact Git facts, and typed owner results stay distinct from disposable projections.

### Todos

None recorded for the ledger-retirement boundary.

### Logic

The contract-state fingerprint includes the real code and memory content outputs for closeout and integration, together with bases, status, and cleanup. Retired ledger commit fields are absent, and consumer-cache changes cannot alter sequential-operation identity.

`operation_state_fingerprint` serializes the contract's base commits, closeout/integration status, candidate commits, integrated commits, and cleanup state into a sorted JSON payload and SHA-256 hashes it.

#### Invariants And Boundaries

- Only lifecycle cells that advance monotonically with a sequential operation are hashed.
- The fingerprint is consumed by organizational completion repair to reject a contract that no longer matches its accepted operation state.

## Evidence

### Repo-Internal References

The following current source boundaries establish the ledger-retirement behavior.

- `operation_state_fingerprint` hashes advancing code/memory contract cells without ledger commit identity. [1]
- `closeout_contract_sha256` hashes the exact canonical contract-publication text. [2]
- `operation_key` derives operation identity from canonical contract path, kind, and fingerprint. [3]

- Stable fingerprint over advancing lifecycle cells. (`operation_state_fingerprint`) [4]

### Docs References

No external Domain Documentation source is configured for this slice. The current behavior is repository-owned and is supported by the source references below.

No configured external source applies.

### Cross-Repo References

No separately configured cross-repository implementation governs this file; any external-memory repository is addressed by the task contract.

No additional cross-repository evidence applies.

## 260821-CLIVE-L1 Canonical Publication Identity

Closeout identity hashes normalized durable input and candidate provenance. Finalization identity now hashes the exact UTF-8 value returned by `contract_publication_text`, the same normalize/validate/serialize owner used by the writer and organizational reset. A no-op or verified-existing closeout can therefore retain its generation through exact publication without fabricated Git evidence.

## Current Landed Composition

`operation_key` is owned here: SHA-256 over the canonical resolved contract path, operation kind and fingerprint separated by NUL bytes. Callers import this identity directly; the coordinator no longer owns its implementation.
