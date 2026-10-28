# mcp/src/agents_remember/canvas/explainer_state.py

## Governing Overview

[Route overview](overview.md)

## Purpose

One leaf's four durable explainer facts — the binding, the generation counter, the retired marker and the retire receipt — with the seat identity derived from them and the process tree a Retire must end.

## Code Commentary

- `ExplainerRefused` is the seat's own refusal shape: one reason a page or a tool can show and one actionable detail, always a value rather than a server error.
- `agent_id` derives the seat id from the workspace path and the generation with `uuid5` and never stores it, so a host that lost a create reply reconciles the same seat and a new generation cannot reuse an archived id.
- `raise_generation` raises the counter by one and answers the new value, under the caller's leaf lock; `restore_generation` puts it back after a failure that made no seat.
- `write_binding` replaces `binding.json` atomically, which is what lets a build and an Update write every other fact first and bind last.
- `process_tree` reads `/proc` only, matches both seat markers and every descendant, and refuses `explainer-process-tree-unavailable` rather than reporting an empty tree as a clean one.
- `end_processes` matches a recorded process by pid and start time, so a recycled pid is never signalled, sends SIGTERM and then SIGKILL, and returns what still answers alive for the receipt to report.

## Evidence

- A refusal carries a nameable reason and an actionable detail, never an untyped failure
- The seat id is derived from the workspace and the generation, so it is stable across a lost reply and never reused [2]
- The generation only grows, and a failed build puts it back to the value it had [3]
- The binding is replaced atomically, so a reader never sees a half-written environment [4]
- A host without `/proc` refuses by name instead of reporting an empty process tree [5]
- A process is the seat's only when its pid and start time match, and whatever survives is returned rather than assumed dead [6]

- Retired at the fifth freeze d59c3493: mcp/src/agents_remember/canvas/explainer_state.py:104-110 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 5f8398b32760677c370e3145add73cfa8388357b. Retired means the anchor no longer stands, not that the cited subject was deleted.
