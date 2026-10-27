# mcp/tests/test_capsule_experiment_install.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

Runs the experimental installation and instruction cutover end to end: an unselected run installs the legacy
startup chain, a selected one cuts over to the capsule path and replaces an earlier legacy installation, and
the next unselected run restores the legacy chain because the selection is per run and never persisted. A
selected run with no usable capsule path refuses and writes nothing.

## Code Commentary

### Logic

`create_install_source()` builds one install source tree from this repository's canonical assets,
`dispatcherless_deps()` keeps the provider stack out, and `run_install()` runs the real installer through the
entry point the run selects. `CORPUS_FINGERPRINT`/`CORPUS_FINGERPRINT_SOURCE` and
`LEGACY_FINGERPRINT`/`LEGACY_FINGERPRINT_SOURCE` are real corpus text, so a zero count means absence rather
than drift; `fingerprint_count()`, `snapshot_regular_files()` and `files_containing()` measure the effective
material.

- **Two modes.** `test_an_unselected_run_installs_the_legacy_startup_chain`,
  `test_a_selected_run_cuts_over_to_the_capsule_path` and
  `test_a_selected_run_removes_an_earlier_legacy_installation` cover each mode and the replacement;
  `test_running_the_installer_again_without_the_selection_restores_the_legacy_chain` shows no global switch is
  left on.
- **Selection.** `test_an_unknown_experiment_is_refused_by_name`,
  `test_the_selection_resolves_from_the_request_then_the_run_environment` and
  `test_the_registered_tool_takes_the_selection_as_this_run_s_own_input` keep the selection an input of this
  run, and `test_the_selection_is_recorded_per_run_and_never_persisted` digests every regular file under the
  coordination root before and after.
- **Fail closed.** `test_a_selected_run_with_an_unavailable_capsule_path_refuses_and_writes_nothing` refuses
  instead of falling back.
- **One corpus copy.** `test_the_legacy_fingerprint_is_present_when_disabled_and_absent_when_opted_in` and
  `test_the_canonical_corpus_reaches_an_opted_in_run_once_through_the_capsule` count the corpus over the real
  effective material from two producers, and
  the historically named `test_the_installed_root_carries_the_canonical_corpus_only_as_authored_source`
  now asserts that the installed coordination root has no `skills/` tree and that startup targets remain
  withheld. The corpus is package-served rather than copied under the coordination root.
- **Record and dry run.** `test_the_run_record_carries_the_packet_shape_and_the_independent_version` and
  `test_a_dry_run_reports_the_cutover_and_writes_nothing` cover the record and the dry run.
- **Source tree.** `test_a_selected_install_writes_nothing_into_the_install_source_tree` keeps caches, manifests
  and generated state out of the tracked tree, and `test_the_rollback_plan_names_the_restore_command` names the
  restore command.
- **Earlier installs.** `test_an_install_over_an_earlier_experimental_installation_fails_on_none_of_its_stores`
  keeps what an earlier build left and fails on none of it.

### Conventions

Facts are read from the retained logged install result and from digests of the tree, not from the installer's
returned summary alone.

### Invariants And Boundaries

- The selection belongs to one run; nothing under the coordination root records it afterwards.
- A selected run never falls back to the legacy chain.

## Evidence

- The no-persistence guard digests every regular file under the coordination root before and after the selected run. [1]

- A selected install leaves no coordination-root skill tree or received startup targets; the corpus remains package-served. [2]

- The registered tool takes the selection as this run's own input and the record names the input that won. [3]

- Private machine settings pre-exist both installations and retain their bytes. [8]

- Selected-run facts are asserted from the retained logged whole result. [9]


- The module drives the real installer end to end and reads its results back from the files it wrote: the legacy-to-capsule cutover, the per-run selection record and the rollback plan, with the install source tree left byte-identical. [4]


The present test module no longer contains that test or asserts those installed-application facts; the earlier witness is retained at its original source epoch, not claimed as a current regression case.

- The current rollback test names the AGENTS.md restore row and its no-experiment restore command, and compares the payload rollback paths with those rows. [5]




> Retained earlier citation wording: - The current settings-guard and portable Node-lockfile artifact rows both declare test_capsule_experiment_install.py as a consumer. The original two-row addition account belongs to its prior source epoch; these declarations establish no invocation.





> Retained earlier citation wording: - The current settings-guard and portable Node-lockfile artifact rows both declare test_capsule_experiment_install.py as a consumer. The original two-row addition account belongs to its prior source epoch; these declarations establish no invocation.










- The current settings-guard and portable Node-lockfile artifact rows both declare test_capsule_experiment_install.py as a consumer. The original two-row addition account belongs to its prior source epoch; these declarations establish no invocation. [6]


- The current settings-guard and portable Node-lockfile artifact rows both declare test_capsule_experiment_install.py as a consumer. The original two-row addition account belongs to its prior source epoch; these declarations establish no invocation. [7]
