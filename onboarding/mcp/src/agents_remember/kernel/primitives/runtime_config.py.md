# mcp/src/agents_remember/kernel/primitives/runtime_config.py

## Governing Overview

[kernel primitives overview](overview.md)

## Purpose

Trusted MCP authority configuration and per-use shared host settings. The retired `retirement`, `providers`, and `providerDegradation` sections (and `timeoutCaps.providerSetupSeconds`) load as unused data in `unused_settings_keys` rather than parsed policy.

## Code Commentary

### Current Contract

Legacy gateDelegation migration warnings are emitted once per authority-file-path/shadowed-state pair in the process, not at every configuration re-resolution. This clarification introduces neither a restored provider/benchmark tool nor a new settings or delegation authority.

### Logic

config_from_mapping resolves absolute coordinator/workspace/log paths, refuses authority inside coordinator, checks repository Git identities and builds repository, timeout, benchmark, dashboard, orchestration, tool-log, and `unused_settings_keys` values. McpRuntimeConfig carries unused_settings_keys; there is no RetirementSettings or retirement field. The host block is read from the shared authority per use, with the command config path attached, not treated as a boot snapshot or per-harness fallback. External memory remains mandatory and a removed internal-memory root is refused. The surviving legacy gateDelegation migration is not the removed agent plane.


`parse_dashboard_settings` (260703 L2) validates the optional `dashboard` object
into `McpRuntimeConfig.dashboard` — a frozen `DashboardSettings(auto_start=False,
port=DEFAULT_DASHBOARD_PORT=8765)`, so omitted settings keep supervision fully
off. It follows the `timeoutCaps` fail-loud discipline: keys outside
`KNOWN_DASHBOARD_FIELDS` (`autoStart`, `port`) are rejected (a typo like
`autostart` must surface at boot, not silently leave the daemon unsupervised),
`autoStart` must be a boolean, and `port` a non-bool integer in 1..65535.


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

- `load_authority_paseo_runtime` reads the authority file's `paseoRuntime` block from `configPath` on every use; the shared reader is retained, not a per-harness fallback. [20]

- [21]

- Current dashboard boot settings are DashboardSettings with auto_start=False and DEFAULT_DASHBOARD_PORT, not ProviderScope. [3]


- McpRuntimeConfig retains repository, timeout, dashboard, orchestration, tool-log and unused_settings_keys fields while retirement, providers and providerDegradation load only as unread unused sections. [6]


- DashboardSettings declares disabled-by-default auto_start and DEFAULT_DASHBOARD_PORT; this is dashboard configuration, not ProviderScope. [9]

- Legacy gateDelegation migration warnings are emitted once per authority-file-path/shadowed-state pair in the process, not at every configuration re-resolution. Retired retirement, providers, providerDegradation, and timeoutCaps.providerSetupSeconds keys load only as unread unused_settings_keys entries. This clarification introduces neither a restored provider/benchmark tool nor a new settings or delegation authority. [22]

## The host block the authority file holds

`harness_skill_root` is gone from `McpRuntimeConfig` and from settings parsing: no skill folder is resolved, so `infer_harness_skill_root` and the optional `harnessSkillRoot` key no longer exist. `paseo_runtime` reads the block from the file named by `config_path` on every use, and `load_paseo_runtime_settings` reads that same file, so the block a cold first run writes and the block every later call reads are the same bytes. An absent authority file is `no host configured` rather than an unreadable settings file — a cold root is exactly that state until a launch establishes the block — while an unreadable or malformed one is answered as a settings refusal with a recovery action.

- The per-use host block read from the named authority file. [23]
- The settings-file read that treats an absent authority file as no host. [24]
