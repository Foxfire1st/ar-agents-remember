# mcp/tests/test_structural_limits.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_structural_limits.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T21:45:53+00:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

Checks structural detectors on small source trees: wide class surfaces and sibling-module methods retain their measured count, properties/setters and overloads count once, all function offenders are reported, crowded directories fail, and an existing declared directory deviation affects exactly its named directory. This documents unchanged structural policy; it does not create a CRAP-score exception mechanism.

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
| A wide class is reported with its measured surface | `test_a_wide_class_is_reported_with_its_measured_surface` | mcp/tests/test_structural_limits.py:132-143 |
| Moving methods into a sibling module does not lower the count | `test_moving_methods_into_a_sibling_module_does_not_lower_the_count` | mcp/tests/test_structural_limits.py:157-166 |
| A property and its setter count once | `test_a_property_and_its_setter_count_once` | mcp/tests/test_structural_limits.py:194-208 |
| Typing overloads count once | `test_typing_overloads_count_once` | mcp/tests/test_structural_limits.py:210-225 |
| The function length check reports every offender not the first | `test_the_function_length_check_reports_every_offender_not_the_first` | mcp/tests/test_structural_limits.py:236-259 |
| The directory check rejects a crowded directory | `test_the_directory_check_rejects_a_crowded_directory` | mcp/tests/test_structural_limits.py:261-278 |
| A declared deviation silences exactly the directory it names | `test_a_declared_deviation_silences_exactly_the_directory_it_names` | mcp/tests/test_structural_limits.py:280-293 |

## Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external evidence is needed for these assertions. | N/A | N/A |

## Update History

- 2026-09-06T21:45:53+00:00 — Reconciled the retained IAS test/helper population and exact citation ranges, preserving prior history and verification provenance; no tests or review were run.


- 2026-08-28T06:40+02:00 — No content impact: moved the structural-limit verification import
  into `agents_remember_test_support`; limit and deviation assertions remain unchanged.
- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
