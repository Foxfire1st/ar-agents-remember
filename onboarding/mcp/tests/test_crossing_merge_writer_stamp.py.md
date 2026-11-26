# mcp/tests/test_crossing_merge_writer_stamp.py

## Governing Overview

[Governing overview](overview.md)

## Purpose

Checks revision authorship, stripped-tie side selection, and stripped-equality review joining when a crossing selects one branch, resolves a stamp-only tie, combines non-conflicting meaning edits, or preserves a meaning conflict.

## Evidence

- Combined meaning receives the product's writer stamp. [1]
- A single side's meaning keeps that side's writer. [2]

- Incoming or own state-converted records that the other side never changed keep the changed side's bytes, and records absent at base prefer the sole state-form side over legacy or unstamped records before falling back to own. [3]
- Stamp-only ties pass stripped equality as `tied` so both sides' reviews join without a `crossingSelections` row on shared selection history or clear a prior peer exclusion, while differing edits to one meaning field stay conflicted without a writer stamp. [4]
