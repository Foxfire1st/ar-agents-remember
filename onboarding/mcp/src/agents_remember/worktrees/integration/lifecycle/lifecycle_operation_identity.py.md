# mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_identity.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_identity.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T00:27+02:00 |
| lastVerifiedCommitHash | `1d446724d099517f6f52d596b47827ae2391a2a4` |
| lastVerifiedCommitDate | 2026-08-24T00:21:10+02:00 |
| governingOverview | `../overview.md` |

## Governing Overview

[governing overview](../overview.md)

## Purpose

Derives a stable fingerprint of the lifecycle cells that change only when a sequential operation advances, so repair can prove the exact accepted contract state.

## Code Commentary

### Logic

`operation_state_fingerprint` serializes the contract's base commits, closeout/integration status, candidate commits, integrated commits, and cleanup state into a sorted JSON payload and SHA-256 hashes it.

### Invariants And Boundaries

- Only lifecycle cells that advance monotonically with a sequential operation are hashed.
- The fingerprint is consumed by organizational completion repair to reject a contract that no longer matches its accepted operation state.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Stable fingerprint over advancing lifecycle cells. | `operation_state_fingerprint` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_identity.py:11-28 |

## Documentation References

No configured domain-documentation or cross-repository source applies to this file.

## 260821-CLIVE-L1 Canonical Publication Identity

Closeout identity hashes normalized durable input and candidate provenance. Finalization identity now hashes the exact UTF-8 value returned by `contract_publication_text`, the same normalize/validate/serialize owner used by the writer and organizational reset. A no-op or verified-existing closeout can therefore retain its generation through exact publication without fabricated Git evidence.

## Current Landed Composition

`operation_key` is owned here: SHA-256 over the canonical resolved contract path, operation kind and fingerprint separated by NUL bytes. Callers import this identity directly; the coordinator no longer owns its implementation.

## Update History

- 2026-08-24T00:27+02:00 — 260821-CLIVE-L2 committed-route reconciliation: moved this preserved sidecar to mirror `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_identity.py`, repointed current source evidence and governing context, and verified the source at code commit `1d446724d099517f6f52d596b47827ae2391a2a4`.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: curated against accepted candidate tree `4241908c`; verification metadata remains pinned until governed closeout stamps the landed code commit.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: source moved to `mcp/src/agents_remember/worktrees/integration/lifecycle_operation_identity.py` (new package route); the citation fixer repointed in-body references; import paths updated inside the module. Verified at code commit e5cb139f.


- 2026-08-17T12:09+02:00 — 260815-DAG-L5: created onboarding for the lifecycle-operation state fingerprint.
## Docs References

No external Domain Documentation source is configured for this internal route; task `260821-CLIVE-L1` and the cited repository source/tests govern this curation.

## Cross-Repo References

This file owns no ambient cross-repository authority. Any external-memory repository it reaches remains explicitly contract-addressed.
