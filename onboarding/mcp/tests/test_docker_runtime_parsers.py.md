# mcp/tests/test_docker_runtime_parsers.py

| Field                  | Value                                          |
| ---------------------- | ---------------------------------------------- |
| repository             | agents-remember                             |
| path                   | `mcp/tests/test_docker_runtime_parsers.py`     |
| doc_type               | `file-level-onboarding`                        |
| lastUpdated            | 2026-05-31T12:30+02:00                         |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`                             |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `../overview.md`                               |

## Purpose

`test_docker_runtime_parsers.py` is the first direct unit coverage for the pure
output parsers in the Docker lifecycle adapter (F13). These helpers translate
raw `docker inspect` JSON into the small typed values the provider lifecycle and
current-state code depend on (timestamps, uptime, health, mounts, ports,
networks). They had been exercised only indirectly through higher-level provider
tests; this suite pins each parser's edge-case behaviour in isolation so the
inspect-to-state contract is proven once, without Docker, network, or a real
container.

The suite also isolates the `docker inspect` command/result adapter without running Docker. It
proves nonzero command results, malformed JSON, non-list payloads, and empty lists return `None`,
while a non-empty inspect list returns its first container record.

## Code Commentary

### Logic

The module imports the parser functions directly from
`agents_remember.providers.lifecycle.docker_runtime` and drives them with inline
fixture dicts that mirror real `docker inspect` shapes. One `unittest.TestCase`
class covers each parser family.

`DockerInspectContainerTests` mocks command and executable resolution to cover the adapter's
fail-closed command/JSON/shape branches and its first-record success contract.

`ParseDockerTimestampTests` pins `parse_docker_timestamp`: a nanosecond `Z`
timestamp is truncated (not rounded) to six fractional digits and normalized to
UTC; an offset timestamp is converted to UTC; a naive timestamp is assumed UTC; a
short fraction (`.5`) is right-padded to microseconds; and the parser returns
`None` for the Go zero time (`0001-01-01T00:00:00Z`), the empty string, and any
unparseable value.

`DockerContainerUptimeTests` pins `docker_container_uptime_seconds`: elapsed
seconds since the start time (asserted within a tolerance band to absorb wall-clock
drift), a future start clamped to `0`, and `None` start returning `None`.

`DockerContainerHealthTests` pins `docker_container_health`: it extracts
`State.Health.Status`, and returns `None` when the `Health` section is absent,
present but missing `Status`, or not a mapping.

`DockerContainerStateSummaryTests` pins `docker_container_state_summary`: a running
container yields state, `running=True`, an integer `uptimeSeconds`, and the health
string; a stopped container reports its status with `uptimeSeconds`/`health` of
`None`; and a `None` inspect payload returns the exact `"missing"` sentinel dict.

`MountSourceTests` pins `mount_source_for_destination` and
`docker_data_mount_source`: a single mount matches only its requested destination
(non-dict mounts and a missing `Source` yield `None`), and the scanner walks the
`Mounts` list for the destination, returning `None` when absent, when inspect is
`None`, or when `Mounts` is not a list.

`DockerHostPathMatchesTests` pins `docker_host_path_matches`: a resolved POSIX path
matches its own `Path`, a trailing slash is ignored, an empty/`None` actual path
never matches, and divergent paths do not match. The Docker Desktop case proves the
`/run/desktop/mnt/host/<drive>/...` prefix is rewritten back to a `<drive>:/...`
form before comparison.

`PortMappingTests` pins `first_port_mapping` and `docker_container_port`: the first
list entry is returned (empty/non-list inputs yield `None`); the container port
resolver reads `NetworkSettings.Ports["<port>/tcp"]`, returns `(host_ip, host_port)`
as a `(str, int)` tuple, defaults a blank `HostIp` to `127.0.0.1`, and returns
`None` when the mapping or the `HostPort` is missing.

`DockerContainerNetworksTests` pins `docker_container_networks`: network names under
`NetworkSettings.Networks` are collected into a `set`, with an empty set for a `None`
inspect payload or a non-dict `Networks` value.

A module-level `_StubResolvePath` helper supplies a `Path`-like object whose
`resolve()` returns a fixed string, so the Windows drive-letter rewrite branch can
be exercised on POSIX (where a real `PureWindowsPath` cannot be resolved); it is
passed to the function via `typing.cast(Path, ...)`.

### Conventions

Standard-library `unittest`, one `TestCase` per parser family, run via
`unittest.main()` under `__main__`. The module prepends the MCP `src/` directory to
`sys.path` (relative to the test file) so the package imports resolve when the
suite is run standalone. Fixtures are built inline as Python dicts that mirror
real inspect output rather than loaded from sample files. Test names describe the
contract pinned, not the function name. Wall-clock-dependent assertions use a
tolerance band rather than exact equality.

### Invariants And Boundaries

- `parse_docker_timestamp` truncates sub-microsecond precision, normalizes to UTC,
  and must return `None` for the Go zero time, empty input, and unparseable values.
- `docker_container_uptime_seconds` is non-negative (future starts clamp to `0`) and
  `None`-propagating; the state summary only reports uptime while the container is
  running.
- `docker_container_state_summary(None)` must return the exact `"missing"` sentinel
  dict; the test asserts the whole dict, so its keys and defaults are load-bearing.
- `docker_container_port` returns a `(str host_ip, int host_port)` tuple and defaults
  a blank host IP to `127.0.0.1`.
- These tests do not invoke Docker or run a container. They cover the pure parsers plus the mocked
  `docker_inspect_container` adapter; wait, ping, digest, and image helpers remain outside this
  module's scope.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| All ten directly imported parser functions under test live in the Docker lifecycle adapter. | `docker_container_state_summary`; `docker_container_uptime_seconds`; `docker_container_health`; `parse_docker_timestamp`; `docker_container_port`; `first_port_mapping`; `docker_data_mount_source`; `mount_source_for_destination`; `docker_host_path_matches`; `docker_container_networks` | mcp/src/agents_remember/providers/lifecycle/docker_runtime.py:47-67; mcp/src/agents_remember/providers/lifecycle/docker_runtime.py:70-73; mcp/src/agents_remember/providers/lifecycle/docker_runtime.py:76-81; mcp/src/agents_remember/providers/lifecycle/docker_runtime.py:84-107; mcp/src/agents_remember/providers/lifecycle/docker_runtime.py:127-139; mcp/src/agents_remember/providers/lifecycle/docker_runtime.py:142-143; mcp/src/agents_remember/providers/lifecycle/docker_runtime.py:146-158; mcp/src/agents_remember/providers/lifecycle/docker_runtime.py:161-165; mcp/src/agents_remember/providers/lifecycle/docker_runtime.py:168-179; mcp/src/agents_remember/providers/lifecycle/docker_runtime.py:187-193 |
| The GrepAI watcher status exposes the Docker summary in its `containerState` field. | `containerState` | mcp/src/agents_remember/providers/grepai/lifecycle/runner.py:97-97 |
| The CGC backend status exposes the Docker summary in its `containerState` field. | `containerState` | mcp/src/agents_remember/providers/cgc/lifecycle/backend.py:212-212 |
| The provider-current-state regression directly exercises the Docker summary. | `test_docker_container_state_summary_reports_uptime` | mcp/tests/test_provider_current_state.py:27-42 |
| The focused inspect adapter tests cover command failure, malformed and wrong-shaped JSON, an empty list, and first-record success. | `DockerInspectContainerTests` | mcp/tests/test_docker_runtime_parsers.py:28-62 |

## Update History

- 2026-08-13T13:08+02:00 — L23 full-Dagger coverage repair: expanded the card from pure parsers to
  the mocked `docker_inspect_container` result adapter and its fail-closed branches; verification
  remains closeout-owned.

- 2026-08-04T02:35:12+02:00 — S18-B05 curator delta: resolved provisional source-local citation bindings with fixer-generated current-source ranges; no approved semantic claim changes.
- 2026-08-04T01:28:33+02:00 — S18-SR2-B05 worker: replaced the untested `docker_container_running` entry with the directly tested networks parser while preserving the nine valid generated ranges; rebound the provider-current-state claim to real consumers and exact-name focused coverage provisionally.
- 2026-08-04T00:22:04+02:00 — 260731-EFA-L6 S18-B05 curator: repaired and normalised mechanical citation findings with current source anchors and fixer-generated ranges; no semantic claim changes. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-31T16:35+02:00 — No content impact: the only change to
  `mcp/tests/test_docker_runtime_parsers.py` since the L2 base commit is the whole-tree `ruff
  format` pass in `00e8379`, which re-wrapped 3 line(s) with no token change whatsoever. Checked
  by parsing both revisions and comparing the abstract syntax trees (identical) and the comment
  tokens (identical), so no symbol, signature, default, decorator, control-flow branch, docstring,
  or assertion this card describes has moved, and every claim this card makes about its own source
  still holds.

- 2026-05-31T12:30+02:00 — Created during the 1.0.0 review remediation.
