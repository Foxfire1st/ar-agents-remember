# mcp/tests/test_abandoned_series_closeout.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

Proves that an `abandoned` row needs no landing in an atomic master's closeout, that a recorded landing cannot be hidden
by that label, and that the chain, checkpoint and master-completion refusals name the master, row or contract cell they
are about and the action that clears them. It runs in the `unit-regression` lane.

## Code Commentary

### Logic

The `series` builder creates a scratch code repository, a series contract, one leaf document per row, and, for each
`Completed` row, a landing commit with a leaf enclosure whose integration is completed. Abandoned rows get a document and
no enclosure unless a case adds one.

- **Abandoned rows pass the closeout proof.** The parameterized witness uses 1 completed and 3 abandoned rows,
  and 50 completed and 7 abandoned rows, including an abandoned row with an empty file cell. Two abandoned rows have
  an enclosure whose cleanup is `abandoned` and whose integration is not completed. The master document is left byte-identical.
- **A landed abandoned row refuses by name.** An abandoned row whose enclosure records a completed integration refuses with
  the row named and the instruction to reconcile its status with its landing.
- **Other states still refuse.** A row that is `planning` refuses; an unreadable leaf document is named, never skipped; an
  all-abandoned master proves an empty chain and still refuses a foreign commit on the master's line; a master without
  abandoned rows closes as before.
- **Messages.** A row without a document file, two rows with the same document, a row that does not bind its leaf and a
  master with no rows each name the master, the row and `set_subtask`. An unordered chain names the leaf pairs and the
  `integrated_code_commit` cells. A leaf that did not land is named with `worktree_integrate`. A foreign enclosure keeps the
  status `atomic-series-leaf-contract-set-incomplete`. The checkpoint refusals name the master and the action.

### Conventions

- The cases call `require_closeout_publication_authority` and the checkpoint helpers directly on a scratch series.

### Invariants And Boundaries

- These cases prove that an abandoned row is outside the landing chain and that an abandoned row with a completed
  integration refuses by name (`worktrees/series_leaf_contracts.py`).

## Evidence

- Abandoned rows with no enclosure, an empty file cell and unlanded enclosures pass; the master document is unchanged. [1]
- An abandoned row that landed refuses with the row named. [2]
- A planning row and a non-abandoned row with an unreadable or missing document refuse by name. [3]
- An all-abandoned master proves an empty chain and refuses a foreign commit. [4]
- Malformed rows are refused with the master, the row and the action named. [5]
- Checkpoint refusals name the master and the action. [6]
