# mcp/src/agents_remember/kernel/harnesses.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/kernel/harnesses.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T13:26+02:00 |
| lastVerifiedCommitHash | `ea9cf0abeab4fe88961bda10b4f54d30266a9634` |
| lastVerifiedCommitDate | 2026-09-17T23:56:19+02:00|
| governingOverview | `../../../overview.md` |

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

## Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation
pass was available for this update.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured `Domain Documentation` source exists in `system/sources.md`; the settings surface this table feeds is documented in-repo. | — | — |

## Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range
holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Defines the row type, including the `runtime_probe` field that decides how a harness is proved launchable. | `Harness` | mcp/src/agents_remember/kernel/harnesses.py:149-184 |
| The curated set: four rows, `eve` last and the only one carrying a readiness probe. | `HARNESSES`; `EVE_RUNTIME_PROBE`; `EVE_RUNTIME_COMMAND` | mcp/src/agents_remember/kernel/harnesses.py:144-145; mcp/src/agents_remember/kernel/harnesses.py:187-212 |
| The probe registry: the name→resolver map, the registration decorator, and the loader that runs the registrations. | `RUNTIME_PROBES`; `register_runtime_probe`; `load_runtime_probes`; `ProbeResult`; `RuntimeProbe` | mcp/src/agents_remember/kernel/harnesses.py:38-38; mcp/src/agents_remember/kernel/harnesses.py:43-43; mcp/src/agents_remember/kernel/harnesses.py:46-46; mcp/src/agents_remember/kernel/harnesses.py:50-57; mcp/src/agents_remember/kernel/harnesses.py:60-68 |
| Detection's two branches: the probe for a probe-declaring row, `which` for everything else. | `is_harness_available`; `harness_availability_detail`; `harness_runtime_verdict` | mcp/src/agents_remember/kernel/harnesses.py:71-79; mcp/src/agents_remember/kernel/harnesses.py:82-103; mcp/src/agents_remember/kernel/harnesses.py:106-139 |
| The probe implementation detection now asks, and the floor it owns for both readers. | `eve_runtime_readiness`; `MINIMUM_NODE_MAJOR` | mcp/src/agents_remember/kernel/eve_runtime_readiness.py:55-55; mcp/src/agents_remember/kernel/eve_runtime_readiness.py:89-128 |
| The settings merge carries a builtin's probe across an override instead of dropping it. | `_merged_harness` | mcp/src/agents_remember/kernel/_agentic_settings_harness.py:133-182 |
| The serving-side consumers: detection detail and the narrower terminal-launchability question. | `is_detected`; `harness_detection_detail`; `terminal_launch_detail`; `detect_harnesses` | mcp/src/agents_remember/serving/harnesses.py:93-107; mcp/src/agents_remember/serving/harnesses.py:110-124; mcp/src/agents_remember/serving/harnesses.py:127-153; mcp/src/agents_remember/serving/harnesses.py:156-174 |
| The capability catalog gates on the readiness verdict rather than on `which`. | `HarnessCapabilityCatalog`; `_probed_install` | mcp/src/agents_remember/serving/harness_capability_catalog.py:84-212; mcp/src/agents_remember/serving/harness_capability_catalog.py:215-224 |
| The separate protocol-adapter registry that an `eve` id also resolves through. | `BUILTIN_PROTOCOL_HARNESSES`; `create_harness_protocol_adapter` | mcp/src/agents_remember/serving/harness_control_factories.py:33-33; mcp/src/agents_remember/serving/harness_control_factories.py:56-102 |
| The cases: the eve row is last and the others are unchanged, it consults its probe and never PATH, and the path harnesses keep the ordinary lookup. | `EveRegistryTests` | mcp/tests/test_eve_product_integration.py:694-748 |
| The settings case pinning that an override of a builtin keeps its runtime readiness probe, and that a settings-defined id declares none. | `test_a_builtin_override_keeps_its_runtime_readiness_probe`; `test_new_id_adds_a_harness_with_defaults_derived` | mcp/tests/test_agentic_settings.py:268-278; mcp/tests/test_agentic_settings.py:280-294 |

## Update History
- 2026-09-17T20:42:17+00:00: Generated citation repair: `EveRegistryTests` repointed to mcp/tests/test_eve_product_integration.py:694-748. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-16T13:26+02:00 — 260915-CAPS-L8 curator: **the card's central claim was inverted by this
  change set, so it is corrected rather than deleted.** The previous entry recorded that the native eve
  protocol adapter "deliberately has no row here" and that an `eve` id "resolves through the protocol
  factory only and never through terminal launch". eve now **has** a row — last in `HARNESSES`, and the
  only row carrying `runtime_probe=EVE_RUNTIME_PROBE` — which is what makes `"harness": "eve"` legal
  everywhere the id set is validated. Recorded the new probe seam this module owns (`RUNTIME_PROBES`,
  `register_runtime_probe`, `load_runtime_probes`, `ProbeResult`/`RuntimeProbe`) and its two-branch
  detection (`is_harness_available`, `harness_availability_detail`, `harness_runtime_verdict`), the
  honest `EVE_RUNTIME_COMMAND` placeholder that is never spawned, the ordering guarantee (row last, so
  the first-detected default is unchanged), and the corrected boundary: a row makes a harness
  *selectable*, not *terminal-launchable*, and an override may not strip a builtin's probe. Reference
  table extended from three rows to eleven. Verification metadata moves to the leaf's synced base
  `ff97072c`; the candidate is deliberately uncommitted, so the governed closeout stamps the real code
  commit and no hash or fingerprint was invented here.

- 2026-09-16T10:15+02:00 — 260915-CAPS-L6 curator (A2 delta pass): **No content impact from the A2
  revision.** This file is byte-identical between the A1 and A2 candidates of the same change set, so
  the body — the `HARNESSES` docstring's record of why the native eve protocol adapter deliberately
  has no row here — is retained unchanged. The pass advanced the verification metadata to the leaf's
  current base `e9300687` under the leaf's one consistent convention (the candidate is uncommitted, so
  the governed closeout re-stamps the real code commit) and re-read the existing citations, which
  remain in the required `Finding | Anchor | Source` shape. No hash or fingerprint was invented.

- 2026-09-16T09:00+02:00 — 260915-CAPS-L6 curator: the curated set is unchanged (still `claude`,
  `codex`, `pi`) and this file's **only** delta is the `HARNESSES` docstring, which now records why
  the new native eve protocol adapter deliberately has no row here: eve's runtime is an AR-owned
  application, not a `PATH` command, so terminal-harness exposure is the packaging/capability leaf's
  decision. Body updated to state that boundary as an invariant rather than leaving the card silent
  about a registry that now contains an adapter with no row. Verification metadata pinned until
  closeout stamps the candidate commit.

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
