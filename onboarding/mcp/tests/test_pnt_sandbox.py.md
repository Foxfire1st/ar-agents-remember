# mcp/tests/test_pnt_sandbox.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

Covers the PNT sandbox tooling (PNT-R11): the safety check's four cases — roots inside the sandbox pass, a root
outside it fails and is named, a root that cannot be resolved fails closed, and a root the build fills in by
default is caught — and what a build is given, including the tool server's environment and the admission that
keeps a sandbox from reaching another host.

## Code Commentary

### Logic

`SafetyCheckTests.judge()`/`found()` run the check against a reported root set, and
`test_build_roots_command_resolves_every_expected_root_without_errors` runs the real resolver command and
requires empty errors, every expected non-null root and the resolver's five keys. `REMOVED_EXACT`,
`REMOVED_BY_PREFIX`, `KEPT` and `RESOLVED_ROOTS` are the environment the build must lose and keep.

- **Safety.** `test_roots_inside_the_sandbox_pass`,
  `test_a_root_outside_the_sandbox_fails_and_is_named`,
  `test_a_root_that_cannot_be_resolved_fails_closed_and_is_named` and
  `test_a_root_the_build_fills_in_by_default_is_caught` cover the four cases, and
  `test_product_node_and_cache_roots_are_required_and_cannot_escape` keeps the product Node and cache roots
  required and inside the sandbox.
- **Build inputs.** `BuildInputTests` keeps a directory that is not a sandbox neither used nor deleted, replaces
  the marker whole when its state changes, allows a reset that could not delete everything to be repeated, keeps
  the settings to sandbox paths and the reserved ports, drops what selects another runtime from the environment
  while keeping logins, and catches a port held by anyone on any address.
- **Tool server.** `test_the_tool_server_receives_the_sandbox_environment` starts the tool server with the
  sandbox's own environment, its own `XDG` roots and no runtime selector, and
  `_helper_under_test()`/`_recording_stream()` observe whether a server was started at all.
- **Admission.** `test_a_resolved_host_outside_the_sandbox_is_refused_before_any_call`,
  `test_a_request_that_names_no_sandbox_is_refused`,
  `test_the_admission_refuses_a_server_with_configured_providers`,
  `test_a_sandbox_whose_settings_select_another_host_is_refused`,
  `test_a_host_outside_the_sandbox_refuses_in_the_unconfigured_phase` and
  `test_a_request_port_that_is_not_a_sandbox_port_is_refused` each refuse by name;
  `test_a_sandbox_that_records_no_host_yet_is_admitted_only_without_one` admits the unconfigured state and names
  it.
- **Receipts.** `test_public_host_install_receipts_keep_payloads_and_name_admission_failures` and
  `test_public_install_retires_success_for_cut_timeout_and_malformed` keep the retained receipt payloads and name
  a cut timeout or a malformed answer, and
  `test_launcher_provisions_from_the_compact_installs_named_report` reads the compact report's fallback and the
  inline host's precedence without changing the retained receipt bytes.

### Conventions

A case that needs a server records the stream it opens, so "nothing started" is an observation rather than an
assumption.

### Invariants And Boundaries

- A sandbox never reaches a host outside itself, and a port that is not a sandbox port is refused.
- A directory that is not a sandbox is never used or deleted.

## Evidence

- The sandbox safety check, build inputs, tool-server environment and admission. [1]
- The safety case for the product Node and cache roots. [2]
- The public install receipt cases. [3]
- The foreign-package admission case. [4]
- The real resolver command returns empty errors, every expected non-null root and five resolver keys. [5]
- Compact report fallback and inline-host precedence determine started bookkeeping without changing retained receipt bytes. [6]
- The tool server is started with the sandbox's own environment, including its own XDG roots and no runtime selector. [7]
- A resolved host outside the sandbox is refused before any call, naming both hosts. [8]
- A request that names no sandbox is refused before anything starts. [9]
- The admission refuses a server with configured providers after the `server_info` read. [10]
- A sandbox whose own settings select another home or the live port refuses. [11]
- The unconfigured state refuses a foreign resolved host. [12]
- A request port that is not a sandbox port is refused. [13]
- The unconfigured state is admitted and named, and a settings host the build cannot resolve refuses. [14]
