# mcp/src/agents_remember/worktrees/integration/terminal_enclosure_archive.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/terminal_enclosure_archive.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T10:05+02:00|
| lastVerifiedCommitHash | `d36109038b3f2b500c138f9dc1ea9c9f9a247489` |
| lastVerifiedCommitDate | 2026-09-06T22:21:49+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Integration overview](overview.md)

## Purpose

Publishes a crash-safe terminal enclosure archive before destructive worktree-root cleanup.

## Code Commentary

### Logic

It proves terminal operations, resolved workers/mutations/publications, exact cleanup arguments, canonical manifest entries, receipt readback, and convergent retry after interrupted archive/unlink.

Since 260831-CCR (commit `99dc249b`) the canonical lifecycle root also owns the preserved legacy
missing-intent generation archives: `_LEGACY_MISSING_INTENT_RECORD` (line 52-55) matches
`closeout-operation.legacy-missing-intent-generation-{n}.json` /
`direct-landing-operation.legacy-missing-intent-generation-{n}.json`. `_canonical_entries`
(line 488-509) admits those names as owned artifacts (operation-record or missing-intent-record),
rejects anything else as `unowned artifact exists in canonical lifecycle root`, and parses the
archive as a `LifecycleOperationRecord` with `current=False` for the archive name (so the 
archived legacy generation is terminal/non-current-validated). The missing-intent archive is thus
carried into the immutable terminal archive beside the successor generation.

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

| Finding | Anchor | Source |
| --- | --- | --- |
| The current `_require_resolved_mutations` boundary implements the preparation contract above. | "def _require_resolved_mutations" | mcp/src/agents_remember/worktrees/integration/terminal_enclosure_archive.py:595-609 |

## Docs References

The configured Domain Documentation registry is empty. No external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain source is required to establish this repository-owned implementation. | `_OPERATION_RECORD` | mcp/src/agents_remember/worktrees/integration/terminal_enclosure_archive.py:1-889 |

## Repo-Internal References

The source file is the direct evidence for this unit; its governing overview records adjacent owners.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's concrete API, control flow, and validation boundary are implemented here. | `_OPERATION_RECORD` | mcp/src/agents_remember/worktrees/integration/terminal_enclosure_archive.py:1-889 |
| Missing-intent generation archives are owned canonical artifacts. | `_LEGACY_MISSING_INTENT_RECORD`; `_canonical_entries` | mcp/src/agents_remember/worktrees/integration/terminal_enclosure_archive.py:52-55; mcp/src/agents_remember/worktrees/integration/terminal_enclosure_archive.py:481-527 |

## Cross-Repo References

No cross-repository source is allowed by the resolved settings, and this unit owns no external
protocol claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repository reference applies. | `_OPERATION_RECORD` | mcp/src/agents_remember/worktrees/integration/terminal_enclosure_archive.py:1-889 |

## CCR-R02@v2 Terminal Archive Of Legacy Intent

The lifecycle store preserves a superseded missing-intent generation as
`*.legacy-missing-intent-generation-{n}.json`; this archive seam admits those files into the
canonical terminal archive so cleanup keeps the proof that the legacy bytes were preserved while a
canonical intent-bound successor replaced them. Part of the landed L25 candidate `99dc249b`.

## CCR-R18@v1 Observed-Exit Archive Guards

260831-CCR-L18 made `_require_archivable_operation` (line 531) consume the projection-owned worker-exit observation: it calls `project_worker_exit(record)` (from `worker/state.py`) once and passes that observed snapshot to `_require_absent_worker_authority` / `_require_resolved_worker_termination`, so the archive proof checks the same coherent worker observation the public projection shows instead of re-deriving worker authority twice from raw record cells. Archive admissibility semantics (absent worker binding and resolved termination before destructive cleanup) are unchanged.

## Update History

- 2026-09-06T23:07:14+00:00 — History-format repair at the actual recorded repair time. The earlier reconciliation note recorded only a local calendar date; its time of day is unknown. Original note preserved verbatim: "- 2026-09-07 — Reconciled the preparation contract introduced by 245057 against surviving d361 source; retained prior history and verification pins."


- 2026-09-04T10:05+02:00 — 260831-CCR-L18 Gate-5 memory pass: recorded the terminal-archive worker guards switching to the shared `project_worker_exit` observation. Verified at code commit f93ac631ca161e5880db3a937728cb256686b13b.

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for 99dc249bd507 (CCR-R02@v2/L25):
  the terminal enclosure archive now recognizes `*.legacy-missing-intent-generation-{n}.json` as
  an owned canonical artifact and archives it as a non-current operation record. Verified at code
  commit 99dc249bd507c20b09ece1169c2b1fa2af8e8c1b.

- 2026-08-25T15:44+02:00 — Created during PDLS whole-system reconciliation after source and
  requirement review. Verification remains closeout-owned.
