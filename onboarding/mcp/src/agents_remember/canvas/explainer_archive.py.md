# mcp/src/agents_remember/canvas/explainer_archive.py

## Governing Overview

[Route overview](overview.md)

## Purpose

What a master retirement or a sprint archive does to every explainer environment of one task: retire each seat under its own lock, then reclaim the folders the cleanup removes.

## Code Commentary

- `environments` names a leaf by its workspace folder, by its generation counter, or by both, and holds a symlinked entry of the task's explainer folder instead of reading anything behind it.
- `retire_environments` retires one environment at a time; a dry run answers `would-retire` or `already-retired` for each and touches no seat, process or file.
- `_retire_one` takes the leaf lock and re-reads the environment under it, so a state that moved between the listing and the retirement is seen rather than acted on stale.
- A step that does not finish leaves the receipt `pending`, never `failed`: a repeat of the same retirement finishes the same receipt by the agent id, generation and tree it recorded.
- `remove_environment` keeps a workspace and its counter whenever a retire is pending or the leaf's own state cannot be read, and asks a caller-supplied admit to refuse any path whose confinement fails.
- `host_seat_archive` answers no callable when no host is configured, and treats a host that knows no such agent as already done, so an unreachable host leaves a pending receipt instead of stopping the retirement.

## Evidence

- A leaf is discovered by its workspace folder, its generation counter, or both, and a symlinked entry is held rather than followed [1]
- A dry run classifies each environment and mutates nothing [2]
- A workspace and its counter are kept while a retire receipt is pending or unreadable [3]

- A configured host archive failure leaves the retirement receipt pending; a host that reports the agent already absent is done, and an installation with no configured host supplies no archive callback [4]

- Every explainer seat a coordination root holds is nameable without a live host, so a restart resumes none of them [5]

- A configured host archive failure keeps the retirement receipt pending; no configured host supplies no archive callback, and an agent reported absent is already done. [6]
