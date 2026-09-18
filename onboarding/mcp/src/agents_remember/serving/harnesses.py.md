# mcp/src/agents_remember/serving/harnesses.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/harnesses.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T13:26+02:00 |
| lastVerifiedCommitHash | `ea9cf0abeab4fe88961bda10b4f54d30266a9634` |
| lastVerifiedCommitDate | 2026-09-17T23:56:19+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Defines the settings-extensible harness id/base-command registry and local executable detection used
by dashboard and role-based spawn. Native Claude, Codex, and Pi model/effort catalogs and launch
channels do not live here; their own adapters derive those dynamically.

**Detection is two different questions, and this module now answers both.** A PATH harness is
detected when its command resolves on `PATH`. A harness whose runtime is an *application* the session
adapter starts itself — eve is the one such row — declares a readiness probe on its registry row
instead, and detection asks that probe. The distinction matters because `which("eve")` can only ever
answer "no": answering detection with it would report a present runtime as a generic not-installed
harness. Terminal launchability is a third, narrower question (`terminal_launch_detail`), because the
terminal path execs `argv[0]` and eve's runtime has no command line to exec.

## Code Commentary

### Logic

`Harness` carries the stable id, display name, executable to detect, fixed base argv, origin, an
optional `runtime_probe` naming a registered readiness probe, and an optional legacy mapping surface
for explicitly settings-defined non-native harnesses. `HARNESSES` carries four base rows — `claude`,
`codex`, `pi` and, last, `eve`; none carries a static native model/effort mapping. The `eve` row is
the only one with a `runtime_probe` (`EVE_RUNTIME_PROBE`), and it is last so the first-detected default
stays `claude` → `codex` → `pi` → `eve` and no existing row moved.

`find_harness`, `unknown_harness_detail`, `detect_harnesses` and the launchable-selection helpers
resolve the built-in or injected effective registry and keep detection injectable.

**Detection delegates to the kernel.** `is_detected(harness)` is now
`harness_availability_detail(harness, which=…, env=…) is None`, so this module holds no second
detection rule: a PATH harness resolves through `which`, a probe-declaring harness goes to its probe,
and `env` is forwarded to the probe while the PATH lookup ignores it. `harness_detection_detail()`
exposes the operator-readable reason — the probe's own sentence, naming the missing component, or the
ordinary not-on-PATH sentence.

**`terminal_launch_detail()` separates detection from spawnability.** It returns `None` when
`which(harness.argv[0])` resolves, so a settings override that gives the row a real program on this
machine's `PATH` is launchable again — the check is the program, not the harness id. When nothing
resolves and the row declares a probe, it returns the truthful not-a-terminal-program refusal naming
the argv that does not exist and pointing at `orchestration.roles` / `orchestration.spawn` as the
route; otherwise it returns the ordinary not-installed refusal. Answering this with detection alone is
what let a ready eve row resolve to an argv whose program exists nowhere — a false affordance rather
than a launch.

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
- This module performs no subprocess launch beyond executable presence lookup. A readiness probe may
  execute one bounded `<node> --version` — that execution lives in the probe, in `kernel`, not here.
- **Never call `shutil.which(harness.command)` directly on a probe-declaring harness.** `is_detected`,
  `harness_availability_detail` and `harness_runtime_verdict` are the only entry points that may answer
  detection; a new `which(...)` call anywhere reintroduces the original defect.
- **Detected is not spawnable.** A detected probe-declaring row is selectable as a session backend and
  is still not a PTY program, so anything that opens a terminal must consult `terminal_launch_detail`
  rather than `is_detected`.
- Only the harness id crosses serving request boundaries, and the browser never sends a command.

### Todos

No known follow-up in this file.

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
| The launch module validates native model and model-local effort against dynamic advertise. | `validate_launch_selection`; `apply_launch_knobs` | mcp/src/agents_remember/serving/harness_launch.py:80-121; mcp/src/agents_remember/serving/harness_launch.py:175-208 |
| The adapter factory constructs builtin protocol adapters and leaves unknown/custom ids unsupported. | `BUILTIN_PROTOCOL_HARNESSES`; `create_harness_protocol_adapter` | mcp/src/agents_remember/serving/harness_control_factories.py:33-33; mcp/src/agents_remember/serving/harness_control_factories.py:56-102; mcp/src/agents_remember/serving/harness_control_factories.py:35-35; mcp/src/agents_remember/serving/harness_control_factories.py:120-167 |
| The settings loader builds the effective registry for explicit custom mappings. | "def _parse_harnesses("; "def _parse_harness_entry(" | mcp/src/agents_remember/kernel/_agentic_settings_harness.py:26-26; mcp/src/agents_remember/kernel/_agentic_settings_harness.py:92-92 |
| Detection delegates here: the registry resolves the probe-declaring row through its probe rather than `PATH`, and returns the probe's own sentence as the detail. | `harness_availability_detail`; `harness_runtime_verdict`; `is_harness_available`; `register_runtime_probe` | mcp/src/agents_remember/kernel/harnesses.py:50-57; mcp/src/agents_remember/kernel/harnesses.py:71-79; mcp/src/agents_remember/kernel/harnesses.py:82-103; mcp/src/agents_remember/kernel/harnesses.py:106-139 |
| The one probe-declaring row and the probe name it carries. | `EVE_RUNTIME_PROBE`; `HARNESSES` | mcp/src/agents_remember/kernel/harnesses.py:144-144; mcp/src/agents_remember/kernel/harnesses.py:187-212 |
| The probe implementation detection now asks, including the bounded interpreter execution and the floor it owns. | `eve_runtime_readiness`; `MINIMUM_NODE_MAJOR` | mcp/src/agents_remember/kernel/eve_runtime_readiness.py:55-55; mcp/src/agents_remember/kernel/eve_runtime_readiness.py:89-128 |
| The settings override path carries the builtin row's probe across an override instead of dropping it. | `_merged_harness` | mcp/src/agents_remember/kernel/_agentic_settings_harness.py:133-182 |
| The terminal opener is the consumer that must ask the narrower launchability question. | `_require_launchable_harness`; `resolve_terminal_launch` | mcp/src/agents_remember/serving/terminal_opener.py:252-296; mcp/src/agents_remember/serving/terminal_opener.py:299-319 |
| The cases pin that the eve row consults its probe and never `PATH`, and that the path harnesses keep the ordinary lookup. | `EveRegistryTests`; `EveTerminalLaunchTests` | mcp/tests/test_eve_product_integration.py:575-629; mcp/tests/test_eve_product_integration.py:632-707; mcp/tests/test_eve_product_integration.py:751-859 |

## Cross-Repo References

No external repository boundary is implemented by this local registry.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History
- 2026-09-16T13:26+02:00 — 260915-CAPS-L8 curator: **detection is no longer one question.** `is_detected`
  now delegates to the kernel's `harness_availability_detail`, so a harness whose runtime is an
  application the session adapter starts itself is detected by its registry row's readiness probe
  rather than by a `which` lookup that can only ever answer "no" for it; `harness_detection_detail`
  exposes the probe's own sentence as the operator-readable reason, and `detect_harnesses` forwards an
  injectable `env`. New `terminal_launch_detail` answers the *narrower* question the terminal path
  actually needs — it execs `argv[0]`, so a detected-but-not-a-program row refuses by name and points
  at `orchestration.roles` / `orchestration.spawn`, while a settings override supplying a real program
  on `PATH` becomes launchable again. Body updated on Purpose, Logic, Invariants (two new must-not
  rules) and the reference table; Todos cleared of the stale L4 note. Verification metadata moves to
  the leaf's synced base `ff97072c`; the candidate is deliberately uncommitted, so the governed
  closeout stamps the real code commit and no hash or fingerprint was invented here.
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
