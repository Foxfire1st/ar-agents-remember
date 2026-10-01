# mcp/src/agents_remember/kernel/harnesses.py

## Governing Overview

[MCP package overview](../../../overview.md)

## Purpose

The harness vocabulary: what a harness IS, and the curated set of them. `HARNESSES` is the
developer-curated **max set** of native harnesses AR supports, and its docstring is the authoritative
statement of who may extend it.

It is a settings vocabulary, so it is `kernel` (`layers.toml`): the `orchestration.harnesses` family is
parsed into these objects by `kernel/agentic_settings.py`, which merges this table with what the user
declared and hands the effective registry downstream. Detection and launch deliberately stay in
`serving/harnesses.py`; what a harness *is* is the half a settings parser needs and the half nothing
above it can define without duplicating.

## Code Commentary

### Logic

`Harness` (150) is the row type: a stable `id`, a display `name`, the `command` to detect on `PATH`,
the fixed `argv`, and the optional knob-mapping fields for settings-defined non-native harnesses.
Two fields carry the readiness seam:

- **`runtime_probe: str | None = None`** (168) — how this harness is proved launchable here. `None`
  means the ordinary PATH probe; a registered id names a readiness resolver in `RUNTIME_PROBES` for a
  harness whose runtime is not a PATH command at all. Its comment states the reason: the question is
  "can this runtime start", not "is this name on PATH", and answering it with `which` would report a
  missing runtime as a generic not-installed harness.
- `command`/`argv` for such a row are an **honest placeholder** — `EVE_RUNTIME_COMMAND`
  (`"ar-eve-runtime-application"`) — a name that exists nowhere and is never spawned.

`HARNESSES` (187) now carries **four** rows: `claude`, `codex`, `pi`, and, **last, `eve`**. The eve
row is the only one with a `runtime_probe` (`EVE_RUNTIME_PROBE`), and it is last so the first-detected
default order `claude` → `codex` → `pi` → `eve` is unchanged and no existing row moved.

The probe registry is three small pieces: `RUNTIME_PROBES` (46) maps a probe name to a resolver,
`register_runtime_probe` (50) is the decorator a probe module uses to install itself, and
`load_runtime_probes` (60) imports the probe modules so their registration runs. Detection then has
one path with two branches inside `harness_availability_detail` (82) and `harness_runtime_verdict`
(106): a probe-declaring row is asked of its probe (with `env` and `which` forwarded), everything else
goes to `which`. `is_harness_available` (71) is the boolean shape of the same answer.

So the module owns the **name** of each probe and the seam that resolves it; the probe implementation
lives with the runtime it describes, in `kernel/eve_runtime_readiness.py`.

### Conventions

- A probe resolver is called with the keyword arguments `env` and `which` only, and returns
  `(ready, reason, locations)` — `ProbeResult`.
- `locations` is ordered **application root first, then interpreter**, because callers that need the
  runtime identity the probe already proved read it from the tail.
- The `HARNESSES` docstring is the authoritative statement of who may add a row; it is prose that
  governs a data table, and it is updated in the same change that adds a row.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.
- **An id becomes legal everywhere by gaining a row here.** The id set used by
  `orchestration.roles.*.harness` and `orchestration.spawn.harness` is derived from this table, and so
  is the loud unknown-harness refusal's list of known ids — so a row is the whole prerequisite for a
  harness being *selectable*, and nothing else in the tree needs a second list.
- **`eve` has a row, and it is a vocabulary row rather than a PATH row.** It is what makes
  `"harness": "eve"` legal; it does **not** make eve a terminal program, and terminal launch refuses it
  by name through `serving.harnesses.terminal_launch_detail`. The two registries still answer different
  questions — this one is "which ids exist and which ships by default", while
  `serving/harness_control_factories.BUILTIN_PROTOCOL_HARNESSES` is "which ids can construct a hosted
  protocol adapter".
- **A protocol adapter's existence does not earn a row here, and a row does not make a harness
  terminal-launchable.** Both directions of that confusion are live; keep them separate.
- **Never detect a probe-declaring row with `which`.** Detection must go through the probe registry;
  a direct `shutil.which(harness.command)` on the eve row would answer "no" on a machine where the
  runtime is present.
- The set is developer-curated: extending it is a product decision with a named owner, not an
  implementation detail a leaf may settle incidentally. A settings entry with a new id adds a harness
  and one with an existing id overrides the defaults — **but an override may not strip a builtin's
  readiness probe**, and `kernel/_agentic_settings_harness.py::_merged_harness` carries it across.

### Todos

None known. Packaging the runtime into `package_data/runtime/eve-agent` is another leaf's scope; the
probe already reads that path first when it exists.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation
pass was available for this update.

No configured `Domain Documentation` source exists in `system/sources.md`; the settings surface this table feeds is documented in-repo.

### Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range
holding the anchor.

- Defines the row type, including the `runtime_probe` field that decides how a harness is proved launchable. [1]
- The curated set: four rows, `eve` last and the only one carrying a readiness probe. [2]
- The probe registry: the name→resolver map, the registration decorator, and the loader that runs the registrations. [3]
- Detection's two branches: the probe for a probe-declaring row, `which` for everything else. [4]
- The probe implementation detection now asks, and the floor it owns for both readers. [5]
- The settings merge carries a builtin's probe across an override instead of dropping it. [6]
- The serving-side consumers: detection detail and the narrower terminal-launchability question. [7]
- The capability catalog gates on the readiness verdict rather than on `which`. [8]
- The separate protocol-adapter registry that an `eve` id also resolves through. [9]
- The cases: the eve row is last and the others are unchanged, it consults its probe and never PATH, and the path harnesses keep the ordinary lookup. [10]
- The settings case pinning that an override of a builtin keeps its runtime readiness probe, and that a settings-defined id declares none. [11]
