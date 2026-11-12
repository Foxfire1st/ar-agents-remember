# mcp/tests/test_role_message_wording.py

## Governing Overview

[overview](overview.md)

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
- **Delivered text.** `message_step()` reads each role's file-message rules only through their declared
  delivery of `reference/message-handover.md`, and `template_message_text()` follows each handover template's
  two action pointers to that file's sender and full-store sections, so the marker check reads what a seat
  actually receives.
- **Held delivery.** `assert_held_shared_delivery()` requires the held-receipt clauses in `core/authority.md`
  and exactly once in the shared block every compiled messaging role receives, with per-clause deletion and
  duplication controls.
- **Role-specific equivalents.** `missing_markers()` keeps common marker equivalents and Reviewer and Curator
  marker alternatives, and
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

`message_step` reads the actual role/operation-aware shared detail instead of concatenating raw Worker prose or a Curator-only payload file. Reviewer direct-verdict ownership is checked in the review operation's intake-and-verdict section, and retired duplicate verdict directions fail reinsertion controls in the Reviewer's review-artifacts section. Six curation handoff targets must resolve to exact headings; Bootstrap keeps its no-message own-chat route, and pointer/declaration/audience/step/action mutations fail. These are source assertions/support behavior, not a fresh invocation, host result or AR acceptance.

## Evidence

- The product surface inventory and the positive and negative controls qualify the wording oracle. [1]

- Roles, operations and templates must express the file-message contract. [2]

- The parentless compiled-text helper collects each selected role's prompt and handover. The compiled-capsule test obtains the role's declared message step, combines that detail with its prompt for the file-message markers and scans both prompt/detail and serialized handover for forbidden wording. [3]

- Message-file markers are checked through the declared shared message step for role and addressed-operation surfaces, and through each handover template's action pointers to the message-handover reference. Operation checks visit every declared recipient, including Worker implementation and Curator/Manager curation, and compiled prompt checks combine the role text with its delivered detail. [4]

- The oracle keeps Reviewer- and Curator-specific file-message marker alternatives and requires each current delivered shared-step facet. Deleting a real marker must fail, and each role's alternatives must fail on unrelated surfaces. Declared operation recipients include both Curator and Manager curation; pointer, declaration, audience and step mutations must also fail. [5]

- `message_step` reads the actual role/operation-aware shared detail. Reviewer direct-verdict ownership is checked in the review operation's intake-and-verdict section, and retired duplicate verdict directions fail reinsertion controls. Six curation handoff targets must resolve to exact headings; Bootstrap keeps its no-message own-chat route, and pointer/declaration/audience/step/action mutations fail. These are source assertions/support behavior, not a fresh invocation, host result or AR acceptance. [6]
