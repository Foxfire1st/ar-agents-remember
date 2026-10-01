# mcp/tests/test_terminal_paste.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Uses injected tmux operations, log evidence and a stepped clock to test safe paste/submission. Log-confirmed success avoids pane capture, an unwritable buffer never presses Enter, and an unobservable pane blocks repaste. Retry submits a visible matching draft once but leaves unrelated or historical-marker drafts pending. These six cases are not a live tmux acceptance suite.

## Code Commentary

### Logic

The current evidence boundary is the source-listed behavior below. Earlier coverage claims in
history describe prior populations and must not be used to recreate removed tests or claim they
still run. The retained behavior and its fixture limits, described above, govern this card.

### Conventions

The table lists retained test definitions, not collected parametrized or subtest counts.
Inspect the cited setup and collaborators before treating a focused result as end-to-end evidence.

### Invariants And Boundaries

Preserve exact refusal, identity, and cleanup assertions rather than adding overlapping helper
cases. Coverage percentages are diagnostic and production CRAP 20 prompts review; neither implies
an obligation to restore removed cases. Full suites and whole-candidate review remain master-end
work. This source inspection does not claim a newly executed test or acceptance result.

### Todos

No additional implementation scope is opened by this memory reconciliation.

## Evidence

### Docs References

The repository has no configured Domain Documentation source. These claims concern its own test
fixtures and assertions, so the exact retained source is the direct evidence.

No external domain claim is required.

### Repo-Internal References

Each current definition below can be inspected in the exact source file. Historical references
to removed methods are superseded by this current inventory.

- Success uses log probe and never captures pane [1]
- An unwritable buffer reports undelivered and never presses enter [2]
- Unobservable pane blocks repaste [3]
- Dispatch retry submits visible same draft without repaste [4]
- Dispatch retry leaves unrelated codex draft pending [5]
- Dispatch retry does not submit historical matching marker [6]

### Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

No external evidence is needed for these assertions.
