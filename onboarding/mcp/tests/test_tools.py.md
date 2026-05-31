# test_tools.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/tests/test_tools.py`                  |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-31T12:50+02:00                     |
| lastVerifiedCommitHash | `c20a3292e667d227a3be0c1fb276f8a701df814f` |
| lastVerifiedCommitDate | 2026-05-31T14:17:11+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

`test_tools.py` verifies public MCP tool payloads, server registration, and
controller-to-service behavior.

## Code Commentary

The test suite covers core server payloads, FastMCP server construction,
context-packet delegation, runtime install payload authority, public tool
surface expectations, skills install behavior, route index refresh, memory
quality exposure, provider status and watcher current-state reporting, typed
GrepAI and CodeGraphContext command construction, worktree tool behavior, and
Codex benchmark execution policy reporting.

After the response-contract wiring, tests also protect that modeled payloads
carry populated token metadata — `test_ping_payload` asserts a real `tokens`
count (> 0), `tokenizer == "tiktoken:o200k_base"`, and `tokenCountExact is True`
since the S6 token-counter wiring — and that service-backed MCP tools do not
expose legacy command-capture wrapper fields such as raw `argv`, `stdout`,
`stderr`, or parsed `payload` wrappers. The `test_ping_payload` version check no
longer pins a literal string; it asserts `payload["version"] == SERVER_VERSION`
(imported from `agents_remember.mcp`) so the test tracks the package version
instead of a hardcoded release number.

The typed CGC assertions keep the old generic `cgc_query` name absent and
verify fixed command construction for symbol search, callers, callees,
dependencies, and complexity. GrepAI assertions keep workspace/project
selection tied to MCP configuration and keep trace action validation explicit.

This file no longer carries the Docker-mode provider-runner-integrity
regressions (the three `test_provider_integrity_ignores_*` cases and their
`check_provider_runner_integrity` / `manifest_path_for_config` imports were
removed); that integrity coverage now lives elsewhere.

Payload tests track the act-by-default `dry_run` contract: the `skills_install`,
`route_index_refresh`, and `memory_init` payload tests assert apply-by-default
(`dryRun` is false), while the typed CGC command-construction test passes
`dry_run=True` per call because the planned provider command is only exposed in
the preview path.

Newer cases assert that every public tool registers a human-facing description,
and that `runtime_install_payload` exposes a `no_cache` parameter defaulting to
`False` and forwards `no_cache=True` into the `RuntimeInstallRequest`.

The Codex benchmark policy coverage now treats `"default"`/`"omitted"` as the
fixed (no-sandbox-argument) reporting and asserts the explicit
`danger-full-access` request separately. `test_codex_benchmark_tools_refuse_when_disabled`
adds a guard case: when `benchmarksEnabled` is `False`, both
`codex_benchmark_run_payload` and `codex_benchmark_prepare_payload` return
`ok is False` with the matching `operation` and a `disabled` error.

## Invariants And Boundaries

- Public MCP tools should remain typed and package-owned.
- Payload tests should protect stable domain payloads and model defaults, not
  command-capture implementation artifacts.
- Real MCP stdio integration remains gated behind
  `AGENTS_REMEMBER_REAL_MCP_CONFIG` so normal unit runs stay hermetic.
- Provider lifecycle MCP tests should keep provider operations on typed service
  functions instead of CLI `main(argv)` wrappers.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Public tool metadata and payload builders live in the `mcp/tools/` package (split by domain behind a facade `__init__.py`). | [tools/](agents-remember-md/mcp/src/agents_remember/mcp/tools) |
| Public response model registry validates payload shapes. | [tool_registry.py](agents-remember-md/mcp/src/agents_remember/models/tool_registry.py) |
| Server registration lives in `server.py`. | [server.py](agents-remember-md/mcp/src/agents_remember/mcp/server.py) |
| Domain controller modules convert public MCP payloads into service calls. | [controllers overview](agents-remember-md/mcp/src/agents_remember/controllers/overview.md) |
| Provider current-state reporting lives in the current-state module and is exposed by provider watcher status payloads. | [current_state.py](agents-remember-md/mcp/src/agents_remember/providers/current_state.py) |

## Update History

- 2026-05-31T12:50+02:00 — `test_ping_payload` now asserts `payload["version"] == SERVER_VERSION` (imported from `agents_remember.mcp`) instead of the `0.9.6` literal; the Codex benchmark policy test flips the fixed default to `default`/`omitted` and asserts `danger-full-access` separately; added `test_codex_benchmark_tools_refuse_when_disabled`; removed the three Docker-mode `test_provider_integrity_ignores_*` cases and their `check_provider_runner_integrity`/`manifest_path_for_config` imports. Corrected the version-assertion, Codex benchmark, and provider-integrity prose to match (1.0.0 review remediation).
- 2026-05-31T01:06+02:00: Updated `test_ping_payload`'s version assertion to `0.9.6` (MCP 0.9.6, W-02 design section). Verification metadata stays pinned until closeout commits the change.
- 2026-05-30T22:29+02:00: Updated `test_ping_payload` for the S6 token-counter wiring — it now asserts populated `tokens`/`tokenizer`/`tokenCountExact` instead of the zero defaults, and the version assertion moved to `0.9.5`. Typed the `fake_run` stub against `RuntimeInstallRequest` (with its import) to clear a Pyright error. Verification metadata stays pinned until closeout commits the change.
- 2026-05-30T21:51+02:00: Documented the new coverage — every public tool must register a description, and `runtime_install_payload` exposes/forwards `no_cache` (default `False`). Repaired the stale `tools.py` reference to the split `mcp/tools/` package. Verified against `57944df`.
- 2026-05-29T21:00+02:00: Updated the `ping_payload()` version assertion to MCP release `0.3.0`.
- 2026-05-29T20:25+02:00: Updated after the `skills_install`/`route_index_refresh`/`memory_init` payload tests moved to act-by-default assertions and the typed CGC command-construction test pinned `dry_run=True` (`dry_run`-default flip task).
- 2026-05-28T19:52+02:00: Updated after public tool payloads began validating through Pydantic response models and `ping_payload()` started emitting token metadata defaults.
- 2026-05-28T15:43+02:00: Updated after `ping_payload()` version expectations moved to MCP release `0.2.0`. Verification metadata remains pinned until closeout commits the source change.
- 2026-05-28T12:32+02:00: Updated after MCP tool tests added provider watcher status current-state coverage.
- 2026-05-26T23:11+02:00: Refreshed verification metadata after source commit `5ab704a` landed GrepAI MCP command-shape and real stdio integration coverage.
- 2026-05-26T22:54+02:00: Updated after GrepAI search/trace unit tests and gated real MCP stdio integration tests covered the new tool shape.
- 2026-05-26T12:51+02:00: Updated after provider integrity stopped treating CodeGraphContext host venvs as authority because CGC is Docker-owned.
- 2026-05-25T19:16+02:00: Updated after service tests patched `providers.lifecycle.main` directly and the `provider_lifecycle.py` compatibility module was deleted.
- 2026-05-25T18:07+02:00: Updated after provider integrity removed `_bin` from current runner authority and kept old `_bin` manifest entries ignored.
- 2026-05-25T17:40+02:00: Updated after provider integrity tests switched the blocking case to CGC runner state and added Docker-mode legacy GrepAI binary/current-manifest ignore coverage.
- 2026-05-24T19:25+02:00: Added regression coverage that provider runner integrity failures block CGC query and watcher execution before lifecycle services run.
- 2026-05-24T10:06+02:00: Refreshed verification metadata after source commit `f48a346` covered `.codex` skill roots and benchmark sandbox payloads.
- 2026-05-24T09:23+02:00: Updated after MCP tool tests moved normal harness-root fixtures from `.agents` to Codex `.codex`.
- 2026-05-24T08:56+02:00: Updated after missing-Codex benchmark payload coverage began asserting `sandboxArgument` for fixed and default sandbox modes.
- 2026-05-24T06:57+02:00: Updated after missing-Codex benchmark payload tests began asserting explicit benchmark-only `PATH` resolution policy.
- 2026-05-24T02:47+02:00: Updated after public tool expectations added `memory_quality_check`.
- 2026-05-24T00:35+02:00: Added regression coverage that service-backed MCP tools no longer expose command-capture artifacts.
- 2026-05-23T20:56+02:00: Added regression coverage that MCP provider tools do not route through the provider lifecycle CLI main.
- 2026-05-23T20:42+02:00: Added typed CGC public-tool and fixed command-shape coverage.
- 2026-05-23T18:05+02:00: Created during direct closeout prep for public MCP tool test coverage.
