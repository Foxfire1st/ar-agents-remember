# mcp/src/agents_remember/benchmarks/runner_modules/models.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/benchmarks/runner_modules/models.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-02T01:05+02:00                     |
| lastVerifiedCommitHash | `b252c42cca200933d5c9c36e26de47a526a569ce` |
| lastVerifiedCommitDate | 2026-08-07T23:58:52+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[runner_modules overview](overview.md)

## Purpose

Typed benchmark case and service request dataclasses.

## Code Commentary

### 260731-EFA-L2 Shared Benchmark Value Objects

Five frozen dataclasses were added here and are what the runner modules are now signed on:

- **`BenchmarkWorkspace(case, workspace_root, coordination_root, source_repo_root, memory_repo,
  provider_ids=())`** — one case's materialized with-memory workspace: the case plus the roots laid
  down for it and the providers it arms. Prepared once by `workspace.prepare_case` and handed whole
  to everything that writes the workspace registration or launches providers.
- **`BenchmarkTask(prompt, variant, repetition)`** — one prompt/variant/repetition scheduled inside
  a run. It replaces the bare `(prompt, variant, repetition)` tuples the batch builder used to emit.
- **`BenchmarkRun(benchmarks_root, case, output_root, dry_run, codex_sandbox=CODEX_BENCHMARK_SANDBOX)`**
  — one case execution: what it reads, where results land, how Codex runs.
- **`BenchmarkPreparation(benchmarks_root, dry_run=True, skill_exposure_mode="copy",
  force_clone=False, provider_timeout=1800, allowed_provider_ids=None)`** — how a workspace is
  (re)materialized before use. **Shared by prepare and run**: `BenchmarkPrepareRequest` and
  `BenchmarkRunRequest` each expose a `preparation` property projecting onto it (resolving
  `benchmarks_root` as they go), so `prepare_case` takes one object instead of the same six fields
  unpacked at every layer — and the two entry points cannot drift apart on preparation semantics.
- **`BenchmarkRunOutcome(cases, output_roots, messages, codex_executable)`** — what one
  `codex_benchmark_run` produced, before it is rendered as a payload.

`allowed_provider_ids` rides on `BenchmarkPreparation` as well as on both requests, so the
containment R1 authority set reaches `filter_benchmark_provider_ids` through the preparation
object; its FAIL-CLOSED `None` handling is unchanged.

### Logic

`models.py` defines `BenchmarkCase`, `BenchmarkPrepareRequest`, and `BenchmarkRunRequest`, including property accessors that normalize manifest dictionaries for downstream modules.

Both service requests carry `allowed_provider_ids: tuple[str, ...] | None`
(containment R1, 260707-HFX-L1): the live MCP authority's provider ids, which
the MCP application entry points always pass so manifest-requested providers outside the
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
  fail-closed at the consuming filter (review B4); the MCP application entry points must
  always pass the live authority set (containment R1).

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The public benchmark facade re-exports this module's public functions and classes for compatibility. | `models` | mcp/src/agents_remember/benchmarks/runner.py:22-22 |
| The route-local overview summarizes how this module fits into the benchmark runner split. | `# mcp/src/agents_remember/benchmarks/runner_modules Overview` | onboarding/mcp/src/agents_remember/benchmarks/runner_modules/overview.md:1-137 |
| Benchmark behavior is covered through the existing worktree/tool test slices. | `BenchmarkRunnerPortabilityTests`, `test_benchmark_provider_ids_follow_selected_variants` | mcp/tests/test_worktree_support_benchmark.py:32-665 |

## Cross-Repo References

No configured sibling repository is required for this module.

## Update History

- 2026-08-03T03:59:59+02:00 — Curated 6 citation claims (3 table rows, 3 source-form repairs): added exact anchors and source paths; scoped fixer generated the final ranges.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-31T00:00+02:00 — 260731-EFA-L2 (gate honesty, `PLR0913` armed with no exemptions):
  added the frozen `BenchmarkWorkspace`, `BenchmarkTask`, `BenchmarkRun`, `BenchmarkPreparation`
  and `BenchmarkRunOutcome`, plus the `preparation` property on both `BenchmarkPrepareRequest` and
  `BenchmarkRunRequest`. Request fields and defaults are unchanged. Verification metadata pinned
  until closeout stamps the L2 commit.
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
