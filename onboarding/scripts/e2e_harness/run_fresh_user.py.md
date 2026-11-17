# scripts/e2e_harness/run_fresh_user.py

## Governing Overview

[scripts/e2e_harness/overview.md](overview.md)

## Purpose

The entry point for the fresh-user acceptance: two clean-room fixtures, one transcript.

```
python scripts/e2e_harness/run_fresh_user.py --reports <dir> [--work-root <dir>]
```

The run root is a fresh temporary directory unless `--work-root` names one. The acceptance fixtures use that root, while `--reports` independently selects the transcript destination `<reports>/fresh-user-acceptance/run.json`; the runner creates that destination and writes the report there. This runner does not establish an absolute no-I/O-outside-root guarantee.

## Code Commentary

### Logic

`arguments` requires `--reports` and leaves `--work-root` optional. `main` creates a
`tempfile.TemporaryDirectory(prefix="ar-fresh-user-")` when no work root was named, drives
`run_fresh_user_acceptance(run_root)`, attaches `environment_facts()`, and writes the transcript to
`<reports>/fresh-user-acceptance/run.json` through the shared `reporting.write_json`.

It then prints a one-line summary — `steps`, `invariants`, `blocked`, `failed` — plus one line per
failed invariant/checkpoint and one per blocked step, and returns **1** if anything failed, 0
otherwise. The temporary root is removed in a `finally` block, so a failed run leaves no fixture
behind.

`HARNESS_DIR` is inserted into `sys.path` as a **string**, not a `Path`: a non-`str` `sys.path`
entry is silently ignored by the import machinery, which would otherwise find nothing here and
report a missing module.

`HARNESS_DIR` names the scripts directory (`parent.parent` of this file). The runner imports `e2e_harness.fresh_user_scenario` and `e2e_harness.reporting` through that qualified route.

### Why it runs on the host rather than in the Dagger graph

The module docstring states a clean-environment requirement and explains the host-versus-Dagger choice; that is a directive, not an independently established absence of machine-local reads. The current main composes the fresh-user scenario and writes the report to the separately supplied `--reports` destination. The earlier ambient `run.py` account is retained below as superseded card wording; that file is absent from this frozen tree.

### Conventions

- Exit status is the run's verdict: non-zero when any invariant or checkpoint did not pass.
- The summary is printed for a human reading a terminal; the **JSON transcript is the evidence**,
  and the printed figures are read from the same report object rather than recomputed.
Retained earlier consumer caption:

- This module is a **governed evidence artifact** with an `[[artifact]]` row in
  `mcp/tests/evidence-lifecycle.toml` and real consumers in `fresh_user_scenario.py` and
  `mcp/tests/test_fresh_user_harness.py`.

Current catalog clause: the runner’s artifact row names only `mcp/tests/test_fresh_user_harness.py` as its consumer.

### Invariants And Boundaries

- Fixture work is rooted at `run_root`; transcript output goes to the independently supplied `--reports` destination. No absolute filesystem-containment result is asserted.
- `--reports` is mandatory; the run root defaults to a temporary directory this run removes.
- The entry point does not certify anything by itself: it writes the transcript the acceptance is
  read from.

### Todos

None.

## Evidence


Superseded card wording retained for custody (not certified as true of any source epoch or measured candidate):

> The run root is a fresh temporary directory unless `--work-root` names one, so a successor can
> re-run this from the repository alone and read the same transcript shape. Nothing outside the run
> root is read or written.

> - Nothing outside the run root is read or written.


> The module states this deliberately: the packet carries a **clean environment** requirement, not a
> Dagger-graph requirement. The fixtures are created from nothing under the run root and no
> machine-local state is consulted, which is what the certification would have bought here. The
> pre-existing `run.py` entry point keeps its own Dagger admission for the ambient role-chat scenario
> and is not modified by this module.


### Repo-Internal References

- The entry point that drives the acceptance and writes the transcript.
- `--reports` is required and `--work-root` is optional.
- The transcript lands under this directory name.

- The acceptance the entry point drives.

- The shared writer for the transcript file.
- The case pinning the argument contract.

- HARNESS_DIR names the scripts directory and is inserted into sys.path as a string. The runner imports scenario and reporting through e2e_harness-qualified names. The lifecycle catalog declares mcp/tests/test_fresh_user_harness.py as the runner artifact’s one consumer.

### Cross-Repo References

No sibling-repository contract defines these values.

No meaningful cross-repo references found.

- The entry point that drives the acceptance and writes the transcript. [1]
- `--reports` is required and `--work-root` is optional. [2]
- The transcript lands under this directory name. [3]
- [4]
- The shared writer for the transcript file. [5]
- The case pinning the argument contract. [7]

- HARNESS_DIR names the scripts directory and is inserted into sys.path as a string. The runner imports scenario and reporting through e2e_harness-qualified names. The lifecycle catalog declares mcp/tests/test_fresh_user_harness.py as the runner artifact’s one consumer. [8]
