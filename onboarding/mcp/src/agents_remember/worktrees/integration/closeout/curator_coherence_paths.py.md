# mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence_paths.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence_paths.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-27T05:02:28+00:00 |
| lastVerifiedCommitHash | `a0b2c18d2b8d08ac1242a13f65bde900a190df7a`|
| lastVerifiedCommitDate | 2026-09-27T07:57:14+02:00|
| governingOverview | `mcp/src/agents_remember/worktrees/integration/closeout/overview.md` |

## Governing Overview

[governing route overview](overview.md)

## Purpose

Own the existing curator artifact layout and explicit code, memory and task evidence namespaces in one acyclic module.

## Code Commentary

### Logic

The leaf external-memory contract selects the stable authority, content-addressed generations, attempt snapshots and durable attestation copies under the existing task report root. Structural applicability does not require the old worktree to remain physically present.

Evidence references name exactly one admitted namespace and relative file. Empty, absolute, root-only, escaping or missing paths refuse. Resolution is shared by live input checking and evidence publication; retained reads use the durable addresses their owners recorded.

### Conventions

Use the existing typed owners and exact recorded identities. Keep operation evidence and candidate provenance in task notes.

### Invariants And Boundaries

Path resolution grants no currentness or semantic approval. No filename scan, alternate root or recreated worktree substitutes for the exact reference.

### Todos

None recorded.

## Docs References

No Domain Documentation source is configured. The repository declarations below support this contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain source could be checked. | — | — |

## Repo-Internal References

The cited owners carry the behavior and failure boundaries described above.

| Finding | Anchor | Source |
| --- | --- | --- |
| The existing artifact layout is derived from one leaf contract. | `curator_coherence_paths` | mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence_paths.py:10-19 |
| Applicability is structural and does not demand a live directory. | `require_leaf_external_memory` | mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence_paths.py:22-34 |
| Explicit namespaces and confinement are enforced once. | `resolve_curator_evidence_ref` | mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence_paths.py:37-68 |

## Cross-Repo References

No separate repository supplies this contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository reference is required. | — | — |

## Update History

- 2026-09-27T05:02:28+00:00 — Created this source-mirrored card for the durable assessment-history boundary. Verification hash/date remain blank until normal closeout records the actual accepted code commit.
