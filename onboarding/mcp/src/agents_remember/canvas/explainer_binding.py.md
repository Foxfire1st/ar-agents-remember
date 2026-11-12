# mcp/src/agents_remember/canvas/explainer_binding.py

## Governing Overview

[Route overview](overview.md)

## Purpose

The launch's explainer binding: the capability word, the closed tool surface, the validated workspace association and the seat-identity checks, kept importable by both the launch and the registration.

## Code Commentary

- `EXPLAINER_SURFACE` is the closed list of tools a binding may discover or call, and both discovery and dispatch check it, so a direct call by name is refused as well as omitted from the roster.
- `validate_explainer_binding` refuses a binding that misses a required field, that names another capability, or whose generation is not a positive integer.
- `_check_workspace` refuses a workspace that is not `<coordination>/explainer/<repository>/<task>/<leaf>`, one that resolves outside the named coordination root, one whose task folder is absent, and one that is a symlink or not on disk.
- `require_current_seat` derives the seat id from the workspace and the current generation counter, so a stale generation, a marker pointing at another workspace, an unreadable counter and a caller with no identity are each refused by their own name.
- `require_launched_seat` compares what the calling process is with what the binding names, so no tool argument, repository text or workspace marker widens a binding or selects another seat.
- `read_explainer_binding` refuses a missing binding on a process that carries the workspace marker: a lost binding is not the ordinary roster. The explainer surface is four tools - `render`, `define_category`, `remove_category` and `grade` - and no tool that reads the workspace back: an answer names files on disk and is bounded, so a long answer or a picture is written to the workspace and cited rather than returned in full.

## Evidence

- This constant is the surface a binding may discover or call, and it is the one list discovery and dispatch both check [1]
- A binding missing a required field, naming another capability or carrying a non-positive generation is refused [2]
- The workspace must be the exact explainer placement of that repository, task and leaf, and must exist as a real directory [3]
- The caller's id must be the one this workspace and its current generation derive [4]
- A call from another seat, another workspace or a superseded generation is refused, and no argument widens the binding [5]
- A missing binding on a marked explainer process is refused rather than read as an ordinary process [6]
