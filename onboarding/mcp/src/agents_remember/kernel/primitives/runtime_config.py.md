# mcp/src/agents_remember/kernel/primitives/runtime_config.py

## Governing Overview

[kernel primitives overview](overview.md)

## Purpose

`kernel/primitives/runtime_config.py` (moved from `mcp/config.py` by 260731-EFA-L9, the leaf's
centre of gravity: 39 of 46 outside imports of `mcp` reached this one module) loads and validates
the trusted MCP authority settings. Kernel owns the record so every package above it can read the
same runtime configuration without importing the `mcp` package.

Builds configured repository/provider authority and optional runtime settings.

## Code Commentary

### Current Contract

Legacy gateDelegation migration warnings are emitted once per authority-file-path/shadowed-state pair in the process, not at every configuration re-resolution. Provider degradation parsing belongs to kernel/primitives/provider_degradation_settings.py. This clarification introduces neither a restored provider/benchmark tool nor a new settings or delegation authority.

### Logic

Before authority-path validation, `load_config` asks the checkout-coordination primitive whether
this is undeclared code loaded from an Agents Remember checkout. A linked task worktree receives
`_checkout_runtime_config`: a synthetic, non-authority record rooted exactly at
`<worktree-group>/provider-runtime/dev-ar-coordination`, with the candidate checkout registered as
`agents-remember`, a dummy external-memory root below that coordinator, and providers, dashboard
autostart, benchmarks, and automatic retirement disabled. The supplied settings file is not read,
so a live `coordinationRoot`/`workspaceRoot` cannot redirect candidate CLI code. No coordinator is
copied. An undeclared primary checkout raises `ConfigError`; declared MCP/dashboard and explicit
pytest modes continue through the ordinary authority loader. An installed wheel has no owning Git
checkout and also keeps the ordinary loader.

The loader requires an absolute JSON settings path, rejects coordinator
`system/settings.json` as an authority file, rejects settings located inside the
coordinator root, defaults omitted transcript roots to `logs/mcp`, parses
configured repositories, derives default memory roots, parses optional contract
paths inside the coordinator, infers harness skill roots from harness-local
`mcp/<settings>.json` placement such as `.codex/mcp/<settings>.json`, derives
provider runtime roots under `providers/runners/<provider>/<instance>` and
provider log roots under `logs/providers/<provider>/<instance>`, and exposes
sorted allowed repo/provider ids. The former
`repositories.<id>.memorySettingsIncludes` parse (dead plumbing — parsed, never
consumed) was REMOVED with 260703-L13: a leftover key in an existing settings
file is tolerated-ignored like any other unknown repository field, and
`RepositoryScope` no longer carries the field. CCR-R22@v1 (L22, commit `685f83c44055`) adds the optional `certification_profile: Path | None` repository field: `_parse_repository_entry` reads `certificationProfile` through `_optional_repository_profile_reference`, which requires exactly one non-empty canonical, traversal-free, repository-relative POSIX path (absolute, drive, backslash, dot-segment, or trailing-slash references raise `ConfigError`); an absent key keeps `None`. `RepositoryScope.certification_profile` then reaches the lifecycle worker and worktree tools, which forward it as the profile authority for code-certifying operations.

`parse_timeout_caps` validates the optional `timeoutCaps` object into the
`timeout_caps` map: every cap must be a non-negative integer, cap names outside
the `KNOWN_TIMEOUT_CAPS` allowlist (`providerSetupSeconds`, `toolSeconds`) are
fail-loud rejected so typos surface instead of being silently stored, and the
renamed `providerSeconds` key is fail-loud rejected with a `ConfigError`
directing callers to `providerSetupSeconds` (indexing and seed are now always
uncapped; only `providerSetupSeconds` is consumed by the runtime, `toolSeconds`
is a documented reserved cap). `parse_benchmarks_enabled` validates the optional
`benchmarksEnabled` flag (must be a boolean) into the `benchmarks_enabled`
field. The retired `directExecutionEnabled` key is ignored for every supplied value, including non-booleans; it creates no configuration field or parser. A trusted settings load that includes it issues one logger.warning naming the key/file and the developer dashboard or architect grant route. Direct permission comes from the task grant read at the call, not settings or a harness restart. The module defines the defaults `DEFAULT_PROVIDER_SETUP_SECONDS = 1800`
and `DEFAULT_DOCKER_CONTROL_SECONDS = 120`. All failures raise `ConfigError`,
now a member of the typed `AgentsRememberError` family (itself a `ValueError`
subclass), so the server fails loudly at startup on unsafe settings.

`config_from_mapping` (260707-HFX-L7) parses the optional `providerDegradation` block through
`agents_remember.kernel.primitives.provider_degradation_settings.parse_provider_degradation_settings`,
wrapping any `ProviderDegradationSettingsError` into `ConfigError` at the call site so the
boot fail-loud contract is unchanged; the result is stored on the new
`McpRuntimeConfig.provider_degradation` field (default `ProviderDegradationSettings()` — detector
enabled, failsafe armed, conservative thresholds). This follows the same fail-loud-allowlist
pattern as `timeoutCaps`/`dashboard` below, just with its own dedicated settings module rather
than an inline parser in this file.

> **Retained historical source account — superseded by the current contract:**
> `config_from_mapping` (260707-HFX-L7) parses the optional `providerDegradation` block through
> `agents_remember.mcp.provider_degradation_settings.parse_provider_degradation_settings`,
> wrapping any `ProviderDegradationSettingsError` into `ConfigError` at the call site so the
> boot fail-loud contract is unchanged; the result is stored on the new
> `McpRuntimeConfig.provider_degradation` field (default `ProviderDegradationSettings()` — detector
> enabled, failsafe armed, conservative thresholds). This follows the same fail-loud-allowlist
> pattern as `timeoutCaps`/`dashboard` below, just with its own dedicated settings module rather
> than an inline parser in this file.

`parse_dashboard_settings` (260703 L2) validates the optional `dashboard` object
into `McpRuntimeConfig.dashboard` — a frozen `DashboardSettings(auto_start=False,
port=DEFAULT_DASHBOARD_PORT=8765)`, so omitted settings keep supervision fully
off. It follows the `timeoutCaps` fail-loud discipline: keys outside
`KNOWN_DASHBOARD_FIELDS` (`autoStart`, `port`) are rejected (a typo like
`autostart` must surface at boot, not silently leave the daemon unsupervised),
`autoStart` must be a boolean, and `port` a non-bool integer in 1..65535.

> **Retained historical source account — superseded by the current contract:**
> `parse_orchestration_settings` (260703-L4, re-homed by 260703-L13) resolves the
> boot-snapshot `orchestration.gateDelegation`. Its HOME is now the GLOBAL user agentic
> settings file (`~/.config/agents-remember/settings.json`, under `XDG_CONFIG_HOME` when set), read ONCE at boot
> through `kernel/agentic_settings.load_agentic_settings` (per-use semantics do
> not apply to this one key; a change needs a restart — documented). The parse
> itself (`parse_gate_delegation` — named policy, per-kind overrides,
> `requireReviewerVerdictAtSeams` via `apply_seam_verdict_requirement`) MOVED to
> `kernel/agentic_settings.py` and is imported back; `AgenticSettingsError` is
> wrapped into `ConfigError` so the boot contract is unchanged. An authority-file
> `orchestration.gateDelegation` is honored as a ONE-CYCLE legacy fallback with a
> `warnings.warn` boot warning naming the new home
> (`_warn_legacy_gate_delegation`); when the global file also sets the key the
> global value wins and the shadowed authority value warns as IGNORED. Every
> other `orchestration.*` key in the authority file
> (`KNOWN_AUTHORITY_ORCHESTRATION_FIELDS` = gateDelegation only) fails loud
> pointing at the global file — including `roles`/`concurrency`, which were
> previously reserved-and-silently-dropped (that trap is closed), and `loops`,
> which never belonged there. Unknown keys, bad roles, human-pinned gate
> delegation, and unsupported delegated kinds still raise `ConfigError` at
> startup, whichever file they come from.

`ProviderAuthority` / `reload_provider_authority` / `require_provider_launch_authority`
(containment R1, task 260707-HFX-L1) make the on-disk settings file — not the
boot snapshot — the provider launch authority. A server process loads its
config once and closes over it, so editing the authority file to
`"providers": {}` (the operator's only fleet-wide kill-switch) previously
changed nothing until every running server restarted.
`reload_provider_authority(config)` re-reads ONLY the providers map from
`config.config_path` (through the same `parse_providers`, against the boot
config's coordination/workspace roots) into the frozen `ProviderAuthority`
dataclass; an unreadable file, a non-object root, or a `ConfigError` from the
parse yields an empty map with the reason in the `error` field — fail-closed,
callers must treat that as "no launch authority" and never fall back to the
snapshot. `ProviderAuthority.apply(config)` returns the boot config with the
live providers map swapped in (`dataclasses.replace`).
`require_provider_launch_authority(config, operation=...)` is the gate
launch-capable operations call: it raises `ConfigError` when the read failed
or when the live map is empty (the refusal names the operation, the authority
path, and the stale boot-snapshot ids) and returns the live-map config when
armed. Stop/status/cleanup paths must not call it — stopping is always legal.

`parse_retirement_settings` (introduced by 260707-HFX-L8; edge gates renamed by HFX2-L11)
validates the optional `retirement` object into `McpRuntimeConfig.retirement` — a frozen
`RetirementSettings(auto_land_on_integration=True, auto_land_on_finalize=True,
auto_close_completed_seats=True)`. The two historical `autoLandOn*` names remain completion-edge
gates; `autoCloseCompletedSeats` selects the cleanup mode when an enabled edge succeeds.
By default, cleanup retires eligible report-bearing Worker/Reviewer/Curator seats and frees their
tmux processes; seats without the exact qualified leaf's durable turn report are deferred.
Setting only `autoCloseCompletedSeats` to `False` restores the prior landed/archive mode, not
cleanup-off. A non-dict `retirement` value, any key outside `KNOWN_RETIREMENT_FIELDS`
(`autoLandOnIntegration`, `autoLandOnFinalize`, `autoCloseCompletedSeats`, and the one-cycle
legacy aliases `autoRetireOnIntegration`, `autoRetireOnFinalize`), or a non-bool value for any
present known field raises `ConfigError`. When both a new and legacy edge key are present,
the new `autoLandOn*` key wins. The aliases preserve HFX-L8 authority-file compatibility. `config_from_mapping` calls
`parse_retirement_settings(data.get("retirement"))` and threads the result into the constructed
`McpRuntimeConfig`. This is a deliberate design choice, not an oversight: `retirement` stays a
LOCAL MCP-authority boot-snapshot setting (like `dashboard`), NOT the global agentic-orchestration
settings file (unlike `orchestration.gateDelegation`, which moved there in 260703-L13) — these are
per-process server-behavior toggles for THIS server's completion-edge hooks
(`worktree_integrate_tool`/`lifecycle_finalize_task_tool`'s `auto_complete_seats` calls in
`application/worktree_tools.py`), not portfolio-wide policy.

### Tool-call log settings (MIK-R108 rule 3)

The optional `toolLog` family (`ToolLogSettings`, parsed by `parse_tool_log_settings` with the same
fail-loud-unknown-key discipline: `keepDays`, `maxBytes`, `enclosureMaxBytes`, 14 days / 256 MiB /
64 MiB when absent) bounds the coordination-root log and each enclosure's `logs/`. `config_from_mapping`
threads it into `McpRuntimeConfig.tool_log`, from where the log writer reads its keeping and budgets.

### Invariants And Boundaries

- MCP settings are the authority for the server path.
- Coordinator files may teach agents what to ask for, but they do not grant MCP
  authority.
- Provider path fields are derived by the server, not repeated in settings.
- `timeoutCaps.providerSetupSeconds` caps only provider setup (image build /
  dependency install); seed/clone/indexing are never time-capped. The old
  `providerSeconds` key must keep being rejected, not silently mapped.
- `timeoutCaps` accepts only the `KNOWN_TIMEOUT_CAPS` allowlist
  (`providerSetupSeconds`, `toolSeconds`); any other cap name is rejected, so
  unknown keys are never silently stored and ignored.
- `dashboard` accepts only `KNOWN_DASHBOARD_FIELDS` (`autoStart`, `port`) with the
  same fail-loud rejection; its defaults keep dashboard supervision off, so
  existing settings files are untouched by the feature.
- `providerDegradation` accepts only the 16-key allowlist in
  `kernel.primitives.provider_degradation_settings.KNOWN_PROVIDER_DEGRADATION_FIELDS`, including
  `recentSampleLimit` (positive integer; default 120). Its defaults keep the degradation detector
  enabled with the critical failsafe armed at conservative thresholds, so existing settings files
  inherit the protection without an explicit opt-in.
- `orchestration.gateDelegation` defaults to all-human. Delegation is opt-in,
  validates through `controlplane.gate_policy`, and fail-loud rejects policies
  that would weaken human-pinned gate kinds.
- The gateDelegation home is the user agentic settings file (boot-snapshot);
  the authority-file value is a one-cycle legacy fallback that always warns. `require_config_path` refuses the user settings file as an MCP `--config` authority alongside the coordinator `system/settings.json` refusal.
  The `gate_policy` wiring downstream of `McpRuntimeConfig.orchestration` is
  unchanged by the re-homing.
- The boot-snapshot `providers` map is NOT launch authority (containment R1):
  launch-capable operations must go through
  `require_provider_launch_authority`, which re-reads the on-disk file
  fail-closed (unreadable/invalid ⇒ refusal, never a snapshot fallback).
  Stop/status/cleanup operations are never gated on the reload.
- `retirement` accepts only `KNOWN_RETIREMENT_FIELDS` (`autoLandOnIntegration`,
  `autoLandOnFinalize`, `autoCloseCompletedSeats`, plus legacy
  `autoRetireOnIntegration`/`autoRetireOnFinalize` aliases), with fail-loud key/type validation.
  All three typed fields default to `True`: omitted settings enable completion-edge cleanup in
  retire-and-free mode. `autoCloseCompletedSeats=False` keeps the enabled edge gates but selects
  landed/archive behavior. Cleanup runs only after successful non-dry-run completion, and the
  automatic role boundary excludes Manager and Orchestrator seats.

### Role Runtime and Scope

McpRuntimeConfig includes optional typed paseo_runtime while config_from_mapping preserves MIK existing authority. load_paseo_runtime_settings reads only the named block for runtime commands, bypassing no coordination authority because those commands own no coordination state. The former host block has no execution field/parser and follows unknown top-level-key behavior. Preserve provider degradation and repository identity rules.

## Evidence

### Repo-Internal References

- The process entry point owns `load_config`; `create_server` receives the resulting typed config and passes it to application initialization and every tool registrar. [1]
- Config tests cover authority rejection, harness-root inference, provider derivation, and include containment. [2]
- `DashboardSettings` defines the boot-snapshot auto-start and port values; the daemon supervisor consumes them to gate autostart and choose the endpoint port. [3]
- Gate delegation policy validation lives in controlplane. [4]
- The dedicated `providerDegradation` parser validates the authority block and constructs typed settings. [5]
- `config_from_mapping` calls that parser and translates `ProviderDegradationSettingsError` into `ConfigError`. [6]
- `evaluate_provider_degradation` consumes `config.provider_degradation` for enablement, sample limits, and classification thresholds on every evaluation. [7]
- `load_agentic_settings` layers and merges agentic settings; `_parse_orchestration` applies the shared `parse_gate_delegation` parser to the resulting block. [8]
- `parse_orchestration_settings` supplies the global boot snapshot to `McpRuntimeConfig.orchestration`; its authority-file legacy path delegates to `_parse_legacy_authority_gate_delegation`, which uses the same gate parser. [9]
- Runtime install takes dependency inputs through lifecycle_settings_from_config and retains separate watcher outcome reporting; these are the actual install owners. [14]

<details>
<summary>Historical retired provider/benchmark consumers — not current owners</summary>



- Worktree start derives background provider setup from `reload_provider_authority`, skipping setup on disabled or unreadable live authority while still creating the worktree. [12]


The provider_tools.py and benchmark_tools.py owners named by these retained historical references are absent from the current candidate; those citations preserve the older declared blobs only, not live call surfaces. reload_provider_authority and worktree setup remain distinct surviving owners.
</details>

| Retirement settings declare two default-on edge gates and the default-on retire-mode selector. | `RetirementSettings` | mcp/src/agents_remember/kernel/primitives/runtime_config.py:128-139 |
| Integration consults its retirement edge gate after successful non-dry-run completion. | `worktree_integrate_tool` | mcp/src/agents_remember/application/worktree_tools.py:535-543 |
| Finalization consults its retirement edge gate after successful non-dry-run completion. | `lifecycle_finalize_task_tool` | mcp/src/agents_remember/application/worktree_tools.py:977-986 |
| Seat cleanup selects report-gated retirement or the prior landed/archive mode and remains subordinate to successful completion. | `auto_complete_seats` | mcp/src/agents_remember/application/completion_cleanup.py:25-71 |

As of the 260703-L8 seam ruling `parse_gate_delegation` CONSUMES requireReviewerVerdictAtSeams: after building the policy it applies `apply_seam_verdict_requirement`, so delegated seam-kind rules (master-handover-approval) demand reviewer-verdict evidence — the flag is no longer parse-only.

### Runtime Source References

- Frozen implementation of McpRuntimeConfig supporting the stated file behavior. [15]
- Frozen implementation of config_from_mapping supporting the stated file behavior. [16]
- Frozen implementation of load_paseo_runtime_settings supporting the stated file behavior. [17]
- Runs all three commands without the block and checks named refusal, exit two and no process operation. [18]

## 260815-DAG-L4 Authority Boundary

L4 routes this file's existing application, configuration, task, model, registration, or memory responsibility through the shared task-derived integration authority. The change preserves the file's owning altitude while ensuring protected code and external-memory refs cannot be mutated through an ordinary workbench or unjournaled helper.

## 260928-MIK-L96 The shared host authority read per use

`load_paseo_runtime_settings` reads the host block from the file the config names, and the new `paseo_authority` reader delegates to `require_user_settings_path` at each call, so the single user-path file supplies the host block, the old `<coordinationRoot>/system/settings.json` is refused, and a block added after a server started is used without a restart. An old per-harness block is ignored with an explicit migration warning and no fallback.

- The host settings read the config exposes. [19]
- The shared authority reader. [20]

- The retired settings key is ignored and warned; current grants are not a runtime-config field. [21]

- Legacy gateDelegation migration warnings are emitted once per authority-file-path/shadowed-state pair in the process, not at every configuration re-resolution. Provider degradation parsing belongs to kernel/primitives/provider_degradation_settings.py. This clarification introduces neither a restored provider/benchmark tool nor a new settings or delegation authority. [22]
