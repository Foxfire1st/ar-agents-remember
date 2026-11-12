# mcp/tests/test_review_limit_wording.py

## Governing Overview

[overview](overview.md)

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
- **Stage-end sections.** `test_stage_end_sections_hold_in_sources_and_compiled_texts` requires each facet of the
  four roles to hold at its current owning section — a role-file section, or `operations/review.md` for the
  Reviewer's record-recheck facets — in both trees' sources and in every declared operation's compiled capsule; `_section_missing()` and `_check_source_sections()` bind each
  facet to the extracted section rather than to anywhere in the file.
- **Binding fails on mutation.** `test_stage_section_binding_fails_on_deletion_and_relocation` and
  `test_compiled_section_binding_fails_on_deletion_and_relocation` delete or relocate each required facet and
  require the check to fail, as does moving the Reviewer's record-only procedure pointer; `_mutate_section()`
  performs the mutation on the real text, and the compiled case mutates one compiled capsule per role.
- **Rule 9.** `test_rule_nine_sentences_hold_for_reviewer_worker_manager` keeps the Reviewer, Worker and
  Manager sentences in both source and compiled projections.

### Conventions

`STAGE_CONTRACTS` gives every facet its owning document, heading, current clause and the clause its deletion
control removes; the Reviewer also needs `REVIEWER_RECORD_POINTER` in its own role section. Curator facets directly name its current stage-end obligations, including manual provenance and covered-write recovery. `STOPS` and `STAGE_PARTS` name the facet identities that `STAGE_CONTRACTS` binds to their owning sections.

### Invariants And Boundaries

- A limit is stated as a property of the settings, never as a number in a text.
- A facet outside the extracted section does not satisfy the check.

Worker stage completion requires the handover checks named in workspace.memoryRoot/system/coding-guidelines.md on a clean copy of final bytes. A dedicated control rejects replacement by or reinsertion of the retired fixed focused-tests/lint/type sentence. Curator stage facets directly preserve covered-write recovery, manual provenance and stop boundaries. These are source assertions/support behavior, not a fresh invocation, host result or AR acceptance.

## Evidence
- Positive detector controls and the intentional label and allowance exemptions. [1]

- Stage facets are bound to the extracted section rather than satisfied by relocated source text. [2]

- The Reviewer, Worker and Manager property and construction sentences survive source and compiled projections. [3]

- Stage-end checks bind each role’s required facets to its current owning section in source and compiled text; the Reviewer's record-recheck facets are owned by `operations/review.md`. Curator facets include clean quality, installed-writer versus manual provenance and covered-write recovery. Deletion/relocation controls require a real mutation, while round-number and rule-nine guards remain. [4]

- Worker stage completion requires the handover checks named in workspace.memoryRoot/system/coding-guidelines.md on a clean copy of final bytes. A dedicated control rejects replacement by or reinsertion of the retired fixed focused-tests/lint/type sentence. Curator stage facets directly preserve covered-write recovery, manual provenance and stop boundaries. These are source assertions/support behavior, not a fresh invocation, host result or AR acceptance. [5]
