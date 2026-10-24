# mcp/tests/test_capsule_serving_surface.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

Covers the shipped capsule surface: the real corpus parses and every served skill has a root revision, the
composition manifest and the serving plane agree on one identity, the server's index resource and the
extension's own entries are complete, and a real client drives the real server over stdio. Containment,
index, naming and idempotence guards are each reached with a seeded mutation.

## Code Commentary

### Logic

`_live_settings()` and `_server_parameters()` build the documented argv in a disposable coordination root with
this worktree's source, `_drive_exchange()` runs one client session against the real server, and
`_drive_extension_methods()` issues the extension's methods over the transport its declaration rode in on.

- **Shipped corpus.** `test_the_shipped_corpus_parses_and_every_served_skill_has_a_root_revision` requires
  frontmatter, a body digest and a readable URI per skill.
- **Identity.** `test_the_composition_manifest_declares_the_skill_that_is_served` keeps the two planes agreeing
  on skill identity and origin.
- **Entries.** `test_this_servers_own_index_resource_keeps_the_agent_skills_discovery_shape` pins this server's
  index resource, and `test_every_sep_2640_entry_is_complete_and_carries_verbatim_frontmatter` checks the
  extension's entry shape against the tree rather than against itself.
- **The real exchange.** `test_a_real_client_and_server_exchange_over_the_installed_sdk` drives the entry point
  over stdio with the installed SDK's client; `test_the_mutation_harness_can_actually_fail` proves the evidence
  can fail.
- **Containment.** `test_the_server_process_never_serves_a_file_outside_a_skill_directory` requires a traversal
  URI to be refused by the running server rather than normalized into a read, and
  `test_a_catalog_record_that_escapes_its_skill_directory_is_refused` reaches the same refusal through a record.
- **Guards.** `test_the_index_reader_refuses_while_a_skill_cannot_be_served`,
  `test_a_skill_whose_directory_name_disagrees_with_its_name_is_recorded_not_served` and
  `test_the_extension_declaration_is_installed_once_per_server` reach the index, name and idempotence guards.
- **Altitude.** `test_altitude_admission_admits_every_role_the_document_can_carry_and_refuses_the_rest` and
  `test_the_capsule_operation_serves_every_seat_its_document_can_carry` keep admission with the task layer rather
  than a hardcoded role name, `test_a_nested_skill_is_published_flat_like_any_other` permits nesting with flat
  publication, and `test_old_role_compile_input_returns_the_canonical_investigator_with_one_notice` keeps the
  legacy rename to one notice.

### Conventions

Cases that need a live server start the real entry point; a guard case seeds the exact defect it claims to
catch, so no guard passes without being reached.

### Invariants And Boundaries

- Nothing outside a skill directory is served, in the process, whatever the URI says.
- Admission is the task layer's rule; the serving surface does not hardcode roles.

## Evidence

- The split contract: surface cases here, worlds and vocabularies imported. [1]
- Shipped corpus, manifest identity, index shape and entry completeness. [2]
- The real stdio exchange and its client-observed checks. [3]
- Live-server traversal refusal and the harness-can-fail sanity check. [4]
- Seeded-mutation guards: containment, index, name rule and idempotence. [5]
- Altitude admission, capsule seats, nesting and the legacy rename. [6]
