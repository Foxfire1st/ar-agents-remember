# mcp/src/agents_remember/serving/harness_control_factories.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/harness_control_factories.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-15T23:16+02:00 |
| lastVerifiedCommitHash | `5fa7026c644edfb4eb884173b64d31c9a14a6585` |
| lastVerifiedCommitDate | 2026-07-15T23:33:30+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Constructs the three built-in launchable protocol adapters from one optional settings-resolved
selection and that adapter's own launch knobs. Unknown or settings-only ids remain explicitly
unsupported.

## Code Commentary

### Logic

`create_harness_protocol_adapter` verifies that a `ResolvedLaunch` names the requested harness and
cannot be supplied without adapter-produced `LaunchKnobs`. Claude and Pi receive the expected
selection so startup can verify effective native state. Codex receives the selected model/effort
and native thread config. When no typed selection exists, the pre-L4 roleless Codex path passes no
model or effort so its session derives the authenticated catalog default and that model's default
effort. Runtime environment remains on `LaunchSpec`; ambient `AR_SPAWN_MODEL` and
`AR_SPAWN_EFFORT` are ignored here as selection authority.

### Conventions

Built-in ids are exactly `claude`, `codex`, and `pi`. Factory inputs are already normalized by the
runner; vendor-specific argv/config production remains on the adapter's `launch_knobs` method.

### Invariants And Boundaries

- A typed launch and its adapter-produced knobs travel together and must name the same harness.
- Role-spawn environment is provenance, not a fallback authority for roleless sessions.
- Custom/unknown harnesses receive the truthful unsupported adapter; no pane, regex, paste, or
  static native-catalog compatibility path is invented.
- Native Codex initial configuration is app-server thread config, never `CODEX_CONFIG`.

### Todos

L4 replaces the temporary roleless/default boundary with explicit daemon request/default authority.

## Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation
pass was available for this update.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

The hosted runner owns ordering, while each built-in adapter owns its native launch material and
startup evidence.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The runner constructs a discovery adapter, obtains knobs, validates dynamic advertise, then constructs the configured runtime adapter. | L152-L191 | [harness_control_runner.py](agents-remember/mcp/src/agents_remember/serving/harness_control_runner.py) |
| Claude consumes expected launch evidence and produces native model/effort flags. | L47-L63; L77-L140; L188-L202 | [harness_control_claude.py](agents-remember/mcp/src/agents_remember/serving/harness_control_claude.py) |
| Codex session settings resolve typed or catalog-default model/effort into thread config. | L37-L83; L106-L176; L295-L337 | [codex_app_server_session.py](agents-remember/mcp/src/agents_remember/serving/codex_app_server_session.py) |
| Pi consumes expected launch evidence and produces native provider-qualified model/thinking flags. | L63-L153; L181-L191 | [pi_rpc_adapter.py](agents-remember/mcp/src/agents_remember/serving/pi_rpc_adapter.py) |

## Cross-Repo References

No external repository boundary is implemented by this factory.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-07-15T23:16+02:00 — 260714-ACPUI-L2 curator: documented paired typed selection/launch
  knobs, expected-launch evidence injection, the roleless Codex dynamic-default boundary, and the
  rule that ambient role env is provenance rather than selection authority. Final audit restored
  every earlier history entry byte-for-byte below this prepend.
- 2026-07-14T16:30:00+02:00 — 260713-PHA-L6 curator: documented version-free factory construction and the
  unchanged explicit custom-harness boundary.
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: recorded built-in adapter selection and explicit unsupported custom behavior.
