# mcp/src/agents_remember/application/role_capsules/wire_budget.py

## Governing Overview

[application overview](../overview.md)

## Purpose

Defines the non-ratcheting final Turn-1 wire-token ceilings (`WIRE_TOKEN_CEILINGS`) and 34-key compiled-capsule token ceilings (`COMPILED_CAPSULE_TOKEN_CEILINGS`) alongside offline `o200k_base` plain-text and compact-bound compiled-capsule measurement and ceiling-evaluation helpers.

## Code Commentary

`WIRE_TOKEN_CEILINGS` is an immutable `MappingProxyType` holding the eight default `(role, operation)` fresh base prompt ceilings (`investigator/orientation: 2_500`, `bootstrap/bootstrap: 2_500`, `worker/implementation: 2_500`, `reviewer/review: 3_000`, `curator/curation: 3_000`, `orchestrator/coordination: 3_800`, `manager/coordination: 3_800`, `architect/planning: 3_800`). `COMPILED_CAPSULE_TOKEN_CEILINGS` is an immutable `MappingProxyType` covering all 34 matrix keys (`worker/*`, `investigator/*`, `bootstrap/*`, `launcher/*`: `1_500`; `reviewer/*`, `curator/*`: `2_000`; `architect/*`, `orchestrator/*`, `manager/*`: `2_600`). Phase 1 appendix allowance constants were removed; caller-supplied held-message payloads and launch appendices are bounded by the 1,000-character offload rule rather than capsule token ceilings.

`measure_wire_tokens(message, *, replacements=())` applies ordered `(old, new)` replacements (skipping empty `old` strings) and counts tokens using the cached vendored `o200k_base` vocabulary (`models/tokens.py::vendored_vocabulary_cache`) with `disallowed_special=()` so special-token literals in prompt text do not raise.

`evaluate_wire_token_ceilings(measurements, ceilings=WIRE_TOKEN_CEILINGS)` returns human-readable failure strings naming the pair key, measured total, and ceiling whenever a key has no configured ceiling or `tokens > ceiling`. Exact equality passes and ceilings never ratchet automatically.

`measure_compiled_capsule_tokens(result, *, corpus_root, every_role=None)` counts `o200k_base` tokens of the role-filtered `core/every-role.md` shared block plus compiled instructions after compact `skill/` and `detail/` Markdown link binding (skipping fenced and inline code spans via `_mask_code`).

## Relationships

- Depends on `tiktoken`, `agents_remember.application.role_capsules.shared_block` (`filter_shared_block`), `agents_remember.models.role_capsules.types` (`CapsuleCompilationResult`, `CapsuleRoleSeat`), and `agents_remember.models.tokens` (`VENDORED_ENCODING_NAME`, `vendored_vocabulary_cache`).
- Consumed by `mcp/tests/test_role_wire_token_budgets.py`, `scripts/instruction_renewal/budgets.py`, and `mcp/tests/test_role_capsule_budgets_d694.py` to gate assembled Turn-1 `agent-create` prompt tokens and all 34 compiled capsule matrix keys separately from tool schemas and system prompts.

## Evidence

- `WIRE_TOKEN_CEILINGS` exports immutable Turn-1 ceilings for all eight default launch pairs (2,500 / 3,000 / 3,800) beside 34-key `COMPILED_CAPSULE_TOKEN_CEILINGS` (1,500 / 2,000 / 2,600). [1]

- `measure_wire_tokens` loads the vendored offline `o200k_base` encoding, applies ordered normalizations, and tokenizes plain text with `disallowed_special=()`. [2]

- `evaluate_wire_token_ceilings` defaults to `WIRE_TOKEN_CEILINGS` and reports unconfigured keys and strictly over-ceiling totals without ratcheting. [3]
- `measure_compiled_capsule_tokens` counts `o200k_base` tokens of the compact-bound role-filtered shared block plus compiled instructions. [4]
