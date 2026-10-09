# mcp/tests/tool_log_witness.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

The reproducible L108 sandbox witness driver (MIK-R108 E4/E7, rule 3): hermetic two-world run binding the frozen bytes to observed log behavior — worker calls in enclosure logs, controller calls at the coordination root, successful public abandon and cleanup with parsed root lines — asserting every proof before writing, so a frozen evidence file only ever binds a passing run.

## Code Commentary

### Logic

- World A proves abandon: force-abandon removes the enclosure whole, its line lands at the root, enclosure logs are gone and never recreated. World B proves cleanup through preview/apply/integrate/finalize plus an outlived-group call logging at the root without recreating the folder.
- `main` records timestamped before/after snapshots, every call's outcome and log location, run provenance (code head, tracked diff, per-file digests, invocation, environment) and the final repository state, and exits nonzero on any failed proof.
- Run from the leaf code root with the test-support and source trees on `PYTHONPATH`, writing the evidence file path argument.

### Invariants And Boundaries

- Fail-loud: no evidence file is written for a failing run.
- The driver is run by hand, not by the suite; the suite pins its helpers (see `test_witness_driver_helpers.py`).

## Evidence

- The driver runs both worlds, asserts every proof, then writes provenance. [1]
