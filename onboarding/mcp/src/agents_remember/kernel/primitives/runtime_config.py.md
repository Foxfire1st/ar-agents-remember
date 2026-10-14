# mcp/src/agents_remember/kernel/primitives/runtime_config.py

## Governing Overview

[kernel primitives overview](overview.md)

## Purpose

Trusted MCP authority configuration and per-use shared host settings. The retired retirement section loads as unused data, not as parsed cleanup policy.

## Code Commentary

### Current Contract

Legacy gateDelegation migration warnings are emitted once per authority-file-path/shadowed-state pair in the process, not at every configuration re-resolution. Provider degradation parsing belongs to kernel/primitives/provider_degradation_settings.py. This clarification introduces neither a restored provider/benchmark tool nor a new settings or delegation authority.

### Logic

config_from_mapping resolves absolute coordinator/workspace/log paths, refuses authority inside coordinator, checks repository Git identities and builds retained provider, timeout, dashboard, orchestration, degradation and tool-log values. McpRuntimeConfig carries unused_settings_keys; there is no RetirementSettings or retirement field. The host block is read from the shared authority per use, with the command config path attached, not treated as a boot snapshot or per-harness fallback. Provider launch authority remains an on-disk fail-closed reread; stopping/cleanup does not require launch authority. External memory remains mandatory and a removed internal-memory root is refused. The surviving legacy gateDelegation migration is not the removed agent plane.

`config_from_mapping` (260707-HFX-L7) parses the optional `providerDegradation` block through
`agents_remember.kernel.primitives.provider_degradation_settings.parse_provider_degradation_settings`,
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

### Tool-call log settings (MIK-R108 rule 3)

The optional `toolLog` family (`ToolLogSettings`, parsed by `parse_tool_log_settings` with the same
fail-loud-unknown-key discipline: `keepDays`, `maxBytes`, `enclosureMaxBytes`, 14 days / 256 MiB /
64 MiB when absent) bounds the coordination-root log and each enclosure's `logs/`. `config_from_mapping`
threads it into `McpRuntimeConfig.tool_log`, from where the log writer reads its keeping and budgets.



## Evidence boundary

This account is current source interpretation only. It creates no executed test/host/bootstrap result and supplies no new CODE or MEMORY grade.

## Source-bound reference inputs

### Runtime Source References

- [15]
- [16]
- [17]
- [19]
- [20]
- [21]
- Current dashboard boot settings are DashboardSettings with auto_start=False and DEFAULT_DASHBOARD_PORT, not ProviderScope. [3]
- [5]
- [6]
- DashboardSettings declares disabled-by-default auto_start and DEFAULT_DASHBOARD_PORT; this is dashboard configuration, not ProviderScope. [9]

- Legacy gateDelegation migration warnings are emitted once per authority-file-path/shadowed-state pair in the process, not at every configuration re-resolution. Provider degradation parsing belongs to kernel/primitives/provider_degradation_settings.py. This clarification introduces neither a restored provider/benchmark tool nor a new settings or delegation authority. [22]
