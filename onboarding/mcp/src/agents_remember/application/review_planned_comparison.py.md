# mcp/src/agents_remember/application/review_planned_comparison.py

## Governing Overview

[Route overview](overview.md)

## Purpose

The application tier's composition point for the explainer routes: it re-exports the pure task-document helpers and binds the application adapters that the serving tier may not import.

## Code Commentary

- `explainer_application_ports` and `watcher_application_ports` are the only two values serving receives; the frame store, evidence preparation, lane classification, comparison and contract readers are named here and nowhere below, so the serving tier never imports upward.
- `task_frames_total` sums the task's frame area across every leaf against the task ceiling; a symlinked task store or a held frame answers `state: unavailable` with the reason and the limit rather than a partial total.
- `fresh_supplemental_receipts` re-admits each retained source: one that is now missing loses its digest and reads `unavailable`, a changed digest reads `changed`, and sources composed since are appended.
- Leaf documents are found by scanning the task folder's JSON files for one whose `id` is the leaf, and a leaf with no document yields no sources instead of an error.

## Evidence

- The application adapters reach serving as one injected value, not a module-global binding [1]
- A frame area that cannot be measured reports itself unavailable with its limit, not a partial sum [2]
- Re-admission marks a missing source unavailable and a changed one changed [3]
- The watcher's capture and lane ports are bound beside the explainer's own [4]
