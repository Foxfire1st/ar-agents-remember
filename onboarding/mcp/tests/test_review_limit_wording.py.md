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

`REVIEWER_STAGE_EQUIVALENTS` holds Reviewer alternatives. Curator facets directly name its current stage-end obligations, including manual provenance and covered-write recovery. `STOPS` and `STAGE_PARTS` define the section boundary the facets are bound to.

### Invariants And Boundaries

- A limit is stated as a property of the settings, never as a number in a text.
- A facet outside the extracted section does not satisfy the check.

Worker stage completion requires the handover checks named in workspace.memoryRoot/system/coding-guidelines.md on a clean copy of final bytes. A dedicated control rejects replacement by or reinsertion of the retired fixed focused-tests/lint/type sentence. Curator stage facets directly preserve covered-write recovery, manual provenance and stop boundaries. These are source assertions/support behavior, not a fresh invocation, host result or AR acceptance.

## Evidence
- Positive detector controls and the intentional label and allowance exemptions. [1]

- Stage facets are bound to the extracted section rather than satisfied by relocated source text. Anchor: `test_stage_section_binding_fails_on_deletion_and_relocation` `test_compiled_section_binding_fails_on_deletion_and_relocation` [2]

- The Reviewer, Worker and Manager property and construction sentences survive source and compiled projections. [3]

- Reviewer facet alternatives are role scoped; Curator facets directly pin its current stage-end text, including manual provenance and covered-write recovery. Source and compiled deletion/relocation controls bind every facet to its own stage section and prove a real mutation; number and rule-nine guards remain. [Past-epoch source caption, detached from live reference 4. Recorded citation custody: mcp/tests/test_review_limit_wording.py blob a53d58ed9a10e4386e8fbc84dea41386c8f74893 (available); historical event commit not identified. No historical event or intent inferred.]

Current source: Stage-end checks bind each role’s required facets to its own section in source and compiled text. Reviewer equivalents remain role-scoped; Curator facets include clean quality, installed-writer versus manual provenance and covered-write recovery. Deletion/relocation controls require a real mutation, while round-number and rule-nine guards remain.

- Stage-end checks bind each role’s required facets to its own section in source and compiled text. Reviewer equivalents remain role-scoped; Curator facets include clean quality, installed-writer versus manual provenance and covered-write recovery. Deletion/relocation controls require a real mutation, while round-number and rule-nine guards remain. [4]

- Worker stage completion requires the handover checks named in workspace.memoryRoot/system/coding-guidelines.md on a clean copy of final bytes. A dedicated control rejects replacement by or reinsertion of the retired fixed focused-tests/lint/type sentence. Curator stage facets directly preserve covered-write recovery, manual provenance and stop boundaries. These are source assertions/support behavior, not a fresh invocation, host result or AR acceptance. [5]
