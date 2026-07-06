# mcp/src/agents_remember/kernel/agentic_settings.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/kernel/agentic_settings.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-07T09:45+02:00 |
| lastVerifiedCommitHash | `49a5e476b918f740bda6eec584eb7bf185aecb6e` |
| lastVerifiedCommitDate | 2026-07-06T21:48:46+02:00|
| governingOverview      | `../../../overview.md`                     |

## Purpose

`agentic_settings.py` is the two-layer AGENTIC settings loader (260703-L13): it reads the
GLOBAL `<coordination_root>/system/settings.json` plus an optional repo-local
`<code_repo>/system/settings.json`, merges them, and parses the top-level `orchestration`
family — gate delegation, the three-party-loop knobs, per-role knob overrides (flat `roles` +
per-level `rolesPerLevel`, incl. the free-form escape hatch), concurrency caps, the spawn harness
preference, and the harness-definition table `orchestration.harnesses` (260703-L16) — into frozen
typed models. It is the single parser
for the agentic family; the MCP authority file, memory-topology settings, and provider
lifecycle settings are separate families with separate parsers.

## Code Commentary

### Logic

L13 review follow-up (L13R-2): the loader REFUSES `gateDelegation` in the repo-local layer — a local value would validate and then silently do nothing (the boot snapshot reads the global file only), a fail-open shape; the refusal names the local file and states "global-layer only".

`load_agentic_settings(coordination_root, repo_root=None)` is the PER-USE entry point: each
call re-reads both files (no caching), so an edit takes effect on the next use without a
server restart. Each present file's `orchestration` block is first validated INDIVIDUALLY
(`_validated_orchestration_block`) so key/type errors name the offending file — since L16 that
per-file pass runs `_parse_orchestration(..., strict=False)`: shapes and unknown keys only, because
one LAYER may legitimately be partial (a repo-local file overriding a single leaf of a
globally-defined harness entry, or referencing a harness id the other layer declares). The blocks
are then merged (`merge_settings` — deep merge at leaf-key granularity, object leaves recurse,
scalars AND arrays are REPLACED by the override, local over global) and the merged block is parsed
STRICT into `AgenticSettings` — cross-layer rules (harness-entry completeness, harness-id
membership) bind on the merged block, with the merged source label in errors.

The fail-loud rule is scoped to `orchestration.*`: every nesting level has a frozen
known-key set (`KNOWN_ORCHESTRATION_FIELDS` = gateDelegation/loops/roles/rolesPerLevel/
concurrency/spawn/harnesses, plus per-family sets for gateDelegation kinds, loop
defaults/complexity/levels, the six l-01 role names, the role-knob fields
harness/model/effort/launchArgs/promptKeywords/sessionCommands, the harness-entry fields, and
concurrency caps) and `_refuse_unknown` raises
`AgenticSettingsError` naming the unknown keys, the allowed set, and the offending file.
Unknown TOP-LEVEL keys are deliberately tolerated-not-parsed: the same coordinator file is
the c-08 memory-settings fallback and the earmarked future home of further families
(`contextProviders` first in line — gate amendment 2026-07-06), so the fail-loud scope must
not foreclose them. Absent files (or an absent `orchestration` key) yield the documented
defaults: all-human gate policy, the L12 loop defaults (`maxRounds` 3, `delta-verify`
reviewer reuse, complexity high/medium, perLevel scored/seam-required/strategist), no role
overrides, uncapped concurrency, no spawn preference. Malformed JSON and non-object roots
fail loud with the path.

`parse_gate_delegation(raw, source=...)` is the gateDelegation parser MOVED here from
`mcp/config.py` (its logic is unchanged: named policy via `named_gate_policy`, per-kind
rule overrides via `_parse_gate_policy_rule`, `requireReviewerVerdictAtSeams` binding via
`apply_seam_verdict_requirement`); it now raises `AgenticSettingsError` with the source
appended and is shared by this loader (the key's new home) and `mcp/config.py`'s one-cycle
legacy authority-file fallback. `AgenticSettings.gate_delegation_configured` records
whether a FILE set the key (vs. the default) — the boot-snapshot consumer branches on it.

**Role knobs (L16 three-layer model).** `RoleKnobs` carries the validated enums (`harness` — a
known id; `model`/`effort` — free strings HERE, the per-harness effort vocabulary is enforced at
DISPATCH where the harness is known) plus the free-form escape hatch (`launchArgs`/
`promptKeywords`/`sessionCommands` — `_require_string_list` shape-checks a non-empty string list,
content is NEVER validated; the spawn path records it in provenance). `orchestration.rolesPerLevel`
(ruling 2026-07-07T08:15) parses the same knob shape per level (`_parse_roles_per_level`, level
vocabulary = `KNOWN_LOOP_LEVELS` leaf|master|portfolio, congruent with `loops.perLevel`);
`AgenticSettings.resolved_role_knobs(role, level="leaf")` deep-merges the level override over the
flat default field-wise (harness inherited unless overridden, lists REPLACE) — realizing the
dispatch chain repo-local level override > global level override > repo-local role default >
global role default on top of the file merge.

**Harness definitions (L16 registry openness).** `_parse_harnesses` (decomposed into
`_parse_harness_entry` → frozen `_HarnessEntry` shape record, `_resolved_launch` command/argv
derivation, `_merged_harness` replace-over-fallback merge, `_refuse_unpaired_vehicles`) parses
`orchestration.harnesses` into the EFFECTIVE registry (`AgenticSettings.harnesses`, default the
builtin `HARNESSES`): entries merge over the builtin table by id — a NEW id must resolve
`command` and/or `argv` (`command` defaults to `argv[0]`, `argv` to `(command,)`) and is tagged
`defined_in="settings"`; a builtin id overrides per field. Delivery-vehicle pairs must resolve
together post-merge (`effortFlag`+`effortFlagValues`, `effortSessionValues`+`effortSessionCommand`
— a flag without a vocabulary would reintroduce the silent-degrade risk). Harness references
(`orchestration.spawn.harness`, `roles.<role>.harness`) are validated against the EFFECTIVE id set
(`_require_harness_id` with the merged ids; the per-file pass passes `None` = shape-only), so a
settings value can never inject argv through a reference — argv is definable only in the explicit,
fail-loud harnesses family.
Loop POSTURE names (`perLevel.<level>.loop`, `perMaster.<master>.<level>.loop`) are
model-interpreted doctrine, validated as non-empty strings, deliberately not a closed set;
complexity thresholds ARE scale-validated against `COMPLEXITY_SCALE` (low/medium/high).
`default_agentic_settings_seed()` / `default_agentic_settings_seed_text()` produce the
seeded global-file content (`$comment` header naming the schema doc, all-human
gateDelegation, the L12 loop defaults, no spawn preference) shared by `install/runtime.py`'s
copy-if-missing seeding and the c-13 interview's starting point.

### Conventions

Kernel-level module: consumers are `mcp/config.py` (boot-snapshot gateDelegation),
`mcp/tools/terminal.py` (per-use knob/harness resolution at dispatch), `serving/app.py`
(effective registry for `GET /api/harnesses` + the dashboard open route, global layer), and
`install/runtime.py` (seed). Frozen dataclasses (`AgenticSettings`, `LoopSettings`, `LoopDefaults`,
`LoopComplexity`, `RoleKnobs`, `ConcurrencySettings`) follow the `McpRuntimeConfig` style;
`AgenticSettingsError` joins the typed `AgentsRememberError` family (a `ValueError`
subclass). The kernel→serving import is a constant-table + frozen-dataclass import only
(`HARNESSES`, `Harness` — the loader constructs effective `Harness` rows, no serving I/O).

### Invariants And Boundaries

- Read PER-USE, never boot-cached — the ONE boot-snapshot consumer is
  `mcp/config.py`'s gateDelegation (documented restart-required semantics).
- Fail-loud is `orchestration.*`-scoped; top-level families are tolerated
  (reserved: contextProviders returns here in a follow-up).
- Doctrine floors are not knobs: no key touches the master-exit seam gate or the
  strategist's mandatory pre-run (L12 ruling, restated in the module docstring).
- Arrays REPLACE on merge, never concatenate; sibling leaves survive an override.
- `sources` records the files actually read (global first) for error/refusal messages.

### Todos

No known follow-up in this file. (The contextProviders family migration and a
dashboard settings write path are tracked outside as follow-ups.)

## Docs References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The schema reference for the agentic family (two-layer model, merge semantics, fail-loud rule, loop schema, reserved families). | Agentic Settings section | [../../../../../docs/reference/settings-json.md](../../../../../docs/reference/settings-json.md) |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The gate policy primitives the gateDelegation parse builds on (named policies, rule construction, seam verdict binding). | L1-L120 | [../controlplane/gate_policy.py](../controlplane/gate_policy.py) |
| The harness registry whose ids bound every harness preference value. | L41-L48 | [../serving/harnesses.py](../serving/harnesses.py) |
| The boot-snapshot consumer: gateDelegation sourced from the global file at boot with the legacy authority fallback. | parse_orchestration_settings | [../mcp/config.py](../mcp/config.py) |
| The per-use spawn consumer: explicit arg > repo-local > global > detection-gated default. | _resolve_spawn_harness | [../mcp/tools/terminal.py](../mcp/tools/terminal.py) |
| The install seeding consumer (copy-if-missing global file). | seed_agentic_settings | [../install/runtime.py](../install/runtime.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The loader operates on coordinator/repo-local files only. | - | - |

## Update History

- 2026-07-07T09:45+02:00 — 260703-L16 (spawn knob application; rulings 2026-07-07T05:30/07:30/08:15):
  role knobs gained the free-form escape hatch (`launchArgs`/`promptKeywords`/`sessionCommands` —
  shape-checked string lists, never content-validated); `effort` documented as a deliberate free
  string at load (per-harness dispatch validation); NEW `orchestration.rolesPerLevel` family
  (per-level knob overrides, `resolved_role_knobs` deep-merge) and NEW `orchestration.harnesses`
  family (`_parse_harnesses` — settings-defined harnesses merge over the builtin registry into
  `AgenticSettings.harnesses`, vehicle-pair rules, `defined_in` tagging); harness references now
  validate against the EFFECTIVE id set, and per-file validation became shape-only
  (`strict=False`) so partial cross-layer overrides merge correctly. Verification metadata pinned
  until closeout stamps the L16 commit.

- 2026-07-06T23:45+02:00 — L13 adversarial-review follow-up (L13R-2): repo-local gateDelegation refused loudly (global-layer only); regression test added. Verification metadata pinned until closeout stamps the L13 commit.

- 2026-07-06T22:10+02:00 — 260703-L13 (settings unification): created the two-layer agentic
  settings loader — per-use global+local read, leaf-key deep merge with array-replace,
  `orchestration.*`-scoped fail-loud unknown-key refusal naming the offending file, typed
  models for gateDelegation (moved here from `mcp/config.py`), the L12 loop schema, role
  knobs, concurrency caps, and the registry-validated spawn harness preference, plus the
  shared install seed. Verification metadata pinned until closeout stamps the L13 commit.
