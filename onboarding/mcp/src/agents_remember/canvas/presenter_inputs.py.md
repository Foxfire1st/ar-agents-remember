# mcp/src/agents_remember/canvas/presenter_inputs.py

## Governing Overview

[governing route overview](overview.md)

## Purpose

The presenter's launch choices, its design text and its instruction composition, kept apart from the attempt store so each can be refused and read in one place. Actual application of a launch belongs to the native receipt.

## Code Commentary

- `presenter_launch` reads the landed agentic settings under this capability's own key and records each choice's file and key; a permission-bearing choice outside the user's permitted sources is refused by name.
- `design_text` resolves the repository's text else the shipped default, refuses an unsafe, unreadable or over-2000-word text, and records its identity.
- `_compose_assignment` puts the capability text, a non-authority fence and the exact design bytes in front of the runner, so the design text can steer appearance and nothing else.
- `admit_retained` and `seed_from_revision` verify a retained revision's bytes before a regeneration starts from them.

## Evidence

- Launch choices come from the landed settings under this capability's key, with provenance. [1]
- The design text is resolved, bounded and fenced as non-authority. [2]
- The installed capability text is read from the shipped resource. [3]
