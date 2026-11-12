# mcp/src/agents_remember/worktrees/integration/terminal_enclosure_evidence.py

## Governing Overview

[Integration overview](overview.md)

## Purpose

The one bounded reader and terminal-authority prover for an enclosure's canonical lifecycle evidence. The terminal
enclosure archive (`terminal_enclosure_archive.py`) publishes what this module reads, and the master-retirement
readiness check reads the same evidence through `terminal_operation_evidence` without adopting anything. It was split
out of `terminal_enclosure_archive.py` to keep that file under the size limit; the proofs it carries are the archive's.

## Code Commentary

### Logic

`_canonical_entries(location, contract_path, operation=...)` walks the canonical lifecycle directory in name order. It
skips lock and log files, accounts for a pre-move sync journal as removed working state (only when that journal is in a
terminal sync state; otherwise it refuses and names `worktree_sync` cancel), refuses any file it does not own as an
unowned canonical artifact, and turns each owned file into a `TerminalEnclosureArchiveEntry` through
`_canonical_evidence_entry`. The owned names are the enclosure manifest, the adoption receipt, the operation records
`closeout|integrate|direct-landing-operation[.generation-N].json` and the legacy missing-intent archives
`closeout|direct-landing-operation.legacy-missing-intent-generation-N.json`. The archive is bounded to 1,024 files and 64
MiB, and an archive with no evidence refuses.

`_canonical_evidence_entry` reads the file as one regular non-symlink file, and for an operation record parses it as a
`LifecycleOperationRecord`, requires the record to match the canonical file name it is stored under
(`_require_record_matches_canonical_path`), and requires it to be archivable (`_require_archivable_operation`): terminal
status, no retryable cleanup disposition for the current generation, no worker authority or unresolved worker
termination (read from the projection-owned worker-exit observation), no private preparation retained, no ambiguous
mutation intent, and no unresolved integration claim or door publication. A record whose content does not match its
name is refused.

`terminal_operation_evidence(group)` reads every recognized current, historical and legacy-intent operation record under
`<group>/.lifecycle` with the same schema, reader and checks, for the operation `worktree_abandon`, and under the same
bounds. A missing directory has no retained records. A record that cannot establish terminal authority is raised as
`terminal-operation-evidence-refused`, naming the file.

### Conventions

- Refusals are typed (`LifecycleOperationLocationError`) with the expected and observed facts.
- The module reads only; it publishes and deletes nothing.

### Invariants And Boundaries

- A retained operation record is accepted only when its content matches the canonical file name it is stored under.
- Evidence that could still hold recovery authority (non-terminal, active worker, retained preparation, ambiguous
  mutation, an active sync journal) is never archived and never read as terminal.

## Evidence

- The canonical root is walked, unowned files refused, a terminal sync journal accounted for, and the bounds enforced. [1]
- An operation record must match its canonical file name and be archivable before it becomes an entry. [2]
- A pre-move sync journal is archived only as removed working state, and only when terminal. [3]
- The archivability proof combines the terminal, retry, worker, mutation and publication checks. [4]
- Retained operation records are read without adoption and refused by name when they cannot establish terminal authority. [5]
- A record stored under a name that does not match its content is refused. [6]
