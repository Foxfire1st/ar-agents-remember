# IAS Source-Pair Coordination Memory State

| Field | Value |
| --- | --- |
| workflow | c-03 existing-memory-slice-maintenance + c-05 file-level onboarding |
| state | ready-for-handoff |
| change kind | direct IAS architecture repair; no task or master artifact |
| source inventory | architect-supplied approved architecture plus current IAS production diff |
| production units | frozen inventory: 32 changed/new MCP Python source files, 6 changed canonical skill files, 6 synchronized package-data skill copies, and 1 changed reference document |
| test/support units | frozen inventory: 22 changed/new focused test files, including 6 final edge suites |
| route overviews | new worktrees, activation, c-09, and affected child/public/docs/lifecycle routes reconciled to the frozen candidate |
| route indexes | 75 routes generated from the frozen code/onboarding roots; final preview reports 0 writes and 0 stale indexes |
| entity catalog | affected queue, ledger, lineage, contract, and integration ownership reconciled; real-commit fingerprints remain closeout-owned |
| verification | exact 67/67 changed-source mapping and deterministic memory integrity checks pass; architect-supplied Dagger pass 13 is recorded without a curator execution claim |
| handoff | ready |

## Approved Architecture Being Preserved

- Task authoring is wholly upstream and never waits on activation or queue state.
- One disposable source-pair activation snapshot selects the currently exposed atomic master;
  multiple live series contracts are normal, and changing selection pauses rather than retires the
  previous series.
- A selecting operation publishes `reconciling`, completes the exact source-pair sync, and only
  then publishes `active` for implementation admission.
- Mid-task sync is a contract-addressed journaled transaction. Genuine conflicts stay in an
  operation-owned worktree for agent resolution and can be continued or explicitly cancelled.
- The sync journal is stable below the worktree-enclosure root and remains readable independently
  of task-document health.
- The closeout queue is a disposable scheduling projection. It owns no commit, claim,
  certification, lifecycle, integration, or recovery evidence.
- Terminal cleanup releases only the exact selected terminal contract; a paused series cannot
  clear a newer selection.
- Readers fail closed. No compatibility or fallback reader is introduced for activation or sync
  authority.

## Current Boundaries

The architecture statements above are approved current intent and are reconciled to the frozen
candidate. Verification hashes and entity fingerprints for uncommitted sources remain closeout
work and must not be invented. The final curator pass refreshed generated route indexes from the
explicit code/onboarding roots and completed deterministic exact-set, governing-link, citation,
table-shape, and patch-integrity checks.

## Remaining Closeout-Owned Facts

- Stamp refreshed cards with the actual landed code commit/date only after that commit exists.
- Recompute entity fingerprints whose evidence sets gain the new activation/sync owners from the
  actual committed Git blobs.

## Next Recommended Action

Architect reviews this curated memory candidate, commits code, performs the real-commit stamp and
entity-fingerprint refresh, then commits memory. No curator-actionable onboarding repair remains.
