# mcp/test_support/agents_remember_test_support/testing/coordination_wording.py

## Governing Overview

[overview](overview.md)

## Purpose

The module holds the expected current coordination and curation clauses, keyed by the lifecycle-skill file that must carry each one. It is independent data: it reads no file and carries no matcher.

## Code Commentary

Keys are paths relative to `skills/l-01-agent-lifecycles` (role files, operation files, core files, `SKILL.md` and the curator memory-handover reference). `mcp/tests/test_role_instruction_wording.py` collapses whitespace in each canonical file and in each clause and requires every clause to occur in its keyed file. A clause here states required wording only; matching it is a wording check, not semantic acceptance.

## Evidence

- The single registry maps each lifecycle-skill file to the clauses it must carry. [1]

- The module holds data only: it imports nothing and reads no file. [2]
