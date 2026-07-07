# mcp/src/agents_remember/mcp/config.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/mcp/config.py`    |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-08T01:00+02:00 |
| lastVerifiedCommitHash | `9a0e6ca69ccc690fc0466db5051571fa2d9902dc` |
| lastVerifiedCommitDate | 2026-07-08T01:34:58+02:00|
| governingOverview      | `../../../overview.md`                     |

## Purpose

`config.py` loads and validates the trusted MCP authority settings.

## Code Commentary

### Logic

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

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Server registration consumes this config object. | [server.py](agents-remember/mcp/src/agents_remember/mcp/server.py) |
| Config tests cover authority rejection, harness-root inference, provider derivation, and include containment. | [test_config.py](agents-remember/mcp/tests/test_config.py) |
| The daemon supervisor consuming `DashboardSettings` (autoStart/port). | [serving/daemon.py](agents-remember/mcp/src/agents_remember/serving/daemon.py) |
| Gate delegation policy validation lives in controlplane. | [controlplane/gate_policy.py](agents-remember/mcp/src/agents_remember/controlplane/gate_policy.py) |
| The dedicated `providerDegradation` settings parser this file wraps into `ConfigError` (260707-HFX-L7). | [mcp/provider_degradation_settings.py](agents-remember/mcp/src/agents_remember/mcp/provider_degradation_settings.py) |
| The degradation detector consuming `McpRuntimeConfig.provider_degradation` every evaluation. | [providers/degradation.py](agents-remember/mcp/src/agents_remember/providers/degradation.py) |
| The agentic-settings loader supplying the boot-snapshot gateDelegation and the shared `parse_gate_delegation`. | [kernel/agentic_settings.py](agents-remember/mcp/src/agents_remember/kernel/agentic_settings.py) |
| Launch-authority consumers: worktree start, watcher/query gating, benchmark filtering, runtime rebind derivation. | [worktree_tools.py](agents-remember/mcp/src/agents_remember/controllers/worktree_tools.py); [provider_tools.py](agents-remember/mcp/src/agents_remember/controllers/provider_tools.py); [benchmark_tools.py](agents-remember/mcp/src/agents_remember/controllers/benchmark_tools.py); [install/runtime.py](agents-remember/mcp/src/agents_remember/install/runtime.py) |
| Containment tests pin the authority reload fail-closed semantics and the launch gate refusal/armed paths. | [test_provider_containment.py](agents-remember/mcp/tests/test_provider_containment.py) |

As of the 260703-L8 seam ruling `parse_gate_delegation` CONSUMES requireReviewerVerdictAtSeams: after building the policy it applies `apply_seam_verdict_requirement`, so delegated seam-kind rules (master-handover-approval) demand reviewer-verdict evidence — the flag is no longer parse-only.

## Update History

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
