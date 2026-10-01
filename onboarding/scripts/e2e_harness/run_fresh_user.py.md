# scripts/e2e_harness/run_fresh_user.py

## Governing Overview

[scripts/e2e_harness/overview.md](overview.md)

## Purpose

The entry point for the fresh-user acceptance: two clean-room fixtures, one transcript.

```
python scripts/e2e_harness/run_fresh_user.py --reports <dir> [--work-root <dir>]
```

The run root is a fresh temporary directory unless `--work-root` names one, so a successor can
re-run this from the repository alone and read the same transcript shape. Nothing outside the run
root is read or written.

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

### Why it runs on the host rather than in the Dagger graph

The module states this deliberately: the packet carries a **clean environment** requirement, not a
Dagger-graph requirement. The fixtures are created from nothing under the run root and no
machine-local state is consulted, which is what the certification would have bought here. The
pre-existing `run.py` entry point keeps its own Dagger admission for the ambient role-chat scenario
and is not modified by this module.

### Conventions

- Exit status is the run's verdict: non-zero when any invariant or checkpoint did not pass.
- The summary is printed for a human reading a terminal; the **JSON transcript is the evidence**,
  and the printed figures are read from the same report object rather than recomputed.
- This module is a **governed evidence artifact** with an `[[artifact]]` row in
  `mcp/tests/evidence-lifecycle.toml` and real consumers in `fresh_user_scenario.py` and
  `mcp/tests/test_fresh_user_harness.py`.

### Invariants And Boundaries

- Nothing outside the run root is read or written.
- `--reports` is mandatory; the run root defaults to a temporary directory this run removes.
- The entry point does not certify anything by itself: it writes the transcript the acceptance is
  read from.

### Todos

None.

## Evidence

### Repo-Internal References

- The entry point that drives the acceptance and writes the transcript. [1]
- `--reports` is required and `--work-root` is optional. [2]
- The transcript lands under this directory name. [3]
- The acceptance the entry point drives. [4]
- The shared writer for the transcript file. [5]
- The existing Dagger-admitted entry point this module deliberately does not modify. [6]
- The case pinning the argument contract. [7]

### Cross-Repo References

No sibling-repository contract defines these values.

No meaningful cross-repo references found.
