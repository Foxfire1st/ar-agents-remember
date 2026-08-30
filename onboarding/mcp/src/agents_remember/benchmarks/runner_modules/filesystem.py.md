# mcp/src/agents_remember/benchmarks/runner_modules/filesystem.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/benchmarks/runner_modules/filesystem.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-22T10:39+02:00 |
| lastVerifiedCommitHash | `346507af24396ab7b491e02511c4af006ccd3dc5`
| lastVerifiedCommitDate | 2026-08-30T07:51:57+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[runner_modules overview](overview.md)

## Purpose

Filesystem mutation helpers for benchmark workspace setup and runtime asset
exposure.

## Code Commentary

### Logic

`filesystem.py` owns safe path removal, copying packaged
runtime/provider assets, rendering root markers, creating benchmark-local
coordination scaffolding, and exposing skills into the benchmark
`.codex/skills` tree. Cross-platform long-path normalization (the Windows
`\\?\` prefix logic) is no longer inlined here; both `removable_path` and the
copy helpers delegate to the shared `long_path` helper imported from
`agents_remember.install.assets`. The benchmark runtime scaffold creates central
`logs/mcp` and `logs/providers/...` directories alongside provider data and
runner roots.

### Invariants And Boundaries

- Copy/remove helpers are benchmark workspace mechanics, not general repository mutation policy.
- Benchmark workspaces should mirror the MCP runtime log layout with central
  `logs/` directories instead of legacy `providers/logs`.
- Skill exposure remains copy-only or disabled; no shell/symlink installer fallback belongs here.

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The public benchmark facade re-exports this module's public functions and classes for compatibility. | "from agents_remember.benchmarks.runner_modules.filesystem import *" | mcp/src/agents_remember/benchmarks/runner.py:18-18 |
| The route-local overview summarizes how this module fits into the benchmark runner split. | `# mcp/src/agents_remember/benchmarks/runner_modules Overview` | onboarding/mcp/src/agents_remember/benchmarks/runner_modules/overview.md:1-137 |
| Benchmark behavior is covered through the existing worktree/tool test slices. | `test_changed_worktree_paths_includes_long_files` | mcp/tests/test_worktree_support_tests_1.py:1150-1163 |

## Cross-Repo References

No configured sibling repository is required for this module.

## Update History

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1 candidate-11 curation rebind: refreshed formatter-moved source coordinates against accepted tree `4241908c`; where applicable, replaced a deleted coordinator anchor with the sole current owner. Verification metadata remains pinned until governed closeout.

- 2026-08-04T18:20+02:00 — 260731-EFA-L6 S18-B15 curator: resolved 1 citation finding:
  `test_changed_worktree_paths_includes_long_files` moved to `test_worktree_support.py:1541-1554`.
  Scoped recheck clean.

- 2026-08-02T21:02:09+02:00 — 260731-EFA-L6 curator W2-B10: repaired 6 citation findings (3 reference rows); scoped recheck clean.

- 2026-05-31T12:50+02:00 — `removable_path` stopped inlining the Windows `\\?\` long-path logic and now delegates to the shared `long_path` helper (imported from `agents_remember.install.assets`); corrected Logic prose to drop "across platforms" ownership and note the delegation (1.0.0 review remediation).
- 2026-05-28T12:32+02:00: Updated after benchmark workspace scaffolding moved MCP/provider logs under the central `logs/` tree.
- 2026-05-26T02:26+02:00: Created when `benchmarks/runner.py` was split into focused implementation modules.
