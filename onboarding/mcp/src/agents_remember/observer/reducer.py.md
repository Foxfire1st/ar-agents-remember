# mcp/src/agents_remember/observer/reducer.py

## Governing Overview

[overview.md](overview.md)

## Purpose

Pure event/snapshot interpretation into current worktree and analytical projections. Old recorded event kinds remain readable; removed lifecycle action and gate/inbox projection assembly is not restored.

## Code Commentary

project_workspace folds nonempty logs, keeps valid anchors, derives abandonment from abandoned enclosure truth without a foreign event append, and synthesizes paused persistent worktree lifecycles when there is no event log. Analytics and engine facts remain derived from supplied inputs. Recorded blocked/awaiting-developer kinds are interpreted even though nothing now writes them. Enclosure action availability is exactly integrate and cleanup with explicit prerequisite/refusal details; there is no lifecycle resume action. State-vocabulary/metrics ownership remains separate from client rendering and no inference is presented as a written signal.

`project_lifecycle` requires a nonempty append-ordered log seeded by lifecycle.started. Append-only `correction.recorded` rows index target event IDs and validated replacement states; malformed correction/state targets are ignored, and later valid corrections for the same target replace its indexed value. A correction is applied at the corrected event's original fold position, not as a new tail state override, so later events still win in order. The last log event owns lastEventTs before inference. Removal of model-facing session signals does not withdraw this durable audit interpretation.

## Evidence boundary

This account is current source interpretation only. It creates no executed test/host/bootstrap result and supplies no new CODE or MEMORY grade.

## Source-bound reference inputs

- [1]
- [3]
- [4]
- [5]
- [7]
- [8]
- [13]
- [14]
- [15]

- The reducer applies valid append-only corrections at their target event position, ignores malformed states and preserves later-event order. [16]
