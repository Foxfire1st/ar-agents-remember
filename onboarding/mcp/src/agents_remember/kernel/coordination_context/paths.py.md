# mcp/src/agents_remember/kernel/coordination_context/paths.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/kernel/coordination_context/paths.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T20:57+02:00                     |
| lastVerifiedCommitHash | `c310611a6678051c9e37b912c522b367530c0686` |
| lastVerifiedCommitDate | 2026-05-26T02:17:03+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[coordination_context overview](overview.md)

## Purpose

`paths.py` owns path and topology primitives for locating code repositories,
coordination roots, memory roots, settings files, and onboarding roots.

## Code Commentary

### Logic

The module detects installed coordinator roots, derives the source-development
default coordination root, normalizes settings scalars and relative paths,
finds code repositories under a workspace, and infers memory roots/settings
paths from either explicit settings or onboarding roots.

### Invariants And Boundaries

- Source-checkout `.env` and `.env.example` are not resolver authority.
- Internal memory resolves under `<code-repository-root>/ar-memory`; external
  memory resolves under `<coordination-root>/memory-repos/ar-<repo>`.
- Path helpers do not parse settings content or inspect Git.

## Docs References

No external documentation is needed for this package-local path policy.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation is needed. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Resolver selection uses these path primitives for topology and settings discovery. | resolver selection | [resolver.py](agents-remember-md/mcp/src/agents_remember/kernel/coordination_context/resolver.py) |
| Worktree support tests cover installed-runtime root detection and `.env` non-authority. | path policy tests | [test_worktree_support.py](agents-remember-md/mcp/tests/test_worktree_support.py) |

## Cross-Repo References

No cross-repository evidence is needed for local path policy.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-25T20:57+02:00: Created by extracting C-08 path and topology helpers from the monolithic resolver.
