# mcp/tests/test_final_gate_prefix_adapter.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_final_gate_prefix_adapter.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T01:48+02:00 |
| lastVerifiedCommitHash | `16d1a4d6d6f8e8572b4bca10b8a4a84485449604` |
| lastVerifiedCommitDate | 2026-09-04T00:55:21+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

CCR-R08 forcing suite for the Gate 1-4 prerequisite-prefix adapter contracts
(`require_green_gate_prefix`): reuse, refusal, invalidation, and memory-only repair routes.
Split from `test_final_full_memory_coherence_certification` (repository file-size hard
limit); the shared Gate-5 fixture scaffold is imported from that module. The suite is explicitly
registered in the `integration` lane of `test-evidence-lanes.toml`.

## Code Commentary

### Logic

Eight module-level tests force the adapter against the shared scaffold:

- `test_green_prefix_adapter_reuses_exact_gate_one_to_four` (40-52) - an unchanged exact
  candidate reuses the ordered green Gates 1-4 and digests the reuse plan.
- `test_green_prefix_adapter_refuses_incomplete_prefix` (55-66) - a non-(1,2,3,4) ordered
  certificate set refuses as `gate-five-prefix-incomplete`.
- `test_green_prefix_adapter_refuses_when_code_tree_mismatches_admission` (69-80) -
  `gate-five-code-candidate-mismatch` when the supplied code tree differs from the admitted
  tree.
- `test_green_prefix_adapter_restarts_at_gate_one_on_code_change` (83-95) - a code input
  change refuses `gate-five-prefix-invalidated` so the candidate restarts at Gate 1 instead
  of a memory-only repair.
- `test_green_prefix_adapter_reuses_prefix_for_memory_only_repair` (98-109) - unchanged
  Gates 1-4 with only Gate 5 invalidated stay reusable as the memory-only start.
- `test_green_prefix_adapter_refuses_stale_certificate_prefix` (112-123) -
  `gate-five-prefix-stale` when the chain validator refuses the prefix against the admission.
- `test_green_prefix_adapter_translates_r21_refusal_with_findings` (126-143) and
  `test_green_prefix_adapter_translates_plain_r21_value_error` (146-160) - R21 refusals are
  translated into typed Gate-5 refusals with the observed summary, with and without findings.

### Conventions

Tests drive the real `require_green_gate_prefix` over certificates from the shared
`_scenario`/`_green_prefix` scaffold; refusal assertions read exact status codes.

### Invariants And Boundaries

- No memory scan or coherence publication may start before the exact green Gate 1-4 prefix is
  proven current.
- The adapter never re-decides R21 reuse policy; it only enforces the exact memory-only start.

### Todos

None.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Reuse and memory-only-repair routes force the green prefix proof. | `test_green_prefix_adapter_reuses_exact_gate_one_to_four`; `test_green_prefix_adapter_reuses_prefix_for_memory_only_repair` | mcp/tests/test_final_gate_prefix_adapter.py:40-52; mcp/tests/test_final_gate_prefix_adapter.py:98-109 |
| Incomplete, code-mismatch, stale, and invalidated prefix refusals. | `test_green_prefix_adapter_refuses_incomplete_prefix`; `test_green_prefix_adapter_refuses_when_code_tree_mismatches_admission`; `test_green_prefix_adapter_restarts_at_gate_one_on_code_change`; `test_green_prefix_adapter_refuses_stale_certificate_prefix` | mcp/tests/test_final_gate_prefix_adapter.py:55-66; mcp/tests/test_final_gate_prefix_adapter.py:69-80; mcp/tests/test_final_gate_prefix_adapter.py:83-95; mcp/tests/test_final_gate_prefix_adapter.py:112-123 |
| R21 refusals translate into typed Gate-5 refusals with and without findings. | `test_green_prefix_adapter_translates_r21_refusal_with_findings`; `test_green_prefix_adapter_translates_plain_r21_value_error` | mcp/tests/test_final_gate_prefix_adapter.py:126-143; mcp/tests/test_final_gate_prefix_adapter.py:146-160 |
| The suite is registered in the integration lane of the evidence manifest. | "mcp/tests/test_final_gate_prefix_adapter.py" | mcp/tests/test-evidence-lanes.toml:401-401 |

## Update History

- 2026-09-05T06:39:59+00:00 — L31 scoped citation curation against frozen ea359649: repaired anchor grammar and exact source coordinates while preserving the current behavioral claims. No content impact; source verification metadata was not advanced.

- 2026-09-04T01:48+02:00 — 260831-CCR-L08 Gate-5 memory pass: created this file-level
  onboarding card for the new CCR-R08 Gate 1-4 prerequisite-prefix adapter forcing suite
  delivered in code commit 16d1a4d6; anchors and ranges derived from the current worktree source
  and pinned to that commit. The suite entered the `integration` lane of
  `test-evidence-lanes.toml` in the same change.
