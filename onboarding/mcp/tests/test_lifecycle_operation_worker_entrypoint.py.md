# mcp/tests/test_lifecycle_operation_worker_entrypoint.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_lifecycle_operation_worker_entrypoint.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T20:55+02:00 |
| lastVerifiedCommitHash | `77bc614506b8b50937aed6846523547d36045947` |
| lastVerifiedCommitDate | 2026-08-24T20:41:34+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

Pins the detached lifecycle worker’s parser, `main`, and installed script entrypoint to task addressing and process declaration before service use.

## Code Commentary

### Logic

One end-to-end-focused test invokes all three entry seams. It proves the worker derives private operation state from the task contract instead of accepting an operation key/PID address, declares its process identity before constructing services that may write the journal, and exits successfully for an already-cancelled record without replaying work.

### Invariants And Boundaries

- Public process argv contains task address and operation kind, not a private record path.
- Writer declaration precedes any lifecycle store update.
- Cancelled work is observed, not relaunched or mutated.

## Docs References

See task `260821-CLIVE-L1` L1-R4 and L1-R5.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Parser, main, and installed script use task addressing and declare the worker before services. | `test_worker_parser_main_and_script_entry_use_task_addressing` | `mcp/tests/test_lifecycle_operation_worker_entrypoint.py:21-77` |
| Production entrypoint dispatches task-addressed durable execution. | `main` | mcp/src/agents_remember/application/lifecycle/lifecycle_operation_worker.py:485-488 |

## Cross-Repo References

No cross-repository boundary applies.

## Update History

- 2026-08-24T20:55+02:00 — No content impact: the owned-state context manager moved from the test
  tree to `agents_remember.testing.global_state`; worker-entrypoint behavior is unchanged.

- 2026-08-24T00:27+02:00 — 260821-CLIVE-L2 committed-route reconciliation: citation-only repair repointed moved lifecycle, tool-model, direct-landing, legacy, or startup evidence to its canonical committed source path; this card's own documented behavior is unchanged.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: created from accepted candidate tree `4241908c`; first verification stamp remains governed-closeout-owned.
