# mcp/tests/test_capsule_experiment_install.py

## Governing Overview

[overview](overview.md)

## Purpose

Runs the experimental installation and instruction cutover end to end: neither an unselected nor a selected run
leaves the retired startup files (`AGENTS.md`, `tasks/AGENTS.md`, `system/AGENTS.md`) in the coordination root,
an earlier installation's copies are removed in both modes, and a selected run cuts over to the capsule path. The
selection is per run and never persisted. A selected run with no usable capsule path refuses and writes nothing.

## Code Commentary

### Logic

`create_install_source()` builds one install source tree from this repository's canonical assets,
`dispatcherless_deps()` keeps the provider stack out, and `run_install()` runs the real installer through the
entry point the run selects. `plant_retired_startup_files()` writes the three retired startup files carrying
`LEGACY_FINGERPRINT` as an earlier installation would have left them, and `assert_no_retired_startup_files()`
requires all three absent, symlinks included. `CORPUS_FINGERPRINT`/`CORPUS_FINGERPRINT_SOURCE` and
`RETIRED_CORE_FINGERPRINT` are real corpus text, so a zero count means absence rather than drift;
`fingerprint_count()`, `snapshot_regular_files()` and `files_containing()` measure the effective material.

- **Two modes.** `test_an_unselected_run_leaves_no_retired_startup_files` (with and without an earlier
  installation), `test_a_selected_run_cuts_over_to_the_capsule_path` and
  `test_a_selected_run_removes_an_earlier_legacy_installation` cover each mode and the removal;
  `test_running_the_installer_again_without_selection_keeps_retired_files_absent` shows no global switch is
  left on, and `test_an_unselected_preview_reports_retirement_without_removing_files` reports the removals on a
  dry run without touching a file.
- **Selection.** `test_an_unknown_experiment_is_refused_by_name`,
  `test_the_selection_resolves_from_the_request_then_the_run_environment` and
  `test_the_registered_tool_takes_the_selection_as_this_run_s_own_input` keep the selection an input of this
  run, and `test_the_selection_is_recorded_per_run_and_never_persisted` digests every regular file under the
  coordination root before and after.
- **Fail closed.** `test_a_selected_run_with_an_unavailable_capsule_path_refuses_and_writes_nothing` refuses
  instead of falling back.
- **One corpus copy.** `test_both_install_modes_remove_the_legacy_fingerprint` and
  `test_the_canonical_corpus_reaches_an_opted_in_run_once_through_the_capsule` count over the real effective
  material: the legacy fingerprint is gone from both modes and no corpus text lands in the coordination root,
  and `test_the_installed_root_carries_the_canonical_corpus_only_as_authored_source` asserts that the installed
  coordination root has no `skills/` tree and that startup targets remain withheld. The corpus is
  package-served rather than copied under the coordination root.
- **Record and dry run.** `test_the_run_record_carries_the_packet_shape_and_the_independent_version` and
  `test_a_dry_run_reports_the_cutover_and_writes_nothing` cover the record and the dry run in both modes.
- **Source tree.** `test_a_selected_install_writes_nothing_into_the_install_source_tree` keeps caches, manifests
  and generated state out of the tracked tree, and `test_an_actual_install_reports_no_startup_rollback` finds an
  empty startup rollback in the selected run's payload.
- **Earlier installs.** `test_an_install_over_an_earlier_experimental_installation_fails_on_none_of_its_stores`
  keeps what an earlier build left and fails on none of it.
- **Benchmark sync.** `test_benchmark_asset_sync_retires_the_same_startup_files` shows the benchmark runner's
  runtime-asset sync removes the same three files, writing nothing on its dry run.
- **Module statement.** `test_the_module_states_that_an_unselected_install_still_retires_startup_files` requires the
  `install/experiment.py` docstring to say that an unselected (`legacy`) run keeps the old startup chain's install
  path while the cutover still retires the `AGENTS.md` copies, and not to call `legacy` the existing installation
  left unchanged.

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


- The module drives the real installer end to end and reads its results back from the files it wrote: removal of the retired startup files in both modes, the capsule cutover and the per-run selection record, with the install source tree left byte-identical. [4]


- An actual selected install reports an empty startup rollback and leaves no retired startup file. [5]

- The retired startup files are planted with the legacy fingerprint and must all be absent afterwards. [10]
- An unselected run removes planted startup files. [11]
- Its preview reports the planted startup files without removing any. [12]
- The module docstring must say that an unselected (`legacy`) run keeps the old startup chain's install path while the cutover still retires the `AGENTS.md` copies. [13]
- The benchmark asset sync retires the same startup files. [14]




- The current lifecycle catalog declares test_capsule_experiment_install.py among the exact consumers of mcp/tests/_user_settings_guard.py, mcp/tests/fixtures/repository_profiles/node/package-lock.json. These current declarations establish no invocation or addition event. The `fixtures/repository_profiles/node/package-lock.json` artifact row declares `test_capsule_experiment_install.py` as an exact consumer. [6]




- The current lifecycle catalog declares test_capsule_experiment_install.py among the exact consumers of mcp/tests/_user_settings_guard.py, mcp/tests/fixtures/repository_profiles/node/package-lock.json. These current declarations establish no invocation or addition event. The `fixtures/repository_profiles/node/package-lock.json` artifact row declares `test_capsule_experiment_install.py` as an exact consumer. [7]
