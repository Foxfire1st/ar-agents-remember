# mcp/tests/test_certification_plan_authority.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_certification_plan_authority.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-01T03:11+02:00 |
| lastVerifiedCommitHash | `0506b57a1a80e0b377e9cc3303e1841d3bd4799a`|
| lastVerifiedCommitDate | 2026-09-01T12:17:08+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Proves that canonical registry compilation is the sole plan authority and that registry work
measurement rejects hostile scale before expensive allocation while accepting the exact boundary.

## Code Commentary

### Logic

The suite forges deleted, inserted, substituted, and candidate-mismatched plan catalogs and
requires result publication to refuse them. It measures linear/shared/dense artifact graphs,
zero-query behavior, exact storage peaks, deterministic wave scaling, exact-cap admission, digest
reuse after exact deduplication, and headroom against a measured portable repository baseline.

### Conventions

The suite imports permanent builders from `certification_registry_test_support.py`; its local
helpers only reconstruct deliberate plan forgeries and passing observations.

### Invariants And Boundaries

- Recomputed digests do not authorize a plan whose semantic catalog differs from compilation.
- Candidate identity is part of result-publication authority.
- Hostile query products refuse before query storage allocation.
- Unconsumed output declarations follow the zero-query path.
- Exact-cap and cap-plus-one cases make the shared work boundary falsifiable.

### Todos

Keep performance assertions deterministic and tied to measured operation/storage counts rather
than machine-specific wall time alone.

## Docs References

No Domain Documentation source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Forged plan catalogs and candidate drift are rejected at terminal publication. | `test_result_publication_refuses_deleted_inserted_and_substituted_plan_catalogs`; `test_result_publication_binds_the_external_candidate_identity` | mcp/tests/test_certification_plan_authority.py:92-156 |
| Artifact reachability has explicit linear, shared, hostile-product, and zero-query evidence. | `test_many_distinct_artifact_producers_have_linear_operations_and_storage`; `test_zero_query_unconsumed_output_skips_every_producer_catalog` | mcp/tests/test_certification_plan_authority.py:157-297 |
| Exact graph storage peaks and execution-wave scaling are censused. | `test_exact_self_query_and_dense_graph_peaks_are_fully_censused`; `test_wave_compilation_scales_for_chain_and_broad_catalogs` | mcp/tests/test_certification_plan_authority.py:298-358 |
| Exact work-budget admission and measured scale headroom are asserted. | `test_registry_work_budget_accepts_exact_cap_and_refuses_cap_plus_one`; `test_budget_has_measured_repository_scale_headroom` | mcp/tests/test_certification_plan_authority.py:365-438 |

## Cross-Repo References

No external repository suite is invoked; portability is demonstrated with generic generated
registries.

| Finding | Anchor | Source |
| --- | --- | --- |
| The suite consumes only the generic support artifact and certification contracts. | `certification_registry_test_support` | mcp/tests/test_certification_plan_authority.py:8-52 |

## Update History

- 2026-09-01T03:11+02:00 — Created for plan-authority, pre-allocation boundedness, and scaling
  evidence. Verification remains closeout-owned until the source candidate is committed.
