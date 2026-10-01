# mcp/src/agents_remember/serving/harnesses.py

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

## Evidence

### Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation
pass was available for this update.

### Repo-Internal References

The opener consumes only base command/custom compatibility mapping, while the normalized launch
path owns dynamic native selection.

- The launch module validates native model and model-local effort against dynamic advertise. [1]
- The adapter factory constructs builtin protocol adapters and leaves unknown/custom ids unsupported. [2]
- The settings loader builds the effective registry for explicit custom mappings. [3]
- Detection delegates here: the registry resolves the probe-declaring row through its probe rather than `PATH`, and returns the probe's own sentence as the detail. [4]
- The one probe-declaring row and the probe name it carries. [5]
- The probe implementation detection now asks, including the bounded interpreter execution and the floor it owns. [6]
- The settings override path carries the builtin row's probe across an override instead of dropping it. [7]
- The terminal opener is the consumer that must ask the narrower launchability question. [8]
- The cases pin that the eve row consults its probe and never `PATH`, and that the path harnesses keep the ordinary lookup. [9]

### Cross-Repo References

No external repository boundary is implemented by this local registry.
