# mcp/tests/test_docker_runtime_parsers.py

| Field                  | Value                                          |
| ---------------------- | ---------------------------------------------- |
| repository             | agents-remember-md                             |
| path                   | `mcp/tests/test_docker_runtime_parsers.py`     |
| doc_type               | `file-level-onboarding`                        |
| lastUpdated            | 2026-05-31T12:30+02:00                         |
| lastVerifiedCommitHash | `c20a3292e667d227a3be0c1fb276f8a701df814f`                             |
| lastVerifiedCommitDate | 2026-05-31T14:17:11+02:00|
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

## Code Commentary

### Logic

The module imports the parser functions directly from
`agents_remember.providers.lifecycle.docker_runtime` and drives them with inline
fixture dicts that mirror real `docker inspect` shapes. One `unittest.TestCase`
class covers each parser family.

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
- These tests exercise the pure parsers only; they do not invoke `docker`, run a
  container, or cover the command-running helpers (`docker_inspect_container`,
  `docker_wait_for_ping`, ping/digest/image helpers) in the same module.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| All ten parser functions under test live in the Docker lifecycle adapter. | [docker_runtime.py](agents-remember-md/mcp/src/agents_remember/providers/lifecycle/docker_runtime.py) |
| `docker_container_state_summary` is the projection these parsers feed into provider current state, which has its own integration coverage. | [test_provider_current_state.py](agents-remember-md/mcp/tests/test_provider_current_state.py) |

## Update History

- 2026-05-31T12:30+02:00 — Created during the 1.0.0 review remediation.
