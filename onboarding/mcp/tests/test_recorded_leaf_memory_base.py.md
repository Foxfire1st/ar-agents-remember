# mcp/tests/test_recorded_leaf_memory_base.py

## Governing Overview

[Test overview](overview.md)

## Purpose

Exercise leaf memory comparisons over an untrailed merge, an unestablished recorded base and a format conversion.

## Code Commentary

The merge fixture brings two attributed lines together and asserts that the merge has no `Code-Commit` trailer. It records the merge as the leaf's memory base. Worklist, trace, writer, closeout, pair and live-review tests use its comparisons to distinguish inherited memory from leaf-authored changes.

The conversion fixture uses the recorded base's trailer or the code base to select the code revision for conversion. The test distinguishes mechanical conversion from authored card content and checks what the writer does when a persisted count disagrees.

The invalid-base cases exercise missing, unreadable and unrelated commits. The pair test uses an independent root with the same memory tree to check that ancestry binds to the judged commit.

## Relationships

The fixtures use local repositories. The checks call the same worklist, writer, gate and live-review entry points that consume the leaf contract.

## Evidence

- The fixture asserts two merge parents and an absent trailer, then passes the merge as the recorded base. [1]
- Converted base comparison rejects a mechanical-only card update and admits the authored card edit. [2]
- Missing, unreadable and unrelated inputs exercise the caller-specific responses. [3]
- Identical trees with unrelated commit ancestry do not share the pair gate's authority. [4]
