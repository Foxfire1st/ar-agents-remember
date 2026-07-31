# mcp/src/agents_remember/serving/harness_control_factories.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/harness_control_factories.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-19T09:15+02:00 |
| lastVerifiedCommitHash | `ca9dd05a295ef5f24c479e2231fdcd174b372e04` |
| lastVerifiedCommitDate | 2026-07-19T10:04:45+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Constructs the three built-in launchable protocol adapters from one optional settings-resolved
selection and that adapter's own launch knobs. Unknown or settings-only ids remain explicitly
unsupported. 260718-CHATS-L0E adds one additive codex-only `resume_thread_id` kwarg feeding the
sole `CodexAppServerSettings` construction site.

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

### Conventions

Built-in ids are exactly `claude`, `codex`, and `pi`. Factory inputs are already normalized by the
runner; vendor-specific argv/config production remains on the adapter's `launch_knobs` method.

### Invariants And Boundaries

- A typed launch and its adapter-produced knobs travel together and must name the same harness.
- Role-spawn environment is provenance, not a fallback authority for roleless sessions.
- Custom/unknown harnesses receive the truthful unsupported adapter; no pane, regex, paste, or
  static native-catalog compatibility path is invented.
- Native Codex initial configuration is app-server thread config, never `CODEX_CONFIG`.
- The resume channel can never target a harness that lacks the semantics: non-codex or malformed
  `resume_thread_id` fails closed at this boundary before any spawn.

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
| Claude consumes expected launch evidence and produces native model/effort flags. | L94-L100; L145-L172; L200-L210; L271-L285 | [harness_control_claude.py](agents-remember/mcp/src/agents_remember/serving/harness_control_claude.py) |
| Codex session settings resolve typed or catalog-default model/effort into thread config. | L37-L83; L106-L176; L295-L337 | [codex_app_server_session.py](agents-remember/mcp/src/agents_remember/serving/codex_app_server_session.py) |
| Pi consumes expected launch evidence and produces native provider-qualified model/thinking flags. | L63-L153; L181-L191 | [pi_rpc_adapter.py](agents-remember/mcp/src/agents_remember/serving/pi_rpc_adapter.py) |

## Cross-Repo References

No external repository boundary is implemented by this factory.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

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
