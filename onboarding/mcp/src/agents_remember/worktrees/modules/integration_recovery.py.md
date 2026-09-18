# mcp/src/agents_remember/worktrees/modules/integration_recovery.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/modules/integration_recovery.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T00:58 |
| lastVerifiedCommitHash | `ea9cf0abeab4fe88961bda10b4f54d30266a9634` |
| lastVerifiedCommitDate | 2026-09-17T23:56:19+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Governing route overview](overview.md)

## Purpose

Proves exact ref convergence and external-memory output identity before integration finalization resumes.

## Code Commentary

### Logic

Recovery proves the actual memory-content commit. A standalone memory worktree must be clean outside root `memory.md`; series recovery reads its named memory branch directly. The cache is neither read nor matched against a pairing before finalization.

`classify_convergent_recovery_refs` delegates to the canonical integration-ref classifier and escalates conflicts as typed decision errors. `prove_external_memory_recovery` reads the task memory branch for a series, or requires a standalone memory worktree clean outside the cache and reads its HEAD, then requires that exact commit to equal the journaled memory-content commit.

### Conventions

Recovery classifies current Git facts; it does not repair refs or infer equivalence.

#### Invariants And Boundaries

- Conflicting refs require a decision rather than a silent fallback.
- Standalone memory recovery requires a worktree clean outside root `memory.md`.
- The recovered memory head must exactly name the recorded memory-content commit.

### Todos

None recorded.

## Docs References

No external Domain Documentation source is configured for this slice. The current behavior is repository-owned and is supported by the source references below.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external source applies. | — | — |

## Repo-Internal References

The following current source boundaries establish the ledger-retirement behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| `prove_external_memory_recovery` requires exact accepted memory HEAD/ref and ignores only root cache dirtiness. | `prove_external_memory_recovery` | mcp/src/agents_remember/worktrees/modules/integration_recovery.py:28-49 |
| `classify_convergent_recovery_refs` delegates exact ref classification and preserves typed conflicts. | `classify_convergent_recovery_refs` | mcp/src/agents_remember/worktrees/modules/integration_recovery.py:18-25 |

| Finding | Anchor | Source |
| --- | --- | --- |
| Convergent refs are classified by the canonical authority classifier and conflicts stay typed. (`classify_convergent_recovery_refs`) | `classify_convergent_recovery_refs` | mcp/src/agents_remember/worktrees/modules/integration_recovery.py:18-25 |
| External-memory proof requires the exact task-memory head to equal the journaled memory-content commit. (`prove_external_memory_recovery`) | `prove_external_memory_recovery` | mcp/src/agents_remember/worktrees/modules/integration_recovery.py:28-49 |

## Cross-Repo References

No cross-repository boundary is owned here; the external memory repository is contract-addressed runtime data.

| Finding | Anchor | Source |
| --- | --- | --- |
| No additional cross-repository evidence applies. | — | — |

## Update History

- 2026-09-15T00:58 UTC — Rechecked the formatted L9 working candidate and rebound current references after source cleanup; source-sha256=7113ac73eca2a2fca328f5b7341a5e90efe8340f10d3248a276ba09bbe5186ba. The older working-candidate snapshot and verification provenance are retained.

- 2026-09-15T00:53 UTC — LCA-L9 working-candidate curation: retired ledger Git authority in this file-specific boundary; preserved real Git and lifecycle safeguards and prior history. Source and diff reviewed, source-sha256=80117c56b42ec8813597c12d68f465336eb7d5bf84d74ecc00315981ad6e990f. Existing verification commit/date remain unchanged until an actual source commit is available; no test or acceptance claim.


- 2026-08-24T00:27+02:00 — 260821-CLIVE-L2 committed-route reconciliation: created the missing strict sidecar and verified it at code commit `1d446724d099517f6f52d596b47827ae2391a2a4`.
