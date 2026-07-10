# mcp/src/agents_remember/benchmarks/runner_modules/models.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/benchmarks/runner_modules/models.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-07T17:40+02:00                     |
| lastVerifiedCommitHash | `0d5ce6784930aa4e9006ab4bbf2b788a3296abce` |
| lastVerifiedCommitDate | 2026-07-10T22:30:19+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[runner_modules overview](overview.md)

## Purpose

Typed benchmark case and service request dataclasses.

## Code Commentary

### Logic

`models.py` defines `BenchmarkCase`, `BenchmarkPrepareRequest`, and `BenchmarkRunRequest`, including property accessors that normalize manifest dictionaries for downstream modules.

Both service requests carry `allowed_provider_ids: tuple[str, ...] | None`
(containment R1, 260707-HFX-L1): the live MCP authority's provider ids, which
the MCP controllers always pass so manifest-requested providers outside the
set are skipped downstream rather than armed or launched. `None` means direct
script use with no authority context; the consuming filter
(`workspace.filter_benchmark_provider_ids`) treats `None` FAIL-CLOSED since
review B4 — an unfiltered direct-script run needs the explicit
`AR_BENCHMARK_ALLOW_UNFILTERED_PROVIDERS=1` escape. (The field's inline
comment still describes the pre-B4 "unfiltered" semantics; the behavior lives
in the filter.)

### Invariants And Boundaries

- Keep request defaults here aligned with the CLI and MCP tool defaults.
- Do not add workflow behavior to the dataclasses.
- `allowed_provider_ids=None` stays reserved for direct script use — and is
  fail-closed at the consuming filter (review B4); the MCP controllers must
  always pass the live authority set (containment R1).

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The public benchmark facade re-exports this module's public functions and classes for compatibility. | [runner.py](agents-remember/mcp/src/agents_remember/benchmarks/runner.py) |
| The route-local overview summarizes how this module fits into the benchmark runner split. | [runner_modules overview](agents-remember/mcp/src/agents_remember/benchmarks/runner_modules/overview.md) |
| Benchmark behavior is covered through the existing worktree/tool test slices. | [test_worktree_support.py](agents-remember/mcp/tests/test_worktree_support.py) |

## Cross-Repo References

No configured sibling repository is required for this module.

## Update History

- 2026-07-07T17:40+02:00 — 260707-HFX-L1 review fix B4 (consumer-side): documented that the
  filter consuming `allowed_provider_ids` now treats `None` fail-closed (env escape
  `AR_BENCHMARK_ALLOW_UNFILTERED_PROVIDERS=1`); the dataclass field itself is unchanged, and its
  inline comment still carries the pre-B4 "unfiltered" wording (flagged, behavior lives in the
  filter). Verification metadata pinned until closeout stamps the HFX-L1 commit.
- 2026-07-07T16:30+02:00 — 260707-HFX-L1 (provider containment R1): `BenchmarkPrepareRequest` and
  `BenchmarkRunRequest` gained `allowed_provider_ids` (None = direct script use, unfiltered; the
  MCP controllers always pass the live authority set). Verification metadata pinned until
  closeout stamps the HFX-L1 commit.
- 2026-05-26T02:26+02:00: Created when `benchmarks/runner.py` was split into focused implementation modules.
