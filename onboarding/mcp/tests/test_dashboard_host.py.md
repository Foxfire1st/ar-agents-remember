# mcp/tests/test_dashboard_host.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

Covers the dashboard host command: which serving mode ensures the Paseo host, which serves without
waiting for it, and what a supervised child does. It also holds the request-head budget: a dashboard read
of a 500-invariant card must fit the server's head limit in every serving mode.

## Code Commentary

### Logic

`config()` and `args()` build the runtime configuration and the command arguments a mode reads, and the
cases use `paseo_start`, `paseo_settings` and the bounded waits in
`agents_remember_test_support.testing.waits`.

- **Status.** `test_status_exit_codes_print_both_and_do_not_start` pins the status exit codes and the two
  printed facts, with no start.
- **Ownership.** `test_adoption_and_autostart_ensure_host_while_stop_does_not` keeps host ownership with the
  modes that ensure it and out of the one that stops.
- **Foreground and simulation.** `test_foreground_serves_without_waiting_for_host_and_sim_skips_it` keeps a
  foreground server serving before a host outcome and a simulation skipping the host entirely.
- **Request head.** `_card_read_head()` builds the request head of one card read naming the route's maximum
  of 500 invariants, and `_parsed_over_two_reads()` parses a head that arrives over two reads the way uvicorn
  feeds it; `test_a_500_invariant_card_read_fits_the_dashboard_servers_request_head_limit` requires the
  head to fit the dashboard's configured limit and shows the default h11 limit rejecting it.
- **Background and supervision.** `test_real_background_function_serves_before_host_outcome_and_logs`
  requires the real background helper to return before its controlled host outcome and to log that outcome
  afterwards, and `test_supervised_child_does_not_start_host_again` keeps a supervised child from starting
  the host a second time.
- **Discovery.** `test_discovered_config_path_is_named_in_normal_and_transition_outcomes` keeps the
  discovered configuration path explicit in both a normal and a transitional outcome.

### Conventions

Host outcomes are controlled through the fake daemon from `paseo_runtime_test_support`, and a case that
depends on ordering waits on the real helper rather than sleeping.

### Invariants And Boundaries

- A mode that does not own the host never starts it.
- The card-read head is measured as bytes, not as a rendered page.

## Evidence

- Status, adoption and stop, and foreground, reload and simulation keep host ownership and dispatch. [5]
- The 500-invariant head and the two-read parser exercise the configured and the default finite limits. [6]

- The real background helper returns before its controlled host outcome, then logs it. [7]


- A supervised child avoids a duplicate start, and a discovered settings path stays explicit in guidance. [8]
