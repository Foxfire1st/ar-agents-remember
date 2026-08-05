# mcp/src/agents_remember/serving/harnesses.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/harnesses.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-15T23:16+02:00 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Defines the settings-extensible harness id/base-command registry and local executable detection used
by dashboard and role-based spawn. Native Claude, Codex, and Pi model/effort catalogs and launch
channels do not live here; their own adapters derive those dynamically.

## Code Commentary

### Logic

`Harness` carries the stable id, display name, executable to detect, fixed base argv, origin, and an
optional legacy mapping surface for explicitly settings-defined non-native harnesses. `HARNESSES`
contains only base rows for `claude`, `codex`, and `pi`; none carries a static native model/effort
mapping. `find_harness`, `unknown_harness_detail`, `is_detected`, and `detect_harnesses` resolve the
built-in or injected effective registry and keep executable detection injectable.

`invalid_model_detail`, `invalid_effort_detail`, `knob_argv`, and
`effort_session_commands` remain the compatibility port for settings-defined non-native harnesses
that explicitly declare flags, enumerated/non-empty policy, or a session command. They never supply
a fallback vocabulary or paste path for the three native adapters. Native selections are validated
against the dynamic capability catalog in `harness_launch.py` and applied through each adapter's
`launch_knobs` method.

### Conventions

Only the harness id crosses serving request boundaries. Base argv comes from this registry or the
validated `orchestration.harnesses` settings family. Values are discrete argv elements, never shell
interpolation. `which` is resolved at call time or injected for deterministic tests.

### Invariants And Boundaries

- Built-in native model/effort catalogs are never hardcoded here; L1 advertise is authoritative.
- Native model/effort is never synthesized into `effort_session_commands` or composer paste.
- Settings-defined non-native mappings remain explicit and fail loudly when incomplete or
  out-of-vocabulary; AR does not guess vendor flags.
- The curated registry is extensible through settings but is not a wire-command injection surface.
- This module performs no subprocess launch beyond executable presence lookup.

### Todos

No known follow-up in this file; L4 consumes the same id/detection surface while adding serving
selection fields.

## Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation
pass was available for this update.

| Finding | Anchor | Source |
| --- | --- | --- |


## Repo-Internal References

The opener consumes only base command/custom compatibility mapping, while the normalized launch
path owns dynamic native selection.

| Finding | Anchor | Source |
| --- | --- | --- |
| The launch module validates native model and model-local effort against dynamic advertise. | `validate_launch_selection`; `apply_launch_knobs` | mcp/src/agents_remember/serving/harness_launch.py:78-119; mcp/src/agents_remember/serving/harness_launch.py:173-206 |
| The adapter factory constructs builtin protocol adapters and leaves unknown/custom ids unsupported. | `BUILTIN_PROTOCOL_HARNESSES`; `create_harness_protocol_adapter` | mcp/src/agents_remember/serving/harness_control_factories.py:26-26; mcp/src/agents_remember/serving/harness_control_factories.py:48-90 |
| The settings loader builds the effective registry for explicit custom mappings. | `_parse_harnesses`; `_parse_harness_entry` | mcp/src/agents_remember/kernel/agentic_settings.py:683-715; mcp/src/agents_remember/kernel/agentic_settings.py:746-763 |

## Cross-Repo References

No external repository boundary is implemented by this local registry.

| Finding | Anchor | Source |
| --- | --- | --- |


## Update History
- 2026-08-04T11:32:09+02:00 — 260731-EFA-L6 S18-B02 curator: replaced unanchored launch references with exact local anchors and generated final ranges with the scoped fixer.
- 2026-07-31T16:35+02:00 — No content impact: the only change to
  `mcp/src/agents_remember/serving/harnesses.py` since the L2 base commit is the whole-tree `ruff
  format` pass in `00e8379`, which re-wrapped 1 line(s) with no token change whatsoever. Checked
  by parsing both revisions and comparing the abstract syntax trees (identical) and the comment
  tokens (identical), so no symbol, signature, default, decorator, control-flow branch, docstring,
  or assertion this card describes has moved, and every claim this card makes about its own source
  still holds. Noted while checking: the references table also cites line ranges inside
  `terminal_opener.py`; those ranges shifted because this task edited those files, so treat the
  cited numbers as approximate and the linked cards as authoritative.
- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator ATTESTATION: this file was touched by the whole-tree `ruff format` commit (`00e8379`) and by nothing else — `git diff 00e8379 -- <this file>` is empty, so no identifier, signature, branch or behaviour in it changed in this leaf and no claim in this sidecar can have been invalidated by it. Attested, deliberately not rewritten.
- 2026-07-15T23:16+02:00 — 260714-ACPUI-L2 curator: removed the obsolete static native
  model/effort and normalized-paste description; documented base-command/detection ownership,
  adapter-owned dynamic native launch, and the retained explicit non-native settings extension.
  Final audit restored every earlier history entry byte-for-byte below this prepend.
- 2026-07-14T16:30:00+02:00 — 260713-PHA-L6 curator: removed the stale Codex package-version claim from the
  registry commentary.
- 2026-07-14T12:00+02:00 — 260713-PHA-L1 curator refresh: corrected the Codex effort policy to
  stripped-non-empty model-advertised values and documented enumerated settings overrides.

- 2026-07-10T13:03+02:00 — 260707-HFX2-L15: added Codex's explicit model/effort argv mapping,
  value-template support, and first-turn-safe effort enum; Pi.dev remains env-only. Verification
  metadata remains pinned until closeout stamps the eventual L15 code commit.

- 2026-07-07T09:45+02:00 — 260703-L16 (spawn knob application): grew the per-harness knob→flag
  mapping (`model_flag`/`effort_flag`+values/`effort_session_values`+command/`defined_in` on
  `Harness`; claude mapped `--model`/`--effort` with the two-vehicle effort vocabulary incl. the
  session-only `ultracode` → `/effort` paste; codex/pi documented env-only) and the enforcement
  helpers (`effort_vocabulary`, `invalid_effort_detail`, `invalid_model_detail`, `knob_argv`,
  `effort_session_commands`, `unknown_harness_detail`); `find_harness`/`detect_harnesses` accept an
  injected EFFECTIVE registry so `orchestration.harnesses` settings entries (new ids or builtin
  overrides) resolve everywhere. Verification metadata pinned until closeout stamps the L16 commit.
- 2026-06-18T21:27+02:00 — Created for task 6 slice 6e-2b: the harness launch registry (`Harness` +
  `HARNESSES` Claude Code/Codex/Pi.dev + `find_harness`/`is_detected`/`detect_harnesses` with an
  injectable call-time `which`) — the data behind `GET /api/harnesses` detection + the
  `kind="harness"` opener resolution. Verification metadata pinned to the task base until closeout
  stamps the 6e-2b code commit.
