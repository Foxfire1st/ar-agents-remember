# mcp/tests/test_quality_gate_public_contract.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_quality_gate_public_contract.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T10:05+02:00 |
| lastVerifiedCommitHash | `cfd0938103b1392e471144b6997c51a41591ad2b` |
| lastVerifiedCommitDate | 2026-09-04T08:34:11+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Focused forcing suite for immutable quality-generation recovery and the strict public quality-result
wire contract.


CCR-R22@v1 (L22, commit `685f83c44055`): the public quality-gate contract tests now cover the
profile-bound public payload -- executor adapter id, profile digest, profile plan digest,
selection id, and result artifact fields on the strict gate result, plus the
`profile-adapter-owned` process policy.


CCR-R12@v4 (260831-CCR-L12, commit `cfd09381`): the suite publishes its recovery generations
through `clean_quality_executor.ReportBindings(attestation=..., runtime_authority_digest=None)`
because `_publish_reports` now takes explicit bindings; the immutable manifest under test is the
schema-v3.1 shape with the optional `runtimeAuthorityDigest` root field (absent/None here).

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
| Pointer rotation after the loader snapshot cannot redirect recovered evidence. | `test_recovery_uses_one_manifest_generation_when_the_pointer_rotates` | mcp/tests/test_quality_gate_public_contract.py:131-205 |
| Strict worktree response models retain both quality paths and reject an unmodeled path. | `test_public_worktree_response_models_and_retains_both_quality_paths` | mcp/tests/test_quality_gate_public_contract.py:207-251 |

## Cross-Repo References

No meaningful cross-repository boundary applies.

## 260824-PDLS Snapshot Evidence Proof

The public recovery contract now pins a candidate tree while proving one caller-held manifest
snapshot survives concurrent publication rotation. Evidence is minted from that verified snapshot,
not from a second mutable read or a diagnostic payload.

## Update History

- 2026-09-04T10:05+02:00 - 260831-CCR-L12 Gate-5 memory pass for cfd09381 (CCR-R12@v4): recorded the `ReportBindings`-based publication in the public quality-gate contract suite and the schema-v3.1 manifest shape it forces.

- 2026-09-03T13:30+02:00 - 260831-CCR-L27 Gate-5 memory pass: re-anchored the two
  public-contract test citations to their current definitions (pointer-rotation 131-205,
  response-models 207-251) after the readiness coverage companion moved later test content.
  Verification remains pinned to the pre-commit source history until closeout.

- 2026-09-03T12:30+02:00 -- 260831-CCR memory curation pass for 685f83c44055 (CCR-R22@v1/L22): recorded the profile-identity field coverage in the public gate contract tests.


- 2026-08-26T10:44:52+02:00 — No content impact: reviewed the clean-executor and quality-gate package relocations; public recovery and response-model contracts are unchanged.
- 2026-08-24T21:23+02:00 — Added candidate-tree and one-snapshot certifying evidence proof.

- 2026-08-24T14:19+02:00 — 260821-DAGQC-L2: created for one-snapshot recovery and strict public quality-result regressions. Verification remains blank until architect-owned closeout stamps the code commit.
