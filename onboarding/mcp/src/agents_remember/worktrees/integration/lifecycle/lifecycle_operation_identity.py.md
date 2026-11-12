# mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_identity.py

## Governing Overview

[Governing route overview](overview.md)

## Purpose

Owns stable lifecycle fingerprints and operation keys, plus the shared identity predicates for completed and retired direct-landing records.

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

## Operation Identity And Direct Ownership

`operation_key` is owned here: SHA-256 over the canonical resolved contract path, operation kind and fingerprint separated by NUL bytes. Callers import this identity directly; the coordinator no longer owns its implementation.

`direct_landing_identity` recognises only a doorless direct record whose fingerprint derives its stored operation key. `completed_direct_owner` additionally requires active disposition and completed status. When an expected generation is supplied, its counter must match; production control pins that counter upstream. The record model normalises an omitted stored generation to 1, so absence is not a reachable predicate state. Both the control offer and completed-disposition check consume this same predicate, not parallel door-based identity checks. `retired_direct_record` is the separate idempotent retire re-answer.

- Doorless direct identity is bound to the same operation-key derivation as admission. [5]
- Completed owner and idempotent retired-record checks use the record itself. [6]
- The retired-record check recognises only completed doorless direct records. [7]
