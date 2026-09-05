# mcp/src/agents_remember/application/worktree_services.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/worktree_services.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-05T06:14:14+00:00 |
| lastVerifiedCommitHash | `668d710bf2a9898fb706614163462ff346d986b7` |
| lastVerifiedCommitDate | 2026-09-05T02:45:47+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Governing route overview](overview.md)

## Purpose

Builds the default service bundle that lets lower-level worktree operations use provider lifecycle, memory checking, citation guards and Gate-5 rail definitions without importing those higher-level packages.

## Code Commentary

### Logic

ProviderLifecycleAdapter translates the worktree-owned setup specification into provider-owned requests and delegates setup/status/teardown. MemoryQualityAdapter delegates check-group discovery, drift context and memory checks. CitationGuardAdapter obtains the memory-quality citation cache guard.

CertificationMemoryRailsAdapter delegates the admitted selection id to gate_five_memory_rails. build_default_worktree_services installs this adapter beside the existing three services; the re-exported bind_worktree_services installs the resulting bundle when the MCP/CLI composition calls it.

### Conventions

Keep imports of providers and memory_quality at this composition boundary. Worktree modules consume protocols from worktrees.services; they do not locate those packages dynamically or construct fallback implementations.

### Invariants And Boundaries

- The bundle wires dependencies; it does not execute a certification gate by being built.
- Supplying Gate-5 rail definitions does not invoke full memory certification or publish coherence.
- Default composition must bind the rail adapter before the Agents Remember certification-record seam requests it.
- Preserve provider teardown and citation-guard ownership while extending the bundle.

### Todos

The rail-definition adapter is implemented; the complete R07/R08 production execution path remains a separate integration obligation.

## Docs References

No external Domain Documentation source is configured for this repository. This card records repository-owned behavior from the source references below; no external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| External domain documentation is not configured. | N/A | N/A |

## Repo-Internal References

The cited source establishes the current contracts and boundaries described above. Source verification is documentation evidence, not acceptance of the implementation.

| Finding | Anchor | Source |
| --- | --- | --- |
| Provider translation/delegation | `ProviderLifecycleAdapter` | mcp/src/agents_remember/application/worktree_services.py:25-129 |
| Memory-rail and memory-quality adapters | `CertificationMemoryRailsAdapter`; `MemoryQualityAdapter` | mcp/src/agents_remember/application/worktree_services.py:132-174 |
| Citation guard, complete default bundle and binding | `CitationGuardAdapter`; `build_default_worktree_services`; `bind_worktree_services` | mcp/src/agents_remember/application/worktree_services.py:177-208 |

## Cross-Repo References

No separate cross-repository protocol is established by this file. The configured cross-repository allowance is empty; no external source is relied upon here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository evidence is required for these file-local claims. | N/A | N/A |

## Update History

- 2026-09-05T06:14:14+00:00 — Extended the preserved dependency-composition account with the Gate-5 rail port and its non-execution boundary.

- 2026-08-08T14:38+02:00 — 260731-EFA-L9 curator: created for the composition-root services
  bundle. Verification metadata pinned until closeout stamps the L9 code commit.
