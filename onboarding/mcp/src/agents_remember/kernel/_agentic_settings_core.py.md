# mcp/src/agents_remember/kernel/_agentic_settings_core.py

## Governing Overview

[MCP package overview](../../../overview.md)

## Purpose

Typed agentic settings models, constants, and validation primitives. The settings family (``orchestration.*``) is merged from a global and an optional repo-local settings file. This module owns the typed models, the fail-loud key vocabularies, the shared shape/type validators, and the seeded defaults; the parsers live in responsibility-split siblings and the loader in :mod:`agents_remember.kern...

Defines typed role knobs and inherited agentic settings defaults. MIK-R113 removes expectation and notifier models: their old family keys, harness execution fields and role launch/session fields are accepted but not read or checked, and `unused_orchestration_keys` reports their dotted names. `AgenticSettings` carries effective harness IDs, not native adapter objects; settings compatibility never restores a launch implementation. Unknown keys outside the declared active-or-unused vocabularies still fail loud.

Defines role defaults and LandingSettings.commit_check_timeout_seconds=900 with the sole commitCheckTimeoutSeconds key.

## Code Commentary

`KNOWN_ORCHESTRATION_FIELDS` admits `roleMessageLimit`, and `AgenticSettings.role_message_limit` uses the shared `DEFAULT_ROLE_MESSAGE_LIMIT` of 1000. This bound counts role-message wake text, not sender/file pointer lines or full-file payloads. The core owns the typed setting/default; the loader validates it and the message facade reads the effective limit per call.

L23 had added the closed `QualityExecutor` choice defaulting `orchestration.qualityGate.executor` to `local`. CCR-R22@v1 (L22, commit `685f83c44055`) removed the executor field entirely: `QualityExecutor` is deleted, `KNOWN_QUALITY_GATE_FIELDS` now contains only `memoryCapBytes`, and `QualityGateSettings` carries only `memory_cap_bytes` -- executor identity belongs to the repository certification profile, not to agentic settings.

- `AgenticSettingsError`
- `LoopComplexity`
- `LoopDefaults`
- `LoopSettings`
- `RoleKnobs`
- `ConcurrencySettings`
- `QualityGateSettings` (260731-EFA-L17/L24: optional `orchestration.qualityGate.memoryCapBytes`; absent means host-managed RAM and swap; CCR-R22 removed the `executor` field -- the profile owns the adapter)
- `AgenticSettings`
- `agentic_settings_path`
- `default_agentic_settings_seed`
- `default_agentic_settings_seed_text`
- `merge_settings`
- `_refuse_unknown`
- `_require_object`
- `_require_string`
- `_require_positive_int`
- `_require_harness_id`

### Role Runtime and Scope

RoleKnobs now carries optional service_tier. resolved_role_knobs merges tier independently of harness/model/effort, so a lower-level model or effort does not erase a role/altitude tier. Legacy role launch/session fields remain accepted-unused; the independent tier/default facts here are not execution-argument authority. RoleKnobs now also carries `mode`, `feature_values` and `notes` with per-choice `origins`: `NON_PERMISSION_FEATURES` (`service_tier`, `fast_mode`) marks speed authority while unknown features carry permission authority until classified, `native_service_tier` normalizes user `fast` to `priority`, and `role_feature_values` compares the tier alias against `featureValues.service_tier` after merging. `agentic_settings_path` names the repository-local file only; `user_agentic_settings_path` and `require_user_agentic_settings_path` resolve and guard the single user file.

## 260731-EFA-L17/L24 Quality-Gate Settings

The module owns the `orchestration.qualityGate` family:
`KNOWN_QUALITY_GATE_FIELDS` contains only `memoryCapBytes` (the `executor` key was removed by
CCR-R22); the frozen `QualityGateSettings` model uses `None` for the adapter-runtime-managed
default; and the generated settings seed deliberately omits the family. An explicit positive
integer remains available for a constrained full-gate run. Unknown keys fail loud through
the shared `_refuse_unknown` machinery exactly like every other orchestration
family.

## Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/agents_remember/kernel/_agentic_settings_core.py`.

## Current Contract — Scoped Launch And Settings Changes

KNOWN_ROLE_LAUNCH_FIELDS isolates the ordinary launch fields; KNOWN_ROLE_KNOB_FIELDS adds stepUp only at the outer role row. RoleKnobs carries optional RoleStepUp(choices, after_tries, source, key); nesting is a parser refusal, not another escalation ladder.

require_distinct_step_up rejects an effective no-op alternative after role/spawn scope and serviceTier fast/priority alias normalization. It compares stated ordinary fields, effective features and tier; it does not validate the host’s offered model/mode/features.

resolved_role_knobs preserves normal flat/per-level field and feature/origin merges and inherits/replaces step_up as an alternative object. It validates distinctness both without an altitude override and after effective merging, so an altitude may not turn an inherited alternative into the role’s own choices.

Only completed failing code review rounds count for Worker; only completed failing memory review rounds count for Curator. Record-only checks of the unchanged candidate do not add a try; no legacy mixed-code row is reinterpreted as a Curator round. The optional user alternative defaults to afterTries=3 for these roles, not to extra review authority.

Existing review maxRounds, roleMessageLimit, landing timeout, optional profile-owned quality memory cap, user-settings location guard and active-versus-unused key vocabulary remain independent.

## Evidence

- Separate ordinary launch vocabulary from outer stepUp. [3]
- Typed alternative has choices, count and provenance. [4]
- No-op validation normalizes native tier aliases. [5]
- Effective flat/altitude merge rechecks distinctness. [6]
- Test source checks no-op alternatives caused by altitude or alias equality. [7]
- Three is the counted-role threshold default, not a new review budget. [8]
- Worker and Curator read independent persisted lanes. [9]
- Only recorded rounds ending with findings in the role’s kind count. [10]

### Repo-Internal References

The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module.

### Runtime Source References

- Frozen implementation of RoleKnobs supporting the stated file behavior. [1]
- Frozen implementation of AgenticSettings supporting the stated file behavior. [2]

## L23 Final Candidate Disposition

Quality settings no longer carry an executor field at all (CCR-R22): the one adopted acceptance
adapter comes from the repository's certification profile. Optional resource policy configures the
graph; agentic settings cannot select or constrain a second runner.

## R39 Dagger Resource Ownership

Executor identity belongs to the repository certification profile, not to these agentic settings. This module declares an optional positive memory cap; its omitted value is runtime-managed. The adapter runtime and fallback policy are owned outside this module.

## CCR-L42 current candidate

The review budget uses the settings number `orchestration.loops.defaults.maxRounds`. `MAX_REVIEW_ROUNDS` is removed; `DEFAULT_LOOP_MAX_ROUNDS` is the fallback used by `LoopDefaults` and the reference seed when no number is named. Any positive whole number is accepted by the parser. The settings/transition owners, not role prose, determine the number in force.

- `CAPABILITY_IDS` names the non-seat capabilities that carry a launch block (`review-presenter`): their choices live under `orchestration.roles.<capability>` with the same per-field provenance and refusal rules as a seat, while the capsule, dispatch and level tables stay seat-only. \[11] [11]
