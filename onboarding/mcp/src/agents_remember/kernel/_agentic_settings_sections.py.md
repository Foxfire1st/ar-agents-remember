# mcp/src/agents_remember/kernel/_agentic_settings_sections.py

## Governing Overview

[MCP package overview](../../../overview.md)

## Purpose

``orchestration`` section parsers: loops, roles, concurrency, expectations, supervisor,
escalation, spawn, and the quality gate (260731-EFA-L17).

Parses role/default and other agentic settings sections.

## Code Commentary

`_parse_expectations` preserves omitted SLA defaults and overrides only explicitly named kinds. Unknown block fields/kinds, booleans, nonnumbers and nonpositive seconds refuse. This preserves configuration meaning documented by the retired expectation test card without claiming that test remains active. Source: mcp/src/agents_remember/kernel/_agentic_settings_sections.py:260-285.

L23 parsed `qualityGate.executor` as exactly `local` or `dagger` and refused any other value. CCR-R22@v1 (L22, commit `685f83c44055`) removed the executor key from the quality gate parser entirely: `_parse_quality_gate` now rejects any `executor` key as an unknown key (fail loud via the shared machinery) and returns `QualityGateSettings(memory_cap_bytes=...)` only -- executor identity belongs to the repository certification profile.

- `_parse_loops`
- `_parse_loop_defaults`
- `_parse_loop_complexity`
- `_parse_loop_levels`
- `_parse_roles`
- `_parse_roles_per_level`
- `_parse_concurrency`
- `_parse_expectations`
- `_parse_supervisor`
- `_require_supervisor_floor_seconds`
- `_parse_escalation`
- `_parse_escalation_sla_seconds`
- `_parse_escalation_rung_seconds`
- `_parse_respawn_after_rung`
- `_parse_spawn`
- `_parse_quality_gate` (260731-EFA-L17/L24: `orchestration.qualityGate`,
  absent/empty means adapter-runtime-managed, fail-loud unknown keys, positive-int
  `memoryCapBytes` when present; CCR-R22 removed the `executor` key)

### Role Runtime and Scope

_parse_service_tier accepts only a nonempty string when serviceTier is present; Boolean fast flags or blank/wrong-shaped values refuse. _parse_roles places it in RoleKnobs for normal and per-altitude settings. Actual provider feature capability is validated at native launch, not guessed during config parsing.

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

## Evidence

### Repo-Internal References

The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module.

### Runtime Source References

- Frozen implementation of _parse_service_tier supporting the stated file behavior. [1]
- Frozen implementation of _parse_roles supporting the stated file behavior. [2]

## L23 Final Candidate Disposition

The orchestration quality section projects Dagger-only executor policy through strict settings
models. Unknown or legacy executor values fail validation instead of activating compatibility code.

## R39 Dagger-Only Settings Refusal

The parser accepts only the Dagger executor and describes every other value as forbidden host test
execution, not a lower-authority diagnostic option. The optional cap is a container resource
policy.

## CCR-L42 current candidate

Loop-default parsing now rejects `maxRounds` above `MAX_REVIEW_ROUNDS` with a typed settings error; positive values at or below the hard review limit retain the existing parsing contract.
