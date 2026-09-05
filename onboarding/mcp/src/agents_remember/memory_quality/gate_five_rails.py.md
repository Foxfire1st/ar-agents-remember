# mcp/src/agents_remember/memory_quality/gate_five_rails.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/gate_five_rails.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-05T06:14:14+00:00 |
| lastVerifiedCommitHash | `668d710bf2a9898fb706614163462ff346d986b7` |
| lastVerifiedCommitDate | 2026-09-05T02:45:47+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Governing route overview](overview.md)

## Purpose

Projects the memory domain's complete final catalog into deterministic R11 Gate-5 rail definitions for certification admission.

## Code Commentary

### Logic

gate_five_memory_rails creates one enforcing memory-quality rail per final-catalog item. Identity/version follow the catalog; ordering uses catalog position plus item id. Each rail belongs to memory-domain authority, assigns correction to memory-curator, selects the requested profile id, and declares bounded JSON evidence through the memory-final-certification adapter.

The default configuration digest binds final-catalog version, checker-registry version and the exact catalog population. Callers can supply an already-bound configuration digest explicitly. The function returns sorted definitions and performs no memory reads, mutation, coherence publication or certificate issuance.

### Conventions

Preserve the memory-domain owner and catalog-derived identities. Do not duplicate a hand-maintained final-catalog list in worktree code.

### Invariants And Boundaries

- Every definition is Gate 5 and enforcing.
- The checker registry and catalog changes invalidate the default configuration digest.
- The memory-checker URI is an execution/evidence identifier, not proof that the checker ran.
- No output artifact or green result is synthesized by deriving rails.

### Todos

The final-catalog execution and R21 Gate-5 publication still require a production caller; this file supplies only the definitions.

## Docs References

No external Domain Documentation source is configured for this repository. This card records repository-owned behavior from the source references below; no external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| External domain documentation is not configured. | N/A | N/A |

## Repo-Internal References

The cited source establishes the current contracts and boundaries described above. Source verification is documentation evidence, not acceptance of the implementation.

| Finding | Anchor | Source |
| --- | --- | --- |
| Catalog-to-rail projection and deterministic order | `gate_five_memory_rails` | mcp/src/agents_remember/memory_quality/gate_five_rails.py:36-90 |
| Configuration digest binds catalog and registry | `_catalog_configuration_digest` | mcp/src/agents_remember/memory_quality/gate_five_rails.py:93-101 |

## Cross-Repo References

No separate cross-repository protocol is established by this file. The configured cross-repository allowance is empty; no external source is relied upon here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository evidence is required for these file-local claims. | N/A | N/A |

## Update History

- 2026-09-05T06:14:14+00:00 — Created the Gate-5 rail-population account and explicitly separated definition construction from memory execution.
