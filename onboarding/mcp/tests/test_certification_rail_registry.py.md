# mcp/tests/test_certification_rail_registry.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_certification_rail_registry.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-01T03:11+02:00 |
| lastVerifiedCommitHash | `0506b57a1a80e0b377e9cc3303e1841d3bd4799a`|
| lastVerifiedCommitDate | 2026-09-01T12:17:08+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Proves the repository-neutral five-gate registry, exhaustive validation, immutable plan models,
and complete typed terminal-result semantics across valid and adversarial contracts.

## Code Commentary

### Logic

The suite exercises deterministic non-Agents-Remember compilation, candidate algorithms, strict
SemVer and semantic text, exact duplicate/conflict treatment, complete sibling findings,
dependency/applicability/artifact rules, gate barriers and waves, result completeness, evidence and
artifact bounds, diagnostic altitude, deep error immutability, sibling preservation, and
report-only enforcement.

### Conventions

Each test changes one contract dimension from the portable support baseline. Stable finding codes
are asserted rather than matching exception prose.

### Invariants And Boundaries

- A valid portable certifying profile compiles exactly Gates 1 through 5 in order.
- Conflicting variants retain their own semantic findings after exact duplicates collapse.
- Gate 3 consumes Gate 2 artifacts and later gates cannot satisfy earlier requirements.
- Terminal manifests contain every planned rail and preserve independent sibling outcomes.
- Missing/extra evidence, artifacts, results, or blockers fail publication.
- Diagnostic/report-only results cannot produce certifying green authority.
- Error findings are deeply immutable snapshots.

### Todos

Add repository-profile behavior only in the profile owner's tests; keep this suite generic.

## Docs References

No Domain Documentation source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| A non-Agents-Remember registry compiles deterministic immutable plans for all five gates. | `test_non_agents_remember_registry_compiles_one_deterministic_plan_per_gate` | mcp/tests/test_certification_rail_registry.py:56-83 |
| Exact duplicates, conflicts, SemVer, and inner sibling findings are independently covered. | `test_canonicalization_deduplicates_identical_rails_but_rejects_conflicts`; `test_conflicting_rail_and_profile_variants_keep_all_inner_findings` | mcp/tests/test_certification_rail_registry.py:99-247 |
| Plan barriers, waves, classification, dependency applicability, and sibling blocking are enforced. | `test_gate_plan_rejects_recomputed_digest_with_missing_gate_barriers`; `test_gate_manifest_keeps_failed_and_independent_siblings_and_blocks_only_dependant` | mcp/tests/test_certification_rail_registry.py:256-382 |
| Complete result, evidence, artifact, diagnostic, and semantic-text contracts refuse malformed publication. | `test_gate_manifest_refuses_result_omission`; `test_exact_semantic_text_bindings_reject_blank_or_padded_values` | mcp/tests/test_certification_rail_registry.py:384-631 |
| Exhaustive bounded findings, cycle-safe reachability, immutable errors, sibling preservation, and report-only behavior are explicit. | `test_under_budget_invalid_registry_returns_every_finding`; `test_report_only_result_cannot_turn_an_enforcing_failure_green` | mcp/tests/test_certification_rail_registry.py:632-803 |

## Cross-Repo References

No external repository suite is called.

| Finding | Anchor | Source |
| --- | --- | --- |
| Portability evidence uses `sample-repository` and a generic `portable-ci` profile. | `test_non_agents_remember_registry_compiles_one_deterministic_plan_per_gate` | mcp/tests/test_certification_rail_registry.py:56-83 |

## Update History

- 2026-09-01T03:11+02:00 — Created for generic registry, plan, and terminal-result contract
  evidence. Verification remains closeout-owned until the source candidate is committed.
