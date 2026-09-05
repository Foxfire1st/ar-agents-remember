# mcp/src/agents_remember/worktrees/services.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/services.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-05T06:14:14+00:00 |
| lastVerifiedCommitHash | `668d710bf2a9898fb706614163462ff346d986b7` |
| lastVerifiedCommitDate | 2026-09-05T02:45:47+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Governing route overview](overview.md)

## Purpose

Defines the service protocols and process-local binding consumed by worktree lifecycle code. It preserves package layering while allowing application composition to provide concrete provider, memory and citation services.

## Code Commentary

### Logic

WorktreeServices carries provider_lifecycle, memory_quality, citation_guard and the optional certification_memory_rails port. CertificationMemoryRailsPort returns R11 RailDefinition objects for an admitted profile selection. ProviderSetupRequestSpec keeps higher-level provider option objects opaque to worktrees.

bind_worktree_services assigns the composed bundle, reset_worktree_services clears it for tests/teardown, and worktree_services refuses when no bundle is bound. The getter does not lazily create dependencies. The optional rail field permits bundles without that capability, but the Agents Remember certification-record consumer explicitly refuses if it is missing.

### Conventions

Protocols are the downward dependency boundary. Adapter implementations live above worktrees; module-level binding is explicit process composition.

### Invariants And Boundaries

- Worktrees must not import providers or memory_quality to satisfy a missing service.
- An unbound service bundle is an error, not a signal to invent a default.
- Rail population is data authority; this port does not run Gate 5.
- The citation terminal guard retains its publication/rollback callback boundary.

### Todos

Absence of the optional rail port must remain visible at the consumer that requires it.

## Docs References

No external Domain Documentation source is configured for this repository. This card records repository-owned behavior from the source references below; no external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| External domain documentation is not configured. | N/A | N/A |

## Repo-Internal References

The cited source establishes the current contracts and boundaries described above. Source verification is documentation evidence, not acceptance of the implementation.

| Finding | Anchor | Source |
| --- | --- | --- |
| Citation, provider, memory-rail and memory-check protocols | `CitationGuardPort`; `ProviderLifecyclePort`; `CertificationMemoryRailsPort`; `MemoryQualityPort` | mcp/src/agents_remember/worktrees/services.py:21-116 |
| Service bundle and opaque provider setup specification | `WorktreeServices`; `ProviderSetupRequestSpec` | mcp/src/agents_remember/worktrees/services.py:119-144 |
| Explicit binding, reset and unbound refusal | `bind_worktree_services`; `reset_worktree_services`; `worktree_services` | mcp/src/agents_remember/worktrees/services.py:147-185 |

## Cross-Repo References

No separate cross-repository protocol is established by this file. The configured cross-repository allowance is empty; no external source is relied upon here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository evidence is required for these file-local claims. | N/A | N/A |

## Update History

- 2026-09-05T06:14:14+00:00 — Documented the new rail-population port alongside the preserved layering and explicit-binding invariants.

- 2026-08-08T14:38+02:00 — 260731-EFA-L9 curator: created for the worktrees service-port
  surface added by the layering cleanup. Verification metadata pinned until closeout stamps the
  L9 code commit.
