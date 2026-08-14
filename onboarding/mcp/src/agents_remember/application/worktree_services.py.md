# mcp/src/agents_remember/application/worktree_services.py

| Field                  | Value                                                         |
| ---------------------- | ------------------------------------------------------------- |
| repository             | agents-remember                                               |
| path                   | `mcp/src/agents_remember/application/worktree_services.py`     |
| doc_type               | `file-level-onboarding`                                       |
| lastUpdated            | 2026-08-08T14:38+02:00                                        |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`                    |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `overview.md`                                                 |

## Governing Overview

[application overview](overview.md)

## Purpose

`application/worktree_services.py` (260731-EFA-L9) composes the default `WorktreeServices` bundle
for the MCP/CLI entry points: the provider lifecycle adapter, the memory-quality gate adapter,
and the citation guard adapter, bound at the composition root so the lower-ranked worktrees
package never imports providers/memory-quality/code-quality.

## Code Commentary

### Logic

`ProviderLifecycleAdapter` (cit:(["class ProviderLifecycleAdapter"], mcp/src/agents_remember/application/worktree_services.py:24-24)) adapts the application provider
runtime to the `ProviderLifecyclePort`; `MemoryQualityAdapter` (cit:(["class MemoryQualityAdapter"], mcp/src/agents_remember/application/worktree_services.py:131-131))
adapts the memory-quality drift check; `CitationGuardAdapter`
(cit:(["class CitationGuardAdapter"], mcp/src/agents_remember/application/worktree_services.py:169-169)) adapts the citation source guard.
`build_default_worktree_services` (cit:([`build_default_worktree_services`], mcp/src/agents_remember/application/worktree_services.py:184-189)) returns the bound bundle
with `__all__` exporting the public surface.

### Invariants And Boundaries

- Composition root only: services are bound here and consumed through `worktrees.services`; the
  worktrees package must stay import-free of the adapted packages.

### Todos

No known follow-up.

## Docs References

No external/domain documentation is configured.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The bound bundle implements the worktrees service ports. | `ProviderLifecyclePort` | mcp/src/agents_remember/worktrees/services.py:42-42 |
| The provider adapter delegates to the provider runtime moved from worktrees. | `launch_provider_setup` | mcp/src/agents_remember/application/provider_runtime.py:73-73 |

## Cross-Repo References

No cross-repository implementation participates.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-08T14:38+02:00 — 260731-EFA-L9 curator: created for the composition-root services
  bundle. Verification metadata pinned until closeout stamps the L9 code commit.
