# mcp/src/agents_remember/kernel/agentic_settings.py

## Governing Overview

[MCP package overview](../../../overview.md)

## Purpose

`agentic_settings.py` is the two-layer AGENTIC settings loader (260703-L13): it reads the
GLOBAL `<coordination_root>/system/settings.json` plus an optional repo-local
`<code_repo>/system/settings.json`, merges them, and parses the top-level `orchestration`
family — gate delegation, the three-party-loop knobs, per-role knob overrides (flat `roles` +
per-level `rolesPerLevel`, incl. the free-form escape hatch), concurrency caps, the spawn harness
preference, and the harness-definition table `orchestration.harnesses` (260703-L16) — into frozen
typed models. It is the single parser
for the agentic family; the MCP authority file, memory-topology settings, and provider
lifecycle settings are separate families with separate parsers. **260707-HFX2-L2 (R1/R5)** adds the
`orchestration.supervisor` family — the deterministic sweep loop's own knobs (enabled, interval
seconds, self-liveness staleness cutoff, inbox-redelivery rate limit, and since HFX2-L8 a
conservative per-sweep redelivery budget). HFX2-L9 makes the supervisor cadence knobs explicitly
production-safe: `redeliverRateLimitSeconds` and the new `signalCooldownSeconds` both refuse values
below the shared 900-second floor.

## Code Commentary

### 260714-ACPUI-L2 Dynamic Native Launch Authority

`RoleKnobs.model` and `RoleKnobs.effort` remain stripped, non-empty settings values at this parser
boundary. For the built-in Claude, Codex, and Pi protocol harnesses, this module deliberately does
not impose a static model or effort vocabulary: dispatch carries the complete settings selection
into the typed native launch boundary, where the adapter validates it against a token-free,
per-install catalog and the selected model's own effort options. Settings-defined non-native
harnesses retain their explicit registry mappings and dispatch-time validation. The free-form
`launchArgs`, `sessionCommands`, and `promptKeywords` fields remain independently user-authored;
the parser never derives a model/effort paste command from them.

### 260707-HFX2-L12 CS-6 Update

`orchestration.supervisor.escalationBudget` is now a known supervisor setting with default 250 and positive-int parsing. The serving supervisor context reads it per-use beside `redeliverBudget` to bound escalation-rung emissions per sweep.

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

## Logic

**260714-ACPUI-L2 effort policy.** When a settings-defined non-native harness declares
`effortFlagValues`, the effective merged harness uses enumerated validation so its explicit menu is
not bypassed. Built-in Claude, Codex, and Pi rows carry no static effort mapping; a partial command
or argv override does not invent one. Their model-gated validation belongs to dynamic adapter
discovery at launch.

**260707-HFX2-L15 dispatch bounds and harness overrides.** The default supervisor redelivery budget
is `1`, matching the synchronous calibrated log-verification envelope of one input. When settings
introduce or replace a Codex `effortFlag`, `_merged_harness` keeps any retired native config-value
template cleared so the explicit custom mapping receives an ordinary discrete value.

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
concurrency/spawn/harnesses/expectations/supervisor/**escalation** (260707-HFX2-L4, R1), plus per-family sets for
gateDelegation kinds, loop defaults/complexity/levels, the eight l-01 role names, the role-knob
fields harness/model/effort/launchArgs/promptKeywords/sessionCommands, the harness-entry fields,
concurrency caps, and the four expectation-row kinds) and `_refuse_unknown` raises
`AgenticSettingsError` naming the unknown keys, the allowed set, and the offending file.

**260707-HFX2-L4 (R1, escalation ladder knobs)**: `orchestration.escalation` configures P-15 tier
3's ladder — `EscalationSettings` (`sla_seconds` per `message_kind`, defaulting from
`DEFAULT_ESCALATION_SLA_SECONDS`; `rung_seconds` keyed 1/2/3, defaulting from
`DEFAULT_ESCALATION_RUNG_SECONDS`; `nudge_rate_limit_seconds` default 900; `respawn_after_rung`
default 2). `_parse_escalation` is now a three-call assembly over one parser per sub-block
(260731-EFA-L2): `_parse_escalation_sla_seconds(raw, *, source)`,
`_parse_escalation_rung_seconds(raw, *, source)` and `_parse_respawn_after_rung(block, *, source)`,
each returning the defaults when its key is absent. **Call order is the refusal order** — a
settings file with more than one bad field is still reported against the first one, exactly as
before the split; do not reorder those calls. The validation itself is unchanged:
`slaSeconds` keys are checked against `KNOWN_ESCALATION_MESSAGE_KINDS`
(a literal set duplicated by hand against `InboxMessageKind`, the same kernel<->controlplane
cycle-avoidance reason `KNOWN_EXPECTATION_KINDS` already uses), `rungSeconds` keys against the
closed `KNOWN_ESCALATION_RUNGS = (1, 2, 3)`, and `respawnAfterRung` against that same closed set (a
respawn cannot trigger at a rung that doesn't exist); every value must be a positive number/int,
and the whole block is checked against `KNOWN_ESCALATION_FIELDS` for unknown top-level keys. Absent
block or absent key falls back to the documented default (`EscalationSettings()`'s field
defaults) — `sla_for(kind)`/`rung_dwell(rung)` are the accessor methods `serving/supervisor.py`'s
`_agent_notifier_context()` reads per-use, mirroring how `SupervisorSettings`/`ExpectationSettings`
are consumed elsewhere in this file.

**260707-HFX2-L2/R8/R9 (supervisor sweep knobs)**: `orchestration.supervisor` configures the
deterministic sweep loop hosted beside the serving daemon's projector/metrics loops —
`SupervisorSettings` (`enabled` default `true`, `interval_seconds` default 10.0,
`stale_cutoff_seconds` default 60.0, `redeliver_rate_limit_seconds` default `None`,
`signal_cooldown_seconds` default `DEFAULT_RATE_LIMIT_SECONDS` / 900, `redeliver_budget` default
1, and `escalation_budget` default 250). `_parse_supervisor` validates boolean/positive fields and checks
`redeliverRateLimitSeconds` plus `signalCooldownSeconds` through `_require_supervisor_floor_seconds`,
which refuses any value below `inbox_backoff.MIN_REDELIVERY_INTERVAL_SECONDS` (900). Absent block or
absent key both fall back to the documented default (`SupervisorSettings()`'s field defaults).
`redeliver_rate_limit_seconds=None` is a deliberate inherit-not-duplicate choice: the sweep passes
`None` straight through to `OperatorInboxStore.list_redeliverable`, which already owns its own
default (`inbox_backoff.DEFAULT_RATE_LIMIT_SECONDS`) — the same "`None` = uncapped/inherit"
convention `ConcurrencySettings` already uses elsewhere in this file, so the floor is never copied
as an unrelated second source of truth. `signal_cooldown_seconds` is an explicit settings value
because repeated owner-signal minting has its own cooldown store. `redeliver_budget` is parsed from
`redeliverBudget` as a positive integer and is intentionally present in the empty-block default so a
default incident deployment gets bounded sweep work without needing a new knob.

**260707-HFX2-L1 (R2, expectation-row SLAs)**: `orchestration.expectations.defaults` configures
the per-kind SLA seconds every dispatch surface's durable expectation row uses (`briefed-by`,
`turn-report-by`, `verdict-by`, `ack-by`) — `ExpectationSettings.sla_for(kind)` falls back to
`DEFAULT_EXPECTATION_SLA_SECONDS` (`ack-by` mirrors the existing `AGENT_PICKUP_TTL_SECONDS`
convention, 300s) for any kind the settings omit. `_parse_expectations` validates every key
against `KNOWN_EXPECTATION_KINDS` (fail-loud on an unknown kind or non-positive SLA). This literal
kind set is duplicated in `controlplane/expectation_rows.py::ExpectationKind` rather than imported,
to avoid a kernel<->controlplane import cycle — the two must be kept in sync by hand.
Unknown TOP-LEVEL keys are deliberately tolerated-not-parsed: the same coordinator file is
the c-08 memory-settings fallback and the earmarked future home of further families
(`contextProviders` first in line — gate amendment 2026-07-06), so the fail-loud scope must
not foreclose them. Absent files (or an absent `orchestration` key) yield the documented
defaults: all-human gate policy, the L12 loop defaults (`maxRounds` 3, `delta-verify`
reviewer reuse, complexity high/medium, perLevel scored/seam-required/strategist), no role
overrides, uncapped concurrency, no spawn preference. Malformed JSON and non-object roots
fail loud with the path. A JSON `null` at ANY known `orchestration.*` family key (either
layer) is REFUSED by `_refuse_null_families` in `_validated_orchestration_block` (260703-L18
finding 6, developer-ruled `null` = refuse): `null` reads as *absent* to every family parser
and `merge_settings` REPLACES a non-object, so `"concurrency": null` in the repo-local layer
would otherwise SILENTLY wipe the global caps — the one scalar collision that used to defeat
both the deep-merge and fail-loud invariants. The refusal names the offending file with the
guidance "remove the key to inherit the global value". Ordering: `_refuse_null_families` runs
inside `_validated_orchestration_block`, so a repo-local `gateDelegation: null` hits the null
refusal FIRST; the dedicated repo-local `gateDelegation` presence refusal in
`load_agentic_settings` still fires for any non-null value.

`parse_gate_delegation(raw, source=...)` is the gateDelegation parser MOVED here from the
former `mcp/config.py` (now `kernel/primitives/runtime_config.py`) (its logic is unchanged: named policy via `named_gate_policy`, per-kind
rule overrides via `_parse_gate_policy_rule`, `requireReviewerVerdictAtSeams` binding via
`apply_seam_verdict_requirement`); it now raises `AgenticSettingsError` with the source
appended and is shared by this loader (the key's new home) and `kernel/primitives/runtime_config.py`'s one-cycle
legacy authority-file fallback. `AgenticSettings.gate_delegation_configured` records
whether a FILE set the key (vs. the default) — the boot-snapshot consumer branches on it.

**Role knobs (L16 three-layer model, ACPUI-L2 launch boundary).** `RoleKnobs` carries the validated
`harness` id plus `model`/`effort` as free strings at this parser boundary. Built-in native values
are structurally required at role dispatch and validated against the model-gated dynamic catalog
inside the hosted runner; explicit non-native registry mappings are validated at dispatch. The
free-form escape hatch (`launchArgs`/
`promptKeywords`/`sessionCommands` — `_require_string_list` requires a non-empty LIST of non-empty
strings; an EMPTY list REFUSES (PR #100 review, Codex P2: `RoleKnobs` cannot distinguish absent from
cleared — empty tuple = not configured — so a per-level `[]` meant to clear a flat default would
silently INHERIT it through the field-wise `or` merge; omit the key to inherit, list values to
override); content is NEVER validated; the spawn path records it in provenance). `orchestration.rolesPerLevel`
(ruling 2026-07-07T08:15) parses the same knob shape per level (`_parse_roles_per_level`, level
vocabulary = `KNOWN_LOOP_LEVELS` leaf|master|portfolio, congruent with `loops.perLevel`);
`AgenticSettings.resolved_role_knobs(role, level="leaf")` deep-merges the level override over the
flat default field-wise (harness inherited unless overridden, lists REPLACE) — realizing the
dispatch chain repo-local level override > global level override > repo-local role default >
global role default on top of the file merge.

HFX-L6 adds `architect` and L6R3 adds `curator` to the closed role vocabulary for both flat
`orchestration.roles` and per-level `orchestration.rolesPerLevel`; unknown-role behavior remains
fail-loud. **260707-HFX-L7** adds `system-specialist` — the ninth `KNOWN_ROLES` member — so the
provider-degradation investigator can carry its own spawn knob overrides
(`orchestration.roles.system-specialist` / `orchestration.rolesPerLevel.<level>.system-specialist`)
the same way every other role does; the module-docstring comment naming the role count was
corrected from "eight" to "nine" in the R2 fix round (closes reviewer F6).

**Harness definitions (L16 registry openness).** `_parse_harnesses` (decomposed into
`_parse_harness_entry` → frozen `_HarnessEntry` shape record, `_resolved_launch` command/argv
derivation, `_merged_harness` replace-over-fallback merge, `_refuse_unpaired_vehicles`) parses
`orchestration.harnesses` into the EFFECTIVE registry (`AgenticSettings.harnesses`, default the
builtin `HARNESSES`): entries merge over the builtin table by id — a NEW id must resolve
`command` and/or `argv` (`command` defaults to `argv[0]`, `argv` to `(command,)`) and is tagged
`defined_in="settings"`; a builtin id overrides per field. Delivery-vehicle pairs must resolve
together post-merge (`effortFlag`+`effortFlagValues`, `effortSessionValues`+`effortSessionCommand`
— a flag without a vocabulary would reintroduce the silent-degrade risk). The
`effortSessionCommand` TEMPLATE is additionally validated post-merge by `_refuse_bad_effort_template`
(260703-L18 finding 4): it must render with `.format(value=…)` and reference no replacement field
other than `{value}` — a stray field (`/set {mode}={value}`), a positional `{}`, or an unmatched
brace refuses naming the harness. A builtin override may supply just the command, so the check lives
here beside the pairing rule; once validated, the raw `KeyError` at `serving/harnesses.py`
(`effort_session_commands`' `.format`) is unreachable from settings. Harness references
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

Kernel-level module: consumers are `kernel/primitives/runtime_config.py` (boot-snapshot gateDelegation),
`mcp/tools/terminal.py` (per-use knob/harness resolution at dispatch), `serving/app.py`
(effective registry for `GET /api/harnesses` + the dashboard open route, global layer), and
`install/runtime.py` (seed). Frozen dataclasses (`AgenticSettings`, `LoopSettings`, `LoopDefaults`,
`LoopComplexity`, `RoleKnobs`, `ConcurrencySettings`) follow the `McpRuntimeConfig` style;
`AgenticSettingsError` joins the typed `AgentsRememberError` family (a `ValueError`
subclass). The kernel→serving import is a constant-table + frozen-dataclass import only
(`HARNESSES`, `Harness` — the loader constructs effective `Harness` rows, no serving I/O).

### Invariants And Boundaries

- Read PER-USE, never boot-cached — the ONE boot-snapshot consumer is
  `kernel/primitives/runtime_config.py`'s gateDelegation (documented restart-required semantics).
- Fail-loud is `orchestration.*`-scoped; top-level families are tolerated
  (reserved: contextProviders returns here in a follow-up).
- A `null` at a known family key is REFUSED (either layer) — never a silent
  wipe, never a reset-to-default; remove the key to inherit the global value.
- `effortSessionCommand` templates are template-validated post-merge, so a bad
  template refuses at load, not at spawn (raw `str.format` crash unreachable).
- Doctrine floors are not knobs: no key touches the master-exit seam gate or the
  strategist's mandatory pre-run (L12 ruling, restated in the module docstring).
- Arrays REPLACE on merge, never concatenate; sibling leaves survive an override.
- An EMPTY free-form list is REFUSED (either layer, flat or per-level): `()` is the
  not-configured sentinel, so `[]` cannot express "cleared" and would silently inherit —
  omit the key to inherit (PR #100 review).
- `sources` records the files actually read (global first) for error/refusal messages.

### Todos

No known follow-up in this file. (The contextProviders family migration and a
dashboard settings write path are tracked outside as follow-ups.)

## Evidence

### Docs References

- The schema reference documents supervisor defaults and constraints, including redelivery budget `1`, escalation budget `250`, and the redelivery floor. [1]

### Repo-Internal References

### Cross-Repo References

No meaningful cross-repo references found.

The loader operates on coordinator/repo-local files only.

## 260712-TRH-L4 Final Candidate

This sidecar was reviewed against the final uncommitted L4 candidate. The source now participates in the explicit spawned-unbriefed → harness-ready → briefed flow; dispatch proof remains exact-session, copy-mode-aware, harness-log-confirmed, and pending without respawn when proof is absent. Catalog writers are fully serialized across one read/body/write transaction while atomic readers remain lock-free.
