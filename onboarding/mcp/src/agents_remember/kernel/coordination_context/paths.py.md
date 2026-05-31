# mcp/src/agents_remember/kernel/coordination_context/paths.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/kernel/coordination_context/paths.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-31T12:50+02:00                     |
| lastVerifiedCommitHash | `c20a3292e667d227a3be0c1fb276f8a701df814f` |
| lastVerifiedCommitDate | 2026-05-31T14:17:11+02:00|
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
resolves a code repository by absolute path or by a direct
`<workspace-root>/<name>` join, and infers memory roots/settings paths from
either explicit settings or onboarding roots. `find_code_repository_root` no
longer scans `workspace_root.iterdir()` for name matches, so it cannot raise the
"multiple code repositories" ambiguity error; a non-direct hit yields only the
"was not found" `ValueError`.

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

- 2026-05-31T12:50+02:00 — `find_code_repository_root` dropped its `workspace_root.iterdir()` name-match scan and the "multiple code repositories" `ValueError`, leaving only absolute-path and direct-join resolution; corrected the Logic section to describe direct-join-only resolution and the removed ambiguity error (1.0.0 review remediation).
- 2026-05-25T20:57+02:00: Created by extracting C-08 path and topology helpers from the monolithic resolver.
