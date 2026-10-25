# mcp/tests/test_bootstrap_converted_onboarding.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

One case per rule of converted-onboarding bootstrap (MIK-R45@v2): a repository must declare itself before a
contractless fixer authors cards, the root must already be converted, an old-format card blocks adoption, and
the bootstrap skill texts state the fixer, the order and the taskless pre-baseline route. It ends with a
composed journey from init through a second refusal.

## Code Commentary

### Logic

`_world()` builds a code repository, a coordination root and a settings file outside both;
`_fresh_converted_memory()` builds a converted memory root with no baseline and no cards;
`bound_validation()` binds real worktree services so a first baseline validates before it commits, and
`_write_card()` writes a card the fixer must leave alone when it refuses.

- **Admission.** `test_fixer_without_contract_refuses_an_undeclared_repository`,
  `..._refuses_an_unconverted_root` and `..._names_a_foreign_resolved_root` cover the three conditions;
  `test_fixer_without_contract_refuses_a_root_with_a_linked_worktree` adds the leaf-worktree condition, and
  `test_fixer_without_contract_is_refused_once_the_baseline_exists` hands the call over to the leaf route
  after the baseline.
- **Authoring before the baseline.** `test_fixer_without_contract_authors_cards_before_the_baseline` proves
  the admitted call writes the named card and its sidecar and says so.
- **Byte identity on refusal.** `test_refused_reauthor_card_and_sidecar_stay_byte_identical` compares digests:
  nothing of a refused card is written by either fixer stage.
- **Old-format cards.** `test_each_old_format_sign_blocks_the_baseline` reports `blocked-legacy-cards` per
  sign, `test_accept_drift_does_not_lift_blocked_legacy_cards` requires `blocked-legacy-cards` with either `accept_drift` value,
  `test_prose_and_code_mentions_of_legacy_keys_are_not_legacy_cards` requires only a metadata-key first cell
  to count as a stamp row, `test_correcting_the_listed_cards_unblocks_adoption` shows the rerun adopting, and
  `test_legacy_cards_cannot_refuse_an_adopted_repository` keeps the rule an adoption gate rather than a
  validator rule.
- **Skill texts.** `test_bootstrap_skill_texts_carry_no_legacy_card_format`,
  `test_bootstrap_skill_texts_state_the_fixer_and_the_order` and
  `test_bootstrap_skill_texts_state_taskless_route_and_audit_trail` read the shipped skill texts.
- **Audit trail.** `test_first_baseline_retains_onboarding_bootstrap_audit_trail` keeps
  `onboarding/bootstrap/` working files in the commit.
- **Route index.** `test_route_index_apply_without_contract_is_admitted_before_the_baseline` and
  `..._is_refused_after_the_baseline` give `route_index_refresh` apply the same admission.
- **Journey.** `test_bootstrap_journey_from_init_to_second_fixer_refusal` keeps the optional converted-fixer
  scenario: init, three cards, the fixer, status, adoption, reads and the second refusal. Before the first
  baseline it expects `context-not-admitted` / `memory_revision_unavailable` with an existing next action;
  after adoption it expects `not-recorded` and a developer-starts-Architect handover, without a
  knowledge-bootstrap command. It does not make this card-authoring journey a requirement of setup.

### Conventions

Cases read the real fixer stages and the real worktree services; `_sha()` makes a byte-identity check
explicit rather than implied by a reread.

### Invariants And Boundaries

- A refused card leaves both its Markdown and its sidecar byte-identical.
- A legacy card blocks adoption and only the listed cards' correction unblocks it; it never un-adopts a tree.

## Evidence

- Contractless fixing authors converted evidence and sidecars under measured pre-baseline admission. [1]
- Refused re-authoring preserves the exact card and sidecar bytes across both fixer stages. [2]
- Every old-format sign stays blocked through adoption with either `accept_drift` value. [3]
- Prose mentions of metadata names do not become legacy cards. [4]

- The source test keeps the c-03 fixer contract separate from setup: setup authors no onboarding and orders memory initialization before baseline adoption before foundation-state handoff to the Architect. [5]

- The first baseline retains the onboarding bootstrap audit artifacts. [6]

- The optional composed fixture keeps the prebaseline context-not-admitted refusal; after adoption its not-recorded answer asks the developer to start the Architect and omits a knowledge-bootstrap command. The fixture still fixes three cards, adopts, names the existing source/card with a string-form read and `state=named`, reads Alpha's prose using its own file tool and refuses a second contractless fixer. [7]


- The source test compiles the Bootstrap capsule and reads its declared step-8 foundation-report file; it checks baseline-before-handoff, no prebaseline leaf, and the retained existing-commit exception on the install owner. [8]
