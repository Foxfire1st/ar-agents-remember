# mcp/src/agents_remember/serving/harness_control_runner.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/harness_control_runner.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-16T06:15+02:00 |
| lastVerifiedCommitHash | `a1b0aa9143fa777efd8389892e3283ff257ef44d` |
| lastVerifiedCommitDate | 2026-07-16T06:37:02+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Process entrypoint for one hosted native harness session. It carries the typed settings-resolved
launch across the tmux process boundary, performs token-free discovery and fail-loud validation,
starts the configured adapter, and keeps exact startup failure evidence available over local IPC.

## Code Commentary

### Logic

`RunnerConfig` serializes exact control identity, harness, cwd, base argv, endpoint root, explicit
session commands, and optional `ResolvedLaunch`. Decode verifies that the typed launch names the
same harness and workspace. `_prepare_controlled_launch` builds the unconfigured native
`LaunchSpec`, asks a transient adapter for its native knobs, applies conflict preflight before any
discovery process, enumerates the dynamic catalog without a prompt, validates model and model-local
launch effort, then builds a fresh runtime adapter carrying expected-launch evidence. Selectionless
sessions still allow the native catalog default; L4 roleless daemon opens can now carry the same
complete typed selection as role-based spawn.

`run_controlled_session` starts IPC before adapter startup. Any discovery, validation, conflict, or
vendor-start exception becomes the bridge's persistent failed snapshot. Session commands are sent
only after ready. A failed runner stays addressable and reads terminal input instead of exiting, so
readiness/daemon consumers can retrieve `control=failed`, `acceptance=rejected`, and the exact
`raw.bridgeError`. Codex argv conversion is exposed as `adapter_argv(harness_id, argv)` so hosted
launch and L4 pre-session discovery share the exact native process boundary. It adds `app-server`
while retaining every supplied argument so duplicate authority is refused, never silently deleted.

### Conventions

The typed payload is URL-safe base64 JSON because tmux launches this module as a fixed argv command.
Native selection ordering is preflight → discover → validate → runtime construction/start. The broad
exception catches at the subprocess/IPC boundary preserve exact external failures; they do not
retry, default, or continue the vendor launch.

### Invariants And Boundaries

- No configured real vendor session starts before token-free catalog validation succeeds.
- Adapter-owned selector conflicts fail before even transient discovery starts.
- Session commands and terminal input cannot run until the bridge is ready.
- Launch failure remains observable over the exact private endpoint; it is not collapsed into a
  generic process disconnect.
- Model/effort is never delivered through composer paste or synthesized session commands.
- The terminal catalog/tmux row may precede asynchronous discovery by design; the vendor session
  does not.

### Todos

None known for the L4 runner boundary.

## Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation
pass was available for this update.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Launch validation and adapter construction remain separate pure/data and vendor-specific seams.

| Finding | Citations | Source Path |
| --- | --- | --- |
| `ResolvedLaunch`, model-gated validation, effective echo checks, and duplicate-selector preflight are centralized in the launch module. | L17-L226 | [harness_launch.py](agents-remember/mcp/src/agents_remember/serving/harness_launch.py) |
| The factory pairs a typed selection with adapter-produced knobs and ignores ambient role env as authority. | L22-L57 | [harness_control_factories.py](agents-remember/mcp/src/agents_remember/serving/harness_control_factories.py) |
| The opener embeds the typed launch in this runner command and persists model/effort provenance on the terminal row. | L170-L216; L311-L460 | [terminal_opener.py](agents-remember/mcp/src/agents_remember/serving/terminal_opener.py) |
| The bridge translates `mark_failed` into failed/rejected state with exact raw error evidence. | L109-L121; L219-L226 | [harness_control_bridge.py](agents-remember/mcp/src/agents_remember/serving/harness_control_bridge.py) |
| The pre-session catalog reuses `adapter_argv` before calling the transient adapter's token-free discovery path. | L180-L195 | [harness_capability_catalog.py](agents-remember/mcp/src/agents_remember/serving/harness_capability_catalog.py) |

## Cross-Repo References

No external repository boundary is implemented by the runner; it launches installed native
harnesses owned by the local adapter process.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-16T06:15+02:00 — 260714-ACPUI-L4 curator: documented the shared native argv helper
  used by hosted launch and token-free pre-session discovery, plus roleless complete-pair launch
  flowing through the existing runner boundary.
- 2026-07-15T23:00+02:00 — 260714-ACPUI-L2 curator: documented typed launch serialization,
  pre-discovery selector conflict refusal, token-free dynamic validation, fresh configured runtime
  construction, ready-only session commands, and persistent exact launch-failure IPC evidence.
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: documented bridge-owned hosted launch, exact identity,
  correlated commands, transcript rendering, and shutdown.
