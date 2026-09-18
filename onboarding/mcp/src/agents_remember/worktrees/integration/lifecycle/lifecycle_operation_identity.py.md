# mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_identity.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_identity.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T00:53 |
| lastVerifiedCommitHash | `ea9cf0abeab4fe88961bda10b4f54d30266a9634` |
| lastVerifiedCommitDate | 2026-09-17T23:56:19+02:00|
| governingOverview | `overview.md` |

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

## Repo-Internal References

The following current source boundaries establish the ledger-retirement behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| `operation_state_fingerprint` hashes advancing code/memory contract cells without ledger commit identity. | `operation_state_fingerprint` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_identity.py:16-31 |
| `closeout_contract_sha256` hashes the exact canonical contract-publication text. | `closeout_contract_sha256` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_identity.py:34-38 |
| `operation_key` derives operation identity from canonical contract path, kind, and fingerprint. | `operation_key` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_identity.py:41-43 |

| Finding | Anchor | Source |
| --- | --- | --- |
| Stable fingerprint over advancing lifecycle cells. (`operation_state_fingerprint`) | `operation_state_fingerprint` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_identity.py:16-31 |

## Docs References

No external Domain Documentation source is configured for this slice. The current behavior is repository-owned and is supported by the source references below.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external source applies. | — | — |

## 260821-CLIVE-L1 Canonical Publication Identity

Closeout identity hashes normalized durable input and candidate provenance. Finalization identity now hashes the exact UTF-8 value returned by `contract_publication_text`, the same normalize/validate/serialize owner used by the writer and organizational reset. A no-op or verified-existing closeout can therefore retain its generation through exact publication without fabricated Git evidence.

## Current Landed Composition

`operation_key` is owned here: SHA-256 over the canonical resolved contract path, operation kind and fingerprint separated by NUL bytes. Callers import this identity directly; the coordinator no longer owns its implementation.

## Cross-Repo References

No separately configured cross-repository implementation governs this file; any external-memory repository is addressed by the task contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| No additional cross-repository evidence applies. | — | — |

## Update History

- 2026-09-15T00:53 UTC — LCA-L9 working-candidate curation: retired ledger Git authority in this file-specific boundary; preserved real Git and lifecycle safeguards and prior history. Source and diff reviewed, source-sha256=b6941df0add58b6ca0e0887b4bd2e929c26ab44daa3761a8105ab847aad0b2bd. Existing verification commit/date remain unchanged until an actual source commit is available; no test or acceptance claim.


- 2026-09-09T02:42:21+02:00 — CCR-L24 inherited/current-source reconciliation 2026-09-09: Re-read the current card purpose, logic, invariants, and cited route against the frozen candidate source; no content or route change was required, and the existing claim bytes remain accurate. source-sha256=31d7cc8d61facb7cbb9f199c437c99b12ae2780e0791a4e32921d01ac8dd90b3; verification metadata remains unchanged because commit-owned realization is pending.


- 2026-08-24T00:27+02:00 — 260821-CLIVE-L2 committed-route reconciliation: moved this preserved sidecar to mirror `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_identity.py`, repointed current source evidence and governing context, and verified the source at code commit `1d446724d099517f6f52d596b47827ae2391a2a4`.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: curated against accepted candidate tree `4241908c`; verification metadata remains pinned until governed closeout stamps the landed code commit.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: source moved to `mcp/src/agents_remember/worktrees/integration/lifecycle_operation_identity.py` (new package route); the citation fixer repointed in-body references; import paths updated inside the module. Verified at code commit e5cb139f.


- 2026-08-17T12:09+02:00 — 260815-DAG-L5: created onboarding for the lifecycle-operation state fingerprint.
