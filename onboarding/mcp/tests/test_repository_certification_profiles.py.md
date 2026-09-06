# mcp/tests/test_repository_certification_profiles.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_repository_certification_profiles.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T21:45:53+00:00 |
| lastVerifiedCommitHash | `d36109038b3f2b500c138f9dc1ea9c9f9a247489` |
| lastVerifiedCommitDate | 2026-09-06T22:21:49+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

Exercises portable repository-owned Gate 1–4 profiles using distinct fixture languages and adapters. It checks digest invalidation, preservation of earlier gate identities after a later edit, explicit not-applicable gates, confined selector/decoder outputs, refusal of unreasoned targeted expansion, passing teardown prerequisites and invalid-graph rejection before compilation. These are fixture protocol checks, not installed-vendor smoke evidence.

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
| Two language distinct repositories compile the same four gate protocol | `test_two_language_distinct_repositories_compile_the_same_four_gate_protocol` | mcp/tests/test_repository_certification_profiles.py:66-90 |
| Profile edit changes profile and plan identity | `test_profile_edit_changes_profile_and_plan_identity` | mcp/tests/test_repository_certification_profiles.py:93-130 |
| Later gate edit retains earlier gate plan identities | `test_later_gate_edit_retains_earlier_gate_plan_identities` | mcp/tests/test_repository_certification_profiles.py:133-165 |
| Explicit not applicable gate remains typed and visible | `test_explicit_not_applicable_gate_remains_typed_and_visible` | mcp/tests/test_repository_certification_profiles.py:168-207 |
| Distinct fixture adapters and decoders complete the declared protocol | `test_distinct_fixture_adapters_and_decoders_complete_the_declared_protocol` | mcp/tests/test_repository_certification_profiles.py:211-241 |
| Result decoder refuses a symlink escape | `test_result_decoder_refuses_a_symlink_escape` | mcp/tests/test_repository_certification_profiles.py:244-253 |
| Repository profile selector refuses an unadmitted absolute output | `test_repository_profile_selector_refuses_an_unadmitted_absolute_output` | mcp/tests/test_repository_certification_profiles.py:256-263 |
| Selector result refuses unreasoned output and targeted full expansion | `test_selector_result_refuses_unreasoned_output_and_targeted_full_expansion` | mcp/tests/test_repository_certification_profiles.py:266-302 |
| Repository profile teardown adapter requires a passing cleanup checkpoint | `test_repository_profile_teardown_adapter_requires_a_passing_cleanup_checkpoint` | mcp/tests/test_repository_certification_profiles.py:305-335 |
| Invalid graphs refuse before plan compilation | `test_invalid_graphs_refuse_before_plan_compilation` | mcp/tests/test_repository_certification_profiles.py:349-395 |

## Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external evidence is needed for these assertions. | N/A | N/A |

## Update History

- 2026-09-06T21:45:53+00:00 — Reconciled the retained IAS test/helper population and exact citation ranges, preserving prior history and verification provenance; no tests or review were run.


- 2026-09-06T04:32:25+00:00 — L32 private-candidate curation at `b34f4a59562b76a3e2413027468e0f699117b36f`: Added the four-case full selector ordering regression and refreshed exact current source anchors without importing later L33 applicability behavior. Verification is source review of the prepared commit; Gate 5 and delivery remain pending.

- 2026-09-06T00:23:26+00:00 — L30 recovery: Reverified retained source or route ownership against actual candidate commit 97e8ed2e1fae21756c3ad995c30613d4fbfcc503; replaced the superseded private-candidate stamp.

- 2026-09-06T00:17+02:00 — Reconciled the teardown proof-output argument without relaxing the missing-checkpoint refusal, and replaced stale task-document citations with exact repository test evidence.

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for
  db57101a9001ede8c681ff9de4eb0147d8b636bc (CCR-R19@v2/L19): created the card and recorded the
  L19 v2 selector-result forcing — digest binding, unreasoned-output/targeted-full refusals,
  external-input digest coupling, identity-bound fixture emission, and the ownership
  configuration-digest equality assertion. Verification is pinned to the owning commit.
