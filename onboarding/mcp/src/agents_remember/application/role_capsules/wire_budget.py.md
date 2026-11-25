# mcp/src/agents_remember/application/role_capsules/wire_budget.py

## Governing Overview

[application overview](../overview.md)

## Purpose

Defines the non-ratcheting Phase 1 Turn-1 wire-token ceilings and explicit appendix allowances alongside offline `o200k_base` plain-text measurement and ceiling-evaluation helpers.

## Code Commentary

`PHASE_1_WIRE_TOKEN_CEILINGS` is an immutable `MappingProxyType` holding the eight default `(role, operation)` fresh base prompt ceilings (`investigator/orientation: 6_600`, `bootstrap/bootstrap: 7_300`, `worker/implementation: 10_200`, `orchestrator/coordination: 10_400`, `architect/planning: 11_100`, `reviewer/review: 11_200`, `curator/curation: 11_600`, `manager/coordination: 11_800`). Two explicit Phase 1 appendix constants extend base ceilings for ordinary-Latin appendix fixtures without mutating base ceilings: `PHASE_1_HELD_APPENDIX_ALLOWANCE = 600` (for opened held leaf prompts carrying `product_start_message` plus Rule 5 bounded batches) and `PHASE_1_LAUNCH_APPENDIX_ALLOWANCE = 900` (for direct launches carrying successor, step-up, ACP, and bounded direct `opening_message` appendices).

`measure_wire_tokens(message, *, replacements=())` applies ordered `(old, new)` replacements (skipping empty `old` strings) and counts tokens using the cached vendored `o200k_base` vocabulary (`models/tokens.py::vendored_vocabulary_cache`) with `disallowed_special=()` so special-token literals in prompt text do not raise.

`evaluate_wire_token_ceilings(measurements, ceilings=PHASE_1_WIRE_TOKEN_CEILINGS)` returns human-readable failure strings naming the pair key, measured total, and ceiling whenever a key has no configured ceiling or `tokens > ceiling`. Exact equality passes and ceilings never ratchet automatically.

## Relationships

- Depends on `tiktoken` and `agents_remember.models.tokens` (`VENDORED_ENCODING_NAME`, `vendored_vocabulary_cache`).
- Consumed by `mcp/tests/test_role_wire_token_budgets.py`, which gates assembled Turn-1 `agent-create` prompt tokens separately from tool schemas, system prompts, and the whitespace-word registry in `skills/l-01-agent-lifecycles/capsule-budgets.json`.

## Evidence

- `PHASE_1_WIRE_TOKEN_CEILINGS` exports immutable Phase 1 base ceilings for all eight default launch pairs beside `PHASE_1_HELD_APPENDIX_ALLOWANCE` (600) and `PHASE_1_LAUNCH_APPENDIX_ALLOWANCE` (900). [1]
- `measure_wire_tokens` loads the vendored offline `o200k_base` encoding, applies ordered normalizations, and tokenizes plain text with `disallowed_special=()`. [2]
- `evaluate_wire_token_ceilings` reports unconfigured keys and strictly over-ceiling totals without ratcheting. [3]
