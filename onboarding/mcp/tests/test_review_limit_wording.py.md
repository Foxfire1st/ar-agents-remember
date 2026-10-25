# mcp/tests/test_review_limit_wording.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

Holds MIK-R116 evidence 6 and 10: no text names a review-round number, and the stage-end sections that
replace such a number hold in both the sources and the compiled capsules. The check runs over the canonical
skill tree and the packaged serving copy.

## Code Commentary

### Logic

`SKILL_TREES` names the canonical and packaged trees, `_role_operations()` yields the operations the
composition manifest gives a role, and `_compile()` builds the capsules a seat receives. The number detector
is built from `_ONES`, `_TEENS`, `_TENS`, `_TWO_DIGIT_WORD`, `_NUMBER_WORD` and `ROUND_NUMBER_PATTERNS`,
which is what makes it a class detector rather than a spelling list.

- **No number.** `test_no_role_source_names_a_review_round_number` and
  `test_no_compiled_capsule_names_a_review_round_number` scan sources and compiled texts.
- **The detector has teeth.** `test_number_detector_catches_limit_forms_and_exempts_labels` proves limit
  forms are caught while intentional labels are exempt.
- **Stage-end sections.** `test_stage_end_sections_hold_in_sources_and_compiled_texts` requires the four
  roles to hold the section and its parts; `_section_missing()` and `_check_source_sections()` bind each
  facet to the extracted section rather than to anywhere in the file.
- **Binding fails on mutation.** `test_stage_section_binding_fails_on_deletion_and_relocation` and
  `test_compiled_section_binding_fails_on_deletion_and_relocation` delete or relocate each required facet and
  require the check to fail; `_mutate_section()` performs the mutation on the real text.
- **Rule 9.** `test_rule_nine_sentences_hold_for_reviewer_worker_manager` keeps the Reviewer, Worker and
  Manager sentences in both source and compiled projections.

### Conventions

`REVIEWER_STAGE_EQUIVALENTS` and `CURATOR_STAGE_EQUIVALENTS` hold role-scoped alternatives, and `STOPS` and
`STAGE_PARTS` define the section boundary the facets are bound to.

### Invariants And Boundaries

- A limit is stated as a property of the settings, never as a number in a text.
- A facet outside the extracted section does not satisfy the check.

## Evidence

- Positive detector controls and the intentional label and allowance exemptions. [1]

- Stage facets are bound to the extracted section rather than satisfied by relocated source text. [2]

- The Reviewer, Worker and Manager property and construction sentences survive source and compiled projections. [3]

- Reviewer/Curator facet alternatives are explicitly role scoped. Presence, deletion and relocation checks still bind to the extracted Stage end section. Source and compiled controls assert the original surface is complete and mutation actually changes text; compiled relocation is now exercised as well as deletion. The four roles are parametrized individually; numeric budget detector and rule-nine cases remain. [4]
