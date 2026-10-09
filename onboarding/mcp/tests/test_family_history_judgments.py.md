# mcp/tests/test_family_history_judgments.py

## Governing Overview

[mcp/tests/overview.md](./overview.md)

## Purpose

Pins MIK-R48: recorded family meaning judgments keep their curator-authored effect
and their writer-recorded own revision, and the publication population judges only
the rows the route publishes.

## Code Commentary

The module proves the rule end to end on real Git commits of fresh fixture
repositories built under `tmp_path`: the four effect
labels stored and read back whole, bad inputs refused with nothing written,
own-revision drift refused until the row is named again, the master landing shape
(a), the open-file refusal (b), the baseless validation pass (c) and the leaf
publication refusal (d), frozen-row preservation, later-attempt currentness, the
hand-closed way out and disposition-specific drift text.

## Evidence

- Each authored label is stored with the family revision and read back whole. [1]
- Bad inputs refuse with files, refs and index unchanged. [2]
- Master landings pass over closed legacy rows the base lacks. [3]
- Open unpublished rows are refused naming file, row and rule. [4]
- The leaf's own unlabelled changed row is refused, open or hand-closed. [5]
- Drift refuses until the current row is authored again. [6]
