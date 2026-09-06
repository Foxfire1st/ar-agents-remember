# mcp/tests/test_quality_gate_public_contract.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_quality_gate_public_contract.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T21:45:53+00:00 |
| lastVerifiedCommitHash | `d36109038b3f2b500c138f9dc1ea9c9f9a247489` |
| lastVerifiedCommitDate | 2026-09-06T22:21:49+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

Checks lossless public closeout readiness and immutable quality evidence. The retained cases preserve finalization authority through projection, keep diagnostic results non-certifying even when their rails match, reject stale certificates and invalid profiles, and refuse changed decoder bytes under the same identifier.

## Code Commentary

### Logic

The current evidence boundary is the source-listed behavior below. Earlier coverage claims in
history describe prior populations and must not be used to recreate removed tests or claim they
still run. The retained behavior and its fixture limits, described above, govern this card.

### Conventions

The table lists retained test definitions, not collected parametrized or subtest counts.
Inspect the cited setup and collaborators before treating a focused result as end-to-end evidence.

### Invariants And Boundaries

Preserve exact refusal, identity, and cleanup assertions rather than adding overlapping helper
cases. Coverage percentages are diagnostic and production CRAP 20 prompts review; neither implies
an obligation to restore removed cases. Full suites and whole-candidate review remain master-end
work. This source inspection does not claim a newly executed test or acceptance result.

### Todos

No additional implementation scope is opened by this memory reconciliation.

## Docs References

The repository has no configured Domain Documentation source. These claims concern its own test
fixtures and assertions, so the exact retained source is the direct evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain claim is required. | N/A | N/A |

## Repo-Internal References

Each current definition below can be inspected in the exact source file. Historical references
to removed methods are superseded by this current inventory.

| Finding | Anchor | Source |
| --- | --- | --- |
| Closeout readiness is lossless on every surface | `test_closeout_readiness_is_lossless_on_every_surface` | mcp/tests/test_quality_gate_public_contract.py:430-444 |
| Diagnostic readiness stays non certifying with matching rails | `test_diagnostic_readiness_stays_non_certifying_with_matching_rails` | mcp/tests/test_quality_gate_public_contract.py:447-467 |
| Stale certificates and invalid profile remain non green | `test_stale_certificates_and_invalid_profile_remain_non_green` | mcp/tests/test_quality_gate_public_contract.py:470-509 |
| Recovery refuses same id decoder byte drift | `test_recovery_refuses_same_id_decoder_byte_drift` | mcp/tests/test_quality_gate_public_contract.py:73-92 |

## Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external evidence is needed for these assertions. | N/A | N/A |

## Update History

- 2026-09-06T21:45:53+00:00 — Reconciled the retained IAS test/helper population and exact citation ranges, preserving prior history and verification provenance; no tests or review were run.


- 2026-09-06T15:11:59+00:00 — L33 pending candidate curation: Re-read the prepared source, documented supplied original publication rendering and pointer independence, and restored the readiness family with an explicit compiler-fixture boundary and current anchors. Verification names the real prepared source commit c69d5171187fa1957025e393270db9f5a864ab14; this entry does not claim CCR acceptance.

- 2026-09-04T10:05+02:00 - 260831-CCR-L12 Gate-5 memory pass for cfd09381 (CCR-R12@v4): recorded the `ReportBindings`-based publication in the public quality-gate contract suite and the schema-v3.1 manifest shape it forces.

- 2026-09-03T13:30+02:00 - 260831-CCR-L27 Gate-5 memory pass: re-anchored the two
  public-contract test citations to their current definitions (pointer-rotation 131-205,
  response-models 207-251) after the readiness coverage companion moved later test content.
  Verification remains pinned to the pre-commit source history until closeout.

- 2026-09-03T12:30+02:00 -- 260831-CCR memory curation pass for 685f83c44055 (CCR-R22@v1/L22): recorded the profile-identity field coverage in the public gate contract tests.


- 2026-08-26T10:44:52+02:00 — No content impact: reviewed the clean-executor and quality-gate package relocations; public recovery and response-model contracts are unchanged.
- 2026-08-24T21:23+02:00 — Added candidate-tree and one-snapshot certifying evidence proof.

- 2026-08-24T14:19+02:00 — 260821-DAGQC-L2: created for one-snapshot recovery and strict public quality-result regressions. Verification remains blank until architect-owned closeout stamps the code commit.
