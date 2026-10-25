# mcp/tests/test_paseo_start.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

Covers the runtime start command as a state machine over one home: a running host is read-only, a live
but unanswering supervisor never gets a second start, a down home starts once, and concurrent starts share
one home lock and one owned outcome. Nothing here installs, configures or queries npm.

## Code Commentary

### Logic

`configured()` builds the runtime settings and configuration a start reads, and the cases drive the start
entry point with a fake daemon and the real settings reader.

- **Read-only when up.** `test_running_host_is_read_only_including_mismatches_and_session_names` answers
  from the running host, including the mismatch and session-name facts, with no start.
- **One start owns the home.** `test_down_states_start_only_once_and_never_install_configure_or_reload`
  starts a down home once and confirms the pass never installs, configures or reloads;
  `test_two_concurrent_starts_share_one_home_lock` proves two concurrent starts take one lock, and
  `test_contending_start_joins_the_same_owned_outcome_without_retry` proves a contender joins that owned
  outcome without retrying.
- **Refusals.** `test_a_live_unanswering_supervisor_never_gets_a_second_start`,
  `test_missing_or_wrong_install_and_occupied_port_do_not_start`,
  `test_no_shared_block_is_a_named_non_starting_state` and
  `test_incomplete_configuration_cannot_start_host_defaults` each name why no start happened.
- **Expiry and discovery.** `test_expired_start_reports_still_live_supervisor_and_does_not_duplicate_it`
  reports a still-live supervisor instead of duplicating it, and
  `test_start_and_status_never_query_npm_and_name_actual_discovered_config` proves start and status never
  call npm and name the configuration they actually discovered.

### Conventions

Cases use `paseo_runtime_test_support` and the bounded waits in `agents_remember_test_support.testing.waits`
so a stuck start fails as a name rather than as a hang.

### Invariants And Boundaries

- A start never installs, configures or reloads; it only starts what is already installed.
- One home lock means one owned outcome, and no case retries into a second start.

## Evidence

- A down home starts once and never installs, configures or reloads. [1]
- Two concurrent starts share one home lock. [2]

- A contending start joins the same owned outcome without retry. [3]

- Start and status never query npm and name the configuration they discovered. [4]
