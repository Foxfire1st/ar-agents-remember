# mcp/src/agents_remember/application/_review_answer_helpers.py

## Governing Overview

[Owning route overview](overview.md)

## Purpose

Hold the pure input, key and answer-policy helpers that `review_answer_preparation` composes, so the recorded-answer owner keeps its file-size budget without changing the questions it asks.

## Code Commentary

The helpers name what a recorded answer is a function of: the comparison's contract, listing, generation directory and object stores; the tree-view query key; the reads a record supplies; and the predicates that decide whether a tree view, a summary or a persisted tree may be kept. `_keepable_tree_view` rejects a tree answer with an unavailable-history side, and card-memory failure when the after knowledge side is available. `_tree_key` carries every query selector. `_expected_reads` compares caller-resolved byte and selection identities before an answer is kept. `_additions_kept` observes each object store as a kept success needs it.

No helper holds state or writes anything. `review_answer_preparation` binds them into its answer policies, its witness and its reuse store, so a reused answer and a fresh one come from the same call.

## Boundaries

The reuse rule these helpers serve lives with the owning `review_answer_preparation` route and its `RecordedReviewAnswers` owner; this module adds no record, policy or store of its own.

## Evidence

- The helpers resolve a recorded comparison's inputs, keys and answer predicates without state. [1]
