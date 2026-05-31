# mcp/src/agents_remember/mcp/config.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/mcp/config.py`    |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-31T12:30+02:00|
| lastVerifiedCommitHash | `c20a3292e667d227a3be0c1fb276f8a701df814f` |
| lastVerifiedCommitDate | 2026-05-31T14:17:11+02:00|
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

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Server registration consumes this config object. | [server.py](agents-remember-md/mcp/src/agents_remember/mcp/server.py) |
| Config tests cover authority rejection, harness-root inference, provider derivation, and include containment. | [test_config.py](agents-remember-md/mcp/tests/test_config.py) |

## Update History

- 2026-05-31T12:30+02:00 — `timeoutCaps` now rejects unknown cap names via the `KNOWN_TIMEOUT_CAPS` allowlist (`providerSetupSeconds`, `toolSeconds`); added the boolean `benchmarksEnabled`/`benchmarks_enabled` flag (`parse_benchmarks_enabled`); `ConfigError` now subclasses the typed `AgentsRememberError` family rather than `ValueError` directly (1.0.0 review remediation).
- 2026-05-30T21:33+02:00: Documented `timeoutCaps` handling added in the 0.9.x run — `parse_timeout_caps` (non-negative-int caps), the fail-loud `ConfigError` on the renamed `providerSeconds` key, the `providerSetupSeconds`/`DEFAULT_PROVIDER_SETUP_SECONDS`/`DEFAULT_DOCKER_CONTROL_SECONDS` defaults, and the `ConfigError` (ValueError) contract. Verified against `8927f03`.
- 2026-05-29T18:35+02:00: Extracted `_parse_repository_entry` from `parse_repositories` to reduce complexity; behavior-preserving (commit `e3dab63`).
- 2026-05-28T12:32+02:00: Updated after transcript roots defaulted to `logs/mcp` and provider log roots moved under `logs/providers/`.
- 2026-05-24T09:23+02:00: Updated after config coverage switched the normal Codex harness placement from `.agents/mcp` to `.codex/mcp`.
- 2026-05-23T18:05+02:00: Created during direct closeout prep after MCP settings became the only authority route.
