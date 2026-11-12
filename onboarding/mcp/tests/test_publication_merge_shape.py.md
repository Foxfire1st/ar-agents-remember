# mcp/tests/test_publication_merge_shape.py

## Governing Overview

[overview](overview.md)

## Purpose

The tests cover the finished-master chain proof's admission of history that no leaf landed directly: a pull-request merge that publishes one recorded leaf landing, the history a repository-default sync records on a master line, and the landing workflow a series reads from its memory work branch.

## Code Commentary

A merge is admitted by its shape when it has two parents, the first the step's start and the second the leaf's landed commit, and its tree equals the landed tree. A `--no-ff` merge of the landed commit passes `_require_admitted_step`. A merge that adds a file of its own is refused because it adds history beyond the exact leaf landing chain; a merge whose second parent is other work and an octopus merge are refused too. A hand merge of a recorded official position, whose parents are both admitted, is refused by `_require_admitted_merges` with the merge named and the remedy to take the commit off the master branch and make the change in a leaf.

A master line that merged the repository's default branch passes the chain proof when its sync log holds the repository-default entry naming the default line's tip; that tip's history, including a merge on the default branch, enters the step from the side. Without the entry the same commits are refused by name. With the entry, a default-branch commit merged past the recorded tip and a direct master commit are still refused, and the recorded tip's history is not among the refused commits. After a fast-forward default sync, a leaf that starts at the recorded source pair stands on the chain through `_require_empty_landings_on_chain`; the same entry without its source commits is refused.

A series contract has no memory worktree, so `_landing_workflow` reads `landing.workflow` from `system/settings.json` at the memory work branch; the case checks `pull-request` and `local`. On the master's own step with no authority range left, a merge at the tip is admitted by shape under the `local` workflow, and `_published_landing` returns the landed commit, or nothing when the second parent is not the end of a recorded leaf range.

## Relationships

The functions under test are in `mcp/src/agents_remember/worktrees/series_merge_admission.py`, apart from `_require_empty_landings_on_chain` in `mcp/src/agents_remember/worktrees/series_closeout.py`; a refusal is a `CloseoutQueueError`. The repositories are built with the `_git` helper of `test_master_chain_offenders.py`.

## Evidence

- A published pull-request merge of the landed commit is admitted. [1]
- A merge that no rule admits is refused with the merge named and the leaf remedy. [2]
- A merge with content of its own is refused as history beyond the landing chain. [3]
- A merge whose second parent is not the leaf landing is refused. [4]
- An octopus merge is refused. [5]
- The recorded default-line tip admits its history; without the record it is refused. [6]
- History past the recorded tip and a direct master commit are still refused. [7]
- A leaf starting at the recorded default source pair stands on the chain. [8]
- A series reads its landing workflow from its memory work branch. [9]
- On the real route a merge at the tip is admitted by shape and names its landing. [10]
