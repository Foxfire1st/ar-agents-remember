# mcp/tests/test_user_settings_guard.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

Holds the test-support guard that keeps a test from writing the user's real settings file (MIK-R135): with a
made-up account and no moved configuration folder the guard refuses and creates nothing, and every test file
and support module that reaches the settings path is required to go through it.

## Code Commentary

### Logic

`_fake_account()` replaces the account database answer and `HOME` with one made-up account, so the guard is
asked about a real-looking path that does not exist. `_run_outside_pytest()` runs a program the way a script
outside pytest does, and `_child_writer_program()` calls every writer the tests hold.

- **Refusal and permission.** `test_the_guard_refuses_the_made_up_real_path_and_creates_nothing` refuses;
  `test_the_guard_allows_a_moved_configuration_folder_and_creates_nothing` allows a moved
  `XDG_CONFIG_HOME` and creates nothing.
- **Without an account database.** The fallback compares against the earliest observed home and says so, and
  still allows a moved folder.
- **Truthful provenance.** `test_the_guard_reports_the_home_it_actually_observed` requires the refusal to
  name the observed home rather than a proven start.
- **The world in a child.** `test_building_the_world_with_the_users_own_environment_is_refused` builds the
  world in a child process on a made-up account and requires the failure and an empty fake home.
- **Rule 4 over support modules.** `_support_modules()` finds every support module without listing any by
  name, and `test_every_support_write_of_the_user_settings_goes_through_the_guard` fails a module that reaches
  the settings path; `_bound_callable_names()`, `_expression_strings()` and
  `_literal_settings_path_lines()` catch imported aliases and a path rebuilt literally, which
  `test_the_check_fails_a_support_module_that_writes_directly` and
  `test_the_check_fails_aliased_and_literal_bypasses` prove can fail.
- **Rule 3 over test files.** `_test_modules()` walks every test file however deep, and
  `test_every_test_file_reaches_the_user_settings_only_through_the_guard` plus
  `test_the_rule3_check_fails_a_test_file_that_writes_directly` and
  `test_the_rule3_check_fails_a_nested_test_file_that_writes_directly` prove the check reddens on a direct
  writer, nested included.
- **Every writer, cleared environment.** `_every_test_support_writer()` reads the writers from the code, and
  `test_cleared_environment_and_stopped_patches_still_refuse_every_writer` plus
  `test_writers_started_in_a_child_without_the_moved_folder_refuse` require each writer to refuse in a child
  with a cleared environment; `test_a_child_the_guard_did_not_stop_proves_no_refusal` refuses to read another
  error as a guarded refusal.
- **Leaks.** `_intact_teardown()` drives the `_user_settings_env_intact` fixture's teardown, and
  `test_the_intact_fixture_fails_a_leaked_environment` names the test that leaked the settings folder.

### Conventions

The checks are syntactic over the tree (`_python_files()` walks every Python file, bytecode caches left out)
and are proved able to fail before they are trusted.

### Invariants And Boundaries

- No test or support module reaches the user's settings path outside the guard, directly, by alias or by a
  rebuilt literal path.
- The guard refuses on the observed home; it never claims to know where an account started.

## Evidence

- The guard refuses a made-up real path, permits a moved `XDG_CONFIG_HOME`, and creates nothing. [1]
- Unreadable-database cases check the comparison and the truthful observed-home report. [2]
- The child executes the world source, refuses, and leaves the fake home empty. [3]
- The recursive population and syntactic checker hold the shared-support boundary. [4]
- Direct, imported-alias and literal-rebuild controls fail while guarded controls pass. [5]
