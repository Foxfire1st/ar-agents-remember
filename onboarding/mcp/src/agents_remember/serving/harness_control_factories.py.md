# mcp/src/agents_remember/serving/harness_control_factories.py

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Constructs the four built-in launchable protocol adapters from one optional settings-resolved
selection and that adapter's own launch knobs. Unknown or settings-only ids remain explicitly
unsupported. 260718-CHATS-L0E adds one additive codex-only `resume_thread_id` kwarg feeding the
sole `CodexAppServerSettings` construction site. 260915-CAPS-L6 adds `eve`, whose expected
selection is recovered from the launch knobs the runner already applied rather than re-derived.
260915-CAPS-L5 adds the second optional kwarg, `capsule_delivery` — the admitted role capsule this
launch must apply — and groups the selection with its knobs as one `LaunchSelection` value so the
factory stays inside the repository's argument limit without an exemption.

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

**260915-CAPS-L5 changes the factory's shape in two ways, and only one of them is behavioural.**

The **behavioural** addition is `capsule_delivery: CodexCapsuleDelivery | None = None`. It is
threaded into the same sole `CodexAppServerSettings` construction site, and `_require_capsule_channel`
refuses a capsule for any harness other than `codex` — the only harness with a verified instruction
channel — so `claude`, `pi` and `eve` refuse rather than silently dropping it. A caller that asked for
a capsule and received a capsule-free process would be the worst outcome this boundary can produce, so
refusal is the point.

The **structural** addition is `LaunchSelection`, a frozen pair of `resolved_launch` + `launch_knobs`
that replaces the two separate parameters. It exists because the fill took the factory to six
parameters and `PLR0913` fired; this repository forbids clearing that finding with a `noqa`, per-file
ignore, baseline or allowlist (`pyproject.toml`), so the only sanctioned options were a refactor or an
unavoidable lint finding. The refactor was already implied by the code: the factory refuses a
`resolved_launch` without `launch_knobs`, i.e. they are always supplied together, and a frozen pair
makes that invariant structural. The three pre-existing checks were extracted as
`_require_consistent_launch`, `_require_launch_knobs_present` and `_require_thread_boundary` with their
messages unchanged. Parameter count returns to five; **no behaviour changed**.

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
- **A capsule only reaches a harness with a verified instruction channel.** `capsule_delivery` on
  anything but `codex` raises `HarnessControlError` naming the harness; there is no silent-drop path.
- **`capsule_delivery=None` is the unmodified legacy launch.** The produced settings keep
  `capsule_delivery is None` and the same `config` object as before, which is what keeps the
  capsule-free payload byte-identical downstream.
- **This is the only producer of `CodexAppServerSettings`,** so it is the only place the carrier can be
  filled; a second construction site would be a second authority and is not sanctioned.

### Todos

L4 replaces the temporary roleless/default boundary with explicit daemon request/default authority.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation
pass was available for this update.

No configured domain documentation could be checked.

### Repo-Internal References

The hosted runner owns ordering, while each built-in adapter owns its native launch material and
startup evidence.

- The runner constructs a discovery adapter, obtains knobs, validates dynamic advertise, then constructs the configured runtime adapter. [1]
- Claude consumes expected launch evidence and produces native model/effort flags. [2]
- Codex session settings resolve typed or catalog-default model/effort into thread config. [3]
- Pi consumes expected launch evidence and produces native provider-qualified model/thinking flags. [4]
- eve consumes a selection recovered from the applied launch knobs and is constructed with no argv-vocabulary flags. [5]
- eve's launch vocabulary is the environment, because its model and effort are compiled application values with no argv spelling. [6]
- The reader that recovers the applied selection from a probe launch spec. [7]
- This factory's own recovery helper; it refuses a resolved launch that arrives without adapter-produced knobs. [8]
- The selection and its knobs are one frozen pair, so the factory's argument count stays inside the repository limit without an exemption. [9]
- The three pre-existing construction guards were extracted with their messages unchanged. [10]
- A capsule is refused for any harness without a verified instruction channel, and filled into the sole Codex settings site otherwise. [11]

### Cross-Repo References

No external repository boundary is implemented by this factory.

No meaningful cross-repo references found.
