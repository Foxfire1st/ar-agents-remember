# mcp/src/agents_remember/worktrees/services.py

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `mcp/src/agents_remember/worktrees/services.py`              |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-08T14:38+02:00                                      |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`                  |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `overview.md`                                               |

## Governing Overview

[worktree modules overview](overview.md)

## Purpose

`worktrees/services.py` (260731-EFA-L9) declares the service ports the worktree lifecycle needs
from packages above it (providers, memory quality, code quality) and the `WorktreeServices`
bundle that binds them at the composition root. Worktrees ranks below those packages, so the
lifecycle modules never import them.

## Code Commentary

### Logic

`TerminalGuard`, `CitationGuardPort`, `ProviderLifecyclePort` (cit:(["class ProviderLifecyclePort"], mcp/src/agents_remember/worktrees/services.py:42-42)), and
"class MemoryQualityPort(Protocol):" are the protocols; "class WorktreeServices:" (cit:(["class WorktreeServices:"], mcp/src/agents_remember/worktrees/services.py:107-107)) is the frozen bundle.
`bind_worktree_services`/`reset_worktree_services` manage the process-global binding and
`worktree_services()` retrieves it, raising `WorktreeServicesUnboundError`
(cit:(["class WorktreeServicesUnboundError"], mcp/src/agents_remember/worktrees/services.py:136-136)) when unbound.

### Invariants And Boundaries

- Ports live in worktrees; implementations live in application (composition root). Do not import
  providers/memory-quality/code-quality from this package.

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
| The default bundle is built in the application layer. | `build_default_worktree_services` | mcp/src/agents_remember/application/worktree_services.py:184-189 |

## Cross-Repo References

No cross-repository implementation participates.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-08T14:38+02:00 — 260731-EFA-L9 curator: created for the worktrees service-port
  surface added by the layering cleanup. Verification metadata pinned until closeout stamps the
  L9 code commit.
