# mcp/tests/test_quality_gate_public_contract.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_quality_gate_public_contract.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T14:19+02:00 |
| lastVerifiedCommitHash |  `f95487ec993b58d34911bba0206a7fa6ef9684eb`|
| lastVerifiedCommitDate |  2026-08-24T15:28:18+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Focused forcing suite for immutable quality-generation recovery and the strict public quality-result
wire contract.

## Code Commentary

### Logic

The pointer-rotation test publishes generation A, rotates the current pointer to generation B after
the recovery loader returns, and proves recovery loaded the manifest once and retained A's immutable
result path and contents. The response-model test proves both `reportPath` and
`publishedResultPath` survive final response validation and appear in the generated schema, while
an undeclared quality field is rejected.

### Invariants And Boundaries

- A recovery attempt operates on one manifest snapshot; it cannot mix generation A metadata with
  generation B paths.
- Public response validation preserves both path meanings and rejects extra vocabulary.
- The tests address the public boundary and one focused recovery mechanism, not an omnibus gate.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies to these repository-internal forcing tests.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Pointer rotation after the loader snapshot cannot redirect recovered evidence. | `test_recovery_uses_one_manifest_generation_when_the_pointer_rotates` | mcp/tests/test_quality_gate_public_contract.py:19-74 |
| Strict worktree response models retain both quality paths and reject an unmodeled path. | `test_public_worktree_response_models_and_retains_both_quality_paths` | mcp/tests/test_quality_gate_public_contract.py:76-123 |

## Cross-Repo References

No meaningful cross-repository boundary applies.

## Update History

- 2026-08-24T14:19+02:00 — 260821-DAGQC-L2: created for one-snapshot recovery and strict public quality-result regressions. Verification remains blank until architect-owned closeout stamps the code commit.
