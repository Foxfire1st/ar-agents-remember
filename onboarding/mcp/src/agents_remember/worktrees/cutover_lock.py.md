# mcp/src/agents_remember/worktrees/cutover_lock.py

## Governing Overview

[worktrees route overview](overview.md)

## Purpose

Unconverted memory is read and converted, not operated on by an ordinary check, write, memory sync,
closeout or landing (MIK-R46). The caller establishes the legacy input; this module refuses it
unconditionally. Converted memory elsewhere changes recovery wording, never admission.

## Code Commentary

### Logic

`cutover_lock_refusal` returns no refusal only when there is no repository to judge: an absent path,
a non-directory, or a definite non-repository. An actual legacy memory repository receives the
central `legacy_format_refusal` even when it has never converted. The message identifies the
operation and line, absent `knowledge/layout.json`, and two recovery routes: `worktree_sync` with
`merge-memory` from a converted source, or the first conversion in `c-13-install-and-onboard` and
`docs/guides/first-conversion.md`.

`converted_memory_location` looks at local branch tips, then registered worktrees. `_converted_branch`
asks for the marker at every tip in one `cat-file --batch-check`; `_converted_worktree` checks actual
working-tree marker files. These probes never make the legacy lock conditional. `legacy_format_refusal` creates one `LegacyFormatCase` where the existing probe runs and returns a text-equal `LegacyFormatRefusal` carrying that value. Both the complete central sentence and the caller’s recovery step derive from this same case: a named converted line permits the merge-memory recovery, no converted memory selects first conversion, and unknown/error supplies no next step. The caller does not parse any diagnostic text or run a second probe to choose the case.

`_is_repository` accepts only a definite non-repository as false. A `.git` entry at this path or a
parent, or bare-repository `HEAD` and `objects`, prevents a failed rev-parse from being treated as
absence. `_git` turns command failure, timeout and OS errors into `CutoverProbeError`.

### Invariants And Boundaries

- Unanswered Git probes refuse by name, never as unlocked or legacy; conversion does not repair an unreadable object.
- Converted/converting candidates retain their existing validator and gate; marker presence is not a validation PASS.
- Missing, unreadable or corrupt memory retains its own error rather than being classified as legacy.
- `is_legacy_format_refusal` recognizes the central code-bearing message; callers use it to preserve the no-write refusal envelope without changing other blocker persistence.
- Card writes (`citation_fix`, route-index apply) now require converted memory too. The old `citation_migrate` tool and `memory-citations --migrate` option are unregistered; implementation deletion remains MIK-R65.
- DEC-FCNRNT and DEC-VMMJDN retain the historical conditional trigger and card-writer exception; MIK-R46 deliberately supersedes those permissions. No switch or repository-wide conversion census decides admission.

## Evidence

### Docs References

No Domain Documentation source is configured. The task authority is MIK-R46@v2 under D39(b)/D47,
which deliberately supersedes the earlier cutover-window exception. No live external evidence is claimed.

### Repo-Internal References

- Unconditional legacy refusal, named probe error, and definite non-repository boundary. [1]
- Converted locations inform recovery but never unlock an ordinary legacy operation. [2]
- Local branch marker probe in one batch. [3]
- Registered working-tree marker lookup. [4]
- The unchanged central text carries the single probe-made case used for conversion guidance. [5]
- Only a definite non-repository reads as absent. [6]
- Structural repository evidence prevents false absence. [7]
- Failed or timed-out Git probes stay named. [8]
- Leaf route names its own memory line. [9]
- Public routes refuse with or without converted memory elsewhere. [10]
- A converting candidate is gated, not legacy-locked. [11]
- Plain directory and unanswered repository probes have distinct outcomes. [12]

### Cross-Repo References

The module probes the caller's one memory repository through Git. No additional cross-repository authority is claimed.
