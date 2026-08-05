# mcp/src/agents_remember/benchmarks/runner_modules/constants.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/benchmarks/runner_modules/constants.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-31T12:30+02:00                     |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[runner_modules overview](overview.md)

## Purpose

Shared benchmark constants for paths, provider ids, Codex usage token fields, Codex policy, and MCP registration names.

## Code Commentary

### Logic

`constants.py` centralizes values that multiple benchmark modules need, including supported benchmark providers, `.codex` paths, sandbox modes, and benchmark MCP names.

### Invariants And Boundaries

- Constants should stay declarative. Add behavior to a named owner module instead of expanding this file into a utility grab bag.

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The public benchmark facade re-exports this module's public functions and classes for compatibility. | `prepare_repo` | mcp/src/agents_remember/benchmarks/runner.py:28-33 |
| The route-local overview summarizes how this module fits into the benchmark runner split. | `## Purpose` | onboarding/mcp/src/agents_remember/benchmarks/runner_modules/overview.md:13-19 |
| Benchmark behavior is covered through the existing worktree/tool test slices. | `BenchmarkRunnerPortabilityTests` | mcp/tests/test_worktree_support.py:3052-3680 |

## Cross-Repo References

No configured sibling repository is required for this module.

## Update History

- 2026-08-02T16:44:03+02:00 — W1-B07 curator: repaired 3 repository-reference citations (3/3 anchored and sourced; scoped citation check clean).

- 2026-06-11T14:12+02:00: No content impact: the repository rename sweep replaced `agents-remember-md` with `agents-remember` in the source file; the card already uses the new name and its semantics are unchanged.
- 2026-05-31T12:30+02:00 — Replaced `TOKEN_KEYS` alias map with `USAGE_TOKEN_KEYS` (Codex turn.completed usage fields) and flipped `CODEX_BENCHMARK_SANDBOX` to secure-by-default `default` (1.0.0 review remediation).
- 2026-05-26T02:26+02:00: Created when `benchmarks/runner.py` was split into focused implementation modules.
