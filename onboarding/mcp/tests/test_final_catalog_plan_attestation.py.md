# mcp/tests/test_final_catalog_plan_attestation.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_final_catalog_plan_attestation.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T04:32:25+00:00 |
| lastVerifiedCommitHash | `16d1a4d6d6f8e8572b4bca10b8a4a84485449604` |
| lastVerifiedCommitDate | 2026-09-04T00:55:21+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

CCR-R08 forcing suite for the final catalog plan and attestation contracts: complete-catalog
registry coverage, `compile_final_catalog_plan`/`final_catalog_attestation` population
contracts, gate-five semantic-input assembly, and coherence-subrecord coverage. Split from the
original single module (repository file-size hard limit); the shared fixture scaffold is
imported from `test_final_full_memory_coherence_certification`. The suite is explicitly
registered in the `integration` lane of `test-evidence-lanes.toml`.

## Code Commentary

### Logic

- `test_complete_final_catalog_covers_the_whole_memory_checker_registry` (56-63) and
  `test_complete_catalog_refuses_uncovered_checker_registry` (255-264) force the closed
  population to match `AVAILABLE_CHECKS` exactly.
- Plan binding: `test_plan_refuses_affected_closure_bound_to_another_memory_tree`
  (143-157), `test_compile_plan_refuses_affected_closure_code_tree_mismatch` (281-294),
  `test_compile_plan_refuses_non_accepting_affected_disposition` (297-311),
  `test_compile_plan_refuses_empty_coherence_subrecords` (267-278) and
  `test_compile_plan_refuses_uncovered_pending_full_only_population` (314-329).
- Attestation exhaustion: `test_attestation_must_exhaust_the_planned_population` (80-93),
  `test_attestation_green_and_red_and_blocked` (96-140),
  `test_attestation_refuses_plan_owning_unknown_item` (332-344), and
  `test_attestation_refuses_plan_without_standard_checks` (347-358).
- Coherence subrecords and Gate-5 inputs: `test_coherence_subrecords_require_affected_coverage`
  (206-223), `test_coherence_subrecords_cover_judgment_evidence` (361-380),
  `test_assemble_gate_five_inputs_binds_exact_certificate_inputs` (165-188),
  `test_assemble_gate_five_inputs_refuses_duplicate_subrecords` (191-203), and
  `test_assemble_gate_five_inputs_refuses_empty_subrecords` (383-392).

### Conventions

Each negative construction asserts a typed `FinalCertificationError` (or an exact refusal
code) rather than a fallback; a shared `_catalog_plan` helper (66-77) builds one valid plan
for the forcing base.

### Invariants And Boundaries

- The complete catalog must cover the whole current memory checker registry.
- The attestation must exhaust exactly the planned population; no weakened incremental-only
  acceptance is a valid substitute.
- Gate-5 semantic inputs require at least one canonical coherence subrecord.

### Todos

None.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Complete-catalog registry coverage and refusal. | `test_complete_final_catalog_covers_the_whole_memory_checker_registry`; `test_complete_catalog_refuses_uncovered_checker_registry` | mcp/tests/test_final_catalog_plan_attestation.py:56-63; mcp/tests/test_final_catalog_plan_attestation.py:255-264 |
| Exact plan binding to one candidate pair. | `test_plan_refuses_affected_closure_bound_to_another_memory_tree`; `test_compile_plan_refuses_affected_closure_code_tree_mismatch` | mcp/tests/test_final_catalog_plan_attestation.py:143-157; mcp/tests/test_final_catalog_plan_attestation.py:281-294 |
| Attestation exhaustion and green/red/blocked mapping. | `test_attestation_must_exhaust_the_planned_population`; `test_attestation_green_and_red_and_blocked` | mcp/tests/test_final_catalog_plan_attestation.py:80-93; mcp/tests/test_final_catalog_plan_attestation.py:96-140 |
| Coherence subrecords and Gate-5 semantic-input assembly. | `test_coherence_subrecords_cover_judgment_evidence`; `test_assemble_gate_five_inputs_binds_exact_certificate_inputs` | mcp/tests/test_final_catalog_plan_attestation.py:361-380; mcp/tests/test_final_catalog_plan_attestation.py:165-188 |
| The suite is registered in the integration lane of the evidence manifest. | "mcp/tests/test_final_catalog_plan_attestation.py" | mcp/tests/test-evidence-lanes.toml:406-406 |

## Update History

- 2026-09-06T04:32:25+00:00 — L32 incoming-evidence curation: verified the exact cited lane member or current test-function owner against private C b34f4a59 and corrected only its moved coordinates. Existing own-source verification provenance is retained.

- 2026-09-06T00:42:13+00:00 — Gate-5 citation repair: re-read the cited evidence-lane member and its declared classification and corrected its incoming range. Existing source verification provenance is retained.

- 2026-09-05T06:39:59+00:00 — L31 scoped citation curation against frozen ea359649: repaired anchor grammar and exact source coordinates while preserving the current behavioral claims. No content impact; source verification metadata was not advanced.

- 2026-09-04T01:48+02:00 — 260831-CCR-L08 Gate-5 memory pass: created this file-level
  onboarding card for the new CCR-R08 final catalog plan/attestation forcing suite delivered in
  code commit 16d1a4d6; anchors and ranges derived from the current worktree source and pinned
  to that commit. The suite entered the `integration` lane of
  `test-evidence-lanes.toml` in the same change.
