# mcp/src/agents_remember/mcp/config.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/mcp/config.py`    |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-04T12:32+02:00|
| lastVerifiedCommitHash | `7679eb76a4c3137f7a4a5e02e455e7759f9d9c19` |
| lastVerifiedCommitDate | 2026-07-04T12:58:55+02:00|
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
sorted allowed repo/provider ids.

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

`parse_dashboard_settings` (260703 L2) validates the optional `dashboard` object
into `McpRuntimeConfig.dashboard` — a frozen `DashboardSettings(auto_start=False,
port=DEFAULT_DASHBOARD_PORT=8765)`, so omitted settings keep supervision fully
off. It follows the `timeoutCaps` fail-loud discipline: keys outside
`KNOWN_DASHBOARD_FIELDS` (`autoStart`, `port`) are rejected (a typo like
`autostart` must surface at boot, not silently leave the daemon unsupervised),
`autoStart` must be a boolean, and `port` a non-bool integer in 1..65535.

`parse_orchestration_settings` (260703-L4) validates the optional
`orchestration` object into `McpRuntimeConfig.orchestration`. The L4 field is
`gateDelegation`: omitted means `DEFAULT_GATE_POLICY` (all-human). It accepts a
built-in `policy` name (`all-human` or `manager-decides-leaf-gates`), optional
per-kind overrides under `kinds`, and
`requireReviewerVerdictAtSeams`. Per-kind entries may be a role string or an
object with `role` and `requireReviewerVerdict`; unknown keys, bad roles,
human-pinned gate delegation, and unsupported delegated kinds raise
`ConfigError` at startup.

### Invariants And Boundaries

- MCP settings are the authority for the server path.
- Coordinator files may teach agents what to ask for, but they do not grant MCP
  authority.
- Provider path fields are derived by the server, not repeated in settings.
- Memory settings includes must stay inside the configured code repo or memory
  repo boundaries.
- `timeoutCaps.providerSetupSeconds` caps only provider setup (image build /
  dependency install); seed/clone/indexing are never time-capped. The old
  `providerSeconds` key must keep being rejected, not silently mapped.
- `timeoutCaps` accepts only the `KNOWN_TIMEOUT_CAPS` allowlist
  (`providerSetupSeconds`, `toolSeconds`); any other cap name is rejected, so
  unknown keys are never silently stored and ignored.
- `dashboard` accepts only `KNOWN_DASHBOARD_FIELDS` (`autoStart`, `port`) with the
  same fail-loud rejection; its defaults keep dashboard supervision off, so
  existing settings files are untouched by the feature.
- `orchestration.gateDelegation` defaults to all-human. Delegation is opt-in,
  validates through `controlplane.gate_policy`, and fail-loud rejects policies
  that would weaken human-pinned gate kinds.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Server registration consumes this config object. | [server.py](agents-remember/mcp/src/agents_remember/mcp/server.py) |
| Config tests cover authority rejection, harness-root inference, provider derivation, and include containment. | [test_config.py](agents-remember/mcp/tests/test_config.py) |
| The daemon supervisor consuming `DashboardSettings` (autoStart/port). | [serving/daemon.py](agents-remember/mcp/src/agents_remember/serving/daemon.py) |
| Gate delegation policy validation lives in controlplane. | [controlplane/gate_policy.py](agents-remember/mcp/src/agents_remember/controlplane/gate_policy.py) |

## Update History

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
