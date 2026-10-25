# mcp/tests/test_role_message_wording.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

Holds the wording oracle for messages-as-files (MIK-R117 rule 7): every role text, handover template and
messaging operation says that a message names its files instead of carrying them, names the `body` and
`attach` inputs and the folder, and states no number. The oracle runs over the canonical skill tree, the
packaged serving copy and the compiled capsule prompt and handover of every handover role.

## Code Commentary

### Logic

`_sync_targets()` loads `scripts/sync-skills.py` and exposes its inventory, so `surfaces()` names every
surface the product ships — canonical first — and `EXPECTED_SURFACE_COUNT` fixes that number at two: the
canonical tree and the packaged serving copy, the only generated copy the product ships. A dropped or
added surface fails the census visibly instead of passing on a smaller scan.

- **The census.** `test_the_surface_census_matches_the_product_inventory` compares the scanned surfaces
  with the inventory.
- **The oracle has teeth.** `test_the_oracle_catches_directives_and_keeps_legal_lines` feeds negative
  variants that must hit and legal lines that must not, so the patterns are not merely present.
- **Every surface states the contract.** `test_every_role_text_states_messages_as_files`,
  `test_every_handover_template_states_messages_as_files`,
  `test_the_messaging_operations_state_messages_as_files` and
  `test_compiled_capsules_state_messages_as_files` cover `ROLE_FILES`, `HANDOVER_TEMPLATE_FILES`,
  `OPERATION_FILES` and the compiled capsules of `COMPILED_ROLES`.
- **Delivered text.** `delivered_text()` returns the delivered Worker text — the operation file plus
  `roles/worker.md` — for `operations/implementation.md` (MIK-R203 rule 3), so the marker check reads what
  a seat actually receives.
- **Role-specific equivalents.** `missing_markers()` keeps Reviewer and Curator marker alternatives, and
  `test_reviewer_equivalents_keep_positive_facets_and_reject_deletion` and
  `test_reviewer_equivalents_keep_each_message_facet_and_reject_deletion` prove each equivalent is still
  checked when reinserted.
- **Addressing.** `test_report_returns_use_role_task_addressing_on_every_surface` keeps an ordinary report
  return addressed to the parent's role.

### Conventions

`FORBIDDEN_PATTERNS`, `FORBIDDEN_NUMBERS`, `MUST_CATCH` and `MUST_KEEP` carry the negative and positive
controls; `scan_lines()`/`scan()` report a hit as `surface/relative: detail`, so a failure names the file.

### Invariants And Boundaries

- No surface names a message-length number; the text points at the limit in the settings.
- Evidence, verdicts, lists and logs are files, named by the message that asks for or hands them over.

## Evidence

- The product surface inventory and the positive and negative controls qualify the wording oracle. [1]
- Roles, operations and templates must express the file-message contract. [2]
- Parentless compiled capsules exercise the shared producer and keep its file-message markers. [3]

- The implementation operation's markers are read from the delivered Worker text; every other surface states them in its own words. [4]

- The oracle keeps role-specific Reviewer and Curator alternatives with deletion and cross-role controls, and reads curation as both Curator and Manager capsules. [5]
