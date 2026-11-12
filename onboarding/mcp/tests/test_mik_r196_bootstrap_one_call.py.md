# mcp/tests/test_mik_r196_bootstrap_one_call.py

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

The leaf's case set for MIK-R196 rules 1–3 and 11: one call starts Bootstrap, and the user settings are
written once. Each case protects one distinct operation — the free agent's admission through the same tables
the dashboard reads, the caller-harness mapping that decides its harness, the host-authority and role-settings
writes with their refusals, and the dashboard address a start answer carries — rather than a mock of those
surfaces. Every corpus lives in the test's own `XDG_CONFIG_HOME`, its own coordination root and its own MCP
settings file.

## Code Commentary

### Logic

- **The free agent (rule 1).** `test_bootstrap_is_a_launcher_role_with_no_document_and_no_parent` asserts
  `bootstrap` is a `LauncherRole`, one of `TASKLESS_ROLES`, and that its `PARENTLESS_START_SELECTIONS` entry is
  `(False, False, False)`. `test_a_bootstrap_selection_refuses_every_document_reference` accepts the empty
  selection and refuses each single sprint, master or leaf reference with "does not accept" (rule 2).
- **Overrides before dispatch.** `test_bootstrap_overrides_are_validated_before_dispatch_when_a_host_is_configured`
  drives `start_role` over the selection/configured/refused table: a configured host validates and then dispatches
  only when the selection is offered, a cold catalogue is bound to the caller's harness before validation, and a
  refusal stops at validation with no configuration write and no `tasks/` scaffold.
  `test_other_roles_still_refuse_a_model_without_its_agent` keeps that general rule for another role.
- **Caller harness (rule 1).** `test_the_caller_harness_maps_to_a_provider_or_to_nothing` covers `claude-code`,
  `Codex`, `hermes-agent`, `cursor-vscode`, an unknown name, no name and an empty catalogue: a name nothing maps to
  is never replaced by the first provider the host lists.
- **Host authority (rule 3, rule 11).**
  `test_the_host_authority_is_created_with_the_five_key_block` reads the created block back as exactly
  `installPrefix`, `home`, `listen`, `providers` and `embed`, with the initialisation marker and the recorded
  coordination root, and asserts the user settings file was not created (MIK-R137).
  `test_a_block_that_already_exists_is_never_rewritten` answers `present` with `changed: false` and identical
  bytes. `test_the_host_authority_is_added_to_a_file_without_one` keeps the file's own keys while adding the block.
  `test_a_symlinked_destination_is_never_written` refuses `destination-is-symlink` and leaves the link target empty.
- **Role settings (rule 11).** `test_role_settings_write_one_harness_per_role_and_read_back` writes one harness per
  role, including `bootstrap` and `architect`, leaves model and effort unset (rule 6), keeps `paseoRuntime` out of
  the user file, and reads the result back as `roleHarnesses`.
  `test_role_settings_on_an_existing_file_are_reported_not_written` reports `already-initialized` with the existing
  choices and identical bytes. `test_a_harness_the_host_does_not_run_is_refused_by_name` refuses
  `harness-not-hosted` and names the harnesses the host does run; `test_no_harness_chosen_is_refused` refuses
  `no-harness-chosen`; `test_a_preview_writes_nothing` keeps a dry run from creating the file.
  `test_the_initializer_refuses_a_destination_that_changed_after_its_preview` refuses `destination-appeared` and
  keeps the file that appeared. `test_the_initializer_reports_an_unreadable_file_instead_of_replacing_it` refuses
  `settings-unreadable` over the raw bytes, and `test_the_created_file_is_not_world_readable` asserts mode `0o600`.
- **The seat's address (rule 1).** `test_the_start_answer_names_the_dashboard_and_the_hosts_chat_route` reads the
  dashboard address, the host chat route for a server and agent, and the two named refusals for a missing runtime
  and a missing server id.
- **The scaffold predicate (rules 2–3).** `test_a_coordination_root_without_its_scaffold_is_not_prepared` walks
  `SCAFFOLD_ENTRIES`, and `test_a_bootstrap_request_carries_no_document_reference` keeps the request free of
  sprint, master, task and caller-harness fields.

### Conventions

The autouse fixture points `XDG_CONFIG_HOME`, `XDG_DATA_HOME` and `XDG_STATE_HOME` into the test's own
`tmp_path`, so the one user settings path is never the developer's. The host's harness catalogue is replaced at
`user_settings_init_module._runnable_harnesses`; the bootstrap override case also stubs the caller binding,
the selection validation and the dispatch endpoint, and everything else runs as shipped.

### Invariants And Boundaries

- A bootstrap selection carries no sprint, master or leaf, and no override is dispatched unvalidated.
- An existing host block, an existing user settings file and an unreadable or symlinked destination are reported,
  never rewritten.
- A created settings file holds only harnesses and carries no group or world read bit.
- These cases assert intent at the surface; they claim no live host, no launch and no acceptance.

## Evidence

- The free agent is a taskless, parentless launcher role and refuses every document reference.
- A configured override is validated before dispatch, and a refusal writes nothing and prepares no scaffold.
- The caller harness maps from its own name or to nothing, never to the first offered provider.
- The host authority is written once with its five keys and is read, not edited, when it already exists.
- Role settings are written once, read back, and left alone when the file already holds choices.
- The public refusals name their cause for an unhosted harness, no choice, an unreadable file, a symlinked
  destination and a destination that appeared after the preview.
- The address helper case constructs the dashboard URL and host chat route from explicit inputs and checks named missing-input reasons; it does not start a seat or inspect a registered start response. The registered response/created-identity assertion is in the separate delivery case.

- This address case invokes construction helpers with explicit server/agent inputs, while the separate registered delivery test requires returned identity and continuation to match its created seat; neither source reading is a native execution witness. [1]
