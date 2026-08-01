# mcp/src/agents_remember/mcp/registration

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| sourceRoute            | `mcp/src/agents_remember/mcp/registration`       |
| doc_type               | `route-local-overview`                           |
| lastUpdated            | 2026-08-01T00:00+02:00                           |
| lastVerifiedCommitHash | `e52edaf5b655f495580efd93306afdf922b19b51`       |
| lastVerifiedCommitDate | 2026-08-01T11:01:51+02:00|
| governingOverview      | `../../../../../overview.md`                     |

## Purpose

`mcp/registration/` is the **advertised MCP tool surface**: every `@server.tool()`
declaration in this repository lives here, one module per tool family. It was carved out of
`mcp/server.py` in 260731-EFA-L2; `server.py` kept only process wiring (compact-content shim,
ambient lifecycle, the `FastMCP` instance) and now loops over `TOOL_REGISTRARS` from this
package's `__init__.py`.

Each module exposes exactly one `register_<family>_tools(server, config) -> None`, declares its
tools as nested functions decorated with `@server.tool()`, and forwards each call to one payload
builder in `mcp/tools/`. Nothing else belongs here.

## The Defining Contract: The Signature IS The Published Schema

**FastMCP derives each tool's published JSON input schema from the Python signature.** A flat
parameter list publishes flat properties; a model-typed parameter republishes the tool as a single
nested object. Measured against the installed mcp 1.28.1 and recorded verbatim in `pyproject.toml`:

```
def flat(repo_id, task_name, leaf_id)  -> properties: [repo_id, task_name, leaf_id]; no $defs
def nested(args: SomeModel)            -> properties: [args];                        has $defs
```

So "tidying" `spawn_agent_session(leaf_key=...)` into `spawn_agent_session(seat: SpawnSeat)` does
not refactor anything — it changes the wire. `{"leaf_key": ...}` becomes `{"seat": {"leaf_key":
...}}` for every MCP client, every row of `docs/reference/mcp-tools.md`, and every flat-kwargs call
in the `c-09` and `l-01` skills.

That is why these modules — and only these — are exempt from `PLR0913` (the ≤5-argument rule that
260731-EFA-L2 armed at full strength across the rest of the tree, refactoring 274 of 293 offenders
into 163 parameter objects rather than listing them). The exemption is a single per-file-ignore in
`pyproject.toml`:

```toml
"mcp/src/agents_remember/mcp/registration/*.py" = ["PLR0913"]
```

The remaining 19 long signatures in the repository are exactly the `@server.tool()` declarations
under this path. There is no ratchet, baseline, grandfather list or burn-down behind it — the
developer ruled all four forbidden — and no `noqa` anywhere holds an argument-count finding down.

**Do not flatten this carve-out into a habit.** It is held shut mechanically by
`mcp/tests/test_code_quality_check.py::ToolSignatureExemptionTests`, which:

- asserts `PLR0913` is selected and neither globally ignored nor softened by a `max-args` override;
- asserts the exempted-pattern set equals exactly `{"mcp/src/agents_remember/mcp/registration/*.py"}`
  — a second exemption anywhere, or a widened pattern, fails;
- walks the AST of every file the pyproject pattern actually matches and fails if any function in
  them is anything but a `@server.tool()` declaration or the registrar that hosts them;
- runs Ruff over the tracked tree with `--ignore-noqa --select PLR0913` and requires exit 0, so a
  line-level suppression cannot hide a finding the gate would otherwise see.

## Layout

| Module              | Family                                                                    |
| ------------------- | ------------------------------------------------------------------------- |
| `__init__.py`       | `TOOL_REGISTRARS` (the ordered tuple `create_server` loops over) and the `ToolRegistrar` alias. |
| `core.py`           | `ping`, `server_info`, `context_packet`, `read_ar_files`, `resolve_context`, `runtime_install`, `skills_install`. |
| `sessions.py`       | `attach_terminal_session_to_leaf`, `spawn_agent_session`, `hosted_session_readiness`, `session_retire`, `session_rename`. |
| `memory.py`         | `drift_check`, `memory_quality_check`, `route_index_refresh`, `memory_init`, `memory_baseline_status`, `memory_baseline_adopt`, `memory_carryover_plan`, `memory_carryover_apply`. |
| `providers.py`      | `provider_status`, `provider_diagnostics`, `provider_watchers`.            |
| `code_search.py`    | `grepai_search`, `grepai_trace`, and the six `cgc_*` graph tools.          |
| `worktrees.py`      | `worktree_start`, `worktree_attach`, `worktree_status`, `worktree_sync` — the working half of a task. |
| `closeout.py`       | `worktree_closeout_preview`, `worktree_closeout_apply`, `worktree_integrate`, `worktree_cleanup`, `worktree_abandon` — the landing half. |
| `tasks.py`          | `task_reopen`, `lifecycle_finalize_task`, `task_doc`.                      |
| `benchmarks.py`     | `codex_benchmark_prepare`, `codex_benchmark_run`.                          |
| `lifecycle.py`      | The six session-lifecycle signals: `lifecycle_start`, `lifecycle_resume`, `lifecycle_turn_end_notification`, `lifecycle_end`, `switch_lifecycle`, `lifecycle_phase`. |
| `gates.py`          | `lifecycle_gate`, `gate_decide`, `gate_list`.                              |
| `orchestration.py`  | `operator_inbox_post`, `operator_inbox_poll`, `operator_inbox_consume`, `orchestration_nudge_manager`. |

Twelve registrars, 58 advertised tools — the same 58 names `mcp/tools/base.py::PUBLIC_TOOLS`
lists, which `mcp/tests/test_tools.py` checks against a live server's `list_tools()`.

## Hot Path Summary

A tool body does exactly two things: pack the flat MCP arguments into the parameter objects the
payload builder and its controller take, and return the builder's result unchanged. The packing is
the whole content — `TaskRef`, `SpawnSeat`, `GateVerdict`, `CarryoverSelection`,
`CloseoutCommitMessages`, `TaskIdentity`/`TaskBases`/`StartExecution`, `BenchmarkSelection`/
`BenchmarkPreparation`/`CodexBenchmarkRun`, `TaskDocTarget`/`TaskDocEdit`, `InboxAddress`/
`InboxMessage`/`InboxPoster`, `NudgeTarget`/`NudgeSubject`, `GrepaiSearchQuery`/`GrepaiRepoScope`/
`ProviderQueryScope`.

The published docstring is the model-visible description of the tool and is checked for presence by
`test_tools.py`; it is the only place a caller learns the semantics, so it carries the refusal
vocabulary and the act-by-default `dry_run` contract in prose.

Two attributions are fixed **in this layer**, not taken from the caller, so an agent cannot
self-attribute a human decision:

- `gate_decide` sends `by="model"`, `via="cli"` for a plain decision; supplying `deciding_role`
  switches `via` to `"orchestration"` and leaves `by` empty for the server to fill from the role.
- `operator_inbox_post` and `operator_inbox_consume` always send `created_by`/`consumed_by="model"`
  and `..._via="cli"`. Trusted dashboard code calls the payload builder directly with
  developer/dashboard attribution instead.

`register_lifecycle_tools` takes `_config` and does not use it: its six payloads act on the
process-wide ambient lifecycle rather than on resolved settings. The parameter stays so every
module in the package has the one registrar signature `TOOL_REGISTRARS` is typed against.

## Invariants And Boundaries

- **Never give a tool function a model-typed parameter.** The signature is the published schema;
  a parameter object here is a breaking wire change for every client. This is the reason for the
  `PLR0913` exemption and the reason nobody may "tidy" these functions.
- Keep bodies to packing + one forwarded call. Any ordinary logic added under this path fails
  `ToolSignatureExemptionTests::test_every_function_in_the_exempted_path_is_a_published_tool_declaration`.
- Do not add a second `PLR0913` exemption or widen the existing pattern; both fail the same suite.
- A new tool means editing one family module and appending to `PUBLIC_TOOLS`, the response-model
  registry, and `docs/reference/mcp-tools.md`; a new family means a new module plus one entry in
  `TOOL_REGISTRARS`. `create_server` itself should not grow a special case.
- Registration order in `TOOL_REGISTRARS` is the order the server advertises tools in; the
  `PUBLIC_TOOLS` equality check is set-based for `list_tools()` but exact-list for `server_info`.
- Request validation belongs in the payload builders and controllers; response validation belongs
  to `base._tool_payload`. This layer validates nothing.
- Do not add a raw shell or arbitrary-command tool to this surface.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| `create_server` loops over `TOOL_REGISTRARS` and owns nothing else about the tool surface. | [server.py](agents-remember/mcp/src/agents_remember/mcp/server.py) |
| The payload builders every declaration forwards to. | [tools overview](../tools/overview.md) |
| `PUBLIC_TOOLS` — the advertised name list this package must match. | [tools/base.py](agents-remember/mcp/src/agents_remember/mcp/tools/base.py) |
| The `PLR0913` per-file-ignore and the reasoning recorded beside it. | [pyproject.toml](agents-remember/pyproject.toml) |
| The AST suite that holds the exemption to published tool declarations only. | [test_code_quality_check.py](agents-remember/mcp/tests/test_code_quality_check.py) |
| What each declaration hands its payload builder, proved through a live FastMCP instance. | [test_mcp_registration_wiring.py](agents-remember/mcp/tests/test_mcp_registration_wiring.py) |
| The advertised-name and docstring-presence checks against a live server. | [test_tools.py](agents-remember/mcp/tests/test_tools.py) |
| `TaskRef` — the shared task locator three read-side tools pack. | [controllers/task_ref.py](agents-remember/mcp/src/agents_remember/controllers/task_ref.py) |

## Update History

- 2026-08-01T00:00+02:00 — No route impact: 260731-EFA-L4 touches exactly one file under this
  path, `closeout.py` (+16/-7), and the change is **entirely inside two published docstrings** —
  `worktree_closeout_preview` and `worktree_closeout_apply` now describe closeout's new
  stage-before-gate step and its two refusals (not a task worktree; unresolved merge conflicts).
  Proven rather than eyeballed: I parsed the file at `abc7cbcc` and at the current revision,
  stripped every module/class/function docstring from both syntax trees, and the two dumps are
  identical — so no signature, parameter, default, annotation, return type, decorator or
  forwarding call moved. That matters here more than elsewhere, because on this route **the
  signature IS the published JSON schema**: a docstring edit changes the model-visible
  description and nothing on the wire, which is exactly the split this overview's defining
  contract describes. The two tools stay in the `closeout.py` family, `TOOL_REGISTRARS` and the
  58-name `PUBLIC_TOOLS` set are untouched, and no new function entered the `PLR0913`-exempted
  path, so `ToolSignatureExemptionTests` sees the same AST it did before. This overview's
  claim that "the published docstring … carries the refusal vocabulary … in prose" is not
  merely still true — L4 is an instance of it. Verification metadata pinned until closeout
  stamps the L4 commit.
- 2026-07-31T15:31+02:00 — 260731-EFA-L2 curator: route created. The `@server.tool()` surface moved
  out of `server.py` into this package (12 family modules + `TOOL_REGISTRARS`), and the route
  records its defining contract — the signature IS the published MCP schema — together with the
  single `PLR0913` per-file-ignore that follows from it and the AST/`--ignore-noqa` suite that holds
  the carve-out shut. Verification metadata is pinned to the pre-change commit until closeout stamps
  the L2 code commit.
