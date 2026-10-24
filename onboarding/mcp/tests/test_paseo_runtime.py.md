# mcp/tests/test_paseo_runtime.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

Covers the Paseo runtime's own lifecycle as the CLI runs it: a fresh provision and a repeat that touches
nothing, replacing another version, reload or restart depending on what changed, a held port, a plugin
load failure, an interrupted pass, a rollback, and the process record and status/stop commands. Every
mutating call is observed, so a pass that changes nothing can be told from one that changed something.

## Code Commentary

### Logic

`PaseoRuntimeTests.provision()` runs the provision path and `provision_report()` reads what it decided;
`rerun()` provisions again with some settings facts changed and reports both the report and the
mutating calls, which is how each case separates a quiet read from a reload and from a restart.

- **Idempotence.** `test_fresh_provision_then_a_repeat_that_touches_nothing` and
  `test_reload_or_untouched_follows_what_changed` keep an unchanged pass inert and name what a changed
  one acts on; `test_a_running_daemon_restarts_for_what_only_a_start_applies` restarts only for the facts
  a start alone applies.
- **Failure leaves nothing behind.** `test_other_version_is_replaced_and_a_failed_install_changes_nothing`,
  `test_held_listen_port_fails_naming_it_and_leaves_nothing_running` and
  `test_a_rollback_undoes_only_what_the_pass_changed` keep a failed install, a held port and a rollback
  bounded to what the pass touched.
- **Convergence.** `test_a_pass_interrupted_at_any_call_converges_on_the_next` interrupts the pass at each
  call in turn and requires the next pass to converge.
- **Foreign state.** `test_provider_values_stay_in_the_daemon_file_and_a_refused_file_is_put_back` and
  `provisioned_with_foreign_keys()` keep keys only Paseo owns out of the product's hands and restore a
  refused file.
- **Process identity.** `test_a_process_record_is_acted_on_only_when_it_names_this_homes_supervisor` and
  `test_a_recorded_process_is_read_from_proc_and_one_that_cannot_be_read_is_never_signalled` bound a
  signal to a record naming this home's supervisor, and never signal a process that cannot be read.
- **Scope.** `test_status_and_stop_address_only_the_configured_home` and
  `test_commands_refuse_without_a_runtime_block_and_drop_paseo_environment` keep every command inside the
  configured home and refuse without a runtime block.
- **Plugin failure.** `test_plugin_load_failure_keeps_the_daemon_up_and_status_says_failed` leaves the
  daemon running and reports the plugin as failed.

### Conventions

Cases use `paseo_runtime_test_support` and `agents_remember_test_support.testing.waits`, and assert on
the recorded mutating calls rather than on a daemon's side effects alone.

### Invariants And Boundaries

- No pass signals or rewrites state outside the configured runtime home.
- A failed pass rolls back only the effects it owns: a failed install changes nothing, and a plugin-load
  failure keeps the running daemon up.

## Evidence

- Provision, reload, restart, failure, rollback, process-record, status and stop behaviour is asserted in this file. [1]
- The runtime cases are contract-sourced: each recorded call is checked against what the pass was allowed to do. [2]
