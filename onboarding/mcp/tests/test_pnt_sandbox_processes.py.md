# mcp/tests/test_pnt_sandbox_processes.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

Covers the PNT sandbox tooling's process side (PNT-R11): start, stop, reset, the lock and the process records. A
start refuses a checkout that is not a PNT build, a reserved port held by a foreign process or a running daemon
without the sandbox environment, and a start that fails half way stops what it started and names the step that
failed.

## Code Commentary

### Logic

`StartAndStopTests.start()`/`stop()` run the sandbox tool against a sandbox from
`pnt_sandbox_test_support`, and `open_files()` reads what a process's descriptors point at, skipping one it closed
since the listing.

- **Refusals.** `test_start_refuses_a_checkout_that_is_not_a_pnt_build`,
  `test_start_refuses_a_reserved_port_held_by_a_foreign_process`,
  `test_start_refuses_a_running_daemon_that_lacks_the_sandbox_environment` and
  `test_start_starts_nothing_when_the_safety_check_fails` each refuse before anything starts.
- **Idempotence.** `test_start_reports_already_running_and_changes_nothing` and
  `test_two_starts_at_once_leave_one_sandbox_that_stop_ends` keep one sandbox whatever the concurrency.
- **Build.** `test_start_builds_a_missing_sandbox_first` builds a missing sandbox first, and
  `test_deferred_install_cannot_qualify_an_older_live_host` keeps a deferred install from qualifying an older
  live host.
- **Failed starts.** `test_a_start_that_fails_half_way_stops_what_it_started`,
  `test_a_failed_start_whose_runtime_cannot_be_stopped_says_so_and_keeps_its_record`,
  `test_a_provision_without_a_report_is_undone_only_when_it_started_the_daemon` and
  `test_a_failed_start_names_the_step_that_failed` bound the undo and name the failure.
- **Stop.** `test_stop_signals_only_the_process_start_recorded` signals only the recorded process, and
  `test_a_dashboard_the_record_does_not_name_is_reported_and_keeps_the_directory` reports an unnamed dashboard
  and keeps the directory.
- **Identity and lock.** `test_one_directory_is_one_sandbox_however_it_is_spelled` and
  `test_the_lock_covers_a_build_and_a_provision_run_and_is_the_file_that_is_there` keep identity path-based and
  the lock the file that is there.
- **Records.** `test_the_paseo_home_record_is_trusted_only_for_this_homes_supervisor` and
  `test_a_stale_paseo_record_is_deleted_before_any_runtime_command` trust a record only for this home's
  supervisor and delete a stale one before any runtime command.

### Conventions

Each case starts real processes and asserts on the process table and descriptors, so a signal that went to the
wrong pid is visible.

### Invariants And Boundaries

- A failed start leaves nothing running that it started, and keeps the record it cannot clean.
- One directory is one sandbox, however the path is spelled.

## Evidence

- Start, stop, reset, the lock and the process records through the real tooling. [1]
- The rebuild case over the sandbox layout. [2]
- The deferred-install reporting case. [3]
