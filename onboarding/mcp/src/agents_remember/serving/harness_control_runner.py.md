# mcp/src/agents_remember/serving/harness_control_runner.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/harness_control_runner.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-19T09:15+02:00 |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d` |
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Process entrypoint for one hosted native harness session. It carries the typed settings-resolved
launch across the tmux process boundary, performs token-free discovery and fail-loud validation,
starts the configured adapter, and keeps exact startup failure evidence available over local IPC.
260718-CHATS-L0E adds the additive codex `resume_thread_id` channel through the same runner
payload.

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

L0E adds `RunnerConfig.resume_thread_id`, serialized as the additive `"resumeThreadId"` payload
key. Parse validation requires non-empty trimmed text or null; a legacy payload without the key
parses unchanged to `None`. The value rides into both real adapter-construction sites (the
selectionless path and the configured path) as the factory's codex-only kwarg — never into the
transient discoverer — and the factory refuses a non-codex harness or a malformed value before any
spawn. The runner does not validate or authorize the resume target; it is a native-identity
selector in the same authority class as verbatim `launch_args`.

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
- `resumeThreadId` is additive: absent preserves legacy parse/dispatch behavior exactly, malformed
  shapes fail before construction, and the transient discovery adapter never receives it.

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
| Contract tests pin the resumeThreadId payload round-trip, legacy field-less parse, malformed refusal, and codex-only factory channel. | L1309-L1460 | [test_harness_control_evidence.py](agents-remember/mcp/tests/test_harness_control_evidence.py) |
| The bridge translates `mark_failed` into failed/rejected state with exact raw error evidence (`raw["bridgeError"]`), refusing to overwrite an already-started bridge. | L170-L184 | [harness_control_bridge.py](agents-remember/mcp/src/agents_remember/serving/harness_control_bridge.py) |
| The pre-session catalog reuses `adapter_argv` before calling the transient adapter's token-free discovery path. | L180-L195 | [harness_capability_catalog.py](agents-remember/mcp/src/agents_remember/serving/harness_capability_catalog.py) |

## Cross-Repo References

No external repository boundary is implemented by the runner; it launches installed native
harnesses owned by the local adapter process.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## 260731-EFA-L2 Current Delta

The runner payload decoder was split into named checks, each stating the contract it enforces:

- `_decode_runner_payload(encoded)` — decode the base64url argv token the opener hands the runner
  into its JSON object.
- `_is_text_list(value)` — a `TypeGuard` for the only argv shape accepted: a list whose every entry
  is non-empty text.
- `_optional_resume_thread_id(raw)` — `resumeThreadId` is additive, so an absent or null field stays
  a legal payload.
- `_require_launch_agrees_with_config(config)` — refuse a payload whose settings-owned selection
  contradicts the session it launches.

The refusals and the launch sequence are unchanged.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## Update History

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 1 cross-file line citation. `HarnessControlBridge.mark_failed` is a single contiguous method at L170-L184 in the 623-line `harness_control_bridge.py`, so the two-range citation collapsed to one; extended the claim to name `raw["bridgeError"]` and the already-started refusal, both read back at L174 and L181.
- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator: recorded the named payload-decode and launch-agreement checks; refusals unchanged.
- 2026-07-19T09:15+02:00 — 260718-CHATS-L0E curator: documented the additive `resumeThreadId`
  payload field — trimmed-non-empty parse validation, legacy field-less compatibility, and delivery
  into both real adapter-construction sites as the codex-only factory kwarg while the transient
  discoverer never receives it. Verification metadata stays pinned until closeout stamps the
  candidate commit.
- 2026-07-16T06:15+02:00 — 260714-ACPUI-L4 curator: documented the shared native argv helper
  used by hosted launch and token-free pre-session discovery, plus roleless complete-pair launch
  flowing through the existing runner boundary.
- 2026-07-15T23:00+02:00 — 260714-ACPUI-L2 curator: documented typed launch serialization,
  pre-discovery selector conflict refusal, token-free dynamic validation, fresh configured runtime
  construction, ready-only session commands, and persistent exact launch-failure IPC evidence.
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: documented bridge-owned hosted launch, exact identity,
  correlated commands, transcript rendering, and shutdown.
