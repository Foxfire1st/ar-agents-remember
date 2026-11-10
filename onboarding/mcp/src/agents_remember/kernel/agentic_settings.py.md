# mcp/src/agents_remember/kernel/agentic_settings.py

## Governing Overview

[overview](../../../overview.md)

## Purpose

The loader still rereads the guarded user file plus optional repository layer and assembles frozen agentic settings. Its current execution registry is an ID vocabulary, not a harness-definition table or free-form escape hatch.

## Code Commentary

`_parse_orchestration` parses `roleMessageLimit` through the shared positive-integer validator with the field/source named in failures, and defaults an absent/null value to `DEFAULT_ROLE_MESSAGE_LIMIT`. The facade exports that constant. Dynamic role-message enforcement is a separate consumer: the delivered wake text is bounded, while body and attachment payload files are not.

### Dynamic Native Launch Authority

Current role model/effort strings are shape-checked here and catalog-validated at native launch. Legacy harness execution fields remain accepted-unused; this loader builds no executable registry mappings or paste commands.

### Optional Quality-Gate Memory Cap

The loader parses `orchestration.qualityGate.memoryCapBytes`:
`KNOWN_ORCHESTRATION_FIELDS` (core) includes `qualityGate`, `_parse_orchestration`
wires `_parse_quality_gate(raw.get("qualityGate"), source=source)` into
`AgenticSettings.quality_gate`, and the facade re-exports `QualityGateSettings`,
`KNOWN_QUALITY_GATE_FIELDS` and
`_parse_quality_gate` through `__all__`. The value is the settings-owned
optional hard cap for full-wrapper runs at the master integration gate; an absent key
keeps RAM and swap host-managed, unknown keys fail loud like every other orchestration
family, and a JSON `null` at the family key is refused.


## Logic

Current _parse_harnesses admits known legacy entry keys as unread execution data and now returns two parts: the effective IDs and the harness-level `extraArgs` entries, which are attached to the settings beside them. It does not enforce effortFlagValues or an execution-command mapping.

Supervisor/redelivery knobs are accepted-unused, and there is no _merged_harness execution-policy owner in this module.

The loader REFUSES `gateDelegation` in the repo-local layer — a local value would validate and then silently do nothing (the boot snapshot reads the global file only), a fail-open shape; the refusal names the local file and states "global-layer only".

`load_agentic_settings(coordination_root, repo_root=None)` rereads both layers per use. Each file is shape/key-validated first; recursive object merge retains siblings while scalar/array values replace local-over-user. Merged parsing validates the spawn harness against effective IDs, not command/argv completeness. Role harness/model/effort remain shape-checked free strings until host catalog validation at launch. Sources retain global-first file order.

The fail-loud rule is scoped to `orchestration.*`. The orchestration allowlist also includes landing; facade exports its model/default/key set/parser and assembles it per use. `_refuse_unknown` names the offending keys, allowed set and source file.

The allowlist and assembly contain no `orchestration.escalation`, `EscalationSettings` or
`_parse_escalation` route; an authored `orchestration.escalation` key is refused as unknown.

Expectation/supervisor/agentNotifier families are reported accepted-unused. No AgentNotifierSettings, sweep cadence, SLA or redelivery floor is assembled by this loader.

Expectation-family configuration is accepted-unused; it does not populate typed SLA fields. Top-level non-orchestration families remain tolerated by the orchestration loader.

`parse_gate_delegation(raw, source=...)`, defined in the `_agentic_settings_policy` sibling and
re-exported here, is the gateDelegation parser (named policy via `named_gate_policy`, per-kind
rule overrides via `_parse_gate_policy_rule`, `requireReviewerVerdictAtSeams` binding via
`apply_seam_verdict_requirement`); it raises `AgenticSettingsError` with the source
appended and is shared by this loader and `kernel/primitives/runtime_config.py`'s legacy
authority-file gateDelegation fallback. `AgenticSettings.gate_delegation_configured` records
whether a FILE set the key (vs. the default) — the boot-snapshot consumer branches on it.

Current flat and altitude role rows carry harness/model/effort/tier/mode/features/notes/origins and optional user-owned stepUp. Legacy launchArgs/promptKeywords/sessionCommands are accepted-unused and not validated as executable string lists. The normal field/feature/origin merge and exact user-only mode/notes/stepUp authority still apply. `_attach_role_origins` binds each authored value to its file, key, provider and model without changing the merge, and skips rows keyed by a removed role name.

The current closed role vocabulary for flat `orchestration.roles` and per-level
`orchestration.rolesPerLevel` is `architect`, `orchestrator`, `manager`,
`worker`, `curator`, `reviewer`, `investigator` and `bootstrap`. The removed role names `designer`
and `strategist` (`UNUSED_ROLES`) are admitted as inert keys: parsing, origin attachment and the
repository-authority refusal skip them, and `unused_keys` reports them. Other unknown roles remain fail-loud.
`system-specialist` is the accepted compatibility spelling normalized to `investigator`, not an additional
canonical role.

- Origin attachment skips removed role rows in flat and per-level tables [12]
- The repository-authority refusal skips removed role rows [13]


Current _parse_harnesses returns built-in IDs plus settings-added IDs together with each harness's `extraArgs` entries, and validates the entry and key shape while parsing each harness's `extraArgs` records, which the loader stores as `harness_extra_args`; a role's own `extraArgs` is checked against its named harness and its capability before it is kept, so the return is the IDs, the entries and those records, not the IDs alone. Command/argv/effort vehicle fields are accepted-unused; no _HarnessEntry, _merged_harness or effort-session-template consumer is constructed here.

### Conventions

Kernel-level loader and typed models are used by launch defaults and other callers; this file imports kernel.harnesses.HARNESS_IDS rather than serving execution adapter objects. AgentsRememberError remains the common typed error family.

### Invariants And Boundaries

- Read PER-USE, never boot-cached — the ONE boot-snapshot consumer is
  `kernel/primitives/runtime_config.py`'s gateDelegation (documented restart-required semantics).
- Fail-loud is `orchestration.*`-scoped; top-level families are tolerated
  (reserved: contextProviders returns here in a follow-up).
- A `null` at a known family key is REFUSED (either layer) — never a silent
  wipe, never a reset-to-default; remove the key to inherit the global value.
Legacy effortSessionCommand is accepted-unused; no template execution or post-merge template validator belongs to the current loader.
- Doctrine floors are not knobs: no key touches the master-exit seam gate (restated in the
  module docstring).
- Arrays REPLACE on merge, never concatenate; sibling leaves survive an override.
Legacy free-form role fields are accepted-unused.
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

Absent input retains the typed defaults: all-human gate policy, maxRounds=5, reviewer reuse delta-verify, high/medium complexity thresholds, leaf/master postures scored/seam-required (no default portfolio posture; an authored portfolio `strategist` posture is dropped and reported unused), uncapped concurrency, no spawn preference and no role overrides. Global-only gateDelegation is read by the separate boot-snapshot consumer; the per-use loader does not make that consumer dynamically reload. These defaults are independent of a configured alternative’s default afterTries=3.

## Evidence


- Per-use layering validates role features and effective alternative distinctness. [2]

- Exact envelope source/key survives typed projection. [3]
- Field origins bind provider/model and authored alternative path. [4]

- Repository alternatives are refused, including altitude rows; rows keyed by a removed role name are skipped. [5]

- Test source names user-only refusal and repository file. [6]

- Removed execution families/fields remain accepted-unused vocabulary. [7]

- Loop defaults remain separate from step-up thresholds. [8]


- Typed settings retain their independent defaults. [9]


- Only effective IDs and accepted-unused execution keys remain. [10]


- Merged parsing assembles settings and checks spawn IDs, not executable registry completeness. [11]


### Docs References

`docs/reference/settings-json.md` is the schema reference the module docstring names.

### Repo-Internal References

### Cross-Repo References

No meaningful cross-repo references found.

The loader rereads the user settings file selected by the location guard (XDG_CONFIG_HOME or the user configuration home) and the optional repository-local file. Reading this implementation is not reading those settings files.
