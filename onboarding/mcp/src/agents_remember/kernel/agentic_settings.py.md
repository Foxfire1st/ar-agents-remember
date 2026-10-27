# mcp/src/agents_remember/kernel/agentic_settings.py

## Governing Overview

[MCP package overview](../../../overview.md)

## Purpose

The loader still rereads the guarded user file plus optional repository layer and assembles frozen agentic settings. Its current execution registry is an ID vocabulary, not a harness-definition table or free-form escape hatch.

> **Historical pre-current-loader account — retained, not an operative parser/consumer promise:**
> `agentic_settings.py` is the two-layer AGENTIC settings loader (260703-L13): it reads the
> USER `~/.config/agents-remember/settings.json` (or under `XDG_CONFIG_HOME`) plus an optional repo-local
> `<code_repo>/system/settings.json`, merges them, and parses the top-level `orchestration`
> family — gate delegation, the three-party-loop knobs, per-role knob overrides (flat `roles` +
> per-level `rolesPerLevel`, incl. the free-form escape hatch), concurrency caps, the spawn harness
> preference, and the harness-definition table `orchestration.harnesses` (260703-L16) — into frozen
> typed models. It is the single parser
> for the agentic family; the MCP authority file, memory-topology settings, and provider
> lifecycle settings are separate families with separate parsers. Removed `orchestration.agentNotifier` and `supervisor` settings load as accepted unused data and are reported, not parsed as active sweep/redelivery knobs. The HFX2-L2/L8/L9 alias, cadence and budget account is historical; no current sweep or notifier authority follows from it.

## Code Commentary

`_parse_orchestration` parses `roleMessageLimit` through the shared positive-integer validator with the field/source named in failures, and defaults an absent/null value to `DEFAULT_ROLE_MESSAGE_LIMIT`. The facade exports that constant. Dynamic role-message enforcement is a separate consumer: the delivered wake text is bounded, while body and attachment payload files are not.

### 260714-ACPUI-L2 Dynamic Native Launch Authority

Current role model/effort strings are shape-checked here and catalog-validated at native launch. Legacy harness execution fields remain accepted-unused; this loader builds no executable registry mappings or paste commands.

> **Historical pre-current-loader account — retained, not an operative parser/consumer promise:**
> `RoleKnobs.model` and `RoleKnobs.effort` remain stripped, non-empty settings values at this parser
> boundary. For the built-in Claude, Codex, and Pi protocol harnesses, this module deliberately does
> not impose a static model or effort vocabulary: dispatch carries the complete settings selection
> into the typed native launch boundary, where the adapter validates it against a token-free,
> per-install catalog and the selected model's own effort options. Settings-defined non-native
> harnesses retain their explicit registry mappings and dispatch-time validation. The free-form
> `launchArgs`, `sessionCommands`, and `promptKeywords` fields remain independently user-authored;
> the parser never derives a model/effort paste command from them.

### 260707-HFX2-L12 CS-6 Update

Historical HFX2-L12 introduced escalationBudget with default250 beside redeliverBudget. Those removed settings/consumer are now accepted unused data; no serving supervisor reads an active escalation setting.

#

- 260731-EFA-L7 (historical trace): settings responsibilities were split into sibling modules and the then-existing facade suite pinned exports. That suite has since been retired. The current loader is `load_agentic_settings`; this historical record does not establish current export coverage.

### 260731-EFA-L17/L24 — Optional Quality-Gate Memory Cap

The loader now parses `orchestration.qualityGate.memoryCapBytes` (260731-EFA-L17-R3):
`KNOWN_ORCHESTRATION_FIELDS` gained `qualityGate` (core), `_parse_orchestration`
(lines 331-367) wires `_parse_quality_gate(raw.get("qualityGate"), source=source)` into
`AgenticSettings.quality_gate`, and the facade re-exports `QualityGateSettings`,
`KNOWN_QUALITY_GATE_FIELDS` and
`_parse_quality_gate` through `__all__` (lines 141-205). The value is the settings-owned
optional hard cap for full-wrapper runs at the master integration gate; an absent key
keeps RAM and swap host-managed, unknown keys fail loud like every other orchestration
family, and a JSON `null` at the family key is refused.


**L184 — NEW-R192-EXTRA-ARGS.** The resolved view is what a launch reads, so the entries and their origins are realized here. The obligation this leaf records for this place is stated in the invariant named here; the card's earlier account of this file stands, and this paragraph adds what the change made true.

## Logic

Current _parse_harnesses admits known legacy entry keys as unread execution data and now returns two parts: the effective IDs and the harness-level `extraArgs` entries, which are attached to the settings beside them. It does not enforce effortFlagValues or an execution-command mapping.

> **Historical pre-current-loader account — retained, not an operative parser/consumer promise:**
> **260714-ACPUI-L2 effort policy.** When a settings-defined non-native harness declares
> `effortFlagValues`, the effective merged harness uses enumerated validation so its explicit menu is
> not bypassed. Built-in Claude, Codex, and Pi rows carry no static effort mapping; a partial command
> or argv override does not invent one. Their model-gated validation belongs to dynamic adapter
> discovery at launch.

Supervisor/redelivery knobs are accepted-unused, and there is no _merged_harness execution-policy owner in this module.

> **Historical pre-current-loader account — retained, not an operative parser/consumer promise:**
> **260707-HFX2-L15 dispatch bounds and harness overrides.** The default supervisor redelivery budget
> is `1`, matching the synchronous calibrated log-verification envelope of one input. When settings
> introduce or replace a Codex `effortFlag`, `_merged_harness` keeps any retired native config-value
> template cleared so the explicit custom mapping receives an ordinary discrete value.

L13 review follow-up (L13R-2): the loader REFUSES `gateDelegation` in the repo-local layer — a local value would validate and then silently do nothing (the boot snapshot reads the global file only), a fail-open shape; the refusal names the local file and states "global-layer only".

`load_agentic_settings(coordination_root, repo_root=None)` rereads both layers per use. Each file is shape/key-validated first; recursive object merge retains siblings while scalar/array values replace local-over-user. Merged parsing validates the spawn harness against effective IDs, not command/argv completeness. Role harness/model/effort remain shape-checked free strings until host catalog validation at launch. Sources retain global-first file order.

> **Historical loader wording — command-registry completeness is superseded, not a current validation promise:**
> `load_agentic_settings(coordination_root, repo_root=None)` is the PER-USE entry point: each
> call re-reads both files (no caching), so an edit takes effect on the next use without a
> server restart. Each present file's `orchestration` block is first validated INDIVIDUALLY
> (`_validated_orchestration_block`) so key/type errors name the offending file — since L16 that
> per-file pass runs `_parse_orchestration(..., strict=False)`: shapes and unknown keys only, because
> one LAYER may legitimately be partial (a repo-local file overriding a single leaf of a
> globally-defined harness entry, or referencing a harness id the other layer declares). The blocks
> are then merged (`merge_settings` — deep merge at leaf-key granularity, object leaves recurse,
> scalars AND arrays are REPLACED by the override, local over global) and the merged block is parsed
> STRICT into `AgenticSettings` — cross-layer harness-definition completeness and spawn-harness
> membership bind on the merged block, with the merged source label in errors. Role harness, model
> and effort values are nonempty strings checked for parser shape, not effective-registry membership;
> the actual launch/dispatch owner validates its catalog or registry choices.

The fail-loud rule is scoped to `orchestration.*`. The orchestration allowlist also includes landing; facade exports its model/default/key set/parser and assembles it per use. `_refuse_unknown` names the offending keys, allowed set and source file.

The escalation-ladder account previously recorded here is historical: the current allowlist and
assembly contain no `orchestration.escalation`, `EscalationSettings` or `_parse_escalation` route.
An authored `orchestration.escalation` key is refused as unknown; the old parser decomposition and
rung/SLA defaults must not be used as a current configuration contract.

Expectation/supervisor/agentNotifier families are reported accepted-unused. No AgentNotifierSettings, sweep cadence, SLA or redelivery floor is assembled by this loader.

> **Historical pre-current-loader account — retained, not an operative parser/consumer promise:**
> **260707-HFX2-L2/R8/R9 (supervisor sweep knobs)**: `orchestration.agentNotifier` configures the
> deterministic sweep loop hosted beside the serving daemon's projector/metrics loops —
> `AgentNotifierSettings` (`enabled` default `true`, `interval_seconds` default 10.0,
> `stale_cutoff_seconds` default 60.0, `redeliver_rate_limit_seconds` default `None`,
> `signal_cooldown_seconds` default `DEFAULT_RATE_LIMIT_SECONDS` / 900, `redeliver_budget` default
> 1, and `escalation_budget` default 250). `_parse_agent_notifier` validates boolean/positive fields and checks
> `redeliverRateLimitSeconds` plus `signalCooldownSeconds` through `_require_agent_notifier_floor_seconds`,
> which refuses any value below `inbox_backoff.MIN_REDELIVERY_INTERVAL_SECONDS` (900). Absent block or
> absent key both fall back to the documented default (`AgentNotifierSettings()`'s field defaults).
> `redeliver_rate_limit_seconds=None` is a deliberate inherit-not-duplicate choice: the sweep passes
> `None` straight through to `OperatorInboxStore.list_redeliverable`, which already owns its own
> default (`inbox_backoff.DEFAULT_RATE_LIMIT_SECONDS`) — the same "`None` = uncapped/inherit"
> convention `ConcurrencySettings` already uses elsewhere in this file, so the floor is never copied
> as an unrelated second source of truth. `signal_cooldown_seconds` is an explicit settings value
> because repeated owner-signal minting has its own cooldown store. `redeliver_budget` is parsed from
> `redeliverBudget` as a positive integer and is intentionally present in the empty-block default so a
> default incident deployment gets bounded sweep work without needing a new knob.

Expectation-family configuration is accepted-unused; it does not populate typed SLA fields. Top-level non-orchestration families remain tolerated by the orchestration loader.

> **Historical pre-current-loader account — retained, not an operative parser/consumer promise:**
> **260707-HFX2-L1 (R2, expectation-row SLAs)**: `orchestration.expectations.defaults` configures
> the per-kind SLA seconds every dispatch surface's durable expectation row uses (`briefed-by`,
> `turn-report-by`, `verdict-by`, `ack-by`) — `ExpectationSettings.sla_for(kind)` falls back to
> `DEFAULT_EXPECTATION_SLA_SECONDS` (`ack-by` mirrors the existing `AGENT_PICKUP_TTL_SECONDS`
> convention, 300s) for any kind the settings omit. `_parse_expectations` validates every key
> against `KNOWN_EXPECTATION_KINDS` (fail-loud on an unknown kind or non-positive SLA). This literal
> kind set is duplicated in `controlplane/expectation_rows.py::ExpectationKind` rather than imported,
> to avoid a kernel<->controlplane import cycle — the two must be kept in sync by hand.
> Unknown TOP-LEVEL keys are deliberately tolerated-not-parsed: the same user file is
> the c-08 memory-settings fallback and the earmarked future home of further families
> (`contextProviders` first in line — gate amendment 2026-07-06), so the fail-loud scope must
> not foreclose them. Absent files (or an absent `orchestration` key) yield the documented
> defaults: all-human gate policy, the current loop defaults (`maxRounds` 5, `delta-verify`
> reviewer reuse, complexity high/medium, perLevel scored/seam-required/strategist), no role
> overrides, uncapped concurrency, no spawn preference. Malformed JSON and non-object roots
> fail loud with the path. A JSON `null` at ANY known `orchestration.*` family key (either
> layer) is REFUSED by `_refuse_null_families` in `_validated_orchestration_block` (260703-L18
> finding 6, developer-ruled `null` = refuse): `null` reads as *absent* to every family parser
> and `merge_settings` REPLACES a non-object, so `"concurrency": null` in the repo-local layer
> would otherwise SILENTLY wipe the global caps — the one scalar collision that used to defeat
> both the deep-merge and fail-loud invariants. The refusal names the offending file with the
> guidance "remove the key to inherit the global value". Ordering: `_refuse_null_families` runs
> inside `_validated_orchestration_block`, so a repo-local `gateDelegation: null` hits the null
> refusal FIRST; the dedicated repo-local `gateDelegation` presence refusal in
> `load_agentic_settings` still fires for any non-null value.

`parse_gate_delegation(raw, source=...)` is the gateDelegation parser MOVED here from the
former `mcp/config.py` (now `kernel/primitives/runtime_config.py`) (its logic is unchanged: named policy via `named_gate_policy`, per-kind
rule overrides via `_parse_gate_policy_rule`, `requireReviewerVerdictAtSeams` binding via
`apply_seam_verdict_requirement`); it now raises `AgenticSettingsError` with the source
appended and is shared by this loader (the key's new home) and `kernel/primitives/runtime_config.py`'s one-cycle
legacy authority-file fallback. `AgenticSettings.gate_delegation_configured` records
whether a FILE set the key (vs. the default) — the boot-snapshot consumer branches on it.

Current flat and altitude role rows carry harness/model/effort/tier/mode/features/notes/origins and optional user-owned stepUp. Legacy launchArgs/promptKeywords/sessionCommands are accepted-unused and not validated as executable string lists. The normal field/feature/origin merge and exact user-only mode/notes/stepUp authority still apply.

> **Historical pre-current-loader account — retained, not an operative parser/consumer promise:**
> **Role knobs (L16 three-layer model, ACPUI-L2 launch boundary).** `RoleKnobs` carries the validated
> `harness` id plus `model`/`effort` as free strings at this parser boundary. Built-in native values
> are structurally required at role dispatch and validated against the model-gated dynamic catalog
> inside the hosted runner; explicit non-native registry mappings are validated at dispatch. The
> free-form escape hatch (`launchArgs`/
> `promptKeywords`/`sessionCommands` — `_require_string_list` requires a non-empty LIST of non-empty
> strings; an EMPTY list REFUSES (PR #100 review, Codex P2: `RoleKnobs` cannot distinguish absent from
> cleared — empty tuple = not configured — so a per-level `[]` meant to clear a flat default would
> silently INHERIT it through the field-wise `or` merge; omit the key to inherit, list values to
> override); content is NEVER validated; the spawn path records it in provenance). `orchestration.rolesPerLevel`
> (ruling 2026-07-07T08:15) parses the same knob shape per level (`_parse_roles_per_level`, level
> vocabulary = `KNOWN_LOOP_LEVELS` leaf|master|portfolio, congruent with `loops.perLevel`);
> `AgenticSettings.resolved_role_knobs(role, level="leaf")` deep-merges the level override over the
> flat default field-wise (harness inherited unless overridden, lists REPLACE) — realizing the
> dispatch chain repo-local level override > global level override > repo-local role default >
> global role default on top of the file merge. Role knobs now also carry `mode`, `featureValues` and `notes` with per-choice origins: `_attach_role_origins` binds each authored value to its file, key, provider and model without changing the merge, repository layers cannot author mode, notes or permission-bearing feature values (`_refuse_repository_role_authority` refuses them naming file and key), and an old-only or both-file state refuses through the location guard before any content read.

The current closed role vocabulary for flat `orchestration.roles` and per-level
`orchestration.rolesPerLevel` is `architect`, `orchestrator`, `designer`, `strategist`, `manager`,
`worker`, `curator`, `reviewer`, `investigator` and `bootstrap`. Unknown roles remain fail-loud.
`system-specialist` is the accepted compatibility spelling normalized to `investigator`, not an additional
canonical role. The earlier eight/nine-role descriptions are historical vocabulary observations,
not the current allowlist or an instruction selecting a seat.

Current _parse_harnesses returns built-in IDs plus settings-added IDs together with each harness's `extraArgs` entries, and validates the entry and key shape while parsing each harness's `extraArgs` records, which the loader stores as `harness_extra_args`; a role's own `extraArgs` is checked against its named harness and its capability before it is kept, so the return is the IDs, the entries and those records, not the IDs alone. Command/argv/effort vehicle fields are accepted-unused; no _HarnessEntry, _merged_harness or effort-session-template consumer is constructed here.

> **Historical pre-current-loader account — retained, not an operative parser/consumer promise:**
> **Harness definitions (L16 registry openness).** `_parse_harnesses` (decomposed into
> `_parse_harness_entry` → frozen `_HarnessEntry` shape record, `_resolved_launch` command/argv
> derivation, `_merged_harness` replace-over-fallback merge, `_refuse_unpaired_vehicles`) parses
> `orchestration.harnesses` into the EFFECTIVE registry (`AgenticSettings.harnesses`, default the
> builtin `HARNESSES`): entries merge over the builtin table by id — a NEW id must resolve
> `command` and/or `argv` (`command` defaults to `argv`, `argv` to `(command,)`) and is tagged
> `defined_in="settings"`; a builtin id overrides per field. Delivery-vehicle pairs must resolve
> together post-merge (`effortFlag`+`effortFlagValues`, `effortSessionValues`+`effortSessionCommand`
> — a flag without a vocabulary would reintroduce the silent-degrade risk). The
> `effortSessionCommand` TEMPLATE is additionally validated post-merge by `_refuse_bad_effort_template`
> (260703-L18 finding 4): it must render with `.format(value=…)` and reference no replacement field
> other than `{value}` — a stray field (`/set {mode}={value}`), a positional `{}`, or an unmatched
> brace refuses naming the harness. A builtin override may supply just the command, so the check lives
> here beside the pairing rule; once validated, the raw `KeyError` at `serving/harnesses.py`
> (`effort_session_commands`' `.format`) is unreachable from settings. The spawn harness reference
> (`orchestration.spawn.harness`) is validated against the EFFECTIVE id set by `_require_harness_id`
> with merged IDs; its per-file pass is shape-only. `_parse_roles` receives no harness ID set and
> shape-checks role harness/model/effort strings; native/Paseo catalog validation or explicit registry
> adapter validation occurs later at launch/dispatch. Harness-definition argv remains in the explicit,
> fail-loud harnesses family; these distinct parser and dispatch boundaries are not a universal
> role-membership guarantee at settings load.
> Loop POSTURE names (`perLevel.<level>.loop`, `perMaster.<master>.<level>.loop`) are
> model-interpreted doctrine, validated as non-empty strings, deliberately not a closed set;
> complexity thresholds ARE scale-validated against `COMPLEXITY_SCALE` (low/medium/high).
> `default_agentic_settings_seed()` / `default_agentic_settings_seed_text()` produce the
> seeded global-file content (`$comment` header naming the schema doc, all-human
> gateDelegation, the L12 loop defaults, no spawn preference) shared by `install/runtime.py`'s
> copy-if-missing seeding and the c-13 interview's starting point.

### Conventions

Kernel-level loader and typed models are used by launch defaults and other callers; this file imports kernel.harnesses.HARNESS_IDS rather than serving execution adapter objects. AgentsRememberError remains the common typed error family.

> **Historical pre-current-loader account — retained, not an operative parser/consumer promise:**
> Kernel-level module: consumers are `kernel/primitives/runtime_config.py` (boot-snapshot gateDelegation),
> `mcp/tools/terminal.py` (per-use knob/harness resolution at dispatch), `serving/app.py`
> (effective registry for `GET /api/harnesses` + the dashboard open route, global layer), and
> `install/runtime.py` (seed). Frozen dataclasses (`AgenticSettings`, `LoopSettings`, `LoopDefaults`,
> `LoopComplexity`, `RoleKnobs`, `ConcurrencySettings`) follow the `McpRuntimeConfig` style;
> `AgenticSettingsError` joins the typed `AgentsRememberError` family (a `ValueError`
> subclass). The kernel→serving import is a constant-table + frozen-dataclass import only
> (`HARNESSES`, `Harness` — the loader constructs effective `Harness` rows, no serving I/O).

### Invariants And Boundaries

- Read PER-USE, never boot-cached — the ONE boot-snapshot consumer is
  `kernel/primitives/runtime_config.py`'s gateDelegation (documented restart-required semantics).
- Fail-loud is `orchestration.*`-scoped; top-level families are tolerated
  (reserved: contextProviders returns here in a follow-up).
- A `null` at a known family key is REFUSED (either layer) — never a silent
  wipe, never a reset-to-default; remove the key to inherit the global value.
Legacy effortSessionCommand is accepted-unused; no template execution or post-merge template validator belongs to the current loader.

> **Historical pre-current-loader account — retained, not an operative parser/consumer promise:**
> - `effortSessionCommand` templates are template-validated post-merge, so a bad
>   template refuses at load, not at spawn (raw `str.format` crash unreachable).
- Doctrine floors are not knobs: no key touches the master-exit seam gate or the
  strategist's mandatory pre-run (L12 ruling, restated in the module docstring).
- Arrays REPLACE on merge, never concatenate; sibling leaves survive an override.
Legacy free-form role fields are accepted-unused; empty-list execution semantics described below are historical, not a current input refusal.

> **Historical pre-current-loader account — retained, not an operative parser/consumer promise:**
> - An EMPTY free-form list is REFUSED (either layer, flat or per-level): `()` is the
>   not-configured sentinel, so `[]` cannot express "cleared" and would silently inherit —
>   omit the key to inherit (PR #100 review).
- `sources` records the files actually read (global first) for error/refusal messages.
- The global layer is the user's file: an old coordination file refuses load before any content read, naming both paths and the explicit whole-file upgrade command.

### Todos

No known follow-up in this file. (The contextProviders family migration and a
dashboard settings write path are tracked outside as follow-ups.)

## Current Contract — Scoped Launch And Settings Changes

load_agentic_settings still resolves the single guarded user file plus optional repository-local layer, validates individual file shapes, deep-merges local over user and returns typed settings per use. It now validates effective alternative distinctness for flat roles and through resolved altitude roles after attaching provenance.

_step_up_row_origins records the alternative envelope and each authored field/feature with exact file/key/provider/model/rank. A changed alternative provider does not inherit the base model binding. _with_role_origins installs the envelope’s exact source/key into RoleStepUp for both flat and altitude rows.

_refuse_repository_role_authority now rejects any stepUp key in flat or altitude repository role rows, alongside mode/notes and permission-bearing features. Optional alternatives are user-owned; a repository cannot silently author their permission or model-switch policy.

Current settings retain shape-only dynamic catalog launch choices, active/unused vocabulary reporting, global-only gateDelegation, known-family null refusal, independent speed-feature/tier validation and canonical role alias handling. Legacy harness execution fields, role launchArgs/sessionCommands/promptKeywords and expectation/supervisor/notifier families are accepted-unused, not a second runner or active sweep configuration.

Absent input retains the typed defaults: all-human gate policy, maxRounds=5, reviewer reuse delta-verify, high/medium complexity thresholds, leaf/master/portfolio postures scored/seam-required/strategist, uncapped concurrency, no spawn preference and no role overrides. Global-only gateDelegation is read by the separate boot-snapshot consumer; the per-use loader does not make that consumer dynamically reload. These defaults are independent of a configured alternative’s default afterTries=3.

## Evidence


- Per-use layering validates role features and effective alternative distinctness. [2]

- Exact envelope source/key survives typed projection. [3]
- Field origins bind provider/model and authored alternative path. [4]

- Repository alternatives are refused, including altitude rows. [5]

- Test source names user-only refusal and repository file. [6]

- Removed execution families/fields remain accepted-unused vocabulary. [7]

- Loop defaults remain separate from step-up thresholds. [8]


- Typed settings retain their independent defaults. [9]



- Only effective IDs and accepted-unused execution keys remain. [10]


- Merged parsing assembles settings and checks spawn IDs, not executable registry completeness. [11]


### Docs References

Historical schema-reference account, not current supervisor authority: the former defaults/floors are retained only as the earlier card’s reference custody.

> **Historical pre-current-loader account — retained, not an operative parser/consumer promise:**

### Repo-Internal References

### Cross-Repo References

No meaningful cross-repo references found.

The loader rereads the user settings file selected by the location guard (XDG_CONFIG_HOME or the user configuration home) and the optional repository-local file. Reading this implementation is not reading those settings files.

## 260712-TRH-L4 Final Candidate

Historical cross-module task observation: the old L4 turn described the spawned-unbriefed → harness-ready → briefed flow and catalog-writer serialization. Those are not this settings loader's operative responsibilities or current proof. This file assembles validated typed settings; dispatch evidence and catalog publication belong to their own modules.
