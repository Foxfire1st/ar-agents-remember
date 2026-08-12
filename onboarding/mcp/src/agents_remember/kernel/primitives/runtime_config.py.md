# mcp/src/agents_remember/kernel/primitives/runtime_config.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/kernel/primitives/runtime_config.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-10T18:31+02:00    |
| lastVerifiedCommitHash | `c9ae4dbd8adb650f116b9d4f86343b496c3e5f32` |
| lastVerifiedCommitDate | 2026-08-12T17:53:40+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[kernel primitives overview](overview.md)

## Purpose

`kernel/primitives/runtime_config.py` (moved from `mcp/config.py` by 260731-EFA-L9, the leaf's
centre of gravity: 39 of 46 outside imports of `mcp` reached this one module) loads and validates
the trusted MCP authority settings. Kernel owns the record so every package above it can read the
same runtime configuration without importing the `mcp` package.

## Code Commentary

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
`RepositoryScope` no longer carries the field.

`parse_timeout_caps` validates the optional `timeoutCaps` object into the
`timeout_caps` map: every cap must be a non-negative integer, cap names outside
the `KNOWN_TIMEOUT_CAPS` allowlist (`providerSetupSeconds`, `toolSeconds`) are
fail-loud rejected so typos surface instead of being silently stored, and the
renamed `providerSeconds` key is fail-loud rejected with a `ConfigError`
directing callers to `providerSetupSeconds` (indexing and seed are now always
uncapped; only `providerSetupSeconds` is consumed by the runtime, `toolSeconds`
is a documented reserved cap). `parse_benchmarks_enabled` validates the optional
`benchmarksEnabled` flag (must be a boolean) into the `benchmarks_enabled`
field. The module defines the defaults `DEFAULT_PROVIDER_SETUP_SECONDS = 1800`
and `DEFAULT_DOCKER_CONTROL_SECONDS = 120`. All failures raise `ConfigError`,
now a member of the typed `AgentsRememberError` family (itself a `ValueError`
subclass), so the server fails loudly at startup on unsafe settings.

`config_from_mapping` (260707-HFX-L7) parses the optional `providerDegradation` block through
`agents_remember.mcp.provider_degradation_settings.parse_provider_degradation_settings`,
wrapping any `ProviderDegradationSettingsError` into `ConfigError` at the call site so the
boot fail-loud contract is unchanged; the result is stored on the new
`McpRuntimeConfig.provider_degradation` field (default `ProviderDegradationSettings()` — detector
enabled, failsafe armed, conservative thresholds). This follows the same fail-loud-allowlist
pattern as `timeoutCaps`/`dashboard` below, just with its own dedicated settings module rather
than an inline parser in this file.

`parse_dashboard_settings` (260703 L2) validates the optional `dashboard` object
into `McpRuntimeConfig.dashboard` — a frozen `DashboardSettings(auto_start=False,
port=DEFAULT_DASHBOARD_PORT=8765)`, so omitted settings keep supervision fully
off. It follows the `timeoutCaps` fail-loud discipline: keys outside
`KNOWN_DASHBOARD_FIELDS` (`autoStart`, `port`) are rejected (a typo like
`autostart` must surface at boot, not silently leave the daemon unsupervised),
`autoStart` must be a boolean, and `port` a non-bool integer in 1..65535.

`parse_orchestration_settings` (260703-L4, re-homed by 260703-L13) resolves the
boot-snapshot `orchestration.gateDelegation`. Its HOME is now the GLOBAL agentic
settings file (`<coordinationRoot>/system/settings.json`), read ONCE at boot
through `kernel/agentic_settings.load_agentic_settings` (per-use semantics do
not apply to this one key; a change needs a restart — documented). The parse
itself (`parse_gate_delegation` — named policy, per-kind overrides,
`requireReviewerVerdictAtSeams` via `apply_seam_verdict_requirement`) MOVED to
`kernel/agentic_settings.py` and is imported back; `AgenticSettingsError` is
wrapped into `ConfigError` so the boot contract is unchanged. An authority-file
`orchestration.gateDelegation` is honored as a ONE-CYCLE legacy fallback with a
`warnings.warn` boot warning naming the new home
(`_warn_legacy_gate_delegation`); when the global file also sets the key the
global value wins and the shadowed authority value warns as IGNORED. Every
other `orchestration.*` key in the authority file
(`KNOWN_AUTHORITY_ORCHESTRATION_FIELDS` = gateDelegation only) fails loud
pointing at the global file — including `roles`/`concurrency`, which were
previously reserved-and-silently-dropped (that trap is closed), and `loops`,
which never belonged there. Unknown keys, bad roles, human-pinned gate
delegation, and unsupported delegated kinds still raise `ConfigError` at
startup, whichever file they come from.

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

`parse_retirement_settings` (260707-HFX-L8, renamed by HFX2-L11) validates the optional `retirement`
object into `McpRuntimeConfig.retirement` — a frozen
`RetirementSettings(auto_land_on_integration=True, auto_land_on_finalize=True)`, both defaulting ON
per the developer ruling that successful completion should classify spent chats as landed/archive
without anyone remembering to clean them up. It follows the same fail-loud-unknown-key discipline as
`parse_dashboard_settings`: a non-dict `retirement` value, any key outside
`KNOWN_RETIREMENT_FIELDS` (`autoLandOnIntegration`, `autoLandOnFinalize`, and one-cycle legacy aliases
`autoRetireOnIntegration`, `autoRetireOnFinalize`), or a non-bool value for any present known field
raises `ConfigError`. When both a new and legacy key are present, the new `autoLandOn*` key wins.
The legacy aliases are deliberate compatibility, not defensive slop: existing authority files using
the HFX-L8 names would otherwise fail boot during this semantic rename. `config_from_mapping` calls
`parse_retirement_settings(data.get("retirement"))` and threads the result into the constructed
`McpRuntimeConfig`. This is a deliberate design choice, not an oversight: `retirement` stays a
LOCAL MCP-authority boot-snapshot setting (like `dashboard`), NOT the global agentic-orchestration
settings file (unlike `orchestration.gateDelegation`, which moved there in 260703-L13) — these are
per-process server-behavior toggles for THIS server's completion-edge hooks
(`worktree_integrate_tool`/`lifecycle_finalize_task_tool`'s `auto_complete_seats` calls in
`application/worktree_tools.py`), not portfolio-wide policy.

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
- `providerDegradation` accepts only the 15-key allowlist in
  `provider_degradation_settings.KNOWN_PROVIDER_DEGRADATION_FIELDS`; its defaults keep the
  degradation detector enabled with the critical failsafe armed at conservative thresholds, so
  existing settings files inherit the protection without an explicit opt-in.
- `orchestration.gateDelegation` defaults to all-human. Delegation is opt-in,
  validates through `controlplane.gate_policy`, and fail-loud rejects policies
  that would weaken human-pinned gate kinds.
- The gateDelegation home is the global agentic settings file (boot-snapshot);
  the authority-file value is a one-cycle legacy fallback that always warns.
  The `gate_policy` wiring downstream of `McpRuntimeConfig.orchestration` is
  unchanged by the re-homing.
- The boot-snapshot `providers` map is NOT launch authority (containment R1):
  launch-capable operations must go through
  `require_provider_launch_authority`, which re-reads the on-disk file
  fail-closed (unreadable/invalid ⇒ refusal, never a snapshot fallback).
  Stop/status/cleanup operations are never gated on the reload.
- `retirement` accepts only `KNOWN_RETIREMENT_FIELDS` (`autoLandOnIntegration`,
  `autoLandOnFinalize`, plus legacy `autoRetireOnIntegration`/`autoRetireOnFinalize` aliases) with
  the same fail-loud rejection as `dashboard`/`timeoutCaps`; both fields default to `True` —
  existing settings files with no `retirement` key keep auto-land ON, not off, unlike `dashboard`'s
  off-by-default posture.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The process entry point owns `load_config`; `create_server` receives the resulting typed config and passes it to application initialization and every tool registrar. | "def main(argv:"; "def create_server(config: McpRuntimeConfig) -> Any:" | mcp/src/agents_remember/mcp/server.py:51-73; mcp/src/agents_remember/mcp/server.py:32-46 |
| Config tests cover authority rejection, harness-root inference, provider derivation, and include containment. | `McpConfigTests` | mcp/tests/test_config.py:73-438 |
| `DashboardSettings` defines the boot-snapshot auto-start and port values; the daemon supervisor consumes them to gate autostart and choose the endpoint port. | `DashboardSettings`; `maybe_autostart_dashboard`; `_autostart` | mcp/src/agents_remember/kernel/primitives/runtime_config.py:90-95; mcp/src/agents_remember/serving/daemon.py:338-358; mcp/src/agents_remember/serving/daemon.py:361-366 |
| Gate delegation policy validation lives in controlplane. | `make_gate_policy`; `apply_seam_verdict_requirement` | mcp/src/agents_remember/kernel/primitives/gate_policy.py:75-107; mcp/src/agents_remember/kernel/primitives/gate_policy.py:130-149 |
| The dedicated `providerDegradation` parser validates the authority block and constructs typed settings. | `parse_provider_degradation_settings` | mcp/src/agents_remember/kernel/primitives/provider_degradation_settings.py:58-128 |
| `config_from_mapping` calls that parser and translates `ProviderDegradationSettingsError` into `ConfigError`. | `config_from_mapping` | mcp/src/agents_remember/kernel/primitives/runtime_config.py:241-290 |
| `evaluate_provider_degradation` consumes `config.provider_degradation` for enablement, sample limits, and classification thresholds on every evaluation. | `evaluate_provider_degradation`; `provider_degradation` | mcp/src/agents_remember/providers/degradation.py:268-323 |
| `load_agentic_settings` layers and merges agentic settings; `_parse_orchestration` applies the shared `parse_gate_delegation` parser to the resulting block. | `load_agentic_settings`; `_parse_orchestration`; "def parse_gate_delegation(" | mcp/src/agents_remember/kernel/_agentic_settings_policy.py:28-28; mcp/src/agents_remember/kernel/agentic_settings.py:209-244; mcp/src/agents_remember/kernel/agentic_settings.py:349-384 |
| `parse_orchestration_settings` supplies the global boot snapshot to `McpRuntimeConfig.orchestration`; its authority-file legacy path delegates to `_parse_legacy_authority_gate_delegation`, which uses the same gate parser. | `parse_orchestration_settings`; `_parse_legacy_authority_gate_delegation` | mcp/src/agents_remember/kernel/primitives/runtime_config.py:479-512; mcp/src/agents_remember/kernel/primitives/runtime_config.py:515-547 |
| `provider_watchers_tool` reloads live launch authority for start, restart, and index invalidation while status, stop, and shutdown remain deliberately ungated. | `provider_watchers_tool` | mcp/src/agents_remember/application/provider_tools.py:48-87 |
| The provider query funnel reloads launch authority for operations with a required provider and rejects a query when that specific provider is absent. | `_provider_operation_result`; `ProviderOperation.required_provider` | mcp/src/agents_remember/application/provider_tools.py:736-783 |
| Worktree start derives background provider setup from `reload_provider_authority`, skipping setup on disabled or unreadable live authority while still creating the worktree. | `worktree_start_tool` | mcp/src/agents_remember/application/worktree_tools.py:77-156 |
| Benchmark preparation and execution both pass provider ids from the live on-disk authority into their requests. | `codex_benchmark_prepare_tool`; `codex_benchmark_run_tool`; `_live_provider_ids` | mcp/src/agents_remember/application/benchmark_tools.py:64-84; mcp/src/agents_remember/application/benchmark_tools.py:137-144; mcp/src/agents_remember/application/benchmark_tools.py:87-134 |
| Runtime install derives provider dependency and watcher-rebind settings from the live on-disk authority. | `install_runtime`; `install_runtime_from_config` | mcp/src/agents_remember/install/runtime.py:462-553; mcp/src/agents_remember/install/runtime.py:556-615 |
| Containment tests pin the authority reload fail-closed semantics and the launch gate refusal/armed paths. | `ReloadProviderAuthorityTests`; `WorktreeStartVetoTests`; `QueryFunnelGateTests`; `RuntimeRebindDerivationTests`; `BenchmarkProviderFilterTests` | mcp/tests/test_provider_containment.py:78-121; mcp/tests/test_provider_containment.py:124-177; mcp/tests/test_provider_containment.py:180-196; mcp/tests/test_provider_containment.py:199-206; mcp/tests/test_provider_containment.py:209-273 |
| `RetirementSettings` defines the two default-on toggles; worktree integration and lifecycle finalization each consult the corresponding `config.retirement` flag before calling `auto_complete_seats`. | "class RetirementSettings:"; "def worktree_integrate_tool("; "def lifecycle_finalize_task_tool("; "def auto_complete_seats(" | mcp/src/agents_remember/application/completion_cleanup.py:29-29; mcp/src/agents_remember/application/worktree_tools.py:359-359; mcp/src/agents_remember/application/worktree_tools.py:514-514; mcp/src/agents_remember/kernel/primitives/runtime_config.py:109-109 |

As of the 260703-L8 seam ruling `parse_gate_delegation` CONSUMES requireReviewerVerdictAtSeams: after building the policy it applies `apply_seam_verdict_requirement`, so delegated seam-kind rules (master-handover-approval) demand reviewer-verdict evidence — the flag is no longer parse-only.

## Update History
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-10T18:31+02:00 — 260731-EFA-L21: `load_config` now selects a deterministic synthetic
  config for undeclared linked-checkout execution before reading caller-supplied settings, and
  refuses undeclared primary-checkout execution. Verification metadata remains pinned until
  approved closeout.

- 2026-08-04T03:26:26+02:00 — 260731-EFA-L6 S18-SR3-B06 curator: generated and source-inspected the seven configuration relationship groups (9 repairs, 2 normalisations, 0 declines); the runtime group was split across both install owners, and the locked final rerun was clean with frozen zero source/tokenize/parse/build telemetry.
- 2026-08-04T03:03:23+02:00 — 260731-EFA-L6 S18-SR3-B06 worker: corrected seven
  underbound relationship groups without changing their approved meaning: server config ownership;
  degradation parsing/translation; agentic/global-versus-legacy orchestration loading; watcher
  gating; worktree setup; benchmark filtering; and runtime install derivation. Cross-owner groups
  were split where needed, and every changed binding is a provisional `:1-1` input for the fresh
  Luna curator; no citation mechanics ran.
- 2026-08-04T02:20:03+02:00 — 260731-EFA-L6 S18-B06 curator delta: repaired the scoped citations against the frozen source snapshot; generated ranges were inspected and the managed index remained warm/frozen with zero source reads, tokenization, parsing, and build.

- 2026-08-04T00:59:36+02:00 — 260731-EFA-L6 S18-SR1 worker correction: source-first repaired the
  seven B06 configuration relationship groups. Loading is owned by `main`/`load_config`; daemon,
  provider-degradation, boot-snapshot gate-delegation, live provider-authority funnels, and both
  retirement hooks now point to their actual consumers. New or rewritten bindings remain honest
  `:1-1` inputs for the later scoped fixer; preserved the prior B06 entry and ran no citation
  mechanics. Verification metadata remains pinned until closeout stamps the L6 code commit.
- 2026-08-04T00:28:23+02:00 — 260731-EFA-L6 S18-B06 curator: repaired and normalized the scoped configuration citations; final exact frozen-snapshot check is clean.
- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-31T15:31+02:00 — 260731-EFA-L2 curator: **mechanical only, attested unchanged.** The
  file's diff against `c1dc505` is two `ruff format` line rewraps —
  `require_provider_launch_authority`'s parameter list and one
  `_warn_legacy_gate_delegation(...)` call — with no behaviour, signature, key, or default touched.
  Every claim in this sidecar was re-checked against the current source and still holds; the prose
  was deliberately not rewritten. (The whole-tree reformat is commit `00e8379`.)
- 2026-07-09T13:07+02:00 — 260707-HFX2-L11 (landed chat archive): renamed the completion toggles to
  `auto_land_on_integration`/`auto_land_on_finalize` and the settings keys to
  `autoLandOnIntegration`/`autoLandOnFinalize`. The parser still accepts HFX-L8's
  `autoRetireOnIntegration`/`autoRetireOnFinalize` aliases so already-written authority files do not
  fail boot during the semantic rename; the new keys take precedence when both are present.
  Verification metadata remains pinned until closeout stamps the HFX2-L11 commit.

- 2026-07-08T02:55+02:00 — 260707-HFX-L8 (seat lifecycle: retirement + live identity +
  turn-state): added `KNOWN_RETIREMENT_FIELDS`, the frozen `RetirementSettings` dataclass
  (`auto_retire_on_integration`/`auto_retire_on_finalize`, both default `True`), the
  `McpRuntimeConfig.retirement` field, and `parse_retirement_settings` (same fail-loud-unknown-key
  pattern as `parse_dashboard_settings`); `config_from_mapping` now threads
  `parse_retirement_settings(data.get("retirement"))` into the constructed config. `retirement`
  deliberately stays a local MCP-authority boot-snapshot setting, not the global agentic settings
  file. Verification metadata pinned until closeout stamps the HFX-L8 commit.
- 2026-07-08T01:00+02:00 — 260707-HFX-L7 route impact (small): `config_from_mapping` now parses
  the optional `providerDegradation` block through the new dedicated
  `provider_degradation_settings.parse_provider_degradation_settings` (wrapped into `ConfigError`)
  and stores it on the new `McpRuntimeConfig.provider_degradation` field
  (default `ProviderDegradationSettings()`). No change to any existing field's parsing behavior.
  Verification metadata pinned until closeout stamps the HFX-L7 commit.
- 2026-07-07T16:30+02:00 — 260707-HFX-L1 (provider containment R1): added `ProviderAuthority`,
  `reload_provider_authority` (re-reads only the providers map from the authority file;
  unreadable/invalid ⇒ empty map + `error`, fail-closed), and
  `require_provider_launch_authority` (refuses with `ConfigError` when the disk disables
  providers or cannot be read; returns the live-map config when armed). Verification metadata
  pinned until closeout stamps the HFX-L1 commit.

- 2026-07-07T12:50+02:00 — No content impact: L16's config.py change is message-wording only (the boot error/warning text now points at the harnesses manual); the parsing behavior and the boot-snapshot contract this sidecar describes are unchanged (review L16R-4 concurred the body is not stale).

- 2026-07-07T09:45+02:00 — 260703-L16 (spawn knob application, message-only): the authority-file
  unsupported-`orchestration.*` refusal now enumerates the grown agentic family
  (gateDelegation, loops, roles, rolesPerLevel, concurrency, spawn, harnesses) when pointing at the
  global settings file. No parsing behavior changed. Verification metadata pinned until closeout
  stamps the L16 commit.

- 2026-07-06T22:20+02:00 — 260703-L13 (settings unification): gateDelegation re-homed to the
  global agentic settings file (boot-snapshot through the kernel loader; authority-file value
  = one-cycle legacy fallback with a boot warning, shadowed values warn as IGNORED); the
  gate-delegation parse functions moved to `kernel/agentic_settings.py`; authority-file
  `orchestration` now accepts gateDelegation ONLY (roles/concurrency/loops fail loud naming
  the new home — the silent-drop trap closed); the dead `memorySettingsIncludes` plumbing and
  `parse_path_list` removed (leftover keys tolerated-ignored). Verification metadata pinned
  until closeout stamps the L13 commit.
- 2026-07-05T16:30+02:00 - L8 seam-ruling remediation (cycle 4): requireReviewerVerdictAtSeams wired through the parse path (no longer inert). Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-04T12:32+02:00 — 260703-L4: added optional
  `orchestration.gateDelegation` parsing into `OrchestrationSettings`, defaulting
  to all-human and fail-loud validating delegated roles, reviewer-verdict
  requirements, and human-pinned kinds. Verification metadata pinned until
  closeout stamps the L4 commit.
- 2026-07-03T11:40+02:00 — 260703 L2: added the optional `dashboard` settings object —
  `parse_dashboard_settings` → frozen `DashboardSettings(auto_start, port)` on
  `McpRuntimeConfig.dashboard`, `KNOWN_DASHBOARD_FIELDS` fail-loud allowlist,
  `DEFAULT_DASHBOARD_PORT = 8765`; defaults keep supervision off. Verification metadata pinned
  until closeout stamps the code commit.
- 2026-05-31T12:30+02:00 — `timeoutCaps` now rejects unknown cap names via the `KNOWN_TIMEOUT_CAPS` allowlist (`providerSetupSeconds`, `toolSeconds`); added the boolean `benchmarksEnabled`/`benchmarks_enabled` flag (`parse_benchmarks_enabled`); `ConfigError` now subclasses the typed `AgentsRememberError` family rather than `ValueError` directly (1.0.0 review remediation).
- 2026-05-30T21:33+02:00: Documented `timeoutCaps` handling added in the 0.9.x run — `parse_timeout_caps` (non-negative-int caps), the fail-loud `ConfigError` on the renamed `providerSeconds` key, the `providerSetupSeconds`/`DEFAULT_PROVIDER_SETUP_SECONDS`/`DEFAULT_DOCKER_CONTROL_SECONDS` defaults, and the `ConfigError` (ValueError) contract. Verified against `8927f03`.
- 2026-05-29T18:35+02:00: Extracted `_parse_repository_entry` from `parse_repositories` to reduce complexity; behavior-preserving (commit `e3dab63`).
- 2026-05-28T12:32+02:00: Updated after transcript roots defaulted to `logs/mcp` and provider log roots moved under `logs/providers/`.
- 2026-05-24T09:23+02:00: Updated after config coverage switched the normal Codex harness placement from `.agents/mcp` to `.codex/mcp`.
- 2026-05-23T18:05+02:00: Created during direct closeout prep after MCP settings became the only authority route.
