# mcp/src/agents_remember/canvas/explainer_binding.py

## Governing Overview

[Route overview](overview.md)

## Purpose

The launch's explainer binding: the capability word, the four explainer-owned tools, the validated workspace association and the seat-identity checks, kept importable by both the launch and the registration.

## Code Commentary

- `EXPLAINER_SURFACE` names the four explainer-owned tools added beside AR’s general tools. Dispatch uses it to apply launched-seat validation to those four calls; general AR tools retain their ordinary admission.
- `validate_explainer_binding` refuses a binding that misses a required field, that names another capability, or whose generation is not a positive integer.
- `_check_workspace` refuses a workspace that is not `<coordination>/explainer/<repository>/<task>/<leaf>`, one that resolves outside the named coordination root, one whose task folder is absent, and one that is a symlink or not on disk.
- `require_current_seat` derives the seat id from the workspace and the current generation counter, so a stale generation, a marker pointing at another workspace, an unreadable counter and a caller with no identity are each refused by their own name.
- `require_launched_seat` compares what the calling process is with what the binding names. The server applies that check to the four explainer-owned tools, so no tool argument, repository text or workspace marker widens their binding or selects another seat.
- `read_explainer_binding` refuses a missing binding on a process that carries the workspace marker: a lost binding is not the ordinary roster. The explainer’s four own tools are `render`, `define_category`, `remove_category` and `grade`; they add no workspace read-back tool. Their bounded answers name files on disk, so a long answer or a picture is written to the workspace and cited rather than returned in full.

## Evidence

- A binding missing a required field, naming another capability or carrying a non-positive generation is refused [2]
- The workspace must be the exact explainer placement of that repository, task and leaf, and must exist as a real directory [3]
- The caller's id must be the one this workspace and its current generation derive [4]
- A missing binding on a marked explainer process is refused rather than read as an ordinary process [6]

- This constant names the four explainer-owned additions; dispatch uses it to select the calls that require launched-seat validation [1]
- A call to an explainer-owned tool from another seat, another workspace or a superseded generation is refused, and no argument widens its binding [5]
