# test_tools.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_tools.py`                  |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-02T01:05+02:00                 |
| lastVerifiedCommitHash | `1580f92715ff93c988f9a15439ad9bec60ef4c5d`|
| lastVerifiedCommitDate | 2026-08-13T00:18:59+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

`test_tools.py` verifies public MCP tool payloads, server registration, and
application-to-service behavior.

## Code Commentary

L23 adds `citation_fix` to the asserted public MCP tool set, preventing guarded citation repair from disappearing from registration.

The test suite covers core server payloads, FastMCP server construction,
context-packet delegation, runtime install payload authority, public tool
surface expectations (which no longer list `direct_closeout_preview`/`apply`
after the issue #62 worktree-only removal), skills install behavior, route
index refresh, memory quality exposure, provider status and watcher
current-state reporting, typed GrepAI and CodeGraphContext command
construction, worktree tool behavior, and Codex benchmark execution policy
reporting.

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
dependencies (`analyze deps <module>`), and complexity. GrepAI assertions keep workspace/project
selection tied to MCP configuration and keep trace action validation explicit.
A regression case configures an uppercase repo id (`Cobalt`) and asserts that
`grepai_search` emits `--project cobalt` and accepts the id in any casing, so the
tool's `--project` matches the watcher's `stable_provider_id`-normalized project.

This file no longer carries the Docker-mode provider-runner-integrity
regressions (the three `test_provider_integrity_ignores_*` cases and their
`check_provider_runner_integrity` / `manifest_path_for_config` imports were
removed); that integrity coverage now lives elsewhere.

Payload tests track the act-by-default `dry_run` contract: the `skills_install`,
`route_index_refresh`, and `memory_init` payload tests assert apply-by-default
(`dryRun` is false), while the typed CGC and GrepAI command-construction tests pass
`scope=DRY_RUN_SCOPE` per call (the module-level `ProviderQueryScope(dry_run=True)`)
because the planned provider command is only exposed in the preview path.

Provider and application entry point payload builders are addressed through parameter objects rather
than loose keywords: GrepAI search/trace take a `GrepaiSearchQuery` / `GrepaiTraceQuery`
plus an optional `repos=GrepaiRepoScope(...)` and `scope=ProviderQueryScope(...)`,
`memory_carryover_plan_payload` takes a `CarryoverSelection`, and
`codex_benchmark_run_payload` takes a `CodexBenchmarkRun`. The validation cases still
assert the same messages (`unknown repo_ids`, `repo_ids is required`, `trace_action`,
`depth`) — only the argument spelling moved.

Newer cases assert that every public tool registers a human-facing description,
and that `runtime_install_payload` exposes a `no_cache` parameter defaulting to
`False` and forwards `no_cache=True` into the `RuntimeInstallRequest`.

Task 10 extends `test_phase_04_tools_are_reported` with the three
`operator_inbox_*` tools so the external-chat inbox surface is pinned in
`PUBLIC_TOOLS`; `test_every_public_tool_has_a_description` also covers their
FastMCP docstrings through the server tool list.

Task 25 changes the public-tool surface expectation: `lifecycle_gate` is included
as the unified gate junction, while `lifecycle_block`, `gate_create`, `gate_wait`,
and `gate_response_wait` are explicitly asserted absent from `PUBLIC_TOOLS`.

L9 extends that public-tool surface expectation with `attach_terminal_session_to_leaf`, the agent-facing
tool for moving an existing hosted terminal/chat session between durable leaves through the dashboard
catalog. L2 extends it further with `spawn_agent_session`, the agent-facing session-dispatch tool, so the
expected `PUBLIC_TOOLS` subset pins both terminal-catalog tools.

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
  `AGENTS_REMEMBER_REAL_MCP_CONFIG` so normal unit runs stay hermetic; `RealMcpIntegrationTests`
  also carries `@pytest.mark.agents_remember_real_mcp_config` so the environment-gated class can be
  selected or deselected by marker under the strict-markers pytest config.
- The real-MCP GrepAI assertion derives its expected `--workspace` from the same
  `grepai_workspace(load_config(...))` call the server uses, never a literal workspace name: once
  provider instances became scoped, `scoped_name` appends the instance id, so a hardcoded name is
  no longer anyone's workspace and would make the (rarely run) integration check vacuous.
- Provider lifecycle MCP tests should keep provider operations on typed service
  functions instead of CLI `main(argv)` wrappers.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Public tool metadata and payload builders live in the `mcp/tools/` package (split by domain behind a facade `__init__.py`). | `_tool_payload` | mcp/src/agents_remember/mcp/tools/base.py:70-72 |
| Public response model registry validates payload shapes. | `PUBLIC_TOOL_RESPONSE_MODELS` | mcp/src/agents_remember/models/tool_registry.py:217-221 |
| Server registration lives in `server.py`. | `create_server` | mcp/src/agents_remember/mcp/server.py:32-44 |
| Application-layer modules convert public MCP payloads into service calls. | `build_context_packet` | mcp/src/agents_remember/application/context_packet.py:59-102 |
| Provider current-state reporting lives in the current-state module and is exposed by provider watcher status payloads. | `build_current_provider_state` | mcp/src/agents_remember/providers/current_state.py:16-36 |
| The agent-facing control surface exposes only structural dispatch, parent/child messaging, lifecycle gates, and role-relative administration. | "test_agent_control_surface_exposes_only_structural_addresses" | mcp/tests/test_tools.py:156-221 |
| Exact-session administrative tools, including inbox rows, task attachment, raw spawn, retire, and rename, are explicitly absent from the public agent roster. | "for retired in (" | mcp/tests/test_tools.py:414-428 |

## 260712-TRH-L4 Final Candidate

This sidecar was reviewed against the final uncommitted L4 candidate. The source now participates in the explicit spawned-unbriefed → harness-ready → briefed flow; dispatch proof remains exact-session, copy-mode-aware, harness-log-confirmed, and pending without respawn when proof is absent. Catalog writers are fully serialized across one read/body/write transaction while atomic readers remain lock-free.

## 260718-CHATS-L5I Incremental Commit-Gate Delta

The closeout-description regression loads the real MCP server and asserts both public tools name
mandatory CRAP enforcement. Preview must say it runs before the code commit; apply must say it runs
before any code mutation and that approval precedes apply.

## Update History

- 2026-08-12T15:56+02:00 — 260731-EFA-L23 curator body review: reconciled this card with the exact current source delta described above; verification provenance remains closeout-owned.

- 2026-08-11T19:58+02:00 — Aligned the regression card for `test_tools.py` with the source's current task-document, seat-routing, inbox, or lifecycle assertions.
- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-03T03:07:44+02:00 — W3-B05 curator: resolved 7 Tier-2 table findings with exact anchors and source paths; fixer generated all final ranges.
- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-31T16:50+02:00 — 260731-EFA-L2 code-quality gate: the provider, memory, and benchmark
  payload builders moved their loose keywords into parameter objects, so the GrepAI and CGC cases
  now pass `GrepaiSearchQuery` / `GrepaiTraceQuery` / `GrepaiRepoScope` and a module-level
  `DRY_RUN_SCOPE = ProviderQueryScope(dry_run=True)` instead of `dry_run=True`, carryover planning
  passes a `CarryoverSelection`, and the benchmark sandbox case passes a `CodexBenchmarkRun`.
  Corrected the `dry_run` paragraph, which still claimed the CGC test passes `dry_run=True` per
  call, and added a paragraph naming the parameter objects. Two further real changes are now
  recorded in Invariants: `RealMcpIntegrationTests` gained
  `@pytest.mark.agents_remember_real_mcp_config` on top of its `AGENTS_REMEMBER_REAL_MCP_CONFIG`
  skip, and its `--workspace` assertion stopped comparing against the stale literal
  `agents-remember-memory`, deriving the expected value from `grepai_workspace(load_config(...))`
  instead. No test case was added, removed, or renamed.

- 2026-07-24T14:31Z — 260718-CHATS-L5I incremental curator: added the public closeout-description
  regression contract for mandatory CRAP, quality-before-mutation, and approval-before-apply;
  verification remains pinned until the code commit.

- 2026-07-12T14:20:00+02:00 — 260712-TRH-L4 curator refresh: final candidate onboarding; exact-session dispatch and serialized-writer/lock-free-reader concurrency recorded.

- 2026-07-04T11:10+02:00 — L2: the expected public-tool subset now includes `spawn_agent_session`,
  pinning the agent-facing session-dispatch surface in `PUBLIC_TOOLS` beside
  `attach_terminal_session_to_leaf`. Verification metadata pinned until closeout stamps the L2 commit.
- 2026-07-02T17:04+02:00 — L9: public-tool coverage now expects
  `attach_terminal_session_to_leaf`, pinning the new agent-facing hosted chat reassignment surface in
  `PUBLIC_TOOLS`. Verification metadata pinned until closeout stamps the L9 commit.
- 2026-07-02T15:40+02:00 — The typed CGC command-construction assertions now
  expect `cgc_dependencies_payload(..., dry_run=True)` to expose
  `analyze deps <module>`, matching the current CodeGraphContext CLI.
- 2026-06-26T14:16+02:00 — Task 25: public tool expectations now include `lifecycle_gate` and assert the retired split helpers are absent from `PUBLIC_TOOLS`.
- 2026-06-25T07:17+02:00 — Task 19: added `gate_response_wait` to the expected public-tool surface. Verification metadata pinned until closeout stamps the task-19 code commit.
- 2026-06-23T13:44+02:00 — Task 10 backend inbox: `test_phase_04_tools_are_reported` now expects `operator_inbox_post`, `operator_inbox_poll`, and `operator_inbox_consume`; the existing public-description smoke test covers their server docstrings. Verification metadata pinned until closeout stamps the task-10 code commit.
- 2026-06-11T14:12+02:00: No content impact: the repository rename sweep replaced `agents-remember-md` with `agents-remember` in the source file; the card already uses the new name and its semantics are unchanged.
- 2026-06-11T06:47+02:00 — `test_phase_04_tools_are_reported` no longer expects `direct_closeout_preview`/`direct_closeout_apply` (issue #62 worktree-only closeout removed the tools from `PUBLIC_TOOLS`).
- 2026-06-10T05:30+02:00 — Diagnostics/watchers tool tests assert the S4 compact wire shape: rawStatus/currentState bodies absent inline, present in the `reportPath` file, `currentStateFile` still on disk.
- 2026-06-02T04:40+02:00: Updated the skills_install payload tests for the flat installer — dropped the `layout == "tree"` assertion and replaced the legacy-namespace-symlink test with a per-skill flat-destination symlink-replacement test. `l-01-session-job-lifecycle` skill series, Sub-task B/S7, mcp 1.1.0.
- 2026-06-02T02:00+02:00 — Added `test_grepai_search_resolves_uppercase_repo_id_to_normalized_project`: a configured uppercase repo id (`Cobalt`) is queried as `--project cobalt` and accepted in any casing. Updated Code Commentary.
- 2026-05-31T12:50+02:00 — `test_ping_payload` now asserts `payload["version"] == SERVER_VERSION` (imported from `agents_remember.mcp`) instead of the `0.9.6` literal; the Codex benchmark policy test flips the fixed default to `default`/`omitted` and asserts `danger-full-access` separately; added `test_codex_benchmark_tools_refuse_when_disabled`; removed the three Docker-mode `test_provider_integrity_ignores_*` cases and their `check_provider_runner_integrity`/`manifest_path_for_config` imports. Corrected the version-assertion, Codex benchmark, and provider-integrity prose to match (1.0.0 review remediation).
- 2026-05-31T01:06+02:00: Updated `test_ping_payload`'s version assertion to `0.9.6` (MCP 0.9.6, `w-02-light-task-workflow` skill design section). Verification metadata stays pinned until closeout commits the change.
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
