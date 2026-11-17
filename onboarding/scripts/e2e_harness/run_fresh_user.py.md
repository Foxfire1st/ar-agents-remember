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

The module docstring states a clean-environment requirement and explains the host-versus-Dagger choice; that is a directive, not an independently established absence of machine-local reads. The current main composes the fresh-user scenario and writes the report to the separately supplied `--reports` destination. The earlier ambient `run.py` account is historical; it does not describe this entry point.

### Conventions

- Exit status is the run's verdict: non-zero when any invariant or checkpoint did not pass.
- The summary is printed for a human reading a terminal; the **JSON transcript is the evidence**,
  and the printed figures are read from the same report object rather than recomputed.
This module remains a **governed evidence artifact** with an `[[artifact]]` row in `mcp/tests/evidence-lifecycle.toml`. The current row names only `mcp/tests/test_fresh_user_harness.py` as its consumer.

### Invariants And Boundaries

- Fixture work is rooted at `run_root`; transcript output goes to the independently supplied `--reports` destination. No absolute filesystem-containment result is asserted.
- `--reports` is mandatory; the run root defaults to a temporary directory this run removes.
- The entry point does not certify anything by itself: it writes the transcript the acceptance is
  read from.

### Todos

None.

## Evidence

### Earlier card account and current limits

The card preserved at memory revision `81cfe4a89f5ffb222bd09640410d268d3fbef254` retained the source's reproducibility rationale: a fresh temporary run root and a recognizable transcript shape let a successor rerun the acceptance from the repository. The current source still states that rationale. Its host-versus-Dagger explanation is a **clean-environment directive**, not an independently established absence of machine-local reads.

The source states the host choice as a packet requirement for a clean environment rather than a Dagger graph. Its explanation that creating fixtures from nothing under the run root supplies “what the certification would have bought here” is retained as the module’s stated rationale, subject to the limits above.

The current module docstring still states “Nothing outside the run root is read or written” and “no machine-local state is consulted” (`run_fresh_user.py:6–7,11`). The earlier card also repeated those claims. They conflict with the current implementation: `main` writes to the independently supplied `--reports` destination and records `environment_facts()` (`:60–63`). The source wording therefore supplies no containment or isolation guarantee.

The earlier card referred to a pre-existing ambient `run.py` and named both `fresh_user_scenario.py` and `mcp/tests/test_fresh_user_harness.py` as consumers. Those are historical card claims, not the present entry-point or catalog account. The current route has no `run.py`, and the runner's catalog row names only `mcp/tests/test_fresh_user_harness.py` as its consumer.

The same earlier card said that the pre-existing ambient `run.py` “keeps its own Dagger admission for the ambient role-chat scenario” and “is not modified by this module.” Those are retained statements from that card, not a claim that this frozen tree contains that entry point or proves its historical Dagger admission.

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

This card uses repository-owned code and test references and invokes no sibling-repository contract.

### Repo-Internal References (continued)

- The entry point that drives the acceptance and writes the transcript. [1]
- `--reports` is required and `--work-root` is optional. [2]
- The transcript lands under this directory name. [3]
- [4]
- The shared writer for the transcript file. [5]
- The case pinning the argument contract. [7]

- HARNESS_DIR names the scripts directory and is inserted into sys.path as a string. The runner imports scenario and reporting through e2e_harness-qualified names. The lifecycle catalog declares mcp/tests/test_fresh_user_harness.py as the runner artifact’s one consumer. [8]
