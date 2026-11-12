# mcp/tests/test_mik_r196_settings_init_preserves_existing.py

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

User settings initialization as one exclusive create, with an existing file left alone. The cases seal MIK-R196
rule 11 in L188-B03, L188-B04 and L188-B07: the surface creates a role-harness settings file only where there is
none, so every pre-existing destination — marked by this product or not — keeps its raw bytes and its mode; there
is no replacement step and no temporary sibling path; and the public answer is a modeled refusal that never
re-reads the file that refused and never needs a live host to report what an existing file holds.

The corpus lives in the test's own `XDG_CONFIG_HOME` and its own coordination root. The developer's real settings
file is never touched.

## Code Commentary

### Logic

- **An existing destination is reported as it stands (B03).**
  `test_an_existing_marked_file_is_reported_and_kept_byte_for_byte` keeps a `settingsInit` marked file with its
  own role choice: `already-initialized`, `changed: false`, `preservedKeys` naming both keys, a "never
  overwrites" detail, and identical bytes and mode.
  `test_an_existing_file_without_role_choices_is_not_completed` reports empty `roleHarnesses`, `initializable:
  false`, and leaves the unrelated content alone — absent choices are reported, never filled in.
  `test_the_existing_file_is_reported_before_any_choice_is_validated` makes the existing file answer while the
  harness catalogue raises, so no host and no catalogue is asked anything (B07).
- **The one write, on an absent destination (B03).**
  `test_an_absent_destination_is_created_exclusively_with_the_chosen_roles` writes only `orchestration`, one
  harness-only row per role, at mode `0o600`.
  `test_a_preview_of_an_absent_destination_writes_nothing` reads `state: preview` through the public payload and
  asserts neither the file nor a temporary sibling exists.
- **No sibling path, no chmod-then-replace, no followed link (B04).**
  `test_a_sibling_init_symlink_is_neither_followed_nor_truncated` plants `.<name>.init` as a symlink to a victim
  file: the surface still creates the destination, the victim keeps its bytes and `0o644` mode, the sibling stays a
  symlink and the destination is a regular file.
  `test_a_destination_present_at_write_time_is_refused` refuses `destination-appeared` through `_write_after_preview`
  with `existed=False`. `test_a_destination_that_appears_after_the_state_read_is_refused` makes the first state read
  see nothing and the write decide on what is on disk now, refusing the same code.
  `test_the_exclusive_create_refuses_a_destination_the_existence_check_missed` blinds `Path.exists` and
  `Path.is_symlink` for the target: `O_EXCL` still refuses `settings-not-writable` and the file keeps its bytes.
- **The public answer refuses once (B07).** `test_the_public_answer_refuses_an_unreadable_file_without_a_second_read`
  answers `ok: false`, `state: refused`, `settings-unreadable`, the file's path and a next action, with no file
  content in the answer and unchanged bytes. `test_the_public_answer_refuses_the_old_location_collision` answers
  `settings-location-upgrade-required` with the upgrade detail, never reads the old file for a migration and creates
  no new one. `test_the_public_answer_reports_existing_choices_without_a_live_host` reads the existing choice while
  the catalogue raises. `test_the_public_answer_refuses_a_symlinked_destination` answers
  `destination-is-symlink` and leaves the target. `test_the_host_block_is_refused_by_name_not_written_into_the_user_file`
  answers `host-authority-not-in-user-settings` naming the MCP authority file, and creates no user file (MIK-R137).

- **Discovery distinguishes unknown from known-empty offerings.**
  `test_discovery_unknown_passes_value_and_known_names_use_paseo_labels` previews a Worker choice of
  `MY Choice`. With no provider answer, the configured spelling is retained; with the host row
  `{id: "native-id", label: "My Choice"}`, the same choice resolves to `native-id`; an answered empty
  provider list refuses the choice as unavailable. The test uses `dry_run=True` and the same temporary
  settings fixture as the existing cases.

### Conventions

`_config` builds a config whose coordination root is the test's, `_write` creates a destination at `0o640` and
`_assert_untouched` is the shared byte-and-mode assertion. The host catalogue is replaced at
`user_settings_init_module._runnable_harnesses`; the read, exclusive create and post-preview write helpers are
reached at their own module attributes so each guard is tested where it lives.

### Invariants And Boundaries

- An existing settings file is read and reported; it is never merged, completed, replaced or chmod-ed.
- The write exists only for an absent destination, is exclusive, and leaves no temporary sibling.
- A refusal names its code, path and next action, carries no file content and does not re-read the file.
- The host authority block belongs to the MCP settings file, never to the user's file.
- These cases own the surface only; they claim no live host and no installation acceptance.

## Evidence

- An existing marked file and an existing unmarked file are both reported unchanged, in bytes and mode.
- An existing file answers before any harness choice is validated, with no live host.
- An absent destination is created exclusively with harness-only role rows at mode `0o600`.
- A sibling `.<name>.init` symlink is neither followed nor truncated, and a destination that appears is refused.
- `O_EXCL` refuses a destination the existence check missed.
- The public answer refuses an unreadable file, an old-location collision, a symlinked destination and a host-block
  request by name, without a second read and without creating a file.

- Unknown provider offerings retain the configured spelling; known host labels resolve to their IDs and known-empty offerings refuse. [1]
