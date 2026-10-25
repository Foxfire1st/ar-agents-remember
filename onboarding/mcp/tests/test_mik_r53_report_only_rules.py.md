# mcp/tests/test_mik_r53_report_only_rules.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

Decides MIK-R53 Part C (rules 10-12) for the report-only rules: a rule that only reports must name its report
reason and be refused registration when it does not, a carried record that no longer holds reports at a merge and
refuses off it, and once a migration census is complete the carried debt refuses on every publication route.

## Code Commentary

### Logic

`_validate()` runs the validator, `_rules()` and `_messages()` read the registry and its messages,
`_census_files()` builds a migration census over two onboarding routes with the given statuses, and
`_validate_counted()` counts `_Admitted` equality comparisons so a case can constrain per-record classification
without timing the wall clock.

- **Registration.** `test_a_plain_report_only_rule_is_refused_registration`,
  `test_a_rule_with_both_report_reasons_is_refused_registration`,
  `test_no_registered_rule_is_plainly_report_only` and
  `test_each_of_the_ten_rules_carries_its_mik_r53_decision` keep the registry honest;
  `test_the_five_refusing_rules_report_inside_the_writer` keeps the five refusing rules reporting inside the
  writer, and `test_governs_refuses_a_decision_that_governs_nothing` refuses an empty decision.
- **Merge and off-merge.** `test_an_existing_record_whose_criterion_no_longer_holds_refuses_off_merge` and
  `..._reports_at_a_merge`, `test_a_carried_route_absent_refuses_off_merge_and_reports_at_a_merge`,
  `test_an_unrealized_family_refuses_off_merge_and_reports_at_a_merge` and
  `test_a_carried_stale_anchor_refuses_off_merge_and_reports_at_a_merge` state the pair for each class.
- **Conversion.** `test_a_conversion_authors_merge_and_debt_states`,
  `test_a_conversion_sidecar_without_markdown_names_conversion_and_next_refusal` and the three
  `test_conversion_with_*_is_refused_at_entry` cases keep a standalone conversion reporting what later routes will
  judge, while a conversion carrying a base, code or a publication refuses at entry.
- **Census.** `test_candidate_overview_route_joins_the_migration_population`,
  `test_no_census_no_routes_stays_incomplete` and `test_latest_status_across_censuses_governs` keep the
  population and its status resolution.
- **Carried versus new.** `test_a_carried_sidecar_without_markdown_reports_while_a_new_one_refuses`,
  `test_a_carried_unresolved_target_reports_while_a_new_one_refuses`,
  `test_a_carried_unassigned_family_reports_while_a_new_state_refuses` and
  `test_carried_legacy_debt_is_counted_while_new_legacy_refuses` keep carried debt reporting while a new one
  refuses, and the `..._once_complete` cases refuse the same carried debt after a full census.
- **Publication routes.** `test_an_unrealized_family_refuses_at_publication`,
  `test_completed_census_debt_refuses_at_landing_and_sync` and `test_a_merge_moved_row_is_refused_at_the_next_publication`
  extend the refusal to landing, sync and the next publication.
- **Messages and texts.** `test_no_violation_message_says_reported_not_refused` and
  `test_a_reported_finding_names_its_reason_and_the_route_that_refuses` keep a report from reading as a refusal,
  and `test_the_command_help_lists_the_ten_rules_with_their_decision` and
  `test_the_c02_skill_lists_the_ten_rules_with_their_decision` (now reading the quality-control workflow text)
  keep the decisions written down.
- **Cost.** `test_all_new_unassessed_classifies_each_record_in_constant_time` and
  `test_mixed_complete_migration_classifies_each_record_in_constant_time` bound the per-record comparisons.

### Conventions

The expected merge-reported and writer-reported rule sets also include `R198.1-reference-anchor`. It reports repair debt during authoring/sync and refuses publication; it is not an unconditionally report-only rule. Existing test function spellings containing ten/five are retained names, not current rule population counts.

A case that asserts a route's behaviour calls the validator through the route (publication, merge, sync) rather
than only through the validator function.

### Invariants And Boundaries

- A report-only rule states its reason; a rule that reports nothing is refused registration.
- Carried debt reports until the census is complete, then refuses.

## Evidence


- Registration rejects unnamed reporting or competing report reasons and verifies the rule sets. [1]

- Leaf and publication versus merge cases exercise the existing-record, absent-route, unrealized-family and gone-path boundaries. [2]
- A standalone conversion rejects bases, paired code and publication, while candidate overviews join the migration population. [3]
- Admission operation counts constrain per-record classification rather than elapsed runtime. [4]
- A merge-moved row reports at merge but is refused by covered-entry validation at publication. [5]

- Messages, command help and the workflow text carry the named reporting and refusal decisions. [6]

- Complete-census cases cover carried debt at both landing and sync with incomplete controls. [7]
- The merge-report set assertion includes the separate link-target rule beside the original ten decisions. [8]
