# mcp/tests/test_capsule_experiment_install.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_capsule_experiment_install.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-17T10:20:31+00:00|
| lastVerifiedCommitHash | `58bf4cde0f5271bbe420ad8e045d18b433f11253` |
| lastVerifiedCommitDate | 2026-09-17T12:31:16+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[tests route overview](overview.md)

## Purpose

The forcing suite for the experimental installation and instruction cutover (260915-CAPS-L9): **19
cases** that drive the real installer against scratch coordination roots and read the resulting
tree, the returned run record and the compiled capsule text. It is the proof surface for behaviour 2
(the per-run recorded selection with no silent switch), behaviour 3 (the cutover and its
deduplication screens) and behaviour 5 (the run record and the way back).

This module is **new in 260915-CAPS-L9** and is **uncommitted on `ar/260915-caps-l9-ar`**; it is not
one of the six lane-manifest `D9` modules (its row is registered and the loader names the same six as
at the clean base), and its two consumer rows in `mcp/tests/evidence-lifecycle.toml` are the measured
catalog delta this leaf contributes.

## Code Commentary

### What each case class is protecting

- **The cutover pair and its positive control.** `…an_unselected_run_installs_the_legacy_startup_chain`
  and `…a_selected_run_cuts_over_to_the_capsule_path` are two real installs in two scratch roots; the
  disabled run is the control for the opted-in one, and `…a_selected_run_removes_an_earlier_legacy_installation`
  proves the removal half rather than only the withholding half.
- **The way back is executable.** `…running_the_installer_again_without_the_selection_restores_the_legacy_chain`
  runs the documented undo as a run, not as prose.
- **The selection surface.** `…the_selection_resolves_from_the_request_then_the_run_environment` and
  `…the_registered_tool_takes_the_selection_as_this_run_s_own_input` drive the registered payload
  builder and assert `selectionSource == "request"` for a request-supplied selection and `legacy`
  with no record for an unselected one; `…an_unknown_experiment_is_refused_by_name` pins the refusal
  vocabulary.
- **Fail-closed refusals write nothing.** `…a_selected_run_with_an_unavailable_capsule_path_refuses_and_writes_nothing`
  and `…a_pin_mismatch_refuses_the_install_and_names_the_capability` assert both the named capability
  and the absence of a created coordination root.
- **The deduplication and delivery screens.** `…the_legacy_fingerprint_is_present_when_disabled_and_absent_when_opted_in`
  counts the four coordinator `AGENTS.md` targets **on disk**; `…the_canonical_corpus_reaches_an_opted_in_run_once_through_the_capsule`
  reads the trusted instruction text the production compile route produces; and
  `…the_installed_root_carries_the_canonical_corpus_only_as_authored_source` reads the **installed**
  coordination root instead of compiling a second time, which is the screen that says what the
  installed `skills/` copy actually is.
- **The record and the rollback plan.** `…the_run_record_carries_the_packet_shape_and_the_independent_versions`
  compares the record against the pinned `package.json` rather than against the product's own output,
  and `…the_rollback_plan_names_the_installed_artifacts_and_the_restore_command` pins the rendered
  undo rows.
- **The no-persistence guard, which is the case `S2`'s strengthened text names.**
  `…the_selection_is_recorded_per_run_and_never_persisted` **content-digests every regular file under
  the coordination root** before and after the selected run and inspects every file that appeared or
  changed; the root-scoped reading demands that every hit be a **byte-identical authored asset**,
  with a control that the scan found something at all. It replaced a first revision whose guard was
  `rglob("*.json")` and therefore blind to a `.toml`, a `.txt` or an extension-less switch — the
  baseline review's `L9-1`, whose four seeded channels (`S12` `.json`, `S12b` `.toml`, `S12c` `.txt`,
  `S12d` extension-less) plus the deselected-install seed `S12e` the case now catches.
- **The install stays inside its destination.** `…a_selected_install_writes_nothing_into_the_install_source_tree`
  and `…the_installed_application_keeps_its_machine_local_trees_out_of_the_mirror` (which asserts the
  installed `node_modules` is a real directory and not a symlink).

### Invariants And Boundaries

- The suite drives the **real** installer entry points against scratch roots; it does not assert on
  the live coordination root.
- Every case that claims a count names the producer of each side; no case presents two different
  producers' numbers as one measurement.
- Seed coverage lives in `notes/reports/caps-l9-mutation-probe.py` (24 caught, 0 vacuous), not in
  this module.
- Failures are never smoothed: the `L9-1` vacuity is recorded as the reason the guard is
  root-scoped rather than as a silent edit.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The no-persistence guard digests every regular file under the coordination root before and after the selected run. | `test_the_selection_is_recorded_per_run_and_never_persisted` | mcp/tests/test_capsule_experiment_install.py:449-515 |
| The installed root's corpus is measured as authored source rather than compiled a second time. | `test_the_installed_root_carries_the_canonical_corpus_only_as_authored_source` | mcp/tests/test_capsule_experiment_install.py:516-542 |
| The registered tool takes the selection as this run's own input and the record names the input that won. | `test_the_registered_tool_takes_the_selection_as_this_run_s_own_input` | mcp/tests/test_capsule_experiment_install.py:543-584 |
| The installed application keeps machine-local trees out of the mirror and its `node_modules` is a real directory, not a symlink. | `test_the_installed_application_keeps_its_machine_local_trees_out_of_the_mirror` | mcp/tests/test_capsule_experiment_install.py:607-639 |
| The rollback plan renders the installed artifacts and the restore command. | `test_the_rollback_plan_names_the_installed_artifacts_and_the_restore_command` | mcp/tests/test_capsule_experiment_install.py:640-666 |
| The two consumer rows this leaf adds to the catalog's consumer proof. | `test_capsule_experiment_install` | mcp/tests/evidence-lifecycle.toml:624-624 |
| The lane manifest registers this module without adding a seventh `D9` row. | `test_capsule_experiment_install` | mcp/tests/test-evidence-lanes.toml:19-19 |

## Update History

- 2026-09-17T10:20:31+00:00 — 260915-CAPS-L9 curator: **created.** The candidate adds the module
  (666 lines, 19 cases, untracked). The card records what each case class protects — including the
  root-scoped no-persistence guard that replaced the vacuous `.json`-only first revision, the
  three separately-labelled deduplication/delivery screens, and the real-directory assertion on the
  installed `node_modules` — and the lane/catalog rows the module contributes. Verification metadata
  names the leaf base commit because the candidate is **uncommitted**; the real stamp is
  closeout-owned.
