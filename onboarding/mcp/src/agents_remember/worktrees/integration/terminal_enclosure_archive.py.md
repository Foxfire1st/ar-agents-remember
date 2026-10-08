# mcp/src/agents_remember/worktrees/integration/terminal_enclosure_archive.py

## Governing Overview

[Integration overview](overview.md)

## Purpose

Publishes a crash-safe terminal enclosure archive before destructive worktree-root cleanup. The reading and
proving of the canonical lifecycle root's evidence (`_canonical_entries`, the operation-record checks and the
bounded regular-file reader) is owned by the sibling `terminal_enclosure_evidence.py`; this module imports
`_canonical_entries`, `_read_regular_file` and `_sha256` from it and owns publication, receipt readback and
convergent retry.

## Code Commentary

### Logic

It proves terminal operations, resolved workers/mutations/publications, exact cleanup arguments, canonical manifest entries, receipt readback, and convergent retry after interrupted archive/unlink.

The canonical lifecycle root also owns the preserved legacy missing-intent generation archives:
`_LEGACY_MISSING_INTENT_RECORD` (in `terminal_enclosure_evidence.py`) matches
`closeout-operation.legacy-missing-intent-generation-{n}.json` /
`direct-landing-operation.legacy-missing-intent-generation-{n}.json`. `_canonical_entries` there
admits those names as owned artifacts (operation-record or missing-intent-record),
rejects anything else as `unowned artifact exists in canonical lifecycle root`, and parses each
record as a `LifecycleOperationRecord` with `current=False` for a generation or legacy archive name (so an
archived generation is validated as terminal and non-current). A record is accepted only when its content
matches the canonical file name it is stored under (`_require_record_matches_canonical_path`); a record
stored under a name that does not match it is refused. The missing-intent archive is thus
carried into the immutable terminal archive beside the successor generation. The same reader serves
`terminal_operation_evidence`, which the master-retirement readiness check uses to read retained operation
records without adopting them.

### Conventions

Typed records and refusal payloads remain owned at the narrowest stable boundary. Callers consume
the public function or model instead of re-deriving its lower-level state machine.

### Invariants And Boundaries

- Cleanup cannot remove the enclosure root until durable archive and receipt prove everything needed for later status/recovery; mismatched existing evidence refuses.
- Missing, unreadable, ambiguous, or conflicting authority fails loudly; this file does not add a
  fallback or compatibility shadow.
- The legacy missing-intent archive is an owned canonical artifact; the plain `.log`/generation
  forms are unchanged.

### Todos

None recorded.

### CCR private preparation boundary

Terminal archive refuses any operation retaining private preparation without an explicit retention disposition (`terminal-archive-operation-preparation-retained`). This check precedes ordinary pending-mutation checks: a terminal-looking status or absence of a Git mutation does not authorize deletion of named private outputs.

- The terminal preparation boundary refuses retained private preparation and ambiguous Git mutation intent. [1]

## Evidence

### Docs References

The configured Domain Documentation registry is empty. No external documentation claim is made.

- Repository-owned canonical lifecycle evidence defines terminal operation-record filename patterns. [2]

### Repo-Internal References

The source file is the direct evidence for this unit; its governing overview records adjacent owners.

- The public terminal archive entry publishes or re-observes the archive before deletion; the evidence owner admits and bounds canonical lifecycle files. [3]

- Missing-intent generation archives are owned canonical artifacts. [4]

### Cross-Repo References

No cross-repository source is allowed by the resolved settings, and this unit owns no external
protocol claim.

- Repository-owned canonical lifecycle evidence defines terminal operation-record filename patterns. [5]

- The archive builder takes the canonical lifecycle evidence from the evidence module. [6]
- A canonical operation record is parsed, must match its canonical file name, and must be archivable before it becomes an archive entry. [7]
- Retained operation records are read without adoption for the master-retirement readiness check, refusing any that cannot establish terminal authority. [8]

## CCR-R02@v2 Terminal Archive Of Legacy Intent

The lifecycle store preserves a superseded missing-intent generation as
`*.legacy-missing-intent-generation-{n}.json`; this archive seam admits those files into the
canonical terminal archive so cleanup keeps the proof that the legacy bytes were preserved while a
canonical intent-bound successor replaced them. Part of the landed L25 candidate `99dc249b`.

## CCR-R18@v1 Observed-Exit Archive Guards

260831-CCR-L18 made `_require_archivable_operation` (in `terminal_enclosure_evidence.py`) consume the projection-owned worker-exit observation: it calls `project_worker_exit(record)` (from `worker/state.py`) once and passes that observed snapshot to `_require_absent_worker_authority` / `_require_resolved_worker_termination`, so the archive proof checks the same coherent worker observation the public projection shows instead of re-deriving worker authority twice from raw record cells. Archive admissibility semantics (absent worker binding and resolved termination before destructive cleanup) are unchanged.
