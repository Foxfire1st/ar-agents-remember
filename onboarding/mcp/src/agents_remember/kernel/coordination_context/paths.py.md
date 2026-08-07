# mcp/src/agents_remember/kernel/coordination_context/paths.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/kernel/coordination_context/paths.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-31T12:50+02:00                     |
| lastVerifiedCommitHash | `b252c42cca200933d5c9c36e26de47a526a569ce` |
| lastVerifiedCommitDate | 2026-08-07T23:58:52+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation is needed. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Resolver selection uses these path primitives for topology and settings discovery. | `resolve_coordination_context`, `_selection_roots`, `_selection_from_settings` | mcp/src/agents_remember/kernel/coordination_context/resolver.py:77-86; mcp/src/agents_remember/kernel/coordination_context/resolver.py:89-104; mcp/src/agents_remember/kernel/coordination_context/resolver.py:151-164 |
| Worktree support tests cover installed-runtime root detection and `.env` non-authority. | `test_resolver_uses_installed_runtime_root_as_coordination_root`, `test_resolver_ignores_dot_env_example_at_runtime` | mcp/tests/test_worktree_support_tests_2.py:799-819; mcp/tests/test_worktree_support_tests_2.py:821-842 |

## Cross-Repo References

No cross-repository evidence is needed for local path policy.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-08-04T18:40+02:00 — 260731-EFA-L6 S18-B18 curator: re-anchored the worktree-support test
  row after the source file shifted: `test_resolver_uses_installed_runtime_root_as_coordination_root`
  at 2326-2346 and `test_resolver_ignores_dot_env_example_at_runtime` at 2348-2369. Zero findings
  remain.

- 2026-08-02T20:47+02:00 — 260731-EFA-L6 W2-B01 curator: anchored 2 citation rows; scoped citation fixing regenerated the source ranges.
- 2026-05-31T12:50+02:00 — `find_code_repository_root` dropped its `workspace_root.iterdir()` name-match scan and the "multiple code repositories" `ValueError`, leaving only absolute-path and direct-join resolution; corrected the Logic section to describe direct-join-only resolution and the removed ambiguity error (1.0.0 review remediation).
- 2026-05-25T20:57+02:00: Created by extracting `c-08-ar-coordination-context-resolver` skill path and topology helpers from the monolithic resolver.
