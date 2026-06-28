# mcp/src/agents_remember/observer/worktree_provider_admission.py

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `mcp/src/agents_remember/observer/worktree_provider_admission.py` |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-06-28T05:38+02:00                                      |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`                  |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `overview.md`                                               |

## Governing Overview

[observer overview](overview.md)

## Purpose

`worktree_provider_admission.py` centralizes active-enclosure admission for
worktree-scoped runtime projection. It separates the stricter provider-alarm
boundary from the broader Engine Room boundary: worktree providers/setup progress
are operational only for active provider-relevant lifecycle phases, while engine
process facts may still project for any non-terminal enclosure lifecycle.

## Code Commentary

### Logic

`admitted_worktree_groups(enclosures, lifecycle_logs, *, now)` folds lifecycle
logs with `project_lifecycle`, joins each enclosure by `lifecycleId`, rejects
terminal lifecycles, rejects cleanup-completed/abandoned enclosures, rejects
closeout/integration-completed enclosures, and admits only provider-relevant
phases (`request`, `trust-checkpoint`, `reframe-research`, `decide`, `build`).
The returned values are worktree group basenames, matching provider-runtime file
layout and the served `ProviderNode.worktreeGroup`.

`active_enclosure_worktree_groups(enclosures, lifecycle_logs, *, now)` uses the
same lifecycle map but keeps any non-terminal enclosure lifecycle whose cleanup
has not completed. Projection uses this broader set to avoid git-probing engine
facts for historical enclosures while still showing active close/integration
work in the Engine Room.

`_project_lifecycle_map` is the shared fold helper; `_enclosure_is_provider_relevant`
is the provider-specific contract-status gate.

### Conventions

The module receives already-read `EnclosureNode`s and lifecycle event logs. It
does not read contracts, provider-runtime files, or observer logs itself; those
remain owned by `snapshots.py` and `projection_store.py`.

### Invariants And Boundaries

- Provider alarms are admitted before provider nodes reach the reducer; the reducer
  still treats admitted provider failures as real.
- Worktree provider-state files alone are not operational truth.
- Engine-process admission is intentionally broader than provider admission so
  non-terminal close/integration work can stay visible without paging provider alarms.
- Group joins always use the worktree group basename.

### Todos

No file-local todos.

## Docs References

No relevant external documentation was found after checking the in-repo design docs.
This file implements repository-local worktree lifecycle admission policy.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found after checking in-repo design docs for active-enclosure admission. | n/a | n/a |

## Repo-Internal References

The projection store consumes both admission sets: strict provider groups for
provider/setup readers and broader active enclosure groups for Engine Room facts.
Focused projection tests pin active provider admission, parked/terminal/provider-phase
rejection, and close-phase Engine Room visibility.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Provider admission folds lifecycle logs, joins enclosures, rejects terminal/non-provider phases, and returns worktree group basenames. | L18-L36 | [worktree_provider_admission.py](worktree_provider_admission.py) |
| Broader active-enclosure groups keep non-terminal cleanup-pending lifecycles for Engine Room status reads. | L39-L57 | [worktree_provider_admission.py](worktree_provider_admission.py) |
| Projection uses strict groups for provider/setup reads and broad groups for engine process facts. | L151-L180 | [projection_store.py](projection_store.py) |
| Admission tests pin active provider groups, parked/terminal/close-phase provider rejection, and close-phase Engine Room group retention. | L169-L258 | [test_observer_projection.py](../../../tests/test_observer_projection.py) |

## Cross-Repo References

No meaningful cross-repo references found. This is an internal observer admission
boundary over local coordination state.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->

- 2026-06-28T05:38+02:00 — Created for task 29: extracted worktree-scoped provider
  admission and broader active-enclosure group derivation so stale provider-runtime
  files and historical enclosure contracts do not page or slow the dashboard. Verification
  metadata pinned until closeout stamps the task-29 code commit.
