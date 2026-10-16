# mcp/src/agents_remember/kernel/_agentic_settings_sections.py

## Governing Overview

[MCP package overview](../../../overview.md)

## Purpose

``orchestration`` section parsers for loops, roles, concurrency, harness IDs, spawn and the quality gate. Expectations, supervisor and agent-notifier sections have no parser or typed execution consumer in this module.

Also parses landing: default 900; positive integers only and unknown keys refuse.

Parses role/default and other agentic settings sections.

## Code Commentary

`_parse_harnesses` returns the built-in ID prefix followed by settings-added IDs. Entries must remain objects with known legacy execution keys, but those fields are not read or validated as execution choices. `_parse_roles` likewise admits unused legacy launch/session keys without placing them in `RoleKnobs`. The host catalog validates actual launch choices later; neither retained vocabulary nor ignored input is a native adapter fallback.

L23 parsed `qualityGate.executor` as exactly `local` or `dagger` and refused any other value. CCR-R22@v1 (L22, commit `685f83c44055`) removed the executor key from the quality gate parser entirely: `_parse_quality_gate` now rejects any `executor` key as an unknown key (fail loud via the shared machinery) and returns `QualityGateSettings(memory_cap_bytes=...)` only -- executor identity belongs to the repository certification profile.

- `_parse_loops`
- `_parse_loop_defaults`
- `_parse_loop_complexity`
- `_parse_loop_levels`
- `_parse_roles`
- `_parse_roles_per_level`
- `_parse_feature_values`
- `_optional_role_text`
- `_parse_concurrency`
- `_parse_harnesses`
- `_parse_service_tier`
- `_resolve_role_keys`
- `_parse_spawn`
- `_parse_quality_gate` (260731-EFA-L17/L24: `orchestration.qualityGate`,
  absent/empty means adapter-runtime-managed, fail-loud unknown keys, positive-int
  `memoryCapBytes` when present; CCR-R22 removed the `executor` key)

### Role Runtime and Scope

_parse_service_tier accepts only a nonempty string when serviceTier is present; Boolean fast flags or blank/wrong-shaped values refuse. _parse_roles places it in RoleKnobs for normal and per-altitude settings. Actual provider feature capability is validated at native launch, not guessed during config parsing. `_parse_roles` now also reads optional `mode`/`notes` text and a `featureValues` map of booleans or nonempty option ids into RoleKnobs, and harness ids are shape-checked free strings while catalog validation stays at launch; the `harness_ids` parameter is gone from `_parse_roles`/`_parse_roles_per_level`.

## 260731-EFA-L17/L24 Quality-Gate Parser

`_parse_quality_gate` parses `orchestration.qualityGate` into
`QualityGateSettings`: an absent family/key keeps `memory_cap_bytes=None`, unknown keys
fail loud via `_refuse_unknown(block, KNOWN_QUALITY_GATE_FIELDS, ...)`, and
`memoryCapBytes` must be a positive integer (`_require_positive_int`). Since CCR-R22 the
former `executor` key is no longer a known field: any value under it is rejected as an
unknown key (the old permissive `dagger`-only acceptance branch was deleted). A `null` at the
family key is refused by `_refuse_null_families` before this parser runs.

## Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/agents_remember/kernel/_agentic_settings_sections.py`.

## Current Contract — Scoped Launch And Settings Changes

_parse_roles delegates ordinary choice parsing to _role_choices and attaches optional _parse_step_up through dataclasses.replace. Existing flat/per-altitude parsing and per-file role-alias conflict checks remain unchanged.

_parse_step_up admits only ordinary KNOWN_ROLE_LAUNCH_FIELDS plus afterTries. afterTries must be a positive whole integer and is allowed only for Worker/Curator, defaulting to three there and None elsewhere. Unknown keys, nested stepUp, null/wrong shapes and conflicting normalized tier aliases refuse with exact owner/source.

Choice shape remains nonempty harness/model/effort strings, optional mode/notes text and boolean/nonempty-option feature values. Host capability validation and effective no-op checks remain later boundaries; repository stepUp authority is refused by the loader, not silently honored by this parser.

Loop budgets, quality memoryCapBytes-only parser, landing timeout and accepted-unused legacy execution keys retain their existing distinct contracts.

## Evidence

- Existing role parsing attaches one typed alternative. [4]
- Ordinary shape parsing is shared without adding a new execution adapter. [5]
- Counted-role-only threshold defaults to three and refuses nested/unknown fields. [6]
- Test source names exact author file/key for invalid alternatives. [7]
- Boolean, zero and fractional thresholds refuse through the shared validator. [8]

### Repo-Internal References

The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module.

### Runtime Source References

- Frozen implementation of _parse_service_tier supporting the stated file behavior. [1]

## L23 Final Candidate Disposition

The quality section parses only optional `memoryCapBytes`; every `executor` key is refused as unknown. Executor identity is profile-owned, not a parser-selected adapter.

## R39 Dagger-Only Settings Refusal

The parser accepts no executor key, including a Dagger-valued key. The optional positive cap is resource-policy data; adapter execution policy is owned outside this parser.

## CCR-L42 current candidate

`_parse_loop_defaults` accepts every positive whole-number `maxRounds` and uses `DEFAULT_LOOP_MAX_ROUNDS` when absent. It no longer checks a hard ceiling. Zero, negative numbers, fractions and booleans still fail through `_require_positive_int` with the settings field; reviewer reuse and complexity parsing are unchanged.

## Investigator scope and request identity

The one earlier role key and canonical Investigator key are compared within each settings file before layering. Equal effective values normalize once; conflicting values refuse with the shared role-alias notice rather than choosing a winner. Stored settings files are not rewritten and no additional aliases are admitted.


- The current source implements this file’s stated Investigator boundary. [3]


## Refreshed current evidence

- Frozen implementation of _parse_roles supporting the stated file behavior. [2]
