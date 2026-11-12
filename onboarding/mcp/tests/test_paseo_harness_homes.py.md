# mcp/tests/test_paseo_harness_homes.py

## Governing Overview

[overview](overview.md)

## Purpose

Proves that a Paseo host provision never stops a running host whose inherited harness storage variables (such as `CODEX_HOME`) would change on restart, unless the user keeps the values, moves them into provider settings or accepts the change, and that the values stay out of logs, Paseo calls, the process record, status and successful answers; the refusal's own detail names each variable with its running and new value.

## Code Commentary

The cases drive `harness_home_status`, `require_preserved_harness_homes`, `provision_runtime`, `provision_with_home_change`, `runtime_status` and the daemon start path against `paseo_runtime_test_support.FakePaseo`, with process facts that carry `harness_homes`. Status reports only the inherited variable names; a variable already set in `providers.<id>.env` is not inherited. A changed value refuses with `harness-home-would-change`, a JSON detail of running and new values, and a message naming the same-values, settings and `--accept-harness-home-change` remedies; the refusal comes before any `daemon stop` or signal, including in the failed-start cleanup path of `_start_daemon`. Each of the three remedies then lets the provision restart the host. An unreadable process environment reports `inheritedHarnessHomes: "unknown"`, adds no new refusal, and leaves the existing `process_record_unverifiable` refusal intact in provision and in the CLI `status` command. The settings parser keeps provider `env` maps unchanged, and the catalog of home variable names includes the Codex, Claude and Pi variables. Everything runs on test-owned roots with a fake host.

## Evidence

- Status names inherited variables without values; settings env or same values or acceptance pass; a change refuses with the remedies [1]
- An unknown environment is reported and adds no refusal; the home variable catalog [2]
- A home change refuses before any stop, and each of the three remedies allows the restart without leaking the value [3]
- The settings parser does not rewrite provider environments [4]
- An unreadable environment reports unknown and keeps the process-identity refusal [5]
- Failed-start cleanup checks homes before its stop [6]
- The guard under test [7]
