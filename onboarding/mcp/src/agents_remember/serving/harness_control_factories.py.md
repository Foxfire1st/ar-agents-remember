# mcp/src/agents_remember/serving/harness_control_factories.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/harness_control_factories.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T10:15+02:00 |
| lastVerifiedCommitHash | `609756111eb3c239d0563d8631bfd564645bc9d1` |
| lastVerifiedCommitDate | 2026-09-16T10:25:13+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Constructs the four built-in launchable protocol adapters from one optional settings-resolved
selection and that adapter's own launch knobs. Unknown or settings-only ids remain explicitly
unsupported. 260718-CHATS-L0E adds one additive codex-only `resume_thread_id` kwarg feeding the
sole `CodexAppServerSettings` construction site. 260915-CAPS-L6 adds `eve`, whose expected
selection is recovered from the launch knobs the runner already applied rather than re-derived.

## Code Commentary

### Logic

`create_harness_protocol_adapter` verifies that a `ResolvedLaunch` names the requested harness and
cannot be supplied without adapter-produced `LaunchKnobs`. Claude and Pi receive the expected
selection so startup can verify effective native state. Codex receives the selected model/effort
and native thread config. When no typed selection exists, the pre-L4 roleless Codex path passes no
model or effort so its session derives the authenticated catalog default and that model's default
effort. Runtime environment remains on `LaunchSpec`; ambient `AR_SPAWN_MODEL` and
`AR_SPAWN_EFFORT` are ignored here as selection authority.

L0E's `resume_thread_id` kwarg is codex-only: any other harness id, an empty value, or outer
whitespace raises `HarnessControlError` before any adapter is constructed or spawned. A well-formed
value is threaded into the sole `CodexAppServerSettings` construction site, whose
`resume_thread_id` field the adapter already honors at start (`thread/resume`). Omitting the kwarg
preserves the pre-L0E construction behavior exactly.

260915-CAPS-L6 routes `harness_id == "eve"` to `EveSessionAdapter` with
`_eve_expected_selection(resolved_launch, launch_knobs)`. That helper reads the selection back off
the knobs the runner already applied — `launch_spec_selection` parses the adapter-owned environment —
so the adapter verifies the running runtime against the same values that reached the child instead of
re-deriving them from ambient state. The recovery is done by constructing a probe `LaunchSpec` that
carries only the identity, cwd and `dict(launch_knobs.env)`; a resolved launch without adapter-produced
knobs raises rather than guessing a selection.

### Conventions

Built-in ids are exactly `claude`, `codex`, `pi`, and `eve`. Factory inputs are already normalized by
the runner; vendor-specific argv/config production remains on the adapter's `launch_knobs` method.
`_LAUNCH_KNOBS` is the one registry the factory itself consults, so a harness added here is held to
the launch-vocabulary contract without editing the parametrized test that drives it.

### Invariants And Boundaries

- A typed launch and its adapter-produced knobs travel together and must name the same harness.
- Role-spawn environment is provenance, not a fallback authority for roleless sessions.
- Custom/unknown harnesses receive the truthful unsupported adapter; no pane, regex, paste, or
  static native-catalog compatibility path is invented.
- Native Codex initial configuration is app-server thread config, never `CODEX_CONFIG`.
- The resume channel can never target a harness that lacks the semantics: non-codex or malformed
  `resume_thread_id` fails closed at this boundary before any spawn.
- eve's launch vocabulary is environment-only (`argv=()`); the probe LaunchSpec's `argv=("eve",)` is a
  placeholder for the selection lookup and is never spawned.
- Adding `eve` here does **not** add it to the developer-curated terminal harness set in
  `kernel/harnesses.py`; the two registries are separate and the kernel row is a later leaf's decision.

### Todos

L4 replaces the temporary roleless/default boundary with explicit daemon request/default authority.

## Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation
pass was available for this update.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

The hosted runner owns ordering, while each built-in adapter owns its native launch material and
startup evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| The runner constructs a discovery adapter, obtains knobs, validates dynamic advertise, then constructs the configured runtime adapter. | "async def _prepare_controlled_launch("; "discoverer = create_harness_protocol_adapter(config.harness_id"; "knobs = harness_launch_knobs("; "launch = apply_launch_knobs(base"; "discovery_env = {"; "validate_launch_selection(selection" | mcp/src/agents_remember/serving/harness_control_runner.py:192-240 |
| Claude consumes expected launch evidence and produces native model/effort flags. | `claude_launch_knobs`; `ClaudeStreamJsonAdapter`; "def verify_effective_launch"; `launch_knobs` | mcp/src/agents_remember/serving/harness_control_claude.py:130-144; mcp/src/agents_remember/serving/harness_control_claude.py:147-573; mcp/src/agents_remember/serving/harness_control_runner.py:239-239; mcp/src/agents_remember/serving/harness_launch.py:124-124 |
| Codex session settings resolve typed or catalog-default model/effort into thread config. | `CodexAppServerSettings`; `connect`; `_thread_params` | mcp/src/agents_remember/serving/codex_app_server_session.py:57-99; mcp/src/agents_remember/serving/codex_app_server_session.py:124-208; mcp/src/agents_remember/serving/codex_app_server_session.py:403-448 |
| Pi consumes expected launch evidence and produces native provider-qualified model/thinking flags. | `PiRpcAdapter`; `pi_launch_knobs` | mcp/src/agents_remember/serving/pi_rpc_adapter.py:94-768; mcp/src/agents_remember/serving/pi_rpc_protocol.py:118-132 |
| eve consumes a selection recovered from the applied launch knobs and is constructed with no argv-vocabulary flags. | `EveSessionAdapter` | mcp/src/agents_remember/serving/eve_adapter.py:143-863 |
| eve's launch vocabulary is the environment, because its model and effort are compiled application values with no argv spelling. | `eve_launch_knobs` | mcp/src/agents_remember/serving/eve_runtime_launch.py:310-327 |
| The reader that recovers the applied selection from a probe launch spec. | `launch_spec_selection` | mcp/src/agents_remember/serving/eve_runtime_launch.py:328-353 |
| This factory's own recovery helper; it refuses a resolved launch that arrives without adapter-produced knobs. | `_eve_expected_selection` | mcp/src/agents_remember/serving/harness_control_factories.py:105-130 |

## Cross-Repo References

No external repository boundary is implemented by this factory.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-16T10:15+02:00 — 260915-CAPS-L6 curator (A2 delta pass): the body is retained (this file is
  byte-identical between the A1 and A2 candidates), and three citation findings were **repaired**
  rather than restamped. The eve row was split into one row per anchor so each names a unique
  declaring source, which also clears the provenance failure that arose because `EveSessionAdapter`,
  `eve_launch_knobs` and `launch_spec_selection` each resolve in more than one file; the
  `harness_control_factories.py` range was corrected from `:105-131` to `:105-130` (the file has 130
  lines). Verification metadata moves to the leaf's current base `e9300687`; the candidate is
  uncommitted, so the governed closeout re-stamps the real code commit and no hash was invented here.

- 2026-09-16T09:00+02:00 — 260915-CAPS-L6 curator: documented the `eve` built-in — the
  `_eve_expected_selection` recovery of the selection from adapter-produced launch knobs (with the
  probe `LaunchSpec` that carries only identity, cwd and env), the environment-only launch vocabulary
  (`argv=()`), the refusal when a resolved launch arrives without adapter-produced knobs, and the
  explicit boundary that this registry is separate from the kernel's developer-curated terminal
  harness set. Built-in ids are now four. Verification metadata stays pinned to the last committed
  source until closeout stamps the candidate commit.

- 2026-08-04T11:40:58+02:00 — 260731-EFA-L6 S18-B08 curator: split runner, Claude, Codex, and Pi launch ownership across their current implementation modules.

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 1 cross-file line citation. The Claude
  adapter grew a two-pass `--forward-subagent-text` startup, so the cited ranges no longer covered
  the material. `ClaudeStreamJsonAdapter` now takes `expected_launch: ResolvedLaunch | None` at
  L94-L100, feeds its `model_key` into catalog negotiation and runs `verify_effective_launch` (with
  a forced transport stop on mismatch) at L145-L172, records `requestedLaunchModel` /
  `requestedLaunchEffort` / `launchEffortEvidence` on the handshake snapshot at L200-L210, and
  `launch_knobs` mints the native `--model`/`--effort` argv at L271-L285. Verified `_expected_launch`
  has no other use in the file. No claim text changed.

- 2026-07-19T09:15+02:00 — 260718-CHATS-L0E curator: documented the codex-only `resume_thread_id`
  kwarg — fail-closed refusal for non-codex harnesses and malformed values before construction,
  threading into the sole `CodexAppServerSettings` site, and exact absent-kwarg behavior
  preservation. Verification metadata stays pinned until closeout stamps the candidate commit.
- 2026-07-15T23:16+02:00 — 260714-ACPUI-L2 curator: documented paired typed selection/launch
  knobs, expected-launch evidence injection, the roleless Codex dynamic-default boundary, and the
  rule that ambient role env is provenance rather than selection authority. Final audit restored
  every earlier history entry byte-for-byte below this prepend.
- 2026-07-14T16:30:00+02:00 — 260713-PHA-L6 curator: documented version-free factory construction and the
  unchanged explicit custom-harness boundary.
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: recorded built-in adapter selection and explicit unsupported custom behavior.
